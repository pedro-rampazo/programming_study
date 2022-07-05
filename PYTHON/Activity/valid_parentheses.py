s = '{[()]()}'
open = "{[("
close = "}])"
waiting_list = []

for char in s:
    if char in open:
        waiting_list.append(close[open.index(char)])
    
    try:
        if char == waiting_list[-1]:
            waiting_list.pop()
    except:
        print("Invalid syntax")
        quit()

if len(waiting_list) == 0:
    print("Valid syntax")
else:
    print("Invalid syntax")
