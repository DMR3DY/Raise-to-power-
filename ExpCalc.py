initial = int(input("Waht would you like your initial number to be:"))
power = int(input("what power would you like to raise the initial number to: "))

def raise_to_power(init, pow): 
    """raising init to pow"""
    print(init ** pow)

raise_to_power(initial, power)