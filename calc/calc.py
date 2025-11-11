import tkinter as tk

def writeLabel(mode):
    global regA
    if regA % 1==0:
        regA=int(regA)
    else:
        regA=float(format(regA,'.6'))
    label["text"]=str(regA)   
    
def on_button_click(event):
    global regA
    global numberInput
    global mode
    button_text = event.widget.cget("text")
    #print(f"{button_text}ボタンが押されました")
    if button_text == "+/-":
        mode=""
        regA=-regA
        writeLabel("")
    elif button_text == "C":
        #reg=0
        mode=""
        label["text"]+="0"
    elif button_text == "√":
        regA=regA**0.5
        mode=""
        writeLabel("")
    elif numberInput: #数値モード
        print(f"数値モード{button_text}")
        if button_text in ("0123456789."):
            #数字の入力
            #符号と小数点を除き10文字を超えたら数字の入力を拒否
            txt=label["text"]
            minous = True if txt[0]=="-" else False
            dot = True if "." in txt else False
            length=len(txt)-(1 if minous else 0)-(1 if dot else 0)
            print(dot)
            if button_text==".":
                if not dot:
                    label["text"]+="."
            elif txt=="0":
                label["text"]=button_text
            elif length<10:
                label["text"]+=button_text
            regA=float(label["text"])
        elif button_text in ("+-X/="):
            #機能ボタンを押されたら数字を確定し表示値を計算値に更新
            numberInput=False
            if mode == "+":
                regA+=float(label["text"])
                #print(label["text"])
            elif mode == "X":
                regA*=float(label["text"])
            elif mode == "/":
                print(f"{regA} {label['text']}")
                regA=float(regA)/float(label["text"])
                print(regA)
            elif mode == "-":
                regA-=float(label["text"])
            elif mode == "":
                regA=float(label["text"])
            mode=button_text
            if regA%1==0:
                regA=int(regA)
            label["text"]=f"{regA}{mode}"
    else: #機能選択モード
        print(f"機能モード{button_text}")
        if button_text in ("0123456789"):
            #数字ボタンを押されたら数字入力モードへ
            label["text"]=button_text
            #regA=float(label["text"])
            numberInput=True
        elif button_text==".":
            label["text"]="0."
            #regA=0
            numberInput=True
            
        elif button_text in ("+-X/"):
            mode = button_text
            label["text"]=f"{regA}{mode}"
            
#メインウィンドウを作る
root = tk.Tk()
root.title("計算機")

regA=0 #前回の入力値または計算結果
mode=""   #現在の計算モードを示す
numberInput=False #数字を入力する状態 
# F---数字ボタン--->(T)---機能ボタン--->F
#                   L---数字ボタン

label=tk.Label(root, text="0")
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