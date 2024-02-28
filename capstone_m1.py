

# CAPSTONE 1 IMAM HIDAYAT JCDS-0308 ON CAMPUS BANDUNG
# CAPSTONE  PROJECT DATA RUMAH SAKIT

#===============================================================================================

# Database dalam dictionary

# DICTIONARY

data_pasien = {
    'A01':{'nama pasien':'reinhard','umur':28,'alamat':'jl helvetia','jenis kelamin':'laki-laki','jenis penyakit':'paru'},
    'A02':{'nama pasien':'antony','umur':33,'alamat':'jl pondok','jenis kelamin':'laki-laki','jenis penyakit':'jantung'},
    'A03':{'nama pasien':'ratna','umur':24,'alamat':'jl mencirim','jenis kelamin':'perempuan','jenis penyakit': 'jantung'},
    'A04':{'nama pasien':'melisa','umur':40,'alamat':'jl rambung','jenis kelamin':'perempuan','jenis penyakit': 'paru'},
    'A05':{'nama pasien':'hartanta','umur':26,'alamat':'jl venus','jenis kelamin':'laki-laki' , 'jenis penyakit': 'demam tinggi'},
}

data_nakes = {
    '01':{'nama nakes':'dr boni','umur':36,'alamat':'jl soeta','jenis kelamin':'laki-laki','bidang':'paru'},
    '02':{'nama nakes':'dr ika','umur':29,'alamat':'jl bumi','jenis kelamin':'perempuan','bidang':'umum'},
    '03':{'nama nakes':'dr asraf','umur':42,'alamat':'jl langkat','jenis kelamin':'laki-laki','bidang':'jantung'},
    '04':{'nama nakes':'dr haris','umur':28,'alamat':'jl langit','jenis kelamin':'laki-laki','bidang':'ginjal'},
    '05':{'nama nakes':'dr andi','umur':51,'alamat':'jl angkasa','jenis kelamin':'laki-laki','bidang':'tht'},     
}


# #========================================= FUNGSI BACA ============================================


def baca_pasien():   # fungsi baca data pasien 
    for key , value in data_pasien.items():  
     print(key,value['nama pasien'],value['umur'],value['alamat'],value['jenis kelamin'],value['jenis penyakit'])

def baca_nakes():      # fungsi baca data Nakes
    for key , value in data_nakes.items():
     print(key,value['nama nakes'],value['umur'],value['alamat'],value['jenis kelamin'],value ['bidang'])

def baca_utama():          # fungsi yg dipakai untuk memilih menu utama
    user_input = input( 'Pilih baca data pasien / Baca data nakes (1/2) = ') 
    print()
    if user_input == '1':
        baca_pasien()
    elif user_input == '2':
        baca_nakes()
    

# #============================================ FUNGSI DELETE ===================================== 
        
def delete_pasien(): # fungsi hapus data pasien
    baca_pasien()
    print('\n')
    user_delete = input('pilih data pasien yang akan di hapus = ')
    if user_delete in  data_pasien :
       print("Data ditemukan dan berhasil dihapus \n")
       del data_pasien [user_delete]
       baca_pasien()

def delete_nakes():  # fungsi hapus data nakes
    baca_nakes()
    print('\n')
    user_delete = input('pilih data  Nakes yang akan di hapus = ')
    if user_delete in  data_nakes :
       print("Data ditemukan dan berhasil dihapus \n")
       del data_nakes [user_delete]
       baca_nakes()

def delete_utama():  # fungsi yg dipakai untuk memilih menu delete
    user_input = input( 'pilih delete data pasien / delete data nakes (1/2) = ') 
    if user_input == '1':
        delete_pasien()
    elif user_input == '2':
        delete_nakes()

#============================================== FUNGSI CREATE ===================================  

# TAMBAH DATA PASIEN

