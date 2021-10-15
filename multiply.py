
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
