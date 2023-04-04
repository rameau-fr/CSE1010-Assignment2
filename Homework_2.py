# Name:
# SBUID: 

# Remove the ellipses (...) when writing your solutions.

# ---------------------------- Exercise I ---------------------------------------
# ----------------- Extract statistical information from a list -----------------
# TODO: Complete the implementation of listStatistic() and listStd().

def listStatistic(list_in):
    ...

def listStd(list_in):
    ...

# ---------------------------- Exercise II --------------------------------------
# -----------------         Implement the Lunh Algorithm        -----------------
# TODO: Complete the implementation of reverseList(), doubleOddIndex()
# digitSum(), replaceDoubleDigit(), isCardValid() and lunhAlgorithm()

def reverseList(list_in):
    ...

def doubleOddIndex(list_in):
    ...

def digitSum(value):
    ...

def replaceDoubleDigit(list_in):
    ...

def isCardValid(list_in):
    ...
    
def lunhAlgorithm(card_nb):
    ...


# ---------------------------- MAIN FCT ---------------------------------
def main():

    #Exercise 1 main
    my_list = [1, 2, 3, 4, 5, 6]
    list_max, list_min, list_average = listStatistic(my_list)
    print("The max of the list is: ", list_max)
    print("The min of the list is: ", list_min)
    print("The average of the list is: ", list_average)
    list_std = listStd(my_list)
    print("The std of the list is: ", list_std)

    #Exercise 2 main
    card_number = ...

    ''' Step-by-step tests (you can remove these  tests when you
    are done with the final function lunhAlgorithm )
    '''
    print("Here is the original card number: ", card_number)
    reversed_card_nb = reverseList(card_number)
    print("Here is the reversed card number: ", reversed_card_nb)
    lunh_product = doubleOddIndex(reversed_card_nb)
    print("One in two element is multipled by 2: ", lunh_product)
    print("Sum the digit in a number: ", digitSum(18))
    single_digit_prod = replaceDoubleDigit(lunh_product)
    print("Replace the double digits in the vector: ", single_digit_prod)
    validity = isCardValid(single_digit_prod)
    print("Is the card valid??", validity)

    # execute the final code
    print("Is the card valid??", lunhAlgorithm(card_number))

# Run the main code
main()
