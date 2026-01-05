from lms import calculate_average_score, performance_status

def test_calculate_average_score():
    assert calculate_average_score([80, 90, 100]) == 90
    assert calculate_average_score([50, 50, 50]) == 50
    assert calculate_average_score([]) == 0

def test_performance_status():
    assert performance_status(90) == "Excellent Performance"
    assert performance_status(75) == "Good Performance"
    assert performance_status(55) == "Average Performance"
    assert performance_status(40) == "Needs Improvement"