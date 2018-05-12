import random
import os
import time

#----------------------------------------------------------------------------------FUNCTIONS

def banner():	#will serve as the header
	os.system("clear")	#clears the visible surface of the terminal
	print()
	print("      00   00  000  0000   00  0000000         000   000  000  0000   00")
	print("     00   00  00 00  00 00  00  00            00 0 0 00  00 00  00 00  00")
	print("    0000000  0000000  00  00 00  00  000     00  0  00  0000000  00  00 00")
	print("   00   00  00     00  00   0 00  00    0   00     00  00     00  00   0 00")
	print("  00   00  00       00  00   0000  0000000 00     00  00       00  00   0000")
	print()
	
def menu():
	banner()
	print()
	print("\t\t\t  * * * * * *  * * * * * *")
	print("\t\t\t  *                      *")
	print("\t\t\t  *   [1]  PLAY          *")
	print("\t\t\t  *   [2]  INSTRUCTIONS  *")
	print("\t\t\t  *   [0]  EXIT          *")
	print("\t\t\t  *                      *")
	print("\t\t\t  * * * * * *  * * * * * *")
	
def intro():
	banner()
	
	print("\t\t\t  * * * * * *  * * * * * *")
	username = input("\t\t\t   Enter your name: ")
	
	#i want to give the feels of a real game 
	print("\t\t\t       Initializing...")
	print("\t\t\t       00000000000000")
	time.sleep(0.7)
	print("\t\t\t        000000000000")
	time.sleep(0.7)
	print("\t\t\t         0000000000")
	time.sleep(0.7)
	print("\t\t\t          00000000")
	time.sleep(0.7)
	print("\t\t\t           000000")
	time.sleep(0.7)
	print("\t\t\t            0000")
	time.sleep(0.7)
	print("\t\t\t             00")
	time.sleep(0.7)
	print("\t\t\t            0000")
	time.sleep(0.7)
	print("\t\t\t           000000")
	time.sleep(0.7)
	print("\t\t\t          00000000")
	time.sleep(0.7)
	print("\t\t\t         0000000000")
	time.sleep(0.7)
	print("\t\t\t        000000000000")
	time.sleep(0.7)
	print("\t\t\t       00000000000000")
	time.sleep(0.7)

	return username		#for saving purposes
	
def instructions():
	banner()
	
	print()
	print("\t\t\t  * * * * * *  * * * * * *")
	print("	HANGMAN is a guessing game. The word to guess is represented")
	print("	  by a row of dashes, representing each letter of the word.")
	print("	                     Zo eazy homie. Eazy.")
	print()
	print("	But I doubt with that ability of yours that ya'll gain scores.")
	print("	   Huhuhu. Cry now coz you ain't got time later alligator.")
	print()
	print("	But because I'm pretty humble, nice and cute, Imma tell you the")
	print("	                 mechanics. Bazic. It's bazic.")
	print("	For each round, there are 10 spectacular, awesome, jaw-dropping")
	print("	words that you need to G U E S S. Yes. That's right. Just guess,")
	print("	   unless you have zuperpowerz. That'd be a really eazy shit.")	
	print()
	print("	               There are 3 levels of difficulty:")
	print("	                 ZUPER EAZY, YOU WON'T ZWEAT")
	print("	                         NOT ZO EAZY")
	print("	                          DIFFICULT")
	print()
	print("	                   And also 5 categories:")
	print("	                           Animals")
	print("	                           School")
	print("	                     Household Cleaning")
	print("	                           Fruits")
	print("	                           Colors")
	print()
	print("	Scoring and trials are pretty simple too. They are all based on")
	print("	                    the level of difficulty.")
	print()
	print("	ZUPER EAZY, YOU WON'T ZWEAT	8 tries		20 each letter")
	print("	NOT ZO EAZY                	15 tries	50 each letter")
	print("	DIFFICULT                  	15 tries	70 each letter")
	print()
	print("	Be ready to waste some time of your life playing this game. >;)")
	time.sleep(45)
	print()
	print("	  You are trolled. You've just wasted 60 seconds of your life")
	print("	        reading these instructions! You mad, huh? >;)")
	time.sleep(2.5)

