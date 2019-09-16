# Simple XML Parser
import requests as req
import xml.etree.ElementTree as ET
import pandas as pd
XML_url = 'https://www.w3schools.com/xml/plant_catalog.xml'
col_labels = ['COMMON', 'BOTANICAL', 'ZONE', 'LIGHT', 'PRICE', 'AVAILABILITY']
def parse(XML_url):
    response = req.get(XML_url)
    return response.text

def extract_data():
    data = parse(XML_url)
    root = ET.fromstring(data)
    plants_characterisitics = []

    # # selective extraction of just COMMON Name of plants
    # common_names = []
    # for plant in root.findall('PLANT'):
    #     common_names.append(plant.find('COMMON').text)
    # return common_names

    #plants_characterisitics.append(col_labels)
    for child in root:
        attributes = list(child)
        temp = []
        for item in attributes:
            temp.append(str(item.text))
        plants_characterisitics.append(temp)
    return plants_characterisitics

def make_df():
    plant_chars = extract_data()
    df = pd.DataFrame(data=plant_chars, columns=col_labels)
    df.to_csv("C:\\Users\\Sahil Shahani\\Desktop\\XMLData.csv")


#Calling function which makes dataframe
make_df()
print("Hello")