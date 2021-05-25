import os
import tkinter as tk
from tkinter import messagebox
import pyttsx3
from translate import Translator
from PIL import Image, ImageTk

engine = pyttsx3.init()

# Cambio la directory in cui lavoro (così mi basta solo specificare il nome del file e non il percorso)
os.chdir(os.getcwd() + r"\Immagini")


class Window(tk.Frame):
    def __init__(window, master=None):
        super().__init__(master)
        window.master.title("Traduttore")
        # DIMENSIONE FINESTRA
        # window.master.geometry("400x400")
        # DIMENSIONE FINESTRA NON MODIFICABILE
        window.master.resizable(0, 0)
        window.grid()
        # Sfondo finestra
        window.configure(background="#282623")
        # Icona finestra
        window.master.iconbitmap("Icona.ico")
        window.widgets()

    def widgets(window):
        global testo_da_tradurre
        global nome_tradotto
        global scelta
        global scelta_2

        # Carico le immagini dei pulsanti
        window.freccia = ImageTk.PhotoImage(Image.open("Freccia.png"))
        window.c = window.freccia
        window.audio1 = ImageTk.PhotoImage(Image.open("Altoparlante_15.png"))
        window.d = window.audio1
        window.audio2 = ImageTk.PhotoImage(Image.open("Altoparlante_25.png"))
        window.e = window.audio2
        window.infor = ImageTk.PhotoImage(Image.open("Punto_Int.png"))
        window.f = window.infor

        window.nome_da_tradurre = tk.StringVar()
        window.nome_tradotto = tk.StringVar()
        window.linguadx = tk.StringVar()
        window.linguasx = tk.StringVar()

        # testo in alto a sinistra
        window.titolo_da_tradurre = tk.Label(
            window, text=" TESTO DA TRADURRE ", font=("Helvetica", 11), fg="#0462f9"
        )
        window.titolo_da_tradurre.grid(row=0, column=0, sticky="n")
        window.titolo_da_tradurre.config(background="#282623")
        # Testo in altro a destra
        window.titolo_tradotto = tk.Label(
            window, text=" TRADUZIONE ", font=("Helvetica", 11), fg="red"
        )
        window.titolo_tradotto.grid(row=0, column=2, sticky="n")
        window.titolo_tradotto.config(background="#282623")

        # Casella di ricerca lingua da cui si vuole tradurre
        # window.cercadx = tk.Button(window, text=" ⏬ ", font=("Helvetica", 11), fg="light blue", relief="flat", command=window.framedx)
        # window.cercadx.grid(row=0, column=1, sticky="w")
        # window.cercadx.config(background="#282623")

        # Casella di ricerca lingua in cui si vuole tradurre
        # window.cercadx = tk.Button(window, text=" ⏬ ", font=("Helvetica", 11), fg="pink", relief="flat", command=window.framesx)
        # window.cercadx.grid(row=0, column=2, sticky="e")
        # window.cercadx.config(background="#282623")

        # Casella per inserire le parole a sinistra
        window.testo_da_tradurre = tk.Entry(
            window, textvariable=window.nome_da_tradurre
        )
        window.testo_da_tradurre.grid(row=2, column=0, sticky="we")
        window.testo_da_tradurre.config(background="#444341")
        # Casella per leggere le parole tradotte
        window.testo_tradotto = tk.Entry(window, textvariable=window.nome_tradotto)
        window.testo_tradotto.grid(row=2, column=2, sticky="we")
        window.testo_tradotto.config(background="#444341")
        # Bottone freccia per tradurre
        window.traduci = tk.Button(
            window,
            text="TRADUCI",
            font=("Helvetica", 11),
            fg="#8e18b2",
            bd=0,
            relief="flat",
            command=window.traduzione2,
            activebackground="#282623",
        )
        window.traduci.grid(row=2, column=1, padx=10)
        window.traduci.config(background="#282623", image=window.freccia)
        # casella di scelta a sinistra
        window.scelta = tk.Listbox(
            window, bg="light blue", width=30, fg="blue", highlightcolor="blue"
        )
        window.scelta.grid(row=1, column=0, sticky="nw")
        # Casella di scelta a destra
        window.scelta_2 = tk.Listbox(
            window, bg="pink", width=30, fg="red", highlightcolor="red"
        )
        window.scelta_2.grid(row=1, column=2, sticky="nw")
        # Bottone per ascoltare la parola/frase inserita
        window.audio_1 = tk.Button(
            window, relief="flat", bd=0, command=window.leggi_1, pady=10
        )
        window.audio_1.grid(row=3, column=0, sticky="sew")
        window.audio_1.config(
            background="#282623", image=window.audio1, activebackground="#282623"
        )
        # Bottone per ascoltare la parola/frase tradotta
        window.audio_2 = tk.Button(
            window, relief="flat", bd=0, command=window.leggi_2, pady=10
        )
        window.audio_2.grid(row=3, column=2, sticky="sew")
        window.audio_2.config(
            background="#282623", image=window.audio2, activebackground="#282623"
        )
        # Bottone per la guida
        window.info = tk.Button(
            window, relief="flat", bd=0, command=window.informazioni, pady=10
        )
        window.info.grid(row=3, column=1, sticky="sew")
        window.info.config(
            background="#282623", image=window.infor, activebackground="#282623"
        )
        # Developer
        window.dani = tk.Label(
            window, text="DanyB0", font=("Helvetica", 7), fg="#12e8bd", bg="#282623"
        ).grid(row=3, column=2, sticky="se")
        # Inserisco nelle listbox le lingue in cui è possibile fare la traduzione
        for i in range(len(lista_lingue)):
            window.scelta.insert("end", lista_lingue[i])
            window.scelta_2.insert("end", lista_lingue[i])
        # Collego la pressione dei tasti specifici con eventi
        window.scelta.bind(
            "<Button-1>", window.prendi_lingua_1
        )  # Button-1 è il tasto destro del mouse
        window.scelta_2.bind("<Button-1>", window.prendi_lingua_2)
        window.testo_da_tradurre.bind(
            "<KeyPress-Return>", window.traduzione
        )  # KeyPress-Return è l'invio

    #    def framedx(window):
    #        global linguadx2
    #        dxframe = tk.Frame()
    #        dxframe.grid(row=0, column=0, sticky="nw")
    #        dxframe.configure(background="#282623")
    #        linguadx2 = tk.Entry(dxframe, textvariable=window.linguadx)
    #        linguadx2.grid(row=0, column=0)
    #        linguadx2.config(background="#444341")
    #        linguadx2.bind("<KeyPress-Return>", window.cerca_lingua_dx)
    #
    #    def framesx(window):
    #        pass
    #
    #    def cerca_lingua_sx(window):
    #        pass
    #
    #    def cerca_lingua_dx(window, event):
    #        linguadx3 = linguadx2.get()
    #        try:
    #        for i in range (len(lista_lingue)):
    #            if linguadx3 == list(lista_lingue[i]):
    #                lingua = lista_lingue[i]
    #        except ValueError:
    #            messagebox.showerror("Lingua non disponibile", "La lingua cercata non è disponibile.")

    # Prendo la lingua della parola che si vuole tradurre
    def prendi_lingua_1(window, event):
        global lingua
        numero = window.scelta.curselection()
        numero = list(numero)
        try:
            lingua = lista_lingue[numero[0]]
        except IndexError:
            pass

    # Prendo la lingua in cui si vuole tradurre la parola
    def prendi_lingua_2(window, event):
        global lingua_2
        numero_2 = window.scelta_2.curselection()
        numero_2 = list(numero_2)
        try:
            lingua_2 = lista_lingue[numero_2[0]]
        except IndexError:
            pass
        window.sistema()

    # Prendo solo la sillaba tra parentesi delle lingue selezionate
    def sistema(window):
        global lingua
        global lingua_2
        i = 0
        k = 0
        # Sillaba tra parentesi di fianco alla lingua della parola che si vuole tradure
        for i in range(len(list(lingua))):
            if lingua[i] == "(":
                lingua = lingua[i + 1 : -2]
                break
        # Sillaba tra parentesi di fianco alla lingua in cui si vuole tradure
        for k in range(len(list(lingua_2))):
            if lingua_2[k] == "(":
                lingua_2 = lingua_2[k + 1 : -2]
                break
        window.traduzione2()

    # Con le prossime 2 funzioni prendo la parola inserita, la traduco nella lingua desiderata e la faccio vedere (1 è per l"invio, l"altra per quando si schiaccia il bottone)
    def traduzione(window, event):
        try:
            # Prendo il testo da tradurre
            testo = window.testo_da_tradurre.get()
            # Lo traduco
            translator = Translator(from_lang=lingua, to_lang=lingua_2)
            # Lo salvo in una variabile
            h = translator.translate(testo)
            # Lo faccio vedere
            window.nome_tradotto.set(h)
        except NameError:
            messagebox.showerror(
                "Lingua non inserita", "Devi inserire la lingua da cui stai traducendo."
            )

    def traduzione2(window):
        try:
            # Prendo il testo da tradurre
            testo = window.testo_da_tradurre.get()
            # Lo traduco
            translator = Translator(from_lang=lingua, to_lang=lingua_2)
            # Lo salvo in una variabile
            h = translator.translate(testo)
            # Lo faccio vedere
            window.nome_tradotto.set(h)
        except NameError:
            messagebox.showerror(
                "Lingua non inserita",
                "Devi inserire la lingua da cui stai traducendo / in cui vuoi tradurre.",
            )

    # Leggo la parola che si vuole tradurre
    def leggi_1(window):
        # Prendo il testo da tradurre
        testo1 = window.testo_da_tradurre.get()
        # Lo leggo
        engine.say(testo1)
        engine.runAndWait()

    # Leggo la parola tradotta
    def leggi_2(window):
        # Prendo il testo tradotto
        testo2 = window.testo_tradotto.get()
        # Lo leggo
        engine.say(testo2)
        engine.runAndWait()

    # Faccio vedere la guida in un"altra finestra
    def informazioni(window):
        # Inizio impostazioni finestra
        info_finestra = tk.Toplevel()
        info_finestra.title("Guida")
        info_finestra.configure(background="#282623")
        info_finestra.resizable(0, 0)
        info_finestra.iconbitmap("Icona.ico")
        # Fine impostazioni finestra
        guida0 = tk.Label(
            info_finestra,
            text="GUIDA:",
            font=("Helvetica", 11),
            fg="#d1127e",
            bg="#282623",
        ).grid(row=0, column=0, sticky="we")
        guida1 = tk.Label(
            info_finestra,
            text="Selezionare la lingua da cui si vuole tradurre dal riquadro blu a sinistra (doppio click)",
            font=("Helvetica", 11),
            fg="#12e8bd",
            bg="#282623",
        ).grid(row=1, column=0, sticky="we")
        guida2 = tk.Label(
            info_finestra,
            text="Selezionare la lingua in cui si vuole tradurre dal riquadro rosso a destra (doppio click)",
            font=("Helvetica", 11),
            fg="#12e8bd",
            bg="#282623",
        ).grid(row=2, column=0, sticky="we")
        guida3 = tk.Label(
            info_finestra,
            text="Inserire la parola da tradurre nel riquadro in basso a sinistra (sopra all'altoparlante) e premere invio o la freccia",
            font=("Helvetica", 11),
            fg="#12e8bd",
            bg="#282623",
        ).grid(row=3, column=0, sticky="we")
        guida4 = tk.Label(
            info_finestra,
            text="Per ascoltare le parole/frasi premere l'altoparlante (alcune lingue non sono disponibili)",
            font=("Helvetica", 11),
            fg="#12e8bd",
            bg="#282623",
        ).grid(row=4, column=0, sticky="we")


def main():
    w = Window()
    w.mainloop()


# Salvo le lingue disponibili in una lista, per poi inserirle nelle listbox
# Apro il file contenente l"elenco delle lingue
lista_lingue_aperta = open(os.getcwd().replace(r"\Immagini", r"\Lingue.txt"), "r")
# Salvo le lingue in una lista
lista_lingue = lista_lingue_aperta.readlines()
# Chiudo il file che ho aperto in precedenza
lista_lingue_aperta.close()
# Ordino la lista con le lingue in ordine alfabetico
lista_lingue.sort()

main()
