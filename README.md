A Python toolkit that replaces vulnerable cryptographic hashes with NIST-approved post-quantum algorithms:

--> MD5 → SHAKE-256 (from SHA-3 family)

--> SHA-256 → SHAKE-256 (configurable length)

--> PBKDF2 → PQC KDF (SHAKE-256 based key derivation)

Designed for developers transitioning to quantum-resistant cryptography.
