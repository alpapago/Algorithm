import sys

input = sys.stdin.readline

s = input().rstrip()

if len(s) == 0:
    print(0)
    exit(0)

if s[0] == ' ':
    ans = 0
else:
    ans = 1



for i in range(len(s)):
    if s[i] == ' ':
        ans += 1
print(ans)
