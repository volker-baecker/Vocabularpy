class Lesson(object):

    def __init__(self):
        self._cards = []

    def addCard(self, aCard):
        self._cards.append(aCard)


class Card(object):

    def __init__(self):
        self._word = ""
        self._translation1 = ""
        self._translation2 = ""
        self._translation3 = ""
        self._sentence = ""
        self._mnemonic = ""
        self._imageURL = ""

    @property
    def word(self):
        return self._word

    @word.setter
    def word(self, aWord):
        self._word = aWord

    @property
    def translation1(self):
        return self._translation1

    @translation1.setter
    def translation1(self, aTranslation):
        self._translation1 = aTranslation

    @property
    def translation2(self):
        return self._translation2

    @translation2.setter
    def translation2(self, aTranslation):
        self._translation2 = aTranslation

    @property
    def translation3(self):
        return self._translation3

    @translation3.setter
    def translation3(self, aTranslation):
        self._translation3 = aTranslation

    @property
    def sentence(self):
        return self._sentence

    @sentence.setter
    def sentence(self, aSentence):
        self._sentence = aSentence

    @property
    def mnemonic(self):
        return self._mnemonic

    @mnemonic.setter
    def mnemonic(self, aMnemonic):
        self._mnemonic = aMnemonic

    @property
    def imageURL(self):
        return self._imageURL

    @imageURL.setter
    def imageURL(self, anImageURL):
        self._imageURL = anImageURL

    def asList(self):
        result = [self.word+"\n",
                  self.sentence + "\n",
                  self.translation1+"\n",
                  self.translation2+"\n",
                  self.translation3+"\n",
                  self.mnemonic+"\n",
                  self.imageURL]
        return result

    def saveTo(self, fileURL):
        with open(fileURL, 'w', encoding='utf-8') as out:
            out.writelines(self.asList())

    @classmethod
    def readFrom(cls, fileURL):
        result = Card()
        with open(fileURL, 'r', encoding='utf-8') as file:
            content = file.read()
            lines = content.split("\n")
        result.word = lines[0]
        result.mnemonic = lines[5]
        result.translation1 = lines[2]
        result.translation2 = lines[3]
        result.translation3 = lines[4]
        result.sentence = lines[1]
        result.imageURL = lines[6]
        return result


