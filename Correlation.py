import plotly.express as px
import csv
import numpy as np
def getData(data_path):
     grade = []
     day = []
     with open(data_path) as csv_file:
         csvReader = csv.DictReader(csv_file)
         for row in csvReader:
             grade.append(float(row["Marks In Percentage"]))
             day.append(float(row["Days Present"]))
     return {"x":grade,"y":day}


def find(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print(correlation[0,1])

def setup():
    data_path = "Student Marks vs Days Present.csv"
    dataSource = getData(data_path)
    find(dataSource)

setup()