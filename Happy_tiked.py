count = 0
hap1 = 0
hap2 = 0
for i1 in range(10):
    for i2 in range(10):
        for i3 in range(10):
            for i4 in range(10):
                for i5 in range(10):
                    for i6 in range(10):
                        if i1+i2+i3 == i4+i5+i6:
                            count +=1
                            hap2 = hap1
                            hap1 = int(f'{i1}{i2}{i3}{i4}{i5}{i6}')
                            print (f'{i1}{i2}{i3} {i4}{i5}{i6}  {hap1-hap2}  {count}')
print(count)
