#! /usr/bin/
from selenium import webdriver
import time, os
from selenium.webdriver.common.keys import Keys

PATH = os.path.dirname(os.path.realpath(__file__))
DRIVER_PATH = PATH + "/chromedriver"
booklist = open('bookList.txt','r')

def welcomePrompt():
	selection = input("Welcome to DiscoverBook, the stop for finding your next book to read.\n How can we help?\n [1]. Find my next book.\n [2]. Update my list.\n [3]. Exit\n")
	return selection

def responseHandler(selection):
	print("Response handler called.")
	if(selection == "1"):
		print("Responded with 1.")
		myBookList = createBooklist(booklist)
		bookSearch(myBookList)
	elif(selection == "2"):
		addBook(booklist)
	else:
		quit


def createBooklist(file1):
	BList = []
	
	for line in file1:
		#print(line)
		BList.append(line.strip())
	return BList

def bookSearch(myBookList):

	driver = webdriver.Chrome(DRIVER_PATH)	
	driver.get("https://www.amazon.com")
	print(driver.title)
	
	for book in myBookList:
		element = driver.find_element_by_id("twotabsearchtextbox")
		element.clear()
		element.send_keys(book)
		element.send_keys(Keys.RETURN)
		time.sleep(3)

	driver.quit()

def addBook(file):
	newTitle = input("What is the title of the new book you would like to add?\n")

	confirmation = input("You entered: " + newTitle + "\n Is this correct?\n")

	if(confirmation == "y" or "Y" or "Yes" or "yes"):
		print("Responsed yes.")
		file1 = open("booklist.txt", "a")
		file1.write(newTitle)
	else:
		print("Cancelled.")
		welcomePrompt()
	
	print("Your list has been updated.")

	welcomePrompt()

def driver():
	response = welcomePrompt()
	responseHandler(response)

def main():
	driver()
	

if __name__ == '__main__':
	main()