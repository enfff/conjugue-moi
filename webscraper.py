import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Firefox, FirefoxOptions

URL = "https://francais.lingolia.com/en/grammar/tenses/irregular-verbs/"

irregular_verbs=list()
regular_verbs=list()

response = requests
options = FirefoxOptions()
options.add_argument('-headless')
driver = Firefox(options=options)
driver.get(URL)

soup = BeautifulSoup(driver.page_source, 'lxml')
rows = soup.find_all('b', class_=None)

for row in rows:
    if row:
        # Remove the content of the <span> tag, if it exists
        for span in row.find_all('span'):
            span.decompose()

        # Extract the text from the first <b> tag
        text = row.text.strip()
        if text:
            irregular_verbs.append(text)


print(irregular_verbs)