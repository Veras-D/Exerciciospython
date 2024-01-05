"""
Fibonacci Sequence
Date: 01/05/23
Author: Veras-D
"""
i = 2
nums = [0, 1]
num = int(input("Escolha a quantidade de termos: "))
if num == 1:
    print(nums[0])
elif num == 2:
    print(f"{nums[0]} - {nums[1]}")
elif num > 2:
    while i < num:
        nums.append(nums[i-1]+nums[i-2])
        i += 1
    for n in nums:
        if n == nums[-1]:
            print(n, end="")
        else:
            print(n, end="->")
else:
    print("Escolha uma opção valida!")
