# Task 1

student = {
    "name": "Vasya",
    "age": 23,
    "subjects": ["maths", "biology", "astronomy"],
    "average_score": 4.7,
}

student["average_score"] = 4.75
student["subjects"].append("physics")
student.pop("age")

if "age" in student:
    print("Ключ 'age' существует в словаре")
else:
    print("Ключa 'age' не существует в словаре")

if "gender" in student:
    print("Ключ 'gender' существует в словаре")
else:
    print("Ключa 'gender' не существует в словаре")

print(student.keys())
print(student.values())


# Task 2

response = {
    "cartButtonEnabled": True,
    "conditions": {
        "campaign": {
            "id": "unlimited_burn_99rub_prd",
            "info": "Доставка в пункт выдачи от",
            "link": "https://support.avito.ru/articles/2369"
        },
        "destination": "по Дзержинску",
        "discount": 900,
        "minDays": 1,
        "price": 99,
        "terms": "От 1 дня, от",
        "trustfactors": [
            {
                "helpIcon": False,
                "icon": "cod",
                "label": "",
                "text": "Можно оплатить при получении"
            }
        ]
    },
    "services": [
        {
            "available": True,
            "enabled": True,
            "type": "delivery"
        },
        {
            "available": True,
            "enabled": True,
            "type": "deliveryCourier"
        },
        {
            "available": False,
            "enabled": False,
            "type": "deliveryCourierD2D"
        },
    ]
}

print(response["conditions"]["trustfactors"][0]["icon"])
print(response["conditions"]["campaign"]["id"])

helpIcon = response["conditions"]["trustfactors"][0]["helpIcon"]
if helpIcon is False:
    print("helpIcon = False")
else:
    print("helpIcon не равен False")

type_of_third_services_element = response["services"][2]["type"]
print(type_of_third_services_element)
