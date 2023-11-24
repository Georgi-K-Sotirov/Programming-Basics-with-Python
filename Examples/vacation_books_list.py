from math import floor

page_count = int(input())
page_reading_for_one_hour = int(input())
days_count = int(input())

total_hours_for_the_book = page_count / page_reading_for_one_hour
hours_for_days = floor(total_hours_for_the_book / days_count)

print(hours_for_days)