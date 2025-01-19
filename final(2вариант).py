note=["Имя пользователя: ",
      "Заголовок заметки: ",
      ["Заголовок1: ","Заголовок2: "],
      "Описание заметки: ",
      "Статус: ",
      "Дата начала: ",
      "Дата окончания: "]
username=input("Введите ваше имя: ")
title=input("Заголовок заметки: ")
title1=input(note[2][0])
title2=input(note[2][1])
content=input("Описание заметки: ")
status=input("Статус заметки: ")
created_date=input("Дата начала события(ДД-ММ-ГГГГ): ")
itog_created_date=created_date[0:5]
issue_date=input("Дата окончания события(ДД-ММ-ГГГГ): ")
itog_issue_date=issue_date[0:5]
print("Ваше имя: ",username)
print("Заголовок заметки: ",title)
print(note[2][0]+title1)
print(note[2][1]+title2)
print("Описание заметки: ",content)
print("Статус: ",status)
print("Дата начала события: ",itog_created_date)
print("Дата окончания события: ",itog_issue_date)
