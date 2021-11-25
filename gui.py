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
            command=lambda: self.go_to_selected_maze(1),
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
            command=lambda: self.go_to_selected_maze(2),
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
            command=lambda: self.go_to_selected_maze(3),
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
            command=lambda: self.go_to_selected_maze(4),
            relief="flat"
        )
        self.button_4.place(
            x=808.9999999999999,
            y=209.99999999999994,
            width=228.0,
            height=266.0
        )

    def go_to_selected_maze(self, maze_number):
        """
        Fungsi untuk berpindah ke
        frame maze yang dipilih untuk
        selanjutnya memilih titik awal dan akhir
        """
        self.frame.forget()
        self.app = MazeFrame(self.master, maze_number)

class MazeFrame:
    """
    Frame untuk menu labirin
    Yang selanjutnya pilih awal dan akhir
    """
    def __init__(self, master, maze_number):
        self.master = master
        self.maze_number = maze_number
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

        self.frame.pack(fill="both", expand=1)

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
