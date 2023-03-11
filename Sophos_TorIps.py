import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install()) # install newest chrome driver
driver.get("https://www.dan.me.uk/torlist/?exit")

ipSearch = driver.find_element(By.TAG_NAME,"pre") # Get the element that holds all the Ips

ipList = ipSearch.text.splitlines() # seperate the whole text into list
print(ipList)

# Create/Open cvs and edit it 
with open('SophosTorIps.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)

    filewriter.writerow(['Allow/Block' ,'Email address/Domain']) # Add the default row as suggested in sophos
    
    # For loop adding all the ips into csv and blocking them
    for ips in ipList:
        filewriter.writerow(['Block' ,ips])
    