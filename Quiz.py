from json import load
from string import ascii_lowercase

with open('questions.json','r') as file:
    data = load(file)
    point = 0

    for question in data:
        print('pytanie: ', question['question'])
        print('odpowiedzi:')
        for letter, answer in zip(ascii_lowercase, question['answers']):
            print(f'{letter} {answer}')

        print('')       
        x = input('Podaj swoją odpowiedź ')
        if x == question['right_answer']:
            print('')
            print('Super to poprawna odpowiedz')
            point += 1
        else:
            print('')
            print('To zla odpowiedz')
            point -= 1
    print('') 
    print(f'Zdobywasz {point} punkty')       

                



    #     print(answers)
    #     x = input('Podaj swoją odpowiedź ')
    #     print(x)
    # if x == right_answer:
    #     print("To prawidłowa odpowiedź")
    # else:
    #     print("Niestety prawidłowa odpowiedź to ", right_answer)
    

   

 
 
   