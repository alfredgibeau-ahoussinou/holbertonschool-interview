#!/usr/bin/python3
"""
Prime Game - Maria et Ben jouent à un jeu. Étant donné un ensemble
d'entiers consécutifs allant de 1 à n inclus, ils choisissent à tour
de rôle un nombre premier dans l'ensemble et retirent ce nombre et ses
multiples de l'ensemble. Le joueur qui ne peut pas jouer perd la partie.
"""


def isWinner(x, nums):
    """
    Determine the winner of the prime game based on optimal play by both
    players.

    Maria always starts. Players alternate picking prime numbers, removing that
    number and all its multiples from the set. The player unable to make a move
    loses the round.

    :param x: Number of rounds.
    :param nums: List of n values for each round.
    :return: "Maria" if Maria wins most rounds, "Ben" if Ben wins most rounds,
        or None if tied.
    """
    if x <= 0 or not nums:
        return None

    # Process only the first x rounds
    rounds_to_process = nums[:x]
    
    if not rounds_to_process:
        return None

    max_n = max(rounds_to_process)
    
    # Step 1: Precompute prime numbers up to max_n using Sieve of Eratosthenes
    if max_n >= 2:
        sieve = [True] * (max_n + 1)
        sieve[0] = sieve[1] = False  # 0 and 1 are not primes

        for i in range(2, int(max_n ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, max_n + 1, i):
                    sieve[j] = False

        # Step 2: Count prime numbers up to each n
        prime_counts = [0] * (max_n + 1)
        count = 0
        for i in range(1, max_n + 1):
            if sieve[i]:
                count += 1
            prime_counts[i] = count
    else:
        # All n values are < 2, no primes available
        prime_counts = [0] * (max_n + 1)

    # Step 3: Simulate rounds
    maria_wins = 0
    ben_wins = 0

    for n in rounds_to_process:
        if n < 2:
            # No primes available, Maria can't make a move, Ben wins
            ben_wins += 1
        elif prime_counts[n] % 2 == 1:
            maria_wins += 1  # Maria wins if the count is odd
        else:
            ben_wins += 1  # Ben wins if the count is even

    # Step 4: Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
