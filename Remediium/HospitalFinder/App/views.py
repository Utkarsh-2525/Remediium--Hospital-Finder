# from django.shortcuts import render
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# options = webdriver.ChromeOptions()
# options.add_argument("headless")
# driver = webdriver.Chrome(executable_path='chromedriver', chrome_options=options)
# driver2 = webdriver.Chrome(executable_path='chromedriver', chrome_options=options)

# def Scrap(request):
#     if request.method == "POST":
#         x = request.POST["symptom"]
#         y = request.POST["city"]
       
#         st = "https://www.google.com/maps/search/"
#         st+=x
#         st+="+hospitals+in+"
#         st+=y

        
#         driver.get(st)
        
        
#         # for i in driver.find_elements(By.CLASS_NAME,"hfpxzc"):
#         #     if(i.is_displayed()):
#         #          i.click()
#         #          print(driver.current_url)
                
#                 #  yt = driver.find_element(By.CLASS_NAME,'Io6YTe')
#                 #  print(yt,"\n")

            
#         # for i in range(len(ls)):
#         #     if(ls[i].is_displayed()):
#         #         ls[i].click()
#         #         driver.timeouts(3)
#         #         yt = driver.find_element(By.CLASS_NAME,'Io6YTe')
#         #         print(yt,"\n")

            
            
#             # yt = driver.find_element(By.CLASS_NAME,'Io6YTe')
#             # print(yt) 

        
       
#         # for i in ls:
#         #     ls = ls.click()
#         #     try:
#         #         yt = driver.find_element(By.CLASS_NAME,'Io6YTe')
#         #         print(yt)   
#         #     except:
#         #         continue
            
            

#         ls=driver.find_elements(By.CLASS_NAME,'hfpxzc')
        
#         v=[]
#         desc=[]
#         temp=[]
#         link =[]
#         for i in ls:
#             v.append(i.get_attribute('aria-label'))
            
        
#         for i in v:
#             s="https://www.google.com/search?q="
#             splt = i.split()
#             for j in splt:
#                 s+=j
#                 s+='+'
            
#             driver2.get(s)
#             try:
#                 t = driver2.find_elements(By.CLASS_NAME,'VwiC3b')[0]
#                 desc.append(t.text)
#             except:
#                 continue

            
#             # t = driver2.find_elements(By.CLASS_NAME,'qLRx3b')[0]
#             # temp.append(t.text)
            
#         # for i in temp:
#         #     link.append(i[0:i.index("›")])
#         # print(link)

#         v = zip(v,desc) 
        
        
#        # driver.get()
#         data = {'x':v}
#         return render(request,"searchdata.html", context=data)


# def Remedy(request):
#     if request.method == "POST":

#         x = request.POST["symptom"]

#         st="https://www.google.com/search?q=home remedies for"+x

#         driver.get(st)

#         t = driver.find_element(By.CLASS_NAME,'yuRUbf').find_element(By.TAG_NAME, "a").get_attribute("href")

#         return render(request, "remedies.html", context={'x':t})





# def remedypage(request):
#         return render(request, "remedies.html")

# def home(request):
#     return render(request,"index.html")

# def Search(request):
#     return render(request, "home.html")

# def Contact(request):
#     return render(request, "contact.html")

# def Team(request):
#     return render(request, "team.html")

# def About(request):
#     return render(request, "about.html")


# #CONTACT DATA

# def CONTACT(request):
#     if request.method == "POST":
#         name = request.POST["name"]
#         email = request.POST["email"]
#         phone = request.POST["phone"]
#         message = request.POST["message"]



from django.shortcuts import render,HttpResponse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.edge.service import Service

import firebase_admin
import os
import json

from firebase_admin import credentials

from firebase_admin import firestore

# options = webdriver.ChromeOptions()
# options.add_argument("headless")
# driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=options)
# driver2 = webdriver.Chrome(executable_path='./chromedriver', chrome_options=options)

