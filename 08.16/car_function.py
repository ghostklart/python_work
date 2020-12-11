#cars or automobiles, words lost in translation...
def make_car(brand, model, **characteristics):
    characteristics['brand_name'] = brand
    characteristics['model_name'] = model
    return characteristics