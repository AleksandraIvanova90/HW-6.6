import requests

from configuration import token, base_url


# Задание №1
def unique_names_mentors(mentors):
    all_list = []
    for m in mentors:
        for m1 in m:
            all_list.append(m1)
    all_names_list = []
    for mentor in all_list:
        name = mentor.split()
        all_names_list.append(name[0])
        unique_names = set(all_names_list)
        all_names_sorted = sorted(list(unique_names))
        res = ", ".join(all_names_sorted)
    return f"Уникальные имена преподавателей: {res}"


def top_3_names(mentors):
    all_list = []
    for m in mentors:
        for m1 in m:
            all_list.append(m1)
    all_names_list = []
    for mentor in all_list:
        name = mentor.split()
        all_names_list.append(name[0])
    popular = []
    for name in all_names_list:
        popular.append((name, all_names_list.count(name)))
    popular = list(set(popular))
    popular.sort(key=lambda x: x[1], reverse=True)
    top_3 = popular[0:3]
    return top_3


def get_ordered_courses(courses, mentors, durations):
    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title": course, "mentors": mentor, "duration": duration}
        courses_list.append(course_dict)
    durations_dict = {}
    for id, cours in enumerate(courses_list):
        duration_key = cours["duration"]
        durations_dict.setdefault(duration_key, [])
        durations_dict[duration_key].append(id)
    durations_dict = dict(sorted(durations_dict.items()))
    list_courses = []
    for duration, ids in durations_dict.items():
        for id in ids:
            list_courses.append(f'{courses_list[id]["title"]} - {duration} месяцев')
    return list_courses


# Задание №2
def creating_a_folder():
    headers = {"Authorization": token}
    params = {"path": "unit-test"}
    response = requests.put(
        f"{base_url}/v1/disk/resources", params=params, headers=headers
    )
    return response.status_code
