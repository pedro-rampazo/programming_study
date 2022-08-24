'''
'''
threshold = 2
logs = ["99 11 22", "25 99 200", "33 33 500", "33 33 1000", "99 99 800", "25 70 2700", "80 25 700"]
sender_user_list = []
receiver_user_list = []
all_user = []
result = []

for lg in logs:
    sender_user_list.append(lg.split()[0])
    receiver_user_list.append(lg.split()[1])

all_user = sender_user_list + receiver_user_list
logs = set(all_user)

for usr in logs:
    counter = all_user.count(usr)
    
    for idx, value in enumerate(sender_user_list):
        if usr == value and receiver_user_list[idx] == usr:
            counter -= 1
    
    print(f"User: {usr} | Transaction: {counter}")
    
    if counter >= threshold:
        result.append(usr)

print(sorted(result, reverse=True))



