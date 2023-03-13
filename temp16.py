poem = input("Введите стихотворение Винни - Пуха: ")
phrases = poem.split()
vowels_counts = []
for phrase in phrases:
    vowels_count = sum([1 for letter in phrase if letter.lower() in "аеёиоуыэюя"])
    if len(set(vowels_counts))==1:
        print("Парам пам- пам")
    else:
        print("Пам парам")