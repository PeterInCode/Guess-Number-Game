import random

print("the correct number is between 1 and 100.")

number_to_guess = random.randint(1, 100)

attempts = 0
max_attempts = 5


while attempts < max_attempts:
    user_number = int(input("Enter your guess: "))
    attempts += 1

    if user_number == number_to_guess:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
    elif user_number < number_to_guess:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

    if attempts == max_attempts:
        print(f"Sorry, you've used all your attempts.")
