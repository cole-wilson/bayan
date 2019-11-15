import requests,base64

d = {}

session_name = ''
filename = 'bayan_tmp'
precision = 300
deb = False

def init(cats,debug=False,save=True):
  for x in cats:
    add_cat(x)
  

def train(f,cat):
  f = f.split(' ')
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

  encodedstring = ' '.join([encodedstring[i:i+precision] for i in range(0, len(encodedstring))])
  #print(encodedstring)
  return encodedstring

def analyze(f):
  totest = f.split()

  totals = {}
  for cat in d:
    for x in totest:
      if x in d[cat]:
        totals[cat] = 0

  for cat in d:
    for x in totest:
      if x in d[cat]:
        totals[cat] = d[cat][x] + totals[cat]
  #print(totals)

  m = ''
  mn = 0

  for x in totals.keys():
    if totals[x] > mn:
      m = x
      mn = totals[x]
    elif totals[x] == mn:
      m = m + ' or ' + x
  return m
