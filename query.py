"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?

    # <flask_sqlalchemy.BaseQuery object at 0x107372430>

# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?

    # An association table manage "many to many" type of relationship between two tables.
    # This table doesn't contain it's own unique private keys, it only contains private keys 
    # from the related tables which are called foreign keys in the association table.


# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the brand_id of ``ram``.
q1 = Brand.query.get('ram')

# Get all models with the name ``Corvette`` and the brand_id ``che``.
q2 = Model.query.filter(Model.name == 'Corvette', Model.brand_id == 'che').all()

# Get all models that are older than 1960.
q3 = Model.query.filter(Model.year > 1960).all()

# Get all brands that were founded after 1920.
q4 = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with ``Cor``.
q5 = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = Brand.query.filter((Brand.discontinued != None) | (Brand.founded < 1950)).all()

# Get all models whose brand_id is not ``for``.
q8 = Model.query.filter(Model.brand_id != 'for').all()



# -------------------------------------------------------------------
# Part 4: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""
    
    # models = Model.query.options(db.joinedload('brand')).all()
    models = Model.query.filter(Model.year == year).all()

    print(f"\nModels for the {year} year:")

    if models:
        for model in models:
            print(f"\n\tModel name: {model.name} (Brand: {model.brand.name} - headquaters {model.brand.headquarters})")
    else:
        print(f"No models with given yea.r")            
            

def get_brands_summary():
    """Prints out each brand name (once) and all of that brand's models,
    including their year, using only ONE database query."""
    
    all_brands = Brand.query.all()

    for brand in all_brands:            
        print(f"\nThe list of {brand.name}'s models: ")
        if brand.models:
            for model in brand.models:
                print(f"\t{model.name } {model.year}")
        else:
            print(f"\tNo models found.")


def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    search_str = '%' + mystr + '%'
    
    brands_by_name = Brand.query.filter(Brand.name.like(search_str)).all()

    return brands_by_name


def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    models = Model.query.filter((Model.year >= start_year) & (Model.year < end_year)).all()

    return models