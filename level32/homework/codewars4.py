def digitize(n):
    result=[]
    n=str(n)
    if n != 0:
        for i in n[::-1]:
            result.append(int(i))
    else:
        result.append(0)
    return result