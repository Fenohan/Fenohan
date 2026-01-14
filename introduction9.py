
def toradroa(x):
    return (x * x)

def direBonjour(nom):
    print(f"Manao ahoana Ra-{nom} manome {toradroa(9)} ny valiny")


direBonjour("bill")

def user (name, age, is_married=False):
    profile = {
        "name": name,
        "age" : age,
        "is_married":is_married
    }

    if is_married:
        profile["status"] = "married"

    return profile

user1 = user("Alice",30)

print(user1)