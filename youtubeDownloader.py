import string
from tkinter import *
from pytube import YouTube

window = Tk()
window.geometry('600x500')
window.resizable(0, 0)
window.title("Welcome to YouTube Downloader")


Label(window, text='YouTube Video Downloader', font='arial 20 bold').pack()

link = StringVar()
#Taking link as a input
Label(window, text='Enter link here: ', font='arial 15 bold').place(x = 50, y = 50)
entered_link = Entry(window, width =50, textvariable=link).place(x=100, y = 90)

#For stream option
qual_text = "1 360\n2 480\n3 720\n4 1080\n5 2160\n"
text_qual = Label(window, text = qual_text, font='arial 10 bold').place(x = 100, y = 160)

Label(window, text="Enter stream quality:", font='arial 10 bold').place(x = 50, y = 110)

#Taking stream quality input
qual_entry = Entry(window, width=20)
qual_entry.place(x = 100, y = 140)


def chooseQual(choice):
    if choice == 1:
        return 1
    elif choice == 2:
        return 12
    elif choice == 3:
        return 2
    elif choice == 4:
        return 7
    elif choice == 5:
        return 4
    else:
        return 7


def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.all()
    choice = qual_entry.get()
    choice = int(choice)
    video[choice].download()
    
    Label(window, text='Downloaded', font='arial 10 bold').place(x=250, y=300)


Button(window, text='Download', font='arial 10', bg='red', command=Downloader).place(x = 250, y = 250)

window.mainloop()



