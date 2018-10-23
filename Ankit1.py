from easygui import *
import sys
while 1:
msgbox("welcome to online shopping")
msg="which site would you prefer"
title="online shopping"
choices=["amazon","snapdeal","flipkart","myntra"]
choice=choicebox(msg,title,choices)
if choices=="Amazon"
  msg1="what would you like to purchase?"
 title1="diwali sale"
choices1=["Electronics","Clothing","Groceries","Furniture"]
if choices1=="Electronics"
  msg2="what type of product do you want?"
 title2="Electronics"
choices2=["Mobile","Laptop","Earphones","Speakers"]
if choices2=="Mobile"
  msg3="which Mobile do you want?"
 title3="Mobiles"
choices3=["Samsung","One Plus","MI","I-Phone"]
if choices3=="Samsung"
   msg4="Choose your Model"
   title4="Samsung"
   choices4=["Galaxy J8","Samsung S9","Galaxy J6"]
if choices4=="Galaxy J8"
    msgbox("vendor1 offers a price of  30000rs. \nvendor2 offers a price of 29000rs. \nvendor3 offers a price of 28000rs.")
elif choices4=="Samsung S9"
    msgbox("vendor1 offers a price of  70000rs. \nvendor2 offers a price of 67000rs. \nvendor3 offers a price of 65000rs.")
elif choices4=="Galaxy J6"
    msgbox("vendor1 offers a price of  83000rs. \nvendor2 offers a price of 77000rs. \nvendor3 offers a price of 72000rs.")
else:
    sys.exit(0)
elif  choices3=="One Plus"
     msg5="Choose your model"
    title5="One Plus"
    choices5=["One plus 5","One plus 5T","One plus 6"]
if choices5=="One Plus 5"
    msgbox("vendor1 offers a price of  30000rs. \nvendor2 offers a price of 27000rs. \nvendor3 offers a price of 25000rs.")
elif choices5=="One Plus 5T"
    msgbox("vendor1 offers a price of  50000rs. \nvendor2 offers a price of 47000rs. \nvendor3 offers a price of 45000rs.")
elif choices5=="One Plus 6"
    msgbox("vendor1 offers a price of  70000rs. \nvendor2 offers a price of 67000rs. \nvendor3 offers a price of 65000rs.")
else:
    sys.exit(0)
elif  choices3=="MI"
     msg6="Choose your model"
    title6="One Plus"
    choices6=["MI note 5","MI note5pro","MI 6"]
if choices6=="MI note 5"
    msgbox("vendor1 offers a price of  13000rs. \nvendor2 offers a price of 15000rs. \nvendor3 offers a price of 17000rs.")
elif choices5=="MI note5pro"
    msgbox("vendor1 offers a price of  15000rs. \nvendor2 offers a price of 13000rs. \nvendor3 offers a price of 11000rs.")
elif choices5=="MI 6"
    msgbox("vendor1 offers a price of  23000rs. \nvendor2 offers a price of 21000rs. \nvendor3 offers a price of 19000rs.")
else:
    sys.exit(0)
lif  choices3=="I-Phone"
     msg7="Choose your model"
    title7="I-Phone"
    choices7=["I-Phone 5","I-Phone 6","I-Phone 7"]
if choices7=="I-Phone 5"
    msgbox("vendor1 offers a price of  30000rs. \nvendor2 offers a price of 27000rs. \nvendor3 offers a price of 25000rs.")
elif choices7=="I-Phone 6"
    msgbox("vendor1 offers a price of  50000rs. \nvendor2 offers a price of 47000rs. \nvendor3 offers a price of 45000rs.")
elif choices7=="I-Phone 7"
    msgbox("vendor1 offers a price of  70000rs. \nvendor2 offers a price of 67000rs. \nvendor3 offers a price of 65000rs.")
else:
    sys.exit(0)

