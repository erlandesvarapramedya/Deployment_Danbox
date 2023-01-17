import streamlit as st

from deta import Deta

DETA_KEY="c05lph41_umJvMdPncrzTfw3dLRynCV8Fb8cQYEaq"

deta=Deta(DETA_KEY)

db=deta.Base("perlengkapan_db")

st.title("Danbox")
st.header("PERALATAN")
st.subheader('Perlengkapan Laboratorium')
from PIL import Image
import streamlit as st

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
st.subheader('Peralatan Laboratorium')

col7, col8, col9=st.columns(3)
with col7:
    st.subheader("Sarung Tangan")
    image = Image.open('gambar/sarung.jpg')
    st.image(image, width=150)
    import streamlit as st
    numberA = st.number_input('Jumlah sarung tangan',0)
    

with col8:
    st.subheader("Serbet")
    image = Image.open('gambar/serbet.jpg')
    st.image(image, width=150)
    import streamlit as st
    numberB = st.number_input('Jumlah serbet',0)
    
with col9:
    st.subheader("Tabung Reaksi")
    image = Image.open('gambar/reak.png')
    st.image(image, width=150)
    import streamlit as st
    numberC = st.number_input('Jumlah tabung reaksi',0)
    
col10, col11, col12=st.columns(3)
with col10:
    st.subheader("Gelas Piala")
    image = Image.open('gambar/piala.jpg')
    st.image(image, width=150)
    import streamlit as st
    numberD = st.number_input('Jumlah Gelas Piala',0)    
    besarr = st.selectbox(
            'Pilih Ukuran Gelas Piala (mL)',
                ('10', ' 25','50','100','150','200','250'))
    st.write('You selected:',besarr)
        
with col11:
    st.subheader("Tabung Ulir")
    image = Image.open('gambar/lir.jpg')
    st.image(image, width=150)
    import streamlit as st
    numberE = st.number_input('Jumlah tabung ulir',0)
    besar = st.selectbox(
            'Pilih Ukuran Tabung Ulir(mm)',
                ('13xH.100', '16xH.100','16xH.150','18xH.180','20xH.150','25xH.150','25xH.200'))
    st.write('You selected:', besar)
    
with col12:
        st.header("Gelas Ukur")
        image = Image.open('gambar/pia.jpg')
        st.image(image, width=150)
        import streamlit as st
        numberE = st.number_input('Jumlah Gelas Ukur',0)
        ukuran = st.selectbox(
            'Pilih Ukuran Gelas Ukur(mL)',
                ('10', ' 25','50','100','150','200','250'))
        st.write('You selected:', ukuran)
        
lab = st.button("rincian")
if lab:
    import pandas as pd
    hargaA=2000*numberA
    hargaB=5000*numberB
    hargaC=10000*numberC
    hargaD=20000*numberD
    hargaE=20000*numberE
    data = [['Sarung Tangan',numberA,hargaA],['Serbet',numberB,hargaB],['Tabung Reaksi',numberC,hargaC],['Gelas Piala',numberD,hargaD],['Tabung Ulir',numberE,hargaE]]
    df=pd.DataFrame(data,columns=['Perlengkapan','jumlah','harga (Rp.)'])
    df

hargaA=2000
hargaB=5000
hargaC=10000
hargaD=20000
hargaE=20000
hitung=(hargaA*numberA)+(hargaB*numberB)+(hargaC*numberC)+(hargaD*numberD)+(hargaE*numberE)
if hitung<30000:
        st.write("total harga perlengkapan Rp.",hitung)
if hitung>30000:
    hitung=hitung-0.1*hitung
    st.write("Diskon 10% total harga perlengkapan Rp.",hitung)
    
agree = st.checkbox('Saya setuju')
if agree:
    st.write('Terima kasih atas pesanannya!')
    
def pesanan(pilihan,namapel,kelas,tanggal,numberA,numberB,numberC,numberD,numberE):
    return db.put({"Pengambilan":pilihan,"Nama":namapel,"Kelas":kelas,"Tanggal":tanggal,"sarung tangan":numberA,"Serbet":numberB,"Tabung Reaksi ":numberC,"Gelas Piala ":numberD," Tabung Ulir":numberE})

pesanan(pilihan,nama,kelas,tanggal,numberA,numberB,numberC,numberD,numberE)

if st.button('KIRIM'):
    st.write('Pesanan Diterima')
else:
        st.write('Terimakasih Atas Pesanannya')
