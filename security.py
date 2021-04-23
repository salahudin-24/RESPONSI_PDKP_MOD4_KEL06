def separator():
    print('------------------------------------------')

def encrypt(plain,key) :
    stringCipher=''
    for character in plain :
        asciiPlain=ord(character)
        asciiCipher=asciiPlain+key
        if ord('a') <= asciiPlain <= ord('z'):
            if asciiCipher > ord('z') :
                asciiCipher-=26
        elif ord('A') <= asciiPlain <= ord('Z') :
            if asciiCipher > ord('Z') :
                asciiCipher -= 26
        else :
            asciiCipher=asciiPlain
        charCipher=chr(asciiCipher)
        stringCipher=stringCipher+charCipher
    return stringCipher

class decrypt :
    def __init__(self,cipher,key) :
        self.stringCipher=cipher
        self.key=key
    def decrypt(self) :
        self.stringPlain=''
        for character in self.stringCipher :
            self.asciiCipher=ord(character)
            self.asciiPlain=self.asciiCipher-self.key
            if ord('a') <= self.asciiCipher <= ord('z') :
                if self.asciiPlain < ord('a') :
                    self.asciiPlain+=26
            elif ord('A') <= self.asciiCipher <= ord('Z') :
                if self.asciiPlain < ord('A') :
                    self.asciiPlain+=26
            else :
                self.asciiPlain == self.asciiCipher
            self.charPlain=chr(self.asciiPlain)
            self.stringPlain=self.stringPlain+self.charPlain
        return self.stringPlain