
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

inputList = input("Input: ").split()
print("Input:[" + ", ".join(inputList) + "]")
print("Output: ", multiply_list(inputList))