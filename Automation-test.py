import pytest
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class  DemoPythonAutomation():
    def locate_browser(self):
        driver = webdriver.Firefox()
        driver.get('https://flipkart.com')
        driver.maximize_window()
        time.sleep(5)
        search = driver.find_element(By.XPATH, '//input[@placeholder="Search for Products, Brands and More"]')
        search.send_keys('phone')
        search.send_keys(Keys.ENTER)
        arr_value = driver.find_element(By.XPATH, '//a[@title="Mobiles & Accessories"]').get_attribute('title')
        print (arr_value)
        assert arr_value == 'Mobiles & Accessories' 
        element = driver.find_element(By.XPATH, '//div[@class="_3E8aIl X3IECw row"]//div[6]')
        driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(5)
find=DemoPythonAutomation()
find.locate_browser()

##############################################################################################################
# Define the base class Car
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def start_engine(self):
#         return f"{self.make} {self.model} engine started."
#
#     def __str__(self):
#         return f"{self.year} {self.make} {self.model}"
#
# # Define a subclass ElectricCar that inherits from Car
# class ElectricCar(Car):
#     def __init__(self, make, model, year, battery_size=75):
#         super().__init__(make, model, year)  # Call the constructor of the base class
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         return f"This car has a {self.battery_size}-kWh battery."
#
#     def start_engine(self):
#         return f"{self.make} {self.model} is ready to go silently."
#
# # Create instances of Car and ElectricCar
# my_car = Car("Toyota", "Camry", 2020)
# my_electric_car = ElectricCar("Tesla", "Model S", 2023)
#
# # Use the methods
# print(my_car.start_engine())          # Output: Toyota Camry engine started.
# print(my_electric_car.start_engine()) # Output: Tesla Model S is ready to go silently.
#
# # Print the description
# print(my_car)                         # Output: 2020 Toyota Camry
# print(my_electric_car)                # Output: 2023 Tesla Model S
#
# # Describe the battery of the electric car
# print(my_electric_car.describe_battery()) # Output: This car has a 75-kWh battery.
