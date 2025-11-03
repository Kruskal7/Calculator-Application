# calculator.py
import tkinter as tk
from math import sqrt

class Calculator(tk.Tk):
    def _init_(self):
        super()._init_()
        self.title("Calculator")
        self.geometry("360x520")
        self.resizable(False, False)
        self.configure(bg="#222")

        self.expression = ""
        self._create_widgets()
        self._bind_keys()

    def _create_widgets(self):
        # Display
        self.display_var = tk.StringVar()
        display = tk.Entry(self, textvariable=self.display_var, font=("Segoe UI", 28),
                           bd=0, bg="#111", fg="white", justify="right", insertbackground="white")
        display.pack(fill="both", ipady=18, padx=10, pady=(18, 6))

        # Buttons layout
        btn_frame = tk.Frame(self, bg="#222")
        btn_frame.pack(expand=True, fill="both", padx=10, pady=6)

        buttons = [
            ["C", "⌫", "%", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "−"],
            ["1", "2", "3", "+"],
            ["±", "0", ".", "="],
            ["(", ")", "^", "√"]
        ]

        for r, row in enumerate(buttons):
            row_frame = tk.Frame(btn_frame, bg="#222")
            row_frame.pack(expand=True, fill="both")
            for c, label in enumerate(row):
                btn = tk.Button(row_frame, text=label, font=("Segoe UI", 20),
                                bd=0, relief="ridge", command=lambda l=label: self.on_button_click(l))
                btn.pack(side="left", expand=True, fill="both", padx=6, pady=6)

    def _bind_keys(self):
        for key in "0123456789.+-*/()":
            self.bind(key, self._key_input)
        self.bind("<Return>", lambda e: self.on_button_click("="))
        self.bind("<BackSpace>", lambda e: self.on_button_click("⌫"))
        self.bind("<Escape>", lambda e: self.on_button_click("C"))
        # also map common keyboard synonyms
        self.bind("*", lambda e: self.on_button_click("×"))
        self.bind("/", lambda e: self.on_button_click("÷"))
        self.bind("^", lambda e: self.on_button_click("^"))

    def _key_input(self, event):
        ch = event.char
        if ch:
            if ch in "0123456789":
                self._append(ch)
            elif ch == ".":
                self._append(".")
            elif ch in "+-*/()":
                symbol = {"*":"×", "/":"÷"}.get(ch, ch)
                self._append(symbol)

    def on_button_click(self, label):
        if label == "C":
            self.expression = ""
            self._update_display()
        elif label == "⌫":
            self.expression = self.expression[:-1]
            self._update_display()
        elif label == "=":
            self._calculate()
        elif label == "±":
            self._toggle_sign()
        elif label == "%":
            self._apply_percent()
        elif label == "√":
            self._apply_sqrt()
        else:
            self._append(label)

    def _append(self, char):
        # normalize input characters for display
        self.expression += str(char)
        self._update_display()

    def _update_display(self):
        self.display_var.set(self.expression)

    def _sanitize_for_eval(self, expr):
        # Replace visual operators with Python equivalents.
        expr = expr.replace("×", "*").replace("÷", "/").replace("−", "-")
        # allow ^ as power
        expr = expr.replace("^", "")
        # handle percent: "50%" -> "(50/100)"
        # simple replacement: any number followed by % becomes (number/100)
        # we'll do a safe parse for trailing % signs
        i = 0
        out = ""
        while i < len(expr):
            ch = expr[i]
            if ch.isdigit() or ch == ".":
                j = i
                while j < len(expr) and (expr[j].isdigit() or expr[j] == "."):
                    j += 1
                number = expr[i:j]
                if j < len(expr) and expr[j] == "%":
                    out += f"({number}/100)"
                    i = j + 1
                else:
                    out += number
                    i = j
            else:
                out += ch
                i += 1
        return out

    def _calculate(self):
        if not self.expression:
            return
        expr = self._sanitize_for_eval(self.expression)
        # Disallow any names; use eval with empty globals and limited locals.
        try:
            # Provide sqrt function if user used "sqrt(" implicitly with √ button we transform it
            result = eval(expr, {"_builtins_": None}, {"sqrt": sqrt})
            # Format result: drop .0 for whole numbers
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.expression = str(result)
        except Exception:
            self.expression = "Error"
        self._update_display()

    def _toggle_sign(self):
        # toggle sign of the whole expression or last number
        if not self.expression:
            return
        # If expression is a plain number, toggle it
        try:
            sanitized = self._sanitize_for_eval(self.expression)
            val = eval(sanitized, {"_builtins_": None}, {"sqrt": sqrt})
            val = -val
            self.expression = str(val)
            self._update_display()
            return
        except Exception:
            # fallback: try to toggle last number
            i = len(self.expression) - 1
            while i >= 0 and (self.expression[i].isdigit() or self.expression[i] == "."):
                i -= 1
            # i is now index before last number
            prefix = self.expression[:i+1]
            number = self.expression[i+1:]
            if number:
                if number.startswith("-"):
                    number = number[1:]
                else:
                    number = "-" + number
                self.expression = prefix + number
                self._update_display()

    def _apply_percent(self):
        # append % symbol (handled in sanitize)
        self._append("%")

    def _apply_sqrt(self):
        # insert sqrt(...) or use unicode √ as prefix for a number
        # We'll append "√(" and user can type number and close
        self._append("sqrt(")  # since eval knows sqrt from locals

if __name__ == "_main_":
    app = Calculator()
    app.mainloop()

    # New feature: square root function added
import math

def sqrt(x):
    if x < 0:
        return "Error: negative input"
    return math.sqrt(x)
