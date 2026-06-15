a = sorted('СТРОКА')

ind = 1
for q in a:
    for w in a:
        for e in a:
            for r in a:
                for t in a:
                    if ind % 2 == 0 and q not in 'АСТ' and (q+w+e+r+t).count('О') == 2:
                        print(ind, q+w+e+r+t)
                    ind += 1


# 5058 РТООТ