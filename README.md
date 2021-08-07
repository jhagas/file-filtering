# File Name Filtering

Script ini awalnya dibuat untuk memudahkan dan mengumpulkan sertifikat [di sini](https://github.com/fisika2020/sertif). Namun script ini saya buat publik untuk memudahkan anda yang mungkin melakukan hal yang sama, yaitu memfilter file berdasarkan nama yang tercantum pada sebuah file list.

## Cara Menjalankan

Saya asumsikan pada sistem anda sudah terinstall `python` versi terbaru, dan anda sudah sedikit mengerti tentang GitHub dan command line interface
1. Download file [script](./filter.py) dari repository ini
2. Buat file list dengan format ditulis dengan huruf kecil, lihat [contoh](./list.txt).
3. Copy file list yang sudah anda buat dan [script](./filter.py) ke folder tempat file anda yang ingin dipilah.
4. `cd` ke folder tadi dengan Terminal/Command Prompt.
5. Jika file-file anda berformat PDF, jalankan script dengan menggunakan perintah
```
python filter.py -r list.txt -f pdf
```
5. Jika formatnya lain, cukup ganti bagian `pdf` pada perintah di atas dengan format file yang sesuai (misal: png, jpg, docx, dan sebagainya)

## License

MIT
