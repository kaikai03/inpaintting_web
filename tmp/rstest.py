from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_public_key
import base64

message = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX25hbWUiOiJqdW56ZSJ9.aRdAsS6b2HAIKS8g1HxFsRR-kIx-ORNJZg3qrJWNLRA'

pubkey = '-----BEGIN RSA PUBLIC KEY-----\nMIGJAoGBAJn0PHL6vuMSqr48Ia65phBt0Lv+e0ksQeEpK+0Q8r5380lItJfeVpN+\nDFe0d9B9b1eEBI3Fe4lmOiuSxWShPYG80g/LOnkaWeZt6ST1fZXxX/SDKuKY7gkF\ntmIuq9IyO41H7a8NR893lGKW5dyvfIbOkbcm6lP1lRMnx1G5debhAgMBAAE=\n-----END RSA PUBLIC KEY-----\n'



pubKey = load_pem_public_key(pubkey.encode('utf8'),default_backend())

ciphertext = pubKey.encrypt(
                        message.encode('utf-8'),
                        padding.PKCS1v15()
                    )

cipher_64 = base64.b64encode(ciphertext)

cipher_64