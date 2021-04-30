class Comment:
    def __init__(self, username, content, likes=0) -> object:
        self.username = username
        self.content = content
        self.likes = likes


comment = Comment("User1", "I like this book", 30)
comment2 = Comment("Vasko", "Python programmer", 48)

print(comment2.username)
print(comment2.content)
print(comment2.likes)