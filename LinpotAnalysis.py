import pandas as pd
import plotly.express as px
import time
from sklearn.cluster import KMeans


class LinpotAnalysis:

    def __init__(self, file_name: str, xl_file_name: str):
        self.file_name = file_name
        self.data = pd.DataFrame(pd.read_csv(self.file_name))
        self.xl_data = pd.DataFrame(pd.read_csv(xl_file_name))

    def convert_voltage_to_mm(self):
        for i, row in self.data.iterrows():
            self.data.loc[i, 'Front Right'] = row['Front Right'] * 15.0
            self.data.loc[i, 'Front Left'] = row['Front Left'] * 15.0
            self.data.loc[i, 'Rear Right'] = row['Rear Right'] * 15.0
            self.data.loc[i, 'Rear Left'] = row['Rear Left'] * 15.0

    def convert_time(self, data):
        for i, row in data.iterrows():
            time_step = row['Time']
            mlsec = repr(time_step).split('.')[1][:3]
            data.loc[i, 'Time'] = time.strftime("%H:%M:%S.{} %Z".format(mlsec), time.localtime(time_step))

    def plot(self):
        fig = px.line(self.data, x='Time', y=['Front Right', 'Front Left',
                                              'Rear Right', 'Rear Left'], color_discrete_sequence=px.colors.qualitative.Vivid)
        fig.update_layout(title='Linear Potentiometer Data', yaxis_title='mm', xaxis_title='Time', height=1080, width=1920)
        fig.show()
        # fig.write_image("saturday_linpot.png")

    def convert_xl_g(self):
        for i, row in self.xl_data.iterrows():
            self.xl_data.loc[i, "X"] = row["X"] * 0.5
            self.xl_data.loc[i, "Y"] = row["Y"] * 0.5
            self.xl_data.loc[i, "Z"] = row["Z"] * 0.5


    def plot_analog_xl(self):
        fig = px.line(self.xl_data, x='Time', y=["X", "Y", "Z"])
        # fig.update_layout(title='Linear Potentiometer Data', yaxis_title='mm', xaxis_title='Time', height=1080, width=1920)
        fig.show()

    def cluster(self):
        kmeans = KMeans(n_clusters=20)
        predictions = kmeans.fit(self.data)
        

if __name__ == '__main__':
    linpot = LinpotAnalysis('output2_linpot_2023-10-14_18-28-08.csv', "output2_analog_2023-10-14_18-28-08.csv")
    linpot.convert_voltage_to_mm()
    linpot.convert_xl_g()
    linpot.convert_time(linpot.data)
    linpot.convert_time(linpot.xl_data)
    linpot.plot()
    linpot.plot_analog_xl()
