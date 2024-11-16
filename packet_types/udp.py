def process_udp_packet(packet):
    """
    Process UDP packet and extract important fields.

    Args:
        packet: Captured packet object.

    Returns:
        dict: Dictionary containing UDP packet information, or None if the required layers are missing.
    """
    # Check if both IP and UDP layers are in the packet
    if 'IP' in packet and 'UDP' in packet:
        return {
            "Protocol": "UDP",
            "Source IP": packet.ip.src,
            "Destination IP": packet.ip.dst,
            "Source Port": packet.udp.srcport,
            "Destination Port": packet.udp.dstport,
            "Length": packet.udp.length
        }
    else:
        # print("Packet does not contain the required IP and UDP layers.")
        return None
