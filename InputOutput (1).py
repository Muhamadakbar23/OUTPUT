#!/usr/bin/env python
# coding: utf-8

# In[1]:


bil1 = input('Isikan bilangan 1: ')
bil2 = input('Isikan bilangan 2: ')
hasil = int(bil1) + int(bil2)

print("Hasil dari:",bil1,"+",bil2,"=",hasil)


# In[2]:


print("A","B","C","D", sep='@_@') #sep = Separator / Pembatas


# <p>3. Cara melakukan <b>print</b> dengan menambahkan end di akhir baris</p>

# In[3]:


print("A","B","C","D", sep='\n', end="^_^")


# In[5]:


num_1 = 8
num_2 = 10
 
# Hasil dari 8 modulus 10 = 8
#str.format()

print('Hasil dari {} modulus {} = {}'.format(num_1,num_2,num_1%num_2))


# <hr><h1>Memformat Indeks<h1><hr>
#     <p>memformat dengan key (kunci)

# In[8]:


fname = "Muhamad"
mname = "Akbar"
lname = "Iqro"

print('Nama anda {0} {1} {2}'.format(fname,mname,lname))


# <h3>Tanda Pengenal<h3>

# In[9]:


print('Nama anda {nama}, nilai anda {nilai}'.format(nama='Andri',nilai=70))


# <h3>Pengenalan String<h3>

# In[13]:


univ = "Universitas Nusa Putra"

print("karakter pertama :",univ[0])
print("karakater terakhir :",univ[-1])
#Universitas
print(univ[0:11])
print(univ[-6:-1])
print(univ[17:])


# <h3>String<h3>

# In[15]:


f_name = 'Akbar'
l_name = 'Iqro'

print(f'Nama saya {f_name} {l_name}')

first = 100
second = 20

print(f'Hasil perjumlahan {first} + {second} = {first+second}')


# <h3>Fungsi String<h3>

# In[22]:


nama = "Andri,Budi,Chika"
nama2 = "Andri Budi Chika"
#split -> memisahkan string berdasarkan karakter tertentu
print(nama2.split())
print(nama.split(','))

#join ->menggabungkan string kedalam kumpulan karakter
print('@'.join(nama.split(',')))

#input tgl lahir-> 18/Oktober/2010
#input nama -> Bill Gate
#output:
#Tgl :18, Bulan:Oktober, Tahun:2010
#Nama Inisial :BG

tgl = input("Masukan tanggal lahir : ")
nama = input("Masukan nama : ")
pemisah = tgl.split("/")
print("Output :")
print(f"Tgl : {pemisah[0]}, Bulan:{pemisah[1]}, Tahun:{pemisah[2]}")
pemisah2 = nama.split()
nama_pertama = pemisah2[0]
nama_terakhir = pemisah2[1]
print(f"Nama inisial : {nama_pertama[0]+nama_terakhir[0]}")


# In[ ]:




