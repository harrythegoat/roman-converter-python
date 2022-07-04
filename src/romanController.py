from multiprocessing.sharedctypes import Value

class romanConverter:
    def romanInteger(self, value):
        try:
            if not type(value) is str:
                return "Value must be string."
            
            if len(value) == 0:
                return "Value cannot be empty."
            
            result = 0
            counter = 0
            romanVal = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
            
            while counter < len(value):
                if value[counter:counter+2] in romanVal:
                    result += romanVal[value[counter:counter+2]]
                    counter+=2
                else:
                    result += romanVal[value[counter:counter+1]]
                    counter+=1
                
                if result > 3999:
                    return "Maximum roman value is 3999."
            return f"The converted value is {result}."
        except Exception:
            return "Invalid roman value."
    
    def integerRoman(self, value):
        try:
            convertValue = int(value)
            
            if convertValue > 3999 or convertValue == 0:
                return "Value must be in range of 0 - 3999."
            
            romanVal = ''
            counter = 0
            numberVal = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
            romanSyb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
            
            while convertValue > 0:
                for _ in range(convertValue // numberVal[counter]):
                    romanVal += romanSyb[counter]
                    convertValue -= numberVal[counter]
                counter += 1

            return f"The converted value is {romanVal}."
        except (TypeError or ValueError):
            return "Value must be Integer."
        except Exception:
            return "Invalid value."