#!/usr/bin/env python3

""" how to run examples:
1) $ python cli_tool.py -ext example.html
2) $ python cli_tool.py --language hindi
3) $ python cli_tool.py -dis hindi
"""

"""Programming test: Text Substitution

Write a python CLI program/tool which should have three commands:

1) extract-text
to parse any html (say, example.html) and extract all text content from <p>, <div>, <b>, <i>, <td>, <h1>...<h5>, and <span> tags. store all text segments in a properties file (say, example.properties), in key=value format. Where key will be hash of the text and value will be the text itself.

2) generate-resource
to generate language resource from the properties file (say, example.properties). this shall take an argument --language and its value (say hindi). In total command should look something like:

pythonscript resource --language hindi

This shall generate an another properties file (say, example.hindi) in the format key=value, where key would be the hash created in example.properties above and value would be hindi translation of example.properties file associated values.

3) display-html
to render translated version of example.html on the browser (say hindi version). this command should take --language argument and its value. In background pick translations from properties file (say, hindi.properties), apply mappings (from example.properties) and display translated version of the file."""

__author__		= "Amal Krishna R"
__date__		= "05/07/2016"

from bs4 import BeautifulSoup
import webbrowser
import argparse
import sys, urllib2
import os
import requests

lang_dict = {		'afrikaans' : 'af',
				'albanian' : 'sq',
				'arabic' : 'ar',
				'belarusian' : 'be',
				'bulgarian' : 'bg',
				'catalan' : 'ca',
				'chinese Simplified' : 'zh-CN',
				'chinese Traditional' : 'zh-TW',
				'croatian' : 'hr',
				'czech' : 'cs', 
				'danish' : 'da',
				'dutch' : 'nl',
				'english' : 'en',
				'estonian' : 'et',
				'filipino' : 'tl',
				'finnish' : 'fi',
				'french' : 'fr',
				'galician' : 'gl',
				'german' : 'de',
				'greek' : 'el',
				'hebrew' : 'iw',
				'hindi' : 'hi',
				'hungarian' : 'hu',
				'icelandic' : 'is',
				'indonesian' : 'id',
				'irish' : 'ga',
				'italian' : 'it',
				'japanese' : 'ja',
				'korean' : 'ko',
				'latvian' : 'lv',
				'lithuanian' : 'lt',
				'macedonian' : 'mk',
				'malay' : 'ms',
				'maltese' : 'mt',
				'norwegian' : 'no',
				'persian' : 'fa',
				'polish' : 'pl',
				'portuguese' : 'pt',
				'romanian' : 'ro',
				'russian' : 'ru',
				'serbian' : 'sr',
				'slovak' : 'sk',
				'slovenian' : 'sl',
				'spanish' : 'es',
				'swahili' : 'sw',
				'swedish' : 'sv',
				'thai' : 'th',
				'turkish' : 'tr', 
				'ukrainian' : 'uk',
				'vietnamese' : 'vi',
				'welsh' : 'cy',
				'yiddish' : 'yi'}

def extract_text(filename):
	#data extraction from the html file.
	file = open(filename)
	data = file.read()

	#read the data using BeautifulSoup.
	soup = BeautifulSoup(data, "html.parser")

	#represent the html document as a nested data structure.
	soup.prettify()
	file.close()
	#extract the data between <p>, <div>, <b>, <i>, <td>, <h1>...<h5>, and <span> tags.
	vari = []
	tags = ['h1','h2','h3','h4','h5','p','div','b','i','td','span']
	for i in range(0, len(tags)):
		var = map(str, (soup.find_all(tags[i])))
		var = map(lambda it: it.strip('<'+tags[i]+'>'), var)
		var = map(lambda it: it.strip('</'), var)
		vari.append(var)

	print vari

	#open a file for writing the data into 'example.properties'
	if os.path.exists('example.properties'):
		f = open('example.properties', 'w+')
	else:
		f = open('example.properties', 'a+')

	#writing the data into 'example.properties'
	for i in range(0, len(tags)):
		f.write(""+tags[i]+" = ")
		for j in range(0, len(vari[i])):
			f.write("%s " % vari[i][j])
		f.write("\n")
	f.close()

def language_trans(lan):
	global lang_dict
	opener = urllib2.build_opener()

	#check if the language exists in the database.
	if lan in lang_dict:
		ind = list(lang_dict.keys()).index(lan) 
	else:
		print "Language not in database"
		sys.exit()

	#extract data from 'example.properties'
	read = []
	with open('example.properties') as f:
		for line in f:
			read.append(line.strip(' \n'))
	tags = [i.split(' = ', 1)[0] for i in read]
	eng = [i.split('= ', 1)[1] for i in read]
	f.close()

	#check if the destination file already exists. 
	if os.path.exists('example.'+lan):
		f = open('example.'+lan, 'w+')
	else:
		f = open('example.'+lan, 'a+')

	#execute language translation using Google translator.
	trans = []
	for i in range(0, len(eng)):
		agents = {'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"}
		before_trans = 'class="t0">'
		link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s" % (lang_dict.values()[ind], 'en', eng[i].replace(" ", "+"))
		request = urllib2.Request(link, headers=agents)
		page = urllib2.urlopen(request).read()
		result = page[page.find(before_trans)+len(before_trans):]
		result = result.split("<")[0]
		trans.append(result)
		
		#write translated text to destination file.
		f.write(("%s = %s\n"% (tags[i], result)))
	f.close()

def display(lan):
	global lang_dict
	opener = urllib2.build_opener()

	#check if the language exists in the database.
	if lan in lang_dict:
		ind = list(lang_dict.keys()).index(lan) 
	else:
		print "Language not in database"
		sys.exit()

	#data extraction from the language properties file.
	read = []
	with open('example.'+lan) as f:
		for line in f:
			read.append(line.strip(' \n'))
	tags = [i.split(' = ', 1)[0] for i in read]
	trans = [i.split('= ', 1)[1] for i in read]

	#data extraction from the main properties file.
	file = open('example.html')
	data = file.read()

	#read the data using BeautifulSoup.
	soup = BeautifulSoup(data, "html.parser")

	#represent the html document as a nested data structure.
	soup.prettify()
	f.close()
	
	#check if the destination file already exists. 
	if os.path.exists('example.'+lan):
		f = open(lan+'.html', 'w+')
	else:
		f = open(lan+'.html', 'a+')

	#write translated text to html file.
	vari = []
	f.write('<html>\n<head>\n<meta http-equiv="Content-Language" content="%s">\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8">\n</head>\n<body>\n' % lang_dict.values()[ind])
	for i in range(0, len(tags)):
		f.write('<'+tags[i]+'>')
		f.write(unicode(trans[i],'utf-8').encode("UTF-8"))
		f.write('</'+tags[i]+'>\n')
	f.write('</body>\n</html>')
	f.close()
	
	#open the file in browser.
	webbrowser.open(lan+'.html')


def main():
	#parser for command-line options, arguments and sub-commands.
	parser = argparse.ArgumentParser(description="A Python CLI program/tool for html data manupulation.")
	group = parser.add_mutually_exclusive_group()
	group.add_argument("-ext", "--extract", help="Performs text-extraction", action="store_true")
	group.add_argument("-lan", "--language", help="Performs transaltion", action="store_true")
	group.add_argument("-dis", "--display", help="Performs display", action="store_true")
	parser.add_argument("value", help="filename to extract or language to translate/display")
	args = parser.parse_args()

	#executes the function based on the parsed command.
	if args.extract:
		extract_text(args.value)
	elif args.language:
		language_trans(args.value)
	elif args.display:
		display(args.value)

if __name__ == '__main__':
    main()
