# tkinterのインポート
import tkinter as tk

import mov_transcription
import txt_summerize

def run():
    mov_transcription.transcription('small', language_box.get())
    txt_summerize.summerize()

# ウインドウの作成
root = tk.Tk()
# ウインドウのサイズ指定
root.geometry("350x100")

# テキストボックス設置 <---追加するコード
language_box = tk.Entry(width = 40)
language_box.place(x = 10, y = 10)

# Runボタン設置
run_button = tk.Button(root, text = "Run", command=run)
run_button.place(x = 160, y = 40)

# ウインドウ状態の維持
root.mainloop()
