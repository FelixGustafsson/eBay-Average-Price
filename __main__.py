from ebaysdk.finding import Connection
from ebaysdk.exception import ConnectionError

APPLICATION_ID = "YOUR APP ID HERE"
keyword = ""


class Ebay(object):
    def __init__ (self, APPLICATION_ID, keyword):
        self.APPLICATION_ID = APPLICATION_ID
        self.keyword = keyword

    def fetch (self):
        try:
            priceList = []
            totalPrice = 0;
            averagePrice = 0;
            api = Connection(appid=self.APPLICATION_ID, config_file=None)
            response = api.execute('findItemsAdvanced', {'keywords': keyword})

            for item in response.reply.searchResult.item:
                priceList.append(item.sellingStatus.currentPrice.value)

            for i in range (len(priceList)):
                totalPrice += float(priceList[i])
            
            averagePrice = totalPrice / len(priceList)
            print(f'The average price for "{keyword}" on eBay is {averagePrice:.2f}')

        except ConnectionError as e:
            print(e)
            print(e.response.dict())



if __name__ == '__main__':

    while True:
        keyword = input("What keyword do you want the average price for: ")
        e = Ebay(APPLICATION_ID, keyword)
        e.fetch()
        print("\n")

        restart = input("Do you want to search again or not? (y/n)\n")
        if restart == "y":
            continue
        else:
            break    
    