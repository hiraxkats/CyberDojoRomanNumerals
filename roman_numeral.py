class RomanNumeral:
    def convert(self, num):
        if num >= 5000:
            return "Number is too large"

        buff_ones_place = self.get_ones_place(num)
        buff_tens_place = self.get_tens_place(num)
        buff_hundreds_place = self.get_hundreds_place(num)
        buff_thousands_place = self.get_thousands_place(num)

        integ_buff = buff_thousands_place + buff_hundreds_place + buff_tens_place + buff_ones_place

        return integ_buff.replace("_", "")

    def get_ones_place(self, num):
        ones_place = num % 10

        # num 1 to 3
        if ones_place <= 3:
            buff = ""
            for i in range(ones_place):
                buff += "I"
            return buff
                
        # num 4
        if ones_place == 4:
            return "IV"

        # num from 5 to 8
        if ones_place >= 5 and ones_place < 9:
            buff = "V"
            for i in range(ones_place - 5):
                buff += "I"
            return buff

        # num 9        
        if ones_place == 9:
            return "IX"

        return "_"

    def get_tens_place(self, num):
        tens_place = (num % 100) // 10

        # num 1* to 3*
        if tens_place < 4:
            buff = ""
            for i in range(tens_place):
                buff += "X"
            return buff

        # num 4*   
        if tens_place == 4:
            return "XL"
        
        # num 5* to 8*
        if tens_place >= 5 and tens_place < 9:
            buff = "L"
            for i in range(tens_place - 5):
                buff += "X"
            return buff

        # num 9*
        if tens_place == 9:
            return "XC"
        
        return "_"

    def get_hundreds_place(self, num):
        hundreds_place = (num % 1000) // 100
        
        # num 1** to 3**
        if hundreds_place < 4:
            buff = ""
            for i in range(hundreds_place):
                buff += "C"
            return buff

        # num 4**
        if hundreds_place == 4:
            return "CD"

        # num 5** to 8**
        if hundreds_place >= 5 and hundreds_place < 9:
            buff = "D"
            for i in range(hundreds_place - 5):
                buff += "C"
            return buff

        # num 9**
        if hundreds_place == 9:
            return "CM"        
        return "_"

    def get_thousands_place(self, num):
        thousands_place = num // 1000

        # num 1***
        if thousands_place == 1:
            return "M"
        
        # num 2***
        if thousands_place == 2:
            return "MM"

        # num 3***
        if thousands_place == 3:
            return "MMM"

        # num 4***
        if thousands_place == 4:
            return "MMMM"
        
        return "_"
