# Solusi Pencarian Labirin dengan A * Search
  
Proyek ini dapat menunjukkan solusi jalur dari 4 labirin dengan ukuran berbeda serta titik awal dan tujuan yang dapat dipilih sendiri. Metode pencarian jalur yang digunakan adalah [A * Search](https://en.wikipedia.org/wiki/A*_search_algorithm).

## Screenshot

![UI Pilih labirin](https://github.com/zeerafle/a-star-is-born/blob/master/images/Pilih%20labirin%20frame_UI.png)

## Cara Menjalankan Program

0. Install Numpy

    ```console
    pip install numpy
    ```

1. Unduh repository ini
    - Jika sudah install git, jalankan perintah berikut di cmd/terminal.
        
        ```console
        git clone https://github.com/zeerafle/a-star-is-born.git
        ```
    
    - Jika belum atau malas install-install lagi
    
        Klik tombol *Code* warna hijau diatas. *Download as zip*, extract zip-nya.

2. Masuk ke direktori repository ini. Atau bisa juga buka folder ini dengan Text Editor kesayangan.

3. Jalankan file *gui.py*.
    
    Atau kalau lewat cmd/terminal jalankan
    
    ```console
    python gui.py
    ```

## Resource
Implementasi metode A * Search di-fork dari repository [ini](https://github.com/fakemonk1/AI-Search-Algorithms-Implementations).

GUI dibuat menggunakan package [Tkinter](https://tkdocs.com/index.html). Sumber belajar:

- [Dasar tkinter, video (bahasa Indonesia)](https://youtu.be/RWCeiOCfIuY)
- [Dasar tkinter, video (bahasa inggris)](https://youtu.be/YXPyB4XeYLA)
- [Python GUI Programming](https://www.tutorialspoint.com/python/python_gui_programming.htm)
- [Dasar tkinter (khususnya cara membuat GUI interaktif) (bahasa Inggris)](https://realpython.com/python-gui-tkinter/#making-your-applications-interactive)
- [Saran membuat struktur kodingan tkinter yang rapi](https://stackoverflow.com/questions/17466561/best-way-to-structure-a-tkinter-application)
- Cara berganti frame di Tkinter ([contoh kode-nya](https://lyw4.life/Resources/039_swapping_between_frames.py), [videonya](https://youtu.be/e6ktaqlXaec))

Desain UI menggunakan [Figma](https://www.figma.com/ui-design-tool/). Daftar [Figma Education Plan](https://www.figma.com/education/) supaya dapat lisensi pro gratis.

Desain UI dapat dengan mudah diterapkan di Tkinter menggunakan tool [Tkinter Designer](https://github.com/ParthJadhav/Tkinter-Designer)