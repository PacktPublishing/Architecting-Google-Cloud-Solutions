import random

def what_to_cook_for_dinner(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        A suggestion for dinner :)
    """
    dinner_ideas = [
        'Spaghetti Squash Mac and Cheese',
        'Chicken Tostadas',
        'Pot Beef Stew',
        'Chicken Chili',
        'Spaghetti and meatballs',
        'Cajun chicken',
        'Shrimp tacos',
        'Caprese Chicken and Zucchini',
        'Meat tacos',
        'Filet mignon and Mushroom Risotto'

    ]

    choice = random.choice(dinner_ideas)
    
    return f'How about {choice} tonight?'