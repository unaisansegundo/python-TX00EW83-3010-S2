class Publication:
    def __init__(self, name: str):
        self.name = name

    def print_information(self):
        print(f"Publication name: {self.name}",end = "")

class Book(Publication):
    def __init__(self, name: str, author: str, page_n: int):
        super().__init__(name)
        self.author = author
        self.page_count = page_n
    def print_information(self):
        super().print_information()
        print(f", Author: {self.author}, Pages: {self.page_count}")
     

class Magazine(Publication):
    def __init__(self, name: str, chief_editor: str):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        super().print_information()
        print(f", Chief Editor: {self.chief_editor}")

magazine = Magazine("Donald Duck", "Aki Hyyppä")
book = Book("Compartment No. 6", "Rosa Liksom", 192)

magazine.print_information()
book.print_information()
