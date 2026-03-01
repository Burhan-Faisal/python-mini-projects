import random,csv
from termcolor import cprint
SUBJECTS=['history','geogrpahy','biology','physics','computerscience','chemistry']
def ask_question(index, question, options):
  print(f'Question {index}: {question}')
  labels = ['a', 'b', 'c', 'd']
  for label, option in zip(labels, options):
    print(f'{label}) {option}')

  return input('Your answer: ').upper().strip()  

def run_quiz(quiz):
  print("Let's start the quiz?")
  random.shuffle(quiz)

  score = 0

  for index, item in enumerate(quiz, 1):
    options_list=[item['Option A'],item['Option B'],item['Option C'],item['Option D']]
    answer = ask_question(index, item['Question'],options_list)

    if answer == item['Correct Answer']:
      cprint('Correct!', 'green')
      score += 1
    else:
      cprint(f"Wrong! The correct answer is {item['Correct Answer']}", 'red')
    
    print()

  print(f'Quiz over! Your final score is {score} out of {len(quiz)}')

def load_file(subject):
  try:
    filename=f'{subject.lower()}_quiz.csv'
    with open(filename,'r') as f:
      return list(csv.DictReader(f))
  except FileNotFoundError as e:
    print(e)
  
def main():
  print("--------------Let's play a quiz game-----------")
  print('/'.join([s.upper()for s in SUBJECTS]))
  while True:
    subject_interest=input("Select The Subject in which you are Interested :").strip().lower()
    if subject_interest in SUBJECTS:
      data=load_file(subject_interest)
      if data:
        run_quiz(data)
      break
    else:
      print("Please make a valid Choice")

if __name__ == '__main__':
  main()