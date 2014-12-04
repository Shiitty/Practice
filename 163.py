0:34f66a(opponent):
    result = 0
    for (i, char) in enumerate(opponent):
        if i<2:
            if char == 'S':
                result += 1
        else:
            tmp = opponent[i-2:i]
            if opponent[i-2]==opponent[i-1]:
                if opponent[i-2]==char:
                    result += 1
            else:
                if tmp.find(char)<0:
                    result += 1
    return result
print wins("PS")
print wins("PSRRPS")
print wins("PSRPSRPRSR")
print wins("SRPSRPSPRSPRPSRPSRP")
print wins("RPPPRRPSSSRRRSRSPPSSPRRPSRRRRSPPPPSSPSSSSSRSSSRPRR")