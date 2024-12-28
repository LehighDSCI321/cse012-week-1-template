import pytest
from pylint.lint import Run
import subprocess
import adventure

# Test Cases for Week 1 Adventure Game

def test_string_manipulation():
    """Test for correct string manipulation in intro."""
    assert isinstance(adventure.intro, str), "intro should be a string"
    assert adventure.character_name in adventure.intro, "intro should contain character_name"
