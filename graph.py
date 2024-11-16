import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime
import matplotlib.dates as mdates


def plot_packet_distribution(packet_counts):
    """
    Plots a bar chart of the packet type distribution.

    Args:
        packet_counts (Counter): Counter with packet types as keys and their counts as values.
    """
    packet_types = list(packet_counts.keys())
    counts = list(packet_counts.values())

    plt.figure(figsize=(10, 6))
    plt.bar(packet_types, counts, color="skyblue")
    plt.xlabel("Packet Type")
    plt.ylabel("Count")
    plt.title("Packet Type Distribution")
    plt.show()


def plot_packet_time_series(timestamps):
    """
    Plots a time-series line chart of packet counts over time.

    Args:
        timestamps (list): List of packet timestamps.
    """
    # Convert timestamps to minutes and count occurrences
    time_series = Counter(timestamps)
    sorted_times = sorted(time_series.keys())
    counts = [time_series[time] for time in sorted_times]

    # Plot the time series data
    plt.figure(figsize=(12, 6))
    plt.plot(sorted_times, counts, marker="o", color="steelblue")
    plt.xlabel("Time")
    plt.ylabel("Packet Count")
    plt.title("Packet Count Over Time")
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    plt.gcf().autofmt_xdate()
    plt.show()
