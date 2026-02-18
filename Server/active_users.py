active_users = 0

def get_active_users():
    return active_users

def add_active_user():
    global active_users
    active_users += 1

def remove_active_user():
    global active_users
    if active_users > 0:
        active_users -= 1
