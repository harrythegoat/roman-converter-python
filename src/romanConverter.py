from tkinter import *
from romanController import romanConverter

# Instantiate new romanClass
converter = romanConverter()

# General GUI configuration
window = Tk()
window.title('Roman Converter')
window.resizable(False,False)
window.configure(bg='lightblue')

# Convert function based on type(romanToInteger / integerToRoman)
def romanToNumberConverter():
    try:
        romanInput = entry.get().upper().replace(' ', '')
        result = converter.romanInteger(romanInput)
        return outputText.set(f'Output: {result}')
    except Exception as error:
        return outputText.set(f'Error: "{error}"')
    finally:
        outputLabel.config(text=outputText.get())

def numberToRomanConverter():
    try:
        numberInput = entry.get()
        result = converter.integerRoman(numberInput)
        return outputText.set(f'Output: {result}')
    except Exception as error:
        return outputText.set(f"Error: {error}")
    finally:
        outputLabel.config(text=outputText.get())

# Clear function
def clearEntry():
    try:
        entry.delete(0, len(entry.get()))
        return outputText.set('**Output will appear here**')
    except Exception as error:
        return outputText.set(f"Error: {error}")
    finally:
        outputLabel.config(text=outputText.get())

# Set global text for output label
outputText = StringVar()
outputText.set('**Output will appear here**')

# GUI: Label components for guides
guide1 = Label(window, text='1. Supported roman numeral range from 1 - 3999', bg='lightblue').grid(row=0, columnspan=3, padx=10, pady=2 ,sticky='w')
guide2 = Label(window, text='2. Supported roman syllables are "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"',  bg='lightblue').grid(row=1, columnspan=3, padx =10, pady=2, sticky='w')
guide3 = Label(window, text='3. You may enter roman or integer value.', bg='lightblue').grid(row=2, columnspan=3, padx=10, pady=2, sticky='w')
guide4 = Label(window, text='4. Click on buttons you wish to convert the value to or clear your entry.', bg='lightblue').grid(row=3, columnspan=3, padx=10, pady=2, sticky='w')

# GUI: Input (Entry) component
entry = Entry(window, width=100, borderwidth=2, justify='center')
entry.grid(row=4, columnspan=3, padx=10, pady=10)

# GUI: Button components
button1 = Button(window, text='Roman to Integer', padx=20, pady=20, command= lambda: romanToNumberConverter()).grid(row=5, column=0)
button2 = Button(window, text='Integer to Roman', padx=20, pady=20, command= lambda: numberToRomanConverter()).grid(row=5, column=1)
button3 = Button(window, text='Click to Clear', padx=20, pady=20, command = lambda: clearEntry()).grid(row=5, column=2)

# GUI: Label component for ouputing result
outputLabel = Label(window, text=f'Output: {outputText.get()}', bg='lightblue')
outputLabel.grid(row=6, columnspan=3, pady=10, ipadx=100)

# GUI: Main loop
window.mainloop()