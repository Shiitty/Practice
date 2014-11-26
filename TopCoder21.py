def fix(param0):
    result = param0
    result = result.strip(' ')
    result = result.capitalize()
    if result[len(result)-1]!='.':
        result += '.'
    i=0
    end = len(result)
    while i<len(result):
        if result[i]==' ':
            if result[i+1]==' ':
                result = result[0:i-1] + result[i+1:len(result)]
                i = i-1
        i = i+1
        end = len(result)
    print result
fix("   asdf  kal    ;dfj .  ")
