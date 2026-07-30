animal = input()

result = ""

if animal == 'dog':
    result = 'mammal'
elif animal == 'snake':
    result = 'reptile'
elif animal == 'tortoise':
    result = 'reptile'
elif animal == 'crocodile':
    result = 'reptile'
else:
    result = 'unknown'

print(result)