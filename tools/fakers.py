from faker import Faker


class Fake:

    def __init__(self, faker: Faker):
        self.faker = faker

    def random_int(self) -> int:
        """
        Генерирует радномное число
        """
        return self.faker.random_int(1, 100000000)

    def random_name(self) -> str:
        """
        Генерирует рандомное имя
        :return:
        """
        return self.faker.first_name(

        )

    def random_last_name(self):
        """
        Генерирует рандомную фамилию
        """
        return self.faker.last_name()

    def random_email(self) -> str:
        """
        Генерирует рандомную почту
        """
        return self.faker.email()

    def random_photo(self) -> list:
        """Генерирует от 1 до 3 случайных URL-адресов для фотографий."""
        return [self.faker.image_url() for _ in range(self.faker.random_int(1, 3))]

    def random_tag(self) -> object:
        """
        Генерирует рандомный тег
        """
        return {
            "id": self.random_int(),
            "name": self.faker.word()
        }

    def random_word(self) -> str:
        """
        Генерирует рандомное слово
        """
        return self.faker.word()

    def random_date(self) -> str:
        """
        Генерирует рандомную дату в формате iso8601
        """
        return str(self.faker.iso8601())

    def random_password(self) -> str:
        """
        Генерирует рандомный пароль
        """
        return self.faker.password(length=8)

    def random_phone(self) -> str:
        """
        Генерирует рандомный номер телефона
        """
        return self.faker.phone_number()


fake = Fake(faker=Faker())

print(fake.random_tag())
