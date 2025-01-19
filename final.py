note=["Имя пользователя: ",
      "Заголовок заметки: ",
      ["Заголовок1: ","Заголовок2: "],
      "Описание заметки: ",
      "Статус: ",
      "Дата начала(ДД-ММ-ГГГГ): ",
      "Дата окончания(ДД-ММ-ГГГГ): "]
note1=[input(note[0]),
input(note[1]),
input(note[2][0]),
input(note[2][1]),
input(note[3]),
input(note[4]),
input(note[5]),
input(note[6])]
print(note[0]+note1[0])
print(note[1]+note1[1])
print(note[2][0]+note1[2])
print(note[2][1]+note1[3])
print(note[3]+note1[4])
print(note[4]+note1[5])
print(note[5]+note1[6][0:5])
print(note[6]+note1[7][0:5])
