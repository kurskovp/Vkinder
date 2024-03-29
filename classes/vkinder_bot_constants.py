PHRASES = dict(do_you_like_it='Нравится? \n["да" | "нет" | "бан" | "выход"]',
               found_x_peoples='Найдено {} людей.',
               last_seen_x_days_ago='\nПоследний вход: {} дней назад',
               last_seen='\nПоследний вход: ',
               x_days_ago='{} дней назад',
               today='сегодня',
               yesterday='вчера',
               day_before_yesterday='позавчера',
               at_this_week='на неделе',
               x_months_ago='{} месяц(ев) назад',
               x_years_ago='{} год(а) назад',
               found_x_peoples_x_new_x_liked_x_disliked_x_banned='Найдено всего людей: {}\n(новых: {}, лайкнутых: {}, '
                                                                 'отклоненных: {}, забаненых: {})',
               no_peoples_found='Людей по вашему запросу не найдено.',
               no_new_peoples_found='Новых людей по вашему запросу не найдено. Используйте список оценок для '
                                    'повторной оценки людей. Или начните поиск сначала.',
               city_x_sex_x_status_x_age_xx="Город '{}', пол '{}', статус '{}', возраст от {} до {}",
               x_x_x_from_x_to_x="{}, {}, {}, от {} до {}",
               started_search_peoples='Начинаем поиск пользователей...',
               minimal_age_more_maximal_age='Минимальный возраст больше максимального.',
               you_chosen_min_age_x_and_max_age_x='Вы выбрали возраст от {} до {}.',
               error_in_age='Вы ввели ошибочный возраст. Начнем сначала.',
               enter_max_age_from_x_127='Введите максимальный возраст \n[число от {} до 127 | "/назад" | "выход"]: ',
               enter_min_age_from_0_127='Введите минимальный возраст \n[число от 0 до 127 | "/назад" | "выход"]: ',
               you_chosen_love_status_x='Вы выбрали статус человека: {}',
               no_such_love_status_in_list='Такого номера в списке нет. Введите заново число или напишите "выход".',
               choose_love_status_number='Введите номер статуса человека: \n[№ пп | "нет" | "выход"]',
               you_chosen_sex_x='Вы выбрали пол: {}.',
               no_such_sex_in_list='Такого номера в списке нет. Введите заново число или напишите "выход".',
               choose_sex_number='Введите номер пола человека \n[№ пп | "назад" | "выход"]',
               you_chosen_city_x='Вы выбрали город: {}.',
               you_chosen_country_x='Вы выбрали страну: {}.',
               no_such_city_in_list='Такого номера в списке нет. Введите заново число или напишите "выход".',
               no_such_country_in_list='Такого номера в списке нет. Введите заново число или напишите "выход".',
               choose_city_number='Введите номер города \n[№ пп | "назад" | "выход"]',
               choose_country_number='Введите номер страны \n[№ пп | "назад" | "выход"]',
               choose_search_history_number='Введите номер поиска \n[№ пп | "назад" | "выход"]',
               no_search_history='У вас пока нет истории поиска',
               no_such_city_name='Городов с таким названием не найдено.',
               no_such_country_name='Страны с таким названием не найдено.',
               enter_city_name_in_x='Введите название города в стране: {}, или смените страну поиска'
                                    '\n[название города | "страна" | "/назад" | "выход"]',
               enter_country_name='Введите название название страны или часть названия для поиска '
                                  '\n[название страны | "/назад" | "выход"]',
               do_you_want_to_find_pair='Поскольку вы у нас еще ничего не искали, расскажу что вы можете писать ответы '
                                        'мне в чат либо нажимать на кнопки, если они вам видны. Текстовые варианты '
                                        'ответов перечислены под каждым моим вопросом. Из любого диалога вы можете '
                                        'выйти написав мне "Стоп".'
                                        '\n\nХотите найти свою вторую половинку?\n["да" | "нет"]',
               no_such_history_in_list='Такого номера в списке нет. Введите заново число или напишите "выход".',
               you_have_search_history='Могу начать новый поиск половинки или показать вашу историю поиска'
                                       '\n["поиск" | "история" | "выход"]',
               greetings_x='Привет {}! Я чат-бот VKinder.',
               sorry_x_you_was_absent_for_x_seconds='{}, к сожалению вас не было слышно более {} секунд. Давайте '
                                                    'начнем сначала. ',
               well_lets_start_again='Похоже вы всех посмотрели, давайте попробуем снова.',
               sorry_i_dont_understand_you='Извините, я вас не понял. Попробуйте другой ответ.',
               goodbye_x='Приятно было пообщаться {}. До свидания!'
               )
STATUSES = dict(has_contacted=0, invited=1, city_input_wait=2, city_choose_wait=3, sex_choose_wait=4,
                status_choose_wait=5, min_age_input_wait=6, max_age_input_wait=7, loading_users=8, decision_wait=9,
                search_history_input_wait=10, country_input_wait=11, country_choose_wait=12)
MAX_MSG_SIZE = 4096
COMMANDS = {
    'yes': [['✓ Да', '+', 'yes'], 'positive'],
    'no': [['✘ Нет', '-', 'no'], 'primary'],
    'back': [['↩ Назад', 'назад', '/назад', 'back'], 'secondary'],
    'new search': [['✚ Новый поиск', 'поиск', 'искать', 'new search'], 'positive'],
    'show history': [['⌛ Поиск из истории', 'история', 'историю', 'show history'], 'primary'],
    'quit': [['❌ Выход', 'выход', '/выход', 'выйти', 'хватит', 'стоп', 'пока', 'финиш', 'stop', 'finish'], 'secondary'],
    'ban': [['☠ Бан', 'бан', 'ban'], 'negative'],
    'woman': [['♀ Женщина', 'женщина', 'ж', 'woman'], 'positive'],
    'man': [['♂ Мужчина', 'мужчина', 'м', 'man'], 'positive'],
    'anybody': [['⚥ Неважно', 'неважно', 'любой', 'anybody', 'any'], 'positive'],
    'liked': [['Лайкнутые', 'лайкнутые', 'liked'], 'secondary'],
    'disliked': [['Отклоненные', 'отклоненные', 'disliked'], 'secondary'],
    'banned': [['Забаненые', 'забаненые', 'banned'], 'secondary'],
    'country': [['☭ Выбор страны', 'страна', '/страна', 'country'], 'primary']
}