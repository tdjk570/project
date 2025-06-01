import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Крестики-нолики")
        self.root.resizable(False, False)
        
        # Настройки игры
        self.board_size = 3
        self.current_player = "X"
        self.board = [["" for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.game_over = False
        
        # Стиль
        self.button_font = ("Arial", 24, "bold")
        self.button_width = 5
        self.button_height = 2
        
        # Создаем игровое поле
        self.create_board()
        
        # Кнопка сброса игры
        self.reset_button = tk.Button(
            self.root, 
            text="Новая игра", 
            font=("Arial", 12), 
            command=self.reset_game
        )
        self.reset_button.grid(row=self.board_size, columnspan=self.board_size, pady=10)
    
    def create_board(self):
        """Создает игровое поле из кнопок"""
        self.buttons = []
        for row in range(self.board_size):
            button_row = []
            for col in range(self.board_size):
                button = tk.Button(
                    self.root, 
                    text="", 
                    font=self.button_font,
                    width=self.button_width,
                    height=self.button_height,
                    command=lambda r=row, c=col: self.on_click(r, c)
                )
                button.grid(row=row, column=col, padx=5, pady=5)
                button_row.append(button)
            self.buttons.append(button_row)
    
    def on_click(self, row, col):
        """Обработчик клика по клетке"""
        if self.game_over or self.board[row][col] != "":
            return
            
        # Делаем ход
        self.board[row][col] = self.current_player
        self.buttons[row][col].config(text=self.current_player)
        
        # Проверяем победу
        if self.check_win(row, col):
            self.game_over = True
            messagebox.showinfo("Победа!", f"Игрок {self.current_player} победил!")
            return
        
        # Проверяем ничью
        if self.check_draw():
            self.game_over = True
            messagebox.showinfo("Ничья!", "Игра закончилась вничью!")
            return
            
        # Меняем игрока
        self.current_player = "O" if self.current_player == "X" else "X"
    
    def check_win(self, row, col):
        """Проверяет, выиграл ли текущий игрок"""
        # Проверка строки
        if all(self.board[row][c] == self.current_player for c in range(self.board_size)):
            return True
        
        # Проверка столбца
        if all(self.board[r][col] == self.current_player for r in range(self.board_size)):
            return True
        
        # Проверка главной диагонали
        if row == col and all(self.board[i][i] == self.current_player for i in range(self.board_size)):
            return True
        
        # Проверка побочной диагонали
        if row + col == self.board_size - 1 and all(self.board[i][self.board_size-1-i] == self.current_player for i in range(self.board_size)):
            return True
        
        return False
    
    def check_draw(self):
        """Проверяет, закончилась ли игра вничью"""
        return all(self.board[r][c] != "" for r in range(self.board_size) for c in range(self.board_size))
    
    def reset_game(self):
        """Сбрасывает игру"""
        self.current_player = "X"
        self.board = [["" for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.game_over = False
        
        for row in range(self.board_size):
            for col in range(self.board_size):
                self.buttons[row][col].config(text="")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    game.run()
