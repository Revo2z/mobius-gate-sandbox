from sandbox.text import word_count


def test_word_count_counts_space_separated_words():
    assert word_count("le chat dort") == 3


def test_word_count_of_empty_text_is_zero():
    assert word_count("") == 0
