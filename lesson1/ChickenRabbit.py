'''
amount = 83
feet = 240
83 * 4 - 240 = 92
92 / 2 = 46 雞
83 - 46 = 37 兔
'''
def calc(amount, feet):
    chicken = (amount * 4 - feet) / 2
    rabbit = amount - chicken
    print("雞: %d 兔: %d" % (chicken, rabbit))

calc(83, 240)
calc(60, 180)


