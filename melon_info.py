"""Print out all the melons in our inventory."""


from melons import melon_names, melon_seedlessness, melon_prices





def print_melon(name, seedless, price, rind_color = 'tan', 
	weight = 2, skin_color = 'pink', *traits):
    """Print each melon with corresponding attribute information."""
   
    melon_traits = {}
    
    # adds dictionary of rind color(exists only for new melon)
    melon_rind_color = {
    	name: rind_color
    }
    # adds dictionary of weight(exists only for new melon)

    melon_weight = {
    	name: weight
    }

    #adds dictionary of skin color (exits only for new melon)
    melon_skin_color = {
    	name: skin_color
    }

    # sets values in names/prices/seedless dictionaries for the new melon
    melon_names[name] = 'x'
    melon_prices[name] = price
    melon_seedlessness[name] = seedless
     
 	# assigns values for each information piece(key) for melons
 	# if weight, rind color, skin color values don't exist, print 'None'
    for melon in melon_names:
    	melon_traits[melon] = {'Price': melon_prices[melon], 
    	'Seedlessness': melon_seedlessness[melon],
    	'Rind Color': melon_rind_color.get(melon, 'None'),
    	'Weight': melon_weight.get(melon, 'None'),
    	'Skin Color': melon_skin_color.get(melon, 'None')}

    # inner function to pring all items seperately
    def print_all_traits(melon_traits):
    	for key, value in melon_traits.items():
    		if type(value) is dict:
    			print(key.upper())
    			print_all_traits(value)
    		else:
    			print(f'{key}: {value}')

    print_all_traits(melon_traits)


print_melon('Watermelon', True, 30)

