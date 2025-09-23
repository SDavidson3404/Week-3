

class User:
    activeUser = []
    users = {}
    def addUser(self):
        username = input("Please enter a username: ")
        if username not in self.users:
            password = input("Please enter a password: ")
            self.users[username] = password
            return True
        else:
            print("Username taken, please enter a new username")
            return False
    def login(self):
        loginUser = input("Please enter your username: ")
        if loginUser in self.users:
            loginPass = input("Please enter your password")
            if loginPass in self.users:
                print("Logged in")
                self.activeUser.append(loginUser)
                return True
            else:
                print("Password incorrect.")
                return False
        else:
            print("Username not found.")
            return False
    def logout(self):
        confirm = input("Are you sure you want to log out? (Y/N): ")
        if confirm == "Y":
            self.activeUser.clear()
class Post:
    postNum = 1
    posts = {}
    def createPost(self):
        postContent = input("Please enter what you'd like to post")
        self.posts[self.postNum] = {User.activeUser: postContent}
        self.postNum += 1
    def readPosts(self):
        print(self.posts)
    def comment(self):
        print(self.posts)
        commentChoice = input("Which post would you like to comment on?: ")
        for post in self.posts:
            if commentChoice == self.postNum:
                comment = input("What would you like to comment?")
                self.posts[post[User.activeUser]] = comment

loggedIn = User.addUser(User)

def mainPage():
    userChoice = int(input("1. Post, 2. Read Posts, 3. Comment"))
    if userChoice == 1:
        Post.createPost(Post)
    elif userChoice == 2:
        Post.readPosts(Post)
    else:
        Post.comment(Post)
def loginPage():
    userChoice = int(input("Would you like to 1. Login, or 2. create new user"))
    if userChoice == 1:
        User.login(User)
    else:
        User.addUser(User)

while not loggedIn:
    loginPage()
else:
    mainPage()