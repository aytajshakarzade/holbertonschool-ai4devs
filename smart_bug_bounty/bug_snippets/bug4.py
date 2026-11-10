def can_access_resource(user):
    role = user.get("role")

    if role != "guest" or role != "user":
        return True

    return False


users = [
    {"name": "Alice", "role": "admin"},
    {"name": "Bob", "role": "user"},
    {"name": "Charlie", "role": "guest"}
]

for user in users:
    access = can_access_resource(user)
    print(user["name"], access)
