# min and sec
a = int(input("Enter the seconds "))
seconds = a
minutes = seconds // 60
seconds = seconds % 60
print( minutes, "minutes" ,seconds,"seconds")

# reverse number

num = int(input("Enter the number"))
reverse= (str(num)[::-1])
print(reverse)
# Day of the year

day = int(input("Enter the day"))
month = int(input("Enter the month"))
days_inmonth = 30
dayof_theyear = (month-1)*(days_inmonth + day)
print(dayof_theyear)