import pytest
from pylint.lint import Run
import subprocess
import adventure

# Test Cases for Week 1 Adventure Game

def test_arithmetic_operations():
    """Test for correct arithmetic operations."""
    original_health = 100  # Assuming initial value
    original_strength = 75.5 # Assuming initial value
    expected_health = original_health - 20
    expected_strength = original_strength + 15.5
    assert adventure.health == expected_health, "health was not updated correctly"
    assert adventure.strength == expected_strength, "strength was not updated correctly"
