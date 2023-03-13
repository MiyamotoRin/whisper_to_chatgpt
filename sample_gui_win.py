# tkinterのインポート
import tkinter as tk
from tkinter import ttk

import mov_transcription
import txt_summerize

def run():
    mov_transcription.transcription('small', 'Japanese')
    txt_summerize.summerize()
    with open('sum.txt', mode='r', encoding='utf-8') as f:
        text = f.read()
        text = text.replace('。', '。\n')
        result_label.configure(text=text)

# ウインドウの作成
root = tk.Tk()
root.title("yt_summerize")
root.geometry("350x150")

# テキストボックス設置 <---追加するコード
url_box = tk.Entry(width = 40)
url_box.place(x = 20, y = 30)

url_label = tk.Label(root, text = "Input Youtube URL")
url_label.place(x = 20, y = 5)

# Runボタン設置
run_button = tk.Button(root, text = "Run", command=run)
run_button.place(x = 160, y = 60)

# 結果表示用のラベル設置
result_label = tk.Label(root, text="Results will be displayed here")
result_label.place(x=20, y=90)

# ウインドウ状態の維持
root.mainloop()
