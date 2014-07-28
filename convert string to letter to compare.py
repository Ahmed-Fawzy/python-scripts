#!/usr/bin/python

#convert string to letter to compare with letter in list "English String and english list"

Answers = raw_input("Enter the student answers : ")
Ans_list = list(Answers)

Template = ['a','b','b','c','d','a','a']
right_ans = 0
false_ans = 0

for i in range(len(Template)) :
	if Ans_list[i]  == Template[i] :
		right_ans += 1
	else :
		false_ans += 1

print "Right Answers are ", right_ans
print "False Answers are ", false_ans
