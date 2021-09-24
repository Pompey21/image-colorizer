from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import urllib.request
import requests
import difflib

from webdriver_manager.firefox import GeckoDriverManager



################
# PARAMAS
################
what_to_search = 'beach sunset'
number_of_images = 100


# 1. Opening up the  browser  and going to a specific web-page (provided in the link)
# this opens a new browser window ready to search
browser = webdriver.Firefox(executable_path='/afs/inf.ed.ac.uk/user/s18/s1813308/bin/geckodriver')
# GeckoDriverManager(path='~/geckodriver').install()
browser.get('https://www.google.ca/imghp?hl=en&tab=ri&authuser=0&ogbl')


# 2. Interacting with Google's home page
#	- that annoying 'Before you continue' notification keeps on popping up
#   	-> need to get rid of it!
browser.find_element_by_id('L2AGLb').click()

#	- finding that search box and putting in our searching qiery
search_box = browser.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
search_box.send_keys(what_to_search)
search_box.send_keys(Keys.ENTER)


html_before = browser.page_source



img = browser.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+str(1)+']/a[1]/div[1]/img')
img.click()


# get the html of the website
html_after = browser.page_source


difference = difflib.ndiff(html_before, html_after)
print(difference)



# src = img.get_attribute('src')
# print(src)


# url = 'https://images.pexels.com/photos/1032650/pexels-photo-1032650.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500'
# r = requests.get(src, allow_redirects=True)
# print(r)

# open('sunsetYOOOOO2222.ico', 'wb').write(r.content)









# # 3. Scrolling down the web-page
# #	- will keep scrolling down the webpage until it cannot scroll no more
# last_height = driver.execute_script('return document.body.scrollHeight')
# while True:
#     driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
#     time.sleep(2)
#     new_height = driver.execute_script('return document.body.scrollHeight')
#     try:
#         driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
#         time.sleep(2)
#     except:
#         pass
#     if new_height == last_height:
#         break
#     last_height = new_height


#####################################################
# 4. Downloading images
#	- to be really smart about it, we will not download manually each picture,
#	  but take screenshots - all of that using Selenium

# for i in range(1, number_of_images):
#     try:
#         driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img').screenshot('/Users/admin/Desktop/images/colorized/smth_else/' + what_to_search + '('+str(i)+').png')
#     except:
        # pass
#####################################################


# 4. Downloading images
# img = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+str(1)+']/a[1]/div[1]/img')
# src = img.get_attribute('src')

# # http.get(src)

# # print('Soource: ' + str(src))


# 	# first option
# name_of_picture = what_to_search + '.png'
# urllib.request.urlretrieve(src, name_of_picture)




####################################################
# for i in range(1,10):
	# print('----------')
	# print(i)
	# print('----------')
	# img = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img')
	# src = img.get_attribute('src')

	# name_of_picture = what_to_search + str(i) + '.png'
	# urllib.request.urlretrieve(src, name_of_picture)


# for i in range(1, number_of_images):
# 	try:
# 		img = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img')

# 		# find source
# 		src = img.get_attribute('src')

# 		# download the image
# 		name_of_picture = what_to_search + '.png'
# 		urllib.urlretrieve(src, name_of_picture)
# 	except:
# 		pass













