import tkinter as tk


class MainWindow:

    def __init__(self, title: str, width: int, height: int, resizeble=(True, True), icon=None):
        self.root = tk.Tk()
        self.init_window(title, width, height, resizeble, icon)
        self.init_ui()

    def init_window(self, title: str, width: int, height: int, resizeble=(True, True), icon=None):
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x = (sw - width) // 2
        y = (sh - height) // 2
        self.root.title(title)
        self.root.geometry("{0}x{1}+{2}+{3}".format(width, height, 100, 100))
        self.root.resizable(resizeble[0], resizeble[1])
        if icon:
            photo = tk.PhotoImage(icon)
            self.root.iconphoto(False, photo)

    def init_ui(self):
        self.button0 = tk.Button(self.root, width=50, height=5, text="Press me!", relief=tk.GROOVE, bd=8)
        self.button1 = tk.Button(self.root, width=50, text="New button", font=("Times", 12, "bold"),
                                 wraplength=30, justify=tk.LEFT, underline=0)
        # self.label0 = tk.Label(self.root, text="I am a lable",
        #                        bg="yellow", relief=tk.GROOVE, wraplength=80,
        #                        font="Calibri 15")
        #self.label_image = tk.PhotoImage(file=r"resources/add.gif")
        #self.label0 = tk.Label(self.root, image=self.label_image)

    def draw_widgets(self):
        # self.label0.pack(anchor=tk.NW)
        self.button0.pack()
        self.button1.pack()
        # top_frame = tk.Frame(self.root, borderwidth=30, relief=tk.SUNKEN, width=300, height=200)
        # bottom_frame = tk.Frame(self.root, borderwidth=30, relief=tk.SUNKEN, width=300, height=200)
        # top_frame.pack()
        # bottom_frame.pack()

        # l1 = tk.Label(self.root, width=30, height=2, bg="red", text="First")
        # l2 = tk.Label(self.root, width=30, height=2, bg="yellow", text="Second")
        # l3 = tk.Label(self.root, width=30, height=2, bg="cyan", text="Third")
        # l1.grid(row=0, column=0)
        # l2.grid(row=0, column=1)
        # l3.grid(row=1, column=0, columnspan=2)
        # tk.Label(self.root, width=30, height=2, bg="green", text="Fourth").grid(row=2, column=0)

        # l1.grid_forget()
        # l1.grid_remove()
        # l1.grid()
        #
        # print(l1.grid_info())
        # print(self.root.grid_size())
        # print(self.root.grid_location(x=10, y=50))

        # tk.Label(self.root ,width=30, height=2, bg="red", text="First").grid(row=0, column=0,
        #                                                                      rowspan=2, sticky=tk.N+tk.S)
        # tk.Label(self.root, width=30, height=2, bg="yellow", text="Second").grid(row=0, column=1, padx=10, pady=10)
        # tk.Label(self.root, width=30, height=2, bg="orange", text="Third").grid(row=2, column=0)
        # tk.Label(self.root, width=30, height=2, bg="green", text="Fourth").grid(row=1, column=1)
        # tk.Label(self.root, width=30, height=2, bg="cyan", text="Fifth").grid(row=3, column=0, columnspan=2)

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

