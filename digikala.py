from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep



driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://digikala.com")

#View page login
driver.find_element('class name', 'o-tooltip').click()
sleep(2)

#Enter email field
user_email = driver.find_element('name', 'login[email_phone]')
user_email.send_keys("milad.hajizadehh@gmail.com")
driver.find_element('class name', 'c-login__form-action').click()

#View password page
user_password = driver.find_element('name',"login[password]")
user_password.send_keys("Milad537383")
driver.find_element('xpath', '//button[@type="submit"]').click()

#View username in land
driver.find_element('class name', 'c-header__btn-profile').click()
sleep(1)