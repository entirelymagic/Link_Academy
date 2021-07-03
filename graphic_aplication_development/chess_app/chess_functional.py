from tkinter import *

window = Tk()

N = 6
square_width = 100
canvas_width = N * square_width

board = Canvas(window, width=canvas_width, height=canvas_width, bg="black")
board.pack()

global stiva, solutii
stiva = []
solutii = []
k = 0


def nivel_stiva():
    return len(stiva)


def print_stiva():
    print("Stiva este formata din:")
    for item in stiva:
        print(item)


def verifica_pe_verticala(pozitie):
    print("da fail la verifica_pe_verticala")
    return True if pozitie not in stiva else False


def verifica_pe_diagonala(pozitie):
    for index, value in enumerate(stiva):
        # if  abs(index + 1 - value) ==  abs(nivel_stiva() + 1 - pozitie ):
        if abs(index - nivel_stiva()) == abs(value - pozitie):
            print("da fail la verifica_pe_diagonala la index si valoare ", index, value)
            print("da fail la verifica_pe_diagonala la index si valoare ", nivel_stiva(), pozitie)
            return False
        if abs(index + 1 + value) == abs(nivel_stiva() + 1 + pozitie):
            print("da fail la verifica_pe_diagonala a 2a la index si valoare", index, value)
            return False
    return True


global next_position
next_position = 1


def backtracking_queens():
    global stiva, solutii, next_position
    stiva.append(next_position)
    k = 0
    while (nivel_stiva() >= 0):
        print("Intra in while")
        print_stiva()
        # verific daca trebuie adaugat
        if nivel_stiva() < N:
            # adaug
            print("nivel_stiva() < N")
            if next_position < N:
                next_position = next_position + 1
                x = next_position
                print("stiva[-1] < N")
                print("x=", x)
                if verifica_pe_diagonala(x) and verifica_pe_verticala(x):
                    print("x este verificat")
                    stiva.append(x)
                    next_position = 0

                else:
                    print("x nu este verificat")
                    # stiva.pop()
            else:
                print("nivel_stiva() = N")
                if nivel_stiva() > 0:
                    next_position = stiva[-1]
                    stiva.pop()
                else:
                    return
        else:
            # verific daca este o solutie
            print("Solutie")
            new_stiva = stiva.copy()
            solutii.append(new_stiva)
            next_position = stiva[-1]
            for item in stiva:
                print(item)
            for item in solutii:
                print(item)
            stiva.pop()


backtracking_queens()

print("Solutiile sunt:")
for solution in solutii:
    print(solution)
    for item in solution:
        print(item)

prima_solutie = solutii[1]

# prima_solutie = [2,4,1,3]

indent_text = square_width / 2

for i in range(0, N):
    for j in range(0, N):
        if (i + j + 1) % 2:
            board.create_rectangle((i * square_width), (j * square_width), (i * square_width) + square_width,
                                   (j * square_width) + square_width, fill="white")
        if prima_solutie[j] == i + 1:
            print("i= ", i, " j=", j)
            board.create_text((indent_text + (i * square_width)), (indent_text + (j * square_width)), text=u"👑",
                              font=('Arial', 50), fill="red")

window.mainloop()
