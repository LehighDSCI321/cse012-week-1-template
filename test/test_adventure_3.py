import pytest
from pylint.lint import Run
import subprocess
import adventure

# Test Cases for Week 1 Adventure Game
def test_pylint_style():
    """Test for Pylint style suggestions (score below 7)."""
    result = Run(['adventure.py', '--disable=E0401,C0114,C0115,C0116'], exit=False)
    score = result.linter.stats.global_note
    assert score >= 7.0, f"Pylint style score is too low: {score}"
