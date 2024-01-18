#-*- coding: utf8 -*-
import tkinter as tk
import tkinter.messagebox as tkm

import GPT

root = tk.Tk()
chat = GPT.Chat("ここにAPIキーを入れる")

# ウインドウのタイトル
root.title("GPT-access")

# 送信ボタン
Button = tk.Button(text="誰か作って")
Button.pack(side="bottom")

print("unko")

root.mainloop()