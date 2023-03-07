import sys
sys.stdin = open("input.txt", "r")
word = sys.stdin.readline()

answer = ''

for i in word:
    if i.islower():
        idx = ord(i) + 13
        if idx > 122:
            idx -= 26
        answer += chr(idx)
        
    if i.isupper():
        idx = ord(i) + 13
        if idx > 90:
            idx -= 26
        answer += chr(idx)
    
    if i.isdigit() or i == ' ':
        answer += i

print(answer)