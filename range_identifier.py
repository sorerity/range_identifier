range_identifier = []

range_list = {
 "range1_10": 0,
 "range11_20": 0,
 "range21_30": 0,
 "range31_40": 0,
 "range41_50": 0,
 }

while True:
    try:
        user_input = int(input("Please input numbers ranging 1-50: "))

        if user_input <= 0 or user_input >= 50:
             print(f"1 - 10: {range_list['range1_10']}")
             print(f"11 - 20: {range_list['range11_20']}")
             print(f"21 - 30: {range_list['range21_30']}")
             print(f"31 - 40: {range_list['range31_40']}")
             print(f"41 - 50: {range_list['range41_50']}")
             break
        
        if user_input <= 1 and user_input <= 10:
                range_list["range1_10"] += 1
        elif user_input <= 11 and user_input <= 20:
                range_list["range11_20"] += 1
        elif user_input <= 21 and user_input <= 30:
                range_list["range21_30"] += 1
        elif user_input <= 31 and user_input <= 40:
                range_list["range31_40"] += 1
        elif range_list <= 41 and user_input <= 50:
                range_list["range41_50"] += 1
        
    except ValueError:
        print(f"1 - 10: {range_list['range1_10']}")
        print(f"11 - 20: {range_list['range11_20']}")
        print(f"21 - 30: {range_list['range21_30']}")
        print(f"31 - 40: {range_list['range31_40']}")
        print(f"41 - 50: {range_list['range41_50']}")
        break
















#Create a program that asks user to input a number ranging from 1 to 50. 
#Ask the user to input again until the user input is invalid. 
#When the user input is invalid, 
#display how many inputted numbers are in the following range:
#1 - 10 = ?
#11- 20 = ?
#21- 30 = ?
#31- 40 = ?
#41- 50 = ?

#Add main variable = []
#Establish while true statement (Loop 1)
   # add while true
    #add try
    #Ask user to input variables,
    #    If less than 0 and more than 50
      #      print main variable (Range) 
    #Add except statement
    #    print main variable (Range)
    
#Establish list (To record the user's inputs)
#    range identifier = {
  #  add the ranges
  #  }
#add append to the list     
#for sorting
   # compare age, if it is less than 10 
       # append
        
