def sieve_of_eratosthenes(limit):
    # Khởi tạo danh sách boolean, True nghĩa là số đó là nguyên tố
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 và 1 không phải là số nguyên tố

    # Áp dụng thuật toán sàng Eratosthenes
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False

    # Tạo danh sách các số nguyên tố từ danh sách boolean
    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes

# Tìm các số nguyên tố nhỏ hơn 1 triệu và chuyển thành tuple
P = tuple(sieve_of_eratosthenes(1_000_000))

# In ra số lượng và một vài phần tử đầu của tuple P
print(f"Số lượng số nguyên tố nhỏ hơn 1 triệu: {len(P)}")
print("Một vài số nguyên tố đầu tiên:", P[:10])
