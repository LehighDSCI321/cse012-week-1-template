import pytest
from pylint.lint import Run
import subprocess
import adventure

# Test Cases for Week 1 Adventure Game
def test_pylint_errors():
    """Test for Pylint errors (any errors)."""
    process = subprocess.run(['pylint', 'adventure.py', '--disable=E0401,C0114,C0115,C0116'], capture_output=True, text=True)
    assert "error" not in process.stdout, f"Pylint errors found:\n{process.stdout}"
