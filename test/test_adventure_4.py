import pytest
from pylint.lint import Run
import subprocess
import adventure

# Test Cases for Week 1 Adventure Game

def test_variable_declarations():
    """Test for correct variable declarations."""
    assert isinstance(adventure.health, int), "health should be an integer"
    assert adventure.health == 100, "health should be initialized to 100"
    assert isinstance(adventure.strength, float), "strength should be a float"
    assert adventure.strength == 75.5, "strength should be initialized to 75.5"
    assert isinstance(adventure.character_name, str), "character_name should be a string"
    assert isinstance(adventure.has_sword, bool), "has_sword should be a boolean"
    assert adventure.has_sword, "has_sword should be True"
