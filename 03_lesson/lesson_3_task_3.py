from address import Address
from mailing import Mailing

to_address = Address("625034", "Тюмень", "Камчатская", "35", "5")
from_address = Address("443047", "Самара", "Пугачевский тракт", "39", "22")

mailing = Mailing(to_address, from_address, 150, "TRACK123")
print(mailing)
