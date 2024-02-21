# Задание 3: Ответственный сотрудник

def find_responsible_employee(tasks_completed):
    max_tasks = max(tasks_completed.values())
    responsible_employees = [employee for employee, tasks in tasks_completed.items() if tasks == max_tasks]
    if len(responsible_employees) == len(tasks_completed):
        return ", ".join(responsible_employees)
    else:
        return responsible_employees[0]

tasks_completed = {"Анна": 5, "Боб": 7, "Сьюзан": 9}
responsible_employee = find_responsible_employee(tasks_completed)
print("Самый ответственный:", responsible_employee)

tasks_completed = {"Джон": 1, "Майк": 1, "Эмили": 1}
responsible_employee = find_responsible_employee(tasks_completed)
print("Самый ответственный:", responsible_employee)
