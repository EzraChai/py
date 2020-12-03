from msedge.selenium_tools import options
from msedge.selenium_tools import Edge,EdgeOptions
from time import sleep

options = EdgeOptions()
options.use_chromium = True 
driver = Edge(options=options)
options.add_experimental_option("excludeSwitches", ['enable-automation'])

kodSekolah = "NEB2054"

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSduotkz5L48QN_vXksFCerIfHF4ihDQyxlARbL4BneSeqzNWg/viewform")
print("Google sites opened")
sleep(0.5)

KodSekolah_box = driver.find_element_by_class_name("quantumWizTextinputPaperinputEl")
KodSekolah_box.send_keys(kodSekolah)
sleep(0.2)

