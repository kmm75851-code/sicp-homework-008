import pytest
from dicts import (
    word_count, group_by_length, invert_dict,
    merge_dicts, most_common, two_sum,
    char_frequency, index_builder
)


class TestWordCount:
    def test_basic(self):
        assert word_count("the cat sat on the mat") == {
            'the': 2, 'cat': 1, 'sat': 1, 'on': 1, 'mat': 1
        }

    def test_case_insensitive(self):
        assert word_count("Hello hello HELLO") == {'hello': 3}

    def test_empty(self):
        assert word_count("") == {}

    def test_single(self):
        assert word_count("hello") == {'hello': 1}


class TestGroupByLength:
    def test_basic(self):
        result = group_by_length(["hi", "hello", "ok", "world", "yes"])
        assert result[2] == ['hi', 'ok']
        assert result[5] == ['hello', 'world']
        assert result[3] == ['yes']

    def test_empty(self):
        assert group_by_length([]) == {}

    def test_order_preserved(self):
        result = group_by_length(["cat", "dog", "ant"])
        assert result[3] == ['cat', 'dog', 'ant']


class TestInvertDict:
    def test_unique_values(self):
        result = invert_dict({'x': 10, 'y': 20})
        assert result == {10: ['x'], 20: ['y']}

    def test_duplicate_values(self):
        result = invert_dict({'a': 1, 'b': 2, 'c': 1})
        assert set(result[1]) == {'a', 'c'}
        assert result[2] == ['b']

    def test_empty(self):
        assert invert_dict({}) == {}


class TestMergeDicts:
    def test_basic(self):
        result = merge_dicts({'a': 1}, {'b': 2})
        assert result == {'a': 1, 'b': 2}

    def test_last_wins(self):
        result = merge_dicts({'a': 1}, {'b': 2}, {'a': 99})
        assert result['a'] == 99
        assert result['b'] == 2

    def test_single(self):
        assert merge_dicts({'x': 1}) == {'x': 1}

    def test_empty(self):
        assert merge_dicts() == {}

    def test_does_not_mutate(self):
        d = {'a': 1}
        merge_dicts(d, {'b': 2})
        assert d == {'a': 1}


class TestMostCommon:
    def test_basic(self):
        result = most_common("the cat sat on the mat the cat", 2)
        assert result == ['the', 'cat']

    def test_n_larger_than_words(self):
        result = most_common("hello", 5)
        assert result == ['hello']

    def test_empty(self):
        result = most_common("", 3)
        assert result == []

    def test_single_word(self):
        result = most_common("go go go stop", 1)
        assert result == ['go']


class TestTwoSum:
    def test_basic(self):
        assert two_sum([2, 7, 11, 15], 9) == (0, 1)

    def test_basic2(self):
        assert two_sum([3, 2, 4], 6) == (1, 2)

    def test_order(self):
        i, j = two_sum([1, 5, 3, 7], 8)
        assert i < j
        assert i == 1 and j == 2

    def test_adjacent(self):
        assert two_sum([1, 2], 3) == (0, 1)


class TestCharFrequency:
    def test_basic(self):
        assert char_frequency("hello") == {'h': 1, 'e': 1, 'l': 2, 'o': 1}

    def test_empty(self):
        assert char_frequency("") == {}

    def test_repeated(self):
        assert char_frequency("aaa") == {'a': 3}

    def test_spaces(self):
        result = char_frequency("a b")
        assert result[' '] == 1


class TestIndexBuilder:
    def test_basic(self):
        docs = {1: "the cat sat", 2: "the cat on the mat", 3: "the dog sat"}
        result = index_builder(docs)
        assert result['the'] == {1, 2, 3}
        assert result['cat'] == {1, 2}
        assert result['sat'] == {1, 3}
        assert result['dog'] == {3}

    def test_single_doc(self):
        result = index_builder({1: "hello world"})
        assert result['hello'] == {1}
        assert result['world'] == {1}

    def test_values_are_sets(self):
        result = index_builder({1: "a", 2: "a"})
        assert isinstance(result['a'], set)
        assert result['a'] == {1, 2}
