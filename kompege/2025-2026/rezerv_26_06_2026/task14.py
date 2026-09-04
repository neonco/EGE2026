a = '0123456789ABCDEFGHI'
# print(len(a))
for x in a:
    res = int(f'76{x}79645', 19) + int(f'35{x}42', 19) + int(f'332{x}6', 19)
    if res % 18 == 0:
        print(x, res//18)

# 365875995