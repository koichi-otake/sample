import tkinter as tk

def on_button_click(event):
    global reg
    global numberInput
    global mode
    button_text = event.widget.cget("text")
    #print(f"{button_text}ボタンが押されました")
    if numberInput:
        if button_text == "C":
            #reg=0
            #mode=""
            label["text"]=f"0"
        elif button_text == "+/-":
            mode=""
            reg=-float(label["text"])
            if reg%1==0:
                reg=int(reg)
            label["text"]=f"{reg}{mode}"
        elif button_text == "√":
            reg=float(label["text"])**0.5
            mode=""
            numberInput=True
            label["text"]=f"{reg}{mode}"
        elif len(label["text"])<10 and button_text in ("0123456789"):
            #数字の入力
            #10文字を超えたら数字の入力を拒否
            label["text"]+=button_text
        elif button_text in ("+-X/="):
            #機能ボタンを押されたら数字を確定し表示値を計算値に更新
            numberInput=False
            if mode == "+":
                reg+=float(label["text"])
            elif mode == "X":
                reg*=float(label["text"])
            elif mode == "/":
                reg/=float(label["text"])
            elif mode == "-":
                reg-=float(label["text"])
            elif mode == "":
                reg=float(label["text"])
            mode=button_text
            if reg%1==0:
                reg=int(reg)
            label["text"]=f"{reg}{mode}"
    else:
        if button_text in ("0123456789"):
            #数字ボタンを押されたら数字入力モードへ
            label["text"]=button_text
            numberInput=True
        elif button_text in ("+-X/"):
            mode = button_text
            reg=-reg
            label["text"]=f"{reg}{mode}"
            
#メインウィンドウを作る
root = tk.Tk()
root.title("計算機")

reg=0 #前回の入力値または計算結果
mode=""   #現在の計算モードを示す
numberInput=False #数字を入力する状態 
# F---数字ボタン--->(T)---機能ボタン--->F
#                   L---数字ボタン

label=tk.Label(root, text="")
label.config(font=("",24),bg="grey", width=12 ,height=1)
label.grid(row=0,column=0, columnspan=4)

#計算機のボタン名のリスト
buttonList = ( "C","+/-","√","/",
               "7","8","9","X",
               "4","5","6","-",
               "1","2","3","+",
               "0","00",".","=")

#ボタンを配置する 
for i in range(0,20):
    button = tk.Button(root, text=buttonList[i])
    button.config(font=("",24), width=3 ,height=1)
    button.grid(row=i//4+1,column=i%4)
    button.bind("<Button-1>",on_button_click)

#イベント待ちに移行
root.mainloop()