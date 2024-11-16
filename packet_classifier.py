# packet_classifier.py
from packet_types.tcp import process_tcp_packet
from packet_types.udp import process_udp_packet
from packet_types.icmp import process_icmp_packet
from packet_types.arp import process_arp_packet
from packet_types.dns import process_dns_packet
from packet_types.dhcp import process_dhcp_packet
from packet_types.data import process_data_packet
from packet_types.tls import process_tls_packet
from packet_types.xmpp import process_xmpp_packet
from packet_types.discard import process_discard_packet


def classify_packet(packet):
    """
    Classifies a packet based on its type and extracts relevant data.

    Args:
        packet: Captured packet object.

    Returns:
        dict: Dictionary containing classified packet information.
    """
    # Check for each protocol in order

    if 'ICMP' in packet:
        return process_icmp_packet(packet)
    elif 'ARP' in packet:
        return process_arp_packet(packet)
    elif 'DNS' in packet:
        return process_dns_packet(packet)
    elif 'DHCP' in packet:  # DHCP protocol encapsulated as BOOTP in PyShark
        return process_dhcp_packet(packet)
    elif 'DATA' in packet:
        return process_data_packet(packet)
    elif 'TLS' in packet:
        return process_tls_packet(packet)
    elif 'XMPP' in packet:
        return process_xmpp_packet(packet)
    elif 'DISCARD' in packet:
        return process_discard_packet(packet)
    elif 'TCP' in packet:
        return process_tcp_packet(packet)
    elif 'UDP' in packet:
        return process_udp_packet(packet)
    else:
        # If packet does not match any known protocols
        print("Unrecognized protocol in packet")
        return {"Protocol": "Unknown"}
