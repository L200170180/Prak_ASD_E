from tugas2 import manusia
class mahasiswa(manusia):
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
    def pkota(self):
        return self.kota
    def perbarui(self,x):
        self.kota=x
    def tambah(self,x):
        self.uang=self.uang+x


m1=mahasiswa('sri',565,'solo',120000)
print(m1.pkota())
m1.perbarui('jogja')
print(m1.pkota())
print(m1.ambiluang())
m1.tambah(5000)
print(m1.ambiluang())