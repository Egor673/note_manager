note=["Имя пользователя: ",
      "Содержание заметки: ",
      "Статус: ",
      "Дата создания: ",
      "Дата изменения: ",
      ["Заголовок1","Заголовок2: "]]
username=input("Введите ваше имя: ")
title=input("Заголовок заметки: ")
title1=[input("1.Основные темы: "),
input("2.Персонажи: "),
input("3.Рекомендации для чтения: ")]
title4=[f"Основные темы:  {title1[0]} ",
        f"Персонажи: {title1[1]} ",
        f"Рекомендации: {title1[2]}"]
content=input("Описание заметки: ")
status=input("Статус заметки: ")
created_date=input("Дата начала события(ДД-ММ-ГГГГ): ")
itog_created_date=created_date[0:5]
issue_date=input("Дата окончания события(ДД-ММ-ГГГГ): ")
itog_issue_date=issue_date[0:5]
print("Ваше имя: ",username)
print("Заголовок заметки: ",title)
print(title4)
print("Описание заметки: ",content)
print("Статус: ",status)
print("Дата начала события: ",itog_created_date)
print("Дата окончания события: ",itog_issue_date)