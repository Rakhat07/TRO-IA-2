def snail(snail_map):
    if len(snail_map) == 1:
        return snail_map[0]
    elif len(snail_map)==0:
        return []

    t = len(snail_map)
    snailr = []
    while snail_map[0]:
        snailr.append(snail_map[0][0])
        del snail_map[0][0]
    del snail_map[0]
    j = 0
    while j <= t-2:
        snailr.append(snail_map[j][len(snail_map) ])
        del snail_map[j][len(snail_map) ]
        j += 1
    z = len(snail_map) - 1
    while z >= 0:
        snailr.append(snail_map[len(snail_map) - 1][z])
        del snail_map[len(snail_map) - 1][z]
        z -= 1
    del snail_map[t - 2]
    z1 = len(snail_map) - 1
    while z1 >= 0:
        snailr.append(snail_map[z1][0])
        del snail_map[z1][0]
        z1 -= 1
    k = snail(snail_map)
    if isinstance(k,list):
        return snailr + k
    else:
        return snailr + [k]


array = [[1, 2, 3, 10],
         [4, 5, 6, 11],
         [7, 8, 9, 12],
         [14, 15, 16, 20]]
print(snail(array))

