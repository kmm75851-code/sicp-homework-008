import pytest
from text_analyzer import analyze, make_analyzer


class TestAnalyze:
    def test_all_keys(self):
        result = analyze("the cat sat on the mat the cat")
        assert set(result.keys()) == {
            'total_words', 'unique_words', 'word_counts',
            'most_common', 'longest_word', 'avg_word_length', 'appears_once'
        }

    def test_total_words(self):
        assert analyze("the cat sat on the mat the cat")['total_words'] == 8

    def test_unique_words(self):
        assert analyze("the cat sat on the mat the cat")['unique_words'] == 5

    def test_word_counts(self):
        result = analyze("the cat sat on the mat the cat")
        assert result['word_counts'] == {
            'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1
        }

    def test_most_common(self):
        assert analyze("the cat sat on the mat the cat")['most_common'] == 'the'

    def test_most_common_is_string(self):
        assert isinstance(analyze("hello hello world")['most_common'], str)

    def test_longest_word(self):
        result = analyze("the cat sat")
        assert result['longest_word'] == 'cat'

    def test_longest_word_alphabetical_tiebreak(self):
        result = analyze("cat bat sat")
        assert result['longest_word'] == 'bat'

    def test_avg_word_length(self):
        result = analyze("the cat sat on the mat the cat")
        assert result['avg_word_length'] == round((3+3+3+2+3)/5, 2)

    def test_appears_once(self):
        result = analyze("the cat sat on the mat the cat")
        assert result['appears_once'] == {'sat', 'on', 'mat'}

    def test_case_insensitive(self):
        result = analyze("Hello hello")
        assert result['total_words'] == 2
        assert result['unique_words'] == 1

    def test_single_word(self):
        result = analyze("hello")
        assert result['total_words'] == 1
        assert result['unique_words'] == 1
        assert result['most_common'] == 'hello'
        assert result['appears_once'] == {'hello'}


class TestMakeAnalyzer:
    def test_basic(self):
        add, stats = make_analyzer()
        add("the cat sat")
        result = stats()
        assert result['total_words'] == 3

    def test_accumulates(self):
        add, stats = make_analyzer()
        add("the cat sat")
        add("the dog ran")
        result = stats()
        assert result['total_words'] == 6

    def test_word_counts_accumulated(self):
        add, stats = make_analyzer()
        add("hello world")
        add("hello python")
        result = stats()
        assert result['word_counts']['hello'] == 2

    def test_independent(self):
        add1, stats1 = make_analyzer()
        add2, stats2 = make_analyzer()
        add1("hello world hello")
        result = stats2()
        assert result['total_words'] == 0 or result == analyze("")
