import random

def generate_random_number(min_value,max_value):
    num = random.randint(min_value,max_value)
    return num

def guess_number(num):
    attempt = 0
    while True:
        
            guess = input("\nGuess the number: ")   
            if not guess.isdigit():
                print("Invalid Input, Try Again!")
                continue
        
            guess = int(guess)
            attempt += 1
            if guess > num:
                print( " Too high ")
            elif guess < num:
                print(" Too low ")
            else:
                print(f" 🎉You got it in {attempt} attempts!!")
                break

def main():
     print("\n -----Welcome to Number Guessing Game-----\n")
     print("\nLevels: ")
     print("1. Easy [1-20]")
     print("2. Moderate [1-50]")
     print("3. Extreme [1-100]")
     level = int(input("\nChoose your level: "))

     if level == 1:
          min_value, max_value = 1,20
    
     elif level == 2:
          min_value, max_value = 1,50
    
     elif level == 3:
          min_value, max_value = 1,100
    
     else:
        print("Invalid Level!!")
        return
     
     secret_number = generate_random_number(min_value, max_value)
     guess_number(secret_number)

if __name__ == "__main__":
     main()
