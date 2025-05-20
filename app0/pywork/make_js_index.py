# coding=utf-8
""" make_js_index.py for meghasrnga repo
"""
from __future__ import print_function
import sys, re, codecs
import json

def int_to_roman(n):
    val_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    roman_numeral = ''
    for value, numeral in val_map:
        while n >= value:
            roman_numeral += numeral
            n -= value
            
    return roman_numeral

# Example usage:
#num = int(input("Enter a positive integer: "))
#print(f"Roman numeral: {int_to_roman(num)}")

def roman_to_int(roman):
 droman_int = {'I':1, 'II':2, 'III':3, 'IV':4,
                'V':5, 'VI':6, 'VII':7, 'VIII':8, 'IX':9,
                'X':10, 'XI':11, 'XII':12,'':0}
 if roman in droman_int:
  return droman_int[roman]
 else:
  # error condition
  return None

def make_js(recs):
 outarr = []
 outarr.append('indexdata = [')
 arr = [] # array of Python dicts
 for rec in recs:
  d = rec.todict()  # a Python dictionary
  arr.append(d)
 return arr

def write_recs(fileout,data):
 with codecs.open(fileout,"w","utf-8") as f:
  f.write('indexdata = \n')
  jsonstring = json.dumps(data,indent=1)
  f.write( jsonstring +  '\n')
  f.write('; // end of indexdata\n')
  
 print('%s json records written to %s' %(len(data),fileout))

class PagerecsPreface:
 def __init__(self,epage,rpref,title):
  self.page = int(epage)
  self.ipage = rpref  # a string
  self.title = title 
  self.vpstr = '%03d' % epage
 def todict(self):
  e = {
   'page':int(self.page),
   'title':self.title,
   'ipage':self.ipage,
   'vp':self.vpstr
  }
  return e
  
def init_pagerecs_preface():
 recs = []
 ipref = 0  # 
 for epage in range(6,15+1):
  ipref = ipref + 1
  rpref = int_to_roman(ipref)
  rpref = rpref.lower()
  ipage = rpref
  title = 'praefatio %s' % rpref
  rec = PagerecsPreface(epage,rpref,title)
  recs.append(rec)
 # two additional pages before the first verse
 #recs.append( PagerecsPreface(16,'1','1'))
 #recs.append( PagerecsPreface(17,'2','2'))
 return recs

def init_pagerecs_main():
 recs = []
 for epage in range(14,53+1):
  ipage = epage - 13
  title = 'Page %s' % ipage
  rec = PagerecsPreface(epage,ipage,title)
  recs.append(rec)
 return recs

def init_pagerecs_annotatio():
 recs = []
 for epage in range(54,69+1):
  ipage = epage - 13
  title = 'annotatio %s' % ipage
  rec = PagerecsPreface(epage,ipage,title)
  recs.append(rec)
 return recs

def init_pagerecs_glossarium():
 recs = []
 for epage in range(70,148+1):
  ipage = epage - 13
  title = 'glossarium %s' % ipage
  rec = PagerecsPreface(epage,ipage,title)
  recs.append(rec)
 return recs

def init_pagerecs_addenda():
 recs = []
 for epage in range(149,149+1):
  ipage = epage - 13
  title = 'addenda %s' % ipage
  rec = PagerecsPreface(epage,ipage,title)
  recs.append(rec)
 return recs


if __name__ == "__main__":
 fileout = sys.argv[1]  # index.js
 filevol = None

 # preface
 pagerecs_preface = init_pagerecs_preface()
 outrecs_preface  = make_js(pagerecs_preface)
 # main
 pagerecs_main = init_pagerecs_main()
 outrecs_main = make_js(pagerecs_main)
 # annotatio critica
 pagerecs_annotatio = init_pagerecs_annotatio()
 outrecs_annotatio = make_js(pagerecs_annotatio)
 # glossarium
 pagerecs_glossarium = init_pagerecs_glossarium()
 outrecs_glossarium = make_js(pagerecs_glossarium)
 # addenda
 pagerecs_addenda = init_pagerecs_addenda()
 outrecs_addenda = make_js(pagerecs_addenda)
 
 # concat and write 
 outrecs = (outrecs_preface + outrecs_main + outrecs_annotatio +
            outrecs_glossarium + outrecs_addenda)
 write_recs(fileout,outrecs)
 
 exit(1)
 pagerecs_prakrit = init_pagerecs_prakrit()
 pagerecs_VS = init_pagerecs_VS()
 
 outrecs_main = make_js(pagerecs_main)
 outrecs_preface = make_js(pagerecs_preface)
 outrecs_prakrit = make_js(pagerecs_prakrit)
 outrecs_VS = make_js(pagerecs_VS)
 
 outrecs = (outrecs_preface + outrecs_main +
            outrecs_prakrit + outrecs_VS)
 write_recs(fileout,outrecs)
 #check1(pagerecs)
 
