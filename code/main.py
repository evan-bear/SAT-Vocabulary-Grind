import random
from barrons_definitions import words
from barrons_roots import roots

style = ""
barrons = input("Definitions or root words? [d/r]\t\t\t")
format = input("Multiple choice or flash cards? [m/f]\t\t\t")
if format == "m":
    if barrons == "d":
        style = input("Definition-to-word or word-to-definition? [d/w]\t\t")
        while not (style == "d" or style == "w"):
            style = input("Invalid. Definition-to-word or word-to-definition? [d/w]\t")
    elif barrons == "r":
        style = input("Definition-to-root or root-to-definition? [d/r]\t\t")
        while not (style == "d" or style == "r"):
            style = input("Definition-to-root or root-to-definition? [d/r]\t")
questions = min(int(input("How many practice words?\t\t\t\t")), len(words))
command = input("Start practice? [y/n]\t\t\t\t\t")

while command == "y":
    correct = 0
    passed = 0
    incorrect = 0
    seen = []
    print()
    
    for z in range(questions):
        if barrons == "d":
            index = int(random.randrange(0, len(words), 1))
            while index in seen:
                index = int(random.randrange(0, len(words), 1))
            seen.append(index)

            if style == "d":
                question = [*words][index]
                answer = words[question]
            else:
                answer = [*words][index]
                question = words[answer]
            
            if format == "m":
                choices = [answer]
                choice_index = [index]
                for i in range(3):
                    temp = int(random.randrange(0, len(words), 1))
                    while temp in choice_index:
                        temp = int(random.randrange(0, len(words), 1))
                    
                    choice_index.append(temp)
                    if style == "d":
                        choices.append(words[[*words][temp]])
                    elif style == "w":
                        choices.append([*words][temp])
                random.shuffle(choices)
                
                print(f"{z + 1}. {question}: ")
                print(f"A) {choices[0]}")
                print(f"B) {choices[1]}")
                print(f"C) {choices[2]}")
                print(f"D) {choices[3]}")
                response = input("Your choice: [A/B/C/D] ")
                
                if response == "quit":
                    break
                elif (response == "A" and answer == choices[0]) or \
                    (response == "B" and answer == choices[1]) or \
                        (response == "C" and answer == choices[2]) or \
                            (response == "D" and answer == choices[3]) or \
                                response == answer:
                    correct += 1
                else:
                    incorrect += 1
                    print(f"Incorrect. Answer: {answer} ({chr(ord('A') + choices.index(answer))})")
                print()
            elif format == "f":
                response = input(f"{z + 1}. {question}: ")
                
                if response == "quit":
                    break
                elif response == "pass":
                    passed += 1
                    print(f"Answer: {answer}")
                elif response == answer:
                    correct += 1
                else:
                    breaking = False
                    incorrect += 1
                    while response != answer:
                        if response == "quit":
                            breaking = True
                            break
                        elif response == "pass":
                            print(f"Answer: {answer}")
                            break
                        response = input(f"Incorrect. {question} : ")
                    if breaking:
                        break
        
        elif barrons == "r":
            index = int(random.randrange(0, len(roots), 1))
            while index in seen:
                index = int(random.randrange(0, len(roots), 1))
            seen.append(index)
            if style == "d":
                question = [*roots][index]
                answer = roots[question]
            elif style == "r":
                answer = [*roots][index]
                question = roots[answer]
            
            if format == "mc":
                choices = [answer]
                choice_index = [index]
                choice_roots = [question]
                for i in range(3):
                    temp = int(random.randrange(0, len(roots), 1))
                    while temp in choice_index:
                        temp = int(random.randrange(0, len(roots), 1))
                    
                    choice_index.append(temp)
                    if style == "d":
                        choices.append(roots[[*roots][temp]])
                    elif style == "r":
                        choices.append([*roots][temp])
                random.shuffle(choices)
                
                print(f"{z + 1}. {question}: ")
                print(f"A) {choices[0]}")
                print(f"B) {choices[1]}")
                print(f"C) {choices[2]}")
                print(f"D) {choices[3]}")
                response = input("Your choice: [A/B/C/D] ")
                
                if response == "quit":
                    break
                elif (response == "A" and answer == choices[0]) or \
                    (response == "B" and answer == choices[1]) or \
                        (response == "C" and answer == choices[2]) or \
                            (response == "D" and answer == choices[3]) or \
                                response == answer:
                    correct += 1
                else:
                    incorrect += 1
                    print(f"Incorrect. Answer: {answer} ({chr(ord('A') + choices.index(answer))})")
                print()

    print(f"\nResults")
    print(f"Correct:\t{correct}")
    print(f"Incorrect:\t{incorrect}")
    if format == "fc":
        print(f"Passed:\t\t{passed}")
    print()
    
    command = input("Again? [y/n] \t\t\t\t\t\t")
exit()
