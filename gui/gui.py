"""
COLOR PALLETE
kuning pudar : fdfcdc
oren terang : f07167
oren pudar : fed9b7
tosca terang : 00afb9
tosca gelap : 0081a7
"""

import tkinter as tk

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

        self.button1 = tk.Button(
            self.frame,
            text="Pilih labirin",
            relief="flat",
            fg="#fff",
            bg="#00afb9",
            command=self.go_to_maze_selection
        )
        self.button1.place(x=466, y=288, width=145, height=64)

        self.button2 = tk.Button(
            self.frame,
            text="Tentang",
            relief="flat",
            fg="#fff",
            bg="#00afb9"
        )
        self.button2.place(x=481, y=372, width=116, height=64)

        self.frame.pack(fill="both", expand=1)

    def go_to_maze_selection(self):
        """
        Method untuk pindah ke
        frame seleksi labirin
        """
        self.frame.forget()
        MazeSelection(self.master)
        # self.newWindow = tk.Toplevel(self.master)
        # self.app = Demo2(self.newWindow)

class MazeSelection:
    """
    Frame untuk seleksi labirin
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
            text="Pilih Labirin",
            fill="#0081a7",
            font=("Lucida Console", 34 * -1)
        )

        self.maze5 = self.Button(
            self.frame,
            image=
        )
        # self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        # self.quitButton.pack()
        self.frame.pack(fill="both", expand=1)
        # ControlMazeFrame(self.frame)

    # def close_windows(self):
    #     self.master.destroy()

class ControlMazeFrame:
    """
    Class untuk mengontrol pilihan
    pada frame seleksi labirin
    """
    def __init__(self, master):
        self.master = master
        self.selected_maze = tk.IntVar()

        tk.Radiobutton(
            self.master,  # container/frame nya
            text="Labirin 5x5",
            relief="flat",
            bg="#fdfcdc",
            value=0,
            variable=self.selected_maze,
            command=self.change_to_maze_frame
        ).place(x=125, y=497)

        tk.Radiobutton(
            self.master,  # container/frame nya
            text="Labirin 8x8",
            relief="flat",
            bg="#fdfcdc",
            value=1,
            variable=self.selected_maze,
            command=self.change_to_maze_frame
        ).place(x=381, y=497)

        tk.Radiobutton(
            self.master,  # container/frame nya
            text="Labirin 10x10",
            relief="flat",
            bg="#fdfcdc",
            value=2,
            variable=self.selected_maze,
            command=self.change_to_maze_frame
        ).place(x=637, y=497)

        tk.Radiobutton(
            self.master,  # container/frame nya
            text="Labirin 12x12",
            relief="flat",
            bg="#fdfcdc",
            value=3,
            variable=self.selected_maze,
            command=self.change_to_maze_frame
        ).place(x=893, y=497)

        # bikin pilihan frame labirin
        self.frames = {}
        self.frames[5] = MazeFrame(5)
        self.frames[8] = MazeFrame(8)
        self.frames[10] = MazeFrame(10)
        self.frames[12] = MazeFrame(12)

        self.change_to_maze_frame()

    def change_to_maze_frame(self):
        """
        Method untuk masuk ke dalam
        frame labirin yang dipilih
        """
        frame = self.frames[self.selected_maze.get()]
        # frame.reset()
        # frame.tkraise()

class MazeFrame:
    """
    Frame untuk menu labirin
    Yang selanjutnya pilih awal dan akhir
    """
    def __init__(self, maze_number):
        print(maze_number)

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
