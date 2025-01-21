import sncf.barcode_sncf as barcode_sncf

b = barcode_sncf.BarcodeSncf.from_file("sncf/sncf.bin")
print(b.magic)
print(b.travel_class_return)