from bs4 import BeautifulSoup as soup
from log import log as log
import time
import datetime
import random
import sqlite3
import threading
from bs4 import BeautifulSoup as soup
from threading import Thread
from discord_webhook import DiscordEmbed, DiscordWebhook
from colorama import init
from colorama import Fore, Back, Style
import json, re, sys
from bs4 import BeautifulSoup as bs
import arrow
from hashlib import md5
from base64 import b64decode
from base64 import b64encode
import secrets
import requests
import urllib.parse

init(autoreset=True)
screen_lock = threading.Lock()

def gettime():
    now = str(datetime.datetime.now())
    now = now.split(' ')[1]
    now = ' [' + str(now) + '] '
    return now

uas = ["Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
               "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
               "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
               "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
               "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36",
               "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
               "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
               "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36",
               "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
               "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36",
               "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
               "Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
               "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
               "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
               "Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
               "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36",
               "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36",
               "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36",
               "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36",
               "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36",
               "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36",
               "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/4E423F",
               "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36 Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10",
               "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36",
               "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36",
               "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36",
               "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36",
               "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36",
               "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36",
               "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36",
               "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36",
               "Mozilla/5.0 (X11; CrOS i686 4319.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36",
               "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36",
               "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36",
               "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36",
               "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36",
               "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1500.55 Safari/537.36",
               "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
               "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
               "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
               "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
               "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
               "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
               "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36",
               "Mozilla/5.0 (X11; NetBSD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36",
               "Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36",
               "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17",
               "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17",
               "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15",
               "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/24.0.1292.0 Safari/537.14"]

u2 = random.choice(uas)

proxies = []

now = datetime.datetime.now()

day = now.strftime("%A")


def takefirstelem(elem):
    return elem[0]

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

try:
    proxies = open("proxies.txt").read().splitlines()
    screen_lock.acquire()
    log('s', gettime() + Fore.GREEN + " [Succesfully loaded " + str(len(proxies)) + " proxies]")  
    screen_lock.release()      
except Exception as e:
    print(e)
    log('e', gettime() + Fore.RED + " [Could not load proxies]")

def getRandomProxy():
  if (len(proxies) != 0):
    proxyDict = {}
    proxy = random.choice(proxies)
    proxySplit = proxy.split(":")
    if (len(proxySplit) != 4):
      proxyDict = {
        "http": "http://" + proxySplit[0] + ":" + proxySplit[1] + "/",
        "https": "https://" + proxySplit[0] + ":" + proxySplit[1] + "/"
      }
    else:
      proxyDict = {
        "http": "http://" + proxySplit[2] + ":" + proxySplit[3] + "@" + proxySplit[0] + ":" + proxySplit[1] + "/",
        "https": "https://" + proxySplit[2] + ":" + proxySplit[3] + "@" + proxySplit[0] + ":" + proxySplit[1] + "/"
      }          
    return proxyDict
  else:
    proxyDict = {}
    proxyDict = {
      "http": "http://",
      "https": "https://"
    }             
    return proxyDict


class Product():
    def __init__(self, title, link, stock, keyword):
        '''
        (str, str, bool, str) -> None
        Creates an instance of the Product class.
        '''
    
        # Setup product attributes
        self.title = title
        self.stock = stock
        self.link = link
        self.keyword = keyword


def read_from_txt(path):
    '''
    (None) -> list of str
    Loads up all sites from the sitelist.txt file in the root directory.
    Returns the sites as a list
    '''

    # Initialize variables
    raw_lines = []
    lines = []

    # Load data from the txt file
    try:
        f = open(path, "r")
        raw_lines = f.readlines()
        f.close()

    # Raise an error if the file couldn't be found
    except:
        log('e', "Couldn't locate <" + path + ">.")
        raise FileNotFound()

    if(len(raw_lines) == 0):
        raise NoDataLoaded()

    # Parse the data
    for line in raw_lines:
        lines.append(line.strip("\n"))

    # Return the data
    return lines


def send_embed(title, pid, sizes, color, price, producturl, image):
    
    url = 'WebhookURL' #Your Discord Webhook URL

    webhook = DiscordWebhook(url=url, username="Sarenza", avatar_url='https://blackfriday-en-france.com/wp-content/uploads/2022/10/sarenza_logo_Black_friday-1200x1200.jpg')
    embed = DiscordEmbed(title=title,url=producturl, description="Restock" ,color=0)
    embed.set_author(name="Sarenza", icon_url="https://blackfriday-en-france.com/wp-content/uploads/2022/10/sarenza_logo_Black_friday-1200x1200.jpg")
    embed.add_embed_field(name='SKU', value=str(pid), inline=True)
    embed.add_embed_field(name='Color', value=color, inline=True)
    embed.add_embed_field(name='Price', value=str(price)+'€', inline=True)
    embed.add_embed_field(name='Sizes', value=sizes, inline=True)
    embed.set_thumbnail(url=image)
    embed.set_footer(text=f'Romain • Sarenza • {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")}', icon_url="https://cdn.discordapp.com/attachments/808528452000808990/1120048908953989290/rascal.jpeg")
    webhook.add_embed(embed)
    webhook.execute()

