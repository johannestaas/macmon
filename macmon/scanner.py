'''
macmon.scanner
==============
'''
from datetime import datetime
from scapy.all import sniff, Dot11

SEEN_DEVICES = set()
PKT_HISTORY = []


def handle_packet(pkt):
    if not pkt.haslayer(Dot11):
        return
    if pkt.type == 0 and pkt.subtype == 8:
        if pkt.addr2 not in SEEN_DEVICES:
            SEEN_DEVICES.add(pkt.addr2)
            PKT_HISTORY.append((datetime.now(), pkt))
            print('AP MAC: {pkt.addr2} '
                  'with SSID: {pkt.info}'.format(pkt=pkt))


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--interface', '-i', default='mon0',
                        help='monitor mode enabled interface')
    args = parser.parse_args()
    sniff(iface=args.interface, prn=handle_packet)


if __name__ == '__main__':
    main()
