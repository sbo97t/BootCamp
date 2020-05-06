print("Enter a FAANG ticker symbol for the average 52 week price")

ticker = str(input())

list = {
    "FB": {
        "Hi": 224.20,
        "Lo": 137.10
    },
    "AMZN": {
        "Hi": 2475.00,
        "Lo": 1626.03
    },
    "AAPL": {
        "Hi": 327.85,
        "Lo": 170.27
        
    },
    "NLFX": {
        "Hi": 449.52,
        "Lo": 252.28
    },
    "GOOG": {
        "Hi": 1530.74,
        "Lo": 1008.87
    },
    
}

for ticker_data in list.items():
    record = [ticker_data]
    
    ticker_avg = ticker_data[1][2]
    
    year_avg = ticker_avg / 2
    
print(year_avg)
    