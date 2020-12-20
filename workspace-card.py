from vocabularpy.model import Card
aCard = Card()
aCard.word = "سلام جهان!"
aCard.translation1 = "Hello World!"
aCard.translation2 = "Hi World!"
aCard.translation3 = "Greetings World!"
aCard.sentence = "سلام جهان, تو چطوری"
aCard.mnemonic = "Saal OM, (d)ja hohn"
aCard.imageURL = "helloworld.jpeg"
print(aCard.word)
print(aCard.translation1)
print(aCard.translation2)
print(aCard.translation3)
print(aCard.sentence)
print(aCard.mnemonic)
print(aCard.imageURL)
aCard.saveTo('test_output.yml')
anotherCard = Card.readFrom('test_output.yml')
print(anotherCard.word)
print(anotherCard.translation1)
print(anotherCard.translation2)
print(anotherCard.translation3)
print(anotherCard.sentence)
print(anotherCard.mnemonic)
print(anotherCard.imageURL)


