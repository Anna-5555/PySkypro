from address import Address
from mailing import Mailing

# Создаём два адреса
to_address = Address("123456", "Москва", "Ленина", "10", "25")
from_address = Address("654321", "Санкт-Петербург", "Пушкина", "5", "30")

# Создаём почтовое отправление
mail = Mailing(to_address, from_address, 1000, "ABC123")

# Выводим данные в заданном формате
print(f"Отправление {mail.track} из {mail.from_address.index},"
      f" {mail.from_address.city}, {mail.from_address.street}, "
      f"{mail.from_address.house} - {mail.from_address.apartment}"
      f" в {mail.to_address.index}, {mail.to_address.city}, "
      f"{mail.to_address.street}, {mail.to_address.house} - "
      f"{mail.to_address.apartment}. Стоимость {mail.cost} рублей.")

