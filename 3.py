from datetime import datetime, timedelta

start_date = datetime(2023, 3, 27, 19, 15)
lecture_count = 32

for i in range(1, lecture_count + 1):
    lecture_date = start_date + timedelta(days=(i - 1) * 3)
    print(f"Lecture {i:2}: {lecture_date.strftime('%d %b %Y %H:%M')}")
