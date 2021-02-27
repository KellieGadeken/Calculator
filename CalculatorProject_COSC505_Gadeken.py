
# coding: utf-8

# In[8]:


# Calculator Project
# COSC 505
# Kellie R. Gadeken

import math


# In[9]:


# create the menu
def print_menu():
    print("\nMenu:")
    print("1. Cartesian distance")
    print("2. Vector x matrix")
    print("3. Normalize")
    print("4. Quit")
   


# In[10]:


# check user input for errors
def check_user_input(user_input):
    
    #test for special characters
    special_characters = ['!','@','#','$','%','^','&','*','(',')','-','+','?','_','=',',','<','>','/','"']
    if any(c in special_characters for c in user_input):
        return "Please input the correct format and number of values for your calculation."
    
    #test for letters
    elif any(c.isalpha() for c in user_input):
        return "Please input the correct format and number of values for your calculation."
    
    # test for whitespaces to be included
    elif not (" ") in user_input:
        return "Please input the correct format and number of values for your calculation."
    
    else:
        return ""


# In[11]:


# modify user input into lists and floats
def modify_user_input(user_input):
    user_values = user_input.split(" ")  # split apart string
    for i in range(len(user_values)):
        user_values[i] = float(user_values[i]) # transform strings into floats

    return user_values


# In[12]:


# perform calculations for each menu option
def perform_calculation_1(user_values):
    # 1. Cartesian distance:
    ### user must enter 4 floating point inputs (x1 y1 x2 y2)
    
    # verify the correct amount of numbers was entered
    if len(user_values) == 4:
        value_xs = (user_values[2]-user_values[0])**2
        value_ys = (user_values[3]-user_values[1])**2
        dist = math.sqrt(value_xs + value_ys)  # calculate distance
        return "Cartesian Distance: {}".format(dist)
    else:
        # inform the user that they entered the incorrect amount of numbers for this calculation
        print("\nPlease input the correct format and number of values for your calculation.\n")
        return ""

def perform_calculation_2(user_values):
    # 2. Vector x matrix:
    ###user must enter 3 floating points for vector and 9 floating point for row
    
    # verify the correct amount of numbers was entered
    if len(user_values) == 12:
        # break apart vector values from matrix values
        vector_values = user_values[:3]
        matrix_values = user_values[3:]

        # make matrix format
        matrix_values_updated = [matrix_values[:3],matrix_values[3:6],matrix_values[6:]]

        result_matrix = []  # set empty matrix for values to populate into
        # use for-loop to multiply
        for i in range(len(matrix_values_updated)):
            summed_row_value = 0  # initialize to zero
            for j in range(len(vector_values)):
                row_value = matrix_values_updated[i][j] * vector_values[j]  # do the math
                summed_row_value += row_value # add together the products for the row
            result_matrix.append(summed_row_value) # append sum of products into the new matrix

        return "Vector x matrix: {}".format(result_matrix)
    else:
        # inform the user that they entered the incorrect amount of numbers for this calculation
        print("\nPlease input the correct format and number of values for your calculation.\n")
        return ""
    
def perform_calculation_3(user_values):
    # 3. Normalize:
    ### user must enter 3 floating points
    
    # verify the correct amount of numbers was entered
    if len(user_values) == 3:
        length_values = (user_values[0]**2) + (user_values[1]**2) + (user_values[2]**2)
        length = math.sqrt(length_values)  # calculate length

        normal_vector = []
        # use for-loop to populate normal_vector
        for i in range(len(user_values)):
            normal_value = user_values[i] / length  # normalize each value
            normal_vector.append(normal_value)     # add normalized value to normal_vector

        return "Normalize: {}".format(normal_vector)
    else:
        # inform the user that they entered the incorrect amount of numbers for this calculation
        print("\nPlease input the correct format and number of values for your calculation.\n")
        return ""
    


# In[20]:


# determine which selection user made from menu and make corrections for errors
def determine_user_selection(user_selection):
    
    if (user_selection=='1' or user_selection=='Cartesian distance' or user_selection=='1. Cartesian distance'        or user_selection=='cartesian distance'):
        # specify values for user input
        print("\nCartesian distance calculation requires 4 float inputs: x1 y1 x2 y2.\n")
        # if the selection is correct, return prompt for user to enter in values
        user_input = input("Please enter values for your Cartesian distance calculation: ")
        
        checking = check_user_input(user_input) # check user_input for errors
        
        # if checking == "", then there are no special characters or letters in the user input
        if checking == "":
            # modify string input into float values
            user_values = modify_user_input(user_input)

            # perform the appropriate calculation and check for more errors
            calculation = perform_calculation_1(user_values)
        
            return calculation
        # else return error message
        else:
            return checking
    
    elif (user_selection=='2' or user_selection=='Vector x matrix' or user_selection=='2. Vector x matrix'          or user_selection=='vector x matrix'):
        # specify values for user input
        print("\nVector x matrix calculation requires 3 float vector inputs and 9 float matrix inputs:\n         x1 x2 x3 m11 m12 m13 m21 m22 m23 m31 m32 m33.\n")
        # if the selection is correct, return prompt for user to enter in values
        user_input = input("Please enter values for your Vector x matrix calculation: ")
        
        checking = check_user_input(user_input) # check user_input for errors
        print(checking)
        
        # if checking == "", then there are no special characters or letters in the user input
        if checking == "":
            # modify string input into float values
            user_values = modify_user_input(user_input)

            # perform the appropriate calculation and check for more errors
            calculation = perform_calculation_2(user_values)
        
            return calculation
        # else return error message
        else:
            return checking
    
    elif (user_selection=='3' or user_selection=='Normalize' or user_selection=='3. Normalize'
         or user_selection=='normalize'):
        # specify values for user input
        print("\nNormalize calculation requires 3 float inputs: v1 v2 v3.\n")
        # if the selection is correct, return prompt for user to enter in values
        user_input = input("Please enter values for your Normalize calculation: ")
        
        checking = check_user_input(user_input) # check user_input for errors
        print(checking)
        
        # if checking == "", then there are no special characters or letters in the user input
        if checking == "":
            # modify string input into float values
            user_values = modify_user_input(user_input)

            # perform the appropriate calculation and check for more errors
            calculation = perform_calculation_3(user_values)
        
            return calculation
        # else return error message
        else:
            return checking
    
    else:
        print("\nPlease input the correct format for selecting a menu option. (Input the number or phrase or both.)")
        return ""


# In[19]:


# time for the main event

# initial instance of menu display and user input
print_menu()
user_selection = input("Enter command: ") 

# error check user selection for command 4 in while-loop
while (user_selection!='4' and user_selection!='Quit' and user_selection!='quit' and user_selection!='4. Quit'        and user_selection!='4. quit'):
    
    # determine user selection, check for errors, and run the appropriate calculation
    user_input = determine_user_selection(user_selection)
    print(user_input)
    

    print_menu()
    # ask for the user selection
    user_selection = input("Enter command: ") 
else:
    print("\nYou have quit :(\nThanks for using the calculator!")

