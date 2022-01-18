"""
Dunder Main:
- __name__ indicate the way how the script is run
- When use ' if __name__ == "__main__": ', let's run the script only in the condition "__main__"
"""
if __name__ == "__main__":
    print("This text appears when the script is run directly")
else:
    print("This text appears when the script is run as module")