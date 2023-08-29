#Q1. Please write simple software to print image as

def showstar(number):
    number_input = number+number+(number-1)
    i = 0
    while i <= (number_input):
            i+=1
            if(i % 2 != 0):
                print(" "*number_input,"* "*i)
            number_input-=1

    number_input = number+number+(number-1)
    i = 0
    while i <= (number_input):
            i+=1
            if(i % 2 != 0):
                if (i == 1 or i == 3):
                    print(" "*number_input,"* "*i)
            number_input-=1
   

while True:
    try:
        number = int(input("Please enter a int number: "))
        break
    except ValueError:
        print("Type input incorrect! Please enter type int number.")

showstar(number)






class star:
     
      def __init__(self, int_num):
        self.int_num = int_num

    
      def output_star(self):
        return showstar(self.int_num)  
      


#test
class_num4 = star(4)
class_num4.output_star()


class_num5 = star(5)
class_num5.output_star()


class_num6 = star(6)
class_num6.output_star()