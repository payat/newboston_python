import random
# in mac
# import urllib
# in windows
import urllib.request
import requests
from bs4 import BeautifulSoup
import operator
# from urllib import request

# word frequency counter tutorial
def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "html.parser")
    for post_text in soup.find_all('a', {'rel': 'bookmark', 'itemprop': 'url'}):
        content = post_text.string
        if content is not None:
            words = content.lower().split()
            for each_word in words:
                word_list.append(each_word)
    clean_up_list(word_list)

def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = "!@#$%^&*()_+{}:\"<>?,./;'[]-='~‘’–"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i],"")
        if len(word) > 0:
            clean_word_list.append(word)
    create_dictionary(clean_word_list)

def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for key, value in sorted(word_count.items(),key=operator.itemgetter(1)):
        print(key, value)

# webcrawler tutorial
def otakit_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = r'https://otakit.my/page/' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.find_all('a', {'rel': 'bookmark', 'itemprop': 'url'}):
            href = link.get('href')
            print(href)
            #print(link.string)
            get_news_item_data(href)
        page += 1

def get_news_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for title in soup.find_all('title'):
        print(title.string)
    for link in soup.find_all('a'):
        href = link.get('href')
        print(href)


# download file from web tutorial
def download_stock_data(csv_url):
    print(csv_url)
    response = urllib.request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'google.csv'
    fx = open(dest_url, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close


# download web image tutorial
def download_web_image(url):
    name = random.randrange(1, 1000)
    full_filename = str(name) + ".png"
    # in mac
    # urllib.urlretrieve(url, full_filename)
    # in windows
    urllib.request.urlretrieve(url, full_filename)

# read & write files tutorial
def write_to_file(filename):
    fw = open(filename, 'w')
    fw.write('i ate too much durian. my breath stinks!!\n')
    fw.write('will need to drink a lot of water')
    fw.close()

def read_file(filename):
    fr = open(filename, 'r')
    text = fr.read()
    print(text)
    fr.close()



# functions tutorial
def bitcoin_to_ringgit(btc):
    amount = btc * 547 * 4
    print(amount)

# return values tutorial
def allowed_dating_age(my_age):
    girls_age = my_age/2 + 7
    return girls_age

# default values for arguments tutorial
def get_gender(sex="unknown"):
    if sex is "m":
        sex = "Male"
    elif sex is "f":
        sex = "Female"
    print(sex)


# variable scope tutorial
a = 123
def scope_a():
    a = 444
    print(a)

def scope_b():
    print(a)

# keyword arguments tutorial
def dumb_sentence(name="payat", action="ate", item="meatballs"):
    print(name, action, item)

# flexible number of arguments tutorial
def add_numbers(*args):
    total=0
    for a in args:
        total += a
    print(total)

# unpacking arguments tutorial
def health_calculator(age, apples_ate, cigs_smoked):
    answer = (100-age) + (apples_ate * 3.5) - (cigs_smoked * 4)
    print(answer)

# unpack list of tuples tutorial
def drop_first_last(grades):
    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print(avg)
