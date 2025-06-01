import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

# Создаем JSON файл с данными, если его нет
if not os.path.exists('alphabet_data.json'):
    data = {
        "А": "Аист - крупная перелетная птица.",
        "Б": "Барсук - ночной зверь с полосатой мордой.",
        "В": "Волк - хищное животное, живущее в лесу.",
        # ... другие буквы
        "Я": "Ящерица - маленькая рептилия, любящая солнце."
    }
    with open('alphabet_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_data():
    with open('alphabet_data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def save_data(data):
    with open('alphabet_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def show_letter_info(letter):
    data = load_data()
    info = data.get(letter, "Информация для этой буквы пока отсутствует.")
    
    info_window = tk.Toplevel(root)
    info_window.title(f"Буква {letter}")
    info_window.geometry("400x300")
    
    if theme_var.get() == "dark":
        info_window.configure(bg='#333333')
        text_color = 'white'
    else:
        text_color = 'black'
    
    tk.Label(info_window, text=f"Буква {letter}", font=('Arial', 18), fg=text_color, 
             bg=info_window.cget('bg')).pack(pady=10)
    
    tk.Label(info_window, text=info, wraplength=380, justify='left', 
             fg=text_color, bg=info_window.cget('bg')).pack(pady=10)
    
    if letter.lower() in ['а', 'о', 'у', 'ы', 'э', 'е', 'ё', 'и', 'ю', 'я']:
        tk.Label(info_window, text="(гласная)", fg='red', 
                 bg=info_window.cget('bg')).pack()

def change_theme():
    theme = theme_var.get()
    if theme == "dark":
        root.configure(bg='#333333')
        style.configure('TButton', background='#555555', foreground='white')
        style.configure('TFrame', background='#333333')
    else:
        root.configure(bg='SystemButtonFace')
        style.configure('TButton', background='SystemButtonFace', foreground='black')
        style.configure('TFrame', background='SystemButtonFace')

def add_new_letter():
    def save_new_letter():
        letter = entry_letter.get().strip().upper()
        info = entry_info.get("1.0", tk.END).strip()
        
        if not letter or not info:
            messagebox.showwarning("Ошибка", "Все поля должны быть заполнены!")
            return
        
        if len(letter) != 1 or not letter.isalpha():
            messagebox.showwarning("Ошибка", "Введите одну букву!")
            return
        
        data = load_data()
        data[letter] = info
        save_data(data)
        
        messagebox.showinfo("Успех", f"Информация для буквы {letter} сохранена!")
        add_window.destroy()
        update_alphabet_buttons()
    
    add_window = tk.Toplevel(root)
    add_window.title("Добавить новую букву")
    add_window.geometry("400x300")
    
    tk.Label(add_window, text="Буква:").pack(pady=5)
    entry_letter = tk.Entry(add_window, width=5, font=('Arial', 14))
    entry_letter.pack()
    
    tk.Label(add_window, text="Информация:").pack(pady=5)
    entry_info = tk.Text(add_window, width=40, height=10)
    entry_info.pack()
    
    tk.Button(add_window, text="Сохранить", command=save_new_letter).pack(pady=10)

def update_alphabet_buttons():
    for widget in alphabet_frame.winfo_children():
        widget.destroy()
    
    data = load_data()
    letters = sorted(data.keys())
    
    for i in range(0, len(letters), 6):
        row_frame = ttk.Frame(alphabet_frame)
        row_frame.pack(fill='x', pady=5)
        
        for letter in letters[i:i+6]:
            btn = ttk.Button(row_frame, text=letter, width=3, 
                           command=lambda l=letter: show_letter_info(l))
            btn.pack(side='left', padx=5)

# Создаем главное окно
root = tk.Tk()
root.title("Алфавитный справочник")
root.geometry("600x400")

style = ttk.Style()
theme_var = tk.StringVar(value="light")

# Меню
menubar = tk.Menu(root)
root.config(menu=menubar)

settings_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Настройки", menu=settings_menu)
settings_menu.add_checkbutton(label="Темная тема", variable=theme_var, 
                            onvalue="dark", offvalue="light", command=change_theme)
settings_menu.add_command(label="Добавить букву", command=add_new_letter)

# Основной интерфейс
main_frame = ttk.Frame(root)
main_frame.pack(pady=20)

tk.Label(main_frame, text="Алфавитный справочник", font=('Arial', 20)).pack()

alphabet_frame = ttk.Frame(main_frame)
alphabet_frame.pack(pady=20)

update_alphabet_buttons()

root.mainloop()