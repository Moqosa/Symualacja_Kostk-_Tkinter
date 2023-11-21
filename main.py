import random
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk() #Tworzenie okna gry
root.title('Throw a dice') #Tworznie tytułu okna
root.geometry('500x500') #Wymiary okna

def draw(): #Funkcja odpowiadajaca za losowanie
    random_number = random.randint(1,6) #losowanie liczby
    img_path = f"{random_number}.png" #Ścieżka do wylosowanej grafiki
    picture = Image.open(img_path) #otworzenie grafiki


    picture_tk = ImageTk.PhotoImage(picture) #Przypisanie grafiki do tkintera
    label_picture.config(image=picture_tk) #Przypisanie grafiki do opowieniego label
    label_picture.image = picture_tk

button = tk.Button(root, text='Roll the dice', command=draw, height=2, width=10, font=('Arial, 18') , background='green') #Button do losowanie
button.pack()

label_picture = tk.Label(root)  #Label do wyswietalnia grafiki
label_picture.pack()


#Symualacja rzutut kostką
text = tk.Label(root, text='Dice throwing simulation \nEnter how many times you want to roll the dice', font=('Arial, 12'))
text.pack()

def simulation(): #Funckaj do symluacji rzutu
    user_input_simulation = int(entry.get()) #Ustawienie typu zmiennej na int
    tab_random_number_simulation = [] #Lista do przechowywania wyników

    for i in range(1, user_input_simulation+1): #Pętla do symalcji
        random_number_simulation = random.randint(1, 6) #Losowanie oczka
        tab_random_number_simulation.append(random_number_simulation) #Dodawanie wyniku do listy
        label_result_of_simulation.config(text=f"Drawing results: {tab_random_number_simulation}", font=('Arial, 12')) #Wyświetalnie losowania
        lenght_tab = len(tab_random_number_simulation) #Sprawdzanie długości listyw w celu policzenia średniego wyniku
        tab_sum = sum(tab_random_number_simulation) #Sumowanie wartości z tablicy
        average_result.config(text=f"Average value: {tab_sum/lenght_tab}", font=('Arial, 12')) #Obliczanie i wyświetalnie średniej wartości oczek


entry = tk.Entry(root) #Pole input
entry.pack()

button_simulation = tk.Button(root, command=simulation, text='Simulate a dice roll', font=('Arial, 18'), background='green', height=2, width=15) #Przycisk do symulacji
button_simulation.pack()

label_result_of_simulation = tk.Label(root) #Pole do wyświetalnie średniej wartości oczek
label_result_of_simulation.pack()

average_result = tk.Label(root)
average_result.pack()


root.mainloop()
