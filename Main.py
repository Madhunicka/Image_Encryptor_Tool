from tkinter import *
from tkinter import filedialog


root = Tk()
root.geometry("250x160")
root.configure(bg="lightblue")


def encrypt_image():
    file1=filedialog.askopenfile(mode='r', filetypes=[('Image Files', '*.jpg'), 
                                                      ('Image Files', '*.png'), ('Image Files', '*.jpeg'), ('Image Files', '*.bmp')])
    if file1 is not None:
        # print(file1)
        filename= file1.name
        # print(filename) 
        key=entry.get(1.0,END)
        print(filename, key)
        extract1 = open(filename, 'rb')
        image = extract1.read()
        extract1.close()
        image = bytearray(image)
        for index, values in enumerate(image):
            image[index] = values^int(key) 
        extract2=open(filename, 'wb')
        extract2.write(image)
        extract2.close()

button_label = Label(root, text="Select File:")
button_label.place(x=10, y=20)
button_label.configure(bg="lightblue")

button1 = Button(root, text="Open File", command=encrypt_image)
button1.place( x=150, y=20)

key_label = Label(root, text="Enter encryption key:")
key_label.place(x=10, y=70)
key_label.configure(bg="lightblue")

entry = Text(root, height=1, width=10)
entry.place(x=150, y=70)

root.mainloop()