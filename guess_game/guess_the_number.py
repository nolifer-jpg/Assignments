import random

def guess_the_number():
    number = random.randint(1, 100)
    attempts = 0

    print("🎯 Guess the number (between 1 and 100)")

    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("❌ Please enter a number within 1 to 100.")
            elif guess < number:
                print("📉 Too low!")
            elif guess > number:
                print("📈 Too high!")
            else:
                print(f"✅ Correct! You guessed it in {attempts} tries.")
                break

        except ValueError:
            print("⚠️ Please enter a valid integer.")

def main():
    while True:
        guess_the_number()
        play_again = input("🔄 Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("👋 Thanks for playing! Goodbye.")
            break

main()