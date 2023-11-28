cake_light = int(input())
cake_with = int(input())
pieces_available = cake_with * cake_light
pieces_counter = 0

while pieces_available > pieces_counter:
    pieces_taken = input()
    if pieces_taken == "STOP":
        break
    pieces_taken = int(pieces_taken)
    pieces_counter += pieces_taken

diff = abs(pieces_available - pieces_counter)
if pieces_counter <= pieces_available:
    print(f"{diff} pieces are left.")
else:
    print(f"No more cake left! You need {diff} pieces more.")