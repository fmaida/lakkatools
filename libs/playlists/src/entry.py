class Entry:

    def __init__(self, playlist="default"):
        self.path = ""
        self.title = ""
        self.core_path = "DETECT"
        self.core_name = "DETECT"
        self.database_link = "DETECT"
        self.playlist = playlist

    def __str__(self):
        temp = ""
        temp += self.path + "\n"
        temp += self.title + "\n"
        temp += self.core_path + "\n"
        temp += self.core_name + "\n"
        temp += self.database_link + "\n"
        temp += self.playlist + "\n"
        return temp
