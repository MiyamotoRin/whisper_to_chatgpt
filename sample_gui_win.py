# tkinterのインポート
import tkinter as tk

# ウインドウの作成
root = tk.Tk()
# ウインドウのサイズ指定
root.geometry("350x100")

# Runボタン設置
run_button = tk.Button(root, text = "Run")
run_button.place(x = 160, y = 40)

# テキストボックス設置 <---追加するコード
input_box = tk.Entry(width = 40)
input_box.place(x = 10, y = 10)

# ウインドウ状態の維持
root.mainloop()
