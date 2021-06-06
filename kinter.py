import tkinter as tk
import logging
from noise import snoise2
import random
import numpy
from palette import Palette
from PIL import Image, ImageTk

A4 = 794, 1123

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)
colors = Palette(temptress="#29161d", wewak="#fa9495")


class Writer:
    im = Image.new("RGBA", A4, (0xFF, 0xFF, 0xFF, 0xFF))
    nm = numpy.array(im)

    def white_noise(self, w, h, f, o):
        a = int(abs(0x7F * snoise2(w / f, h / f, o))) + 0x7F
        if a < 0xC8:
            a = random.choice([0xD0, 0xD2, 0xD4])
        return a



root = tk.Tk()
root.configure(bg=colors.temptress)
root.iconbitmap("icon.ico")

logo_img = ImageTk.PhotoImage(Image.open("lain.png").resize((64, 64)))
logo_label = tk.Label(image=logo_img).grid(row=0, column=0)

text_entry = tk.Text(root, wrap=tk.WORD, bg=colors.temptress, fg=colors.wewak)
text_entry.grid(row=1, column=0, columnspan=2)

button_process = tk.Button(
    text="Process",
    bg=colors.temptress,
    fg=colors.wewak,
    command=lambda: logging.info(text_entry.get("1.0", "end")),
)
button_process.grid(row=0, column=1)

paper_sheet = Image.new("RGBA", A4, (0xFF, 0xFF, 0xFF, 0xFF))
tinker_sheet = ImageTk.PhotoImage(paper_sheet.resize((A4[0] // 3, A4[1] // 3)))
tinker_sheet_label = tk.Label(image=tinker_sheet).grid(row=0, column=2, rowspan=2)


root.mainloop()
