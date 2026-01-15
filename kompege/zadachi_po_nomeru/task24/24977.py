from collections import Counter

with open('24_24977.txt') as f:
    s = f.readline()

print(len(s))
print(Counter(s))

for i in range(0, 10):
    i += 1
    print(i)

# m = []
# for i in range(len(s)):
#     if s[i] == '2' and s[i+2] == '0' and s[i+4] == '2' and s[i+6] == '6':
