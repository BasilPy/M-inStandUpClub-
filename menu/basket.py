from menu.models import MultiLangText, ShoppingBasket
basket = ShoppingBasket(
    name = MultiLangText(
        eng="Basket:",
        ru="Корзина",
        kz="Себет"
    ),
    number_of_items=0,
    items_in_basket=list()
)