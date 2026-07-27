import tkinter as tk
import random #ランダムを使うのでimport文を追加

def dispLabel():
    kuji = ['大吉', '中吉', '小吉', '凶'] #おみくじのリストを用意
    lbl.configure(text=random.choice(kuji)) #ランダムに一つ選んで用意

root = tk.Tk() #ここから先はこれまでのプログラムと一緒
root.geometry("200x100")

lbl = tk.Label(text="LABEL") #ラベルを作る
btn = tk.Button(text="PUSH", command = dispLabel) # ボタンを作る

lbl.pack()
btn.pack()
tk.mainloop()
