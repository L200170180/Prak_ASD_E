class manusia(object):
    """ clas manusia dengan inisiasi 'nama' """
    keadaan='lapar'
    def __init__(self,nama):
        self.nama=nama
    def ucap(self):
        print("halo namaku: ",self.nama)
    def olah(self,k):
        print('saya habis',k)
        self.keadaan='lapar'
    def makan(self,s):
        print("saya baru saja makan ",s)
        self.keadaan='kenyang'
    def kali(self,n):
        return n*2

