def rot13(para):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    capalphabet = "ABCEDFGHIJKLMNOPQRSTUVWXYZ"
    #indexes = []
    result = ""
    for char in para:
        if ord('a')<=ord(char)<=ord('z'):
            index = ((ord(char)-ord('a')+13)%26)
            result += alphabet[index]
        elif ord('A')<=ord(char)<=ord('z'):
            index = ((ord(char)-ord('A')+13)%26)
            result += capalphabet[index]
        else:
            result += char
    return result

print rot13('z')
print rot13('a')
print rot13('x')
print rot13("Hello world!")
print rot13("This is a test message.")
print rot13("abc123<>,xyz?*$")