def levels():
	banner()
	print("\t\t* * * * * * * * * * *   * * * * * * * * * * *")
	print("\t\t*                                           *")
	print("\t\t* [1] ZUPER EAZY, YOU WON'T ZWEAT           *")
	print("\t\t* [2] NOT ZO EAZY                           *")
	print("\t\t* [3] DIFFICULT                             *")  
	print("\t\t*                                           *")
	print("\t\t* * * * * * * * * * *   * * * * * * * * * * *")

def categories():
	banner()
	print("\t\t\t* * * * * * *   * * * * * *")
	print("\t\t\t*                         *")
	print("\t\t\t* [1] ANIMALS             *")
	print("\t\t\t* [2] SCHOOL              *")
	print("\t\t\t* [3] HOUSEHOLD CLEANING  *")
	print("\t\t\t* [4] FRUITS              *")
	print("\t\t\t* [5] COLORS              *")
	print("\t\t\t*                         *")	
	print("\t\t\t* * * * * * *   * * * * * *")
	
def hangman(l, inc):	#stick figures vary for level 1 and levels 2&3
	#l is the chosen level of the user
	#inc stands for incorrect everytime the player guesses wrongly; inc is equal to the total turns
	if l == 1:			#this is the set of stick figures for zuper eazy level; upto 8 incorrects
		if inc == 0:
			print()
			print(" _________ ")
			print(" |        |")
			print(" |         ")
			print(" |         ")
			print(" |         ")
			print(" |         ")
			print("/_\        ")
		elif inc == 1:
			print()
			print(" _________ ")
			print(" |        |")
			print(" |        |")
			print(" |         ")
			print(" |         ")
			print(" |         ")
			print("/_\        ")
		elif inc == 2:
			print()
			print(" _________ ")
			print(" |        |")
			print(" |        |")
			print(" |        O")
			print(" |         ")
			print(" |         ")
			print("/_\        ")
		elif inc == 3:
			print()
			print(" _________ ")
			print(" |        |")
			print(" |        |")
			print(" |        O")
			print(" |        |")
			print(" |         ")
			print("/_\        ")
		elif inc == 4:
			print()
			print(" _________ ")
			print(" |        |")
			print(" |        |")
			print(" |        O")
			print(" |       /|")
			print(" |         ")
			print("/_\        ")
		elif inc == 5:
			print()
			print(" _________ ")
			print(" |        |")
			print(" |        |")
			print(" |        O")
			print(" |       /|\ ")
			print(" |         ")
			print("/_\        ")
		elif inc == 6:
			print()
			print(" _________ ")
			print(" |        |")
			print(" |        |")
			print(" |        O")
			print(" |       /|\ ")
			print(" |        |")
			print("/_\        ")
		elif inc == 7:
			print()
			print(" _________ ")
			print(" |        |")
			print(" |        |")
			print(" |        O")
			print(" |       /|\ ")
			print(" |        |")
			print("/_\       / ")
		elif inc == 8:
			print()
			print(" _________ ")
			print(" |        |")
			print(" |        |")
			print(" |        O")
			print(" |       /|\ ")
			print(" |        | ")
			print("/_\       /\ ")		
			
	#these are for the not zo eazy and the difficult levels; upto 15 incorrects		
	elif l == 2 or l == 3:
		if inc == 0:
			print()
			print(" _________ ")
			print(" |        |")
			print(" |         ")
			print(" |         ")
			print(" |         ")
			print(" |         ")
			print("/_\        ")
		elif inc == 1 or inc == 2 or inc == 3:
			print()
			print(" _________ ")
			print(" |        |")
			print(" |        |")
			print(" |         ")
			print(" |         ")
			print(" |         ")
			print("/_\        ")
		elif inc == 4 or inc == 5 or 6 or inc == 7:
			print()
			print(" _________ ")
			print(" |        |")
			print(" |        |")
			print(" |        O")
			print(" |         ")
			print(" |         ")
			print("/_\        ")
		elif inc == 8:
			print()
			print(" _________ ")
			print(" |        |")
			print(" |        |")
			print(" |        O")
			print(" |        |")
			print(" |         ")
			print("/_\        ")
		elif inc == 9:
			print()
			print(" _________ ")
			print(" |        |")
			print(" |        |")
			print(" |        O")
			print(" |       /|")
			print(" |         ")
			print("/_\        ")
		elif inc == 10:
			print()
			print(" _________ ")
			print(" |        |")
			print(" |        |")
			print(" |        O")
			print(" |       /|\ ")
			print(" |         ")
			print("/_\        ")
		elif inc == 11 or inc == 12 or inc == 13:
			print()
			print(" _________ ")
			print(" |        |")
			print(" |        |")
			print(" |        O")
			print(" |       /|\ ")
			print(" |        |")
			print("/_\        ")
		elif inc == 14:
			print()
			print(" _________ ")
			print(" |        |")
			print(" |        |")
			print(" |        O")
			print(" |       /|\ ")
			print(" |        |")
			print("/_\       / ")
		elif inc == 15:
			print()
			print(" _________ ")
			print(" |        |")
			print(" |        |")
			print(" |        O")
			print(" |       /|\ ")
			print(" |        | ")
			print("/_\       /\ ")	
		
