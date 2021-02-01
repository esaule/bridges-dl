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

elements = browser.find_elements_by_xpath("//div[contains(@id,\"slideButton\")]")  #all the slider button

for a in elements:

    button = a.get_attribute('id')
    elem = browser.find_element_by_id(button)  # Find the search box
    


    # create action chain object 
    action = ActionChains(browser) 

    action.click(on_element = labelelem) #toggle label off
#    action.pause(1)
    # click the item 
    action.click(on_element = elem) #click on tab
    action.pause(1)
    action.click(on_element = labelelem) #toggle label on
#    action.pause(1)
    
    
    # perform the operation 
    action.perform() 

    svgelem = browser.find_element_by_id('svg0')  # Find the search box

    f = open(button+'.svg', 'w')
    f.write(svgelem.get_attribute('outerHTML'))
    f.close();
    
    time.sleep(2)

browser.quit()
