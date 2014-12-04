0:350381issingLetters(sentence):
    sentence = sentence.upper()
    print sentence
    alphaList = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = list(alphaList)
    for char in alphaList:
        if sentence.find(char)>=0:
            result.remove(char)
    result = "".join(result)
    return result
print getMissingLetters("A quick brown fox jumps over the lazy dog")
print getMissingLetters('A slow yellow fox crawls under the proactive dog')
print getMissingLetters('Lions, and tigers, and bears, oh my!')
print getMissingLetters('')