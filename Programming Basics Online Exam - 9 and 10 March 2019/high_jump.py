target_high = int(input())
starting_high = target_high - 30
fails_attempts = 3
total_jumps = 0
while starting_high <= target_high:
    total_jumps += 1
    jumped_high = int(input())
    if jumped_high <= starting_high:
        fails_attempts -= 1
    else:
        if starting_high >= target_high:
            break
        starting_high += 5
        fails_attempts = 3
    if fails_attempts == 0:
        break

if fails_attempts == 0:
    print(f"Tihomir failed at {starting_high}cm after {total_jumps} jumps.")
else:
    print(f"Tihomir succeeded, he jumped over {starting_high}cm after {total_jumps} jumps.")



