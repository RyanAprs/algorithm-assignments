print("==============================KELOMPOK 4==============================")

print("ANGGOTA:")

print("1. FAUZAAN RAFI PUTRA ABDULLAH (0060)")
print("2. FERRY KURNIAWAN (0063)")
print("3. ALVIYANT RIZQI MAULANA (0070)")
print("4. ALIF RAJA FATAHILLAH (0074)")
print("5. RYAN ADI PRASETYO (0080)")
print("6. IRSYAD MUHAMAD FIRDAUS (0083)")

print("======================================================================")

from datetime import datetime, timedelta

tanggal_sekarang = datetime.today()

# ARRAY MAHASISWA
mahasiswa = [
    {"Nama": "Fery", "Npm": 63},
    {"Nama": "Alif", "Npm": 74},
    {"Nama": "Ojan", "Npm": 60},
    {"Nama": "Irsyad", "Npm": 83},
    {"Nama": "Alviyant", "Npm": 70},
    {"Nama": "Ryan", "Npm": 80},
]

# ARRAY PEMINJAM
data_peminjaman = []

# ARRAY KATALOG BUKU
Buku = [
    {"isbn": 12,"judul" : "Merenung dalam kesunyian", "tahun terbit" : 2019, "penerbit" : "Ferry", "stok" : 5},
    {"isbn": 98,"judul" : "Pake Nanya", "tahun terbit" : 2020, "penerbit" : "Ryukoshi", "stok" : 3},
    {"isbn": 67,"judul" : "Waduh", "tahun terbit" : 2010, "penerbit" : "El psy congroo", "stok" : 1},
    {"isbn": 34,"judul" : "AFTER DARK", "tahun terbit" : 2023, "penerbit" : "Kurisu", "stok" : 7},
    {"isbn": 78,"judul" : "AFTER LIGHT", "tahun terbit" : 2022, "penerbit" : "Takamoyo", "stok" : 0}
]

# ARRAY HISTORY
data_history_peminjaman = []

while True:
    print("\n========================================")
    print("\n           MENU UTAMA                ")
    print("\n========================================")
    print("1. Data Mahasiswa/Peminjam")
    print("2. Data Katalog Buku")
    print("3. Data Transaksi Peminjaman")
    print("4. Data History Peminjaman dan Pengembalian")
    choice = input("masukkan pilihan anda: ")

    if choice.isdigit():
        choice = int(choice)

        
