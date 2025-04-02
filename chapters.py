actions = {
	"1A": "ripped down the poster",
	"1B": "texted",
	"2A": "ran home as fast as possible",
	"2B": "continued home like nothing was wrong"
}


class Reader:
	def __init__(self, name, animal):
		self.name = name
		self.animal = animal
		self.answers = []


def introduction():
	name = input("Hello! What is your name? ")
	animal = input("What is your favorite animal? ")
	reader = Reader(name,animal)
	print(f"Nice to meet you {name}, let's start your adventure!")
	return reader

def chapter_one(reader):
	print(f"You come across a poster with your picture on it and big bold letters \n'WANTED {reader.name} for kidnapping {reader.animal} \nText this number if you have any information'.")
	answer1 = input("You are shocked by the poster, you have not kidnapped any animals! What do you do? A) Rip down the poster B) Text the number on the poster ")
	return answer1

def chapter_two_rip():
	print(f"You rip down the poster and toss it in the nearest garbage can. 'There' you think, 'problem solved!', as you continue your walk. You turn the corner to head back to your house and see a poster on every street sign.")
	answer2 = input("What do you do? A) Run home and hide  B) Act casual and walk home like nothing is wrong ")
	return answer2

def chapter_two_text(reader):
	print(f"You write a quick message, 'Hello, my name is {reader.name} but I don't know about any missing {reader.animal}'. Immediately after sending the text, you recive back a response, 'Where are you??'")
	answer2 = input("What do you do? A) Run home and shut off your phone B) Continue walking home while thinking how to respond ")
	return answer2

def chapter_three_home(reader):
	chapter2Action = "2" + reader.answers[1]
	print(f"Since you {actions[chapter2Action]}, you anxiously pace the living room when you hear a knock on the door")
	answer2 = input("What do you do? A)  B)  ")
	return answer2
