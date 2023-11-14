import pandas as pd
import plotly.express as px
import numpy as np

"""
FRH: 4.95+${chassisHeaveScalar} 
RRH: 5.73+(69.76*sin(${Chassis Angle}))+${chassisHeaveScalar}

Chassis heave: -0.5 to 1.5in
Chassis angle: -2 to 1 degree
"""


def plot_ride_heights():
    ride_height_combinations = pd.DataFrame(
        columns=["FRH", "RRH", "Chassis Angle", "Chassis Heave"]
    )
    num_heaves = 250
    num_angles = 250
    heave_increment = (0.5 + abs(-1.2)) / (num_heaves - 1)
    angle_increment = (1.3 + abs(-1.3)) / (num_angles - 1)
    iteration = 0
    for i in range(0, num_heaves):
        for j in range(0, num_angles):
            # chassis_heave = np.round(self.HEAVE_MIN + (i * heave_increment), 5)
            #             FRH: 4.95+${chassisHeaveScalar}
            # RRH: 5.73+(69.76*sin(${Chassis Angle}))+${chassisHeaveScalar}
            chassis_heave = np.round(-1.2 + (i * heave_increment), 5)
            chassis_angle = np.round(-1.3 + (j * angle_increment), 5)
            frh = 0.12573 + chassis_heave
            rrh = (
                0.145542
                + (1.771904 * np.sin(chassis_angle * (np.pi / 180)))
                + chassis_heave
            )
            ride_height_combinations.loc[iteration, "Chassis Heave"] = chassis_heave
            ride_height_combinations.loc[iteration, "Chassis Angle"] = chassis_angle

            ride_height_combinations.loc[iteration, "FRH"] = frh
            ride_height_combinations.loc[iteration, "RRH"] = rrh
            iteration += 1
    # print(ride_height_combinations)
    fig = px.scatter(ride_height_combinations, x="FRH", y="RRH")
    fig.show()
    ride_height_combinations.to_csv("Ride_Heights.csv", index=False)
    return ride_height_combinations


def test_min_max(df):
    print(df["FRH"].min())
    print(df["FRH"].max())
    print(df["RRH"].min())
    print(df["RRH"].max())


df = plot_ride_heights()
test_min_max(df)
