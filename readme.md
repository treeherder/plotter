plotter, a static html generator to keep the site's theme and layout consistent for gardenplot.info.
I decided to build this tool as an aid to my first attempts at building a website, after realizing how tedious it can be to generate all of this static content by hand. 
Since I'm unfamiliar with PHP, and am launching this site on a Raspberry Pi, anyway, I figured I would just take a stab at it in python, for educational purposes.

	To Do:
		- compile list of elements for args
		- make a template for each element
		- ???
		- profit

    - edit existing files?
		- create more complex args for element number position and size?

pltr.py --dir <str> --depth <int> --element <str> --style <str>

pltr --dir wiki/broccoli --depth 2 --style <str> --element jumbotron  --element right-column  

I might be able to eliminate depth with a style source, basically just need some way to line up the appropriate depth for various file locations in the directory tree.