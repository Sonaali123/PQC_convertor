from pqc_converter import PQCHashConverter

def convert_md5(data: bytes) -> dict:
    converter = PQCHashConverter()
    return converter.convert("md5", data)

if __name__ == "__main__":
    result = convert_md5(b"Hello, PQC!")
    print("Original MD5:", result['original'])
    print("PQC (SHAKE-256):", result['pqc'])