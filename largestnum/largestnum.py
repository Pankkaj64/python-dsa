

nums = [-1, 3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37]
def largesnum(nums):
    best = nums[0]
    for i in range(len(nums)):
        current = 0
        for j in range(i, len(nums)):
            current += nums[j]
            if current > best:
                best = current
    return best

if __name__ == "__main__":
    print(largesnum(nums))



    