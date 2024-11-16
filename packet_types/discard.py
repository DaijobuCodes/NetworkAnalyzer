# packet_types/discard.py
def process_discard_packet(packet):
    """
    Process DISCARD packet (if such a protocol is detected).

    Args:
        packet: Captured packet object.

    Returns:
        dict: Dictionary containing DISCARD packet information.
    """
    packet_info = {"Protocol": "DISCARD"}

    # Since DISCARD doesn't return data, keep fields minimal
    packet_info["Info"] = "Packet discarded (no payload)"

    return packet_info
