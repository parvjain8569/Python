# dictionary 


dell = {
    "brand": "Dell",
    "color": "black",
    "price": 20000,
    "price": 40000, # previous value overide
    "material": "Stainless Steel",
    "RAM": "20GB"
}
dell["hardisk"] = "500GB" # updating a dictionary if key doesn't exist earlier.
dell["color"]= "grey"  # similar to list but list value changes through indexing.
print(dell)
print(dell["price"])
print(dell.get("material"))
print(dell.get("materal"))
dell.pop("price")  # removes key and value
print(dell)
dell.popitem() # removes last key value pair
print(dell)
del(dell)  # Deletes the complete dictionary 
print(dell)

#question 
deatils={
    "name":"parv jain ",
    "email":"parv,jain930@gmail,com" ,
    "roll no.":"",

    
    }
deatils["roll no."]=int(input("enter the correct roll number:"))
print(deatils)