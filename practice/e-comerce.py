class product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

class cartitems:
    def __init__(self,pro,quantity):
        self.pro = pro
        self.quantity = quantity
        

    def item_total(self):
        return self.pro.price *self.quantity
    
p1 = product('Class', 1200)
p2 = product('shirt', 1000)
p3 = product('apple', 100)


q1 = cartitems(p1,4)
q2 = cartitems(p2,1)
q3 = cartitems(p3,2)

total_bill = q1.item_total() + q2.item_total() + q3.item_total()
print(total_bill)