catAl = []
catBl = []

catA = {}
catB = {}

prec = 300

import  base64
import requests

def getfile(url,p = prec):
  name = 'bayan_tmp'
  r = requests.get(url, allow_redirects=True)
  open(name, 'wb').write(r.content)

  with open(name, "rb") as image_file:
      encodedstring = base64.b64encode(image_file.read ())

  encodedstring = str(encodedstring)

  encodedstring = ' '.join([encodedstring[i:i+2] for i in range(0, len(encodedstring), prec)])

  return encodedstring

def train(category,string):
  text = []
  text=string.split()
  catltype = category
  for x in range(len(text)):
    if catltype == 2:
      catBl.append(text[x])
    elif catltype == 1:
      catAl.append(text[x])
  
  for x in range(len(catAl)):
    catA[catAl[x]] = 0

  for x in range(len(catBl)):
    catB[catBl[x]] = 0

  for x in range(len(catAl)):
    catA[catAl[x]] = catA[catAl[x]] + 1

  for x in range(len(catBl)):
    catB[catBl[x]] = catB[catBl[x]] + 1



def precision(p):
  global prec 
  prec= p



def assign(s1v,s2v):
  global s1
  s1 = s1v
  global s2 
  s2 = s2v

def analyze(string):
  totest = string
  totest = totest.split()

  catAtotal = 0 
  for x in range(len(totest)):
    if totest[x] in catA:
      catAtotal = catAtotal + catA[totest[x]]

  catBtotal = 0 
  for x in range(len(totest)):
    if totest[x] in catB:
      catBtotal = catBtotal + catB[totest[x]]
      
  if catBtotal > catAtotal:
    return 2
  elif catAtotal > catBtotal:
    return 1
  else:
    return 0
