from msedge.selenium_tools import Edge,EdgeOptions

options = EdgeOptions()
options.use_chromium = True 
driver = Edge(options=options)

driver.get("https://facebook.com/ ")