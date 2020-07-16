def freq(col, printThis = True, printCount = -1):
    result = {}
    for row in col:
        if row in result: result[row] += 1
        else: result[row] = 1
    
    if printThis:
        sort = []
        for (k, v) in result.items(): sort.append((k,v))
        sort = sorted(sort, key = lambda x: -x[1])
        for el in sort:
            print(str(el[0]) + "\t" + str(el[1]))
            printCount = printCount - 1
            if printCount == 0: break
                
    return result