# MAHASISWA
        if choice == 1 :
        # FUNGSI TAMBAH MAHASISWA
                def tambah_mahasiswa(npm):
                    for i in mahasiswa:
                        if i["Npm"] == npm:
                            return False
                        
                    return True

            # FUNGSI EDIT MAHASISWA
                def edit_mahasiswa(validate_npm):
                    for i in mahasiswa:
                        if i["Npm"] == validate_npm:
                            nama_baru = input("Masukkan nama yang baru: ")
                            validate = input("Apakah Anda yakin akan mengganti " + i['Nama'] + "?" + " dengan " + (nama_baru) + "(y/n): ")
                            if validate.lower() == "y":
                                i["Nama"] = nama_baru
                                print("Mahasiswa berhasil diedit")
                            else:
                                print("Perubahan dibatalkan")
                            break
                    else:
                        print("Mahasiswa tidak ditemukan")

            # FUNGSI HAPUS MAHASISWA
                def hapus_mahasiswa(validate_npm):
                    for i in mahasiswa:
                        if i["Npm"] == validate_npm:
                            validate = input("Apakah Anda yakin akan menghapus " + i['Nama'] + "? (y/n): ")
                            if validate.lower() == "y":
                                mahasiswa.remove(i)
                                print("Mahasiswa berhasil dihapus")
                            else:
                                print("Penghapusan dibatalkan")
                            break
                    else:
                        print("Mahasiswa tidak ditemukan")


                while True:
                    print("\n========================================")
                    print("            MENU MAHASISWA                ")
                    print("========================================")
                    print("1. Tampil Mahasiswa")
                    print("2. Tambah Mahasiswa")
                    print("3. Edit Mahasiswa")
                    print("4. Hapus Mahasiswa")
                    print("5. Kembali ke Menu Utama")
                    choose = input("Masukkan pilihan Anda: ")

                    if choose.isdigit():
                        choose = int(choose)

                        if choose == 1:
                            print("\nDaftar Mahasiswa: ")
                            for i in range(len(mahasiswa)):
                                mhs = mahasiswa[i]
                                print("||" + str(i + 1) + ". || Npm: " + str(mhs["Npm"]) + " || Nama: " + mhs["Nama"] + " ||")

                        elif choose == 2:
                            print("\n")
                            while True:
                                npm = input("Masukkan Npm Mahasiswa :")
                                if npm.isdigit():
                                    break
                                else:
                                    print("Masukkan angka")
                            if tambah_mahasiswa(npm):
                                nama = input("Masukkan nama mahasiswa: ")
                                mahasiswa.append({"Nama": nama, "Npm": npm})
                                print("Tambah data berhasil")
                            else:
                                print("Data dengan npm " + str(npm) + " sudah digunakan")

                        elif choose == 3:
                            while True:
                                validate_npm = input("Masukkan Npm yang akan diedit: ")
                                if validate_npm.isdigit():
                                    edit_mahasiswa(int(validate_npm))
                                    break
                                else:
                                    print("Masukkan angka")


                        elif choose == 4:
                            while True:
                                validate_npm = input("Masukkan Npm yang akan diedit: ")
                                if validate_npm.isdigit():
                                    hapus_mahasiswa(int(validate_npm))
                                    break
                                else:
                                    print("Masukkan angka")

                        elif choose == 5:
                            break
                        else:
                            print("Masukkan nomor dengan benar")
                    else: 
                        print("Masukkan Nomor Yang Sesuai!!")

