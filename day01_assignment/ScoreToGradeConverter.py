"""
    Write a script that takes a numeric test score from the user (0 to 100) and
    displays a corresponding letter grade based on the following scale:

    90-100: A
    80-89: B
    70-79: C
    60-69: D
    Below 60: F
"""
def display_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
def get_valid_score(prompt):
    while True:
        try:
            score = float(input(prompt))
            if 0 <= score <= 100:
                return score
            print("Error: Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid numerical score.")
def main():
    while True:
        score = get_valid_score("Enter the score (0 to 100): ")
        grade = display_grade(score)
        display_score = int(score) if score.is_integer() else score
        print(f"Grade for score {display_score}: {grade}\n")
        print("_" * 80)
        print("Choose an option:\n1. Check another score\n2. Exit\n")
        while True:
            try:
                choice = int(input("Enter your choice (1 or 2): "))
                if choice in (1, 2):
                    break
                print("Invalid choice. Please enter 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a number (1 or 2).")
        if choice == 2:
            print("\nThank you for using the Grade Calculator!")
            print("Exiting the program...")
            break
        print("\n" + "=" * 80)

if __name__ == "__main__":
    print("*" * 80)
    print(f"{' Grade Calculator ':^80}")
    print("-" * 80)
    main()