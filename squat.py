#!/usr/bin/env python

import sys
import subprocess
try:
	from src.Game import Main
except ImportError as e:
	print("Cannot load game, full message :\n%s"%e.message)

def main():
	if len(sys.argv) > 1:
		if sys.argv[1] == 'run':
			run()
		elif sys.argv[1] == 'clean':
			clean()

def run():
	main = Main(800,600)
	main.main()

def clean():
	print(subprocess.check_output('find src -name "*.pyc" | xargs rm',shell=True))

if __name__=="__main__":
	main()
