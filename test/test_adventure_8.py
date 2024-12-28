import pytest
from pylint.lint import Run
import subprocess
import adventure

# Test Cases for Week 1 Adventure Game

def test_comments():
    """Test for the presence of comments."""
    with open("adventure.py", "r") as f:
        code = f.read()
    assert "#" in code, "Code should contain comments"
