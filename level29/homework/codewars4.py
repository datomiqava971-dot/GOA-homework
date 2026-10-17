def find_multiples(integer, limit):
    result = []
    n=integer
    while n<=limit:
        result.append(n)
        n+=integer
    return result