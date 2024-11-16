def process_tls_packet(packet):
    """
    Processes a TLS packet and extracts relevant information.

    Args:
        packet (pyshark.packet): The packet to process.

    Returns:
        dict: A dictionary containing extracted TLS packet information.
    """
    packet_info = {"Protocol": "TLS"}

    # Check if IP layer exists before accessing IP attributes
    if hasattr(packet, 'ip'):
        packet_info["Source IP"] = packet.ip.src
        packet_info["Destination IP"] = packet.ip.dst
    else:
        packet_info["Source IP"] = "N/A"
        packet_info["Destination IP"] = "N/A"

    # Check if the packet has a TCP layer
    if hasattr(packet, 'tcp'):
        packet_info["Source Port"] = packet.tcp.srcport
        packet_info["Destination Port"] = packet.tcp.dstport
    else:
        packet_info["Source Port"] = "N/A"
        packet_info["Destination Port"] = "N/A"

    # Add TLS-specific fields if available
    if hasattr(packet, 'tls'):
        packet_info["Cipher Suite"] = getattr(packet.tls, "handshake_ciphersuite", "N/A")
    else:
        packet_info["Cipher Suite"] = "N/A"

    return packet_info
