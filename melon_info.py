"""Print out all the melons in our inventory."""


from melons import melon_names, melon_seedlessness, melon_prices



def print_melon(name, seedless, price, rind_color = 'tan', weight = 2, *traits):
    """Print each melon with corresponding attribute information."""
    melon_info = {}
    melon_traits = {}
    
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

    # inner function to pring all items seperately
    def print_all_traits(melon_traits):
    	for key, value in melon_traits.items():
    		if type(value) is dict:
    			print(key.upper())
    			print_all_traits(value)
    		else:
    			print(f'{key}: {value}')

    print_all_traits(melon_traits)

    #	for item in melon_traits.items():
    #		print(item)
    	
    """for melon in melon_names:
    	for item in melon_traits:
    		print((value, key in melon_traits.items())"""
print_melon('Watermelon', True, 30)

