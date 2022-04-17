""" import practice44_module

practice44_module.price(3)
practice44_module.price_morning(4)
practice44_module.price_soldier(5) """


""" import practice44_module as mv

mv.price(3)
mv.price_morning(4)
mv.price_soldier(5) """


""" from practice44_module import *

price(3)
price_morning(4)
price_soldier(5) """


""" from practice44_module import price, price_morning

price(5)
price_morning(6) """


from practice44_module import price_soldier as price

price(5)