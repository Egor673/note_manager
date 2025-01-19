note=["Имя пользователя: ",
      "Содержание заметки: ",
      "Статус: ",
      "Дата создания: ",
      "Дата изменения: ",
      ["Заголовок1","Заголовок2: "]]
note1=[input(note[0]),
input(note[1]),
input(note[2]),
input(note[3]),
input(note[4]),
input(note[5])]
print(note[0]+note1[0])
print(note[1]+note1[1])
print(note[2]+note1[2])
print(note[3]+note1[3])
print(note[4]+note1[4])
print(f"Заголовки: ",note1[5])
