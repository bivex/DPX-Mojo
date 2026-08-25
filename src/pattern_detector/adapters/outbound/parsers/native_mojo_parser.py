"""High-speed native parser adapter for Mojo source code (.mojo, .🔥)."""

from __future__ import annotations

import re
from pattern_detector.domain.code_model import (
    CodeModel,
    MojoAlias,
    MojoField,
    MojoFile,
    MojoFunction,
    MojoParam,
    MojoStruct,
    MojoTrait,
)
from pattern_detector.domain.value_objects import SourceLocation
from pattern_detector.ports.outbound import ParserPort


class NativeMojoParserAdapter(ParserPort):
    """Linear, robust single-pass parser extracting Mojo AST semantics."""

    STRUCT_START = re.compile(
        r"^\s*struct\s+(?P<name>[A-Za-z0-9_]+)(?:\[(?P<params>[^\]]+)\])?(?:\((?P<traits>[^)]+)\))?\s*:"
    )
    TRAIT_START = re.compile(
        r"^\s*trait\s+(?P<name>[A-Za-z0-9_]+)(?:\((?P<parents>[^)]+)\))?\s*:"
    )
    ALIAS_PATTERN = re.compile(
        r"^\s*alias\s+(?P<name>[A-Za-z0-9_]+)\s*=\s*(?P<expr>.+)$"
    )
    FUNC_START = re.compile(
        r"^\s*(?P<kind>fn|def)\s+(?P<name>[A-Za-z0-9_]+)(?:\[(?P<comptime_params>[^\]]+)\])?\s*\((?P<params>.*)\)(?:\s*(?:->|raises\s+->)\s*(?P<ret>[A-Za-z0-9_{}\[\],.\s]+))?\s*(?:raises)?\s*:"
    )
    FIELD_PATTERN = re.compile(
        r"^\s*(?P<kind>var|let)\s+(?P<name>[A-Za-z0-9_]+)\s*:\s*(?P<type>[A-Za-z0-9_{}\[\],.\s]+)$"
    )
    DECORATOR_PATTERN = re.compile(r"^\s*(@[a-zA-Z0-9_]+(?:\([^)]*\))?)")
    BRANCH_KEYWORDS = re.compile(r"\b(if\s+|elif\s+|for\s+|while\s+|except\b|and\b|or\b)")
    TRANSFER_PATTERN = re.compile(r"\b[a-zA-Z_]\w*\^")

    def _parse_params(self, params_str: str) -> list[MojoParam]:
        if not params_str.strip():
            return []

        params: list[MojoParam] = []
        for raw_p in params_str.split(","):
            p_clean = raw_p.strip()
            if not p_clean or p_clean in ("self", "mut self", "inout self", "borrowed self", "owned self"):
                continue

            convention = "borrowed"
            for conv in ("inout", "owned", "borrowed", "ref", "var", "val"):
                if p_clean.startswith(f"{conv} "):
                    convention = conv
                    p_clean = p_clean[len(conv) + 1:].strip()
                    break

            if ":" in p_clean:
                p_name, p_type = p_clean.split(":", 1)
                default_val = None
                if "=" in p_type:
                    p_type, default_val = p_type.split("=", 1)
                params.append(
                    MojoParam(
                        name=p_name.strip(),
                        type_name=p_type.strip(),
                        convention=convention,
                        default_val=default_val.strip() if default_val else None,
                    )
                )
            else:
                params.append(MojoParam(name=p_clean, type_name="Any", convention=convention))

        return params

    def parse_file(self, file_path: str, content: str) -> MojoFile:
        lines = content.splitlines()
        file_obj = MojoFile(file_path=file_path, raw_content=content, lines=lines)

        current_struct: MojoStruct | None = None
        current_trait: MojoTrait | None = None
        current_function: MojoFunction | None = None
        current_func_body: list[str] = []
        current_decorators: list[str] = []

        struct_indent = -1
        trait_indent = -1
        func_indent = -1

        for line_idx, raw_line in enumerate(lines, 1):
            trimmed = raw_line.strip()
            indent = len(raw_line) - len(raw_line.lstrip())

            # Skip comments and empty lines
            if trimmed.startswith("#") or not trimmed:
                continue

            # Check Decorator
            dec_m = self.DECORATOR_PATTERN.match(trimmed)
            if dec_m:
                if current_function and indent > func_indent:
                    current_func_body.append(raw_line)
                    continue
                current_decorators.append(dec_m.group(1))
                continue

            # Check Alias
            alias_m = self.ALIAS_PATTERN.match(trimmed)
            if alias_m:
                file_obj.aliases.append(
                    MojoAlias(
                        name=alias_m.group("name"),
                        target_expr=alias_m.group("expr").strip(),
                        location=SourceLocation(file_path=file_path, line=line_idx, column=1),
                        raw_text=raw_line,
                    )
                )
                current_decorators = []
                continue

            # Check Struct End / Scope Exit
            if current_struct and indent <= struct_indent and not trimmed.startswith("@"):
                if current_function:
                    current_function.body = "\n".join(current_func_body)
                    current_struct.methods.append(current_function)
                    current_function = None
                    current_func_body = []
                if current_struct.location:
                    current_struct.line_count = line_idx - current_struct.location.line
                file_obj.structs.append(current_struct)
                current_struct = None
                struct_indent = -1

            # Check Trait End / Scope Exit
            if current_trait and indent <= trait_indent and not trimmed.startswith("@"):
                file_obj.traits.append(current_trait)
                current_trait = None
                trait_indent = -1

            # Check Function End (top-level)
            if current_function and not current_struct and indent <= func_indent and not trimmed.startswith("@"):
                current_function.body = "\n".join(current_func_body)
                file_obj.functions.append(current_function)
                current_function = None
                current_func_body = []
                func_indent = -1

            # Check Struct Start
            struct_m = self.STRUCT_START.match(trimmed)
            if struct_m and not current_struct:
                name = struct_m.group("name")
                params_str = struct_m.group("params") or ""
                traits_str = struct_m.group("traits") or ""

                comptime_params = [p.strip() for p in params_str.split(",") if p.strip()]
                traits = [t.strip() for t in traits_str.split(",") if t.strip()]

                current_struct = MojoStruct(
                    name=name,
                    comptime_params=comptime_params,
                    traits=traits,
                    decorators=list(current_decorators),
                    location=SourceLocation(file_path=file_path, line=line_idx, column=1),
                    raw_text=raw_line,
                )
                current_decorators = []
                struct_indent = indent
                continue

            # Check Trait Start
            trait_m = self.TRAIT_START.match(trimmed)
            if trait_m and not current_trait and not current_struct:
                name = trait_m.group("name")
                parents_str = trait_m.group("parents") or ""
                parents = [p.strip() for p in parents_str.split(",") if p.strip()]

                current_trait = MojoTrait(
                    name=name,
                    parent_traits=parents,
                    location=SourceLocation(file_path=file_path, line=line_idx, column=1),
                    raw_text=raw_line,
                )
                current_decorators = []
                trait_indent = indent
                continue

            # Check Struct Fields
            if current_struct and not current_function:
                field_m = self.FIELD_PATTERN.match(trimmed)
                if field_m:
                    current_struct.fields.append(
                        MojoField(
                            name=field_m.group("name"),
                            type_name=field_m.group("type").strip(),
                            is_var=(field_m.group("kind") == "var"),
                            location=SourceLocation(file_path=file_path, line=line_idx, column=1),
                            raw_text=raw_line,
                        )
                    )
                    continue

            # Check Function Start
            fn_m = self.FUNC_START.match(trimmed)
            if fn_m:
                if current_function:
                    current_function.body = "\n".join(current_func_body)
                    if current_struct:
                        current_struct.methods.append(current_function)
                    else:
                        file_obj.functions.append(current_function)
                    current_function = None
                    current_func_body = []

                kind = fn_m.group("kind")
                f_name = fn_m.group("name")
                comptime_params_str = fn_m.group("comptime_params") or ""
                params_str = fn_m.group("params") or ""
                ret_t = (fn_m.group("ret") or "None").strip()

                comptime_params = [p.strip() for p in comptime_params_str.split(",") if p.strip()]
                parsed_params = self._parse_params(params_str)

                fn_obj = MojoFunction(
                    name=f_name,
                    kind=kind,
                    signature=trimmed,
                    is_method=bool(current_struct),
                    parameters=parsed_params,
                    comptime_params=comptime_params,
                    return_type=ret_t,
                    decorators=list(current_decorators),
                    location=SourceLocation(file_path=file_path, line=line_idx, column=1),
                    raw_text=raw_line,
                )
                current_decorators = []

                if current_trait:
                    current_trait.methods.append(fn_obj)
                    continue

                current_function = fn_obj
                func_indent = indent
                current_func_body = [raw_line]
                continue

            # Accumulate Function Body
            if current_function:
                current_func_body.append(raw_line)
                current_function.branch_count += len(self.BRANCH_KEYWORDS.findall(raw_line))
                if self.TRANSFER_PATTERN.search(raw_line):
                    current_function.has_transfer_move = True

        # Flush remaining blocks at EOF
        if current_function:
            current_function.body = "\n".join(current_func_body)
            if current_struct:
                current_struct.methods.append(current_function)
            else:
                file_obj.functions.append(current_function)

        if current_struct:
            if current_struct.location:
                current_struct.line_count = len(lines) - current_struct.location.line + 1
            file_obj.structs.append(current_struct)

        if current_trait:
            file_obj.traits.append(current_trait)

        return file_obj

    def parse_codebase(self, files: list[tuple[str, str]], target_path: str = "") -> CodeModel:
        model = CodeModel(target_path=target_path)
        for fpath, content in files:
            mojo_file = self.parse_file(fpath, content)
            model.files.append(mojo_file)
        return model
