from faker import Faker

from clients.pet.pet_schema import TagSchema


class Fake:

    def __init__(self, faker: Faker):
        self.faker = faker

    def random_int(self) -> int:
        return self.faker.random_int(1, 100000000)

    def random_name(self) -> str:
        return self.faker.first_name(

        )

    def random_photo(self) -> list:
        """Генерирует от 1 до 3 случайных URL-адресов для фотографий."""
        return [self.faker.image_url() for _ in range(self.faker.random_int(1, 3))]

    def random_tag(self) -> object:
        return TagSchema(id=self.random_int(), name=self.faker.string)

    def random_word(self) -> str:
        return self.faker.word()

    def random_date(self) -> str:
        return str(self.faker.iso8601())

    def random_password(self) -> str:
        return self.faker.password(length=8)

fake = Fake(faker=Faker())

print(fake.random_tag())
