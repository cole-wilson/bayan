# Created by Cole Wilson
# http://cole-wilson.github.io
# 
# documentation at: http://cole-wilson.github.io/bayan
#                 & http://github.com/bayan


# System Variables (edit):

preision_level = 500
url_sniffing = False

# Don't Edit:
precision = precision_level

import requests,base64

d = {}

session_name = ''
filename = 'bayan_tmp'

deb = False

def source(url):
  data = str(requests.get(url).content)
  data = data.replace('b\'','').replace('\\n','\n').replace('"','').replace('\'b','').replace('bhttp','http')
  data = data.split('\n')[0:len(data.split('\n'))-1]
  print()
  da = {}
  for x in range(0,len(data),2):
    da[data[x]] = data[x+1]
  xc = 0
  xt = len(da.keys())
  for x in da.keys():
    xc = xc+1
    f = get_file(x)
    train(f,da[x])
    
def init(cats,debug=False,save=True):
  for x in cats:
    add_cat(x)
  
def train(f,cat):
  f = f['data'].split(' ')
  for x in f:
    if x in d[cat].keys():
      d[cat][x] = d[cat][x]+1
    else:
      d[cat][x] = 1

def add_cat(m):
  d[m] = {}

def get_file(url):
  r = requests.get(url, allow_redirects=True)
  open(filename, 'wb').write(r.content)
  with open(filename, "rb") as image_file:
      encodedstring = base64.b64encode(image_file.read ())
  encodedstring = str(encodedstring)
  f = open('file.txt','a')
  f.write(encodedstring)
  f.close()
  encodedstring = ' '.join([encodedstring[i:i+precision] for i in range(0, len(encodedstring),precision)])
  #print(encodedstring)
  return {'data':encodedstring,'url':url}

def chp(pre):
  global d
  dt = d
  
  for x in d.keys():
    dt[x] = {}
    for y in d[x].keys(): 
      dt[x][y] = ' '.join([y.replace(' ','')[i:i+precision] for i in range(0, len(y.replace(' ','')),precision)])
  for x in d.keys():
    d[x] = dt[x]

def analyze(f):
  totest = f['data'].split()
  totals = {}
  for cat in d:
    for x in totest:
      if x in d[cat]:
        totals[cat] = 0
  for cat in d:
    if cat in f['url']:
      totals[cat] = totals[cat] + 2000
    for x in totest:
      if x in d[cat]:
        totals[cat] = d[cat][x] + totals[cat]
  #print(totals)
  m = ''
  mn = 0
  global precision
  while precision > 50:
    for x in totals.keys():
      if totals[x] > mn:
        di = totals[x]-mn
        om = m
        m = x
        mn = totals[x]
      elif totals[x] == mn:
        m = '' + m + ' or ' + x
    f = open('save.txt','a')
    f.write('d:\n' + str(d) +   '\n\n\n\n\n\n\n------\n\n\n\n\n\ntotals:\n' + str (totals))
    f.close()
    if m != '':
      return {'result':m,'runnerup':om,'confidence':di}
    else:
      op = precision
      precision = precision - 50
      print('Error, changing precision from: ' + str(op) + ' to: ' + str(precision))
      chp(precision)
      f = str(f).replace(' ','')
      f = ' '.join([f.replace(' ','')[i:i+precision] for i in range(0, len(f.replace(' ','')),precision)])
  return ''
  global oprec
  precision = oprec
