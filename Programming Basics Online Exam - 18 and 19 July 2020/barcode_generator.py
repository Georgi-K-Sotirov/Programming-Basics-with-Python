start_number = int(input())
end_number = int(input())
barcode_list = []

first_chr_start = start_number // 1000
second_chr_start = start_number // 100 % 10
third_chr_start = start_number // 10 % 10
forth_chr_start = start_number % 10

first_chr_end = end_number // 1000
second_chr_end = end_number // 100 % 10
third_chr_end = end_number // 10 % 10
forth_chr_end = end_number % 10


next_number = start_number - 1
while next_number <= end_number:
    next_number += 1
    first_chr = next_number // 1000
    if first_chr < first_chr_start or first_chr > first_chr_end:
        continue

    second_chr = next_number // 100 % 10
    if second_chr < second_chr_start or second_chr > second_chr_end:
        continue

    third_chr = next_number // 10 % 10
    if third_chr < third_chr_start or third_chr > third_chr_end:
        continue

    forth_chr = next_number % 10
    if forth_chr < forth_chr_start or forth_chr > forth_chr_end:
        continue

    if forth_chr % 2 == 0 or second_chr % 2 == 0 or third_chr % 2 == 0 or first_chr % 2 == 0:
        continue

    else:
        barcode_list += [next_number]

print(' '.join(map(str, barcode_list)))
