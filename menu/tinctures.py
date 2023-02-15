from menu.models import MenuItem, MultiLangText

all_tinctures = [
    MenuItem(
        name=MultiLangText(
            eng='some_tincture',
            ru='какая_то_настойка',
            kz='какая_то_настойка_kz'
        ),
        price=1500,
        item_id='absolut_j'
    ),
    MenuItem(
        name=MultiLangText(
            eng='some_tincture_2',
            ru='какая_то_настойка_2',
            kz='какая_то_настойка_kz2'
        ),
        price=1500,
        item_id='absolut_j'
    ),
    MenuItem(
        name=MultiLangText(
            eng='Gin and tonic',
            ru='ДЖИН ТОНИК',
            kz='Джин және тоник'
        ),
        price=2000,
        item_id='absolut_j'
    ),
    MenuItem(
        name=MultiLangText(
            eng='Rum with mint soda 🥃',
            ru='РОМ с мятной содовой 🥃',
            kz='Жалбыз содасы бар ром 🥃'
        ),
        price=2000,
        item_id='absolut_j'
    )
]
