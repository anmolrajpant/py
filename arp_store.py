veg = ['','Tomato', 'Potato', 'Onion', 'Pumpkin', 'Banana', 'Garlic', 'Ginger', 'Mushroom', 'Celery', 'Cabbage']
maxPrice = [0,40,55,50,40,90,150,110,180,110,50]
minPrice = [0,50,60,60,50,100,200,120,200,120,60]

avgPrice=[((x + y)/2) for x, y in zip(maxPrice, minPrice)]

print(avgPrice)