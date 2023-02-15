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
    item_id : str = None

    def __init__(self, name: MultiLangText, instruction: MultiLangText, category_items: list[MenuItem], item_id: str):
        self.name = name
        self.instruction = instruction
        self.category_items = category_items
        self.item_id = item_id


class Menu:
    categories: list[MenuCategory] = None

    def __init__(self, categories: list[MenuCategory]):
        self.categories = categories


