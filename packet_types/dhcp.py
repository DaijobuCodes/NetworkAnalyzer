# packet_types/dhcp.py
def process_dhcp_packet(packet):
    """
    Process DHCP (BOOTP) packet and extract important fields if available.

    Args:
        packet: Captured packet object.

    Returns:
        dict: Dictionary containing DHCP packet information.
    """
    packet_info = {"Protocol": "DHCP"}

    # Check if the 'bootp' layer exists in the packet
    if hasattr(packet, 'bootp'):
        packet_info["Transaction ID"] = packet.bootp.id
        packet_info["Client IP"] = packet.bootp.yiaddr
        packet_info["Your IP"] = packet.bootp.siaddr
        packet_info["Server IP"] = packet.bootp.giaddr
    else:
        # Log or handle the case where the bootp layer isn't found
        print("Warning: No BOOTP (DHCP) layer found in the packet.")
        packet_info["Transaction ID"] = "N/A"
        packet_info["Client IP"] = "N/A"
        packet_info["Your IP"] = "N/A"
        packet_info["Server IP"] = "N/A"

    return packet_info
