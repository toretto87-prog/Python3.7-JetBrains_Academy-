N = int(input())
R = int(input())
time = 0
half_life = 0

while N >= R:
    N = N // 2
    time += 12
    half_life += 1
half_life *= 12
print(int(half_life))
