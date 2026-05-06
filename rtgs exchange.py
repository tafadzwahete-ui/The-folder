# EXCHANGE RATE FROM USD TO RTGS
def convert_usd_to_rtgs(usd):
    rate=40
    rtgs=usd * rate
    return rtgs

amount=float(input("enter amunt in USD: "))
converted = convert_usd_to_rtgs(amount)
print(f"{amount} USD = {converted}RTGS")

#  EXCHANGE RATE FROM RAND TO RTGS
def convert_rand_to_rtgs(rand):
    rate=200
    rtgs=rand * rate
    return rtgs

amount=float(input("enter amunt in RAND: "))
converted = convert_rand_to_rtgs(amount)
print(f"{amount} rand = {converted}RTGS")

# EXCHANGE RATE FROM POUND TO RTGS
def convert_pound_to_rtgs(pound):
    rate=80
    rtgs=pound * rate
    return rtgs
amount=float(input("enter amunt in pound: "))
converted=convert_pound_to_rtgs(amount)

print(f"{amount} POUND = {converted}RTGS")