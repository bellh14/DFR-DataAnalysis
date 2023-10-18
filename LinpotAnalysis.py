import pandas as pd
import plotly.express as px
import time
from sklearn.cluster import KMeans


class LinpotAnalysis:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.data = pd.DataFrame(pd.read_csv(self.file_name))

    def convert_voltage_to_mm(self):
        for i, row in self.data.iterrows():
            self.data.loc[i, "Front Right"] = row["Front Right"] * 15.0
            self.data.loc[i, "Front Left"] = row["Front Left"] * 15.0
            self.data.loc[i, "Rear Right"] = row["Rear Right"] * 15.0
            self.data.loc[i, "Rear Left"] = row["Rear Left"] * 15.0

    def convert_time(self, data):
        for i, row in data.iterrows():
            time_step = row["Time"]
            mlsec = repr(time_step).split(".")[1][:3]
            data.loc[i, "Time"] = time.strftime(
                "%H:%M:%S.{} %Z".format(mlsec), time.localtime(time_step)
            )

    def plot(self, title: str = None):
        fig = px.line(
            self.data,
            x="Time",
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
        fig.show()
        fig.write_image(f"10-14/linpot_{title}.png")


if __name__ == "__main__":
    linpot = LinpotAnalysis(
        "output2_linpot_2023-10-14_13-23-28.csv",
    )
    linpot.convert_voltage_to_mm()
    linpot.convert_time(linpot.data)
    linpot.plot("200_Run_1")

    # linpot = LinpotAnalysis(
    #     "output2_linpot_2023-10-14_17-15-24.csv",
    # )
    # linpot.convert_voltage_to_mm()
    # linpot.convert_time(linpot.data)
    # linpot.plot("150_Run_2")

    # linpot = LinpotAnalysis(
    #     "output2_linpot_2023-10-14_17-17-54.csv",
    # )
    # linpot.convert_voltage_to_mm()
    # linpot.convert_time(linpot.data)
    # linpot.plot("150_Run_3")
