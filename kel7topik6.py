# Papan permainan dengan jumlah lubang berbeda
papan = {
    "pemain1": [7, 7, 7, 7, 7],  # Lubang kecil pemain 1 (5 lubang)
    "pemain2": [7, 7, 7, 7, 7, 7, 7],  # Lubang kecil pemain 2 (7 lubang)
    "lumbung1": 0,  # Lumbung pemain 1
    "lumbung2": 0   # Lumbung pemain 2
}

def sebarkan_biji(papan, pemain, posisi_awal):
    """
    Sebarkan biji mulai dari posisi yang dipilih pemain, lintas sisi jika perlu.
    """
    biji = papan[pemain][posisi_awal]
    papan[pemain][posisi_awal] = 0  # Kosongkan lubang yang dipilih
    posisi = posisi_awal
    sisi_saat_ini = pemain

    while biji > 0:
        posisi += 1
        if sisi_saat_ini == "pemain1" and posisi < len(papan["pemain1"]):
            papan["pemain1"][posisi] += 1
        elif sisi_saat_ini == "pemain2" and posisi < len(papan["pemain2"]):
            papan["pemain2"][posisi] += 1
        else:
            # Pindah ke sisi lawan
            sisi_saat_ini = "pemain2" if sisi_saat_ini == "pemain1" else "pemain1"
            posisi = -1
            continue
        biji -= 1

    return sisi_saat_ini, posisi  # Lokasi terakhir biji

def ganti_giliran(pemain_saat_ini):
    return "pemain2" if pemain_saat_ini == "pemain1" else "pemain1"

def periksa_akhir_permainan(papan):
    """
    Periksa apakah permainan selesai (semua lubang kosong di salah satu sisi).
    """
    if all(biji == 0 for biji in papan["pemain1"]) or all(biji == 0 for biji in papan["pemain2"]):
        papan["lumbung1"] += sum(papan["pemain1"])
        papan["lumbung2"] += sum(papan["pemain2"])
        papan["pemain1"] = [0] * len(papan["pemain1"])
        papan["pemain2"] = [0] * len(papan["pemain2"])
        return True
    return False

def tampilkan_papan(papan):
    """
    Tampilkan papan permainan.
    """
    print("\nPapan Permainan:")
    print("  Pemain 2:", papan["pemain2"])
    print("  Lumbung 2:", papan["lumbung2"])
    print("  Pemain 1:", papan["pemain1"])
    print("  Lumbung 1:", papan["lumbung1"], "\n")

def main():
    """
    Jalankan permainan Congklak.
    """
    pemain_saat_ini = "pemain1"
    while not periksa_akhir_permainan(papan):
        tampilkan_papan(papan)
        print(f"Giliran {pemain_saat_ini}.")
        try:
            pilihan = int(input(f"Pilih lubang (1-{len(papan[pemain_saat_ini])}): ")) - 1
            if 0 <= pilihan < len(papan[pemain_saat_ini]) and papan[pemain_saat_ini][pilihan] > 0:
                sisi_terakhir, posisi_terakhir = sebarkan_biji(papan, pemain_saat_ini, pilihan)
                pemain_saat_ini = ganti_giliran(pemain_saat_ini)
            else:
                print("Pilihan tidak valid. Coba lagi.")
        except ValueError:
            print("Masukkan angka yang valid.")
    
    tampilkan_papan(papan)
    pemenang = "Pemain 1" if papan["lumbung1"] > papan["lumbung2"] else "Pemain 2"
    print(f"Permainan selesai! Pemenangnya adalah {pemenang}.")

if __name__ == "__main__":
    main()