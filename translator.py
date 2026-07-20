dictionary = {
    "hello":"привет",
    "goodbye" : "до свидания",
    "cat":"кот",
    "dog":"собака",
    "water":"вода",
}
word = input("Enter an english word: ").lower()

if word in dictionary:
    print(dictionary[word])
else:
   print("Word not in dictionary")