def tambah_pasien(): 
    id = input(' Masukkan id pasien : ')
    nama = input (' Masukkan nama pasien : ')
    umur = int(input(' Masukkan umur pasien : '))
    alamat = input(' Masukkan alamat pasien : ')
    jenis_kelamin = input(' Masukkan jenis kelamin pasien : ')
    jenis_penyakit = input ( ' Masukkan jenis penyakit pasien : ')
    konfirmasi_user = input(' Apakah data sudah benar (benar/salah) : ')

    if konfirmasi_user.lower() == 'benar':
        

        data_pasien[id] = {
            'id': id,
            'nama pasien': nama ,
            'umur': umur,
            'alamat': alamat,
            'jenis kelamin': jenis_kelamin,
            'jenis penyakit': jenis_penyakit,
            'konfirmasi user': konfirmasi_user
        }

        print('\n Data pasien berhasil di input')
    else: 
        print('\n Input ulang kembali data pasien ')

# TAMBAH DATA NAKES 

def tambah_nakes():
    id = input (' Masukkan id nakes : ')
    nama = input (' Masukkan nama nakes : ')
    umur = int(input(' Masukkan umur nakes : '))
    alamat = input(' Masukkan alamat nakes : ')
    jenis_kelamin = input(' Masukkan jenis kelamin nakes : ')
    bidang = input ( ' Masukkan bidang penyakit nakes : ')
    konfirmasi_user = input(' Apakah data sudah benar (benar/salah) : ')

    if konfirmasi_user.lower() == 'benar':
        

        data_nakes[id] = {
            'id': id,
            'nama nakes': nama ,
            'umur': umur,
            'alamat': alamat,
            'jenis kelamin': jenis_kelamin,
            'bidang': bidang,
            'konfirmasi_user': konfirmasi_user,
        }

        print('\n Data nakes berhasil di input')
    else: 
        print('\n Input ulang kembali data nakes ')

# fungsi tambah utama data rumah sakit imam medica
        
def tambah_utama():
    user_input = input( 'Pilih tambah data pasien / tambah data nakes (1/2) = ') 
    if user_input == '1':
        tambah_pasien()
    elif user_input == '2':
        tambah_nakes()


#============================================ FUNGSI UPDATE ======================================

#  fungsi update data pasien


def update_data_pasien():
    while True :
        print('   MASUKKAN PILIHAN : \n ')
        print('1. Memperbaharui data pasien berdasarkan ID')
        print('2. Memperbaharui data nakes berdasarkan ID\n')
        show_1 = input('Masukkan pilihan anda : ')
        if show_1 =='1' : 
            baca_pasien()
            id_update = input('silahkan masukkan id pasien yang akan diperbaharui : ').title()
            if id_update in data_pasien :
                print()
                print('Silahkan pilih jenis data pasien yang akan di ubah : \n')
                print('1. Nama Pasien')
                print('2. Umur')
                print('3. Alamat')
                print('4. Jenis Kelamin')
                print('5. Jenis Penyakit')
                show_2 = input(' masukkan pilian anda : ')
                print()
                if show_2=='1':
                    nama_update = 'nama pasien'
                    data_pasien[id_update][nama_update]= input('Nama yang akan disimpan : ')
                    baca_pasien()
                    break
                elif show_2=='2':
                    umur_update = ('umur')
                    data_pasien[id_update][umur_update]= input('Umur baru yang ingin disimpan  : ')
                    baca_pasien()
                    break
                elif show_2=='3':
                    alamat_update = ('alamat')
                    data_pasien[id_update][alamat_update] = input('Alamat yang akan disimpan  : ')
                    baca_pasien()
                    break
                elif show_2=='4':
                    jenis_kelamin_update = ('jenis kelamin')
                    data_pasien[id_update][jenis_kelamin_update]=input('Jenis kelamin yang akan disimpan : ')
                    baca_pasien()
                    break
                if show_2=='5':
                    jenis_penyakit_pasien_update =  ('jenis penyakit')
                    data_pasien[id_update][jenis_penyakit_pasien_update] = input('Jenis penyakit yang akan disimpan : ')
                    baca_pasien()
                    break

 #  fungsi update data nakes    
                
        elif show_1 =='2' : 
                baca_nakes()
                id_update = input('silahkan masukkan id nakes yang akan diperbaharui : ').title()
                if id_update in data_nakes :
                    print(' silahkan pilih jenis data pasien yang akan di ubah : ')
                    print('1. Nama nakes')
                    print('2. Umur')
                    print('3. Alamat')
                    print('4. Jenis Kelamin')
                    print('5. Bidang nakes')
                    show_2 = input('Masukkan pilian anda : ')
                    print('\n')
                    if show_2=='1':
                        nama_update = 'nama nakes'
                        data_nakes[id_update][nama_update]= input('Nama yang akan disimpan : ')
                        print()
                        baca_nakes()
                        break
                    elif show_2=='2':
                        umur_update = ('umur')
                        data_nakes[id_update][umur_update]= input('Umur baru yang ingin disimpan  : ')
                        baca_nakes()
                        break
                    elif show_2=='3':
                        alamat_update = ('alamat')
                        data_nakes[id_update][alamat_update] = input('Alamat yang akan disimpan  : ')
                        baca_nakes()
                        break
                    elif show_2=='4':
                        jenis_kelamin_update = ('jenis kelamin')
                        data_nakes[id_update][jenis_kelamin_update]=input('Jenis kelamin yang akan disimpan : ')
                        baca_nakes()
                        break
                    if show_2=='5':
                        bidang_nakes_update =  ('jenis penyakit')
                        data_nakes[id_update][bidang_nakes_update] = input('Bidang nakes yang akan disimpan : ')
                        baca_nakes()
                        break
            
