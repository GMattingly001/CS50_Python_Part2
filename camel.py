
text = list(input("camelCase: "))
new_list = []
for i in text:
    if i.isupper():
        i = "_"+i.lower()
    new_list.append(i)

for text in new_list:
    print(text, end="")
