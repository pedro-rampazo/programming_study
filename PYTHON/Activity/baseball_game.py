match = ["5", "2", "C", "D", "+"]
operation = match[2:5]
result = []

for score in match:
    try:
        score = int(score)
        result.append(score)
    except:
        if score == "+":
            result.append(sum(result))
        elif score == "D":
            result.append(result[-1] * 2)
        else:
            result.pop()

print(f"Final Result: {sum(result)}")
