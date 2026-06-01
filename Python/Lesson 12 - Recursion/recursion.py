# def factorial(n: int) -> int:
#     if n == 1 or n == 0:
#         return 1
#     print(f"Calculating {n} * {n - 1}!")
#     return n * factorial(n - 1)


# nineninenine = factorial(999)
# print(nineninenine * 1000)


# def re_sum_one(num_list: list[int]) -> int:
#     print("Entering another recursion")
#     if len(num_list) == 1:
#         return num_list.pop()

#     last = num_list.pop()
#     print(f"Calculating {num_list[:]} + {last}")
#     val = re_sum_one(num_list[:])
#     print(f"Finished recursion for {num_list[:]}")
#     return val + last


# max = 10
# numbers = list(range(1, max + 1))
# # print(re_sum_one(numbers[:]))

# def re_sum_half(num_list: list[int]) -> int:
#     if len(num_list) == 1:
#         return num_list[0]

#     half = len(num_list) // 2
#     print(f"Calculating {num_list[:half]} + {num_list[half:]}")
#     return re_sum_half(num_list[:half]) + re_sum_half(num_list[half:])

# print(re_sum_half(numbers[:]))


# def bad():
#     return bad()

# bad()


# def fib(n: int) -> int:
#     """
#     0, 1, 2, 3, 4, 5, 6,  7,  8, ...
#     0, 1, 1, 2, 3, 5, 8, 13, 21, ...
#     """
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1

#     print(f"Calculating fib({n-1}) + fib({n-2})")
#     return fib(n - 1) + fib(n - 2)


# print(fib(6))


# def binary_search(arr, low, high, x):
#     """assumes array is already sorted"""
#     if high >= low:
#         mid = (high + low) // 2
#         if arr[mid] == x:
#             return mid
#         elif arr[mid] > x:
#             return binary_search(arr, low, mid - 1, x)
#         else:
#             return binary_search(arr, mid + 1, high, x)
#     else:
#         return -1


# # Test array
# arr = [2, 3, 4, 10, 40]
# x = 10

# # Function call
# result = binary_search(arr, 0, len(arr) - 1, x)

# if result != -1:
#     print("Element is present at index", str(result))
# else:
#     print("Element is not present in array")


# import os

# def list_dir_recursive(directory):
#     for entry in os.listdir(directory):
#         full_path = os.path.join(directory, entry)
#         if os.path.isdir(full_path):
#             list_dir_recursive(full_path)
#         else:
#             print(full_path)

# list_dir_recursive('/my_folder')
