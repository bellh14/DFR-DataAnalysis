import pandas as pd
import plotly.express as px
import time


class AccelerometerAnalaysis:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.xl_data = pd.DataFrame(pd.read_csv(self.file_name))
        self.x_basis = self.xl_data.loc[0, "X Axis"]
        self.y_basis = self.xl_data.loc[0, "Y Axis"]
        self.z_basis = self.xl_data.loc[0, "Z Axis"]

    def convert_time(self, data):
        for i, row in data.iterrows():
            time_step = row["Time"]
            mlsec = repr(time_step).split(".")[1][:3]
            data.loc[i, "Time"] = time.strftime(
                "%H:%M:%S.{} %Z".format(mlsec), time.localtime(time_step)
            )

    def convert_xl_g(self):
        for i, row in self.xl_data.iterrows():
            self.xl_data.loc[i, "X"] = (row["X Axis"] - self.x_basis) * 0.53
            self.xl_data.loc[i, "Y"] = (row["Y Axis"] - self.y_basis) * 0.53
            self.xl_data.loc[i, "Z"] = (row["Z Axis"] - self.z_basis) * 0.53

    def plot_analog_xl(self, title: str = None):
        fig = px.line(
            self.xl_data,
            x="Time",
            y=["X Axis", "Y Axis", "Z Axis"],
            color_discrete_sequence=px.colors.qualitative.Vivid,
        )
        fig.update_layout(
            title=f"Accelerometer Data {title}",
            yaxis_title="g",
            xaxis_title="Time",
            height=1080,
            width=1920,
        )
        fig.show()
        fig.write_image(f"10-14/accelerometer_{title}.png")


if __name__ == "__main__":
    # will refactor later

    accel = AccelerometerAnalaysis("XL-NonProcess/xl1.csv_xl1_2023-11-17_16-03-07-run2.csv")
    accel.convert_time(accel.xl_data)
    # accel.convert_xl_g()
    accel.plot_analog_xl("Run 2")

    # accel = AccelerometerAnalaysis("output2_analog_2023-10-14_17-15-24.csv")
    # accel.convert_time(accel.xl_data)
    # accel.convert_xl_g()
    # accel.plot_analog_xl("150_Run_2")

    # accel = AccelerometerAnalaysis("output2_analog_2023-10-14_17-17-54.csv")
    # accel.convert_time(accel.xl_data)
    # accel.convert_xl_g()
    # accel.plot_analog_xl("150_Run_3")
