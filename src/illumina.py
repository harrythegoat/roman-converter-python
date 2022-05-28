from tkinter import *

# General GUI configuration
window = Tk()
window.title('illumina - Roman Converter')
window.resizable(False,False)
window.configure(bg='lightblue')

# Convert function based on type(romanToInteger / integerToRoman)
def romanToNumberConverter():
    try:
        numVal = 0
        counter = 0
        romanInput = entry.get().upper().replace(' ', '')
        romanVal = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        
        if romanInput == "":
            return outputText.set(f'Error: Entry cannot be empty.')

        while counter < len(romanInput):
            if counter+1 < len(romanInput) and romanInput[counter:counter+2] in romanVal: # Verify if the input length is < 1 and input[0:2] is in romanVal dict
                numVal+=romanVal[romanInput[counter:counter+2]] # Accumulatively increment the numVal by romanVal[input[0:2]]
                counter+=2 # Counter increment by 2 because sliced 2 char from input
            else:
                numVal+=romanVal[romanInput[counter]]
                counter+=1
        
        if numVal > 3999:
            return outputText.set(f'Error: The roman numeral value is out of range.')
        
        return outputText.set(f'Output: The converted value is {numVal}.')
    except Exception:
        outputText.set(f'Error: Invalid roman syllable "{romanInput}".')
    finally:
        outputLabel.config(text=outputText.get())

def numberToRomanConverter():
    try:
        romanVal = ''
        counter = 0
        numberInput = int(entry.get()) # Exception Handled by TypeError, ValueError
        numberVal = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romanSyb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        if (len(str(numberInput)) > 4):
            return outputText.set(f'Error: Supported integer range is from 1 - 3999.')
        while numberInput > 0:
            print('Traversing...', counter)
            print(f"Set for range to... {numberInput} // {numberVal[counter]} = {numberInput // numberVal[counter]}")
            for _ in range(numberInput // numberVal[counter]):
                romanVal += romanSyb[counter] # Get romanSyb[counter] based on counter traversed
                numberInput -= numberVal[counter] # Minus numberInput with value from numberVal[counter]
            counter += 1
            # when numberInput not > 0 while breaks
        return outputText.set(f'Output: The converted value is {romanVal}.')
    except (TypeError, ValueError):
        return outputText.set(f'Error: Entry must be an integer from 1-3999.')
    except Exception:
        outputText.set(f'Error: Please contact administrator.')
    finally:
        outputLabel.config(text=outputText.get())

# Clear function
def clearEntry():
    entry.delete(0, len(entry.get()))
    return outputText.set('**Output will appear here**')

# Set global text for output label
outputText = StringVar()
outputText.set('**Output will appear here**')

# GUI: Label components for guides
guide1 = Label(window, text='1. Supported roman numeral range from 1 - 3999', bg='lightblue').grid(row=0, columnspan=3, pady=2)
guide2 = Label(window, text='2. Supported roman syllables are "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"',  bg='lightblue').grid(row=1, columnspan=3, pady=2)
guide3 = Label(window, text='3. You may enter roman or integer value.', bg='lightblue').grid(row=2, columnspan=3, pady=2)
guide4 = Label(window, text='4. Click on buttons you wish to convert the value to or clear your entry.', bg='lightblue').grid(row=3, columnspan=3, pady=2)

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