meta:
  id: barcode_rsp
  file-extension: bin
  encoding: "iso-8859-1"
  endian: be
seq:
  - id: manual_inspection_required
    type: b1
    doc: ""
  - id: unknown_data_1
    type: b7
    doc: ""
  - id: ticket_ref
    type: b54
    doc: ""
  - id: checksum_char
    type: b6
    doc: ""
  - id: version_number
    type: b4
    doc: ""
  - id: is_ticket_standard_class
    type: b1
    doc: ""
  - id: lennon_type_ticket
    type: b18
    doc: ""
  - id: fare_label
    type: b18
    doc: ""
  - id: origin
    type: b24
    doc: ""
  - id: destination
    type: b24
    doc: ""
  - id: retailer
    type: b24
    doc: ""
  - id: is_child_ticket
    type: b1
    doc: ""
  - id: coupon_type
    type: b2
    doc: ""
  - id: discount_code
    type: b10
    doc: ""
  - id: route_code
    type: b17
    doc: ""
  - id: departure_date
    type: b14
    doc: "1997-01-01"
  - id: departure_time
    type: b11
    doc: "seconds"
  - id: departure_time_flag
    type: b2
    doc: ""
  - id: passenger_id
    type: b17
    doc: ""
  - id: passenger_name
    type: b72
    doc: ""
  - id: passenger_gender
    type: b2
    doc: ""
  - id: restriction
    type: b18
    doc: ""
  - id: unknown_data_2
    type: b24
    doc: ""
  - id: unknown_data_3
    type: b1
    doc: ""
  - id: is_bidirectional
    type: b1
    doc: ""
  - id: unknown_data_4
    type: b6
    doc: ""
  - id: limited_duration_code
    type: b4
    doc: ""
  - id: is_free_text_extended
    type: b1
    doc: ""
  - id: is_full_ticket
    type: b1
    doc: ""
  - id: has_free_text
    type: b1
    doc: ""
  - id: num_reservations
    type: b4
    doc: ""
  - id: purchase_details
    type: purchase_details
    if: is_full_ticket
    doc: ""
  - id: reservations
    type: reservation
    repeat: expr
    repeat-expr: num_reservations


types:
  purchase_details:
    seq: 
      - id: purchase_date
        type: b14
        doc: ""
      - id: purchase_time
        type: b11
        doc: ""
      - id: purchase_price
        type: b21
        doc: ""
      - id: unknown_data_1
        type: b13
        doc: ""
      - id: purchase_reference
        type: b48
        doc: ""
      - id: purchase_validity
        type: b9
        doc: ""
      - id: unknown_data_2
        type: b6
        doc: ""
  reservation:
    seq:
      - id: reserved_service_id_chars
        type: b12
        doc: ""
      - id: reserved_service_id_digits
        type: b14
        doc: ""
      - id: reserved_coach
        type: b6
        doc: ""
      - id: reserved_seat_letter
        type: b6
        doc: ""
      - id: reserved_seat_number
        type: b7
        doc: ""