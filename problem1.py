import random
import timeit


def sum_equals_num(numbers: list, x: int) -> bool:
    for i in range(0, len(numbers)):
        res = x - numbers[i]
        if res >= 0 and res in numbers:
            return True

    return False


if __name__ == '__main__':
    total_nums = 1000000
    k = 517

    nums = []
    for i in range(0, total_nums):
        nums.append(random.randint(1, total_nums))

    start_time = timeit.default_timer()
    result = sum_equals_num(nums, k)
    end_time = timeit.default_timer() - start_time

    print(f'{result}. Executed in {end_time}s.')
