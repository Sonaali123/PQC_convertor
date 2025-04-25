from pqc_converter import PQCHashConverter

def convert_pbkdf2(data: bytes, salt: bytes = None) -> dict:
    converter = PQCHashConverter()
    return {'pqc': converter.convert("pbkdf2", data, salt=salt)['pqc']}

if __name__ == "__main__":
    result = convert_pbkdf2(b"password", salt=b"randomsalt")
    print("PQC KDF:", result['pqc'])