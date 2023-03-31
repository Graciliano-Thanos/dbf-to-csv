import pandas as pd
from simpledbf import Dbf5
import os

if __name__ == "__main__":
    csv_folder = "csv"
    for dbf_file in os.listdir("dbf"):
        dbfPath = "dbf/"+dbf_file
        dbfname = dbf_file.split(".")[0]
        print(dbfname+" in progress...")
        csvPath = os.getcwd()+"\csv"
        print(csvPath)
        #df = Dbf5(dbfPath).to_dataframe()
        #df.to_csv(csvPath+dbfname+".csv")
    print("Successfully converted to .csv!")

