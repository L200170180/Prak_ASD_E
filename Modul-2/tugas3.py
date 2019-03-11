from tugas2 import manusia
class Mahasiswa(manusia):
    """ class mahsiswa yang dibangun dai class manusia """
    def __init__(self,nama,NIM,kota,us):
        self.Nama=nama
        self.NIM=NIM
        self.kota=kota
        self.uang=us
    def __str__(self):
        s=self.nama+',NIM '+str(self.NIM)\
           +'. tinggal di '+self.kota\
           +'. uang saku Rp '+str(self.uang)\
           +'. tiap bulan'
        return s
    def ambilin(self):
        return self.Nama
    def ambilnim(self):
        return self.NIM
    def ambiluang(self):
        return self.uang
    def makan(self,s):
        print ("saya makan",s)
        self.keadaan='kenyang'
    def kota(self):
        return self.kota
    def perbarui(self,x):
        self.kota=x

a=input("masukan nama: ")
b=input("masukan NIM: ")
c=input("masukan kota asal: ")
d=input("masukan uang saku: ")

m1=Mahasiswa(a,b,c,d)
print(m1.ambilin())
