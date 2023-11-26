# pip install requests
# pip install beautifulsoup4
# pip install google

import requests
from bs4 import BeautifulSoup
from googlesearch import search

def search_wiki(last_word):
    url = "https://en.wikipedia.org/wiki/" + last_word
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    text = ""
    for i in range(len(soup.findAll('p'))):
        one_a_tag = soup.findAll('p')[i]
        text += one_a_tag.text
    return text

def google_search(query):
    search_results = list(search(query, num=1, stop=1))
    if search_results:
        url = search_results[0]
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        text = ""
        for paragraph in soup.find_all('p'):
            text += paragraph.get_text() + "\n"
        return text
    else:
        return "No results found."

print(":")
print(".W")
print(".G")

option = input(": ")

if option == "1":
    user_input = input(": ")
    print(search_wiki(user_input))
elif option == "2":
    user_query = input(": ")
    search_result_text = google_search(user_query)

    if search_result_text:
        print("\n")
        print(search_result_text)
    else:
        print("No results found.")
else:
    print("Invalid option. Please choose a valid option (1, 2).")
