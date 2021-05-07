class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes

dragons = []

while True:
    a = input().split()
    comment = Comment(a[0], a[1], a[2])
    dragons.append(comment)
    print(comment.username)
    print(comment.content)
    print(comment.likes)
