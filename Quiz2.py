from json import load
from string import ascii_lowercase

with open('questions2.json','r') as file:
    data = load(file)
    point = 0

    for y in data:
        print('pytanie: ', y['question'])
        print('')
        print('odpowiedzi:')
        
        for letter, answer in zip(ascii_lowercase, y['answers']):
            print(f'{letter}) {answer}')

        print('')       
        x = input('Podaj swoją odpowiedź ')
        if x == y['right_answer']:
            print('')
            print('Jest to poprawna odpoweidz')
            point += 1
        else:
            print('')
            print('Jest to zla odpowiedz')
            point -= 1

    print('') 
    print(f'Zdobywasz {point} punkty')  