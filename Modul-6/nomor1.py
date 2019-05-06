from tugas2sub import mahasiswa
from coba import urut

mh1 = mahasiswa("aaaa", 104, "qqqqq", 10000)
mh2 = mahasiswa("bbbb", 84, "wwwww", 13000)
mh3 = mahasiswa("cccc", 124, "eeeee", 5000)
mh4 = mahasiswa("dddd", 544, "rrrrr", 12000)
mh5 = mahasiswa("eeee", 4, "ttttt", 2000)

nimMH = [mh1.NIM, mh2.NIM, mh3.NIM, mh4.NIM, mh5.NIM]
usMH = [mh1.us, mh2.us, mh3.us, mh4.us, mh5.us]

a1 = urut(nimMH)
b2 = urut(usMH)

a1.printMerge(nimMH)
b2.printMerge(usMH)

a1.printQuick(nimMH)
b2.printQuick(usMH)
