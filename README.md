# restapi
A RESTAPI using python and flask for a shopping mall
TO see the outputs follow ollowing steps: 
 1.	run the program
2.	click on the URL that pops out.
3.	To see the items in the list write "/items" beside the url.
  eg. http://127.0.0.1:5000/items
4.	To see the items in the cart write "/cart" beside the url.
  eg. http://127.0.0.1:5000/cart
5.	To see the a particular item in the list write "/items/itemno" beside the url.
  eg. http://127.0.0.1:5000/items/3
6.	To Add the item in the cart open terminal and write 
  ‘curl -i -H "Content-Type: Application/json" -X ADD http://localhost:5000/cart’
7.	To delete the item from the cart open terminal and write 
  ‘curl -i -H "Content-Type: Application/json" -X REMOVE http://localhost:5000/cart/3’
  (3 can be changed with any item no which open wants to delete)
8.	To delete the item from the items list open terminal and write 
  curl -i -H "Content-Type: Application/json" -X DELETE http://localhost:5000/items/3
  (3 can be changed with any item no which open wants to delete)
  
  NOTE: In each step keep opening the URL to see the result.

 ^
