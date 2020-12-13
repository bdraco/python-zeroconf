import socket
from zeroconf import (
    DNSPointer,
    DNSService,
    DNSText,
    DNSAddress,
    DNSIncoming,
    DNSOutgoing,
    _TYPE_TXT,
    _FLAGS_QR_RESPONSE,
    _TYPE_A,
    _DNS_HOST_TTL,
    _FLAGS_AA,
    _CLASS_UNIQUE,
    _TYPE_SRV,
    _TYPE_PTR,
    _CLASS_IN,
    _DNS_OTHER_TTL,
)

out = DNSOutgoing(_FLAGS_QR_RESPONSE | _FLAGS_AA)

service_type = '_hap._tcp.local.'

address = socket.inet_pton(socket.AF_INET, "192.168.208.5")

RECORDS = [
    {
        "name": "HASS Bridge ZJWH FF5137._hap._tcp.local.",
        "address": address,
        "port": 51832,
        "text": b'\x13md=HASS Bridge ZJWH\x06pv=1.0\x14id=01:6B:30:FF:51:37\x05c#=12\x04s#=1\x04ff=0\x04ci=2\x04sf=0\x0bsh=L0m/aQ==',
    },
    {
        "name": "HASS Bridge 3K9A C2582A._hap._tcp.local.",
        "address": address,
        "port": 51834,
        "text": b'\x13md=HASS Bridge 3K9A\x06pv=1.0\x14id=E2:AA:5B:C2:58:2A\x05c#=12\x04s#=1\x04ff=0\x04ci=2\x04sf=0\x0bsh=b2CnzQ==',
    },
    {
        "name": "Master Bed TV CEDB27._hap._tcp.local.",
        "address": address,
        "port": 51830,
        "text": b'\x10md=Master Bed TV\x06pv=1.0\x14id=9E:B7:44:CE:DB:27\x05c#=18\x04s#=1\x04ff=0\x05ci=31\x04sf=0\x0bsh=CVj1kw==',
    },
    {
        "name": "Living Room TV 921B77._hap._tcp.local.",
        "address": address,
        "port": 51833,
        "text": b'\x11md=Living Room TV\x06pv=1.0\x14id=11:61:E7:92:1B:77\x05c#=17\x04s#=1\x04ff=0\x05ci=31\x04sf=0\x0bsh=qU77SQ==',
    },
    {
        "name": "HASS Bridge ZC8X FF413D._hap._tcp.local.",
        "address": address,
        "port": 51829,
        "text": b'\x13md=HASS Bridge ZC8X\x06pv=1.0\x14id=96:14:45:FF:41:3D\x05c#=12\x04s#=1\x04ff=0\x04ci=2\x04sf=0\x0bsh=b0QZlg==',
    },
    {
        "name": "HASS Bridge WLTF 4BE61F._hap._tcp.local.",
        "address": address,
        "port": 51837,
        "text": b'\x13md=HASS Bridge WLTF\x06pv=1.0\x14id=E0:E7:98:4B:E6:1F\x04c#=2\x04s#=1\x04ff=0\x04ci=2\x04sf=0\x0bsh=ahAISA==',
    },
    {
        "name": "FrontdoorCamera 8941D1._hap._tcp.local.",
        "address": address,
        "port": 54898,
        "text": b'\x12md=FrontdoorCamera\x06pv=1.0\x14id=9F:B7:DC:89:41:D1\x04c#=2\x04s#=1\x04ff=0\x04ci=2\x04sf=0\x0bsh=0+MXmA==',
    },
    {
        "name": "HASS Bridge W9DN 5B5CC5._hap._tcp.local.",
        "address": address,
        "port": 51836,
        "text": b'\x13md=HASS Bridge W9DN\x06pv=1.0\x14id=11:8E:DB:5B:5C:C5\x05c#=12\x04s#=1\x04ff=0\x04ci=2\x04sf=0\x0bsh=6fLM5A==',
    },
    {
        "name": "HASS Bridge Y9OO EFF0A7._hap._tcp.local.",
        "address": address,
        "port": 51838,
        "text": b'\x13md=HASS Bridge Y9OO\x06pv=1.0\x14id=D3:FE:98:EF:F0:A7\x04c#=2\x04s#=1\x04ff=0\x04ci=2\x04sf=0\x0bsh=u3bdfw==',
    },
    {
        "name": "Snooze Room TV 6B89B0._hap._tcp.local.",
        "address": address,
        "port": 51835,
        "text": b'\x11md=Snooze Room TV\x06pv=1.0\x14id=5F:D5:70:6B:89:B0\x05c#=17\x04s#=1\x04ff=0\x05ci=31\x04sf=0\x0bsh=xNTqsg==',
    },
    {
        "name": "AlexanderHomeAssistant 74651D._hap._tcp.local.",
        "address": address,
        "port": 54811,
        "text": b'\x19md=AlexanderHomeAssistant\x06pv=1.0\x14id=59:8A:0B:74:65:1D\x05c#=14\x04s#=1\x04ff=0\x04ci=2\x04sf=0\x0bsh=ccZLPA==',
    },
    {
        "name": "HASS Bridge OS95 39C053._hap._tcp.local.",
        "address": address,
        "port": 51831,
        "text": b'\x13md=HASS Bridge OS95\x06pv=1.0\x14id=7E:8C:E6:39:C0:53\x05c#=12\x04s#=1\x04ff=0\x04ci=2\x04sf=0\x0bsh=Xfe5LQ==',
    },
]

