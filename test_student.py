from student import calculate_average, calculate_grade, student_result


def test_calculate_average():
    assert calculate_average([80, 75, 90]) == 81.66666666666667


def test_grade_A():
    assert calculate_grade(95) == "A"


def test_grade_B():
    assert calculate_grade(80) == "B"


def test_grade_C():
    assert calculate_grade(65) == "C"


def test_grade_D():
    assert calculate_grade(50) == "D"


def test_grade_F():
    assert calculate_grade(30) == "F"


def test_student_result():
    result = student_result("Rahul", [80, 75, 90])

    assert result["name"] == "Rahul"
    assert result["grade"] == "B"
