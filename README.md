# Acu-Frend 1.0

## Deskripsi
**Acu-Frend 1.0** adalah sebuah tool pendukung yang dirancang untuk membantu pengguna dalam membuat *template CSV target* bagi **Acunetix**. Dengan tool ini, pengguna dapat dengan mudah menyusun, mengelola, serta mengekspor daftar target sesuai format standar yang dibutuhkan oleh Acunetix. 

Tujuan utama dari aplikasi ini adalah mempersingkat waktu dan meminimalisir kesalahan manual ketika membuat daftar target secara masif.

---

## Fitur Utama
- Membuat file CSV target dengan format standar Acunetix.
- Mendukung input file berupa daftar URL (*targets.txt*).
- Menambahkan parameter:
  - **Profil Pemindaian** (*Scan Profile*).
  - **Tingkat Kritisitas** (*Criticality*).
  - **Grup Target** (*Target Group*).
- Opsi untuk menambahkan atau menghilangkan baris header CSV.
- Opsi *force overwrite* untuk menimpa file output yang sudah ada.
- Validasi URL otomatis (hanya menerima format `http://` atau `https://`).

---

## Instalasi
1. Pastikan Python 3 sudah terinstal.
2. Clone repository ini atau salin file Python ke dalam direktori lokal.
3. Instal dependensi yang dibutuhkan:
   ```bash
   pip install colorama
   ```

---

## Cara Penggunaan
Jalankan perintah berikut di terminal:

```bash
python acufrend.py INPUT_FILE [opsi]
```

### Argumen dan Opsi
- **INPUT_FILE**: Jalur ke file `targets.txt` yang berisi daftar URL.
- `-o`, `--output`: Jalur ke file CSV output (default: `acunetix_targets.csv`).
- `-p`, `--profile`: Nama profil pemindaian (default: `Default Scan`).
- `-c`, `--criticality`: Tingkat kritisitas target (default: `High`). Pilihan: `High`, `Medium`, `Low`.
- `-g`, `--group`: Nama grup target (default: `Default Group`).
- `--no-header`: Jangan tambahkan baris header di file CSV.
- `-f`, `--force`: Timpa file output yang sudah ada tanpa konfirmasi.

### Contoh
1. Membuat CSV sederhana dengan parameter default:
   ```bash
   python acufrend.py targets.txt
   ```

2. Menentukan nama file output dan profil pemindaian:
   ```bash
   python acufrend.py targets.txt -o hasil.csv -p "Full Scan"
   ```

3. Membuat CSV tanpa header:
   ```bash
   python acufrend.py targets.txt --no-header
   ```

4. Menimpa file output tanpa konfirmasi:
   ```bash
   python acufrend.py targets.txt -f
   ```

---

## Struktur Output CSV
Format file CSV yang dihasilkan:

| Target_URL | Scan_Profile   | Criticality | Target_Group   |
|------------|---------------|-------------|----------------|
| http://... | Default Scan  | High        | Default Group  |

---

## Catatan
- Hanya URL yang valid dengan awalan `http://` atau `https://` yang akan diproses.
- URL tidak valid akan dilewati secara otomatis.

---

## Lisensi
Proyek ini dirilis dengan lisensi **MIT License**. Silakan gunakan, modifikasi, dan distribusikan sesuai kebutuhan.
