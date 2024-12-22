from functools import cache
@cache
def mix(m: int, s: int) -> int:
    return m ^ s

@cache
def prune(p: int) -> int:
    return p % 16777216

@cache
def step(n: int) -> int:
    # Calculate the result of multiplying the secret number by 64.
    s1 = n << 6
    # Then, mix this result into the secret number.
    s2 = mix(n, s1)
    # Finally, prune the secret number.
    s3 = prune(s2)
    # Calculate the result of dividing the secret number by 32. Round the result down to the nearest integer.
    s4 = s3 // 32
    # Then, mix this result into the secret number.
    s5 = mix(s3, s4)
    # Finally, prune the secret number.
    s6 = prune(s5)
    # Calculate the result of multiplying the secret number by 2048.
    s7 = s6 * 2048
    # Then, mix this result into the secret number.
    s8 = mix(s7, s6)
    # Finally, prune the secret number.
    s9 = prune(s8)
    return s9

answer1 = 0
data = open('input_22.txt', 'r', encoding='utf-8').read()
first_numbers = list(map(int, data.splitlines()))
print(first_numbers[0])
print(len(first_numbers))
for ss in first_numbers:
    for i in range (2000):
        ss = step(ss)
    answer1 +=ss
print(answer1)