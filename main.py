from typing import List


def counting_sort(nums: List[int]) -> List[int]:
    minimum = min(nums)
    maximum = max(nums)
    counts = [0] * (maximum - minimum + 1)
    for num in nums:
        counts[num - minimum] += 1
    for i in range(1, maximum - minimum + 1):
        counts[i] += counts[i - 1]
    res = [0] * len(nums)
    for num in nums:
        res[counts[num - minimum] - 1] = num
        counts[num - minimum] -= 1
    return res


def main():
    print(counting_sort([1, 4, 1, 2, 7, 5, 2]))
    print(counting_sort([-5, -10, 0, -3, 8, 5, -1, 10]))


if __name__ == '__main__':
    main()


