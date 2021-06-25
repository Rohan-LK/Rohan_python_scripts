class RetailOrder(object):
    def __init__(self, qty, price):
        self.qty = qty
        self.price = price
    
    def ebeebay_make_best_deal(seller, buyers):
        pass
        # SELLER QTY AND PRICE FROM INPUT LIST
        seller_Q = int(seller[0]); seller_P = float(seller[1])

        # CREATE SEPARATE BUYER QTY & PRICE LISTS FROM INPUT
        buy_Q = []
        buy_P = []
        for i in range(0, len(buyers)):
            if i%2==0:
                ele_Q = float(buyers[i])
                buy_Q.append(ele_Q)
            else:
                ele_P = int(buyers[i])
                buy_P.append(ele_P)

        if len(buy_Q)!=len(buy_P):
            raise Exception("buy_Q and buy_P are not equal")

        # FIND MID PRICE FOR EACH BUYER
        arr_mid = []
        for i in range(0, len(buy_P)):
            # MID PRICE
            ele = (int(buy_P[i]) + int(seller_P)) /2
            arr_mid.append(ele)

        # EXPECTED AND ACTUAL SELLING PRICE
        arr_expect_from_buyer = []
        arr_get_from_buyer = []
        for i in range(0, len(buy_P)):
            # SELLER EXPECTS FROM BUYER
            ele2 = int(buy_Q[i]) * float(seller_P)
            arr_expect_from_buyer.append(ele2)
            # SELLER GETS FROM BUYER
            ele3 = int(buy_Q[i]) * float(arr_mid[i])
            arr_get_from_buyer.append(ele3)
        
# ----- Q 1
        print('\nTOTAL SELLING PRICE: ',sum(arr_get_from_buyer))

# ----- Q 2
        print('\nEACH BUYERS TOTAL BUYING PRICE: ',arr_get_from_buyer)


        for i in range(0, len(arr_get_from_buyer)):
            if arr_get_from_buyer[i]==max(arr_get_from_buyer):
# ------------- Q 3
                print('\nBUYER "'+str(i+1)+'" CONTRIBITED HIGHERST TO THE DEAL')


# FOR SOLUTIONS
seller = [100,200]
buyers = [60,220,40,210]
RetailOrder.ebeebay_make_best_deal(seller, buyers)
