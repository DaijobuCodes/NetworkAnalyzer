def process_http_packet(packet):
    """
    Process HTTP packet and extract important fields.

    Args:
        packet: Captured packet object.

    Returns:
        dict: Dictionary containing HTTP packet information.
    """
    return {
        "Protocol": "HTTP",
        "Request Method": packet.http.request_method if hasattr(packet.http, "request_method") else None,
        "Request URI": packet.http.request_uri if hasattr(packet.http, "request_uri") else None,
        "Response Code": packet.http.response_code if hasattr(packet.http, "response_code") else None,
        "Content Type": packet.http.content_type if hasattr(packet.http, "content_type") else None
    }
