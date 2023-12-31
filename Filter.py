import pandas as pd
from scipy.signal import butter, filtfilt

class Filter:

    def average(data: pd.DataFrame, column: str, window_size: int) -> pd.DataFrame:
        data[column] = data[column].rolling(window_size).mean()

        return data

    def butter_lowpass_filter(data: pd.DataFrame, column: str, cutoff: float, fs: float, order: int) -> pd.DataFrame:
        nyq = 0.5 * fs
        normal_cutoff = cutoff / nyq
        b, a = butter(order, normal_cutoff, btype="low", analog=False)
        data[f"{column}_lowpass"] = filtfilt(b, a, data[column])

        return data
