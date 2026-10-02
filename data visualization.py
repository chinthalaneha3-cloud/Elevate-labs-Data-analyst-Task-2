TASK 2 - DATA VISUALIZATION AND STORYTELLING

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

sales = [12000, 15000, 14000, 18000, 20000, 19000,
         23000, 25000, 22000, 27000, 30000, 33000]

profit = [2000, 2500, 2300, 3500, 4000, 3800,
          4800, 5200, 4500, 6000, 7000, 8000]

print("MONTHLY SALES REPORT")
print("--------------------")

for i in range(len(months)):
    print(months[i], "Sales =", sales[i],
          "Profit =", profit[i])

print("\nTotal Sales =", sum(sales))
print("Total Profit =", sum(profit))

highest_sales = max(sales)
highest_month = months[sales.index(highest_sales)]

print("Highest Sales =", highest_month)
print("Amount =", highest_sales)

print("\nKEY INSIGHTS")
print("1. Sales increased gradually during the year.")
print("2. December has the highest sales.")
print("3. Profit also increased with sales.")
print("4. Overall business performance improved.")