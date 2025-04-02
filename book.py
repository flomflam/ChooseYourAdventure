import chapters

#Start the book with the introduction
reader = chapters.introduction()

#Pass the introduction questions to chapter one
answer1 = chapters.chapter_one(reader)
#Capitalize the answer so both lowercase and uppercase work the same
answer1 = answer1.capitalize()
#Save the answer to chapter one in spot 0
reader.answers.insert(0, answer1)

answer2 = None
#If they ansered 'A' go down the chapter two rip path
if 'A' == answer1:
	answer2 = chapters.chapter_two_rip()
#If they answered 'B' go down the chapter two text path
elif 'B' == answer1:
	answer2 = chapters.chapter_two_text(reader)

reader.answers.insert(1, answer2)

answer3 = None
#If they ansered 'A' go down the chapter two rip path
if 'A' == answer2:
	answer3 = chapters.chapter_three_home(reader)
#If they answered 'B' go down the chapter two text path
elif 'B' == answer2:
	answer3 = chapters.chapter_three_home(reader)
answer3 = answer3.capitalize()
reader.answers.insert(2, answer3)
