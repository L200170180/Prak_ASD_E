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




m1 = mahasiswa("Ika", 23, "Sukoharjo", 230000)
m2 = mahasiswa("Budi", 56, "Sragen", 3445556)
m3 = mahasiswa("Salman", 465, "Bandung", 38989547)
m4 = mahasiswa("Faizal", 234, "Semarang", 90739789)

Daftar = [m1.NIM, m2.NIM, m3.NIM, m4.NIM]
for i in range(len(Daftar)): 
    min_idx = i 
    for j in range(i+1, len(Daftar)): 
        if Daftar[min_idx] > Daftar[j]: 
            min_idx = j 
    
    Daftar[i], Daftar[min_idx] = Daftar[min_idx], Daftar[i]

print(Daftar)
