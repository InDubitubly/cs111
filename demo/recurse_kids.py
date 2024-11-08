students = {"bob":3,
            "joe":3,
            "scott":4,
            "jeb":5,
            "greaseball":5,
            "goose":6,
            "kneep":7,
            "staton":7,
            "vice":8,
            "gander":9,
            "fireball":9,
            "sue":10,
            "jen":10,
            "zamasu":10
            }

def failing_iter(n):
    failures = []
    i = 0
    for i in students.keys():
        if student.get(i) < n:
            failures.append(i)

