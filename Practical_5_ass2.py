price_input = input("Enter the prices of items sold today (separated by space): ")
prices = tuple(float(p) for p in price_input.split())

if prices:
    print("a) Total number of items sold:", len(prices))
    
    cheapest = min(prices)
    print("b) Price of cheapest item:", cheapest)
    
    costliest = max(prices)
    print("c) Price of costliest item:", costliest)
    
    sorted_prices = sorted(prices)
    print("d) Price list in ascending order:", sorted_prices)
    
    count_costliest = prices.count(costliest)
    print("e) Number of costliest items sold:", count_costliest)
else:
    print("No items were sold today.")
  
