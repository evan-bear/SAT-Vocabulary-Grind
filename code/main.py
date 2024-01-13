import random
from barrons import words

questions = min(int(input("How many practice words? ")), len(words))
command = input("Start practice? [y/n] ")
print()
if command == "n":
    exit()
elif command == "y":
    correct = 0
    passed = 0
    incorrect = 0
    seen = []
    for z in range(questions):
        index = int(random.randrange(0, len(words), 1))
        while index in seen:
            index = int(random.randrange(0, len(words), 1))
        seen.append(index)
        answer = [*words][index]
        definition = words[answer]

        response = input(f"{definition} : ")
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
    print(f"Correct:    {correct}")
    print(f"Incorrect:  {incorrect}")
    print(f"Passed:     {passed}")
    exit()
