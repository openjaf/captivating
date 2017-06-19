__author__ = 'yuriq'

import json

f = open('orders_orig.txt')
orders = json.load(f)
f.close()

# Fixing hotel names
HOTELS = {
    'PARQUE CENTRAL': 'IBEROSTAR PARQUE CENTRAL',
    'CASA PARTICULAR PLAYA LARGA - ERNESTO DELGADO Y YODAINES': 'CASA PARTICULAR PLAYA LARGA - CASA ERNESTO DELGADO',
    'CASA PARTICULAR SANTIAGO DE CUBA - CASA YULIET RAMOS': 'CASA PARTICULAR SANTIAGO DE CUBA - CASA YULIET',
    'CASA PARTICULAR TRINIDAD - DEBORAH Y JOSE': 'CASA PARTICULAR TRINIDAD - CASA DEBORAH Y JOSE',
    'CASA PARTICULAR SUPERIOR TRINIDAD - CASA REAL 54': 'CASA PARTICULAR TRINIDAD - CASA REAL 54',
    'CASA PARTICULAR HAVANA - SUPERIOR - CASA HOSTAL HAVANA 101': 'CASA PARTICULAR HAVANA - CASA HOSTAL HABANA 101',
    'CASA PARTICULAR CIENFUEGOS - VILLA MARIA': 'CASA PARTICULAR CIENFUEGOS - CASA VILLA MARIA',
    'SEVILLA': 'MERCURE SEVILLA',
    'NACIONAL': 'HOTEL NACIONAL DE CUBA',

}

# Others
OTHERS = {
	'CUBA REPRESENTATIVE SERVICE FEE': 'CUBA REPRESENTATION SERVICE FEE'} 
	
for o in orders:
    for ol in o['order_lines']:
        if ol['product_name'].upper() in HOTELS.keys():
            print "Correcting ", ol['product_name'], 'to ', HOTELS[ol['product_name']]
            ol['product_name'] = HOTELS[ol['product_name']]
        if ol['product_name'].upper() in OTHERS.keys():
            print "Correcting ", ol['product_name'], 'to ', OTHERS[ol['product_name']]
            ol['product_name'] = OTHERS[ol['product_name']]
            

# Fixing tourist cards
for o in orders:
    for ol in o['order_lines']:
        if ol['product_category'] == 'Tourist Card':
            ol['product_name'] = 'Tourist Card'
            ol['start_date'] = o['start_date']

# Fixing categories
CATEGORIES = {
    'Car hire': 'Car',
    'Car Hire': 'Car',
    'Rep Fee': 'Miscellaneous',
    'Extra': 'Miscellaneous',
    'Tour': 'Package',
    'tour': 'Package',
    'Casa': 'Hotel',
    'casa': 'Hotel',
    'Tourist Card': 'Miscellaneous',
    'Excursion': 'Activity'
}

for o in orders:
    for ol in o['order_lines']:
        if ol['product_category'] in CATEGORIES.keys():
            ol['product_category'] = CATEGORIES[ol['product_category']]
            
PARTNERS = {
	'Direct Customer Eur': 'DESTINATION CUBA'
}

for o in orders:
	if o['client'] in PARTNERS.keys():
		print "Correcting ", o['client'], 'to ', PARTNERS[o['client']]
		o['client'] = PARTNERS[o['client']]


f = open('orders_mod.txt', 'w+')
json.dump(orders, f)
f.close()