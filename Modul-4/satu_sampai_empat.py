class mhsTIF():
    def __init__(self, nama, asal, saku):
        self.nama = nama
        self.asal = asal
        self.saku = saku

c0 = mhsTIF('aaa','sukoharjo',240000)
c1 = mhsTIF('bbb','klaten', 260000)
c2 = mhsTIF('ccc','salatiga',280000)
c3 = mhsTIF('ddd','klaten',200000)
c4 = mhsTIF('eee','surakarta',200000)
c5 = mhsTIF('fff','salatiga',290000)
c6 = mhsTIF('ggg','sukoharjo',230000)

daftar = [c0,c1,c2,c3,c4,c5,c6]

########################NOMOR 1##################
def cari(n):
    baru = []
    for i in range(len(n)):
        if(n[i].asal.lower() == 'klaten'):
            baru.append(i)
    return baru


########################NOMOR 2##################
def sakuKcl(n):
    baru = n[0].saku
    for i in range(len(n)):
        if(n[i].saku<baru):
            baru = n[i].saku
    return baru

########################NOMOR 3##################
def sakuKcl2(n):
    baru = n[0].saku
    list = []
    for i in range(len(n)):
        if(n[i].saku==baru):
            list.append(n[i].nama)
        elif(n[i].saku<baru):
            baru = n[i].saku
            list = []
            list.append(n[i].nama)
    return list

########################NOMOR 4##################
def sakuKrg(n):
    batas = 250000
    list = []
    for i in range(len(n)):
        if(n[i].saku < batas):
            list.append(n[i].nama)
    return list
print(cari(daftar))
print(sakuKcl(daftar))
print(sakuKcl2(daftar))
print(sakuKrg(daftar))
