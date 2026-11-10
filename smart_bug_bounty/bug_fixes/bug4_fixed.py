def can_access_resource(user):
    if not isinstance(user, dict):
        return False

    allowed_roles = {"admin"}
    role = user.get("role")

    return role in allowed_roles


users = [
    {"name": "Alice", "role": "admin"},
    {"name": "Bob", "role": "user"},
    {"name": "Charlie", "role": "guest"},
    {"name": "David"}
]

assert can_access_resource(users[0]) is True
assert can_access_resource(users[1]) is False
assert can_access_resource(users[2]) is False
assert can_access_resource(users[3]) is False
assert can_access_resource(None) is False

print("All bug4 tests passed!")
