class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0 # default value always assigned during initialization
        self.following = 0
    
    # methods always require a 'self' input (unlike a funciton)
    def follow(self, user):
        user.followers += 1
        self.following += 1



# with defined function in classes
user_1 = User("001", "Kerry")
user_2 = User("002", "Angela")

user_1.follow(user_2)

print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)



# without defined function arguments in classes
# user_1 = User()
# user_1.id = "001"
# user_1.username = "Kerry"

# print(user_1.username)