def process_https_packet(packet):
    """
    Process HTTPS packet and extract important fields.

    Args:
        packet: Captured packet object.

    Returns:
        dict: Dictionary containing HTTPS packet information.
    """
    return {
        "Protocol": "HTTPS",
        "Source IP": packet.ip.src,
        "Destination IP": packet.ip.dst,
        "Source Port": packet.tcp.srcport,
        "Destination Port": packet.tcp.dstport
    }
