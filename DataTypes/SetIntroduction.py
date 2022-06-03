data = [
    {'name': 'zhangsan', 'age': 18,'phone':123456789},
    {'name': 'lisi','age':18,'phone':123456789},
    {'name':'wangwu','age':20,'phone': 40000},
]
print(data[1]['name'], data[2]['phone'])

user = {'name':'zhangsan',
        'address':{
            'province':'Nepal',
            'city':{
                'name':'Kathmandu',
            }

        }
        }
print(user['address']['city']['name'])
# how set and dictionary works
# values cannot be repeated in a set
# dictionary includes key values and a value assigned for the key values
# uses {} to enter values for both set and dictionary
