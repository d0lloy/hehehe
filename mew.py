import requests
from bs4 import BeautifulSoup
from googlesearch import search
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

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

def summarize_text(text, sentences=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences)
    return ' '.join([str(sentence) for sentence in summary])

# User option
print("Choose an option:")
print("1. WikY")
print("2. SuMy")
print("3. FulY")

option = input(": ")

if option == "1":
    user_input = input("Query: ")
    print(search_wiki(user_input))
elif option == "2":
    user_query = input("Query: ")
    search_result_text = google_search(user_query)

    if search_result_text:
        summarized_text = summarize_text(search_result_text)
        print("\n")
        print(summarized_text)
    else:
        print("No results found.")
elif option == "3":
    user_query = input("Query: ")
    search_result_text = google_search(user_query)

    if search_result_text:
        print("\n")
        print(search_result_text)
    else:
        print("No results found.")
else:
    print("Invalid option. Please choose a valid option (1, 2, or 3).")
