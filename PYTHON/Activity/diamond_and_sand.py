n = int(input("Type number of times of run: "))
waiting_list = []

for time in range(0, n):
    diamond = 0
    diamond_miner = input("Diamonds and Sand: ")

    for character in diamond_miner:
        
        if character == "<":
            waiting_list.append(">")
        elif character == ">":
            if ">" in waiting_list:
                waiting_list.pop()
                diamond += 1
        elif character == ".":
            continue
        else:
            print("Incorrect character")
            break
    
    print(f"Number of diamonds: {diamond}")



