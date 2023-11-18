import pandas as pd
import plotly.express as px
import time
from sklearn.cluster import KMeans
from Filter import Filter


class LinpotAnalysis:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.data = pd.DataFrame(pd.read_csv(self.file_name))
        self.switch_columns()

    def switch_columns(self):
        self.data = self.data.rename(
            columns={
                "Front Right": "Front Left",
                "Front Left": "Rear Left",
                "Rear Left": "Front Right",
            }
        )

    def convert_voltage_to_mm(self):
        for i, row in self.data.iterrows():
            self.data.loc[i, "Front Right"] = -(row["Front Right"] * 15.0) + 75.0
            self.data.loc[i, "Front Left"] = -(row["Front Left"] * 15.0) + 75.0
            self.data.loc[i, "Rear Right"] = -(row["Rear Right"] * 15.0) + 75.0
            self.data.loc[i, "Rear Left"] = -(row["Rear Left"] * 15.0) + 75.0

    def convert_time(self, data):
        for i, row in data.iterrows():
            time_step = row["Time"]
            mlsec = repr(time_step).split(".")[1][:3]
            data.loc[i, "Time"] = time.strftime(
                "%H:%M:%S.{} %Z".format(mlsec), time.localtime(time_step)
            )

    def clean_data(self):
        # self.data = Filter.average(self.data, "Front Right", 25)
        # self.data = Filter.average(self.data, "Front Left", 25)
        # self.data = Filter.average(self.data, "Rear Right", 25)
        # self.data = Filter.average(self.data, "Rear Left", 25)
        self.data = Filter.butter_lowpass_filter(self.data, "Front Right", 4, 30, 2)
        self.data = Filter.butter_lowpass_filter(self.data, "Front Left", 4, 30, 2)
        self.data = Filter.butter_lowpass_filter(self.data, "Rear Right", 4, 30, 2)
        self.data = Filter.butter_lowpass_filter(self.data, "Rear Left", 4, 30, 2)

    def plot(self, title: str = None):
        fig = px.line(
            self.data,
            x="Time",
            # y=[
            #     "Front Right_lowpass",
            #     "Front Left_lowpass",
            #     "Rear Right_lowpass",
            #     "Rear Left_lowpass",
            # ],
            y=["Front Right", "Front Left", "Rear Right", "Rear Left"],
            color_discrete_sequence=px.colors.qualitative.Vivid,
        )

        fig.update_layout(
            title=f"Linear Potentiometer Data {title}",
            yaxis_title="mm",
            xaxis_title="Time",
            height=1080,
            width=1920,
        )
        # fig.show()
        fig.write_image(f"10-18/Unfiltered/linpot_{title}.png")


if __name__ == "__main__":
    linpot = LinpotAnalysis(
        "LinPot-Processed/output2_linpot_2023-11-17_15-57-58-warm.csv",
    )
    linpot.convert_voltage_to_mm()
    linpot.convert_time(linpot.data)
    # linpot.clean_data()
    linpot.plot("Run Warm")

    linpot = LinpotAnalysis(
        "LinPot-Processed/output2_linpot_2023-11-17_16-00-28-run1.csv",
    )
    linpot.convert_voltage_to_mm()
    linpot.convert_time(linpot.data)
    # linpot.clean_data()
    linpot.plot("Run 1")

    linpot = LinpotAnalysis(
        "LinPot-Processed/output2_linpot_2023-11-17_16-03-07-run2.csv",
    )
    linpot.convert_voltage_to_mm()
    linpot.convert_time(linpot.data)
    # linpot.clean_data()
    linpot.plot("Run 2")

    linpot = LinpotAnalysis(
        "LinPot-Processed/output2_linpot_2023-11-17_16-09-26-run3.csv",
    )
    linpot.convert_voltage_to_mm()
    linpot.convert_time(linpot.data)
    # linpot.clean_data()
    linpot.plot("Run 3")

    linpot = LinpotAnalysis(
        "LinPot-Processed/output2_linpot_2023-11-17_16-12-19-run4.csv",
    )
    linpot.convert_voltage_to_mm()
    linpot.convert_time(linpot.data)
    # linpot.clean_data()
    linpot.plot("Run 4")

    linpot = LinpotAnalysis(
        "LinPot-Processed/output2_linpot_2023-11-17_16-14-15-run5.csv",
    )
    linpot.convert_voltage_to_mm()
    linpot.convert_time(linpot.data)
    # linpot.clean_data()
    linpot.plot("Run 5")


    linpot = LinpotAnalysis(
        "LinPot-Processed/output2_linpot_2023-11-17_14-53-29.csv",
    )
    linpot.convert_voltage_to_mm()
    linpot.convert_time(linpot.data)
    # linpot.clean_data()
    linpot.plot("Run 6")

    linpot = LinpotAnalysis(
        "LinPot-Processed/output2_linpot_2023-11-17_14-55-33.csv",
    )
    linpot.convert_voltage_to_mm()
    linpot.convert_time(linpot.data)
    # linpot.clean_data()
    linpot.plot("Run 7")

    linpot = LinpotAnalysis(
        "LinPot-Processed/output2_linpot_2023-11-17_15-08-09.csv",
    )
    linpot.convert_voltage_to_mm()
    linpot.convert_time(linpot.data)
    # linpot.clean_data()
    linpot.plot("Run 8")

    linpot = LinpotAnalysis(
        "LinPot-Processed/output2_linpot_2023-11-17_15-15-30.csv",
    )
    linpot.convert_voltage_to_mm()
    linpot.convert_time(linpot.data)
    # linpot.clean_data()
    linpot.plot("Run 9")

    linpot = LinpotAnalysis(
        "LinPot-Processed/output2_linpot_2023-11-17_15-17-09.csv",
    )
    linpot.convert_voltage_to_mm()
    linpot.convert_time(linpot.data)
    # linpot.clean_data()
    linpot.plot("Run 10")

    linpot = LinpotAnalysis(
        "LinPot-Processed/output2_linpot_2023-11-17_15-22-27.csv",
    )
    linpot.convert_voltage_to_mm()
    linpot.convert_time(linpot.data)
    # linpot.clean_data()
    linpot.plot("Run 11")

    linpot = LinpotAnalysis(
        "LinPot-Processed/output2_linpot_2023-11-17_15-23-13.csv",
    )
    linpot.convert_voltage_to_mm()
    linpot.convert_time(linpot.data)
    # linpot.clean_data()
    linpot.plot("Run 12")