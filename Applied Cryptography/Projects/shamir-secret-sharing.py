import random
from math import ceil
from decimal import Decimal

FIELD_SIZE = 10**5

def reconstruct_secret(shares):
    
    total_sum = 0

    for j, (xj, yj) in enumerate(shares):
        prod = Decimal(1)

        for i, (xi, _) in enumerate(shares):
            if i != j:
                prod *= Decimal(xi) / Decimal(xi - xj)

        prod *= Decimal(yj)
        total_sum += prod

    return int(total_sum)

def polynomial_value(x, coefficients):
    
    evaluation_point = 0
    for coefficient_index, coefficient_value in enumerate(coefficients[::-1]):
        evaluation_point += x ** coefficient_index * coefficient_value
    return evaluation_point

def generate_coefficients(threshold, secret):
    
    coefficients = [random.randrange(0, FIELD_SIZE) for _ in range(threshold - 1)]
    coefficients.append(secret)
    return coefficients

def generate_shares(total_shares, threshold, secret):
    
    coefficients = generate_coefficients(threshold, secret)
    shares = []

    for _ in range(1, total_shares + 1):
        x = random.randrange(1, FIELD_SIZE)
        shares.append((x, polynomial_value(x, coefficients)))

    return shares

if __name__ == '__main__':
    
    threshold = 3
    total_shares = 5
    secret = 1337
    
	# Part 1: Generation of shares
    print("-------------------------")
    print("| Shamir Secret Sharing |")
    print("-------------------------")
    print(f'Original Secret: {secret}')
    shares = generate_shares(total_shares, threshold, secret)
    print(f'Generated Shares: {", ".join(str(share) for share in shares)}')

    # Part 2: Secret Reconstruction
    pool = random.sample(shares, threshold)
    print(f'Combining Shares: {", ".join(str(share) for share in pool)}')
    print(f'Reconstructed Secret: {reconstruct_secret(pool)}')
    print()
