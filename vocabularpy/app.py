import yaml
class VocabularpyApp:

    @classmethod
    def getUsers(cls):
        if not cls.users:
            cls.users = {}

        return cls.users

    def __init__(self, aUser, aLanguage):
        self.user = aUser
        self.language = aLanguage

