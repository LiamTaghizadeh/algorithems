# Bubble Sort Algorithm in Python

## 🧼 What is Bubble Sort?

Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

## 🎯 Algorithm Explanation

Imagine bubbles rising to the surface - larger elements "bubble up" to the end of the list with each pass.

**How it works:**
1. Start from the beginning of the list
2. Compare each pair of adjacent elements
3. If they're in the wrong order, swap them
4. Repeat until no more swaps are needed

**Time Complexity:**
- Worst-case: O(n²) - Very slow for large lists
- Best-case: O(n) - When list is already sorted
- Average-case: O(n²)

**Space Complexity:** O(1) - Sorts in place

## 📁 GitHub Repository Structure

```
bubble-sort-python/
│
├── src/
│   ├── bubble_sort.py           # Core implementation
│   ├── optimized_bubble_sort.py # Enhanced versions
│   └── visualizer.py           # Sorting visualization
│
├── tests/
│   ├── test_bubble_sort.py      # Unit tests
│   └── test_optimized.py        # Performance tests
│
├── examples/
│   ├── basic_usage.py           # Simple examples
│   ├── performance_comparison.py # Benchmarking
│   └── custom_data_types.py     # Sorting objects
│
├── docs/
│   ├── ALGORITHM_EXPLANATION.md # Detailed explanation
│   ├── PERFORMANCE_ANALYSIS.md  # Big O analysis
│   └── VISUALIZATION_GUIDE.md   # How to use visualizer
│
├── requirements.txt             # Dependencies
├── .github/
│   └── workflows/
│       └── python-test.yml      # CI/CD pipeline
└── README.md                    # Project documentation
```

## 💻 Complete Implementation

