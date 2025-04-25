from md5_pqc import convert_md5
from sha256_pqc import convert_sha256
from pbkdf2_pqc import convert_pbkdf2

def main():
    data = b"Hello, PQC!"
    password = b"my_secure_password"
    salt = b"randomsalt"
    
    print("=== Cryptographic Hash Conversions ===")
    
    # MD5 Conversion
    md5_result = convert_md5(data)
    print("\n[MD5]")
    print("Original:", md5_result['original'])
    print("PQC:", md5_result['pqc'])
    
    # SHA-256 Conversion
    sha256_result = convert_sha256(data)
    print("\n[SHA-256]")
    print("Original:", sha256_result['original'])
    print("PQC:", sha256_result['pqc'])
    
    # PBKDF2 Conversion
    pbkdf2_result = convert_pbkdf2(password, salt)
    print("\n[PBKDF2]")
    print("PQC KDF:", pbkdf2_result['pqc'])

if __name__ == "__main__":
    main()