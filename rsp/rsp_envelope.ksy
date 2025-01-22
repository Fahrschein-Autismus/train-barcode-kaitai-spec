meta:
  id: barcode_rsp_envelope
  file-extension: bin
  encoding: "iso-8859-1"
  endian: le
seq:
  - id: magic
    type: str
    size: 2
    valid: 
      expr: |
        _ == "06" ? true : _ == "08" ? true : false
    doc: "`06` or `08` are magic bytes identifying RSP tickets issued in the UK."
  - id: ticket_ref
    type: str
    size: 9
    doc: ""
  - id: unknown_data
    type: str
    size: 2
    doc: ""
  - id: issuer_id
    type: str
    size: 2
    doc: ""
  - id: payload
    type: str
    size-eos: true
    doc: "base26 encoded encrypted payload"