def play(l, c, wList):	#main game play; l = chosen level, c = chosen category wList = wordList)

	#global --> declares a global var name in the scope of the function
	global score			#quoted score from the outside of the function
	global playerName		#quoted playerName from the outside of the function
	
	readHandle = open("easy.txt", "r")	#all the words are saved in easy.txt

	# i designed and arranged every line of the txt to be of the same category and level
	for line in readHandle:					
		catlist = line[:-1].split(" ")	#splitting the words in one line then adds them into a 															new list
		wList.append(catlist)				#because there are 15 lines in easy.txt, there were 															also 15 new lists; all those will be added to 																another list; list within a list
	#wList will consist of 15 lists, 5 lists under each difficulty
		
	if l == 1:		# if user chooses zuper eazy, first five lists of the five categories will 							be the next choices
		banner()		#clear screen, header
		
		print("\t\t\t\tPlayer:", playerName)			
		print("\t\t\t ZUPER EAZY, YOU WON'T ZWEAT")
		
		if c == 1:	#if user chooses animals category
			word = random.choice(wList[0])	# random word will be generated under the zuper eazy 																level, animals category
			print("\t\t\t\t    Animals")
			
		elif c == 2:	#if user chooses school category
			word = random.choice(wList[1])	# random word will be generated under the zuper eazy 																level, school category
			print("\t\t\t\t    School")
			
		elif c == 3: #if user chooses household cleaning category 
			word = random.choice(wList[2]) 	# random word will be generated under the zuper eazy 																level, household cleaning category
			print("\t\t\t      Household Cleaning")
			
		elif c == 4: #if user chooses fruits category
			word = random.choice(wList[3])	# random word will be generated under the zuper eazy 																level, fruits category
			print("\t\t\t\t    Fruits")
			
		elif c == set5: #if user chooses colors category
			word = random.choice(wList[4])	# random word will be generated under the zuper eazy 																level, colors category
			print("\t\t\t\t    Colors")

	elif l == 2:	#if user chooses not zo eazy, the second five lists will be the next choices
		banner()		#clears screen again, shows header
		
		print("\t\t\t\tPlayer:", playerName)
		print("\t\t\t\t NOT ZO EAZY")
		
		if c == 1:	#if user chooses animals category
			word = random.choice(wList[5])	# random word will be generated under the not zo 																	eazy level, animals category
			print("\t\t\t\t    Animals")
			
		elif c == 2: #if user chooses school category
			word = random.choice(wList[6])	# random word will be generated under the not zo 																	eazy level, school category
			print("\t\t\t\t    School")
			
		elif c == 3:	#if user chooses household cleaning category
			word = random.choice(wList[7])	# random word will be generated under the not zo 																	eazy level, household cleaning category
			print("\t\t\t      Household Cleaning")
			
		elif c == 4:	#if user chooses fruits category
			word = random.choice(wList[8])	# random word will be generated under the not zo 																	eazy level, fruits category
			print("\t\t\t\t    Fruits")
			
		elif c == 5:	#if user chooses colors category
			word = random.choice(wList[9])	# random word will be generated under the not zo 																	eazy level, colors category
			print("\t\t\t\t    Colors")
			
	elif l == 3:	#if user chooses difficult level
		banner()
		
		print("\t\t\t\tPlayer:", playerName)
		print("\t\t\t\t   DIFFICULT")
		
		if c == 1:	#if user chooses animals category
			word = random.choice(wList[10])	# random word will be generated under the difficult 																	 level, animals category
			print("\t\t\t\t    Animals")
			
		elif c == 2:	#if user chooses school category
			word = random.choice(wList[11])	# random word will be generated under the difficult 																	 level, school category
			print("\t\t\t\t    School")
			
		elif c == 3:	#if user chooses household cleaning category
			word = random.choice(wList[12])	# random word will be generated under the difficult 																	 level, household cleaning category
			print("\t\t\t      Household Cleaning")
			
		elif c == 4:	#if user chooses fruits category
			word = random.choice(wList[13])	# random word will be generated under the difficult 																	 level, fruits category
			print("\t\t\t\t    Fruits")
			
		elif c == 5:	#if user chooses colors category
			word = random.choice(wList[14])	# random word will be generated under the difficult 																	 level, colors category
			print("\t\t\t\t    Colors")
	
	wLetter = []		#set the list for the letters of the word
	correct = 0
	turns = 0			#varies according to the difficulty of the level
	incorrect = 0		#varies according to the difficulty of the level
	guessed = []		#set the list for the used words in guessing
	notDead = True
	
	for letter in word:			#each letters in the random word will be added to wLetter list
		wLetter.append(letter)
		print("_", end=" ")		#prints blanks instead since the gae is about guessing the word
	print()
	
	hide = ['_'] * len(wLetter)	#set the list for hidden letters with the same length as the 												list with the characters of the random word
											# the elements of this set are the ones to be replaced with 											the correctly guessed letter so that i can display it
	
	while notDead:
		hangman(l, incorrect)	#function call to the stick figures container

		guess = input("Guess a letter: ")
		if guess.isalpha() == False or len(guess) != 1:		#checks the input of the user
			print("Please enter ONE LETTER only.")
			continue
		elif guess in guessed:	#checks the input of the user
			print("You've already used this word.")
			continue
		else:
			guessed.append(guess)	#if the input was valid and was not used in previous guesses, 													the letter will be added to 'guessed' list
			if guess in wLetter:		#if the letter user guessed is in the random word character 												list
				for index in range(0,len(word)):	#numbers 0 upto the length of the random word
					if guess == wLetter[index]:	#if guess matches a letter in wLetter in 																whichever index,
						guess = guess.upper()		# capitalizes guess
						hide[index] = guess			#replaces the blank with the same index as 																wLetter with the correctly guessed letter
															#what to guess = me  wLetter = ['m', 'e'] 															hide = ['_', '_'] myguess = m; m is in wLetter so 																m will replace a blank in hide with the same 																place as wLetter ['m','_']	
						for a in hide:
							print(a, end=" ")			#print the updated
						correct += 1
						
						#here goes the scoring
						if l == 1:				
							score += 20
						elif l == 2:
							score += 50
						elif l == 3:
							score += 70
						print("\nScore: ",score)
						
						if correct == len(word):
							notDead = False	#if wLetter == hide already, the break the loop
							break

			elif guess not in wLetter:
				for b in hide:				#if not, print what is so far the status
					print(b, end=" ")
				incorrect += 1

				if l == 1:			
					if incorrect == 8:				#as said before, turns are according to the level of 												difficulty
						notDead = False
						break
				elif l == 2 or l == 3:
					if incorrect == 15:
						notDead = False
						break
	
	if notDead == False:
		if correct == len(word):			
			for setno in range(len(wList)):	#the word guessed already will be removed from the 															category list it belongs
				if word in wList[setno]:
					wList[setno].remove(word)
					break
			banner()
			print("\t\t\t *  *  *  *  *  *  *  *")
			print("\n\t\t\t         Chamba bes.")
			print()
			print("\t\t\t           00000 ")
			print("\t\t\t          0 o o 0")
			print("\t\t\t          0 \_/ 0")
			print("\t\t\t           00000")
			print()
			print("\n\t\t\t\t", playerName, score)	#displays the player's name and his score
			time.sleep(1.5)
			
		elif hide != wLetter:
			banner()
			print("\t\t\t *  *  *  *  *  *  *  *")
			print("\n\t\t\t  Correct answer:", word)
			print("\n\t\t\t  Dead na bes. Tama na.")
			print()
			print("\t\t\t           00000 ")
			print("\t\t\t          0 x x 0")
			print("\t\t\t          0  /\ 0")
			print("\t\t\t           00000")
			print()
			print("\n\t\t\t\t\t",  playerName, score)	#displays the player's name and his score
			time.sleep(2)
	print()
	
	afterplay()	#function call for another menu
	readHandle.close()
	return score
	
