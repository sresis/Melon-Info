"""Print out all the melons in our inventory."""


from melons import melon_names, melon_seedlessness, melon_prices


def print_melon(name, seedless, price, rind_color = 'tan', weight = 2, *traits):
    """Print each melon with corresponding attribute information."""
    melon_info = {}
    melon_traits = {}
    melon_traits[price] = 1
    #melon_traits[seedless] = True
    #melon_traits[rind_color] = rind_color
    #melon_traits[weight] = weight

    
    melon_names[name] = 'x'
    melon_prices[name] = price
    melon_seedlessness[name] = seedless

 
    for melon in melon_names:
    	melon_traits[melon] = {'Price': melon_prices[melon], 
    	'Seedlessness': melon_seedlessness[melon],
    	'Rind Color': rind_color,
    	'Weight': weight}
    print(melon_traits)
    """for melon in melon_names:
    	for item in melon_traits:
    		print((value, key in melon_traits.items())"""
print_melon('Watermelon', True, 30)

