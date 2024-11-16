def process_arp_packet(packet):
    """
    Process ARP packet and extract important fields.

    Args:
        packet: Captured packet object.

    Returns:
        dict: Dictionary containing ARP packet information.
    """
    return {
        "Protocol": "ARP",
        "Sender IP": packet.arp.src_proto_ipv4,
        "Sender MAC": packet.arp.src_hw_mac,
        "Target IP": packet.arp.dst_proto_ipv4,
        "Target MAC": packet.arp.dst_hw_mac,
        "Opcode": packet.arp.opcode
    }
