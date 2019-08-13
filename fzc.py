import requests
import argparse
from bs4 import BeautifulSoup



twurl = "https://twitter.com/"

class argus_get():
   pr = argparse.ArgumentParser()
   pr.add_argument("-f", "--fname", default="id.txt", help="select id file name")
   args = pr.parse_args()

def main():
   argus = argus_get()
   ag = argus.args
   
   f_check(ag.fname)

def f_check(fname):
   f = open(fname, 'r')
   uid = f.readline()
   headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}
   while uid:
      r = requests.get(twurl + uid.strip(), headers=headers)
      
      sp = BeautifulSoup(r.text, "html.parser")
      
      if len(r.text) < 300000:
         print("###@" + uid.strip() + ": freeze or not exist account!!!")
      
      else:
         n = (sp.title.string).find(')') + 1
         print(sp.title.string[0:n])

      uid = f.readline()

   f.close()

if __name__ == "__main__":
      main()
