import itertools
import string
import time

# ✅ Simulasi target header yang dianggap valid oleh server
TARGET_HEADER = "device-a1b2c3"  # Ini "secret" yang akan ditebak

# ✅ Charset yang digunakan dalam token (bisa disesuaikan)
charset = string.ascii_lowercase + string.digits  # a-z0-9

# ✅ Panjang token bagian belakang (tanpa prefix "device-")
token_length = 6

def brute_force_header_token():
    print("\n🔐 Simulasi Brute Force: X-Device-ID")
    print(f"Target Header yang akan ditebak: ??? (panjang token = {token_length})\n")
    start_time = time.time()

    attempts = 0

    for guess in itertools.product(charset, repeat=token_length):
        token = ''.join(guess)
        header = f"device-{token}"
        attempts += 1

        print(f"[{attempts}] Trying header: {header}")

        if header == TARGET_HEADER:
            elapsed = time.time() - start_time
            print(f"\n✅ Match ditemukan!\nHeader: {header}\nTotal Percobaan: {attempts}\nWaktu: {elapsed:.2f} detik")
            return

        # Delay kecil agar terlihat prosesnya
        # time.sleep(0.01)

    print("\n❌ Tidak ditemukan (perlu lebih banyak kombinasi atau charset).")

if __name__ == "__main__":
    brute_force_header_token()
