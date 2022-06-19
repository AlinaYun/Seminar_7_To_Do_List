import csv
import datetime


def task_input():
    task_input = input('Введите задачу: ').capitalize()
    task_date = datetime.date.today()
    task_description = [task_date, task_input]
    print(f'ЗАДАЧА {task_input} СОЗДАНА {task_date}')
    with open ('list_of_current_tasks.csv', 'a', newline='', encoding='utf-8') as file:
        task = csv.writer(file, delimiter = '\t') 
        task.writerow(task_description)

        
