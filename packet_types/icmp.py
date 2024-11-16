def process_icmp_packet(packet):
    """
    Process ICMP packet and extract important fields.

    Args:
        packet: Captured packet object.

    Returns:
        dict: Dictionary containing ICMP packet information.
    """
    return {
        "Protocol": "ICMP",
        "Source IP": packet.ip.src,
        "Destination IP": packet.ip.dst,
        "Type": packet.icmp.type,
        "Code": packet.icmp.code,
        "Checksum": packet.icmp.checksum
    }
