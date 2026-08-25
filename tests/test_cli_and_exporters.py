"""Unit tests for CLI commands and formatters/exporters in DPX-Mojo."""

from __future__ import annotations

from typer.testing import CliRunner
from pattern_detector.adapters.inbound.cli.main import app
from pattern_detector.adapters.outbound.persistence import (
    HtmlReportFormatter,
    JsonReportFormatter,
    LlmReportFormatter,
    MarkdownReportFormatter,
    SarifReportFormatter,
)
from pattern_detector.domain.detection import Detection, DetectionReport
from pattern_detector.domain.value_objects import (
    Confidence,
    Evidence,
    PatternCategory,
    PatternType,
    SourceLocation,
)

runner = CliRunner()


def _create_sample_report() -> DetectionReport:
    loc = SourceLocation(file_path="src/kernel.mojo", line=15, column=1)
    ev = Evidence(rule_code="HARDWARE_SIMD_VECTORIZATION", description="SIMD vector register operation", weight=0.95, location=loc)
    det = Detection(
        pattern_type=PatternType.SIMD_VECTORIZATION_KERNEL,
        pattern_category=PatternCategory.SIMD_HARDWARE_ACCELERATION,
        target_name="vector_matmul",
        target_kind="fn",
        confidence=Confidence(score=0.95, evidences=[ev]),
        primary_location=loc,
        evidences=[ev],
    )
    return DetectionReport(
        project_path="src",
        scanned_files_count=2,
        detections=[det],
        elapsed_seconds=0.015,
    )


def test_cli_rules_command() -> None:
    result = runner.invoke(app, ["rules"])
    assert result.exit_code == 0
    assert "DPX-Mojo" in result.stdout
    assert "MOJO_IDIOMATIC" in result.stdout


def test_cli_info_command() -> None:
    result = runner.invoke(app, ["info", "simd_vectorization_kernel"])
    assert result.exit_code == 0
    assert "SIMD Vectorization" in result.stdout


def test_exporters_format() -> None:
    report = _create_sample_report()

    html_out = HtmlReportFormatter().format(report)
    assert "<!DOCTYPE html>" in html_out
    assert "Pattern Scanner Report" in html_out
    assert "vector_matmul" in html_out
    assert "Copy AI Context Prompt" in html_out

    md_out = MarkdownReportFormatter().format(report)
    assert "# 🔥 DPX-Mojo" in md_out
    assert "vector_matmul" in md_out

    json_out = JsonReportFormatter().format(report)
    assert '"total_detections_count": 1' in json_out

    sarif_out = SarifReportFormatter().format(report)
    assert '"$schema"' in sarif_out

    llm_out = LlmReportFormatter().format_scan_report(report)
    assert '<codebase_architecture_analysis language="mojo">' in llm_out
