#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import library untuk membaca file yang akan kita gunakan sebagai bahan analisa
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


# Membaca file
data_penjualan = pd.read_excel("C:\\Users\\Anteraja\\Documents\\Data_dummy_clean.xlsx")
data_penjualan.head()


# In[3]:


# Cek info data 
data_penjualan.info()


# In[4]:


# Cek data untuk mengetahui apakah ada nilai yang tidak terbaca atau null 
data_penjualan.isnull().sum()


# In[5]:


# kita ingin mengetahui nama-nama dari kolom data
data_penjualan.columns


# In[6]:


data_penjualan.dtypes


# NEXT.. LET'S BEGIN TO EXPLORATORY DATA ANALYSIS
# Statistik deskriptif tentang mendeskripsikan dan menyederhanakan suatu data. Dalam statistik deskriptif menggunakan dua pendekatan :
# 1. Pendekatan kuantitatif dengan mendeskripsikan dan membuat summary data numerik.
# 2. Pendekatan visual dengan mengilustrasikan data menggunakan chart, plot, histogram, dan visual grafis lainnya.
# 
# *Poin terpenting dalam EDA yaitu curiosity atau rasa ingin tau yang tinggi. Sehingga melakukan list down pertanyaan akan mempermudah proses EDA.
# 
# 5 Pertanyaan yang ingin kita ketahui :
# 1. Berapa rata-rata produk terjual ?
# 2. pada tanggal berapa pendapatan tertinggi didapatkan ?
# 3. Cek range tanggal penjualan, tampilkan table jumlah transaksi harian, lalu pada tanggal berapa penjualan terbanyak?
# 4. Cabang mana yang memiliki penjualan terbanyak ?
# 5. Cabang mana yang memiliki penjualan paling rendah ?

# In[7]:


data_penjualan.head()


# In[8]:


# persentase target dari cabang
data_penjualan['target_yn'].value_counts().plot.pie(autopct='%1.1f%%',shadow=True)
plt.show()


# Target pencapaian selama 1 week sebesar 96%.

# 1. Berapa rata-rata produk terjual ?

# In[9]:


data_penjualan['total_produk_terjual_today'].describe()


# In[10]:


#Another Insight (rataan produk terjual dimasing-masing store)
data_penjualan_group_produk_terjual = data_penjualan.groupby('nama_cabang')['total_produk_terjual_today'].mean().reset_index()


# In[11]:


data_penjualan_group_produk_terjual


# In[12]:


sns.barplot(x="nama_cabang", y="total_produk_terjual_today",data=data_penjualan_group_produk_terjual)
plt.show()


# In[13]:


Dari insight yang didapat, bahwa rata-rata penjualan adalah 451.514286, 
dan rata-rata cabang dengan penjualan terbanyak di cabang A14 dengan mean sebesar 827.714286


# 2. pada tanggal berapa pendapatan tertinggi didapatkan ?

# In[14]:


# Langkah 1. Mengelompokkan transaksi berdasarkan tanggal
data_pendapatan = data_penjualan.groupby('tanggal_penjualan')['pendapatan_bersih_cabang'].sum()
data_pendapatan


# In[15]:


# Langkah 2. Mengurutkan nilai 
data_pendapatan.sort_values(ascending = False)


# In[16]:


data_pendapatan = data_pendapatan.reset_index()
data_pendapatan.rename(columns={'pendapatan_bersih_cabang':'pendapatan_terbanyak'},inplace=True)
data_pendapatan


# In[17]:


# Cek tipe data
data_pendapatan.dtypes


# In[18]:


# Plot
g=sns.relplot(x="tanggal_penjualan", y="pendapatan_terbanyak", kind="line", data=data_pendapatan)
g.fig.set_size_inches(20,8)


# Line chart menunjukkan pendapatan tertinggi pada tanggal 5 agustus dengan total pendapatan bersih sebanyak Rp.111.384.000 rupiah.

# 3. Karena pendapatan terbesar terjadi pada tanggal 5 agustus, kita cek range tanggal penjualan, tampilkan table jumlah transaksi harian, lalu pada tanggal tersebut berapa total penjualan nya ?

# In[19]:


# Langkah 1. Mengelompokkan total produk terjual berdasarkan tanggal
data_harian = data_penjualan.groupby('tanggal_penjualan')['total_produk_terjual_today'].sum()
data_harian


# In[20]:


data_harian = data_harian.reset_index()
data_harian.rename(columns={'total_produk_terjual_today':'produk_terjual_summary'},inplace=True)
data_harian


# In[21]:


# Plot
g=sns.relplot(x="tanggal_penjualan", y="produk_terjual_summary", kind="line", data=data_harian)
g.fig.set_size_inches(20,8)


# Dari grafik line chart terlihat produk terjual paling banyak pada tanggal 5 agustus sebesar 13923 produk.

# 4. Cabang mana yang memiliki penjualan terbanyak ? 

# In[22]:


# Mengelompokkan cabang dengan penjualan terbanyak
data_cabang = data_penjualan.groupby('nama_cabang')['total_produk_terjual_today'].sum()
data_cabang


# In[23]:


data_cabang = data_cabang.reset_index()
data_cabang.rename(columns={'total_produk_terjual_today':'produk_terjual_summary'},inplace=True)
data_cabang


# In[24]:


sns.barplot(x="nama_cabang", y="produk_terjual_summary", data=data_cabang)
plt.show()


# Pada hasil visualisasi terlihat bahwa, cabang dengan penjualan terbanyak adalah di cabang A14 dengan total produk terjual sebanyak 5794.

# 5. Cabang yang memiliki penjualan terendah ?

# In[25]:


# Langkah 1. Mengelompokkan transaksi berdasarkan cabang sama seperti langkah sebelumnya, tetapi kita ganti sum dengan min
data_cabang = data_penjualan.groupby('nama_cabang')['total_produk_terjual_today'].min()
data_cabang


# In[26]:


data_cabang = data_cabang.reset_index()
data_cabang.rename(columns={'total_produk_terjual_today':'produk_terjual_terendah'},inplace=True)
data_cabang


# In[27]:


sns.barplot(x="nama_cabang", y="produk_terjual_terendah", data=data_cabang)
plt.show()


# Dari grafik cabang dengan penjualan terendah yaitu pada cabang A25 dengan total penjualan 20 produk, hal ini terjadi karena cabang A25 merupakan anak cabang yang baru saja launcing di wilayah tersebut.
# Saran : Buat trust ke masyarakat pada wilayah tersebut agar mereka mau membeli produk kita. dengan cara meningkatkan promosi dan edukasi tentang manfaat produk kita.
