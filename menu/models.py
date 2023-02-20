class MultiLangText:
    eng = None
    ru = None
    kz = None

    def __init__(self, eng: str, ru: str, kz: str):
        self.eng = eng
        self.ru = ru
        self.kz = kz

    def get_text_by_language(self, lang):
        match lang:
            case 'eng':
                return self.eng
            case 'ru':
                return self.ru
            case 'kz':
                return self.kz


class MenuItem:
    name: MultiLangText = None
    price: float = None
    item_id = None

    def __init__(self, name: MultiLangText, price: float, item_id: str):
        self.name = name
        self.price = price
        self.item_id = item_id


class MenuCategory:
    name: MultiLangText = None
    instruction: MultiLangText = None
    category_items: list[MenuItem] = None
    item_id: str = None

    def __init__(self, name: MultiLangText, instruction: MultiLangText, category_items: list[MenuItem], item_id: str):
        self.name = name
        self.instruction = instruction
        self.category_items = category_items
        self.item_id = item_id


class Menu:
    title_categories: MultiLangText = None
    categories: list[MenuCategory] = None

    def __init__(self, title_categories: MultiLangText, categories: list[MenuCategory]):
        self.title_categories = title_categories
        self.categories = categories


class ShoppingBasket:
    name: MultiLangText = None
    number_of_items: int = None
    items_in_basket: list = None

    def __init__(self, name: MultiLangText, number_of_items: int, items_in_basket: list):
        self.name = name
        self.number_of_items = number_of_items
        self.items_in_basket = items_in_basket

    def add_new_item(self, adding_item: MenuCategory):
        # self.items_in_basket.append("-")
        self.items_in_basket.append(adding_item)
        # self.items_in_basket.append("+")

    def delete_one_item(self, removing_item: MenuCategory):

        index_of_item = self.items_in_basket.index(removing_item)
        # self.items_in_basket.pop(index_of_item-1)
        self.items_in_basket.pop(index_of_item)

        # self.items_in_basket.pop(index_of_item+1)

    def clear_all_basket(self):
        self.items_in_basket.clear()
