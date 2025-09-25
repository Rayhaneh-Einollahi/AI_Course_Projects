import pandas as pd

df = pd.read_csv("Grades.csv")

df.drop(columns=["sex", "age", "reason"], errors="ignore", inplace=True)
valid_values = {
    "university": {"PR", "CM"},
    "address": {"U", "R"},
    "motherEducation": range(0, 5),
    "fatherEducation": range(0, 5),
    "motherJob": {"teacher", "health", "services", "at_home"},
    "fatherJob": {"teacher", "health", "services", "at_home"},
    "travelTime": {1, 2, 3, 4},
    "studyTime": {1, 2, 3, 4},
    "failures": {0, 1, 2, 3, 4},
    "universitySupport": {"yes", "no"},
    "paid": {"yes", "no"},
    "higher": {"yes", "no"},
    "internet": {"yes", "no"},
    "romantic": {"yes", "no"},
    "freeTime": range(1, 6),
    "goOut": range(1, 6),
    "Dalc": range(1, 6),
    "Walc": range(1, 6),
    "absences": range(0, 94),
    "EPSGrade": range(0, 21),
    "DSGrade": range(0, 21),
    "finalGrade": range(0, 21),
}

default_values = {
    "university": "PR",
    "address": "U",
    "motherEducation": 2,
    "fatherEducation": 2,
    "motherJob": "services",
    "fatherJob": "services",
    "travelTime": 1,
    "studyTime": 2,
    "failures": 0,
    "universitySupport": "no",
    "paid": "no",
    "higher": "yes",
    "internet": "yes",
    "romantic": "no",
    "freeTime": 3,
    "goOut": 3,
    "Dalc": 1,
    "Walc": 1,
    "absences": 0,
    "EPSGrade": 10,
    "DSGrade": 10,
    "finalGrade": 10,
}

def validate_and_fix(value, valid_set, default):
    try:
        if isinstance(valid_set, range):
            return int(value) if int(value) in valid_set else default
        return value if value in valid_set else default
    except:
        return default

for col in valid_values:
    if col in df.columns:
        df[col] = df[col].apply(lambda x: validate_and_fix(x, valid_values[col], default_values[col]))

text_to_num = {
    "university": {"PR": 0, "CM": 1},
    "address": {"U": 0, "R": 1},
    "motherJob": {"teacher": 0, "health": 1, "services": 2, "at_home": 3},
    "fatherJob": {"teacher": 0, "health": 1, "services": 2, "at_home": 3},
    "universitySupport": {"no": 0, "yes": 1},
    "paid": {"no": 0, "yes": 1},
    "higher": {"no": 0, "yes": 1},
    "internet": {"no": 0, "yes": 1},
    "romantic": {"no": 0, "yes": 1},
}

for col, mapping in text_to_num.items():
    if col in df.columns:
        df[col] = df[col].map(mapping)

df.to_csv("Grades_prep.csv", index=False)
