from exercise import Exercise
from cohort import Cohort
from person import Person
from instructor import Instructor
from student import Student

'''
Create 4, or more, exercises.
Create 3, or more, cohorts.
Create 4, or more, students and assign them to one of the cohorts.
Create 3, or more, instructors and assign them to one of the cohorts.
Have each instructor assign 2 exercises to each of the students.
'''

create_webpage = Exercise('Create webpage', 'HTML')
style_webpage = Exercise('Style webpage', 'CSS')
make_dynamic = Exercise('Make dynamic', 'JavaScript')
modularize_javascript = Exercise('Modularize JavaScript', 'JavaScript')

cohort_10 = Cohort('Cohort 10')
cohort_20 = Cohort('Cohort 20')
cohort_30 = Cohort('Cohort 30')

julia = Student('Julia', 'Louis-Dreyfuss', 'Julia Louis-Dreyfuss', cohort_10)
jerry = Student('Jerry', 'Seinfeld', 'Jerry Seinfeld', cohort_20)
jason = Student('Jason', 'Alexander', 'Jason Alexander', cohort_30)
michael = Student('Michael', 'Richards', 'Michael Richards', cohort_10)

joe = Instructor('Joe', 'Shepherd', 'Joe Shepherd', cohort_10, 'Funny Voices')
steve = Instructor('Steve', 'Brownlee', 'Steve Brownlee', cohort_20, 'Teaching')
brenda = Instructor('Brenda', 'Long', 'Brenda Long', cohort_30, 'Design')

joe.assign_exercise(create_webpage, julia)
joe.assign_exercise(create_webpage, jerry)
joe.assign_exercise(create_webpage, jason)
joe.assign_exercise(create_webpage, michael)
joe.assign_exercise(style_webpage, julia)
joe.assign_exercise(style_webpage, jerry)
joe.assign_exercise(style_webpage, jason)
joe.assign_exercise(style_webpage, michael)

steve.assign_exercise(make_dynamic, julia)
steve.assign_exercise(make_dynamic, jerry)
steve.assign_exercise(make_dynamic, jason)
steve.assign_exercise(make_dynamic, michael)
steve.assign_exercise(modularize_javascript, julia)
steve.assign_exercise(modularize_javascript, jerry)
steve.assign_exercise(modularize_javascript, jason)
steve.assign_exercise(modularize_javascript, michael)

brenda.assign_exercise(create_webpage, julia)
brenda.assign_exercise(create_webpage, jerry)
brenda.assign_exercise(create_webpage, jason)
brenda.assign_exercise(create_webpage, michael)
brenda.assign_exercise(make_dynamic, julia)
brenda.assign_exercise(make_dynamic, jerry)
brenda.assign_exercise(make_dynamic, jason)
brenda.assign_exercise(make_dynamic, michael)