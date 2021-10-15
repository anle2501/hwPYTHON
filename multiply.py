'''
Python program to take in a list as input and multiply all of the 
elements in the list and return the result as output.
Parameter
    inputList: list[]
                the integer list as input
    result: int
                the result of multiplying all of the element
'''
def multiply_list(inputList):

    result = 1; 
    for number in inputList:
        try:
            int(number)
        except:
            return False

    for number in inputList:
        result *= int(number)
            
    return result

# driver code
inputList = input("Input: ").split()
print("Input:[" + ", ".join(inputList) + "]")
print("Output: ", multiply_list(inputList))