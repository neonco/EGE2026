progs = {
    (' ', 0): (' ', -1, 1),
    (' ', 1): ('1', -1, 2),
    (' ', 2): (' ', 2, 2),
    ('0', 1): ('1', 2, 2),
    ('1', 1): ('0', -1, 1),
}

def mt(s):
    s = list(100 * ' ' + s + ' ')
    q = 0
    i = -1
    while True:
        cmd = progs[(s[i], q)]
        if cmd[1] == 2:
            s[i] = cmd[0]
            break
        s[i] = cmd[0]
        i += cmd[1]
        q = cmd[2]
    return "".join(s).strip().lstrip()

print(int(mt(bin(1023)[2:]), 2))