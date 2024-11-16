def display_packet_info(packet_info):
    """
    Display the information extracted from a packet.

    Args:
        packet_info (dict): Dictionary containing packet information.
    """
    print("\n--- Packet Information ---")
    for key, value in packet_info.items():
        print(f"{key}: {value}")
