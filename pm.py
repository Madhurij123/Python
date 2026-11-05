# Load credentials
users = {}
with open("users.txt") as f:
    for line in f:
        u, p = line.split()
        users[u] = p

# Login
user = input("Enter username: ")
pwd = input("Enter password: ")

if user in users and users[user] == pwd:
    print("Login Successful!")
else:
    print("Invalid username or password.")
