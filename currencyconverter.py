conversion_rates = {
       "USD": {
            "PKR": 279,
            "EURO": 0.58,
            "SAUDI-RIYAL": 3.75,
            "CAD": 1.58
        },
        "PKR": {
            "USD": 0.0036,
            "SAUDI-RIYAL": 0.013,
            "EURO": 0.0030,
            "CAD": 0.0049
        },
        "CAD": {
            "PKR": 204.96,
            "USD": 0.73,
            "EURO": 0.62,
            "SAUDI-RIYAL": 2.73
        },
        "SAUDI-RIYAL": {
            "PKR": 74.49,
            "USD": 0.27,
            "CAD": 0.37,
            "EURO": 0.23
        },
        "EURO": {
            "PKR": 329.82,
            "USD": 1.18,
            "SAUDI-RIYAL": 4.43,
            "CAD": 1.61
        }
    }

CURRENCIES = tuple(conversion_rates.keys())
def currency_converter(amount, source, target):
    if source == target:
        return amount
    else:
        return conversion_rates[source][target] * amount
    
def other_rates(amount,source,target):
    for i in CURRENCIES:
        if i not in (source,target):
            result=currency_converter(amount,source,i)
            print(f"{amount} {source} = {result:.2f} {i}")

def dispaly_history(History):
    for i in History:
        print(i)


def main():
    Coversions=[]

    while True:
        try:   
            amount = float(input("Enter the amount: "))
            
            source_currency = input("Source Currency (USD/EURO/CAD/PKR/SAUDI-RIYAL): ").strip().upper()
            if source_currency not in CURRENCIES:
                raise ValueError("INVALID SOURCE CURRENCY")
            
            target_currency = input("Target Currency (USD/EURO/CAD/PKR/SAUDI-RIYAL): ").strip().upper()
            if target_currency not in CURRENCIES:
                raise ValueError("INVALID TARGET CURRENCY")
            
            # Calculate result
            result = currency_converter(amount, source_currency, target_currency)
            
            # Print result and exit loop
            print(f"\nYour conversion result is:\n {amount} {source_currency} = {result:.2f} {target_currency}")

            print("<----------Your Amount-Rate in other Currencies-------->")
            other_rates(amount,source_currency,target_currency)
            
            Coversions.append(f"{amount} {source_currency} = {result:.2f} {target_currency}")

            choice=input("Do you want to make another conversion? y/n").strip().lower()
            if choice=='y':
                continue
            else:
                print("Your previous conversions were : ")
                dispaly_history(Coversions)
                break

        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.\n")




main()