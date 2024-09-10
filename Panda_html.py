import pandas as pd
html = pd.read_html("https://en.wikipedia.org/wiki/Mobile_country_code")
print(type(html))
print(html[0])
print(html[1])
html1 = pd.read_html("https://en.wikipedia.org/wiki/Minnesota",match = "Average daily maximum and minimum temperatures for selected cities in Minnesota")
print(html1[0])
print(type(html1[0]))
html1[0].to_html('demo.html')