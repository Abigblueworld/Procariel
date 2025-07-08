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
Objectnouns = ["It's ", "It is ", "It will be "]
Genericone = ["Okay", "Ok", "Alright", "Fine", "Meh", "Good", "Not Much"]
Generictwo = [", you?", ", how about you?", ", u?", ", what about you?"]
Genericthree = ["I guess", "I see", "I understand", "Sure", "Yeah"]
Opinionthought = ["I have no opinion", "I have no thoughts", "I don't know", "I can't tell you", "I don't do opinions"]
Askingaboutbot = ["I guess", "Whatever you say", "Yes and no?", "I'm a program", "Beep Boop boop", "Maybe, I guess"]
Whatanswer = ["Nothing", "Was I being confusing?", "Whoops", "My bad", "Forget it", "Whatever"]
Whatisname = ["My name is Procariel", "I'm Procariel", "I am Procariel", "My name's Procariel", "I'm just Procariel"]
      


import random
Jump = input("Input a response to start the bot: ")
print("You: " + Jump)
while (0 == 0):
  if ("Hi" in Jump or Jump == "hi" or "hello" in Jump or "Hello" in Jump or "Hey" in Jump or "hey" in Jump):
    Scoots = random.randrange(0, 3)
    Scoots2 = random.randrange(0, 3)
    Scooty = random.randrange(0, 4)
    Codeliner = Woo[Scoots] + Woo2[Scoots2] + Finall[Scooty]
  elif ("ayo" in Jump or "Ayo" in Jump or "Yo" in Jump or "yo" in Jump and not "you" in Jump and not "You" in Jump):
    Scoots = random.randrange(0, 3)
    Scoots2 = random.randrange(0, 3)
    Codeliner = Woobutswagger[Scoots] + Woo2swagger[Scoots2]
  elif ("rude" in Jump or "mean" in Jump):
    Scoots = random.randrange(0, 2)
    Scoots2 = random.randrange(0, 3)
    Codeliner = Formatgram[Scoots] + Sorrylevels[Scoots2]
  elif ("bored" in Jump or "need to do something" in Jump or "need a new hobby" in Jump):
    Scoots = random.randrange(2, 3)
    Scoots2 = random.randrange(0, 4)
    Codeliner = Youformat2[Scoots] + Hobbies[Scoots2]
  elif ("sorry" in Jump or "feel bad for you" in Jump or "feel bad for ya" in Jump):
    Scoots = random.randrange(0, 2)
    Scoots2 = random.randrange(0, 4)
    Codeliner = Objectnouns[Scoots] + Opinions[Scoots2]
  elif ("Do you" in Jump or "do you" in Jump):
    Scoots2 = random.randrange(0, 4)
    Codeliner = Opinionthought[Scoots2]
  elif ("How are" in Jump or "how are" in Jump):
    Spinner = random.randrange(0, 2)
    if (Spinner == 1):
      Scoots2 = random.randrange(0, 5)
      Codeliner = Genericone[Scoots2]
    else:
      Scoots2 = random.randrange(0, 5)
      Scoots = random.randrange(0, 3)
      Codeliner = Genericone[Scoots2] + Generictwo[Scoots]
  elif ("Are you a robot" in Jump or "you a robot" in Jump):
    Scoots = random.randrange(0, 5)
    Codeliner = Askingaboutbot[Scoots]
  elif ("What" in Jump or "what" in Jump or "Huh" in Jump or "huh" in Jump):
    Scoots = random.randrange(0, 5)
    Codeliner = Whatanswer[Scoots]
  elif ("your name" in Jump or "Your name" in Jump):
    Spinner = random.randrange(0, 2)
    if (Spinner == 1):
      Scoots = random.randrange(0, 5)
      Codeliner = Whatisname[Scoots]
    else:
      Scoots = random.randrange(0, 5)
      Scoots2 = random.randrange(0, 3)
      Codeliner = Whatisname[Scoots] + Generictwo[Scoots2]
      #Here's where the fun starts!
      Names = input(Codeliner)
  elif ("" in Jump or Jump == " " or "  " in Jump):
    Ranie = random.randrange(0, 2)
    if (Ranie == 1):
      Scoots = random.randrange(0, 6)
      Codeliner = Genericone[Scoots]
    else:
      Scoots = random.randrange(0, 4)
      Codeliner = Genericthree[Scoots]
  print(Codeliner + ":")
  Jump = input("You: ")
