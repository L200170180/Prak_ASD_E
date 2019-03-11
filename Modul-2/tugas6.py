from tugas2 import manusia

class Siswa(manusia):
    def __init__ (self,nama,kelas,jurusan):
        self.nm=nama
        self.kls=kelas
        self.jur=jurusan
    
    def __str__ (self):
        x=self.nm+' kealas '+self.kelas+' jurusan '+self.jur
        return x
    
    def ambiln(self):
        return self.nm
    
    def ambiljur(self):
        return self.jur
    
    def gantij(self,x):
        self.jur=x
    
    def ambilk(self):
        return self.kls
    
    def gantik(self,x):
        self.kls=x

x=Siswa('ino',12,'solo-jogja')
print(x.ambiln())
print(x.ambiljur())
x.gantij('informatika')
print(x.ambiljur())
print(x.ambilk())
x.gantik(10)
print(x.ambilk())
