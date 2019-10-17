#! python3
# Random Quiz.py - its a random quiz gen.

import random

#the quiz data, keys are states and values are their number of house members

capitals = {'Alabama': '7', 'Alaska': '1', 'Arizona': '9',
'Arkansas': '4', 'California': '53', 'Colorado': '7',
'Connecticut': '5', 'Delaware': '1', 'Florida': '27',
'Georgia': '14', 'Hawaii': '2', 'Idaho': '2', 'Illinois':
'18', 'Indiana': '9', 'Iowa': '4', 'Kansas':
'4', 'Kentucky': '6', 'Louisiana': '6', 'Maine':
'2', 'Maryland': '8', 'Massachusetts': '9', 'Michigan':
'14', 'Minnesota': '8', 'Mississippi': '4', 'Missouri':
'4', 'Montana': '1', 'Nebraska': '3', 'Nevada':
'4', 'New Hampshire': '2', 'New Jersey': '12', 'New Mexico':
'3', 'New York': '27', 'North Carolina': '13',
'North Dakota': '1', 'Ohio': '16', 'Oklahoma': '5',
'Oregon': '5', 'Pennsylvania': '18', 'Rhode Island': '2',
'South Carolina': '7', 'South Dakota': '1', 'Tennessee':
'9', 'Texas': '36', 'Utah': '4', 'Vermont':
'1', 'Virginia': '11', 'Washington': '10', 'West Virginia':
'3', 'Wisconsin': '8', 'Wyoming': '1'}

#Generate 35 quiz files.
for quizNum in range(35):
	quizFile = open('houserepresentativesquiz%s.txt' % (quizNum + 1),
	'w')
	quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
	quizFile.write((' ' * 20) + 'State House of Representatives Quiz (Form %s)' 
	% (quizNum + 1))
	quizFile.write('\n\n')
	
	#shuffle state order
	states = list(representatives.keys())
	random.shuffle(states)
	
	#Get right and wrong answers.
	correctAnswer = representatives[states[questionNum]]
	wrongAnswers = list(representatives.values())
	del wrongAnswers[wrongAnswers.index(correctAnswer)]
	wrongAnswers = random.sample(wrongAnswers, 3)
	answerOptions = wrongAnswers + [correctAnswer]
	random.shuffle(answerOptions)
	
	#write the question and answer options
	quizFile.write('%s. How many House of Representatives are in %s?\n' % (questionNum + 1, states[questionNum]))
	for i in range(4):
		quizFile.write('	%s. %s\n' % ('ABCD'[i], answerOptions[i]))
	quizFile.write('\n")
	
	#write the answer key to file
	answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[ answerOptions.index(correct)]))
	quizFile.close()
	answerKeyFile.close()
