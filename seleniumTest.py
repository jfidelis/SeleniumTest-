from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("http://xxxx.xxxx.com.br")
assert "Sistema de Controle de Acesso" in driver.title

# Login --------------------------------------------------------------------------

elem = driver.find_element_by_name("txtUsrLogin")
elem.clear()
elem.send_keys("admin")

elem = driver.find_element_by_name("txtUserPassLogin")
elem.clear()
elem.send_keys("senha")

elem.send_keys(Keys.RETURN)

# --------------------------------------------------------------------------------
# Link Pessoas
time.sleep(1)

elem = driver.find_element_by_link_text("Pessoas")

elem.click()

# --------------------------------------------------------------------------------
# Link Cadastro de Pessoa
time.sleep(1)

elem = driver.find_element_by_link_text("Cadastro de Pessoa")

elem.click()

# --------------------------------------------------------------------------------
# Botão Cadastrar
time.sleep(1)

elem = driver.find_element_by_name("ctl00$ctl00$SaveButtonMainMaster$ActionButtonsHolder$btnNewItem")

elem.click()
# --------------------------------------------------------------------------------

#ctl00$ctl00$MainContentMainMaster$MainContent$txtRegistration
time.sleep(1)
elem = driver.find_element_by_name("ctl00$ctl00$MainContentMainMaster$MainContent$txtRegistration")
elem.clear()
elem.send_keys("100")
elem.send_keys(Keys.RETURN)

#ctl00$ctl00$MainContentMainMaster$MainContent$txtName
time.sleep(1)
elem = driver.find_element_by_name("ctl00$ctl00$MainContentMainMaster$MainContent$txtName")
elem.clear()
elem.send_keys("Pessoa 100")
elem.send_keys(Keys.RETURN)

#ctl00$ctl00$MainContentMainMaster$MainContent$ddlSituation
driver.find_element_by_xpath("//select[@name='ctl00$ctl00$MainContentMainMaster$MainContent$ddlSituation']/option[text()='Liberada']").click()

#ctl00$ctl00$MainContentMainMaster$MainContent$btnSearchStructure
time.sleep(1)
elem = driver.find_element_by_xpath("//input[@name='ctl00$ctl00$MainContentMainMaster$MainContent$btnSearchStructure']")
elem.click()

#MainContentMainMaster_MainContent_StructureTreeviewPopup_tvStructuren0CheckBox
time.sleep(2)
elem = driver.find_element_by_xpath("//input[@name='MainContentMainMaster_MainContent_StructureTreeviewPopup_tvStructuren0CheckBox']")
elem.click()

# clica em ok
time.sleep(1)
elem = driver.find_element_by_name("ctl00$ctl00$MainContentMainMaster$MainContent$StructureTreeviewPopup$btnOkStructure")
elem.click()

#image
#ctl00$ctl00$MainContentMainMaster$MainContent$accessProfileControlPersonEdt$AccessProfileLookUp
time.sleep(1)
elem = driver.find_element_by_xpath("//input[@name='ctl00$ctl00$MainContentMainMaster$MainContent$accessProfileControlPersonEdt$AccessProfileLookUp']")
elem.click()

#check
#ctl00$ctl00$MainContentMainMaster$MainContent$accessProfileControlPersonEdt$AccessProfilePopup$gv_AvailableAccessProfiles$ctl02$chk_Selected
time.sleep(2)
elem = driver.find_element_by_xpath("//input[@name='ctl00$ctl00$MainContentMainMaster$MainContent$accessProfileControlPersonEdt$AccessProfilePopup$gv_AvailableAccessProfiles$ctl02$chk_Selected']")
elem.click()

#btn
#ctl00$ctl00$MainContentMainMaster$MainContent$accessProfileControlPersonEdt$AccessProfilePopup$btnAccessProfileLookUpOK
time.sleep(1)
elem = driver.find_element_by_name("ctl00$ctl00$MainContentMainMaster$MainContent$accessProfileControlPersonEdt$AccessProfilePopup$btnAccessProfileLookUpOK")
elem.click()

time.sleep(1)
elem = driver.find_element_by_link_text("Credenciais")
elem.click()

#links = driver.find_elements(By.TAG_NAME, "a")

assert "No results found." not in driver.page_source

#driver.close()