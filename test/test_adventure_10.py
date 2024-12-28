import pytest
from pylint.lint import Run
import subprocess
import adventure

def test_file_exists():
    """Test that adventure.py exists."""
    try:
        with open("adventure.py", "r") as f:
            assert True
    except FileNotFoundError:
        assert False, "adventure.py not found"
