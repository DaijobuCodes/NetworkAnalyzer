def process_tcp_packet(packet):
    """
    Process TCP packet and extract important fields.

    Args:
        packet: Captured packet object.

    Returns:
        dict: Dictionary containing TCP packet information.
    """

    packet_info = {"Protocol": "TCP"}

    if hasattr(packet, 'ip'):
        packet_info["Source IP"] = packet.ip.src
        packet_info["Destination IP"] = packet.ip.dst
    else:
        packet_info["Source IP"] = "N/A"
        packet_info["Destination IP"] = "N/A"

    if hasattr(packet, 'tcp'):
        packet_info["Source Port"] = packet.tcp.srcport
        packet_info["Destination Port"] = packet.tcp.dstport
        packet_info["Sequence Number"] = packet.tcp.seq
        packet_info["Acknowledgment Number"] = packet.tcp.ack
        packet_info["Window Size"] = packet.tcp.window_size

    return packet_info
