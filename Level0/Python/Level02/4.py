# Check if a given year is a leap year.
#  السنة بتكون كبيسة إذا: بتقبل القسمة على 400، أو بتقبل القسمة على 4، بشرط إنها ما تقبل القسمة على 100.

year = int(input("Enter a year: "))
if(year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
