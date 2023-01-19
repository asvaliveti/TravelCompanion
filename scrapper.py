import requests
from bs4 import BeautifulSoup
from selenium import webdriver

travellingFrom = input("Where are you departing from? ")
destination = input("What is your destination? ")
startDate = input("when do you leave? (yyyy-mm-dd): ")
endDate = input("when do you come back? (yyyy-mm-dd): ")

page = requests.get('http://www.airportcodes.org/')
soup = BeautifulSoup(page.text, 'lxml')
table = soup.find('div',attrs={"class":"i1"})
cities = table.text.split("\n")

def findCode(city):
    fullData = []
    for item in cities:
        if city in item:
            fullData.append(item.split()[len(item.split()) - 1])

    for index in range(len(fullData)):
        fullData[index] = fullData[index][1:-1]
    
    if len(fullData) > 1:
        possibleCities = fullData
        fullData = input("Specify which airport: " + str(possibleCities) + ": ")
    return fullData

startCode = findCode(travellingFrom)    
endCode = findCode(destination)