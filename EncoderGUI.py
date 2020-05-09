from tkinter import *
import TextEncoderV2 as TE2

class Error(Exception):
    pass
class NoMessageError(Error):
    pass
class NoFileError(Error):
    pass

def onBtnClick():
    entered_text =""
    file = ""
    text_check = False
    file_check = False
    
    while(True):
        try:
            entered_text += inputBox.get()
            if entered_text == "" or entered_text == " ":
                raise NoMessageError
        except NoMessageError:
            inputBox.insert(0, '***Field Required***')
        else:
            text_check = True
            break
        
    
    while(True):
        try:
            file += fileBox.get()
            if file == "" or file ==" ":
                raise NoFileError
        except NoFileError:
            fileBox.insert(0, '***Field Required***')
        else:
            file_check = True
            break
        
    if '***Field Required***' in entered_text:
        text_check = False
    
    if '***Field Required***' in file:
        file_check = False
        
    if (text_check == True and file_check == True):
        textEncoder = TE2.main(entered_text, file)
        onBtnClear()
    

def onBtnClear():
    inputBox.delete(0, END)
    inputBox.update()
    fileBox.delete(0, END)
    fileBox.update()
        
    
root_window = Tk()
root_window.title("A Simple Encryption Program")
root_window.geometry("500x300")
root_window.resizable(False, False)
root_window.configure(background = "black")


instruction_label1 = Label(root_window, text = "Enter the message you would like to encrypt and a name for the file.", bg = "black", fg = "white").grid(row = 1, column = 0, padx = 60, pady =5)
instruction_label2 = Label(root_window, text = "that you'd like to output the coded message to, into the text boxes below.", bg = "black", fg = "white").grid(row = 2, column = 0, padx = 60, pady =5)
instruction_label3 = Label(root_window, text = 'Then press the "Encrypt It" button to proceed. Press the "Clear All" to restart.', bg = "black", fg = "white").grid(row = 3, column = 0, padx = 20, pady =5)


Label(root_window, text = "Message: ", bg = "black", fg = "white").grid(row = 4, column = 0, padx = 30, sticky = W)
inputBox = Entry(root_window, width=30, bg = "white")
inputBox.grid(row = 4, column = 0, padx = 10, pady = 10)


Label(root_window, text = "File Name: ", bg = "black", fg = "white").grid(row = 5, column = 0, padx = 30, sticky = W)
fileBox = Entry(root_window, width=30, bg = "white")
fileBox.grid(row = 5, column = 0, padx = 10, pady = 10)


spacer = Label(root_window, text = "", bg = "black").grid(row = 6, column = 0)
Button(root_window, text = "Encrypt It", width = 10, command = onBtnClick).grid(row = 7, column = 0)
Button(root_window, text = "Clear All", width = 10, command = onBtnClear).grid(row = 9, column = 0)


root_window.mainloop()
