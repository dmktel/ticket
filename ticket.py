# Homework 13.8.19

ticket = int(input('Number of tickets? '))
price = []

for i in range(1, ticket + 1):
    age = int(input(f'Person {i} age? '))
    if age < 18:
        price.append(0)
    elif 18 <= age <= 25:
        price.append(990)
    else:
        price.append(1390)

if ticket > 3:
    total = int(sum(price) - sum(price)*0.1)
else:
    total = int(sum(price))

print(total)
