"""Domain CodeModel entities representing Mojo AST and structural semantics."""

from __future__ import annotations

from dataclasses import dataclass, field
from pattern_detector.domain.value_objects import SourceLocation


@dataclass
class MojoField:
    """Struct member field in Mojo."""

    name: str
    type_name: str
    is_var: bool = True
    location: SourceLocation | None = None
    raw_text: str = ""


@dataclass
class MojoParam:
    """Function/Method parameter with ownership convention."""

    name: str
    type_name: str
    convention: str = "borrowed"  # "borrowed", "inout", "owned", "ref"
    default_val: str | None = None


@dataclass
class MojoFunction:
    """Function or method definition in Mojo ('fn' or 'def')."""

    name: str
    kind: str = "fn"  # "fn" or "def"
    signature: str = ""
    is_method: bool = False
    parameters: list[MojoParam] = field(default_factory=list)
    comptime_params: list[str] = field(default_factory=list)  # [type: DType, simd_width: Int]
    return_type: str = "None"
    decorators: list[str] = field(default_factory=list)
    body: str = ""
    branch_count: int = 1
    has_transfer_move: bool = False
    location: SourceLocation | None = None
    raw_text: str = ""

    @property
    def is_constructor(self) -> bool:
        return self.name in ("__init__", "__copyinit__", "__moveinit__")

    @property
    def is_destructor(self) -> bool:
        return self.name == "__del__"


@dataclass
class MojoStruct:
    """Struct definition in Mojo with value semantics and parameters."""

    name: str
    comptime_params: list[str] = field(default_factory=list)  # [DType, Int]
    traits: list[str] = field(default_factory=list)
    decorators: list[str] = field(default_factory=list)
    fields: list[MojoField] = field(default_factory=list)
    methods: list[MojoFunction] = field(default_factory=list)
    line_count: int = 1
    location: SourceLocation | None = None
    raw_text: str = ""

    @property
    def has_value_decorator(self) -> bool:
        return any("@value" in dec for dec in self.decorators)

    @property
    def is_register_passable(self) -> bool:
        return any("@register_passable" in dec for dec in self.decorators)

    @property
    def is_singleton(self) -> bool:
        return len(self.fields) == 0 or "Singleton" in self.name or "Config" in self.name


@dataclass
class MojoTrait:
    """Trait interface definition in Mojo."""

    name: str
    parent_traits: list[str] = field(default_factory=list)
    methods: list[MojoFunction] = field(default_factory=list)
    location: SourceLocation | None = None
    raw_text: str = ""


@dataclass
class MojoAlias:
    """Compile-time alias declaration in Mojo."""

    name: str
    target_expr: str
    location: SourceLocation | None = None
    raw_text: str = ""


@dataclass
class MojoFile:
    """Parsed single Mojo source file (.mojo or .🔥)."""

    file_path: str
    raw_content: str
    lines: list[str] = field(default_factory=list)
    structs: list[MojoStruct] = field(default_factory=list)
    traits: list[MojoTrait] = field(default_factory=list)
    functions: list[MojoFunction] = field(default_factory=list)
    aliases: list[MojoAlias] = field(default_factory=list)


@dataclass
class CodeModel:
    """Aggregated structural model of a scanned Mojo codebase."""

    target_path: str = ""
    files: list[MojoFile] = field(default_factory=list)

    @property
    def all_structs(self) -> list[MojoStruct]:
        return [s for f in self.files for s in f.structs]

    @property
    def all_traits(self) -> list[MojoTrait]:
        return [t for f in self.files for t in f.traits]

    @property
    def all_functions(self) -> list[MojoFunction]:
        funcs = [fn for f in self.files for fn in f.functions]
        for s in self.all_structs:
            funcs.extend(s.methods)
        return funcs

    @property
    def all_aliases(self) -> list[MojoAlias]:
        return [a for f in self.files for a in f.aliases]
