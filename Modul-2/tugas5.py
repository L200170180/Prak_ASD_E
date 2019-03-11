from tugas2 import manusia
class Mahasiswa(manusia):
    """ class mahsiswa yang dibangun dai class manusia """
    mk=[]
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
    def kuliah(self,x):
        return self.mk.append(x)
    def hapus(self,x):
        return self.mk.remove(x)
    def lihat(self):
        return self.mk

m1=Mahasiswa('sri',565,'solo',120000)
m1.kuliah('asda')
m1.kuliah('adwa')
print(m1.lihat())
m1.hapus('adwa')
print(m1.lihat())