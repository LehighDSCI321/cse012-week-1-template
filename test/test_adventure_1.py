import pytest
from pylint.lint import Run
import subprocess
import adventure

# Test Cases for Week 1 Adventure Game

def test_pylint_warnings():
    """Test for Pylint warnings (score below 5)."""
    result = Run(['adventure.py', '--disable=E0401,C0114,C0115,C0116'], exit=False)
    score = result.linter.stats.global_note
    assert score >= 5.0, f"Pylint warning score is too low: {score}"
