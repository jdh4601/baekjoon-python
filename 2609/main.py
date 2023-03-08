import sys
sys.stdin = open("input.txt", "r")
a, b = map(int, sys.stdin.readline().split())

# 최대공약수
def gcd(a, b):
    while b != 0:
        a = a % b
        a, b = b, a
    return a

# 최소공배수
def icd(a, b):
    return a * b // gcd(a, b)

print(gcd(a, b))
print(icd(a, b))

