print("D3 D2 D1 D0 | Y1 Y0")
print("-------------------")

for D3 in [0,1]:
    for D2 in [0,1]:
        for D1 in [0,1]:
            for D0 in [0,1]:
                if D3 + D2 + D1 + D0 == 1:
                    Y1 = D2 or D3
                    Y0 = D1 or D3
                    print(D3, D2, D1, D0, "|", int(Y1), int(Y0))
