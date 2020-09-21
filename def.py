print('---------8-1')


def display_message():
    print('I study python')


display_message()

print('----------8-2')


def favorite_book(book_name):
    print('i am looking at '+book_name)


favorite_book('Study Spring Boot')
favorite_book('Study Spring Clound')


print('------------------8-3')


def make_shirt(size, char='I Love Python'):
    print('The T-shirt size is '+str(size)+' with printing '+char)


make_shirt('M','Hello World')
make_shirt('L')
make_shirt(size='XL')
make_shirt(size='S', char='Hello Sky~')
# make_shirt(char='Hello') --> Exception by missing size argument


print('------------8-6')


def city_country(city_name, country_name):
    print(city_name+' , '+country_name)


city_country('Guangzhou','China')
city_country(city_name='Beijing', country_name='China')


print('-------------8-7')


def make_album(singer_name, cd_name, song_count=''):
    if song_count:
        print(cd_name+' with '+singer_name+' has '+str(song_count)+' songs')
    else:
        print(singer_name+' has cd named '+cd_name)


make_album('becky','first_CD')
make_album(cd_name='secondCD', singer_name='gary')
make_album('Nannnan',cd_name='HelloWorld',song_count=8)


print('-----------8-9')


def show_magicians(names):
    print('=====start printing ====')
    for name in names:
        print('Hello '+name)
    if 'Gary' not in names:
        names.append('Gary')

magicians = ['becky','nannan','Yangyang']
show_magicians(magicians[:])
print("magician size is "+str(len(magicians)))
show_magicians(magicians)
print("magician size is "+str(len(magicians)))
show_magicians(magicians)
print("magician size is "+str(len(magicians)))


print('------------8-12')


def sanwich(user_name, *toppings):
    print(user_name+' ordered sanwichi ')
    for topping in toppings:
        print('- '+topping)


sanwich('becky','egg','apple')
sanwich('gary','egg','lemon','milk')

print('------------8-13')


def build_profile(first_name,last_name,**names):
    mapping = {'first': first_name, 'last': last_name}
    for key, value in names.items():
        mapping[key] = value
    return mapping


user_profile = build_profile('albert','einstein',location='guangzhou',country='China')
print(user_profile)

