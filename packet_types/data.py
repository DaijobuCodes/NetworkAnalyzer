# packet_types/data.py
def process_data_packet(packet):
    """
    Process DATA packet and extract information.

    Args:
        packet: Captured packet object.

    Returns:
        dict: Dictionary containing DATA packet information.
    """
    packet_info = {"Protocol": "DATA"}

    # Check if 'data' layer is present
    if hasattr(packet, 'data'):
        # Attempt to access the data field safely
        try:
            packet_info["Data"] = packet.data.data[:100]  # Show only the first 100 characters
        except AttributeError:
            # If `data.data` attribute is missing, set to "N/A"
            packet_info["Data"] = "N/A"
    else:
        # If no 'data' layer, set field as "N/A"
        packet_info["Data"] = "N/A"

    return packet_info
