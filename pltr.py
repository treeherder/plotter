import argparse
import os
import errno
from xml.dom.minidom import parse

parser = argparse.ArgumentParser(description='make static html with consitent styling')
parser.add_argument('--jmtrn', dest='jmtrn')
parser.add_argument('--cols', dest='cols')
parser.add_argument('--rows', dest='rows')
parser.add_argument('--cells', dest='cells')
parser.add_argument('--dir', dest='dir')

args = parser.parse_args()
dir = args.dir
nav = args.nav
jmtrn - args.jmtrn


root = '/var/www/' #where html files are served from
subdir = root+dir #the name of the html page we want to create

def chk_pth(pth):
  try:
    os.makedirs(pth)
  except OSError:
    if except.errno != errno.EEXIST:
      raise
						
						
def gen_static(loc):  # use this method to make some html
  with open('template.txt') as r:  #this is a more or less complete page
    with open('{0}/index.html'.format(loc), 'a+') as w:  # for test purposes
      for line in r:
        w.write(line)
  r.close()
  w.close()

	
	
chk_pth(subdir)
gen_static(subdir)
