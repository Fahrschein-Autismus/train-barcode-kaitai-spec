# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class BarcodeSncf(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.magic = self._io.read_bytes(4)
        if not self.magic == b"\x69\x30\x43\x56":
            raise kaitaistruct.ValidationNotEqualError(b"\x69\x30\x43\x56", self.magic, self._io, u"/seq/0")
        self.passenger_name_record = (self._io.read_bytes(6)).decode(u"iso-8859-1")
        self.ticket_number = (self._io.read_bytes(9)).decode(u"iso-8859-1")
        self.unknown = self._io.read_bytes(4)
        if not self.unknown == b"\x31\x32\x31\x31":
            raise kaitaistruct.ValidationNotEqualError(b"\x31\x32\x31\x31", self.unknown, self._io, u"/seq/3")
        self.traveller_dob = (self._io.read_bytes(10)).decode(u"iso-8859-1")
        self.departure_station = (self._io.read_bytes(5)).decode(u"iso-8859-1")
        self.arrival_station = (self._io.read_bytes(5)).decode(u"iso-8859-1")
        self.train_number = (self._io.read_bytes(5)).decode(u"iso-8859-1")
        self.travel_date = (self._io.read_bytes(5)).decode(u"iso-8859-1")
        self.traveller_sncf_id = (self._io.read_bytes(19)).decode(u"iso-8859-1")
        self.traveller_surname = (self._io.read_bytes(19)).decode(u"iso-8859-1")
        self.traveller_forename = (self._io.read_bytes(19)).decode(u"iso-8859-1")
        self.travel_class = (self._io.read_bytes(1)).decode(u"iso-8859-1")
        self.tariff_code = (self._io.read_bytes(4)).decode(u"iso-8859-1")
        self.travel_class_return = (self._io.read_bytes(1)).decode(u"iso-8859-1")
        self.departure_station_return = (self._io.read_bytes(5)).decode(u"iso-8859-1")
        self.arrival_station_return = (self._io.read_bytes(5)).decode(u"iso-8859-1")
        self.train_number_return = (self._io.read_bytes(5)).decode(u"iso-8859-1")


