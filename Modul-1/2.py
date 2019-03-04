def gambar_persegi_panjang(tinggi,lebar):
    for i in range(tinggi):
        if i==0 or i == tinggi-1:
           print ("@"*tinggi)

        else:
            x = tinggi - lebar
            print ("@"+" "*(tinggi-2)+"@")


gambar_persegi_panjang(4,5)
