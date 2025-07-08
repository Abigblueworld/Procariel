Woo = ["Hi, ", "Hey, ", "Hello, ", "Heya, "]
Woobutswagger = ["Ayo, ", "Yo, ", "Heyo, "]
Woo2 = ["how are ", "how is ", "", "how's ", "how're "]
Woo2swagger = ["wazzup?", "what's up?", "what's good?", "how you doing?", "what's going on?"]
Finall = ["everything?", "your life?", "your day?", "you?", "you doing?"]
Formatgram = ["I am ", "I'm ", "I", "I was"]
Formatgram2 = ["I've ", "I have ", "I'd ", "I could ", "I would "]
Formatgram3 = ["I got ", "I've got ", "I have got ", "I recived ", "I have recived ", "I've recived "]
Sorrylevels = ["sorry", "very sorry", "so sorry", "super sorry"]
Youformat = ["You are ", "You're ", "You've ", "You have "]
Youformat2 = ["You'd ", "You would ", "You could ", "You should "]
Hobbies = ["read a book", "write a story", "play a game", "sing a song", "dance", "listen to music", "play an instrument"]
Opinions = ["cool", "alright", "good", "fine", "ight"]
Praisestart = ["That's ", "That is ", "Very ", "Wow, ", "Wow, that's"]
Objectnouns = ["It's", "It is"]
Genericone = ["Okay", "Ok", "Alright", "Fine", "Meh", "Good", "Not Much"]
Generictwo = [", you?", ", how about you?", ", u?", ", what about you?"]
Genericthree = ["I guess", "I see", "I understand", "Sure", "Yeah"]


import random
Jump = input("Input a response to start the bot: ")
print("You: " + Jump)
while (0 == 0):
  if ("Hi" in Jump or "hi" in Jump or "hello" in Jump or "Hello" in Jump or "Hey" in Jump or "hey" in Jump):
    Scoots = random.randrange(0, 3)
    Scoots2 = random.randrange(0, 3)
    Scooty = random.randrange(0, 4)
    Codeliner = Woo[Scoots] + Woo2[Scoots2] + Finall[Scooty]
  elif ("ayo" in Jump or "Ayo" in Jump or "Yo" in Jump or "yo" in Jump):
    Scoots = random.randrange(0, 3)
    Scoots2 = random.randrange(0, 3)
    Codeliner = Woobutswagger[Scoots] + Woo2swagger[Scoots2]
  elif ("rude" in Jump or "mean" in Jump):
    Scoots = random.randrange(0, 2)
    Scoots2 = random.randrange(0, 3)
    Codeliner = Formatgram[Scoots] + Sorrylevels[Scoots2]
  elif ("bored" in Jump or "need to do something" in Jump or "need a new hobby" and not "got a hobby" in Jump):
    Scoots = random.randrange(2, 3)
    Scoots2 = random.randrange(0, 4)
    Codeliner = Youformat[Scoots] + Opinions[Scoots2]
  elif ("sorry" in Jump or "feel bad for you" in Jump or "feel bad for ya" in Jump):
    Scoots = random.randrange(0, 1)
    Scoots2 = random.randrange(0, 6)
    Codeliner = Objectnouns[Scoots] + Hobbies[Scoots2]
  else:
    Ranie = random.randrange(1, 2)
    if (Ranie == 1):
      Scoots = random.randrange(0, 6)
      Codeliner = Genericone[Scoots]
    else:
      Scoots = random.randrange(0, 4)
      Codeliner = Genericthree[Scoots]
  print(Codeliner + ":")
  Jump = input("You: ")
