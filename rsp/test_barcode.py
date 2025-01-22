import rsp.barcode_rsp_envelope as barcode_rsp_envelope
import rsp.barcode_rsp as barcode_rsp

import base26
import datetime
import hashlib
import json
import typing

class Certificate:
    issuer_id: str
    modulus: int
    modulus_len: int
    exponent: int
    valid_from: datetime.datetime
    valid_until: datetime.datetime

    def __init__(self, issuer_id, modulus, modulus_len, exponent, valid_from, valid_until):
        self.issuer_id = issuer_id
        self.modulus = modulus
        self.modulus_len = modulus_len
        self.exponent = exponent
        self.valid_from = valid_from
        self.valid_until = valid_until

    @classmethod
    def from_json(cls, data) -> "Certificate":
        modulus = bytes.fromhex(data["modulus_hex"])
        return cls(
            issuer_id=data["issuer_id"],
            modulus=int.from_bytes(modulus, "big"),
            modulus_len=len(modulus),
            exponent=int(data["public_exponent_hex"], 16),
            valid_from=datetime.datetime.fromisoformat(data["valid_from"]),
            valid_until=datetime.datetime.fromisoformat(data["valid_until"]),
        )


class CertificateStore:
    certificates: typing.Dict[str, typing.List[Certificate]]

    def __init__(self):
        self.certificates = {}

    def load_certificates(self):
        certificates = {}
        with open("rsp/keys.json", "r") as f:
            data = json.loads(f.read())
            for issuer, keys in data.items():
                keys = list(map(lambda k: Certificate.from_json(k), keys))
                certificates[issuer] = keys
        self.certificates = certificates

def ascii6(v: int):
    s = v
    out = ""
    while s != 0:
        out = chr((s & 0b111111) + 32) + out
        s >>= 6
        
    return out

def decrypt_with_cert(payload: bytes, cert: Certificate) -> typing.Optional[bytes]:
    h = int.from_bytes(payload, 'big')
    m = pow(h, cert.exponent, cert.modulus)
    data = m.to_bytes(cert.modulus_len, 'big')

    if data[0] != 0:
        return None

    if data[1] == 1:
        offset = 2
        while data[offset] == 0xFF:
            offset += 1
        if data[offset] == 0:
            data = data[offset+1:]
        else:
            return None
    elif data[1] == 2:
        offset = 2
        while data[offset] != 0x00:
            offset += 1
        data = data[offset+1:]
    else:
        return None

    data, message_hash = data[:-8], data[-8:]

    if hashlib.sha256(data).digest()[:8] != message_hash:
        raise Exception("Invalid message integrity hash")

    return data


b = barcode_rsp_envelope.BarcodeRspEnvelope.from_file("rsp/rsp2.bin")
print(b.magic)
print(b.ticket_ref)
print(b.issuer_id)
print(b.unknown_data)
print(b.payload)

cert_store = CertificateStore()
cert_store.load_certificates()
pre_payload = base26.decode(b.payload)

for cert in cert_store.certificates[b.issuer_id]:
    try:
        payload = decrypt_with_cert(pre_payload, cert)
        break
    except: 
        print(f"cert {cert.modulus} not working, moving on...")

f = open('rsp/rsp_payload.bin', 'wb')
f.write(payload)
f.close()
c = barcode_rsp.BarcodeRsp.from_bytes(payload)
print("Manual Inspection", c.manual_inspection_required)
#print(c.unknown_data_1)
print(ascii6(c.ticket_ref), b.ticket_ref)
print("Checksum", ascii6(c.checksum_char))
print("Version Number", c.version_number)
print("Standard Class", c.is_ticket_standard_class)
print("Lennon", ascii6(c.lennon_type_ticket))
print("Fare", ascii6(c.fare_label))
print("Start", ascii6(c.origin))
print("End", ascii6(c.destination))
print("Retailer", ascii6(c.retailer))
print("Child?", c.is_child_ticket)
print("Coupon type", c.coupon_type)
print("Discount Code", c.discount_code)
print("Route Code", c.route_code)
print("Date", datetime.datetime(1997,1,1)+ datetime.timedelta(days=c.departure_date, seconds=c.departure_time))
print("Time Flag", c.departure_time_flag)
print("Passenger ID", c.passenger_id)
print("Passenger Name", ascii6(c.passenger_name))
print("Passenger Gender", c.passenger_gender)
print("Restriction", ascii6(c.restriction))
print("Bidir", c.is_bidirectional)
print("Lim Dur Code", c.limited_duration_code)
print("Is Ext", c.is_free_text_extended)
print("Is Full Ticket", c.is_full_ticket)
print("Has free text", c.has_free_text)
print("Resas", c.num_reservations)

# if c.is_full_ticket:
print("Purchase Date", datetime.datetime(1997,1,1)+ datetime.timedelta(days=c.purchase_details.purchase_date, seconds=c.purchase_details.purchase_time))
print("Price", c.purchase_details.purchase_price)
print("Reference", ascii6(c.purchase_details.purchase_reference))
print("Validity", c.purchase_details.purchase_validity)

for r in range(c.num_reservations):
    print(f"Reservation {r+1}")
    print(f"{ascii6(c.reservations[r].reserved_service_id_chars)} {c.reservations[r].reserved_service_id_digits}")
    print(f"Coach {ascii6(c.reservations[r].reserved_coach)}")
    print(f"Seat {ascii6(c.reservations[r].reserved_seat_letter)} {c.reservations[r].reserved_seat_number}")