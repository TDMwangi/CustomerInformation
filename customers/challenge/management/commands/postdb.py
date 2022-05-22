from django.core.management.base import BaseCommand
import psycopg2
import pandas as pd

df = pd.read_csv('customer_location.csv')

class Command(BaseCommand):
    con = psycopg2.connect(
        host = "localhost",
        database = "customers",
        user = "postgres",
        password = "postgres_password",
        port = 5432
    )
    cur = con.cursor()
    for row in df.itertuples():
        command = '''
            INSERT INTO challenge_customer(
                id, first_name, last_name, email, gender, company, city, title, lat, lng
            )
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
        columns = (
            row.id, row.first_name, row.last_name, row.email, row.gender,
            row.company, row.city, row.title, row.lat, row.lng
        )
        cur.execute(command, columns)
        con.commit()
    con.close()
    def handle(self, *args, **kwargs):
        print("Execution success")