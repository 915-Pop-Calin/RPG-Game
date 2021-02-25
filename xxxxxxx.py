from Characters.HumanPlayer import HumanPlayer
from Shop.Shop import Shop

player = HumanPlayer("ek")
shop = Shop(player, 5)
s = shop.find_cost_by_class("Xalatath")
print(s)