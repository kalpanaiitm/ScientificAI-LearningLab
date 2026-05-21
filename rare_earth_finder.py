rare_earths = [
    "La", "Ce", "Pr", "Nd", "Pm", "Sm",
    "Eu", "Gd", "Tb", "Dy", "Ho",
    "Er", "Tm", "Yb", "Lu", "Y", "Sc"
]

text = input("Paste chemistry text: ")

found = []

for element in rare_earths:
    if element in text:
        found.append(element)

print("\nRare-earth elements found:")

if found:
    for item in found:
        print("-", item)
else:
    print("None found")
