import os

from .entry import Entry


class Playlist:

    def __init__(self, path, title=None):
        self.title = "default" if not title else title
        self.path = path
        self.values = []
        self.import_folder(self.path)

    def import_folder(self, path):
        for a, b, values in os.walk(path):
            for element in values:
                if element[0] != "." and ((".zip" in element) or
                                        (".chd" in element)):
                    path = os.path.join(self.rom_path, element)
                    path = os.path.abspath(path)
                    self.values.append((path, element))

    def save(self, filename):
        f = open(filename, "w")
        temp = ""
        for elemento in self.values:
            title = elemento[1].split(".")[0].strip()
            path = elemento[0]
            e = Entry(playlist=self.title)
            e.path = path
            e.title = title
            temp += str(e)
        f.write(temp)
        f.close()
