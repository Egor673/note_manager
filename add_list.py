username=input("Введите ваше имя:")
title=input("Заголовок заметки:")
title1=input("Основные темы")
title2=input("Персонажи")
title3=input("Рекомендации для чтения")
title4=[title1,title2,title3]
print(title4[:3])
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





