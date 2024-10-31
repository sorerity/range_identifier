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

        if user_input <= 0 or user_input > 50:
             print("Invalid input, please enter numbers ranging 1-50 only, displaying results.")
             print(f"Range 1 - 10: {range_list['range1_10']}")
             print(f"Range 11 - 20: {range_list['range11_20']}")
             print(f"Range 21 - 30: {range_list['range21_30']}")
             print(f"Range 31 - 40: {range_list['range31_40']}")
             print(f"Range 41 - 50: {range_list['range41_50']}")
             break
        
        if 1 <= user_input <= 10:
                range_list["range1_10"] += 1
        elif 11 <= user_input <= 20:
                range_list["range11_20"] += 1
        elif 21 <= user_input <= 30:
                range_list["range21_30"] += 1
        elif 31 <= user_input <= 40:
                range_list["range31_40"] += 1
        elif 41 <= user_input <= 50:
                range_list["range41_50"] += 1
        
    except ValueError:
        print("Invalid input, please enter numbers only, displaying results.")
        print(f"Range 1 - 10: {range_list['range1_10']}")
        print(f"Range 11 - 20: {range_list['range11_20']}")
        print(f"Range 21 - 30: {range_list['range21_30']}")
        print(f"Range 31 - 40: {range_list['range31_40']}")
        print(f"Range 41 - 50: {range_list['range41_50']}")
        break