import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("電卓")

        # 入力フィールドの作成
        self.display = tk.Entry(master, width=30, justify="right")
        self.display.grid(row=0, column=0, columnspan=6, padx=5, pady=5)

        # ボタンの作成
        buttons = [
            '7', '8', '9', '/', 'sin', 'cos',
            '4', '5', '6', '*', 'tan', 'exp',
            '1', '2', '3', '-', 'log', 'sqrt',
            '0', '.', '=', '+', '!', 'MR'
        ]
        row = 1
        col = 0
        for button in buttons:
            if button == '=':
                tk.Button(master, text=button, width=5, command=self.calculate).grid(row=row, column=col, padx=5, pady=5)
            elif button in ['sin', 'cos', 'tan', 'exp', 'log', 'sqrt', '!']:
                tk.Button(master, text=button, width=5, command=lambda x=button: self.click_function(x)).grid(row=row, column=col, padx=5, pady=5)
            elif button == 'MR':
                tk.Button(master, text=button, width=5, command=self.memory_recall).grid(row=row, column=col, padx=5, pady=5)
            else:
                tk.Button(master, text=button, width=5, command=lambda x=button: self.click(x)).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 5:
                col = 0
                row += 1

        # クリアボタン
        tk.Button(master, text='C', width=5, command=self.clear).grid(row=5, column=0, padx=5, pady=5)

        # 履歴ボタン
        tk.Button(master, text='History', width=5, command=self.show_history).grid(row=5, column=1, padx=5, pady=5)

        # 履歴をクリアするボタン
        tk.Button(master, text='Clear History', width=11, command=self.clear_history).grid(row=5, column=2, columnspan=2, padx=5, pady=5)

        # メモリボタン
        tk.Button(master, text='MS', width=5, command=self.memory_store).grid(row=5, column=4, padx=5, pady=5)
        tk.Button(master, text='MC', width=5, command=self.memory_clear).grid(row=5, column=5, padx=5, pady=5)

        # 履歴を保存するリスト
        self.history = []

        # メモリ用の変数
        self.memory = None

    def click(self, key):
        if key == '=':
            self.calculate()
        else:
            self.display.insert(tk.END, key)

    def click_function(self, function):
        self.display.insert(tk.END, function + '(')

    def calculate(self):
        try:
            result = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
            self.history.append(self.display.get())
        except:
            messagebox.showerror("エラー", "無効な入力です")

    def clear(self):
        self.display.delete(0, tk.END)

    def show_history(self):
        history_window = tk.Toplevel(self.master)
        history_window.title("履歴")
        history_text = tk.Text(history_window, width=30, height=10)
        history_text.pack(padx=5, pady=5)
        for item in self.history:
            history_text.insert(tk.END, item + '\n')

    def clear_history(self):
        self.history.clear()

    def memory_store(self):
        self.memory = self.display.get()

    def memory_recall(self):
        if self.memory:
            self.display.insert(tk.END, self.memory)

    def memory_clear(self):
        self.memory = None

root = tk.Tk()
calc = Calculator(root)
root.mainloop()
