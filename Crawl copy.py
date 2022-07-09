from urllib.request import Request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.request
import re
import numpy as np
import time
import os
import random
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup

a = urlopen('https://www.naver.com/')
# a를 호출해 html을 parser
soup = BeautifulSoup(a.read(), 'html.parser')
# soup에서 div tag의 class가 corp_area인 태그를 가져온다.
b = soup.find_all("p", {'class':"desc"})
print(b)