for record in RECORDS:
    out.add_answer_at_time(DNSPointer(service_type, _TYPE_PTR, _CLASS_IN, _DNS_OTHER_TTL, record["name"]), 0)
    out.add_additional_answer(
        DNSService(
            record["name"],
            _TYPE_SRV,
            _CLASS_IN | _CLASS_UNIQUE,
            _DNS_HOST_TTL,
            0,
            0,
            record["port"],
            record["name"],
        )
    )
    out.add_additional_answer(
        DNSText(
            record["name"],
            _TYPE_TXT,
            _CLASS_IN | _CLASS_UNIQUE,
            _DNS_OTHER_TTL,
            record["text"],
        )
    )
    out.add_additional_answer(
        DNSAddress(
            record["name"],
            _TYPE_A,
            _CLASS_IN | _CLASS_UNIQUE,
            _DNS_HOST_TTL,
            record["address"],
        )
    )

for i in range(0,5):
    for packet in out.packets():
        print(DNSIncoming(packet))


print (DNSIncoming(b'\x00\x00\x84\x00\x00\x00\x00\x01\x00\x00\x00\x1b\x17HASS Bridge WLTF 4BE61F\x04_hap\x04_tcp\x05local\x00\x00\x10\x80\x01\x00\x00\x11\x94\x00U\x13md=HASS Bridge WLTF\x06pv=1.0\x14id=E0:E7:98:4B:E6:1F\x04c#=2\x04s#=1\x04ff=0\x04ci=2\x04sf=0\x0bsh=HiZUhw==\x15Living Room TV 921B77\xc0$\x00!\x80\x01\x00\x00\x00x\x00\x08\x00\x00\x00\x00\xcay\xc0\x94\xc0\x94\x00\x10\x80\x01\x00\x00\x11\x94\x00U\x11md=Living Room TV\x06pv=1.0\x14id=11:61:E7:92:1B:77\x05c#=17\x04s#=1\x04ff=0\x05ci=31\x04sf=0\x0bsh=F2gJwg==\xc0\x94\x00\x01\x80\x01\x00\x00\x00x\x00\x04\xc0\xa8\xd0\x05\x15Snooze Room TV 6B89B0\xc0$\x00!\x80\x01\x00\x00\x00x\x00\x08\x00\x00\x00\x00\xca{\xc1/\xc1/\x00\x10\x80\x01\x00\x00\x11\x94\x00U\x11md=Snooze Room TV\x06pv=1.0\x14id=5F:D5:70:6B:89:B0\x05c#=17\x04s#=1\x04ff=0\x05ci=31\x04sf=0\x0bsh=9ixLPA==\xc1/\x00\x01\x80\x01\x00\x00\x00x\x00\x04\xc0\xa8\xd0\x05\x17HASS Bridge 3K9A C2582A\xc0$\x00!\x80\x01\x00\x00\x00x\x00\x08\x00\x00\x00\x00\xcaz\xc1\xca\xc1\xca\x00\x10\x80\x01\x00\x00\x11\x94\x00V\x13md=HASS Bridge 3K9A\x06pv=1.0\x14id=E2:AA:5B:C2:58:2A\x05c#=12\x04s#=1\x04ff=0\x04ci=2\x04sf=0\x0bsh=D3le0g==\xc1\xca\x00\x01\x80\x01\x00\x00\x00x\x00\x04\xc0\xa8\xd0\x05\x17HASS Bridge Y9OO EFF0A7\xc0$\x00!\x80\x01\x00\x00\x00x\x00\x08\x00\x00\x00\x00\xca~\xc2h\xc2h\x00\x10\x80\x01\x00\x00\x11\x94\x00U\x13md=HASS Bridge Y9OO\x06pv=1.0\x14id=D3:FE:98:EF:F0:A7\x04c#=2\x04s#=1\x04ff=0\x04ci=2\x04sf=0\x0bsh=JotcDA==\xc2h\x00\x01\x80\x01\x00\x00\x00x\x00\x04\xc0\xa8\xd0\x05\x14Master Bed TV CEDB27\xc0$\x00!\x80\x01\x00\x00\x00x\x00\x08\x00\x00\x00\x00\xcav\xc3\x05\xc3\x05\x00\x10\x80\x01\x00\x00\x11\x94\x00T\x10md=Master Bed TV\x06pv=1.0\x14id=9E:B7:44:CE:DB:27\x05c#=18\x04s#=1\x04ff=0\x05ci=31\x04sf=0\x0bsh=MhIepQ==\xc3\x05\x00\x01\x80\x01\x00\x00\x00x\x00\x04\xc0\xa8\xd0\x05\x17HASS Bridge OS95 39C053\xc0$\x00!\x80\x01\x00\x00\x00x\x00\x08\x00\x00\x00\x00\xcaw\xc3\x9e\xc3\x9e\x00\x10\x80\x01\x00\x00\x11\x94\x00V\x13md=HASS Bridge OS95\x06pv=1.0\x14id=7E:8C:E6:39:C0:53\x05c#=12\x04s#=1\x04ff=0\x04ci=2\x04sf=0\x0bsh=kOtNcA==\xc3\x9e\x00\x01\x80\x01\x00\x00\x00x\x00\x04\xc0\xa8\xd0\x05\x16FrontdoorCamera 8941D1\xc0$\x00!\x80\x01\x00\x00\x00x\x00\x08\x00\x00\x00\x00\xd6r\xc4<\xc4<\x00\x10\x80\x01\x00\x00\x11\x94\x00T\x12md=FrontdoorCamera\x06pv=1.0\x14id=9F:B7:DC:89:41:D1\x04c#=2\x04s#=1\x04ff=0\x04ci=2\x04sf=0\x0bsh=Pqrwug==\xc4<\x00\x01\x80\x01\x00\x00\x00x\x00\x04\xc0\xa8\xd0\x05\xc0\x0c\x00!\x80\x01\x00\x00\x00x\x00\x08\x00\x00\x00\x00\xca}\xc0\x0c\xc0\x0c\x00\x10\x80\x01\x00\x00\x11\x94\x00U\x13md=HASS Bridge WLTF\x06pv=1.0\x14id=E0:E7:98:4B:E6:1F\x04c#=2\x04s#=1\x04ff=0\x04ci=2\x04sf=0\x0bsh=HiZUhw==\xc0\x0c\x00\x01\x80\x01\x00\x00\x00x\x00\x04\xc0\xa8\xd0\x05\x1dAlexanderHomeAssistant 74651D\xc0$\x00!\x80\x01\x00\x00\x00x\x00\x08\x00\x00\x00\x00\xd6\x1b\xc5\\\xc5\\\x00\x01\x80\x01\x00\x00\x00x\x00\x04\xc0\xa8\xd0\x05\xc5\x9e\x00\x01\x80\x01\x00\x00\x00x\x00\x04\xc0\xa8\xd0\x05'))