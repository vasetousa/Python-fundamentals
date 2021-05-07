class Slido:
    def __init__(self, author_name, content, data_time="now", likes=0, dislikes=0, photo="shorturl.at/gwU39"):
        self.author_name = author_name
        self.data = content
        self.data = data_time
        self.likes = likes
        self.dislikes = dislikes
        self.photo = photo

    def present_comment(self):
        return f"{self.author_name}\nLikes: {self.likes} Dislikes: {self.dislikes}\n{self.photo}"


data_input = Slido('Koko', content="not sure")
data_input.likes += 1
data_input.dislikes -= 1
print(data_input.present_comment())