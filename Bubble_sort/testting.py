import pytest
from src.bubble_sort import BubbleSort, SortOrder

def test_basic_sort_ascending():
    sorter = BubbleSort()
    data = [3, 1, 4, 2]
    result = sorter.basic_bubble_sort(data)
    assert result == [1, 2, 3, 4]

def test_basic_sort_descending():
    sorter = BubbleSort()
    data = [3, 1, 4, 2]
    result = sorter.basic_bubble_sort(data, SortOrder.DESCENDING)
    assert result == [4, 3, 2, 1]

def test_optimized_sort_already_sorted():
    sorter = BubbleSort()
    data = [1, 2, 3, 4]
    result = sorter.optimized_bubble_sort(data)
    assert result == [1, 2, 3, 4]
    # Should have fewer comparisons than basic version
