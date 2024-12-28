import pytest
from pylint.lint import Run
import subprocess
import adventure

# Test Cases for Week 1 Adventure Game


def test_header_comment():
    """Test for a header comment with name and date."""
    with open("adventure.py", "r") as f:
        lines = f.readlines()
    
    header = lines[:2]  # Check the first two lines for the header
    assert any("#" in line for line in header), "Header comment is missing"
    assert any(line.strip() != "#" for line in header), "Header comment should contain text"
