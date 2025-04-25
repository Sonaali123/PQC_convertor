from pqc_converter import PQCHashConverter

def convert_sha256(data: bytes) -> dict:
    converter = PQCHashConverter()
    return converter.convert("sha256", data)

if __name__ == "__main__":
    result = convert_sha256(b"Hello, PQC!")
    print("Original SHA-256:", result['original'])
    print("PQC (SHAKE-256):", result['pqc'])