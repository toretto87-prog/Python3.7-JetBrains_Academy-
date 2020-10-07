num = abs(int(input()))
number_one = num // 100
number_two = (num - number_one * 100) // 10
number_three = (num - number_one * 100 - number_two * 10) // 1
print(number_one + number_two + number_three)