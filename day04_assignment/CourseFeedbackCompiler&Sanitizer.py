'''
    Course Feedback Compiler & Sanitizer
    Scenario
    Student feedback records contain ratings from 1 to 5 stars. Due to raw data entry issues, the feedback database has some course entries with list values that are empty, or lists containing invalid elements (such as string annotations like "Excellent" or None values).

    Problem Description
    Write a function compile_feedback(ratings_dict) that processes course feedback:

    The parameter ratings_dict is a dictionary where keys are course names (strings) and values are lists of ratings (which should be numeric but may contain invalid types).
    The function must return a dictionary mapping each course name to its average rating, rounded to 2 decimal places.
    Implement the following error handling criteria:
    For each rating inside a course's list, attempt to convert it to a float. If a rating cannot be converted (throws a ValueError or TypeError), catch the exception, print a warning: "Warning: Invalid rating value '<val>' in course '<course>' skipped.", and continue processing the rest of the list.
    If a course has no valid ratings (the list is empty or contains no convertible numbers), computing the average will trigger a division-by-zero error. Catch ZeroDivisionError, print a warning: "Warning: No valid ratings found for course '<course>'. Rating set to 0.0.", and assign the course an average rating of 0.0.
    Sample Input
    feedback_data = {
        "Python Programming": [5, 4, "4", "Great", 5],
        "Machine Learning": [],
        "Deep Learning": ["Good", "Average", None]
    }
    Expected Output
    Console Warnings Printed:

    Warning: Invalid rating value 'Great' in course 'Python Programming' skipped.
    Warning: No valid ratings found for course 'Machine Learning'. Rating set to 0.0.
    Warning: Invalid rating value 'Good' in course 'Deep Learning' skipped.
    Warning: Invalid rating value 'Average' in course 'Deep Learning' skipped.
    Warning: Invalid rating value 'None' in course 'Deep Learning' skipped.
    Warning: No valid ratings found for course 'Deep Learning'. Rating set to 0.0.
    Returned Dictionary:

    {
        "Python Programming": 4.5,
        "Machine Learning": 0.0,
        "Deep Learning": 0.0
    }
'''
import os
def compile_feedback(ratings_dict):
    result = {}

    for course, ratings in ratings_dict.items():
        valid_ratings = []

        for val in ratings:
            try:
                rating = float(val)
                valid_ratings.append(rating)
            except (ValueError, TypeError):
                print(
                    f"Warning: Invalid rating value '{val}' "
                    f"in course '{course}' skipped."
                )

        try:
            average = sum(valid_ratings) / len(valid_ratings)
            result[course] = round(average, 2)

        except ZeroDivisionError:
            print(
                f"Warning: No valid ratings found for course "
                f"'{course}'. Rating set to 0.0."
            )
            result[course] = 0.0

    return result


def main():
    feedback_data = {
        "Python Programming": [5, 4, "4", "Great", 5, 4.5],
        "Machine Learning": [],
        "Deep Learning": ["Good", "Average", None]
    }

    output = compile_feedback(feedback_data)
    print(output)


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("*" * 80)
    print(f"{' Course Feedback Compiler & Sanitizer ':^80}")
    print("-" * 80)
    main()
    print("-" * 80)
