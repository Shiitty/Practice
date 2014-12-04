def pictureFrames(pieces):
    result = 0
    if len(pieces)<3:
        return result
    for i in range(0, len(pieces)-2):
        for j in range(i+1, len(pieces)-1):
            for k in range(j+1, len(pieces)):
                if pieces[i]+pieces[j]<=pieces[k]:
                    continue
                if pieces[j]+pieces[k]<=pieces[i]:
                    continue
                if pieces[k]+pieces[i]<=pieces[j]:
                    continue
                print [pieces[i], pieces[j], pieces[k]]
                result += 1
    return result
print pictureFrames([1,2,3,4,5])
print pictureFrames([8,5,3])
print pictureFrames([4,23,76,22,87,3,1,99])
print pictureFrames([10000,9999,9998,9997,9996,1,2,3,4,5])
print pictureFrames([100])