def any7(nums):
    for num in nums:
        if num == 7:
            return True

    return False


result = any7([1, 2, 4, 5])
print(result)

# print("should be true", any7([1, 2, 7, 4, 5]))
# print("should be false", any7([1, 2, 4, 5]))






