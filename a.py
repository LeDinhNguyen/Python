# arr = ["leetcode", "leed", "leets"]
#
#
# def longestCommonPrefix(arr: list):
#     if len(arr) == 0:
#         return ""
#     prefix = arr[0]
#     for i in range(1, len(arr)):
#         while arr[i].index(prefix):
#             prefix = prefix[0 : len(prefix) - 1]
#
#     return prefix
#
#
# print(longestCommonPrefix(arr))
def calcu(n):
    if n == 1:
        return 0
    else:
        return 2 * calcu(n / 2) + n


print(calcu(8))
