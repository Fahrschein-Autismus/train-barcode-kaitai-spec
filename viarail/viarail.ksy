meta:
  id: viarail
  file-extension: bin

seq:
  - id: ticketnumber
    size: 13
    type: str
    encoding: UTF-8
  - id: surname
    size: 30
    type: str
    encoding: UTF-8
  - id: car
    size: 4
    type: str
    encoding: UTF-8
  - id: seat
    size: 3
    type: str
    encoding: UTF-8
  - id: departure_station
    size: 4
    type: str
    encoding: UTF-8
  - id: arrival_station
    size: 4
    type: str
    encoding: UTF-8
  - id: train
    size: 7
    type: str
    encoding: UTF-8
  - id: departure_time
    type: datetime_short
  - id: name
    size: 20
    type: str
    encoding: UTF-8
  - id: loyalty_level
    doc: P1/P2/P3 (P1 is lowest)
    size: 2
    type: str
    encoding: UTF-8
  - id: inventory_class
    size: 2
    type: str
    encoding: UTF-8
  - id: passenger_type
    size: 3
    type: str
    encoding: UTF-8
    doc: 'Observed values: ADT/YTH/SEN(ior)/CHD/INF(ant)/TUR (Group escort (free))'
  - id: pnr
    size: 6
    type: str
    encoding: UTF-8
  - id: purchase_time
    type: datetime_long
    
types:
  datetime_short:
    seq:
      - id: year
        size: 4
        type: str
        encoding: UTF-8
      - id: month
        size: 2
        type: str
        encoding: UTF-8
      - id: day
        size: 2
        type: str
        encoding: UTF-8
      - id: hour
        size: 2
        type: str
        encoding: UTF-8
      - id: minute
        size: 2
        type: str
        encoding: UTF-8
  datetime_long:
    seq:
      - id: year
        size: 4
        type: str
        encoding: UTF-8
      - id: month
        size: 2
        type: str
        encoding: UTF-8
      - id: day
        size: 2
        type: str
        encoding: UTF-8
      - id: hour
        size: 2
        type: str
        encoding: UTF-8
      - id: minute
        size: 2
        type: str
        encoding: UTF-8
      - id: second
        size: 2
        type: str
        encoding: UTF-8
