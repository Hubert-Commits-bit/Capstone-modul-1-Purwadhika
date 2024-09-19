def tampilkan_menu():
    print("Pilihan Menu Pengelolaan Nilai:")
    print("1. Lihat Semua Nilai Siswa")
    print("2. Tambah Nilai Siswa Baru")
    print("3. Update Nilai Siswa")
    print("4. Hapus Data Nilai Siswa")
    print("5. Keluar dari Program")
def tampilkan_data_nilai(data_nilai):
  if data_nilai:
        print("Daftar Nilai Siswa:")
        for index, (nama, nilai) in enumerate(data_nilai.items(), 1): 
            uts = nilai['UTS']
            uas = nilai['UAS']
            rata2 = (uts * 0.4) + (uas * 0.6)  
            print(f"{index}. {nama} - UTS: {uts}, UAS: {uas}, Rata-rata: {rata2:.2f}")
  else:
        print("Belum ada data.")
def tambahkan_data_nilai(data_nilai):
    nama = input("Nama siswa yang ingin ditambahkan: ")  
    uts = float(input(f"Masukkan nilai UTS untuk {nama}: "))  
    uas = float(input(f"Masukkan nilai UAS untuk {nama}: "))  
    data_nilai[nama] = {'UTS': uts, 'UAS': uas} 
    print(f"Berhasil! Nilai untuk {nama} sudah ditambahkan.")

def perbarui_data_nilai(data_nilai):
  nama = input("Masukkan Nama Siswa yang ingin diperbarui: ")
  if nama in data_nilai:
       uts = float(input(f"Masukkan nilai UTS baru untuk {nama}: "))
       uas = float(input(f"Masukkan nilai UAS baru untuk {nama}: "))
       data_nilai[nama] = {'UTS': uts, 'UAS': uas}  
       print(f"Nilai  {nama} berhasil diupdate.")
  else:
       print("Data siswa tdk ketemu.")

def hapus_data_nilai(data_nilai):
    nama = input("Masukkan Nama Siswa yang ingin dihapus: ")
    if nama in data_nilai:
        del data_nilai[nama]  
        print(f"Data nilai siswa atas nama {nama} telah dihapus.")
    else:
        print("Data siswa tdk ketemu.")


def keluar_program():
    konfirmasi_keluar = input("Apakah yakin ingin keluar? (yes/no): ")
    if konfirmasi_keluar.lower() == 'yes':
        print("Anda berhasil keluar :).")
        return True
    else:
        return False

def main():
    data_nilai = {}
    while True:
        tampilkan_menu()
        pilihan = input("Pilih : ")
        
        if pilihan == '1':
            tampilkan_data_nilai(data_nilai)
        elif pilihan == '2':
            tambahkan_data_nilai(data_nilai)
        elif pilihan == '3':
            perbarui_data_nilai(data_nilai)
        elif pilihan == '4':
            hapus_data_nilai(data_nilai)
        elif pilihan == '5':
            if keluar_program():
                break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
