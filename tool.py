#!/usr/bin/env python3

import requests


def banner ():

	bnr = f"""
		    ______________           _____
		   |              |         |_   |
		   |_____    _____|           |  |
			 |  |  _____   _____  |  |
			 |  | |     | |     | |  |
			 |  | | ^ ^ | | ^ ^ | |  |
			 |  | | ___ | | ___ | |  |_
			 |__| |_____| |_____| |____|
			
			coded by :- @shamsperwez   """

	print(bnr)


banner ()


url = input("Enter Target URL : ")

password = open('common.txt', 'r')

for i in password:
    urls = f'{url}{i}'
    target = requests.get(urls)
    if target.status_code == 200:
        print(target.url, end=" ")
        print(" --> " + str(target.status_code)) 
    


