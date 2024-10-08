"""Maps: Data Abstractions"""



from utils import mean

# Phase 1: Data Abstraction #



def make_review(restaurant_name, score):
    """Return a review data abstraction."""
    return [restaurant_name, score]

def review_restaurant_name(review):
    """Return the restaurant name of the review, which is a string."""
    return review[0]

def review_score(review):
    """Return the number of stars given by the review, which is a
    floating point number between 1 and 5."""
    return review[1]


# Users

def make_user(name, reviews):
    """Return a user data abstraction."""
    return [name, {review_restaurant_name(r): r for r in reviews}]

def user_name(user):
    """Return the name of the user, which is a string."""
    return user[0]

def user_reviews(user):
    """Return a dictionary from restaurant names to reviews by the user."""
    return user[1]


### === +++ USER ABSTRACTION BARRIER +++ === ###

def user_reviewed_restaurants(user, restaurants):
    """Return the subset of restaurants reviewed by user.

    Arguments:
    user -- a user
    restaurants -- a list of restaurant data abstractions
    """
    names = list(user_reviews(user))
    return [r for r in restaurants if restaurant_name(r) in names]

def user_score(user, restaurant_name):
    """Return the score given for restaurant_name by user."""
    reviewed_by_user = user_reviews(user)
    user_review = reviewed_by_user[restaurant_name]
    return review_score(user_review)


# Restaurants

def make_restaurant(name, location, categories, price, reviews):
    """Return a restaurant data abstraction."""
    return {
        'name': name,
        'location': location,
        'categories': categories,
        'price': price,
        'reviews': reviews
    }

def restaurant_name(restaurant):
    """Return the name of the restaurant, which is a string."""
    return restaurant['name']

def restaurant_location(restaurant):
    """Return the location of the restaurant, which is a list containing
    latitude and longitude."""
    return restaurant['location']

def restaurant_categories(restaurant):
    """Return the categories of the restaurant, which is a list of strings."""
    return restaurant['categories']

def restaurant_price(restaurant):
    """Return the price of the restaurant, which is a number."""
    return restaurant['price']

def restaurant_scores(restaurant):
    """Return a list of scores, which are numbers from 1 to 5, of the
    restaurant based on the reviews of the restaurant."""
    return [review_score(r) for r in restaurant['reviews']]



### === +++ RESTAURANT ABSTRACTION BARRIER +++ === ###

def restaurant_num_scores(restaurant):
    """Return the number of scores for restaurant."""
    return len(restaurant_scores(restaurant))

def restaurant_mean_score(restaurant):
    """Return the average score for restaurant."""
    return mean(restaurant_scores(restaurant))
