import pandas as pd
import plotly.express as px
import time


class LinpotAnalysis:

    def __init__(self, file_name: str):
        self.file_name = file_name
        self.data = pd.DataFrame(pd.read_csv(self.file_name))

    def convert_voltage_to_mm(self):
        for i, row in self.data.iterrows():
            self.data.loc[i, 'Front Right'] = row['Front Right'] * 15.0
            self.data.loc[i, 'Front Left'] = row['Front Left'] * 15.0
            self.data.loc[i, 'Rear Right'] = row['Rear Right'] * 15.0
            self.data.loc[i, 'Rear Left'] = row['Rear Left'] * 15.0

    def convert_time(self):
        for i, row in self.data.iterrows():
            time_step = row['Time']
            mlsec = repr(time_step).split('.')[1][:3]
            self.data.loc[i, 'Time'] = time.strftime("%Y-%m-%d %H:%M:%S.{} %Z".format(mlsec), time.localtime(time_step))

    def plot(self):
        fig = px.line(self.data, x='Time', y=['Front Right', 'Front Left',
                                              'Rear Right', 'Rear Left'])
        fig.update_layout(title='Linear Potentiometer Data', yaxis_title='mm', xaxis_title='Time')
        fig.show()


if __name__ == '__main__':
    linpot = LinpotAnalysis('output1_linpot_4.csv')
    linpot.convert_voltage_to_mm()
    linpot.convert_time()
    linpot.plot()