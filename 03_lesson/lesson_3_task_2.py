from smartphone import Smartphone


catalog = [Smartphone("Samsung", "Galaxy", "+75199678636"),
           Smartphone("Huawei", "12Pro", "+74776984828"),
           Smartphone("Honor", "30", "+70725466510"),
           Smartphone("Redmi", "note", "+74038962629"),
           Smartphone("Nokia", "3310", "+71102226496")]
for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model} - {smartphone.number}")
