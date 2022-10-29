e = input("->")
counter = 0
for i in e:
    if i .isdigit():
        counter+=1
print(f'цифри={counter},символи = {len(e)}')