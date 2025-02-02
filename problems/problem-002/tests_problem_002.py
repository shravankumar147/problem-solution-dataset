import pytest
from solution import reverse_string

def test_reverse_string():
    # Test cases to validate the solution
    assert reverse_string("hello") == "olleh"
    assert reverse_string("world") == "dlrow"
    assert reverse_string("abc") == "cba"
    assert reverse_string("") == ""  # Edge case: empty string
    assert reverse_string("a") == "a"  # Edge case: single character
