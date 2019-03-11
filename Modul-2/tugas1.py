class pesan(object):
    """
    sebuah class bernama pesan
    """
    def __init__(self,string):
        self.teks=string
    def cetak(self):
        print(self.teks)
    def cetakkapital(self):
        print(str.upper(self.teks))
    def cetakkecil(self):
        print(str.lower(self.teks))
    def jumkar(self):
        return len(self.teks)
    def cetakjumlah(self):
        print("kalimatku mempunyai: ",len(self.teks),"karakter")
    def perbarui(self,strbaru):
        self.teks = strbaru
    def terkandung(self,x):
        a=str(x)
        if x in self.teks:
            print("true")
        else:
            print("false")
    def hitungv(self):
        a='aioueAIOUE'
        x=0
        for i in self.teks:
            if i in a:
                x+=1
        return(x)
    def hitungk(self):
        a='aioueAIOUE'
        x=0
        for i in self.teks:
            if i not in a:
                x+=1
        return(x)
    
a=pesan("indonesia")
print(a.hitungv())
