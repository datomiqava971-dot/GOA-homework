def to_alternating_case(string):
    result = ''
    
    for i in string:
        if i != i.lower():
            result += i.lower()
        else:
            result += i.upper()
    return result
        
        