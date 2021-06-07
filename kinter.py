import tkinter as tk
import logging
from noise import snoise2
import random
import numpy
from palette import Palette
from PIL import Image, ImageTk
import os
from pypresence import Presence
import time

client_id = '851529902858567681'
RPC = Presence(client_id) 
RPC.connect() 

print(RPC.update(state="STATE HERE", details="DETAILS HERE", large_image="NAME OF LARGE IMAGE HERE", small_image="NAME OF SMALL IMAGE HERE", large_text="LARGE IMAGE TEXT HERE", start=time.time()))  # Set the presence

A4 = 794, 1123
A4X = tuple([int(i // 1.5) for i in A4])
print(A4X)

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)
pal = Palette(temptress="#29161d", wewak="#fa9495")


class Writer:
    im = Image.new("RGBA", A4, (0xFF, 0xFF, 0xFF, 0xFF))
    nm = numpy.array(im)
    octaves = 0
    freq = 0

    def __init__(self, tkinter_instance=None):
        self.thekinter = tkinter_instance
        self.tinker_sheet = ImageTk.PhotoImage(self.im.resize(A4X))
        self.tinker_sheet_label = tk.Label(self.thekinter, image=self.tinker_sheet)
        self.tinker_sheet_label.grid(row=0, column=5, rowspan=2)
        self.d = dict()
        for i in os.listdir("./data/"):
            self.d[i[0]] = [
                Image.open(f"./data/{i}/{im}") for im in os.listdir(f"./data/{i}/")
            ]
        self.im_ki_copy = self.im.copy()

    def white_noise(self, w, h, f, o):
        a = int(abs(0x7F * snoise2(w / f, h / f, o))) + 0x7F
        if a < 0xD8:
            a = random.choice([0xD0, 0xD2, 0xD4])
        return a

    def create_new_page(self):
        octaves = random.randint(16, 32)
        freq = (float(random.randint(1, 16))) * octaves
        self.freq = freq
        self.octaves = octaves
        for h in range(A4[1]):
            for w in range(A4[0]):
                self.nm[h, w] = (
                    a := (self.white_noise(w, h, freq, octaves)),
                    a,
                    a,
                    0xFF,
                )
        self.im = Image.fromarray(self.nm)
        self.im_ki_copy = self.im.copy()

    def pm(self, y):
        return y + random.choice([0, 0, 0, 3, 2, 1])

    def typechars(self, typethis):
        self.im = self.im_ki_copy.copy()
        typethis = typethis.split("\n")
        typethese = []
        for i in typethis:
            typethese.append(i.split(" "))

        x = random.randint(20, 50)
        y = random.randint(32, 40)
        slant = 0

        for i in typethese:
            for j in i:
                if len(j) * 18 + x > A4[0]:
                    r = random.choice([32, 36, 40])
                    y += r
                    y - random.randint(slant // 2, slant)
                    x = random.randint(20, 50)
                    slant = 0
                    if y > A4[1] - 50:
                        return self.show_on_page()
                for k in j:
                    if k in ("f", "g", "j", "p", "q", "y"):
                        self.im.paste(
                            a := random.choice(self.d[k]),
                            (x, (slant := self.pm(slant)) + y + 8),
                            a,
                        )
                    elif k == "‘" or k == "’":
                        self.im.paste(
                            a := random.choice(self.d["'"]),
                            (x, (slant := self.pm(slant)) + y),
                            a,
                        )
                    elif k == ".":
                        self.im.paste(
                            a := random.choice(self.d["☺"]),
                            (x, (slant := self.pm(slant)) + y),
                            a,
                        )
                    elif k == ">":
                        self.im.paste(
                            a := random.choice(self.d["♥"]),
                            (x, (slant := self.pm(slant)) + y),
                            a,
                        )
                    elif k == "<":
                        self.im.paste(
                            a := random.choice(self.d["♦"]),
                            (x, (slant := self.pm(slant)) + y),
                            a,
                        )
                    elif k == "*":
                        self.im.paste(
                            a := random.choice(self.d["♠"]),
                            (x, (slant := self.pm(slant)) + y),
                            a,
                        )
                    elif k == ":":
                        self.im.paste(
                            a := random.choice(self.d["○"]),
                            (x, (slant := self.pm(slant)) + y),
                            a,
                        )
                    elif k == "/":
                        self.im.paste(
                            a := random.choice(self.d["•"]),
                            (x, (slant := self.pm(slant)) + y),
                            a,
                        )
                    elif k == "|":
                        self.im.paste(
                            a := random.choice(self.d["◘"]),
                            (x, (slant := self.pm(slant)) + y),
                            a,
                        )
                    elif k == "-":
                        self.im.paste(
                            a := random.choice(self.d["♣"]),
                            (x, (slant := self.pm(slant)) + y),
                            a,
                        )
                    elif k == '"':
                        self.im.paste(
                            a := random.choice(self.d["☻"]),
                            (x, (slant := self.pm(slant)) + y - 8),
                            a,
                        )
                    else:
                        self.im.paste(
                            a := random.choice(self.d[k]),
                            (x, (slant := self.pm(slant)) + y),
                            a,
                        )
                    x += random.randint(15, 16)
                r = random.randint(16, 30)
                x += r
            r = random.choice([32, 36, 40])
            y += r
            y - random.randint(slant // 2, slant)
            if y > A4[1] - 50:
                return self.show_on_page()
            x = random.randint(20, 50)
            slant = 0
        # self.im.paste(self.d["ñ"][0], (A4[0]//2, 0), self.d["ñ"][0])
        self.show_on_page()

    def show_on_page(self):
        self.tinker_sheet_label.grid_forget()
        self.tinker_sheet = ImageTk.PhotoImage(self.im.resize(A4X))
        self.tinker_sheet_label = tk.Label(self.thekinter, image=self.tinker_sheet)
        self.tinker_sheet_label.grid(row=0, column=5, rowspan=2)

    def newpageblit(self):
        self.create_new_page()
        self.tinker_sheet_label.grid_forget()
        self.tinker_sheet = ImageTk.PhotoImage(self.im.resize(A4X))
        self.tinker_sheet_label = tk.Label(self.thekinter, image=self.tinker_sheet)
        self.tinker_sheet_label.grid(row=0, column=5, rowspan=2)

    def savefile(self, filename, filetext):
        self.im.save(f"./{filename}.png")
        with open(f"./{filename}.txt", "w") as file:
            file.write(filetext)


root = tk.Tk()
writer = Writer(root)
root.configure(bg=pal.colors["temptress"])
if os.name != "posix":
    root.iconbitmap("icon.ico")

logo_img = ImageTk.PhotoImage(Image.open("lain.png").resize((64, 64)))
tk.Label(image=logo_img).grid(row=0, column=0)

file_entry = tk.Entry(root, bg=pal.colors["temptress"], fg=pal.colors["wewak"])
file_entry.grid(row=0, column=3)

download_button = tk.Button(
    root,
    text="Download",
    bg=pal.colors["temptress"],
    fg=pal.colors["wewak"],
    command=lambda: writer.savefile(file_entry.get(), text_entry.get("1.0", "end")),
)
download_button.grid(row=0, column=4)

text_entry = tk.Text(
    root,
    wrap=tk.WORD,
    bg=pal.colors["temptress"],
    fg=pal.colors["wewak"],
)
text_entry.grid(row=1, column=0, columnspan=5)

button_process = tk.Button(
    root,
    text="Process",
    bg=pal.colors["temptress"],
    fg=pal.colors["wewak"],
    command=lambda: writer.typechars(text_entry.get("1.0", "end")),
)
button_process.grid(row=0, column=1)

button_generate_new = tk.Button(
    root,
    text="Generate Sheet",
    bg=pal.colors["temptress"],
    fg=pal.colors["wewak"],
    command=writer.newpageblit,
)
button_generate_new.grid(row=0, column=2)


root.mainloop()
