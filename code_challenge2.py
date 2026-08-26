Amount = 19863

print("Deposit Amount", Amount)

thousand_bills = Amount // 1000

fiveHundred_bills = (Amount - (thousand_bills * 1000)) // 500
Amount = (Amount - (thousand_bills * 1000))

twoHundred_bills = (Amount - (fiveHundred_bills * 500)) // 200
Amount = (Amount - (fiveHundred_bills * 500))

oneHundred_bills = (Amount - (twoHundred_bills * 200)) // 100
Amount = (Amount - (twoHundred_bills * 200))

fifty_bills = (Amount - (oneHundred_bills * 100)) // 50
Amount = (Amount - (oneHundred_bills * 100))

twenty_bills = (Amount - (fifty_bills * 50)) // 20
Amount = (Amount - (fifty_bills * 50))

ten_bills = (Amount - (twenty_bills * 20)) // 10
Amount = (Amount - (twenty_bills * 20))

five_coins = (Amount - (ten_bills * 10)) // 5
Amount = (Amount - (ten_bills * 10))

one_coins = (Amount - (five_coins * 5)) // 1
# Amount = (Amount - (five_coins * 5))

print("1000 Bills:", thousand_bills)
print("500 Bills:", fiveHundred_bills)
print("200 Bills:", twoHundred_bills)
print("100 Bills:", oneHundred_bills)
print("50 Bills:", fifty_bills)
print("20 Bills:", twenty_bills)
print("10 Bills:", ten_bills)
print("5 Coins:", five_coins)
print("1 Coins:", one_coins)

# my idea was that i have the deposit amount variable and we continue subtracting it everytime we get the number of bills for each calculation
# for instance after we get how many 1000 bills in the Amount which is 19, in the next five hundred bills, we can now substract that (19 * 1000) bills from it so now it's (19863 - 19000) which we get 863 left
# now we store that 863 in our Amount so it's updated and then we can use that to get the next bill which is 500, so we just repeat that pattern and hopefully we actually get the right answer hehehe :3