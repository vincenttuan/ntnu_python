import tkinter as tk
from PIL import Image, ImageTk
import urllib.request
from io import BytesIO

win = tk.Tk()

url = "https://image.u-car.com.tw/carsummaryimage7_50578.jpg"
raw_data = urllib.request.urlopen(url).read()

im = Image.open(BytesIO(raw_data))
photo = ImageTk.PhotoImage(im)

label = tk.Label(image=photo)
label.image = photo
label.pack()

win.mainloop()