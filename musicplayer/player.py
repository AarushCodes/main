from tkinter import *
import pygame
from tkinter import filedialog

root = Tk()
root.title("Aarush's music player")
root.geometry("500x300")

# initialize pygame mixer
pygame.mixer.init()

#conv tup
def convtup(tup):
	str = ''.join(tup)
	return str


# Add song function
def add_song():
	song = filedialog.askopenfilename(initialdir="C:\\Users\\Admin\\Music", title='Choose a Song', filetypes=(("wav files", "*.wav"), ("mp3 files", "*.mp3"), ))

	# Strip dir
	song = song.replace("C:/Users/Admin/Music/", "")
	song = song.replace(".wav", "")
	song = song.replace(".mp3", "")



	# Add song to list box
	song_box.insert(END, song)

# PLay selected song
def play():
	song = song_box.get(ACTIVE)
	song = f'C:/Users/Admin/Music/{song}.wav'
	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)


#stop playing
def stop():
	pygame.mixer.music.stop()
	song_box.selection_clear(ACTIVE)


# Create playlist box
song_box = Listbox(root, bg="black", fg="cyan", width=60, selectbackground="gray", selectforeground="cyan")
song_box.pack(pady=20)

# Define button images
back_btn_img = PhotoImage(file='back50.png')
forward_btn_img = PhotoImage(file='forward50.png')
play_btn_img = PhotoImage(file='play50.png')
pause_btn_img = PhotoImage(file='pause50.png')
stop_btn_img = PhotoImage(file='stop50.png')

# Create Player Buttons frames
controls_frame = Frame(root)
controls_frame.pack()

# Create player control buttons
back_button = Button(controls_frame, image=back_btn_img, borderwidth=0)
forward_button = Button(controls_frame, image=forward_btn_img, borderwidth=0)
play_button = Button(controls_frame, image=play_btn_img, borderwidth=0, command=play)
pause_button = Button(controls_frame, image=pause_btn_img, borderwidth=0)
stop_button = Button(controls_frame, image=stop_btn_img, borderwidth=0, command=stop) 

back_button.grid(row=0, column=0,padx=10)
forward_button.grid(row=0, column=4,padx=10)
play_button.grid(row=0, column=2,padx=10)
pause_button.grid(row=0, column=3,padx=10)
stop_button.grid(row=0, column=1,padx=10)

# Create a Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add Add song menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label='Add songs', menu=add_song_menu)
add_song_menu.add_command(label="Add one song to playlist", command=add_song)


#mainloop
root.mainloop()



