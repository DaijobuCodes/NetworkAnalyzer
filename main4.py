import pyshark
import csv
from packet_classifier import classify_packet
from display import display_packet_info
from graph2 import plot_packet_distribution, plot_packet_time_series
from collections import Counter
from datetime import datetime
import matplotlib.pyplot as plt
import pygeoip
import ipaddress

gi = pygeoip.GeoIP('GeoLiteCity.dat')
myip = "106.213.87.186"


def is_valid_ip(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        return ip_obj.is_global  # Only allow public IPs
    except ValueError:
        return False


def generate_kml_entry(src_ip, dst_ip):
    # Replace invalid or non-public source IP with your public IP
    if not is_valid_ip(src_ip):
        print(f"Invalid or non-public source IP {src_ip}. Replacing with {myip}.")
        src_ip = myip

    # Validate destination IP
    if not is_valid_ip(dst_ip):
        print(f"Invalid or non-public destination IP {dst_ip}. Skipping.")
        return ''

    src_record = gi.record_by_name(src_ip)
    dst_record = gi.record_by_name(dst_ip)

    if not src_record or not dst_record:
        print(f"GeoIP lookup failed for src: {src_ip} or dst: {dst_ip}")
        return ''

    try:
        src_lat = src_record.get('latitude')
        src_lon = src_record.get('longitude')
        dst_lat = dst_record.get('latitude')
        dst_lon = dst_record.get('longitude')

        if not (src_lat and src_lon and dst_lat and dst_lon):
            print(f"Coordinates missing for src: {src_ip} or dst: {dst_ip}")
            return ''

        kml_entry = (
                        '<Placemark>\n'
                        '<name>%s to %s</name>\n'
                        '<extrude>1</extrude>\n'
                        '<tessellate>1</tessellate>\n'
                        '<styleUrl>#transBluePoly</styleUrl>\n'
                        '<LineString>\n'
                        '<coordinates>%6f,%6f\n%6f,%6f</coordinates>\n'
                        '</LineString>\n'
                        '</Placemark>\n'
                    ) % (src_ip, dst_ip, src_lon, src_lat, dst_lon, dst_lat)

        return kml_entry
    except Exception as e:
        print(f"Error generating KML for IP {dst_ip}: {e}")
        return ''


def write_to_master_csv(packet_info, csv_filename):


    packet_info_with_timestamp = {"Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), **packet_info}


    with open(csv_filename, mode='a', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=packet_info_with_timestamp.keys())
        if csv_file.tell() == 0:
            writer.writeheader()
        writer.writerow(packet_info_with_timestamp)


def write_to_protocol_csv(packet_info, protocol):

    filename = f"{protocol}_packets.csv"

    packet_info_with_timestamp = {"Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), **packet_info}

    with open(filename, mode='a', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=packet_info_with_timestamp.keys())
        if csv_file.tell() == 0:
            writer.writeheader()
        writer.writerow(packet_info_with_timestamp)


def packet_callback(packet, packet_counts, timestamps, master_csv_filename, kml_filename):
    packet_info = classify_packet(packet)
    if packet_info:
        display_packet_info(packet_info)

        # Update packet counts and timestamps
        packet_counts[packet_info["Protocol"]] += 1
        timestamps.append(datetime.now())

        # Write packet information to the master CSV and protocol-specific CSV
        write_to_master_csv(packet_info, master_csv_filename)
        write_to_protocol_csv(packet_info, packet_info["Protocol"])

        # Generate KML entry for the packet's IPs
        src_ip = packet_info.get("Source IP")
        dst_ip = packet_info.get("Destination IP")
        if src_ip and dst_ip:
            kml_entry = generate_kml_entry(src_ip, dst_ip)
            if kml_entry:
                with open(kml_filename, 'a') as kml_file:
                    kml_file.write(kml_entry)



def capture_live_packets(interface, packet_count, master_csv_filename, kml_filename):
    """
    Capture live packets from the specified network interface.

    Args:
        interface (str): The network interface to capture packets from.
        packet_count (int): Number of packets to capture.
        master_csv_filename (str): The name of the master CSV file.
    """
    packet_counts = Counter()
    timestamps = []

    capture = pyshark.LiveCapture(interface=interface)
    print(f"Capturing packets from interface {interface}...")
    # Capture packets continuously with a packet limit
    for packet in capture.sniff_continuously(packet_count=packet_count):
        packet_callback(packet, packet_counts, timestamps, master_csv_filename, kml_filename)

    # Plot only after capturing all packets
    plot_packet_distribution(packet_counts)
    plot_packet_time_series(timestamps)
    plt.show()


def capture_from_file(pcap_file, master_csv_filename, kml_filename):
    """
    Load packets from a PCAP file.

    Args:
        pcap_file (str): Path to the PCAP file.
        master_csv_filename (str): The name of the master CSV file.

    Returns:
        list: List of packets from the PCAP file.
    """
    capture = pyshark.FileCapture(f"pcaps/{pcap_file}")
    print(f"Reading packets from file {pcap_file}...")
    return capture


def main():
    master_csv_filename = "all_packets.csv"  # Master CSV file for all packets
    kml_filename = "output.kml"  # KML file for geographic data

    # Initialize the KML file with header
    with open(kml_filename, 'w') as kml_file:
        kml_file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        kml_file.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
        kml_file.write('<Document>\n')
        kml_file.write('<Style id="transBluePoly">\n')
        kml_file.write('<LineStyle>\n<width>1.5</width>\n<color>501400E6</color>\n</LineStyle>\n')
        kml_file.write('</Style>\n')

    choice = input("Choose capture mode:\n1. Live capture\n2. Analyze PCAP file\nEnter choice (1 or 2): ")

    if choice == "1":
        interface = input("Enter the network interface to capture from (e.g., 'eth0', 'wlan0'): ")
        packet_count = int(input("Enter the number of packets to capture: "))
        capture_live_packets(interface, packet_count, master_csv_filename, kml_filename)

    elif choice == "2":
        pcap_file = input("Enter the path to the PCAP file: ")
        packets = capture_from_file(pcap_file, master_csv_filename, kml_filename)

        packet_counts = Counter()
        timestamps = []

        # Process each packet from file
        for packet in packets:
            packet_callback(packet, packet_counts, timestamps, master_csv_filename, kml_filename)

        # Plot only after processing all packets
        plot_packet_distribution(packet_counts)
        plot_packet_time_series(timestamps)
        plt.show()

    else:
        print("Invalid choice. Exiting.")
        return

    # Close the KML file with footer
    with open(kml_filename, 'a') as kml_file:
        kml_file.write('</Document>\n</kml>\n')

    print(f"\nKML document saved as {kml_filename}.")
    print("You can use your generated KML file in Google My Maps.")
    print("Go to https://www.google.com/maps/d/, create a new map, and import your output.kml file.")



if __name__ == "__main__":
    main()
