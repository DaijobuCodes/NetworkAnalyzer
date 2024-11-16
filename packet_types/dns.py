def process_dns_packet(packet):
    """
    Process DNS packet and extract important fields.

    Args:
        packet: Captured packet object.

    Returns:
        dict: Dictionary containing DNS packet information.
    """
    return {
        "Protocol": "DNS",
        "Transaction ID": packet.dns.id,
        "Query Name": packet.dns.qry_name if hasattr(packet.dns, "qry_name") else None,
        "Query Type": packet.dns.qry_type if hasattr(packet.dns, "qry_type") else None,
        # "Response Code": packet.dns.flags_rcode,
        "Answer Count": packet.dns.count_answers
    }
