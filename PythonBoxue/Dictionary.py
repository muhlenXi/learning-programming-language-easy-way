
# 在 Python 中使用 dictionary

empty = {}
user = {"email": "11@boxue.io", "wotkId": 11}

empty1 = dict()
user1 = dict(user)

print(user)
print(user["email"])

user["email"] = "10@boxue.io"
user["address"] = "beijing xxxxx"

print(user)
user.update({"age": 18, "sex": "male"})
print(user)

del(user["sex"])

user1.clear()
print(user1)

user1[(11,1101)] = "Floor&room"
print(user1)

print(user.keys())
print(user.values())

print("name" in user)
print("email" in user.keys())