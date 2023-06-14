import csv
import os
import psycopg2


def main():
    with psycopg2.connect(host="localhost", database="north", user="postgres", password="25041988") as conn:
        with conn.cursor() as cur:

            with open(os.path.join('north_data', 'customers_data.csv'), "r", encoding='utf-8') as file:
                customers = csv.DictReader(file)
                for customer in customers:
                    cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", (customer['customer_id'],
                                                                              customer['company_name'],
                                                                              customer['contact_name']))

            with open(os.path.join('north_data', 'employees_data.csv'), "r", encoding='utf-8') as file:
                employees = csv.DictReader(file)
                count = 1
                for employee in employees:
                    cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", (count,
                                                                                          employee['first_name'],
                                                                                          employee['last_name'],
                                                                                          employee['title'],
                                                                                          employee['birth_date'],
                                                                                          employee['notes']))
                    count += 1

            with open(os.path.join('north_data', 'orders_data.csv'), "r", encoding='utf-8') as file:
                orders = csv.DictReader(file)
                for order in orders:
                    cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", (order['order_id'],
                                                                                   order['customer_id'],
                                                                                   order['employee_id'],
                                                                                   order['order_date'],
                                                                                   order['ship_city']))

    conn.close()


if __name__ == '__main__':
    main()
