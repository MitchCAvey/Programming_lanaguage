

# class User:
#     pass
#     # id = ""
#     # username = ""

# user_1 = User()

# # We can create attributes on the fly,
# # as shown below
# user_1.id = "001"
# user_1.username = "Mitch"

# print(user_1.username)
# print(user_1.id)

# user_2 = User()

# user_2.id = "002"
# user_2.username = "Jim"

class User:
    # This is to set what each object is initial values should be
    def __init__(self, user_id, username):
        print("New User Being Created...")
        self.username = username
        self.id = user_id
        self.score = 0
        self.followers = 0
        self.following = 0
    
    def updateUserScore(self):
        self.score += 1
    
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Mitch")    
user_2 = User("002", "Jim")
# user_1.id = "001"
# user_1.username = "Mitch"
print(user_1.username)
print(user_1.id)
print(user_1.score)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)