from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = webdriver.Firefox()

browser.get('http://bridges-cs.herokuapp.com/assignments/555/esaule')

labelelem = browser.find_element_by_id('nodelabels')  # Find the search box

elem = browser.find_element_by_id('slideButton1')  # Find the search box

action = ActionChains(browser) 
action.click(on_element = labelelem) #because of a bug need to click twice before
action.click(on_element = elem) #becasue of a bug need to click away
action.perform()

for i in range(0, 29):

    button = 'slideButton'+str(i)
    elem = browser.find_element_by_id(button)  # Find the search box
    


    # create action chain object 
    action = ActionChains(browser) 

    action.click(on_element = labelelem) #becasue of a bug need to click twice
    action.pause(1)

    
    # click the item 
    action.click(on_element = elem) 

    action.pause(1)
    
    action.click(on_element = labelelem)
    action.pause(1)
    
    
    # perform the operation 
    action.perform() 

    svgelem = browser.find_element_by_id('svg0')  # Find the search box

    print (svgelem.get_attribute('outerHTML'))
    
    time.sleep(2)

browser.quit()
