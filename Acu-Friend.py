import csv
import argparse
import os
from colorama import Fore, Style, init

# Initialize colorama for automatic color reset
init(autoreset=True)

def create_banner():
    """
    Creates a left-aligned terminal banner with description.
    """
    banner_art = r"""
  ______                               ________            __                            __ 
 /      \                             /        |          /  |                          /  |
/$$$$$$  |  _______  __    __         $$$$$$$$/   ______  $$/   ______   _______    ____$$ |
$$ |__$$ | /       |/  |  /  | ______ $$ |__     /      \ /  | /      \ /       \  /    $$ |
$$    $$ |/$$$$$$$/ $$ |  $$ |/      |$$    |   /$$$$$$  |$$ |/$$$$$$  |$$$$$$$  |/$$$$$$$ |
$$$$$$$$ |$$ |      $$ |  $$ |$$$$$$/ $$$$$/    $$ |  $$/ $$ |$$    $$ |$$ |  $$ |$$ |  $$ |
$$ |  $$ |$$ \_____ $$ \__$$ |        $$ |      $$ |      $$ |$$$$$$$$/ $$ |  $$ |$$ \__$$ |
$$ |  $$ |$$       |$$    $$/         $$ |      $$ |      $$ |$$       |$$ |  $$ |$$    $$ |
$$/   $$/  $$$$$$$/  $$$$$$/          $$/       $$/       $$/  $$$$$$$/ $$/   $$/  $$$$$$$/ 
============================================================================================
Acu-Frend 1.0
============================================================================================
Acu-Frend 1.0 adalah aplikasi pendukung yang dirancang untuk mempermudah pembuatan
template CSV target bagi Acunetix. Dengan alat ini, pengguna dapat dengan cepat
menyusun, mengelola, dan mengekspor daftar target sesuai format standar.
"""

    return Fore.CYAN + banner_art + Style.RESET_ALL

def generate_acunetix_targets(input_file, output_file, profile, criticality, group, header, force):
    """
    Generates a comprehensive Acunetix target CSV file.
    """
    if not os.path.exists(input_file):
        print(f"Error: File input '{input_file}' tidak ditemukan.")
        return

    if os.path.exists(output_file) and not force:
        response = input(f"File output '{output_file}' sudah ada. Timpa (y/n)? ")
        if response.lower() != 'y':
            print("Operasi dibatalkan.")
            return

    try:
        print("\nMemulai konversi file...")
        with open(input_file, 'r') as f_in, open(output_file, 'w', newline='') as f_out:
            writer = csv.writer(f_out)

            if header:
                writer.writerow(['Target_URL', 'Scan_Profile', 'Criticality', 'Target_Group'])

            for line in f_in:
                target_url = line.strip()
                if target_url:
                    if target_url.startswith(('http://', 'https://')):
                        writer.writerow([target_url, profile, criticality, group])
                    else:
                        print(f"Peringatan: URL tidak valid '{target_url}' dilewati.")

        print(f"\nBerhasil membuat file target '{output_file}'.")
        print(f"URL dari '{input_file}' telah diisi dengan parameter berikut:")
        print(f" - Profil Pemindaian: {profile}")
        print(f" - Kritisitas: {criticality}")
        print(f" - Grup Target: {group}")

    except Exception as e:
        print(f"Terjadi kesalahan saat membuat file: {e}")

if __name__ == "__main__":
    banner_text = create_banner()
    print(banner_text)

    parser = argparse.ArgumentParser(
        description="Gunakan -h atau --help untuk menampilkan opsi.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        'input_file',
        metavar='INPUT_FILE',
        type=str,
        help="Jalur ke file targets.txt Acunetix."
    )
    parser.add_argument(
        '-o', '--output',
        dest='output_file',
        type=str,
        default='acunetix_targets.csv',
        help="Jalur ke file CSV output (default: acunetix_targets.csv)."
    )
    parser.add_argument(
        '-p', '--profile',
        dest='scan_profile',
        type=str,
        default='Default Scan',
        help="Nama profil pemindaian di Acunetix (default: 'Default Scan')."
    )
    parser.add_argument(
        '-c', '--criticality',
        dest='criticality',
        type=str,
        default='High',
        choices=['High', 'Medium', 'Low'],
        help="Tingkat kritisitas target (default: 'High'). Pilihan: High, Medium, Low."
    )
    parser.add_argument(
        '-g', '--group',
        dest='target_group',
        type=str,
        default='Default Group',
        help="Nama grup target di Acunetix (default: 'Default Group')."
    )
    parser.add_argument(
        '--no-header',
        action='store_true',
        help="Jangan tambahkan baris header di file CSV."
    )
    parser.add_argument(
        '-f', '--force',
        action='store_true',
        help="Timpa file output yang sudah ada tanpa konfirmasi."
    )

    args = parser.parse_args()

    generate_acunetix_targets(
        input_file=args.input_file,
        output_file=args.output_file,
        profile=args.scan_profile,
        criticality=args.criticality,
        group=args.target_group,
        header=not args.no_header,
        force=args.force
    )
