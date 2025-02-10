import re

class RegistrasiEmail:
    def __init__(self):
        self._pengguna = {}
        self._pengguna_terdaftar = []
        self._pengguna_masuk = None
        self._percobaan_masuk = {}

    def _validasi_email(self, email):
        pola = r'^[a-zA-Z0-9]+@sdt.ac.id$'
        if re.match(pola, email):
            return True
        else:
            return False

    def daftar_email(self):
        email = input("Masukkan email baru Anda: ")
        while not self._validasi_email(email):
            print("Email tidak valid, silakan coba lagi sesuai aturan.")
            email = input("Masukkan email baru Anda: ")
        password = input("Masukkan password baru Anda: ")
        self._pengguna[email] = password
        self._pengguna_terdaftar.append(email)
        print("Registrasi email baru berhasil.")

    def masuk_email(self):
        email = input("Masukkan email Anda: ")
        while not self._validasi_email(email):
            print("Email tidak valid, silakan coba lagi.")
            email = input("Masukkan email Anda: ")
        if email not in self._pengguna:
            print("Email belum terdaftar.")
            pilih = input("Apakah Anda ingin mendaftar email baru? (y/t): ")
            if pilih.lower() == "y":
                self.daftar_email()
            else:
                return
            
        max_attempts = 3
        attempt = 0
        while attempt < max_attempts:
            password = input("Masukkan password Anda: ")
            if self._pengguna[email] == password:
                print("Masuk email berhasil.")
                self._pengguna_masuk = email
                break
            else:
                attempt += 1
                remaining_attempts = max_attempts - attempt
                if remaining_attempts > 3:
                    print(f"Password salah. Anda memiliki {remaining_attempts} percobaan tersisa.")
                else:
                    print("Anda telah melebihi batas percobaan masuk. Silakan coba lagi.")

                print("Batas percobaan masuk telah tercapai. Silakan coba lagi nanti.")

    def jalankan(self):
        print("""
        =====================================================================================================
        Selamat datang di program sederhana registrasi email @sdt.ac.id
        Aturan:
        1. Lakukan registrasi pembuatan email baru terlebih dahulu jika Anda belum memiliki email baru.
        2. Nama pengguna (username) hanya boleh menggunakan huruf a-z, A-Z, atau angka 0-9.
        3. Pastikan saat membuat email baru, setelah nama pengguna menggunakan alamat email @sdt.ac.id.
        4. Setelah membuat email baru, silakan masuk.
        5. Jika masuk berhasil, Anda dapat keluar dari program.
        =====================================================================================================
        """)
        print()

        while True:
            print("1. Registrasi email baru")
            print("2. Masuk dengan email yang sudah ada")
            print("3. Keluar")
            pilih = input("Pilih menu: ")
            if pilih == "1":
                self.daftar_email()
            elif pilih == "2":
                self.masuk_email()
            elif pilih == "3":
                print("Terima kasih telah menggunakan program sederhana ini.")
                break
            else:
                print("Pilihan tidak valid.")


