import os

def get_currency_rates():
    return {
        "EUR": 0.93193616579433,
        "GBP": 0.82781645215259,
        "JPY": 131.19949431214,
        "AUD": 1.4397738643225,
        "CHF": 0.92028900908102,
        "CAD": 1.3423076593907,
        "NZD": 1.5833908076057,
        "TRY": 18.834026664285,
        "NGN": 460.38643603134,
        "KGS": 86.204686365509,
        "MGA": 4304.1015625001,
        "SRD": 32.599112426036,
        "GHS": 12.171775752555,
        "CUP": 1,
        "NOK": 10.292276111553,
        "QAR": 3.647456564218,
        "CZK": 22.151198870847,
        "HRK": 7.3622679377822,
        "RSD": 108.50813677066,
        "NIO": 36.5456053068,
        "SBD": 8.4142802596411,
        "MWK": 1026.1699650757,
        "YER": 250.16460438188,
        "VES": 23.119577018125,
        "BDT": 105.55357494865,
        "RON": 4.561702839269,
        "DZD": 136.08707546405,
        "ARS": 189.54063945171,
        "STN": 23.015143603134,
        "BIF": 2075.0470809793,
        "MMK": 2099.7617913292,
        "MUR": 45.343621399176,
        "AED": 3.6729258207663,
        "IDR": 15094.627023151,
        "MXN": 18.930368210099,
        "UAH": 36.471949418503,
        "CRC": 582.30700358177,
        "BZD": 2.0152720621857,
        "GNF": 8608.2031250002,
        "SZL": 17.517488076312,
        "SOS": 568.33010960672,
        "INR": 82.61621692441,
        "NPR": 132.22300217532,
        "XAF": 611.44726610174,
        "AZN": 1.6969620326628,
        "PYG": 7285.4048170774,
        "GYD": 210.95103623224,
        "RWF": 1084.4980314961,
        "ERN": 15.073187414501,
        "WST": 2.6917063637474,
        "BRL": 5.1979076060451,
        "LKR": 366.23092436016,
        "TND": 3.0659547199457,
        "VND": 23535.787798723,
        "IQD": 1459.9450898656,
        "AFN": 90.147470904667,
        "NAD": 17.517488076312,
        "SYP": 2448.5555555556,
        "MOP": 8.0825233816249,
        "BAM": 1.8237265692887,
        "DKK": 6.9317566293577,
        "PKR": 268.49663239375,
        "BGN": 1.8216378121043,
        "RUB": 73.13025012108,
        "TMT": 3.4991991571149,
        "SVC": 8.7535253227409,
        "XCD": 2.7057523482105,
        "LAK": 16822.137404581,
        "GTQ": 7.8409535669812,
        "SAR": 3.7522112664965,
        "PLN": 4.4128685921236,
        "GIP": 0.8280832513416,
        "GEL": 2.6507535577517,
        "MKD": 57.302961749486,
        "AWG": 1.8098718791065,
        "AOA": 512.48837209302,
        "MVR": 15.453716690042,
        "BHD": 0.3766439820792,
        "EGP": 30.364809844914,
        "KRW": 1260.4690703693,
        "MRO": 36.020106861643,
        "COP": 4746.4294229853,
        "BBD": 2.0185948520656,
        "DJF": 177.9832815087,
        "HNL": 24.649888143177,
        "KES": 124.86613593224,
        "HKD": 7.8488108130589,
        "MAD": 10.227205009126,
        "ZAR": 17.71922356111,
        "MDL": 18.796201297002,
        "PAB": 1,
        "FJD": 2.2012785935471,
        "CDF": 2074.0705882353,
        "MZN": 64.247813411081,
        "UGX": 3672.8333333334,
        "KWD": 0.30555750395281,
        "THB": 33.400439168086,
        "PHP": 54.814725806971 
    }

def convert_currency(amount, currency_code, rates):
    if currency_code in rates:
        return amount * rates[currency_code]
    else:
        return None

def main():
    rates = get_currency_rates()
    
    try:
        amount = float(input("How much dollar do you have? "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    
    currency_code = input("What currency you want to have? ").upper()
    
    converted_amount = convert_currency(amount, currency_code, rates)
    
    if converted_amount is not None:
        print(f"\nDollar: {amount} USD")
        print(f"{currency_code}: {converted_amount:.6f}")
    else:
        print("Invalid currency code.")

if __name__ == "__main__":
    main()

#Couldn't directly link the csv file to the code even if it's in the same directory.