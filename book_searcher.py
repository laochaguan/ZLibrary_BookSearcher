from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

#Enter your zlibrary email and password
email = ''
password = ''
url = 'https://singlelogin.me/'


chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

def get_webpage(url):

    driver.get(url)

    time.sleep(2)

def get_login_fields():
    email_field = driver.find_element('name','email')

    password_field = driver.find_element('name','password')

    return email_field, password_field

def send_login_keys(email_field,password_field,email,password):
    email_field.send_keys(email)
    password_field.send_keys(password)

    password_field.send_keys(Keys.RETURN)

def main_login(url,email,password):
    get_webpage(url)
    email_field,password_field = get_login_fields()
    send_login_keys(email_field,password_field,email,password)
    time.sleep(3)

def get_search_field():

    search_field = driver.find_elements('name','q')
    return search_field

def send_search_keys(search_field,search_input):
    search_field[1].clear()
    search_field[1].send_keys(search_input)
    search_field[1].send_keys(Keys.RETURN)

def get_books():
    book_titles = driver.find_elements(By.XPATH,'//h3[@itemprop="name"]/a')
    count = 0
    books = {}
    links = {}
    for title in book_titles[:10]:
        count += 1
        print(f"{count}-) {title.text}")
        books[count] = title.text
        links[count] = title.get_attribute('href')

    return books,links

def main_search():
    search_input = input("Enter a book name: ")
    while True:
        search_field = get_search_field()
        send_search_keys(search_field,search_input)
        time.sleep(2)
        books,links = get_books()
        while True:
            index = input("(s: search another book, q: quit)\nEnter a book index: ")
            if index.isdigit():
                index = int(index)
                print("----------------------------------------------")
                print(books.get(index,"Enter a valid index"))
                print(links.get(index,"-"))
                print("----------------------------------------------")
            elif index == 'q':
                return
            elif index == 's':
                search_input = input("Enter a book name: ")
                break


main_login(url,email,password)
main_search()
driver.close()