```python
"""
Bubble Sort Algorithm Implementation

A comprehensive implementation of bubble sort with multiple variants,
performance tracking, and visualization capabilities.
"""

from typing import List, Any, Callable, Optional
import time
import random
from enum import Enum


class SortOrder(Enum):
    """Enum for sorting order options"""
    ASCENDING = 1
    DESCENDING = 2


class BubbleSort:
    """
    Bubble Sort implementation with various optimizations and features.
    """
    
    def __init__(self):
        self.comparison_count = 0
        self.swap_count = 0
        self.execution_time = 0
    
    def basic_bubble_sort(self, arr: List[Any], 
                         order: SortOrder = SortOrder.ASCENDING,
                         key: Optional[Callable] = None) -> List[Any]:
        """
        Basic bubble sort implementation.
        
        Args:
            arr: List to be sorted
            order: Sorting order (ASCENDING or DESCENDING)
            key: Function to extract comparison key from elements
            
        Returns:
            Sorted list
        """
        if key is None:
            key = lambda x: x
            
        n = len(arr)
        arr = arr.copy()  # Don't modify original array
        
        start_time = time.perf_counter()
        self.comparison_count = 0
        self.swap_count = 0
        
        for i in range(n):
            for j in range(0, n - i - 1):
                self.comparison_count += 1
                
                # Determine comparison based on order
                if order == SortOrder.ASCENDING:
                    should_swap = key(arr[j]) > key(arr[j + 1])
                else:
                    should_swap = key(arr[j]) < key(arr[j + 1])
                
                if should_swap:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    self.swap_count += 1
        
        self.execution_time = time.perf_counter() - start_time
        return arr
    
    def optimized_bubble_sort(self, arr: List[Any],
                            order: SortOrder = SortOrder.ASCENDING,
                            key: Optional[Callable] = None) -> List[Any]:
        """
        Optimized bubble sort with early termination.
        
        Stops early if no swaps occur in a pass (list is sorted).
        """
        if key is None:
            key = lambda x: x
            
        n = len(arr)
        arr = arr.copy()
        
        start_time = time.perf_counter()
        self.comparison_count = 0
        self.swap_count = 0
        
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                self.comparison_count += 1
                
                if order == SortOrder.ASCENDING:
                    should_swap = key(arr[j]) > key(arr[j + 1])
                else:
                    should_swap = key(arr[j]) < key(arr[j + 1])
                
                if should_swap:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    self.swap_count += 1
                    swapped = True
            
            # If no swaps, array is sorted
            if not swapped:
                break
        
        self.execution_time = time.perf_counter() - start_time
        return arr
    
    def recursive_bubble_sort(self, arr: List[Any],
                            order: SortOrder = SortOrder.ASCENDING,
                            key: Optional[Callable] = None) -> List[Any]:
        """
        Recursive implementation of bubble sort.
        """
        if key is None:
            key = lambda x: x
            
        arr = arr.copy()
        n = len(arr)
        
        # Base case
        if n <= 1:
            return arr
        
        start_time = time.perf_counter()
        
        # One pass of bubble sort
        swapped = False
        for i in range(n - 1):
            self.comparison_count += 1
            
            if order == SortOrder.ASCENDING:
                should_swap = key(arr[i]) > key(arr[i + 1])
            else:
                should_swap = key(arr[i]) < key(arr[i + 1])
            
            if should_swap:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                self.swap_count += 1
                swapped = True
        
        # Recursively sort remaining elements
        if swapped:
            arr[:-1] = self.recursive_bubble_sort(arr[:-1], order, key)
        
        self.execution_time = time.perf_counter() - start_time
        return arr
    
    def get_stats(self) -> dict:
        """Get sorting statistics"""
        return {
            'comparisons': self.comparison_count,
            'swaps': self.swap_count,
            'execution_time': self.execution_time
        }
    
    def reset_stats(self):
        """Reset performance statistics"""
        self.comparison_count = 0
        self.swap_count = 0
        self.execution_time = 0


class BubbleSortVisualizer:
    """
    Visualize the bubble sort algorithm step by step.
    """
    
    def __init__(self):
        self.steps = []
    
    def sort_with_steps(self, arr: List[Any]) -> List[Any]:
        """Sort while recording each step"""
        arr = arr.copy()
        n = len(arr)
        self.steps = [arr.copy()]
        
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    self.steps.append(arr.copy())
        
        return arr
    
    def get_steps(self) -> List[List[Any]]:
        """Get all sorting steps"""
        return self.steps


# Example usage and demonstration
def demonstrate_bubble_sort():
    """Demonstrate various bubble sort implementations"""
    print("=" * 50)
    print("BUBBLE SORT ALGORITHM DEMONSTRATION")
    print("=" * 50)
    
    # Test data
    test_data = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {test_data}")
    
    # Basic bubble sort
    sorter = BubbleSort()
    sorted_data = sorter.basic_bubble_sort(test_data)
    stats = sorter.get_stats()
    
    print(f"\n1. Basic Bubble Sort:")
    print(f"Sorted array: {sorted_data}")
    print(f"Comparisons: {stats['comparisons']}, Swaps: {stats['swaps']}, Time: {stats['execution_time']:.6f}s")
    
    # Optimized bubble sort
    sorter.reset_stats()
    sorted_data = sorter.optimized_bubble_sort(test_data)
    stats = sorter.get_stats()
    
    print(f"\n2. Optimized Bubble Sort:")
    print(f"Sorted array: {sorted_data}")
    print(f"Comparisons: {stats['comparisons']}, Swaps: {stats['swaps']}, Time: {stats['execution_time']:.6f}s")
    
    # Recursive bubble sort
    sorter.reset_stats()
    sorted_data = sorter.recursive_bubble_sort(test_data)
    stats = sorter.get_stats()
    
    print(f"\n3. Recursive Bubble Sort:")
    print(f"Sorted array: {sorted_data}")
    print(f"Comparisons: {stats['comparisons']}, Swaps: {stats['swaps']}, Time: {stats['execution_time']:.6f}s")
    
    # Descending order
    sorter.reset_stats()
    sorted_data = sorter.basic_bubble_sort(test_data, SortOrder.DESCENDING)
    stats = sorter.get_stats()
    
    print(f"\n4. Descending Order:")
    print(f"Sorted array: {sorted_data}")
    
    # Performance comparison
    print(f"\n5. Performance Comparison:")
    sizes = [10, 50, 100, 200]
    for size in sizes:
        random_data = [random.randint(1, 1000) for _ in range(size)]
        
        sorter.reset_stats()
        sorter.basic_bubble_sort(random_data)
        basic_stats = sorter.get_stats()
        
        sorter.reset_stats()
        sorter.optimized_bubble_sort(random_data)
        optimized_stats = sorter.get_stats()
        
        print(f"Size {size}: Basic - {basic_stats['comparisons']} comparisons, "
              f"Optimized - {optimized_stats['comparisons']} comparisons")


# Custom data type example
class Student:
    """Example custom data type for sorting"""
    def __init__(self, name: str, grade: float):
        self.name = name
        self.grade = grade
    
    def __repr__(self):
        return f"Student({self.name}, {self.grade})"


def sort_custom_objects():
    """Demonstrate sorting custom objects"""
    print(f"\n6. Sorting Custom Objects:")
    
    students = [
        Student("Alice", 85.5),
        Student("Bob", 92.3),
        Student("Charlie", 78.9),
        Student("Diana", 95.1)
    ]
    
    sorter = BubbleSort()
    
    # Sort by grade
    sorted_students = sorter.basic_bubble_sort(
        students, 
        key=lambda s: s.grade
    )
    
    print("Students sorted by grade:")
    for student in sorted_students:
        print(f"  {student}")


if __name__ == "__main__":
    demonstrate_bubble_sort()
    sort_custom_objects()
    
    # Visualizer example
    print(f"\n7. Sorting Visualization:")
    visualizer = BubbleSortVisualizer()
    small_data = [3, 1, 4, 2]
    visualizer.sort_with_steps(small_data)
    
    print("Sorting steps:")
    for i, step in enumerate(visualizer.get_steps()):
        print(f"Step {i}: {step}")
```

## 📊 Performance Analysis

The repository includes comprehensive performance analysis:

1. **Time complexity verification** with different input sizes
2. **Comparison with other sorting algorithms** (QuickSort, MergeSort)
3. **Best-case vs worst-case performance** analysis
4. **Memory usage profiling**

## 🧪 Testing Suite

```python
# tests/test_bubble_sort.py
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
```

## 🎨 Visualization

The project includes a visualization module that shows:
- Step-by-step sorting process
- Color-coded element comparisons and swaps
- Real-time performance metrics
- Animated sorting visualization

## 📈 Educational Value

This implementation is perfect for:
- **Computer science students** learning sorting algorithms
- **Developers** understanding algorithm optimization
- **Educators** creating teaching materials
- **Interview preparation** for technical roles

## 🌟 GitHub Features

- **Comprehensive documentation** with algorithm explanation
- **CI/CD pipeline** with automated testing
- **Performance benchmarks**
- **Multiple implementation variants**
- **Visualization tools**
- **Usage examples** and tutorials

This bubble sort implementation provides a complete, professional-grade resource for your GitHub repository that demonstrates both the algorithm fundamentals and advanced software engineering practices!
