import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x420")

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right",
                              bg="#f0f0f0", bd=0, relief="flat")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)
        separator = tk.Frame(root, height=2, bd=1, relief="sunken", bg="#999999")
        separator.pack(fill="x", padx=4, pady=(0, 5))

        # 버튼 생성
        buttons = [
            ['C', '/', '*', '⭠'],
            ['7', '8', '9', '-'],
            ['4', '5', '6', '+'],
            ['1', '2', '3', '.'],
            ['0', '=']
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                if char == 'C':
                    fg_color = "red"
                else:
                    fg_color = "black"
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    fg = fg_color,
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both", padx=4, pady=4)

    def on_click(self, char):
        if not char:
            return
        if char == 'C':
            self.expression = ""
        #backspace기능
        elif char == '⭠':
            self.expression = self.expression[:-1]
        #"."중복 방지 및 "."을 맨 처음 입력시 "0."으로 출력
        elif char == '.':
            last_number = self.expression.split('+')[-1].split('-')[-1].split('*')[-1].split('/')[-1]
            if not self.expression or self.expression[-1] in '+-*/':
                self.expression += '0.'
            elif '.' in last_number:
                return
            else:
                self.expression += '.'
        #연산자 중복 방지
        elif char in '+-*/.' and (not self.expression or self.expression[-1] in "+-*/."):
            self.expression = self.expression[:-1] + char
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except ZeroDivisionError:
                self.expression = "0으로 나눌 수 없습니다"
            except Exception:
                self.expression = "유효하지 않음"
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)



