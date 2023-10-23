import hashlib
import json

class Profile:

    def __init__(self, name, public_key, private_key):
        self.name = name
        self.public_key = public_key
        self.private_key = private_key
        self.data = {}

    def add_data(self, key, value):
        self.data[key] = value

    def get_data(self, key):
        return self.data.get(key, None)

def create_signature(data, private_key):

    hashed_data = hashlib.sha256(data.encode()).hexdigest()
    signature = hashlib.sha256((hashed_data + private_key).encode()).hexdigest()

    return signature

class SSI:

    def __init__(self):
        self.identities = {}

    def register_identity(self, identity):
        self.identities[identity.public_key] = identity

    def verify_signature(self, public_key, data, signature):

        identity = self.identities.get(public_key, None)
        if not identity:
            return False
        
        hashed_data = hashlib.sha256(data.encode()).hexdigest()
        reconstructed_signature = hashlib.sha256((hashed_data + identity.private_key).encode()).hexdigest()
        
        return signature == reconstructed_signature

def main():

    ssi_system = SSI()
    jason_profile = Profile("Jason", "jason_public_key", "jason_private_key")
    jason_profile.add_data("email", "jason@jchowlabs.com")
    jason_profile.add_data("phone", "1234567890")

    ssi_system.register_identity(jason_profile)
    data_to_sign = json.dumps(jason_profile.data)
    jason_signature = create_signature(data_to_sign, jason_profile.private_key)

    print()
    print("----------------------------------")
    print("| Self-Sovereign Identity System |")
    print("----------------------------------")
    print(f"Name: {jason_profile.name}")
    print(f"Public Key: {jason_profile.public_key}")
    print(f"Private Key: {jason_profile.private_key}")
    print(f"Data: {jason_profile.data}")
    print(f"Signature: {jason_signature}")

    if ssi_system.verify_signature(jason_profile.public_key, data_to_sign, jason_signature):
        print("Status: Signature is verified.")
        print()
    else:
        print("Status: Signature is not valid.")
        print()

if __name__ == "__main__":
    main()
