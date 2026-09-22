"""
Data Science and Statistical Utilities Module.
Co-authored collaborative learning implementation for Python basics and data analytics.
"""

from typing import List, Union, Tuple, Optional
import math


def calculate_mean(numbers: List[Union[int, float]]) -> float:
    """Calculate the arithmetic mean of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate mean of empty list.")
    return sum(numbers) / len(numbers)


def calculate_median(numbers: List[Union[int, float]]) -> float:
    """Calculate the median of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate median of empty list.")
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2.0
    return float(sorted_nums[mid])


def calculate_variance(numbers: List[Union[int, float]], sample: bool = True) -> float:
    """Calculate the variance of a list of numbers."""
    if len(numbers) < 2 and sample:
        raise ValueError("Sample variance requires at least 2 numbers.")
    mean = calculate_mean(numbers)
    sum_sq_diff = sum((x - mean) ** 2 for x in numbers)
    divisor = len(numbers) - 1 if sample else len(numbers)
    return sum_sq_diff / divisor


def calculate_std_dev(numbers: List[Union[int, float]], sample: bool = True) -> float:
    """Calculate the standard deviation of a list of numbers."""
    return math.sqrt(calculate_variance(numbers, sample=sample))


def min_max_normalize(numbers: List[Union[int, float]]) -> List[float]:
    """Normalize a list of numbers between 0 and 1 using Min-Max scaling."""
    if not numbers:
        return []
    min_val = min(numbers)
    max_val = max(numbers)
    if min_val == max_val:
        return [0.0] * len(numbers)
    return [(x - min_val) / (max_val - min_val) for x in numbers]


def z_score_normalize(numbers: List[Union[int, float]]) -> List[float]:
    """Standardize a list of numbers to have mean 0 and standard deviation 1."""
    if len(numbers) < 2:
        raise ValueError("Z-score normalization requires at least 2 numbers.")
    mean = calculate_mean(numbers)
    std = calculate_std_dev(numbers, sample=True)
    if std == 0:
        return [0.0] * len(numbers)
    return [(x - mean) / std for x in numbers]


if __name__ == "__main__":
    sample_data = [12, 15, 18, 20, 22, 25, 30]
    print(f"Dataset: {sample_data}")
    print(f"Mean: {calculate_mean(sample_data):.2f}")
    print(f"Median: {calculate_median(sample_data):.2f}")
    print(f"Std Dev: {calculate_std_dev(sample_data):.2f}")
    print(f"Min-Max Normalized: {[round(x, 2) for x in min_max_normalize(sample_data)]}")
