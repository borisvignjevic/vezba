

students = [{
    "name" : "Boris",
    "score" : 95,
    "active" : True
},
{
    "name" : "Sneki",
    "score" : 95,
    "active" : True

},
{
    "name" : "Masa",
    "score" : 75,
    "active" : False
},
]

for student in students:
    if not student['active']:
        continue
    if student ['score'] >= 80:
        student['grade'] = "A"
    elif student['score'] <= 80 and student['score'] >= 60:
        student['grade'] = "B"
    elif student['score'] < 60 and student['score'] >= 40:
          student['grade'] = "C"
    elif student['score'] < 40 and student['score'] >= 20:
          student['grade'] = "D"
    else:
        student['grade'] = "F"

print(students)