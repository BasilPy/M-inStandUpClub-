from menu.models import MenuItem, MultiLangText

all_tinctures = [
    MenuItem(
        name=MultiLangText(
            eng='Cherry 🍒 1500₸',
            ru='Вишня 🍒 1500₸',
            kz='Шие 🍒 1500₸'
        ),
        price=1500,
        item_id='cherry'
    ),
    MenuItem(
        name=MultiLangText(
            eng='Currant ◇ 1500₸',
            ru='Смородина ◇ 1500₸',
            kz='Қарақат ◇ 1500₸'
        ),
        price=1500,
        item_id='currant'
    ),
    MenuItem(
        name=MultiLangText(
            eng='Sea buckthorn ◇ 1500₸',
            ru='Облепиха ◇ 1500₸',
            kz='Теңіз шырғаны ◇ 1500₸'
        ),
        price=1500,
        item_id='sea_buckthorn'
    ),
    MenuItem(
        name=MultiLangText(
            eng='Cranberry ◇ 1500₸',
            ru='Клюква ◇ 1500₸',
            kz='Мүкжидек ◇ 1500₸'
        ),
        price=1500,
        item_id='cranberry'
    )
]
