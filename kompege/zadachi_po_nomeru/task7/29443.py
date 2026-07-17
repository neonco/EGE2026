second_b = 10*8//8 * 32_000 * 3 + 1024
second_a = 2 * 32_000
v_a = 3750*1024
t = v_a // second_a
v_b = second_b * t
print(v_b / 1024 / 1024)
# 55