edgeService = Service(r"D:\\Projects\\Remediium\\msedgedriver.exe")
#options = webdriver.EdgeOptions()
#options.add_argument("headless")
driver = webdriver.Edge(service=edgeService )
driver2 = webdriver.Edge(service=edgeService)

def Scrap(request):
    if request.method == "POST":
        x = request.POST["symptom"]
        y = request.POST["city"]
       
        st = "https://www.google.com/maps/search/"
        st+=x
        st+="+hospitals+in+"
        st+=y

        
        driver.get(st)
        
        
        # for i in driver.find_elements(By.CLASS_NAME,"hfpxzc"):
        #     if(i.is_displayed()):
        #          i.click()
        #          print(driver.current_url)
                
                #  yt = driver.find_element(By.CLASS_NAME,'Io6YTe')
                #  print(yt,"\n")

            
        # for i in range(len(ls)):
        #     if(ls[i].is_displayed()):
        #         ls[i].click()
        #         driver.timeouts(3)
        #         yt = driver.find_element(By.CLASS_NAME,'Io6YTe')
        #         print(yt,"\n")

            
            
            # yt = driver.find_element(By.CLASS_NAME,'Io6YTe')
            # print(yt) 

        
       
        # for i in ls:
        #     ls = ls.click()
        #     try:
        #         yt = driver.find_element(By.CLASS_NAME,'Io6YTe')
        #         print(yt)   
        #     except:
        #         continue
            
            

        ls=driver.find_elements(By.CLASS_NAME,'hfpxzc')
        
        v=[]
        names={}
        description={}
        desc=[]
        temp=[]
        link =[]
        for i in ls:
            v.append(i.get_attribute('aria-label'))

        
        
        for i in v:
            s="https://www.google.com/search?q="
            splt = i.split()
            for j in splt:
                s+=j
                s+='+'
            
            driver2.get(s)
            try:
                t = driver2.find_elements(By.CLASS_NAME,'VwiC3b')[0]
                rate = driver2.find_elements(By.CLASS_NAME,'ZkP5Je')[0]
                desc.append(t.text)
                desc.append(rate.text)
            except:
                continue

            
            # for i in range(len(v)):
            #     names['name']= v[i]
            #     names['desc']=desc[i]

            # print(description)
            
            # t = driver2.find_elements(By.CLASS_NAME,'qLRx3b')[0]
            # temp.append(t.text)
            
        # for i in temp:
        #     link.append(i[0:i.index("›")])
        # print(link)

        names = [{"name": v, "desc": desc,"rating": rate}]
        j1 = json.dumps(v)
        j2 = json.dumps(names)


        v = zip(v,desc) 
        
        
       # driver.get()
        data = {'x':v}
        # return render(request,"searchdata.html", context=data)
        return HttpResponse(j1)


def Remedy(request):
    if request.method == "POST":

        x = request.POST["name"]

        st="https://www.google.com/search?q=home remedies for"+x

        driver.get(st)

        t = driver.find_element(By.CLASS_NAME,'yuRUbf').find_element(By.TAG_NAME, "a").get_attribute("href")

        return HttpResponse(t)





def remedypage(request):
        return render(request, "remedies.html")

def home(request):
    return render(request,"index.html")

def Search(request):
    return render(request, "home.html")

def Contact(request):
    return render(request, "contact.html")

def Team(request):
    return render(request, "team.html")

def About(request):
    return render(request, "about.html")


#CONTACT DATA
cred = credentials.Certificate(os.path.join(os.path.dirname(__file__), 'serviceKey.json'))
firebase_admin.initialize_app(cred)
fDb = firestore.client()

def CONTACT(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]

        cData = {
            'name':name,
            'email':email,
            'phone':phone,
            'message':message
        }
        # From Here it will send the data to firebase

        update_time, city_ref = fDb.collection(u'Contact').add(cData)

        return HttpResponse("1")