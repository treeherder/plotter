import argparse
import os
import errno


parser = argparse.ArgumentParser(description='make static html with consitent styling')
parser.add_argument('--jmtrn', dest='jmtrn')
parser.add_argument('--cols', dest='cols')
parser.add_argument('--rows', dest='rows')
parser.add_argument('--cells', dest='cells')
parser.add_argument('--dir', dest='dir')

args = parser.parse_args()
dir = args.dir

root = '/var/www/' #where html files are served from
subdir = root+dir

def chk_pth(pth):
  try:
    os.makedirs(pth)
  except OSError as expt:
    if expt.errno != errno.EEXIST:
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
