import pytest

def count_words(lines):
    return [len(line.split()) for line in lines]

def test_count_words():
    lines = ["Hello world", "This is a test", "Python is awesome"]
    expected = [2, 4, 3]
    assert count_words(lines) == expected

def test_count_words_empty():
    lines = []
    expected = []
    assert count_words(lines) == expected

def test_count_words_single():
    lines = ["Hello"]
    expected = [1]
    assert count_words(lines) == expected

def test_count_words_multiple_spaces():
    lines = ["Hello   world"]
    expected = [2]
    assert count_words(lines) == expected
