# slicing = create a substring by extracting elements from another string
# indexing[] or slice()
# [start:stop:step] step is by defult 1

name = "Jahidul Hasan"

# creating a substring
# first_name = name[0]
first_name = name[0:7]
last_name = name[8:]
funky_name = name[::-1]


print(first_name)
print(last_name)
print(funky_name)

# slice()

website = "https://google.com"
website2 = "https://jahidul.info"
# slice object
slice = slice(8,-4)
print(website[slice])
print(website2[slice])