import pandas as pd
import plotly.express as px


class PitotTubeAnalysis:

    def __init__(self, file_name: str, folder_name: str):

        self.folder_name = folder_name
        self.file_name = file_name
        self.data = self.load_data()
        # self.clean_data()
        # self.print_corr()
        self.plot_data()

    def load_data(self):

        data = pd.DataFrame(pd.read_csv(f"{self.folder}/{self.file_name}"))

        return data

    def print_corr(self):

        corr = self.data.corr()

        print(corr)

    def convert_to_float(self):
        """Have to convert to float anyways so might as well do it
        manually to catch for value errors"""

        for i in range(len(self.data)):
            try:
                self.data.loc[i] = self.data.loc[i].astype(float)
            except ValueError:
                self.data.loc[i] = self.data.drop(i, inplace=True)

    def clean_data(self):

        self.convert_to_float()

        for i in range(len(self.data)):
            if self.data.loc[i, "Pressure"] > 1:
                self.data.drop(i, inplace=True)

        self.remove_repeats()
        # self.remove_probable_outliers()

    def remove_repeats(self):

        previous_pressure = self.data.loc[0, "Pressure"]

        for i, row in self.data.iterrows():
            if i == 1:
                continue

            if row["Pressure"] == previous_pressure:
                self.data.drop(i, inplace=True)

            previous_pressure = row["Pressure"]

        self.data.to_csv(f"{self.folder_name}/{self.file_name}", index=False)

    def remove_probable_outliers(self):

        previous_pressure = self.data.loc[0, "Pressure"]

        for i, row in self.data.iterrows():
            if i == 1:
                continue

            if row["Pressure"] == 0.01 and previous_pressure == 0:
                self.data.drop(i, inplace=True)

            previous_pressure = row["Pressure"]

        self.data.to_csv("new_cleaned_run1_data.csv", index=False)

    def plot_data(self):
        fig = px.scatter(self.data, x="Time(s)",
                         y="Pa to m/s", color="Pressure")
        fig.show()


if __name__ == "__main__":
    PitotTubeAnalysis("cleaned_run1_data_v3.csv", "pitot_tube_data")
