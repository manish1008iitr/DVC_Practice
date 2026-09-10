import pandas as pd 
import os 

data = {
    "Name": ["Alice", "Bob", "Cat"],
    "Age" : [28,22,32],
    "City":["New york", "Delhi","Yorkshire"]
}

df = pd.DataFrame(data)

os.makedirs("data", exist_ok = True)

file_path = os.path.join("data","sample.csv")

df.to_csv(file_path, index = False)

print("CSV file has been created successfully")