import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
import time
import warnings

warnings.filterwarnings('ignore')

class EfficiencyModel:
    def __init__(self, data_path):
        self.df = pd.DataFrame(pd.read_excel(data_path))
        self.df['efficiency'] = self.df['Projects_Done'] / self.df['Year_of_Study']
        self.model = DecisionTreeRegressor(random_state=42)
        self.prepare_data()

    def prepare_data(self):
        x = self.df[['Year_of_Study', 'Projects_Done']]
        y = self.df['efficiency']
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
        self.model.fit(x_train, y_train)

    def find_most_efficient_person(self, domain):
        domain_data = self.df[self.df['Domain'] == domain]
        if domain_data.empty:
            return "No data found for the given domain."
        x_domain = domain_data[['Year_of_Study', 'Projects_Done']]
        domain_data['predicted_efficiency'] = self.model.predict(x_domain)
        most_efficient_persons = domain_data.loc[domain_data['predicted_efficiency'].idxmax()]
        return most_efficient_persons['Name']


data_paths = "C:\\Users\\sanka\\Downloads\\WUIX HUB Example Dataset.xlsx"
efficiency_model = EfficiencyModel(data_paths)

input_domain = input("Enter the required Domain: ")
start_time = time.time()
a=input_domain.lower()
b=input_domain.upper()
if a=="web development" or a=="webdevelopment":
    b="Web Development"
    a="web development"
elif a=="cybersecurity" or a=="cyber security":
    b="Cyber Security"
    a="cybersecurity"
elif a=="app development" or a=="appdevelopment":
    b = "App Development"
    a = "app development"
elif a == "data science" or a == "datascience" or a == "ds":
    b = "Data Science"
    a = "data science"
elif a == "iot" or a == "internet of things":
    b = "IoT"
    a = "iot"
most_efficient_person = efficiency_model.find_most_efficient_person(a)
end_time = time.time()

print(f"The most efficient person in {b} is: {most_efficient_person}")
print(f"{end_time - start_time:.6f} seconds")
