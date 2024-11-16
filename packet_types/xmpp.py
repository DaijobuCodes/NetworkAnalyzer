# packet_types/xmpp.py
def process_xmpp_packet(packet):
    """
    Process XMPP packet and extract information.

    Args:
        packet: Captured packet object.

    Returns:
        dict: Dictionary containing XMPP packet information.
    """
    packet_info = {"Protocol": "XMPP"}

    # Check for fields in XMPP layer
    if hasattr(packet, 'xmpp'):
        # packet_info["Message Type"] = packet.xmpp.stanza_type
        # packet_info["Message From"] = packet.xmpp.from_jid
        # packet_info["Message To"] = packet.xmpp.to_jid
        packet_info["Source IP"] = packet.ip.src
        packet_info["Destination IP"] = packet.ip.dst
        packet_info["Source Port"] = packet.tcp.srcport
        packet_info["Destination Port"] = packet.tcp.dstport
    else:
        packet_info["Message Type"] = "N/A"
        packet_info["Message From"] = "N/A"
        packet_info["Message To"] = "N/A"

    return packet_info
