laptop_info = {
	'macbook': {
    	'manufacturer': 'apple',
        'processor': 'intel',
        'disk': 'ssd'
        },
    'legion 5': {
    	'manufacturer': 'lenovo',
        'processor': 'amd',
        'disk': 'ssd+hdd'
        }	
}

for laptop, info in laptop_info.items():
    print(f"\n{laptop.title()} characteristics are:")
    manuf = info['manufacturer']
    proc = info['processor']
    disc = info['disk']
    print(f"{manuf}\n{proc}\n{disc}")

