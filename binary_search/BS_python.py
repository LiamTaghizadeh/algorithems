"""
Binary Search Implementation with Object-Oriented Programming in Python
"""

from typing import List, Any, Callable, Optional, Dict
import time

class BinarySearch:
    def __init__(self, data: List[Any]):
        """
        Initialize with sorted data
        """
        if not self._is_sorted(data):
            raise ValueError("Data must be sorted for binary search")
        self.data = data
    
    def _is_sorted(self, data: List[Any]) -> bool:
        """Check if data is sorted in ascending order"""
        return all(data[i] <= data[i+1] for i in range(len(data)-1))
    
    def search(self, target: Any) -> int:
        """
        Perform binary search iteratively
        Returns index if found, otherwise -1
        """
        left, right = 0, len(self.data) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if self.data[mid] == target:
                return mid
            elif self.data[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
    
    def search_recursive(self, target: Any, left: int = 0, right: Optional[int] = None) -> int:
        """
        Perform binary search recursively
        """
        if right is None:
            right = len(self.data) - 1
        
        if left > right:
            return -1
        
        mid = (left + right) // 2
        
        if self.data[mid] == target:
            return mid
        elif self.data[mid] < target:
            return self.search_recursive(target, mid + 1, right)
        else:
            return self.search_recursive(target, left, mid - 1)
    
    def __contains__(self, target: Any) -> bool:
        """Enable 'in' operator usage"""
        return self.search(target) != -1
    
    def __repr__(self) -> str:
        return f"BinarySearch(data={self.data})"


class AdvancedBinarySearch:
    def __init__(self, data: List[Any]):
        self.data = sorted(data)  # Auto-sort the data
        self.search_count = 0
        self.comparison_count = 0
    
    def search(self, target: Any) -> int:
        """Search with performance tracking"""
        self.search_count += 1
        comparisons = 0
        left, right = 0, len(self.data) - 1
        
        while left <= right:
            comparisons += 1
            mid = (left + right) // 2
            
            if self.data[mid] == target:
                self.comparison_count += comparisons
                return mid
            elif self.data[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        self.comparison_count += comparisons
        return -1
    
    def get_stats(self) -> Dict[str, float]:
        """Get search statistics"""
        return {
            'total_searches': self.search_count,
            'total_comparisons': self.comparison_count,
            'avg_comparisons_per_search': (
                self.comparison_count / self.search_count if self.search_count > 0 else 0
            )
        }
    
    def find_first_occurrence(self, target: Any) -> int:
        """Find first occurrence of target (for duplicates)"""
        index = self.search(target)
        if index == -1:
            return -1
        
        # Move left to find first occurrence
        while index > 0 and self.data[index - 1] == target:
            index -= 1
        
        return index
    
    def find_last_occurrence(self, target: Any) -> int:
        """Find last occurrence of target (for duplicates)"""
        index = self.search(target)
        if index == -1:
            return -1
        
        # Move right to find last occurrence
        while index < len(self.data) - 1 and self.data[index + 1] == target:
            index += 1
        
        return index
    
    def __contains__(self, target: Any) -> bool:
        return self.search(target) != -1
    
    def __repr__(self) -> str:
        return f"AdvancedBinarySearch(data={self.data}, searches={self.search_count})"


class GenericBinarySearch:
    def __init__(self, data: List[Any], key: Optional[Callable] = None):
        """
        Initialize with optional key function for custom sorting
        """
        self.data = data
        self.key = key or (lambda x: x)
        self._sort_data()
    
    def _sort_data(self):
        """Sort data using the key function"""
        self.data.sort(key=self.key)
    
    def search(self, target: Any) -> int:
        """Search for target using the key function"""
        left, right = 0, len(self.data) - 1
        target_key = self.key(target)
        
        while left <= right:
            mid = (left + right) // 2
            mid_value = self.key(self.data[mid])
            
            if mid_value == target_key:
                return mid
            elif mid_value < target_key:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
    
    def __contains__(self, target: Any) -> bool:
        return self.search(target) != -1
    
    def __repr__(self) -> str:
        return f"GenericBinarySearch(data={self.data}, key={self.key})"


class BenchmarkBinarySearch(BinarySearch):
    def timed_search(self, target: Any) -> Dict[str, Any]:
        """Search with timing"""
        start_time = time.perf_counter()
        result = self.search(target)
        end_time = time.perf_counter()
        
        return {
            'result': result,
            'time_taken': end_time - start_time,
            'data_size': len(self.data)
        }
    
    def benchmark_searches(self, targets: List[Any]) -> List[Dict[str, Any]]:
        """Benchmark multiple searches"""
        results = []
        for target in targets:
            results.append(self.timed_search(target))
        return results


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person({self.name}, {self.age})"
    
    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        return self.name == other.name and self.age == other.age


# Example usage and demonstration
def demonstrate_binary_search():
    print("=" * 50)
    print("BINARY SEARCH OOP DEMONSTRATION")
    print("=" * 50)
    
    # Example 1: Basic BinarySearch
    print("\n1. Basic BinarySearch:")
    data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    bs = BinarySearch(data)
    
    print(f"Data: {data}")
    print(f"Search for 7: Index {bs.search(7)}")
    print(f"Search for 10: Index {bs.search(10)}")
    print(f"Is 13 in data? {13 in bs}")
    print(f"Recursive search for 9: Index {bs.search_recursive(9)}")
    
    # Example 2: AdvancedBinarySearch with statistics
    print("\n2. AdvancedBinarySearch with Statistics:")
    advanced_bs = AdvancedBinarySearch(data)
    
    targets = [7, 2, 15, 19, 25]
    for target in targets:
        result = advanced_bs.search(target)
        print(f"Search for {target}: {'Found' if result != -1 else 'Not found'}")
    
    stats = advanced_bs.get_stats()
    print(f"\nStatistics: {stats}")
    
    # Example 3: GenericBinarySearch with custom objects
    print("\n3. GenericBinarySearch with Custom Objects:")
    people = [
        Person("Alice", 25),
        Person("Bob", 30),
        Person("Charlie", 20),
        Person("Diana", 35)
    ]
    
    # Search by age
    age_search = GenericBinarySearch(people, key=lambda p: p.age)
    result_index = age_search.search(Person("", 30))
    print(f"Search for age 30: Index {result_index}")
    if result_index != -1:
        print(f"Found: {people[result_index]}")
    
    # Example 4: Benchmarking
    print("\n4. Benchmarking:")
    large_data = list(range(1, 10001))  # 10,000 elements
    benchmark_bs = BenchmarkBinarySearch(large_data)
    
    benchmark_targets = [500, 7500, 9999, 15000]
    results = benchmark_bs.benchmark_searches(benchmark_targets)
    
    for result in results:
        status = "Found" if result['result'] != -1 else "Not found"
        print(f"Target {benchmark_targets[results.index(result)]}: {status}, "
              f"Time: {result['time_taken']:.8f}s")
    
    # Example 5: Handling duplicates
    print("\n5. Handling Duplicates:")
    duplicate_data = [1, 2, 2, 2, 3, 4, 4, 5, 6]
    dup_bs = AdvancedBinarySearch(duplicate_data)
    
    print(f"Data with duplicates: {duplicate_data}")
    print(f"First occurrence of 2: Index {dup_bs.find_first_occurrence(2)}")
    print(f"Last occurrence of 2: Index {dup_bs.find_last_occurrence(2)}")
    print(f"First occurrence of 4: Index {dup_bs.find_first_occurrence(4)}")


if __name__ == "__main__":
    demonstrate_binary_search()
    
    print("\n" + "=" * 50)
    print("ADDITIONAL TEST CASES")
    print("=" * 50)
    
    # Test edge cases
    test_cases = [
        ([], 5),  # Empty array
        ([1], 1),  # Single element
        ([1], 2),  # Single element not found
        ([1, 3, 5], 1),  # First element
        ([1, 3, 5], 5),  # Last element
    ]
    
    for data, target in test_cases:
        try:
            bs = BinarySearch(data)
            result = bs.search(target)
            print(f"Data: {data}, Target: {target} -> Result: {result}")
        except ValueError as e:
            print(f"Data: {data}, Target: {target} -> Error: {e}")
