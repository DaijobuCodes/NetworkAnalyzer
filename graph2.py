import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime
import matplotlib.dates as mdates


def plot_packet_distribution(packet_counts):
    """
    Plots a stylized pie chart showing the distribution of packet types.

    Args:
        packet_counts (Counter): Counter with packet types as keys and their counts as values.
    """
    packet_types = list(packet_counts.keys())
    counts = list(packet_counts.values())
    colors = plt.cm.Paired(range(len(packet_types)))  # Use colormap for diverse colors

    plt.figure(figsize=(8, 8))
    wedges, texts, autotexts = plt.pie(
        counts, labels=packet_types, colors=colors, autopct='%1.1f%%', startangle=140,
        textprops=dict(color="black"), wedgeprops=dict(edgecolor='w', linewidth=1.5), pctdistance=0.85
    )

    # Add a center circle for a donut effect
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    plt.gca().add_artist(centre_circle)

    for text in texts:
        text.set_fontsize(10)
        text.set_weight('bold')

    for autotext in autotexts:
        autotext.set_fontsize(10)
        autotext.set_weight('bold')
        autotext.set_color('white')

    plt.title("Packet Type Distribution", fontsize=16, weight='bold')
    plt.show()


def plot_packet_time_series(timestamps):
    """
    Plots a stylized time-series line chart of packet counts over time.

    Args:
        timestamps (list): List of packet timestamps.
    """
    # Convert timestamps to minutes and count occurrences
    time_series = Counter(timestamps)
    sorted_times = sorted(time_series.keys())
    counts = [time_series[time] for time in sorted_times]

    # Plot the time series data
    plt.figure(figsize=(12, 6))
    plt.plot(sorted_times, counts, marker="o", color="#4c72b0", markersize=8, linewidth=2, linestyle='-', alpha=0.8)
    plt.fill_between(sorted_times, counts, color="#4c72b0", alpha=0.2)

    # Styling for axes and grid
    plt.xlabel("Time", fontsize=12, fontweight='bold')
    plt.ylabel("Packet Count", fontsize=12, fontweight='bold')
    plt.title("Packet Count Over Time", fontsize=16, fontweight='bold')
    plt.grid(color='grey', linestyle='--', linewidth=0.5, alpha=0.7)

    # Format x-axis with time
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.gcf().autofmt_xdate()

    # Highlight the peak point(s)
    peak_time = sorted_times[counts.index(max(counts))]
    peak_count = max(counts)
    plt.annotate(
        f'Peak: {peak_count}', xy=(peak_time, peak_count), xytext=(peak_time, peak_count + 5),
        arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5),
        fontsize=10, fontweight='bold', color="black"
    )

    plt.show()