#========================================== FUNGSI SORTING ======================================


# fungsi untuk melihat data pasien tertentu
                    
def sorting_pasien():
    id_pasien = input('Masukkan id pasien yang ingin dilihat : ').title()
    found = False
    for key , value in data_pasien.items():
         if id_pasien ==key:
            found = True
            print(key,value['nama pasien'],value['umur'],value['alamat'],value['jenis kelamin'],value['jenis penyakit'])
    if  not found :
        print('Id tidak ditemukan, silahkan coba lagi dengan Id yang benar')
    


 # fungsi untuk melihat data nakes tertentu                  

def sorting_nakes():
    id_nakes = input('Masukkan id nakes yang ingin dilihat : ').title()
    found = False
    for key , value in data_nakes.items():
         if id_nakes ==key:
            found=True
            print(key,value['nama nakes'],value['umur'],value['alamat'],value['jenis kelamin'],value ['bidang'])
    if  not found :
        print('Id tidak ditemukan, silahkan coba lagi dengan Id yang benar')
    

# menu utama melihat data pasien/nakes utama
            
def sorting_utama():
    user_input_sorting = input( 'Pilih sorting data pasien / data nakes (1/2) = ') 
    print()
    if user_input_sorting == '1':
        sorting_pasien()
    elif user_input_sorting == '2':
        sorting_nakes()
    

#=============================================== MENU UTAMA ==================================

# menu pilihan utama program rs imam medica

while True:
    
    print('='*80)
    print()
    print(' SELAMAT DATANG DI')
    print(' RUMAH SAKIT IMAM MEDICA')
    print()
    print('='*80)
    print()
    print('PILIHAN MENU :') 
    print()
    print('A. Lihat Data Pasien / Data Nakes')
    print('B. Input Data Pasien Baru / Data Nakes Baru')
    print('C. Memperbaharui Data Pasien / Data Nakes')
    print('D. Delete Data Pasien / Data Nakes')
    print('E. Lihat data pasien / Data nakes tertentu')
    print('F. Keluar Program')
    print('-'*80)
    print()
        
    menu = input('Masukkan pilihan untuk memilih program diatas (A/B/C/D/E) = ').lower()
    print()
    if menu =='a':
        baca_utama()
    elif menu =='b':
        tambah_utama()
    elif menu =='c':
        update_data_pasien()
    elif menu =='d':
        delete_utama()
    elif menu =='e':
        sorting_utama()
    elif menu =='f':
        print ('TERIMAKASIH MENJUAH JUAH')
        break

    
# ===================================================== GREAT REGARDS ======================================
