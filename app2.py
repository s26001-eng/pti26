import tkinter as tk #tkinterという機能をtkという名前で覚えるようにしている

def dispLabel(): #dispLabelという関数
    lbl.configure(text="こんにちは") #レベルの文字を「こんにちは」に変更する

root = tk.Tk() #画面を作る
root.geometry("200x100") #横200、縦100の画面サイズ

lbl = tk.Label(text="LABEL") #ラベルを作る
btn = tk.Button(text="PUSH", command = dispLabel) # ボタンを作る

lbl.pack() #ラベルを配置する
btn.pack() # ボタンを配置する
tk.mainloop() #ウィンドウを表示する
