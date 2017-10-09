import subprocess
import os

repositories = {
	'project1': '/<full path to project>/project1/',
	'project2': '/<full path to project>/project2/',
	'projectn': '/<full path to project>/projectn/'
}

def print_inf(msg):
	print '\n####################################################'
	print '          ' + msg + '           '
	print '####################################################\n'

def pull():
	os.system('git pull')

def pwd():
	os.system('pwd')

def pull_project(k,v):
	print_inf('Atualizando ' + k)
	os.chdir(v)
	pwd()
	pull()

def main():
	for k, v in repositories.items():
	    pull_project(k,v)

if __name__ == '__main__':
	main()
