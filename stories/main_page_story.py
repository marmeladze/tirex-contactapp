class MainPageStory:
    def __init__(self):
        pass

    def run(self):
        print("""
MAIN    [Returns main page]
ADD     [Add person to contacts]
FIND    [Find person in contacts]
""")
        return input("::=>")