# KATALOG BUKU
        elif choice == 2:       
                # Fungsi Menambahkan Buku
                def tambah_buku(ISBN):
                    for x in Buku:
                        if x['isbn'] == ISBN:
                            print("Buku tidak bisa ditambahkan, ISBN TIDAK BOLEH SAMA")
                            break
                    else :
                        judul = input("Judul Buku :")
                        penerbit = input("Penerbit Buku :")
                        while True:
                            tahun = input("Tahun terbit Buku :")
                            if tahun.isdigit():
                                break
                            else:
                                print("Masukkan angka")
                        while True:
                            stokbuku = input("Jumlah buku yang ingin dimasukkan: ")
                            if stokbuku.isdigit():
                                print("Buku Berhasil Ditambahkan")
                                break
                            else:
                                print("Masukkan angka")


                    Buku.append({"isbn": ISBN, "judul" : judul, "penerbit" : penerbit, "tahun terbit" : tahun, "stok" : stokbuku })

                # Fungsi Edit Buku
                def edit_buku(validate_isbn):
                    for x in Buku :
                        if x['isbn'] == validate_isbn:
                            print(f"Isbn : {x['isbn']} || Judul : {x['judul']} || Tahun terbit : {x['tahun terbit']} || Penerbit : {x['penerbit']} || Stok : {x['stok']}")
                            found = True
                            judul_baru = input("Masukkan judul buku yang baru :")
                            while True:
                                tahunTerbit_baru = input("tahun terbit Buku :")
                                if tahunTerbit_baru.isdigit():
                                    break
                                else:
                                    print("Masukkan angka")
                            penerbit_baru = input("Masukkan Penerbit yang baru :")
                            while True:
                                stok_baru = input("Jumlah buku yang ingin dimasukkan: ")
                                if stok_baru.isdigit():
                                    print("Buku Berhasil Ditambahkan")
                                    break
                                else:
                                    print("Masukkan angka")
                            validate = input(f"Apakah anda yakin ingin mengganti data buku dengan nomor ISBN {validate_isbn}, dengan data buku yang baru saja dimasukkan? (y/n) :")
                            if validate.lower() == 'y':
                                x['judul'] = judul_baru
                                x['tahun terbit'] = tahunTerbit_baru
                                x['penerbit' ] = penerbit_baru
                                x['stok'] = stok_baru
                                print(f"Data buku dengan nomor ISBN {validate_isbn} telah berhasil diubah")
                                break
                            elif validate.lower() == 'n':
                                print(f"Perubahan data buku dengan nomor ISBN {validate_isbn} dibatalkan")
                                break
                            else:
                                print("Masukkan pilihan yang sesuai")
                    else:
                            print(f"Daftar buku dengan nomor ISBN {validate_isbn} tidak ditemukan.")
                
                # FUNGSI PENGHAPUSAN BUKU
                def hapus_buku(validate_isbn):
                    for x in Buku:
                        if x['isbn'] == validate_isbn :
                            if x['stok'] < 1 :
                                print("Buku sedang dipinjam")
                                print("Penghapusan buku dibatalkan")
                                break
                            else:
                                validate = input(f"Apakah anda yakin ingin menghapus buku dengan nomor Isbn {validate_isbn}? (y/n) :")
                                if validate.lower() == 'y':
                                    Buku.remove(x)
                                    print("Buku berhasil dihapus")
                                    break
                                elif validate.lower() == 'n':
                                    print("Penghapusan dibatalkan")
                                    break
                                else:
                                    print("Masukkan pilihan yang sesuai")
                    else:
                        print(f"Buku dengan nomor Isbn \'{validate_isbn}' tidak ditemukan. ")



                while True : 
                    print("\n========================================")
                    print("         MENU KATALOG BUKU                ")
                    print("========================================")
                    print("1. Tampil buku")
                    print("2. Tambah buku")
                    print("3. Edit buku")
                    print("4. Hapus buku")
                    print("5. Kembali ke menu utama")
                    pilih = input("Masukkan pilihan anda : ")

                    if pilih.isdigit():
                        pilih = int(pilih)

                        if pilih == 1 :
                            print("\n=====Daftar Buku=====")
                            for x in range(len(Buku)):
                                book = Buku[x]
                                print(f"|| {x+1}. || Isbn: {book['isbn']} || Judul: {str(book['judul'])} || Tahun terbit: {str(book['tahun terbit'])} || Penerbit: {str(book['penerbit'])} || Stok: {str(book['stok'])}. || ")

                        elif pilih == 2 :
                            print("\n=====Penambahan Buku=====")
                            while True:
                                ISBN = input("Masukkan Isbn Buku :")
                                if ISBN.isdigit():
                                    tambah_buku(int(ISBN))
                                    break
                                else:
                                    print("Masukkan angka")
                                                
                        elif pilih == 3:
                            print('\n=====Pengeditan data buku=====')
                            while True:
                                validate_isbn = input("Masukkan ISBN Buku: ")
                                if validate_isbn.isdigit():
                                    found = False
                                    edit_buku(int(validate_isbn))
                                    break
                                else:
                                    print("Masukkan angka")
                        
                        elif pilih == 4:
                            print('\n=====Penghapusan data buku=====')
                            while True:
                                validate_isbn = input("Masukkan Isbn Buku :")
                                if validate_isbn.isdigit():
                                    hapus_buku(int(validate_isbn))
                                    break
                                else:
                                    print("Masukkan angka")
                        
                        elif pilih == 5:
                            break
                        else:
                            print("Pilihlah nomor yang sesuai")
                    else:
                        print("Masukkan Nomor Yang Sesuai!!")
                        
