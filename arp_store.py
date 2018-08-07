veg = ['','Tomato', 'Potato', 'Onion', 'Pumpkin', 'Banana', 'Garlic', 'Ginger', 'Mushroom', 'Celery', 'Cabbage']
minPrice = [0,40,55,50,40,90,150,110,180,110,50]
maxPrice = [0,50,60,60,50,100,200,120,200,120,60]

avgPrice=[((x + y)/2) for x, y in zip(maxPrice, minPrice)]

"""count = 10
while count != 10:
    print str(count+1)+"\t\t\t"+veg[count]+"\t\t\t"+str(maxPrice[count])
    count+=1"""

#print(avgPrice)
print ("S.No" "     " "Product" "        "  "Price")
print ("-------------------------------------------")
print ("1." "       " "Tomato" "         "    "Rs. 50" )
print ("2." "       " "Potato" "         "    "Rs. 60" )
print ("3." "       " "Pumpkin" "        "    "Rs. 50" )
print ("4." "       " "Banana" "         "    "Rs. 100" )
print ("5." "       " "Garlic" "         "    "Rs. 50" )
print ("6." "       " "Ginger" "         "    "Rs. 120" )
print ("7." "       " "Mushroom" "       "    "Rs. 200" )
print ("8." "       " "Celery" "         "    "Rs. 120" )
print ("9." "       " "Cabbage" "        "    "Rs. 60" )
print ("10." "      " "Onion" "          "    "Rs. 60" )

item = []
qty = []
while (item != ""):
    item = input("Enter the S.No Number of Vegetable:")
    qty = input("Enter the Quantity:")
