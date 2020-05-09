from tkinter import *
import TextDecoderV2 as TD2


class Error(Exception):
    pass
class NoFileError(Error):
    pass
class NoEncryption(Error):
    pass

def onBtnClick():
    inputFile =""
    file_check = False
    
    while(True):
        try:
            inputFile += inputBox.get()
            if inputFile == "" or inputFile == " ":
                raise NoFileError
            f = open(inputFile + ".txt", 'r')
            line1 = f.readline(-1).strip()
            if line1 != "3NCRY":
                raise NoEncryption
        except FileNotFoundError:
            inputBox.delete(0, END)
            inputBox.insert(0, '***Invalid File***')
        except NoFileError:
            inputBox.insert(0, '***Field Required***')
        except NoEncryption:
            inputBox.delete(0, END)
            inputBox.insert(0, '***This file is not encrypted***')
        else:
            file_check = True
            break
        
    
    if '***Field Required***' in inputFile:
        file_check = False
        
    if '***This file is not encrypted***' in inputFile:
        file_check = False
        
    if (file_check):
        textEncoder = TD2.main(inputFile)
        onBtnClear()
            
def onBtnClear():
    inputBox.delete(0, END)
    inputBox.update()
    
root_window = Tk()
root_window.title("A Simple Decryption Program")
root_window.geometry("500x300")
root_window.resizable(False, False)
root_window.configure(background = "black")


instruction_label1 = Label(root_window, text = "Enter the name of the file you would like to decrypt and a name for the file.", bg = "black", fg = "white").grid(row = 1, column = 0, padx = 60, pady =5)
instruction_label2 = Label(root_window, text = "that you'd like to output the decoded message to, into the text boxes below.", bg = "black", fg = "white").grid(row = 2, column = 0, padx = 60, pady =5)
instruction_label3 = Label(root_window, text = 'Then press the "Decrypt It" button to proceed. Press the "Clear All" to restart.', bg = "black", fg = "white").grid(row = 3, column = 0, padx = 20, pady =5)


Label(root_window, text = "File Name: ", bg = "black", fg = "white").grid(row = 4, column = 0, padx = 30, sticky = W)
inputBox = Entry(root_window, width=30, bg = "white")
inputBox.grid(row = 4, column = 0, padx = 10, pady = 10)


spacer = Label(root_window, text = "", bg = "black").grid(row = 6, column = 0)
Button(root_window, text = "Decrypt It", width = 10, command = onBtnClick).grid(row = 7, column = 0)
Button(root_window, text = "Clear All", width = 10, command = onBtnClear).grid(row = 9, column = 0)


root_window.mainloop()
