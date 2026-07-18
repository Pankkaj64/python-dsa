def find_median_sorted_arrays(nums1, nums2):
    # Merge the two sorted arrays
    merged = sorted(nums1 + nums2)
    n = len(merged)

    # If the total number of elements is odd
    if n % 2 == 1:
        return merged[n // 2]

    # If the total number of elements is even
    return (merged[n // 2 - 1] + merged[n // 2]) / 2


# Example usage
nums1 = [1, 3]
nums2 = [2]

print(find_median_sorted_arrays(nums1, nums2))