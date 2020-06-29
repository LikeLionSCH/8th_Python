class Calculator:
    def setData(self):
        self.AddCount = 0
        self.SubCount = 0
        self.MulCount = 0
        self.DivCount = 0
    
    def Add(self, num1, num2):
        self.AddCount += 1
        print("덧셈결과:", num1+num2)
    
    def Sub(self, num1, num2):
        self.SubCount += 1
        print("뺄셈결과:", num1-num2)

    def Mul(self, num1, num2):
        self.MulCount += 1
        print("곱셈결과:", num1*num2)

    def Div(self, num1, num2):
        self.DivCount += 1
        print("나눗셈결과:", num1/num2)
    
    def ShowCount(self):
        print()
        print("덧셈 :", self.AddCount)
        print("뺄셈 :", self.SubCount)
        print("곱셈 :", self.MulCount)
        print("나눗셈 :", self.DivCount)

cal = Calculator()
cal.setData()
cal.Add(10, 20)
cal.Add(20, 30)
cal.Add(30, 40)
cal.Sub(10, 20)
cal.Mul(10, 20)
cal.Div(10, 20)
cal.ShowCount()