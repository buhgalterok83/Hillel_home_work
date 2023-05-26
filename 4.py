import pandas as pd
import pymysql


connection = pymysql.connect(host='localhost', user='username', password='password', db='master')

query = "SELECT dns FROM master.school"
dns_df = pd.read_sql_query(query, connection)
dns_list = dns_df['dns'].tolist()

total_excellent_10 = 0
total_excellent_11 = 0
total_students_11 = 0

for dns in dns_list:

    db = pymysql.connect(host=dns, user='username', password='password', db='school%')


    school_query = "SELECT id FROM master.school WHERE dns = %s AND academic_year = '2022,2023'"
    school_id = pd.read_sql_query(school_query, db, params=[dns])['id'].values[0]


    class_query = "SELECT id FROM class WHERE school_id = %s AND parallel = '11'"
    class_df = pd.read_sql_query(class_query, db, params=[school_id])
    class_ids = class_df['id'].tolist()


    for class_id in class_ids:
        schoolboy_query = "SELECT id FROM schoolboy WHERE class_id = %s"
        schoolboy_df = pd.read_sql_query(schoolboy_query, db, params=[class_id])
        schoolboy_ids = schoolboy_df['id'].tolist()

        
        total_students_11 += len(schoolboy_ids)

     
        for schoolboy_id in schoolboy_ids:
            rate_query = "SELECT rate FROM rate WHERE schoolboy_id = %s"
            rate_df = pd.read_sql_query(rate_query, db, params=[schoolboy_id])
            rates = rate_df['rate'].tolist()


            average_rate = sum(rates) / len(rates)


            if average_rate >= 10:
                total_excellent_10 += 1

            if average_rate >= 11:
                total_excellent_11 += 1





print("Total Excellent Students (10+):", total_excellent_10)
print("Total Outstanding Students (11+):", total_excellent_11)
print("Total Students in 11th parallel:", total_students_11)

