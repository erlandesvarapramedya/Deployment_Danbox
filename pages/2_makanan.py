import streamlit as st

from deta import Deta

DETA_KEY="c0vyzncy_FtHYP14kaerkDsVKqs5eGtBBNaRVwtH7"

deta=Deta(DETA_KEY)

db=deta.Base("pelanggan_db")


st.title("DANBOX")
st.header("MAKANAN")
st.subheader("Aplikasi Pemesanan Makanan")


st.sidebar.success("Pilih halaman")

    
pilihan = st.selectbox(
    'Pilihan Pengambilan',
    ('pick up', ' delivered'))
st.write('You selected:', pilihan)


#NAMA
import streamlit as st
nama=st.text_input('Nama Pelanggan')
if not nama:
    st.warning('Mohon masukkan nama.')

#KELAS    
kelas=st.text_input('Kelas')
if not kelas:
    st.warning('Mohon masukkan Kelas.')

#TANGGAL
tanggal=st.text_input('Tanggal Pemesanan')
if not tanggal:
    st.warning('Mohon masukkan tanggal')
    
st.subheader('Menu Makanan')

from PIL import Image
import streamlit as st

col1, col2, col3=st.columns(3)
with col1:
    st.subheader('Donat')
    st.image('gambar/don.jpg',width=150)
    number1 = st.number_input('Jumlah Donat',0)
with col2:
    st.subheader('Pisang Coklat')
    st.image('gambar/sang.jpg',width=150)
    number2 = st.number_input('Jumlah pisang coklat',0)
with col3:
    st.subheader('Kue sus')
    st.image('gambar/sss.jpg',width=150)
    number3 = st.number_input('Jumlah kue sus',0)
    
col4, col5, col6=st.columns(3)
with col4:
    st.subheader('Risol mayo')
    st.image('gambar/maaaa.jpg',width=150)
    number4 = st.number_input('Jumlah Risol',0)
with col5:
    st.subheader('Pie buah')
    st.image('gambar/coba.jpg',width=150)
    number5 = st.number_input('Jumlah Pie buah',0)
with col6:
    st.subheader('Bomboloni')
    st.image('gambar/bom.jpg',width=150)
    number6 = st.number_input('Jumlah Bomboloni',0)
    
jumlah = float(number1 or number2 or number3 or number4 or number5 or number6)

Total=st.button("Rincian")
if Total:
    st.success("pesanan berhasil")
if Total:
    import pandas as pd
    harga1=2000*number1
    harga2=3000*number2
    harga3=2000*number3
    harga4=2000*number4
    harga5=2000*number5
    harga6=2000*number6
    data = [['Risol',number1,harga1],['Keu Sus',number2,harga2],['Pisang Roll',number3,harga3],['Martabak Telor',number4,harga4],['Pastel',number5,harga5],['kue sus buah',number6,harga6]]
    df=pd.DataFrame(data,columns=['Makanan','jumlah','harga (Rp.)'])
    df

harga1=2000
harga2=3000
harga3=2000
harga4=2000
harga5=2000
hitung1=(harga1*number1)+(harga2*number2)+(harga3*number3)+(harga4*number4)+(harga5*number5)
if hitung1<20000:
        st.write("total harga makanan Rp.",hitung1)
if hitung1>20000:
    hitung1=hitung1-0.1*hitung1
    st.write("Diskon 10% total harga makanan Rp.",hitung1)

def pesanan(pilihan,namapel,kelas,tanggal,number1,number2,number3,number4,number5,number6):
    return db.put({"Pengambilan":pilihan,"Nama":namapel,"Kelas":kelas,"Tanggal":tanggal,"Donat":number1,"Piscok":number2,"Kue Sus":number3,"Kue susu":number4,"Pie buah":number5,"Bomboloni":number6})

pesanan(pilihan,nama,kelas,tanggal,number1,number2,number3,number4,number5,number6)    


