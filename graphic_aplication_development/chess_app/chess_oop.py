from tkinter import *
from time import time

class Chess():
    def __init__(self, window) -> None:
        # UI
        self.N = 4
        self.square_width = 100
        self.canvas_width = self.N * self.square_width
        self.dashboard = Frame(window, width=self.canvas_width, height=self.canvas_width // 2)
        self.dashboard.pack()
        self.board = Canvas(window, width=self.canvas_width, height=self.canvas_width, bg="black")
        self.board.pack()
        self.indent_text = self.square_width / 2

        self.next_sol_button = Button(self.dashboard, text="Next Solution", command=self.draw_next_solution)
        self.next_sol_button.grid(row=0, column=0)

        self.solution_no_label = Label(self.dashboard, text=f"Solution 1/{self.N}")
        self.solution_no_label.grid(row=0, column=1)

        self.N_ui = StringVar()
        self.N_ui.set(self.N)
        self.N_spinbox = Spinbox(self.dashboard, from_=4, to_=10, textvariable=self.N_ui, command=self.reset_board)
        self.N_spinbox.grid(row=1, column=0)
        self.all_N_solutions = {}
        self.time_label = Label(self.dashboard, text=f"Time to calculate ")
        self.time_label.grid(row=1, column=1)
        # Algorithm
        self.stiva = []
        self.solutii = []

        self.next_position = 1
        self.solution_index = 0
        self.draw_board()

    def config_init(self):

        self.stiva = []
        self.solutii = []
        self.next_position = 1
        self.solution_index = 0
        self.canvas_width = self.N * self.square_width
        self.board.configure(width=self.canvas_width, height=self.canvas_width, )

    def draw_board(self):
        self.backtracking_queens()
        print("Solutii")
        self.draw_chess_board()
        self.draw_queens_on_board()

    def reset_board(self):
        self.N = int(self.N_ui.get())
        self.config_init()
        print("New N=", N)
        self.board.delete("all")
        self.draw_board()

    def draw_chess_board(self):
        for i in range(0, self.N):
            for j in range(0, self.N):
                if (i + j + 1) % 2:
                    self.board.create_rectangle((i * self.square_width), (j * self.square_width),
                                                (i * self.square_width) + self.square_width,
                                                (j * self.square_width) + self.square_width, fill="white")

    def draw_queens_on_board(self):
        solution = self.solutii[self.solution_index]
        for i in range(0, self.N):
            for j in range(0, self.N):
                if solution[j] == i + 1:
                    self.board.create_text((self.indent_text + (i * self.square_width)),
                                           (self.indent_text + (j * self.square_width)), text=u"👑", font=('Arial', 50),
                                           fill="red", tags="queen")
        self.solution_no_label.configure(text=f"Solution {self.solution_index + 1}/{len(self.solutii)}")
        self.time_label.configure(text=f"time to calculate {self.all_N_solutions[str(self.N)]['time']}")
    def draw_next_solution(self):
        print("Should next solution")
        self.solution_index += 1
        if self.solution_index == len(self.solutii):
            self.solution_index = 0
        self.board.delete("queen")
        self.draw_queens_on_board()

    def nivel_stiva(self):
        return len(self.stiva)

    def print_stiva(self):
        print("Stiva este formata din:")
        for item in self.stiva:
            print(item)

    def verifica_pe_verticala(self, pozitie):
        print("da fail la verifica_pe_verticala")
        return True if pozitie not in self.stiva else False

    def verifica_pe_diagonala(self, pozitie):
        for index, value in enumerate(self.stiva):
            # if  abs(index + 1 - value) ==  abs(nivel_stiva() + 1 - pozitie ):
            if abs(index - self.nivel_stiva()) == abs(value - pozitie):
                print("da fail la verifica_pe_diagonala la index si valoare ", index, value)
                print("da fail la verifica_pe_diagonala la index si valoare ", self.nivel_stiva(), pozitie)
                return False
            if abs(index + 1 + value) == abs(self.nivel_stiva() + 1 + pozitie):
                print("da fail la verifica_pe_diagonala a 2a la index si valoare", index, value)
                return False
        return True

    def backtracking_queens(self):
        print(self.all_N_solutions)
        if not str(self.N) in self.all_N_solutions:
            self.do_backtracking()
        else:
            self.solutii = self.all_N_solutions[str(self.N)]["solution"]

    def do_backtracking(self):
        self.stiva.append(self.next_position)
        self.k = 0
        start = time()
        while (self.nivel_stiva() >= 0):
            print("Intra in while")
            # verific daca trebuie adaugat
            if self.nivel_stiva() < self.N:
                # adaug
                print("nivel_stiva() < N")
                if self.next_position < self.N:
                    self.next_position = self.next_position + 1
                    x = self.next_position
                    print("stiva[-1] < N")
                    print("x=", x)
                    if self.verifica_pe_diagonala(x) and self.verifica_pe_verticala(x):
                        print("x este verificat")
                        self.stiva.append(x)
                        self.next_position = 0

                    else:
                        print("x nu este verificat")
                        # stiva.pop()
                else:
                    print("nivel_stiva() = N")
                    if self.nivel_stiva() > 0:
                        self.next_position = self.stiva[-1]
                        self.stiva.pop()
                    else:
                        end = time()
                        time_taken = end-start
                        self.all_N_solutions[str(self.N)] = {"solution": self.solutii,
                                                             "time": str(time_taken)}

                        return
            else:
                # verific daca este o solutie
                print("Solutie")
                new_stiva = self.stiva.copy()
                self.solutii.append(new_stiva)
                self.next_position = self.stiva[-1]
                for item in self.stiva:
                    print(item)
                for item in self.solutii:
                    print(item)
                self.stiva.pop()


def main():
    window = Tk()
    chessboard = Chess(window)
    window.mainloop()


if __name__ == "__main__": main()