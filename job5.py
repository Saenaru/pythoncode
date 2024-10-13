import random
from pathlib import Path

from faker import Faker

import file_operations


def main():
    folder_name = 'charsheet'
    new_folder = Path(folder_name)
    new_folder.mkdir(exist_ok=True)

    fake = Faker("ru_RU")

    custom_font = {
        'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠', 'г': 'г͒͠', 'д': 'д̋',
        'е': 'е͠', 'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋', 'и': 'и',
        'й': 'й͒͠', 'к': 'к̋̋', 'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
        'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠', 'с': 'с͒', 'т': 'т͒',
        'у': 'у͒͠', 'ф': 'ф̋̋', 'х': 'х͒͠', 'ц': 'ц̋', 'ч': 'ч̋͠',
        'ш': 'ш͒͠', 'щ': 'щ̋', 'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
        'э': 'э͒͠', 'ю': 'ю̋͠', 'я': 'я̋', 'А': 'А͠', 'Б': 'Б̋',
        'В': 'В͒͠', 'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е', 'Ё': 'Ё͒͠',
        'Ж': 'Ж͒', 'З': 'З̋̋', 'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
        'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒', 'О': 'О̋', 'П': 'П̋͠',
        'Р': 'Р̋͠', 'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠', 'Ф': 'Ф̋̋',
        'Х': 'Х͒͠', 'Ц': 'Ц̋', 'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
        'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋', 'Э': 'Э͒͠', 'Ю': 'Ю̋͠',
        'Я': 'Я̋', ' ': ' '
    }

    options = [
        'Стремительный прыжок', 'Электрический выстрел', 'Ледяной удар',
        'Стремительный удар', 'Кислотный взгляд', 'Тайный побег',
        'Ледяной выстрел', 'Огненный заряд'
    ]

    for chars in range(1, 11):
        random_selections = random.sample(options, 3)
        runic_skills = []

        for random_selection in random_selections:
            styled_skill = ""
            for char in random_selection:
                styled_skill += custom_font.get(char, char)
            runic_skills.append(styled_skill)

        context = {
            "first_name": fake.first_name_male(),
            "last_name": fake.last_name_male(),
            "job": fake.job(),
            "town": fake.city(),
            "strength": fake.random_int(min=3, max=18),
            "agility": fake.random_int(min=3, max=18),
            "endurance": fake.random_int(min=3, max=18),
            "intelligence": fake.random_int(min=3, max=18),
            "luck": fake.random_int(min=3, max=18),
            "skill_1": runic_skills[0],
            "skill_2": runic_skills[1],
            "skill_3": runic_skills[2]
        }

        filename = new_folder / f"char_{chars}.svg"
        file_operations.render_template("charsheet.svg", filename, context)


if __name__ == '__main__':
    main()