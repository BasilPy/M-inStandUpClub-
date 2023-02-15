from menu.models import MenuItem, MultiLangText

all_cocktails = [
    MenuItem(
        name=MultiLangText(
            eng='Apple 🍎 1000₸',
            ru='Яблоко 🍎 1000₸',
            kz='Алма 🍎 1000₸'
        ),
        price=1000,
        item_id='apple_j'
    ),
    MenuItem(
        name=MultiLangText(
            eng='Cherry 🍒 1000₸',
            ru='Вишня 🍒 1000₸',
            kz='Шие 🍒 1000₸'
        ),
        price=1000,
        item_id='cherry_j'
    ),
    MenuItem(
        name=MultiLangText(
            eng='Orange 🍊 1000₸',
            ru='Апєльсин 🍊 1000₸',
            kz='Апельсин 🍊 1000₸'
        ),
        price=1000,
        item_id='orange_j'
    ),
]