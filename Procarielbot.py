Woo = ["Hi, ", "Hey, ", "Hello, ", "Heya, "]
Woobutswagger = ["Ayo, ", "Yo, ", "Heyo, "]
Woo2 = ["how are ", "how is ", "", "how's ", "how're "]
Woo2swagger = ["wazzup?", "what's up?", "what's good?", "how you doing?", "what's going on?"]
Finall = ["everything?", "your life?", "your day?", "you?", "you doing?"]
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
  print(Codeliner + ":")
  Jump = input("You: ")
