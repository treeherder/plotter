import argparse
import os
import errno
from xml.dom.minidom import parse

parser = argparse.ArgumentParser(description='make static html with consistent styling')
parser.add_argument('--wiki', dest='wiki')
parser.add_argument('--blog', dest='blog')
parser.add_argument('--general', dest='general')

parser.add_argument('--dir', dest='dir')
parser.add_argument('--rd' dest='rd')




args = parser.parse_args() 
#this is the list of relevant 
dir = args.dir


root = '/var/www/' #where html files are served from
subdir = root+dir #the name of the html page we want to create


def chk_pth(pth):
  try:
    os.makedirs(pth)
  except OSError:
    if except.errno != errno.EEXIST:
      raise
						
						
def gen_static(loc):  # use this method to make some html
  with open('{0}'.format(args.rd)) as r:  #this is a more or less complete page
    with open('{0}/index.html'.format(loc), 'a+') as w:  # for test purposes
      for line in r:
        w.write(line)
  r.close()
  w.close()

def template():
  if args.wiki != False:
    make_page()
  elif args.blog != False:
  elif args.general != False:

def make_page():   # do stuff
  chk_pth(subdir)
  gen_static(subdir)