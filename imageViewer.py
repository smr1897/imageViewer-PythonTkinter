from tkinter import*
root = Tk()
root.title("Image Viewer")
root.geometry("1200x500")
iconphoto = PhotoImage(file="icon.png")
root.configure(background="black")
root.resizable(0,0)

def onclick_next():
    image_show_box_photo.configure(file='wallpaper2.png')
    back_button_label.bind("<Button-1>",lambda e:onclick_back())

def onclick_back():
    image_show_box_photo.configure(file='wallpaper1.png')
    back_button_label.bind("<Button-1>",lambda e:onclick_next())    

#back button
back_button_photo = PhotoImage(file="Back.png")
back_button_label = Label(root,image=back_button_photo,border=0)
back_button_label.place(x=0,y=245)

#forward button
forward_button_photo = PhotoImage(file="Forward.png")
forward_button_label = Label(root,image=forward_button_photo,border=0)
forward_button_label.place(x=1150,y=245)

#image show
image_show_box_photo = PhotoImage(file="wallpaperShow.png")
image_show_box_label = Label(root,image=image_show_box_photo,border=0)
image_show_box_label.place(x=50,y=50)

#label bind
back_button_label.bind("<Button-1>",lambda e:onclick_next())
forward_button_label.bind("<Button-1>",lambda e:onclick_back())

root.mainloop()