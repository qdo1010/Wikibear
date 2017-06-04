import rake
import operator
import os
import wikipedia
from google import google
from random_words import RandomWords
import random
os.system("say 'Hi, I am wikibear'")
os.system("say 'What is your name'")
name = raw_input("What is your name: ")
#summ = str(wikipedia.summary("'" + name+ "'", sentences = 1))
os.system("say " + '"'+ "Hi "+  name+'"')
os.system("say 'You can ask me anything. I am'")
os.system('say -v "Good News" "Wikibear"')
question = raw_input("Ask me anything: ")
rake_object = rake.Rake("SmartStoplist.txt", 5,3,1)
#keywords = rake_object.run(question)
#query = ""
#for key in keywords:
#	 query = query + key[0]
#	 query = query + " "
#print query
#priint(wikipedia.search(query))
while question != "Bye":
	num_page = 1
	search_results = google.search(question, num_page)
	print(search_results)
	if search_results is not None:
		os.system("say " + '"' + search_results[0].description.encode('utf-8') + '"')
		keywords = rake_object.run(search_results[0].description)
		query = ""
		search_results = None
	#print keywords
		for key in keywords:
			#print key[0]
			ans = wikipedia.search(key[0])
	 		query = random.choice(ans)
			ans.remove(query)
		#print (wikipedia.summary("'" + query + "'", sentences = 1))
			try:
				os.system("say " + '"' + wikipedia.summary("'" + query + "'", sentences = 1).encode('utf-8') + '"')
#			if len(ans) !=0:
#				q = random.choice(ans)
#				try:
#					os.system("say " + '"' + wikipedia.summary("'" + q + "'", sentences = 1).encode('utf-8') + '"')
#				except UnicodeEncodeError:
#					pass
			except UnicodeEncodeError:
				pass			
#print (wikipedia.summary("'" + q + "'", sentences = 1))
 
	else:
		os.system("say -r 'I don't know, but I know this'")
		rw = RandomWords()
		num_page = 1
		search_results = google.search(rw, num_page)
		os.system("say " + '"' + search_results[0].description + '"')
#	summ = str(wikipedia.summary("'" + + "'", sentences = 1))
		os.system('say -v "Good News" "Wikibear"')
	os.system("say 'Ask me something else. I am'")
	os.system('say -v "Albert" "Wikibear"')
	question = raw_input("Ask me anything: ")

os.system("say 'Goodbye!'")

