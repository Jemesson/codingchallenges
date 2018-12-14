import random
import timeit


def sum_equals_num(numbers: list, k: int) -> bool:
    """
    This problem was recently asked by Google.
    Given a list of numbers and a number k, return whether any two numbers from the list add up to k
    :param numbers:
    :param k:
    :return: Boolean two numbers added matches k
    """
    for i in range(0, len(numbers)):
        res = k - numbers[i]
        if res >= 0 and res in numbers:
            return True

    return False


if __name__ == '__main__':
    total_nums = 1000
    goal_number = 517

    nums = []
    for i in range(0, total_nums):
        nums.append(random.randint(1, total_nums))

    start_time = timeit.default_timer()
    result = sum_equals_num(nums, goal_number)
    end_time = timeit.default_timer() - start_time

    print(f'{result}. Executed in {end_time}s.')
