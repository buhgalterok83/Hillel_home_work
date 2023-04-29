import datetime

start_date = datetime.date(2023, 3, 27)
lecture_days = [0, 3]  
lecture_time = datetime.time(19, 15)
num_lectures = 32

lecture_dates = []
current_date = start_date
while len(lecture_dates) < num_lectures:
    if current_date.weekday() in lecture_days:
        lecture_dates.append(current_date)
    current_date += datetime.timedelta(days=1)

for i, date in enumerate(lecture_dates):
    day_of_week = date.strftime('%a')
    print(f"Lecture {i+1:2}: {day_of_week} {date:%d %b %Y} {lecture_time}")
