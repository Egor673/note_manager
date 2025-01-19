username=input("Введите ваше имя: ")
title=input("Заголовок заметки: ")
title1=input("1.Основные темы: ")
title2=input("2.Персонажи: ")
title3=input("3.Рекомендации для чтения: ")
title4=[title1,title2,title3]
content=input("Описание заметки: ")
status=input("Статус заметки: ")
created_date=input("Дата начала события(ДД-ММ-ГГГГ): ")
itog_created_date=created_date[0:5]
issue_date=input("Дата окончания события(ДД-ММ-ГГГГ): ")
itog_issue_date=issue_date[0:5]
print("Ваше имя: ",username)
print("Заголовок заметки: ",title)
print(f"1.Основные темы:  {title4[0]} 2.Персонажи: {title4[1]} Рекомендации для чтения: {title4[1]}")
print("Описание заметки: ",content)
print("Статус: ",status)
print("Дата начала события: ",itog_created_date)
print("Дата окончания события: ",itog_issue_date)
