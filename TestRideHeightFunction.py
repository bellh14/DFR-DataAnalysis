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
    num_heaves = 500
    num_angles = 500
    inches_to_meters = 0.0254
    meters_to_inches = 39.37008
    heave_min = -1.2 * inches_to_meters
    heave_max = 0.5 * inches_to_meters
    angle_min = -1.3
    angle_max = 1.3
    heave_increment = (heave_max + abs(heave_min)) / (num_heaves - 1)
    angle_increment = (angle_max + abs(angle_min)) / (num_angles - 1)

    iteration = 0
    for i in range(0, num_heaves):
        for j in range(0, num_angles):
            # chassis_heave = np.round(self.HEAVE_MIN + (i * heave_increment), 5)
            #             FRH: 4.95+${chassisHeaveScalar}
            # RRH: 5.73+(69.76*sin(${Chassis Angle}))+${chassisHeaveScalar}
            chassis_heave = np.round(heave_min + (i * heave_increment), 5)
            chassis_angle = np.round(angle_min + (j * angle_increment), 5)
            frh = (0.12573 + chassis_heave) * meters_to_inches
            rrh = (
                0.145542
                + (1.771904 * np.sin(chassis_angle * (np.pi / 180)))
                + chassis_heave
            ) * meters_to_inches
            ride_height_combinations.loc[iteration, "Chassis Heave"] = (
                chassis_heave * meters_to_inches
            )
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
    print("FRH Min: ", df["FRH"].min())
    print("FRH Max: ", df["FRH"].max())
    print("RRH Min: ", df["RRH"].min())
    print("RRH Max: ", df["RRH"].max())


df = plot_ride_heights()
test_min_max(df)
