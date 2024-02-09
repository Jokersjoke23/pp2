# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]


# 2.1 func

movie = {
    "name": "Usual Suspects", 
    "imdb": 7.0,
    "category": "Thriller"
}
def above55(movie):
    if movie['imdb'] > 5.5:
        return True
print(above55(movie))


# 2.2 func

def above_5_5_movies(movies):
    above55_list = []
    for x in movies:
        if x['imdb'] > 5.5:
            above55_list.append(x['name'])
    return above55_list
above5_5 = above_5_5_movies(movies)
for x in above5_5:
    print(x)


# 2.3 func

def category_selector(movies, a):
    category_list = []
    for x in movies:
        if a == x['category']:
            category_list.append(x['name'])
    return category_list
category = category_selector(movies, input("Select category:"))
for x in category:
    print(x)
    

# 2.4 func

def average_imdb(movies):
    cnt = 0
    for x in movies:
        cnt += x['imdb']
    cnt = cnt / len(movies)
    return round(cnt,2)
print("Average IMDB:",average_imdb(movies))


# 2.5 func

def category_imdb(movies, a):
    cnt = 0
    lencnt = 0
    for x in movies:
        if a == x['category']:
            cnt += x['imdb']
            lencnt += 1
    cnt = cnt / lencnt
    return round(cnt,2)
a = input("Select category")
print("Average IMDB:", category_imdb(movies, a))