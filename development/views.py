from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import View, TemplateView
import requests
from bs4 import *
import html5lib
from django.views.decorators.csrf import csrf_exempt
from development.forms import my_form
from .models import first_url
import selenium
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options


class Home(View):
    def get(self, request):
        return render(request,'home.html')


def app(request):
    return render(request, "App_Searcher.html")



@csrf_exempt
def google_app(request):
    if request.method == "POST":
        pack = request.POST.get('first')
        print(pack)

        url = f"https://play.google.com/store/apps/details?id={pack}&hl=en_IN"
        # "https://play.google.com/store/apps/details?id=com.space.shooter.alien.battle.invaders.galaxy.war&hl=en_IN"

        r = requests.get(url)
        b = BeautifulSoup(r.content, 'html5lib')
        img = b.find('div', class_='xSyT2c').find('img').get('src')
        print(img)

        app_name = b.find('h1', class_='AHFaub').find('span').get_text()
        # print(app_name)

        developer_name = b.find(
            'span', class_='T32cc UAO9ie').find('a').get_text()
        # print(developer_name)

        description = b.find('div', class_='DWPxHb').find(
            'span').find('div').get_text()
        # print(description)

        download = b.find_all('span', class_='htlgb')[4].find(
            'div', class_='IQ1z0d').find('span', class_='htlgb').get_text()
        # print(download)

        app_rating = b.find('span', class_='AYi5wd TBRnV').find(
            'span').get_text()
        # print(app_rating)

        reviews = b.find('div', class_='BHMmbe').get_text()
        #print(app_rating, reviews)
    return JsonResponse({'image': img, 'app_name': app_name, 'developer_name': developer_name, 'description': description, 'download': download, 'app_rating': app_rating, 'reviews': reviews})


def apple_app(request):
    if request.method == 'POST':
        app_name = request.POST.get('second')
        app_id = request.POST.get('third')

        url = f"https://apps.apple.com/in/app/{app_name}/id{app_id}"
        # "https://apps.apple.com/in/app/alien-hive/id571149889"

        r = requests.get(url)
        b = BeautifulSoup(r.content, 'html5lib')

        img = b.find('picture', class_='we-artwork we-artwork--downloaded product-hero__artwork we-artwork--fullwidth we-artwork--ios-app-icon').find('source').get('srcset')
        img = img[0:img.index(',')-2]

        app_name = b.find(
            'h1', class_='product-header__title app-header__title').text[0:-2]
        print(app_name)

        developer_name = b.find('a', class_='link').text
        print(developer_name)

        description = b.find(
            'div', class_='section__description').find('p').get_text()
        print(description)

        app_rating = b.find(
            'div', class_='we-customer-ratings__averages').get_text()[0:3]
        print(app_rating[0:3])

    return JsonResponse({'image': img, 'app_name': app_name, 'developer_name': developer_name, 'description': description,
                         'app_rating': app_rating})



def keyword_find(request):
    return render(request, "Keyword_finder.html")



def keyword_finder(request):
    if request.method== 'POST':
        new_url = request.POST.get('first')
        print(new_url)
        a = first_url.objects.all()[0]
        ke = a.keywords_url
        ke_list = list(ke.split(','))
        de = a.description_url
        #de_list = list(de.split(''))
        og = a.ogdescription_url

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(
        executable_path=r'C:\Users\AJ\Downloads\chromedriver.exe', options=chrome_options)

        url2 = f"{new_url}"
        #https://stratz.com/welcome
        driver.get(url2)
        
        keywords = driver.find_elements_by_xpath("//meta[@name='keywords']")
        keywords=keywords[0].get_attribute('content')
        #description = driver.find_elements_by_xpath("//meta[@name='description']")
        #og_description = driver.find_elements_by_xpath("//meta[@name='og:description']")

        #print(keywords[0].get_attribute('content'))
        #print(description[0].get_attribute('content'))
        

        list_keywords = []
        recommended = []
        for i in ke_list:
            if i in keywords:
                list_keywords.append(i)
            else:
                recommended.append(i)
        print(list_keywords)
        print(recommended)

    return JsonResponse({'keywords':list_keywords,'recommended':recommended})
