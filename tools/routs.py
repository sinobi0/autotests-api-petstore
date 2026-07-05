from enum import Enum

class APIEndpoints(str, Enum):

    PET = "/v2/pet"
    STORE = "/v2/store/order"
    USER = "/v2/user"

    def __str__(self):
        return self.value