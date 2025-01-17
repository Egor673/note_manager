username=input("Введите ваше имя:")
title=input("Заголовок заметки:")
content=input("Описание заметки:")
status=input("Статус заметки:")
created_date = input("Дата начала события(ДД-ММ-ГГГГ):")
temp_created_date="12-11-2020"
issue_date = input("Дата окончания события(ДД-ММ-ГГГГ):")
temp_issue_date="14-11-2020"
print("Введите ваше имя:",username)
print("Заголовок заметки:",title)
print("Описание заметки:",content)
print("Статус заметки:",status)
print("Дата начала события:",temp_created_date[0:5])
print("Дата окончания события:",temp_issue_date[0:5])