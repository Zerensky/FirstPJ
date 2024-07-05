# Здесь мной был создан файл test_list_comparator.py для тестирования нашего класса.

import pytest
from list_comparator import ListComparator
python -m venv myenv

def test_empty_lists():
    comparator = ListComparator([], [])
    assert comparator.compare_averages() == "Средние значения равны"

def test_first_list_greater():
    comparator = ListComparator([1, 2, 3], [1, 1, 1])
    assert comparator.compare_averages() == "Первый список имеет большее среднее значение"

def test_second_list_greater():
    comparator = ListComparator([1, 1, 1], [1, 2, 3])
    assert comparator.compare_averages() == "Второй список имеет большее среднее значение"

def test_equal_averages():
    comparator = ListComparator([1, 2, 3], [3, 2, 1])
    assert comparator.compare_averages() == "Средние значения равны"

def test_with_negative_numbers():
    comparator = ListComparator([-1, -2, -3], [-3, -2, -1])
    assert comparator.compare_averages() == "Средние значения равны"
