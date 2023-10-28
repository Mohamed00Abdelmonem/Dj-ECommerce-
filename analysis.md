
App Products
 - Product
   - user
   - categories - relation
   - name
   - price
   - image 
   - subtitle
   - size -Choies -  [S , M, L, XL, XXL, XXXL]
   - color
   - quantity
   - description
   - additional_information  ---> With(samernote)
   - sku
   - created_at




 - Categories
   - user
   - tilte
   - created_at




- ProductImage
   - product
   - image




- Reviews
   - product
   - user
   - review
   - rate
   - created_at        



steps 
 1- create model --> True
 2- add template --> True 
 3- add view  ---> InProgress
 4- add urls


to do for every day  
 - update pagingtions  --- True
 - add slug ---- True
 - add debug toboler --- True
 
 - using api in app product  --- True

 - understand api for product --->  
 - starting in app setting ---> 
 

__________________________________________________________


 App Orders :
   - Cart 
   CART_STATUS = {
    ('InProgress','InProgress'),
    ('Completed','Completed'),
}
     - user 
     - statud
     - coupon
     - total after coupon

   - Cart_Detail
     - Product Relationship
     - Cart   Relationshi
     - price_total ---- counter agrregate_function or custom

<!-- 
     - country_for_shipping 
     - zip code country ----optional
     - price_total ---- counter agrregate_function or custom
     - coupon_code --- optional
     - created_date  -->

   - Order 
     - cart
     - status
     - code 
     - order time 
     - delivery_time
     - coupon 
     - total_after_coupon


   - OrderDetail
     - order 
     - product
     - price
     - quantity
     - total 

   - Coupon
     - code 
     - discount
     <!-- - user  -->
     - start_date
     - end_date    