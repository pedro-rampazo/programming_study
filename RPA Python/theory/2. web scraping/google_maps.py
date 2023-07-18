import webbrowser

address = input("Adress: ")

address = address.split(" ")

for x in address:
    index = address.index(x)
    if "," in x:
        x = x.replace(",", "")
        address[index] = x

link = "https://www.google.com/maps/place/"

for l in address:
    link += f"{l}+"

link = link[:-1]

webbrowser.open(link)