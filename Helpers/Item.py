class Item:
    def __init__(self,itemName,itemQty):
        self.itemName = itemName
        self.itemQty = itemQty
        self.itemPrice = None
        self.itemSubTotal = None
    
    def setItemPrice(self,itemPrice):
        self.itemPrice = itemPrice
    
    def setItemSubTotal(self,itemqty, itemPrice):
        self.itemSubTotal = itemqty*itemPrice
    