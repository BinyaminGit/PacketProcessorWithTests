# Simulates a network packet processor

def checksum(packet):
    """Calculate the checksum of a given packet."""
    return sum(packet)

def encrypt(packet, key):
    """Encrypts the packet using XOR with a given key."""
    return [x ^ key for x in packet]

def decrypt(packet, key):
    """Decrypts the packet using XOR with a given key."""
    return [x ^ key for x in packet]

def validate(packet):
    """Validates if all values in the packet are non-negative."""
    return all(x >= 0 for x in packet)

def drop_invalid_packets(packet_list):
    """Drops packets that do not validate."""
    return [p for p in packet_list if validate(p)]

def add_headers(packet, headers):
    """Adds headers to the packet."""
    return headers + packet

def remove_headers(packet, header_length):
    """Removes headers from the packet."""
    return packet[header_length:]
