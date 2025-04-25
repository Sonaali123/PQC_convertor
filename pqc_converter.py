import hashlib
import os

class PQCHashConverter:
    def __init__(self):
        self.algorithm_mapping = {
            'md5': {'original': self._md5, 'pqc': self._shake_hash},
            'sha256': {'original': self._sha256, 'pqc': self._shake_hash},
            'pbkdf2': {'original': None, 'pqc': self._pqc_kdf},
        }

    def convert(self, algorithm: str, data: bytes, **kwargs):
        if algorithm.lower() not in self.algorithm_mapping:
            raise ValueError(f"Unsupported algorithm: {algorithm}")
        
        result = {}
        if self.algorithm_mapping[algorithm.lower()]['original']:
            result['original'] = self.algorithm_mapping[algorithm.lower()]['original'](data)
        result['pqc'] = self.algorithm_mapping[algorithm.lower()]['pqc'](data, algorithm=algorithm, **kwargs)
        return result

    def _md5(self, data: bytes) -> str:
        return hashlib.md5(data).hexdigest()

    def _sha256(self, data: bytes) -> str:
        return hashlib.sha256(data).hexdigest()

    def _shake_hash(self, data: bytes, algorithm: str = "", **kwargs) -> str:
        h = hashlib.shake_256()
        h.update(f"{algorithm}:{data}".encode())
        return h.digest(32).hex()

    def _pqc_kdf(self, data: bytes, salt: bytes = None, **kwargs) -> str:
        if not salt:
            salt = os.urandom(16)
        h = hashlib.shake_256()
        h.update(salt + data)
        return h.digest(32).hex()