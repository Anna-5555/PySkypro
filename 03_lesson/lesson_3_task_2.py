from smartphone import Smartphone

# Создаём пустой каталог
catalog = []

# Добавляем 5 смартфонов в каталог
catalog.append(Smartphone("Samsung", "Galaxy S23", "+79123456789"))
catalog.append(Smartphone("Apple", "iPhone 15", "+79234567890"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 12", "+79345678901"))
catalog.append(Smartphone("Google", "Pixel 7", "+79456789012"))
catalog.append(Smartphone("OnePlus", "11 Pro", "+79567890123"))

# Выводим каталог в заданном формате
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