class RegistrasiEmailLanjutan(RegistrasiEmail):
    def __init__(self):
        super().__init__()
        self._pengguna_premium = []
        self._pesan_masuk = {}

    def daftar_email(self):
        email = input("Masukkan email baru Anda: ")
        while not self._validasi_email(email):
            print("Email tidak valid, silakan coba lagi sesuai aturan.")
            email = input("Masukkan email baru Anda: ")

        if email in self._pengguna_terdaftar:
            print("Email sudah terdaftar.")
            return

        password = input("Masukkan password baru Anda: ")
        self._pengguna[email] = password
        self._pengguna_terdaftar.append(email)
        print("Registrasi email baru berhasil.")

    def naik_premium(self):
        if self._pengguna_masuk in self._pengguna_terdaftar and self._pengguna_masuk not in self._pengguna_premium:
            self._pengguna_premium.append(self._pengguna_masuk)
            print("Naik ke akun premium berhasil.")
        else:
            print("Anda belum masuk atau belum menjadi pengguna premium.")   

    def ganti_password(self):
        if self._pengguna_masuk in self._pengguna_terdaftar:
            password_lama = input("Masukkan password lama Anda: ")
            if self._pengguna[self._pengguna_masuk] == password_lama:
                password_baru = input("Masukkan password baru Anda: ")
                self._pengguna[self._pengguna_masuk] = password_baru
                print("Password berhasil diubah.")
            else:
                print("Password lama salah.")
        else:
            print("Anda belum masuk.")

    def kirim_pesan(self):
        if self._pengguna_masuk in self._pengguna_terdaftar and self._pengguna_masuk in self._pengguna_premium:
            penerima = input("Masukkan email penerima: ")
            pesan = input("Masukkan pesan: ")
            if penerima in self._pengguna_terdaftar:
                if penerima in self._pesan_masuk:
                    self._pesan_masuk[penerima].append(pesan)
                else:
                    self._pesan_masuk[penerima] = [pesan]
                print("Pesan berhasil dikirim.")
            else:
                print("Email penerima tidak terdaftar.")
        else:
            print("Anda belum masuk atau belum menjadi pengguna premium.")

    def lihat_pesan(self):
        if self._pengguna_masuk in self._pengguna_terdaftar and self._pengguna_masuk in self._pengguna_premium:
            if self._pesan_masuk:
                print("Pesan yang masuk:")
                for penerima, pesan in self._pesan_masuk.items():
                    print(f"Email: {penerima}")
                    for p in pesan:
                        print(f"Pesan: {p}")
                    print("----------")
            else:
                print("Tidak ada pesan yang masuk.")
        else:
            print("Anda belum masuk atau belum menjadi pengguna premium.")
    
    def kelola_pengguna(self):
        if self._pengguna_masuk in self._pengguna_terdaftar and self._pengguna_masuk in self._pengguna_premium:
            print("Daftar Pengguna Terdaftar:")
            for email in self._pengguna_terdaftar:
                print(f"- {email}")
        else:
            print("Anda belum masuk atau belum menjadi pengguna premium.")

    def jalankan(self):
        print("""
        =====================================================================================================
        Selamat datang di program sederhana registrasi email @sdt.ac.id
        Aturan:
        1. Lakukan registrasi pembuatan email baru terlebih dahulu jika Anda belum memiliki email baru.
        2. Nama pengguna (username) hanya boleh menggunakan huruf a-z, A-Z, atau angka 0-9.
        3. Pastikan saat membuat email baru, setelah nama pengguna menggunakan alamat email
        4. Setelah membuat email baru, silakan masuk.
        5. Jika masuk berhasil, Anda dapat keluar dari program.
        6. Pengguna yang telah masuk dapat naik ke akun premium.
        7. Pengguna yang telah masuk dapat mengganti password.
        8. Pengguna premium dapat mengirim dan melihat pesan masuk.
        9. Pengguna premium dapat melihat daftar pengguna terdaftar.
        =====================================================================================================
        """)

        while True:
            print()
            print("1. Registrasi email baru")
            print("2. Masuk dengan email yang sudah ada")
            print("3. Naik ke akun premium")
            print("4. Ganti password")
            print("5. Kirim pesan")
            print("6. Lihat pesan masuk")
            print("7. Kelola pengguna terdaftar")
            print("8. Keluar")
            pilih = input("Pilih menu: ")

            if pilih == "1":
                self.daftar_email()
            elif pilih == "2":
                self.masuk_email()
            elif pilih == "3":
                self.naik_premium()
            elif pilih == "4":
                self.ganti_password()
            elif pilih == "5":
                self.kirim_pesan()
            elif pilih == "6":
                self.lihat_pesan()
            elif pilih == "7":
                self.kelola_pengguna()
            elif pilih == "8":
                print("Terima kasih telah menggunakan program sederhana ini.")
                break
            else:
                print("Pilihan tidak valid.")

email_reg = RegistrasiEmailLanjutan()
email_reg.jalankan()