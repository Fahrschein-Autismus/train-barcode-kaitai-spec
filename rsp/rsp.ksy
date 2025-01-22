meta:
  id: barcode_rsp
  file-extension: bin
  encoding: "iso-8859-1"
  endian: le
seq:
  - id: magic
    type: str
    size: 2
    valid: 
      - [0x30, 0x36]
      - [0x30, 0x38]
    doc: "`06` or `08` are magic bytes identifying tickets issued in the UK."