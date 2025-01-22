username=input("Введите ваше имя: ")
title=input("Заголовок заметки: ")
content=input("Описание заметки: ")
status=input("Статус заметки: ")
created_date=input("Дата начала события(ДД-ММ-ГГГГ): ")
issue_date=input("Дата окончания события(ДД-ММ-ГГГГ): ")
note=[username,
      [title],
      content,
      status,
      created_date,
     issue_date]
print(f"Имя пользователя: {note[0]} "
      f"\nЗаголовок заметки: {note[1][0]} "
      f"\nОписание заметки: {note[2]}"
      f"\nСтатус заметки: {note[3]}"
      f"\nДата начала: {note[4][:5]}"
      f"\nДата окончания: {note[5][:5]}")
