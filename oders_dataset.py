import numpy as np
orders_ids= np.array([101,102,103,104,105])
prices = np.array([55000,300,1500,400,7000])
quantities = np.array([1,2,1,3,1])
discount = np.array([5,0,10,0,15])

total_price = prices *quantities
discount_amount =total_price *(discount/100)
final_price = total_price - discount_amount
final_price = np.round(final_price, 2)

print("Total Price:", total_price)
print("Discount Amount:", discount_amount)
print("Final Price After Discount:", final_price)

got_discount =np.where(discount > 0, "Yes", "No")
print("did the order get a discoutn?:", got_discount)

from sklearn.preprocessing import MinMaxScaler 
final_price_reshaped = final_price.reshape(-1,1)
scaler =MinMaxScaler()
scaled_prices = scaler.fit_transform(final_price_reshaped)

print("Final price after scaling (0 to 1):")
print(np.round(scaled_prices,2))

max_price = np.max(final_price)
min_price =np.min(final_price)

print("most expensive order:", max_price)
print("cheapest order:",min_price)

sorted_indices = np.argsort(final_price)
print("order ranking (low to high)", sorted_indices)

from scipy import stats 
print("Mean price",np.mean(final_price))
print("Median price ",np.median(final_price))
print("Mode of discount",stats.mode(discount, keepdims= True))
