import sys
sys.path.append('..')
import pytest
from movie import *
import solution
import student


@pytest.mark.parametrize('year', range(1950, 2050))
def test_titles(year):
    function_name = 'movies_from_year'
    args = [year]

    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name} in student module")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    solution_result = solution_function(movies, *args)
    student_result = student_function(movies, *args)

    assert student_result == solution_result


@pytest.mark.parametrize('actor', {actor for movie in movies for actor in movie.actors})
def test_titles(actor):
    function_name = 'movies_with_actor'
    args = [actor]

    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name} in student module")

    solution_function = getattr(solution, function_name)
    student_function = getattr(student, function_name)

    solution_result = solution_function(movies, *args)
    student_result = student_function(movies, *args)

    assert student_result == solution_result