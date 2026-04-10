This artifact demonstrates enhancements made to a vector-based sorting program implemented in C++.

The program uses a vector data structure to store a collection of elements. A vector was selected because it allows dynamic resizing and efficient access to elements using indexing. This makes it suitable for managing lists of data that need to be sorted.

The primary algorithm implemented is selection sort. This algorithm works by repeatedly finding the smallest element in the unsorted portion of the vector and swapping it with the element at the current position. This process continues until the entire vector is sorted.

Selection sort has a time complexity of O(n^2), which makes it inefficient for large datasets. However, it is useful for demonstrating fundamental algorithm concepts and understanding how sorting operations work step by step.

Enhancements include:
- Implementation of the selection sort algorithm
- Performance timing using clock() to measure execution time
- Improved code structure and readability
- Refactoring loops to reduce redundancy and improve maintainability

Testing was performed using multiple datasets of different sizes to verify correct sorting behavior and to analyze execution time. The results confirmed that the algorithm correctly sorts the data and behaves as expected based on its time complexity.

The original folder contains the initial version of the program, while the enhanced folder contains the improved implementation with added functionality and performance tracking.
