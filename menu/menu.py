from menu.cocktails import all_cocktails
from menu.types_of_beer import all_bears
from menu.types_of_cider import all_ciders
from menu.tinctures import all_tinctures
from menu.snacks import all_snacks
from menu.wines import all_wines
from menu.non_alco_drinks import all_non_alco
from menu.models import Menu, MenuCategory, MultiLangText


menu = Menu(
    categories=[
        MenuCategory(
            category_name='tinctures',
            instruction=MultiLangText(
                eng='Choose a tincture 🍋🍍🍇 50мл:',
                ru='Выберите настойку 🍋🍍🍇 50мл:',
                kz='Тұнбаны таңдаңыз 🍋🍍🍇 50мл:',
            ),
            category_items=all_tinctures,
        ),
        MenuCategory(
            category_name='bears',
            instruction=MultiLangText(
                eng='Choose a bear 🍺 500мл:',
                ru='Выберите пиво 🍺 500мл:',
                kz='Сыраны таңдаңыз 🍺 500мл:',
            ),
            category_items=all_bears,
        ),
        MenuCategory(
            category_name='ciders',
            instruction=MultiLangText(
                eng='Choose a ciders 🍏🍺🍐 500мл:',
                ru='Выберите сидр 🍏🍺🍐 500мл:',
                kz='Сидр таңдаңыз 🍏🍺🍐 500мл:',
            ),
            category_items=all_ciders,
        ),
        MenuCategory(
            category_name='cocktails',
            instruction=MultiLangText(
                eng='Choose a cocktail 🍸 400мл:',
                ru='Выберите коктейль 🍸 400мл:',
                kz='Коктейльді таңдаңыз 🍸 400мл:',
            ),
            category_items=all_cocktails,
        ),
        MenuCategory(
            category_name='snacks',
            instruction=MultiLangText(
                eng='Choose a snack 🍴',
                ru='Выберите snack 🍴',
                kz='Жеңіл тамақ таңдаңыз 🍴',
            ),
            category_items=all_snacks,
        ),
        MenuCategory(
            category_name='wines',
            instruction=MultiLangText(
                eng='Choose a wine ',
                ru='Выберите вино ',
                kz='Шарап таңдаңыз ',
            ),
            category_items=all_wines,
        ),
        MenuCategory(
            category_name='non_alcoholic',
            instruction=MultiLangText(
                eng='Choose a non alco drink ',
                ru='Выберите безалкогольный напиток',
                kz='Алкогольсіз сусынды таңдаңыз',
            ),
            category_items=all_non_alco,
        ),
    ]
)
