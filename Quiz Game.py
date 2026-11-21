questions = ("How many elements are found in the periodic table ",
             "What is the compositon of Aqua Regina?",
             "What if the namee of earth's permanent satellite ?",
             "What if the symbol of Magnetic Flux?",
             "Name the most electronegative element in the periodic table ?")

options = (("A.116", "B.36","C.118","D,98"),
          ("A.HCL", ".NHO","C.NO","D.Tt"),
          ("A.Moon", "B. Mars","C,Gas","D,Donkey"),
          ("A. Null", "B.phi,", "C","D.Flower"),
          ("A.Fluorine", "B.Titanium","C. Venedium","D. Caesium"))

answers = ("C", "A", "D", "c" , "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------")
    print(question)
    for option in options[question_num]: 
      print(option)

guess = input("Enter (A,B,C,D):").upper()
guesses.append(guess)
if guess == answers[question_num]:
    score += 1 
    print("correct man ")
else : 
    print("INCORRECT")
    print(f"{answers[question_num]} is the correct answer of the question.]")
question_num += 1 
