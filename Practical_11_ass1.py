import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('company_sales_data.csv')

# a) Line Plot for Total Profit
plt.plot(df['month_number'], df['total_profit'], label='Total Profit', marker='o', color='blue', linewidth=2)
plt.xlabel('Month Number')
plt.ylabel('Profit (in $)')
plt.title('Monthly Total Profit Analysis')
plt.xticks(df['month_number'])
plt.legend(loc='lower right')
plt.savefig('total_profit_line.png')
plt.clf()

# b) Multiline Plot for all products
products = ['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']
for product in products:
    plt.plot(df['month_number'], df[product], label=product, marker='.', linestyle='--')

plt.xlabel('Month Number')
plt.ylabel('Sales Units')
plt.title('Sales Data for All Products')
plt.xticks(df['month_number'])
plt.legend()
plt.savefig('all_products_line.png')
plt.clf()

# c) Bar Chart for Face Cream and Face Wash
width = 0.3
plt.bar(df['month_number'] - width/2, df['facecream'], width, label='Face Cream', color='orange')
plt.bar(df['month_number'] + width/2, df['facewash'], width, label='Face Wash', color='cyan')
plt.xlabel('Month')
plt.ylabel('Units Sold')
plt.title('Face Cream vs Face Wash Sales Comparison')
plt.xticks(df['month_number'])
plt.legend()
plt.savefig('facecream_facewash_bar.png')
plt.clf()

# d) Pie Chart for Total Annual Sales per product
total_units = [df[p].sum() for p in products]
plt.pie(total_units, labels=products, autopct='%1.1f%%', startangle=90)
plt.title('Annual Market Share per Product')
plt.axis('equal')
plt.savefig('annual_sales_pie.png')
plt.clf()
