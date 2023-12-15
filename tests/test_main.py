import pytest


from main import unique_names_mentors, top_3_names, get_ordered_courses, creating_a_folder
from tests.data import mentors_1, expected_1, mentors_2, expected_2, mentors_3, expected_3, courses_all, durations, \
    dict_errors


# Задание №1
@pytest.mark.parametrize(
    'mentors, expected',(
        [mentors_1, expected_1],
        [mentors_2, expected_2],
        [mentors_3, expected_3]
    ))
def test_unique_names_mentors(mentors, expected):
    result = unique_names_mentors(mentors)
    assert result == expected
    assert len(result) != 0


@pytest.mark.parametrize(
    'mentors, expected',(
        [mentors_1, 3],
        [mentors_2, 3],
        [mentors_3, 3]
    ))
def test_top_3_names(mentors, expected):
    result = top_3_names(mentors)
    assert len(result) == expected



def test_get_ordered_courses():
    courses = courses_all
    mentors = mentors_1
    duration = durations
    result = get_ordered_courses(courses, mentors, duration)
    for i in result:
        k = i.split(' ')
        assert ' '.join(k[:3]) in courses
        assert int(k[4]) in duration
    assert len(result) == 4

# Задание №2
def test_creating_a_folder():
    result = creating_a_folder()
    assert result == 201, dict_errors.get(result)

def test_creating_a_folder_negative():
    result = creating_a_folder()
    assert result != 201



if __name__ == '__main__':
    pytest.main()