# TRANSAKSI
        elif choice == 3:
            while True:
                print("\n========================================")
                print("         MENU TRANSAKSI                ")
                print("========================================")
                print("1. Daftar Peminjam Aktif")
                print("2. Tambah Peminjaman")
                print("3. Edit Peminjaman")
                print("4. Pengembalian")
                print("5. Hapus Peminjaman")
                print("6. Kembali ke Menu Utama")
                choose = input("Masukkan pilihan Anda: ")
                
                if choose.isdigit():
                    choose = int(choose)

                    if choose == 1:
                        print("\n Daftar Peminjam Aktif:")
                        for i in range(len(data_peminjaman)):
                            data = data_peminjaman[i]

                            tanggal = tanggal_sekarang.day

                
                            tanggal_pinjam = datetime.strptime(data["Tanggal Pinjam"], "%d-%m-%Y")
                            print(type(tanggal_pinjam))
                            kembali_buku = tanggal_pinjam + timedelta(days=7)
                            tanggal_pengembalian = kembali_buku         
                            selisih_hari = (tanggal_sekarang - tanggal_pinjam).days
                            if selisih_hari > 7:
                                jml_keterlambatan = selisih_hari - 7
                                total_denda = jml_keterlambatan * 500
                                data["Denda"] = total_denda
                            else:
                                data["Denda"] = 0                    
                            print(str(i + 1) + "." + "Tanggal Pinjam : " + str(data["Tanggal Pinjam"]) + " | Nama : " + data["Nama Peminjam"] + " | Buku Yang Dipinjam : " + data["Buku Yang Dipinjam"] + "| Batas Tanggal Pengembalian : " + str(tanggal_pengembalian.strftime("%d-%m-%Y")) + "| Denda : " + str(data["Denda"]) + " | Status : " + data["Status"])
                            
                    elif choose == 2:
                        nama_peminjam = input("Masukkan nama peminjam: ")
                        for i in mahasiswa:
                            if i["Nama"] == nama_peminjam:
                                for j in data_peminjaman:
                                    if j["Nama Peminjam"] == nama_peminjam:
                                        print("Anda masih memiliki pinjaman buku:")
                                        print("Tanggal Pinjam: "+ str(j["Tanggal Pinjam"])+ " | Nama: "+ j["Nama Peminjam"]+ " | Buku Yang Dipinjam: "+ j["Buku Yang Dipinjam"]+ " | Batas Tanggal Pengembalian: "+ str(j["Batas Tanggal Pengembalian"])+ " | Denda: "+ str(j["Denda"])+ " | Status: "+ j["Status"])
                                        break
                                else:
                                    print("\nDaftar Buku")
                                    for x in range(len(Buku)):
                                        book = Buku[x]
                                        print(f"{x+1}. Isbn: {book['isbn']} || Judul: {str(book['judul'])} || Tahun terbit: {str(book['tahun terbit'])} || Penerbit: {str(book['penerbit'])} || Stok: {str(book['stok'])}. ")
                                    judul = input("Judul Buku yang akan dipinjam: ")
                                    for book in Buku:
                                        if book["judul"] == judul and book['stok'] >= 1 :
                                            stok = book["stok"]
                                            stok -= 1
                                            book['stok'] = stok
                                            valid_format = False

                                            while not valid_format:
                                                tanggal_peminjaman = input("Masukkan Tanggal peminjaman (contoh: 01-01-2023): ")
                                                try:
                                                    tanggal_pinjam = datetime.strptime(tanggal_peminjaman, "%d-%m-%Y")
                                                    # print(type(tanggal_pinjam))
                                                    valid_format = True
                                                except ValueError:
                                                    print("Format tanggal yang dimasukkan salah. Silahkan coba lagi")

                                            tanggal = tanggal_sekarang.day
                                            kembali_buku = tanggal_pinjam + timedelta(days=7)
                                            tanggal_pengembalian = kembali_buku
                                            
                                            if tanggal_sekarang < tanggal_pinjam:
                                                print("Tidak dapat melakukan peminjaman, karena tanggal yang dimasukkan melebihi tanggal", tanggal_sekarang)
                                                book["stok"] +=1
                                                break

                                            if tanggal_pengembalian.day > 30:
                                                tanggal_pengembalian -= timedelta(days=30)
                                                bulan = (tanggal_pengembalian.month % 12) + 1
                                                tahun = tanggal_pengembalian.year + (tanggal_pengembalian.month // 12)
                                                tanggal_pengembalian = tanggal_pengembalian.replace(day=30, month=bulan, year=tahun)
            
                                            status = "Di Pinjam"

                                            data_peminjaman.append({
                                                "Tanggal Pinjam": tanggal_peminjaman,
                                                "Nama Peminjam": nama_peminjam,
                                                "Buku Yang Dipinjam": judul,
                                                "Batas Tanggal Pengembalian": tanggal_pengembalian.strftime("%d-%m-%Y"),
                                                "Denda": 0,
                                                "Status": status
                                            })
                                            print("Pinjam Buku Berhasil")
                                            break    
                                    else:
                                        print("Buku Tidak Tersedia")
                                break
                        else:
                            print("Anda tidak terdaftar sebagai mahasiswa!")

                    elif choose == 3:
                        nama_peminjam = input("Masukkan nama peminjam: ")

                        for data in data_peminjaman:
                            if data["Nama Peminjam"] == nama_peminjam:
                                print("Data peminjaman sebelumnya:")
                                print("Tanggal Pinjam:", data["Tanggal Pinjam"])
                                print("Buku Yang Dipinjam:", data["Buku Yang Dipinjam"])

                                valid_format = False
                                while not valid_format:
                                    tanggal_pinjam_baru = input("Masukkan tanggal pinjam baru (contoh: 01-01-2023): ")
                                    try:
                                        tanggalPinjam = datetime.strptime(tanggal_pinjam_baru, "%d-%m-%Y")                                      
                                        valid_format = True
                                    except ValueError:
                                        print("Format tanggal yang anda masukkan salah. Silahkan coba lagi")
                                data["Tanggal Pinjam"] = tanggal_pinjam_baru
                                # print(type(data["Tanggal Pinjam"]))
                                kembali_buku = tanggalPinjam + timedelta(days=7)
                                tanggal_pengembalian = kembali_buku
                                data["Batas Tanggal Pengembalian"] = tanggal_pengembalian.strftime("%d-%m-%Y")
                                print("Peminjaman berhasil diubah")
                                break
                        else:
                            print("Peminjaman tidak ditemukan")

                    elif choose == 4:
                            # Pengembalian
                            nama_peminjam = input("Masukkan nama mahasiswa peminjam: ")

                            # Cari data peminjaman
                            for peminjaman in data_peminjaman:
                                if peminjaman["Nama Peminjam"] == nama_peminjam:
                                    peminjaman["status"] = "kembali"
                                    for buku in Buku:
                                        if buku["judul"] == peminjaman["Buku Yang Dipinjam"]:
                                            buku["stok"] += 1

                                    data_history_peminjaman.append(peminjaman)
                                    data_peminjaman.remove(peminjaman)

                                    print("Buku berhasil dikembalikan.")
                                    break
                            else:
                                print("Data mahasiswa peminjam tidak ditemukan.")
            
                    elif choose == 5:
                        nama = input("Masukkan nama peminjaman: ")

                        for i in data_peminjaman:
                            if i["Nama Peminjam"] == nama:
                                validate = input("Apakah Anda yakin akan menghapus " + i['Nama Peminjam'] + "? (y/n): ")
                                if validate.lower() == "y":
                                    data_peminjaman.remove(i)
                                    for buku in Buku:
                                        buku["stok"] += 1
                                    print("Peminjaman berhasil dihapus")
                                else:
                                    print("Penghapusan dibatalkan")
                                break
                        else:
                            print("Peminjaman tidak ditemukan")

                    elif choose == 6:
                        break

                    else:
                        print("Masukkan nomor dengan benar")
                else:
                    print("Masukkan Nomor Yang Sesuai!!")

# HISTORY
        elif choice == 4:
            print("\n========================================")
            print("   MENU RIWAYAT PEMINJAMAN                ")
            print("========================================")
            for i in range(len(data_history_peminjaman)):
                data = data_history_peminjaman[i]
                status = "Di Kembalikan"
                print(f"|| {i+1}. || Tanggal Pinjam: {data['Tanggal Pinjam']} || Nama: {data['Nama Peminjam']} || Buku Yang Dipinjam: {data['Buku Yang Dipinjam']} || Batas Tanggal Pengembalian: {data['Batas Tanggal Pengembalian']} || Tanggal Buku dikembalikan : {tanggal_sekarang.strftime('%d-%m-%Y')} || Denda: {data['Denda']} || Status: {status}")

        else:
            print("Masukkan nomor dengan benar")
    else:
        print("Masukkan Nomor Yang Sesuai!!")