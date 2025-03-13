from tkinter import *
from tkinter.ttk import *
from practica19 import *

musica = Reproductor ('mora.mp3')
is_playing = True

def play_music():
    musica.volumen(0.8)
    musica.play()



# Función para pausar o reanudar la música
def toggle_play_pause():
    global is_playing
    if is_playing:
        pygame.mixer.music.pause()  # Pausar
        is_playing = False
    else:
        pygame.mixer.music.unpause()  # Reanudar
        is_playing = True

# Función para detener la música
def stop_music():
    pygame.mixer.music.stop()

master = Tk()
master.geometry("200x200")

Label = Label(master,text = "Reproductor de musica")

Label.pack(pady = 10)
btn_play = Button(master,text = "Reproducir", command= play_music)
btn_play.pack(pady=10)

Label.pack(pady = 10)
btn_play = Button(master,text = "pausar", command= toggle_play_pause)
btn_play.pack(pady=10)

mainloop()

