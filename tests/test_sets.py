import pytest
from sets import (
    unique_words, common_words, only_in_first,
    dedup_preserve_order, anagram_groups, set_stats
)


class TestUniqueWords:
    def test_basic(self):
        assert unique_words("the cat sat on the mat") == {'the', 'cat', 'sat', 'on', 'mat'}

    def test_case_insensitive(self):
        assert unique_words("Hello hello HELLO") == {'hello'}

    def test_empty(self):
        assert unique_words("") == set()

    def test_returns_set(self):
        assert isinstance(unique_words("hello world"), set)


class TestCommonWords:
    def test_basic(self):
        assert common_words("the cat sat", "the dog sat") == {'the', 'sat'}

    def test_no_common(self):
        assert common_words("hello world", "foo bar") == set()

    def test_identical(self):
        assert common_words("hi there", "hi there") == {'hi', 'there'}


class TestOnlyInFirst:
    def test_basic(self):
        result = only_in_first("the cat sat on the mat", "the dog sat")
        assert result == {'cat', 'on', 'mat'}

    def test_nothing_unique(self):
        assert only_in_first("hi", "hi there") == set()

    def test_all_unique(self):
        assert only_in_first("hello world", "foo bar") == {'hello', 'world'}


class TestDedupPreserveOrder:
    def test_basic(self):
        assert dedup_preserve_order([3, 1, 2, 1, 3, 4]) == [3, 1, 2, 4]

    def test_strings(self):
        assert dedup_preserve_order(['a', 'b', 'a', 'c']) == ['a', 'b', 'c']

    def test_empty(self):
        assert dedup_preserve_order([]) == []

    def test_no_duplicates(self):
        assert dedup_preserve_order([1, 2, 3]) == [1, 2, 3]

    def test_all_same(self):
        assert dedup_preserve_order([5, 5, 5]) == [5]

    def test_does_not_mutate(self):
        items = [1, 2, 1]
        dedup_preserve_order(items)
        assert items == [1, 2, 1]


class TestAnagramGroups:
    def test_basic(self):
        words = ["eat", "tea", "tan", "ate", "nat", "bat"]
        result = anagram_groups(words)
        result_sets = [set(g) for g in result]
        assert {'ate', 'eat', 'tea'} in result_sets
        assert {'nat', 'tan'} in result_sets
        assert {'bat'} in result_sets

    def test_groups_sorted_internally(self):
        result = anagram_groups(["eat", "tea", "ate"])
        assert result == [['ate', 'eat', 'tea']]

    def test_no_anagrams(self):
        result = anagram_groups(["abc", "xyz"])
        result_sets = [set(g) for g in result]
        assert {'abc'} in result_sets
        assert {'xyz'} in result_sets

    def test_empty(self):
        assert anagram_groups([]) == []


class TestSetStats:
    def test_basic(self):
        result = set_stats([1, 2, 2, 3, 3, 3, 4])
        assert result['unique_count'] == 4
        assert result['duplicates'] == {2, 3}
        assert result['unique_only'] == {1, 4}

    def test_no_duplicates(self):
        result = set_stats([1, 2, 3])
        assert result['unique_count'] == 3
        assert result['duplicates'] == set()
        assert result['unique_only'] == {1, 2, 3}

    def test_all_same(self):
        result = set_stats([5, 5, 5])
        assert result['unique_count'] == 1
        assert result['duplicates'] == {5}
        assert result['unique_only'] == set()

    def test_empty(self):
        result = set_stats([])
        assert result['unique_count'] == 0
        assert result['duplicates'] == set()
        assert result['unique_only'] == set()
