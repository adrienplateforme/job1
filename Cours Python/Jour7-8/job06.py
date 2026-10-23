def skyrelou(list):
    listb = []
    for i in list:
        if i >= 40 and i < 100 and i % 5 > 2:
            i = i + 5 - i % 5
            listb.append(i)
        else:
            listb.append(i)
    return(listb)