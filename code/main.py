import random
from barrons_definitions import words

questions = min(int(input("How many practice words? ")), len(words))
format = (input("Multiple choice or flash cards? [mc/fc] "))
command = input("Start practice? [y/n] ")
print()

correct = 0
passed = 0
incorrect = 0
seen = []

if command == "y":
    for z in range(questions):
        index = int(random.randrange(0, len(words), 1))
        while index in seen:
            index = int(random.randrange(0, len(words), 1))
        seen.append(index)
        answer = [*words][index]
        definition = words[answer]
        if format == "mc":
            choice_index = [index]
            choices = [answer]
            for i in range(3):
                temp = int(random.randrange(0, len(words), 1))
                while temp in choice_index:
                    temp = int(random.randrange(0, len(words), 1))
                    
                choice_index.append(temp)
                choices.append([*words][temp])
            random.shuffle(choices)
            
            print(f"{z + 1}. {definition}: ")
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
                        (response == "D" and answer == choices[3]):
                            correct += 1
            else:
                incorrect += 1
                print(f"Incorrect. Answer: {answer} ({chr(ord('A') + choices.index(answer))})")
            print()

        elif format == "fc":
            response = input(f"{z + 1}. {definition}: ")
            
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
                    response = input(f"Incorrect. {definition} : ")
                if breaking:
                    break

    print(f"\nResults")
    print(f"Correct:\t{correct}")
    print(f"Incorrect:\t{incorrect}")
    if format == "fc":
        print(f"Passed:\t\t{passed}")
exit()
