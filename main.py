import pandas as pd
from simpledbf import Dbf5
import os

if __name__ == "__main__":
    csv_folder = "csv"

    #Get all .dbf files in dbf directory
    for dbf_file in os.listdir("dbf"):
        if "gitignore" not in dbf_file:
            dbfPath = "dbf/"+dbf_file
            dbfname = dbf_file.split(".")[0]
            print(dbfname+"conversion in progress...")
            csvPath = os.getcwd()+"\csv"                 #Define .csv files path

            #Convert to Dataframe then to .csv
            df = Dbf5(dbfPath).to_dataframe()
            path = csvPath+f"\{dbfname}" +".csv"
            df.to_csv(path)
    print("Successfully converted files to .csv!")