def monitor(link, keywords):

    s = requests.Session()

    pid = link

    produrl = f"http://api.sarenza.com/store/product/get?id={pid}&domain=1"

    headers1 = {
    'Host': 'api.sarenza.com',
    'ApiKey': 'fQNvzW5Ij4aBEjqARV33RvjvK9c4IBjv',
    'Accept': '*/*',
    'AnonymousSession': 'oLxIB1Brik6DCl6FtNrMtBPv6r8xibPxmw4ufvoWCFoUHZvwN9vDKqoKuWz6QUeuhR287mdAwdxzVgkYAu0IMQ2',
    'User-Agent': 'Sarenza/4.15.0 (iPhone; iOS 16.0; Scale/3.00)',
    'Accept-Language': 'fr-FR;q=1',
    'AppVersion': '4.15.0'
}

    try:
        r = requests.get(produrl, headers=headers1)
        if "ModelName" in r.text:
        	screen_lock.acquire()
        	log('i', gettime() + Fore.YELLOW +  " [Monitoring Sarenza...] ["+str(pid)+"]")
        	screen_lock.release()
        else:
        	screen_lock.acquire()
        	log('e', gettime() + Fore.RED +  " [Failed Monitoring Sarenza...] ["+str(pid)+"]")
        	screen_lock.release()
    except:
    	screen_lock.acquire()
    	log('e', gettime() + Fore.RED + " [Connection to URL <" + link + "> failed - Retrying...]")
    	screen_lock.release()
    	try:
    		r = requests.get(link, timeout=8, verify=False)
    	except:
    		screen_lock.acquire()
    		log('e', gettime() + Fore.RED + " [Connection to URL <" + link + "> failed]")
    		screen_lock.release()
    		return

    try:
        file = open(link+'.txt', 'r')
        stockold = file.read()
    except:
        file = open(link+'.txt', 'w')
        stockold = file.read()

    true = True
    false = False

    found = False

    try:

      res = r.text

      if 'ModelName' in res:
        try:
          rrr = json.loads(r.text)
          
          producturl = rrr["UrlOfProductViewOnWebSite"]
          
          brand = rrr["BrandModel"]["Name"]
          model = rrr["BrandModel"]["ProductList"][0]["ProductColorList"][0]["ModelName"]

          title = brand + ' ' + model

          color = rrr["BrandModel"]["ProductList"][0]["ProductColorList"][0]["Color"]["SupplierColorName"]
          price = rrr["BrandModel"]["ProductList"][0]["ProductColorList"][0]["Price"]["SellingPrice"]
          image = rrr["BrandModel"]["ProductList"][0]["ProductColorList"][0]["ProductPictureList"][0]["Raw"]

          stock1 = rrr["BrandModel"]["ProductList"][0]["ProductColorList"][0]["VariantList"]

          sizesall = []
          stockall = []


          for i in stock1:
            sizesall.append(str(i["SupplierSize"]))
            try:
                stockall.append(str(i["IsAvailable"]))
            except:
                stockall.append('False')

          everything = [f"{e} ({i})" for e, i in zip(sizesall, stockall)]

          finalsize = []

          for i in everything:
            if '(False)' in i:
                found = False
            else:
                finalsize.append(i)

          inventory1 = "\n".join(finalsize)

          inventory = inventory1.replace('(True)', '')

          if inventory == '':
            sizes = 'outofstock'
          else:
            sizes = inventory
          

          if sizes == stockold:
            file.close()
            found = False

          elif sizes != stockold:
            file.close()
            found = True
            log('s', gettime() + Fore.GREEN + " [Stock change detected]")
            file1 = open(link+'.txt',"w") 
            file1.write(sizes)
            file1.close()
            if sizes == "outofstock":
                aaab = ''
            else:
                send_embed(title, pid, sizes, color, price, producturl, image)
          
          else:
            found = False


        except Exception as e:
          print('Error')
          print(e)
   
         
    except Exception as e:
      screen_lock.acquire()
      log('e', gettime() + Fore.RED + " [Exception]")
      print(e)
      screen_lock.release()
      found = False


if(__name__ == "__main__"):
    # Ignore insecure messages
    requests.packages.urllib3.disable_warnings()

    # Keywords (seperated by -)
    keywords = [
        "test",
        "jordan-mid",
        "jordan-mid-gs",
        "air-jordan-1-mid",
        "air-jordan",
        "air-jordan-1",
        "air-jordan-1-mid-gs",
        "air-jordan-1-low",
        "jordan-1-low",
        "jordan-1-low-gs",
        "air-jordan-1-low-gs",
        "jordan-low-gs",
        "jordan-low",
        "nike",
        "paranoise",
        "jordan",
        "yeezy"
        "air-max",
        "dunk",
        "dunk-low",
        "casablanca",
        "newbalance"
    ]
    
    # Load sites from file
    sites = read_from_txt("pids_to_run.txt")

    # Start monitoring sites
    while(True):
        threads = []
        for site in sites:
          t = Thread(target=monitor, args=(site, keywords))
          threads.append(t)
          t.start()
          time.sleep(3) #DELAY HERE in SECONDS
