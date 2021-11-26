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
            font=("WorkSans Bold", 34 * -1)
        )

        self.canvas.create_rectangle(
            393.9999999999999,
            163.99999999999994,
            683.9999999999999,
            453.99999999999994,
            fill="#C4C4C4",
            outline=""
        )

        self.entry_image_1 = tk.PhotoImage(file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            461.4999999999999,
            529.5,
            image=self.entry_image_1
        )
        self.entry_1 = tk.Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        self.entry_1.place(
            x=400.9999999999999,
            y=499.99999999999994 + 23,
            width=121.0,
            height=30.0
        )

        self.entry_image_2 = tk.PhotoImage(file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            615.4999999999999,
            529.5,
            image=self.entry_image_2
        )
        self.entry_2 = tk.Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
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
            font=("IBMPlexSans SemiBold", 14 * -1)
        )

        self.canvas.create_text(
            554.9999999999999,
            507.99999999999994,
            anchor="nw",
            text="Titik akhir",
            fill="#00AFB9",
            font=("IBMPlexSans SemiBold", 14 * -1)
        )

        self.sisi = 290/self.maze_size
        self.frame.pack(fill="both", expand=1)
        self.maze_to_show(self.maze_size)
        self.maze_matrix = self.create_maze_matrix(self.maze_size)
        self.place_numbers(self.maze_matrix, self.maze_size, self.sisi)

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

class ShowSolution:
    def __init__(self, master):
        pass
        # buat petaknya
        # for node in solusi:
        #     node_location = np.where(maze_matrix == node)
        #     x_1 = np.where(transposed == node)[0][0]
        #     y_1 = np.where(transposed == node)[1][0]

        # self.canvas_maze.create_rectangle(
        #     0.5,0.5,panjang_sisi,panjang_sisi,
        #     fill="#fed9b7",
        #     outline=""
        # )
        # solusi = ['7', '15', '23', '31', '30', '29', '21', '22', '14', '13', '5', '4', '12', '20', '28', '27', '19', '11', '10', '2', '1', '9', '17', '18', '26', '34', '35', '36', '44', '52', '60', '61']

def main():
    """
    Main driver
    """
    root = tk.Tk()
    root.geometry("1078x640")
    app = MainMenu(root)
    root.mainloop()

if __name__ == '__main__':
    main()
