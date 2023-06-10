def average_grade(grade_list):
    """
    Calculates the average grade from a list of grades.
    
    Parameters:
    grade_list (list): A list of numerical grades.
    
    Returns:
    float: The average grade.
    """
    if not isinstance(grade_list, list):
        raise TypeError("Invalid input: grade_list must be a list.")
    
    if not grade_list:
        return 0  # Return a default value when the list is empty
    
    return sum(grade_list) / len(grade_list)


def highest_grade(grade_list):
    """
    Finds the highest grade from a list of grades.
    
    Parameters:
    grade_list (list): A list of numerical grades.
    
    Returns:
    int or float: The highest grade.
    """
    if not isinstance(grade_list, list):
        raise TypeError("Invalid input: grade_list must be a list.")
    
    if not grade_list:
        return None  # Return None when the list is empty
    
    return max(grade_list)


def failing_grades(grade_list):
    """
    Identifies failing grades from a list of grades.
    
    Parameters:
    grade_list (list): A list of numerical grades.
    
    Returns:
    str: A message indicating the number of failing grades and the list of failing grades.
    """
    if not isinstance(grade_list, list):
        raise TypeError("Invalid input: grade_list must be a list.")
    
    fail_grades = [grade for grade in grade_list if grade <= 55]
    return f"There are {len(fail_grades)} failing grade(s): {fail_grades}"


def perfect_grades(grade_list):
    """
    Checks if there is a perfect grade (100) in a list of grades.
    
    Parameters:
    grade_list (list): A list of numerical grades.
    
    Returns:
    bool: True if a perfect grade is found, False otherwise.
    """
    if not isinstance(grade_list, list):
        raise TypeError("Invalid input: grade_list must be a list.")
    
    return any(grade == 100 for grade in grade_list)


# Example usage
grade_list = [55, 90, 100, 66, 92, 76, 85]
print(f"The list of grades: {grade_list}")
print(f"Average grade: {average_grade(grade_list)}")
print(f"The Highest grade is: {highest_grade(grade_list)}")
print(f"The number of Failing grades is: {failing_grades(grade_list)}")
print(f"Is there a perfect grade in this list? {perfect_grades(grade_list)}")

