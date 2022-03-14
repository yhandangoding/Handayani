#contoh code boolean
saya_orang_indonesia = True
saya_adalah_robot = False

print('Apakah saya orang Indonesia?', saya_orang_indonesia)
print('Apakah saya adalah robot?', saya_adalah_robot)
print('Tipe dari saya_orang_indonesia', type(saya_orang_indonesia))
print('Tipe dari saya_adalah_robot', type(saya_adalah_robot))

#contoh code integer
a = 11
print (a, "merupakan tipe", type (a))

#Contoh code string
nama_depan = "Wahit"
nama_belakang = 'Abdulloh'
nama_lengkap = nama_depan + ' ' + nama_belakang
usia = '12'
alamat = 'Bangkalan'
kata_mutiara = "Don't judge a book by it's cover"

print(nama_lengkap, '(' + usia + ')', ',', 'dari', alamat, ', kata mutiara:', kata_mutiara)

print('Tipe dari nama_lengkap:', type(nama_lengkap))
print('Tipe dari usia:', type(usia))
print('Tipe dari alamat:', type(alamat))
print('Tipe dari kata_mutiara:', type(kata_mutiara))

#contoh code float
a = 4.0
print (a, "merupakan tipe", type (a))

#contoh code if
nilai = 80

if nilai >= 85 :
  print ('nilai A')
  
  #contoh code if else
  nilai = 60

if nilai >= 70:
  print ('nilai A')
else :
  print ('mengulang')
  
  #contoh code if elif else
  nilai = int(input ("masukkan nilai:"))

if nilai >= 90:
  print ('predikat A')
elif nilai >= 80:
  print ('predikat B')
elif nilai >= 70:
  print ('predikat C')
elif nilai >= 60:
  print ('predikat C')
else :
  print ('predikat E')