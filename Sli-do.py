class Slido:
    def __init__(self, username, content,  data_time="now",  likes=0, dislikes=0, photo="shorturl.at/gwU39"):
        self.username = username
        self.photo = photo
        self.likes = likes
        self.dislikes = dislikes
        self.data = content
        self.data = data_time

    def present_comment(self):
        return f"{self.username}\n{self.likes} {self.dislikes}\n{self.photo}"


data_input = Slido('Koko', content="not sure")
print(data_input.present_comment())