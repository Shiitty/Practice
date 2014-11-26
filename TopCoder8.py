def getComplement(param):
    result = ""
    for char in param:
        if char=='G':
            result = result + 'C'
        elif char=='C':
            result = result + 'G'
        elif char=='T':
            result = result + 'A'
        elif char=='A':
            result = result + 'T'
        else:
            return "error"
    return result
    
print getComplement("GAAACT")