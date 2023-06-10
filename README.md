# help_your_instructor

The code provided defines four functions: average_grade, highest_grade, failing_grades, and perfect_grades. These functions perform calculations and operations on a list of numerical grades.

Here's a summary of what each function does:

average_grade(grade_list): This function calculates the average grade from a list of grades. It takes a list of numerical grades as input (grade_list) and returns the average grade as a float. If the input is not a list, it raises a TypeError exception. If the list is empty, it returns a default value of 0.

highest_grade(grade_list): This function finds the highest grade from a list of grades. It takes a list of numerical grades as input (grade_list) and returns the highest grade as an integer or float. If the input is not a list, it raises a TypeError exception. If the list is empty, it returns None.

failing_grades(grade_list): This function identifies failing grades from a list of grades. It takes a list of numerical grades as input (grade_list) and returns a string message indicating the number of failing grades and the list of failing grades. If the input is not a list, it raises a TypeError exception. Failing grades are defined as grades that are less than or equal to 55.

perfect_grades(grade_list): This function checks if there is a perfect grade (100) in a list of grades. It takes a list of numerical grades as input (grade_list) and returns a boolean value. It returns True if a perfect grade is found in the list and False otherwise. If the input is not a list, it raises a TypeError exception.

The example usage section at the end of the code demonstrates how to use these functions. It creates a list of grades, calls each function with the grade list as input, and prints the results.
