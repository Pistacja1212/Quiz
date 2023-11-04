import json;
import questions.json;

with open('questions.json') as file:
    data = json.load(file)

for question in questions:
    print(question)
    print(answers)
    x = input('Podaj swoją odpowiedź ')
    print(x)
if x == right_answer:
    print("To prawidłowa odpowiedź")
else:
    print("Niestety prawidłowa odpowiedź to ", right_answer)
    

   

 
 
   