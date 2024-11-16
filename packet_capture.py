import pyshark


def capture_packets(interface=None, packet_count=100):
    """
    Capture packets on a specific interface or from a file.

    Args:
        interface (str): Interface to capture packets on.
        packet_count (int): Number of packets to capture.

    Returns:
        list: List of captured packets.
    """
    capture = pyshark.LiveCapture(interface=interface)
    capture.sniff(packet_count=packet_count)
    return capture
