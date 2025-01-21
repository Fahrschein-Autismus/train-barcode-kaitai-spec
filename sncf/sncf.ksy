meta:
  id: barcode_sncf
  file-extension: bin
  encoding: "iso-8859-1"
  endian: le
seq:
  - id: magic
    contents: [0x69, 0x30, 0x43, 0x56]
    doc: "`i0CV` are the four magic bytes identifying tickets issued by SNCF."
  - id: passenger_name_record
    type: str
    size: 6
    doc: "Passenger Name Record (assumedly)"
  - id: ticket_number
    type: str
    size: 9
    doc: ""
  - id: unknown
    contents: [0x31, 0x32, 0x31, 0x31]
    doc: "Unknown"
  - id: traveller_dob
    type: str
    size: 10
    doc: "Traveller Date of Birth (format: `%d/%m/%Y`)"
  - id: departure_station
    type: str
    size: 5
    doc: ""
  - id: arrival_station
    type: str
    size: 5
    doc: ""
  - id: train_number
    type: str
    size: 5
    doc: ""
  - id: travel_date
    type: str
    size: 5
    doc: "Date (format: `%d/%m`)"
  - id: traveller_sncf_id
    type: str
    size: 19
    doc: ""
  - id: traveller_surname
    type: str
    size: 19
    doc: ""
  - id: traveller_forename
    type: str
    size: 19
    doc: ""
  - id: travel_class
    type: str
    size: 1
    doc: ""
  - id: tariff_code
    type: str
    size: 4
    doc: ""
  - id: travel_class_return
    type: str
    size: 1
    doc: ""
  - id: departure_station_return
    type: str
    size: 5
    doc: ""
  - id: arrival_station_return
    type: str
    size: 5
    doc: ""
  - id: train_number_return
    type: str
    size: 5
    doc: ""