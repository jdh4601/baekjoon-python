import sys
sys.stdin = open("input.txt", "r")
word = sys.stdin.readline()

arr = [0] * 26

for alpb in word:
    idx = ord(alpb) - 97
    arr[idx] += 1

print(*arr)