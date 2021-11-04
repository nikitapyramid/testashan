import pickle
from urllib.parse import urlparse
from urlextract import URLExtract
import requests
import time
import logging
logging.basicConfig(filename="main.log", level=logging.INFO)


start_time = time.time()
logging.info("Запуск времени программы")


AllUrls = [] #Массив всех проверенных Url
logging.info("Создание AllUrls Массив всех проверенных Url")
AllUrlsshorten = [] #Массив коротких  Url (shorten)(unshorten)
logging.info("Создание AllUrlsshorten Массив всех проверенных Url коротких и полных")
f = open('messages_to_parse (1).dat', 'rb')

L2 = pickle.load(f)
logging.info("Загрузка файла messages_to_parse (1).dat")

extractor = URLExtract()
urls = extractor.find_urls(str(L2))
logging.info("Поиск Url в файле messages_to_parse (1).dat")



for url in urls:
    try:
        x = requests.head(url)
        AllUrls.append([url, x.headers])
        logging.info("Добавляем в массив AllUrls")
        originalurl = urlparse(url).hostname
        AllUrlsshorten.append([originalurl, url])
        logging.info("Добавляем в массив AllUrlsshorten")
    except:
        logging.error(str(url)+"Url не найден")
        print("Url не найден")


for url in AllUrls:
    logging.info("Выводим один из елементов AllUrls")
    print(url)

print("\n\n\n\n\n\n\n")


for url in AllUrlsshorten:
    logging.info("Выводим один из елементов AllUrlsshorten")
    print(url)

print("\n\n\n\nЧас виконання в секундах")
print(time.time() - start_time)


f.close()