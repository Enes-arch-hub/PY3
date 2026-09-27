import pandas as pd

students = {
    "Name": ["Enes", "Alice", "Brian", "Faith", "Mercy"],
    "Age": [22, 20, 21, 23, 22],
    "Score": [88, 95, 79, 91, 85]
}

df = pd.DataFrame(students)

print(df)