def afterplay():
	banner()
	print("\t\t\t  * * * * * * *   * * * * * *")
	print("\t\t\t  *                         *")
	print("\t\t\t  *     [1] Next word       *")
	print("\t\t\t  *     [2] Levels          *")
	print("\t\t\t  *     [3] Categories      *")
	print("\t\t\t  *     [4] Instructions    *")
	print("\t\t\t  *     [5] Save and Go     *")
	print("\t\t\t  *                         *")
	print("\t\t\t  * * * * * * *   * * * * * *")
		
def saveGame(dic):
	#local = dic, global = tempscoreBoard
	appendHandle = open("lead.txt", "a")
	list1 = []	#list for the name and score of the player
	for i,j in dic.items():	#for the key and the value of tempscoreBoard
		j = str(j)				# j = score  ---> string
		list1.append(i)		# added the name and the score the list
		list1.append(j)
		
	for k in list1:			# the elements of the list were added to the lead.txt document
		appendHandle.write(k+" ")
	appendHandle.write("\n")
	
	appendHandle.close()

'''
def leaderboard():
	readHandle = open("lead.txt", "r")
	newdic = {}
	for line in readHandle:
		profile = line[:-1].split(" ")
		name = profile[0]
		profile[1] = int(profile[1])
		score = profile[1]
		newdic[name] = score
	readHandle.close()	

	list1 = sorted(newdic.values())
	highest = list1[-1]
	reverse = list1[::-1]
	print(reverse)
	print(highest)	
	
	for i,j in newdic.items():
		if i == highest:
			print(i,j)
	time.sleep(1)
'''
	
