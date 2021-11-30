"""
COLOR PALLETE
kuning pudar : fdfcdc
oren terang : f07167
oren pudar : fed9b7
tosca terang : 00afb9
tosca gelap : 0081a7
"""

from pathlib import Path
import tkinter as tk
import numpy as np
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    """
    Menghasilkan jalur file relatif terhadap path
    """
    return ASSETS_PATH / Path(path)

class MainMenu:
    """
    Frame untuk main menu
    """
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.canvas = tk.Canvas(
            self.frame,
            bg = "#FDFCDC",
            height = 640,
            width = 1078,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.place(x=0, y=0)
        self.canvas.create_text(
            429.0,
            78.0,
            anchor="nw",
            text="Labirin Solver",
            fill="#0081a7",
            font=("Lucida Console", 34 * -1)
        )

        self.button1_image = tk.PhotoImage(file=relative_to_assets("pilih_labirin.png"))
        self.button1 = tk.Button(
            self.frame,
            image=self.button1_image,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=self.go_to_maze_selection
        )
        self.button1.place(
            x=455.9999999999999,
            y=277.99999999999994,
            width=166.0,
            height=84.0
        )

        self.button2_image = tk.PhotoImage(file=relative_to_assets("tentang.png"))
        self.button2 = tk.Button(
            self.frame,
            relief="flat",
            image=self.button2_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.go_to_about
        )
        self.button2.place(
            x=480.9999999999999,
            y=371.99999999999994,
            width=116.0,
            height=64.0
        )

        self.frame.pack(fill="both", expand=1)

    def go_to_maze_selection(self):
        """
        Method untuk pindah ke
        frame seleksi labirin
        """
        self.frame.forget()
        self.app = MazeSelection(self.master)
        # self.newWindow = tk.Toplevel(self.master)
        # self.app = Demo2(self.newWindow)

    def go_to_about(self):
        """
        Method untuk pindah ke frame tentang
        """
        self.frame.forget()
        self.app = About(self.master)

class MazeSelection:
    """
    Frame untuk seleksi labirin
    """
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack(fill="both", expand=1)

        self.canvas = tk.Canvas(
            self.frame,
            bg = "#FDFCDC",
            height = 640,
            width = 1078,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.place(x=0, y=0)
        self.canvas.create_text(
            429.0,
            78.0,
            anchor="nw",
            text="Pilih Labirin",
            fill="#0081a7",
            font=("Lucida Console", 34 * -1)
        )

        self.button_image_1 = tk.PhotoImage(file=relative_to_assets("maze5.png"))
        self.button_1 = tk.Button(
            self.frame,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.go_to_selected_maze(5),
            relief="flat"
        )
        self.button_1.place(
            x=40.999999999999886,
            y=209.99999999999994,
            width=228.0,
            height=266.0
        )

        self.button_image_2 = tk.PhotoImage(file=relative_to_assets("maze8.png"))
        self.button_2 = tk.Button(
            self.frame,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.go_to_selected_maze(8),
            relief="flat"
        )
        self.button_2.place(
            x=296.9999999999999,
            y=209.99999999999994,
            width=228.0,
            height=266.0
        )

        self.button_image_3 = tk.PhotoImage(file=relative_to_assets("maze10.png"))
        self.button_3 = tk.Button(
            self.frame,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.go_to_selected_maze(10),
            relief="flat"
        )
        self.button_3.place(
            x=552.9999999999999,
            y=209.99999999999994,
            width=228.0,
            height=266.0
        )

        self.button_image_4 = tk.PhotoImage(file=relative_to_assets("maze12.png"))
        self.button_4 = tk.Button(
            self.frame,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.go_to_selected_maze(12),
            relief="flat"
        )
        self.button_4.place(
            x=808.9999999999999,
            y=209.99999999999994,
            width=228.0,
            height=266.0
        )

    def go_to_selected_maze(self, maze_size):
        """
        Fungsi untuk berpindah ke
        frame maze yang dipilih untuk
        selanjutnya memilih titik awal dan akhir
        """
        self.frame.forget()
        self.app = MazeFrame(self.master, maze_size)

class About:
    """
    Frame untuk Tentang
    """
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack(fill="both", expand=1)

        self.canvas = tk.Canvas(
            self.frame,
            bg = "#FDFCDC",
            height = 640,
            width = 1078,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.place(x=0, y=0)
        self.canvas.create_text(
            471.9999999999999,
            77.99999999999994,
            anchor="nw",
            text="Tentang",
            fill="#0081A7",
            font=("SegoeUIBlack", 34 * -1)
        )

        self.button_image_1 = tk.PhotoImage(file=relative_to_assets("home_button.png"))
        self.button_1 = tk.Button(
            self.frame,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.go_to_home,
            relief="flat"
        )
        self.button_1.place(
            x=489.9999999999999,
            y=501.99999999999994,
            width=98.0,
            height=64.0
        )

        self.canvas.create_text(
            212.9999999999999,
            157.99999999999994,
            anchor="nw",
            text="Proyek Akhir Praktikum\nMata Kuliah Kecerdasan Buatan\nKelompok 2",
            fill="#000000",
            font=("SegoeUI Bold", 20 * -1)
        )

        desc = """Solusi Pencarian Jalur Labirin dengan A * Search.
Proyek ini mengimplementasikan metode pencarian heuristik A * Search untuk menemukan solusi jalur labirin.
Proyek ini dibuat menggunakan bahasa pemrograman Python."""
        self.canvas.create_text(
            212.9999999999999,
            260.99999999999994,
            anchor="nw",
            text=desc,
            fill="#000000",
            font=("SegoeUI", 13 * -1)
        )

        name_text = """Fara Meydina Youndseand
Ahmad Lutfi Alfares
Vauwez Sam El Fareez
Alyani Noor Septalia
"""
        self.canvas.create_text(
            409.9999999999999,
            340.99999999999994,
            anchor="nw",
            text=name_text,
            fill="#000000",
            font=("SegoeUI", 13 * -1)
        )

        self.canvas.create_text(
            583.9999999999999,
            340.99999999999994,
            anchor="nw",
            text="2009106061\n2009106074\n2009106054\n2009106100",
            fill="#000000",
            font=("SegoeUI", 13 * -1)
        )

    def go_to_home(self):
        """
        Fungsi untuk kembali ke menu awal
        """
        self.frame.forget()
        self.app = MainMenu(self.master)

class MazeFrame:
    """
    Frame untuk menu labirin
    Yang selanjutnya pilih awal dan akhir
    """
    def __init__(self, master, maze_size):
        self.master = master
        self.maze_size = maze_size
        self.frame = tk.Frame(self.master)

        self.canvas = tk.Canvas(
            self.frame,
            bg = "#FDFCDC",
            height = 640,
            width = 1078,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.place(x=0, y=0)
        self.canvas.create_text(
            341.9999999999999,
            77.99999999999994,
            anchor="nw",
            text="Pilih titik awal dan akhir",
            fill="#0081A7",
            font=("WorkSans Bold", 34 * -1),
            tags=("title")
        )

        self.canvas.create_rectangle(
            393.9999999999999,
            163.99999999999994,
            683.9999999999999,
            453.99999999999994,
            fill="#C4C4C4",
            outline=""
        )

        self.titik_awal = tk.StringVar()
        self.entry_image_1 = tk.PhotoImage(file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            461.4999999999999,
            529.5,
            image=self.entry_image_1,
            tags=("entry")
        )
        self.entry_1 = tk.Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0,
            textvariable=self.titik_awal
        )
        self.entry_1.place(
            x=400.9999999999999,
            y=499.99999999999994 + 23,
            width=121.0,
            height=30.0
        )

        self.titik_akhir = tk.StringVar()
        self.entry_image_2 = tk.PhotoImage(file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            615.4999999999999,
            529.5,
            image=self.entry_image_2,
            tags=("entry")
        )
        self.entry_2 = tk.Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0,
            textvariable=self.titik_akhir
        )
        self.entry_2.place(
            x=554.9999999999999,
            y=499.99999999999994 + 23,
            width=121.0,
            height=30.0
        )

        self.canvas.create_text(
            400.9999999999999,
            507.99999999999994,
            anchor="nw",
            text="Titik awal",
            fill="#00AFB9",
            font=("IBMPlexSans SemiBold", 14 * -1),
            tags=("entry")
        )

        self.canvas.create_text(
            554.9999999999999,
            507.99999999999994,
            anchor="nw",
            text="Titik akhir",
            fill="#00AFB9",
            font=("IBMPlexSans SemiBold", 14 * -1),
            tags=("entry")
        )

        self.sisi = 290/self.maze_size
        self.frame.pack(fill="both", expand=1)
        self.maze_to_show(self.maze_size)
        self.maze_matrix = self.create_maze_matrix(self.maze_size)
        self.place_numbers(self.maze_matrix, self.maze_size, self.sisi)
        self.entry_2.bind('<Return>', self.find_solution)

    def maze_to_show(self, maze_size):
        """
        Menampilkan labirin yang dipilih
        berdasarkan maze_size yang dimasukkan
        """
        self.file_name = "maze" + str(maze_size) + "_pure.png"
        self.image_file = tk.PhotoImage(file=relative_to_assets(self.file_name))

        # bikin semacam container untuk labirinnya
        self.canvas_maze = tk.Canvas(
            self.frame,
            height=290,
            width=290,
            relief="flat"
        )
        self.canvas_maze.place(x=394.0, y=164.0,)
        self.canvas_maze.create_image(
            145.5,
            145.5,
            image=self.image_file
        )

    def create_maze_matrix(self, maze_size):
        """
        Membuat matrix yang sesuai dengan maze_size
        Ukuran labirin dalam frame ini adalah 290x290.
        Maka, panjang sisi satu petak = 290/maze_size.
        """
        maze_matrix = np.arange(1, maze_size*maze_size+1).reshape(maze_size, -1)
        return np.transpose(maze_matrix)

    def place_numbers(self, maze_matrix, maze_size, sisi):
        """
        Menempatkan angka di tiap petak
        """
        x_1 = y_1 = sisi/2
        for column in range(maze_size):
            for row in range(maze_size):
                self.canvas_maze.create_text(
                    x_1,
                    y_1,
                    text=str(maze_matrix[row,column]),
                    font=("Arial", 7)
                )
                y_1 += sisi # karena ini iterasi baris maka y yang bergerak
            x_1 += sisi # setelah kolom pertama selesai, x bergerak
            y_1 = sisi/2 # reset nilai y_1

    def find_solution(self, event):
        """
        Menggambar solusi jalur labirin
        """
        from Search_Algorithms import astar_search, maze8, maze5, maze10, maze12

        if self.maze_size == 5:
            graph = maze5()
        elif self.maze_size == 8:
            graph = maze8()
        elif self.maze_size == 10:
            graph = maze10()
        else:
            graph = maze12()

        # _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
        path, explored = astar_search(graph, self.titik_awal.get(), self.titik_akhir.get())
        # _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
        print(self.maze_matrix.shape)
        print("Jalur:", path)
        print("Tereksplor:", explored)

        for node in path:
            self.place_box(node) # warnain kotak di setiap node solusi

        self.place_box(path[0], "#00afb9") # warnain kotak titik awal
        self.place_box(path[-1], "#00afb9") # warnain kotak titik akhir

        self.go_to_result_frame()

    def place_box(self, node, fill="#f07167"):
        """
        Fungsi untuk mewarnai kotak
        """
        node_location = np.where(self.maze_matrix == int(node))
        x_mat = node_location[0][0]
        y_mat = node_location[1][0]

        self.canvas_maze.create_rectangle(
            self.sisi*y_mat + 7, #x1
            self.sisi*x_mat + 7, #y1
            self.sisi*(y_mat+1) - 4, #x2
            self.sisi*(x_mat+1) - 4, #y2
            fill=fill,
            outline=""
        )

    def go_to_result_frame(self):
        """
        Fungsi menghilangkan text entry
        kemudian menampilkan button
        'Jalankan lagi' dan 'home'.
        Serta mengganti judul.
        """
        # hapus yang ingin diganti
        self.entry_1.place_forget()
        self.entry_2.place_forget()
        self.canvas.delete("entry")
        self.canvas.delete("title")

        self.app = ResultFrame(self.master, self.frame, self.canvas, self.maze_size)

class ResultFrame:
    """
    Frame hasil. Terdapat tombol jalankan lagi
    dan Home
    """
    def __init__(self, master, frame, canvas, maze_size):
        self.master = master
        self.frame = frame
        self.canvas = canvas
        self.maze_size = maze_size

        self.canvas.create_text(
            488.9999999999999,
            77.99999999999994,
            anchor="nw",
            text="Hasil",
            fill="#0081A7",
            font=("WorkSans Bold", 34 * -1),
            tags=("title")
        )

        self.button_image_1 = tk.PhotoImage(file=relative_to_assets("jalankan_lagi.png"))
        self.button_1 = tk.Button(
            self.frame,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.re_run,
            relief="flat"
        )
        self.button_1.place(
            x=392.9999999999999,
            y=501.99999999999994,
            width=159.0,
            height=64.0
        )

        self.button_image_2 = tk.PhotoImage(file=relative_to_assets("home_button.png"))
        self.button_2 = tk.Button(
            self.frame,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.go_to_home,
            relief="flat"
        )
        self.button_2.place(
            x=582.9999999999999,
            y=501.99999999999994,
            width=98.0,
            height=64.0
        )

    def re_run(self):
        """
        Fungsi untuk menjalankan pencarian jalur lagi.
        Pengguna diminta memasukkan titik awal dan akhir lagi.
        """
        self.frame.forget()
        self.app = MazeFrame(self.master, self.maze_size)

    def go_to_home(self):
        """
        Fungsi untuk kembali ke menu awal
        """
        self.frame.forget()
        self.app = MainMenu(self.master)

def main():
    """
    Main driver
    """
    root = tk.Tk()
    root.geometry("1078x640")
    root.title("Labirin Solver GUI")
    app = MainMenu(root)
    root.resizable(False, False)
    root.mainloop()

if __name__ == '__main__':
    main()
