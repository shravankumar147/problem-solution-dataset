import pytest
import sys
import os

sys.path.append(os.path.dirname(__file__))  # Ensure the test file imports from the correct directory

from solution import reverse_string

def test_reverse_string():
    # Test cases to validate the solution
    assert reverse_string("hello") == "olleh"
    assert reverse_string("world") == "dlrow"
    assert reverse_string("abc") == "cba"
    assert reverse_string("") == ""  # Edge case: empty string
    assert reverse_string("a") == "a"  # Edge case: single character