#------------------------------------------------------------------------------------EXECUTION

menu()		#function call --> dislays menu
selectMenu = int(input("\t\t\t   Please choose one: "))

tempscoreBoard= {}	#dictionary for saving the name and the score
wordList = []			#global for a while ago's wList, list of category word lists
score = 0				

while selectMenu != 0:
	if selectMenu == 1:
		playerName = intro()		# return username --> user = playerName

		levels()						#function call for the levels menu
		chooselevel = int(input("\t\t\t   Please choose one: "))	
		
		categories()				#function call for the category menu
		choosecat = int(input("\t\t\tPlease choose one category: "))
		
		score = score + play(chooselevel, choosecat, wordList)	#function call for the game to 											run, the function returns the score and is added here for update

		afterplayOptions = int(input("\t\t\t   Please choose one: "))
		while afterplayOptions != 0:
			if afterplayOptions == 1:
				score = score + play(chooselevel, choosecat, wordList) #function call for the game 										to run, the function returns the score and is added here for update
			
			elif afterplayOptions == 2:
				levels()		#levels menu still under the same category
				chooselevel = int(input("\t\t\t   Please choose one: "))
				score = score + play(chooselevel, choosecat, wordList) #function call for the game 									to run, the function returns the score and is added here for update
					
			elif afterplayOptions == 3:
				categories()	#categories menu still under the same level
				choosecat = int(input("\t\t\tPlease choose one category: "))
				score = score + play(chooselevel, choosecat, wordList)	#function call for the 								game to run, the function returns the score and is added here for update

			elif afterplayOptions == 4:
				instructions()
				afterplay()	#the after game menu
				afterplayOptions = int(input("\t\t\t   Please choose one: "))
				continue
				
			elif afterplayOptions == 5:
				tempscoreBoard[playerName] = score	#player name is added in the dictionary with 																the score as the value
				saveGame(tempscoreBoard)	#function call to save the game before exiting; autosave
				exit()
			afterplayOptions = int(input("\t\t\t   Please choose one: "))	
		
	elif selectMenu == 2:
		instructions()
		
	elif selectMenu == 0:
		saveGame()
		exit()
		
	menu()
	selectMenu = int(input("\t\t\t   Please choose one: "))
