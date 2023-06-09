from PyQt5.QtCore import QTime
win_x, win_y = (200, 100)
win_width, win_height = (1000, 600)

txt_hello = "Вітаю! Ви запустили додаток «тест Руф'є»"
txt_next = 'Почати'
txt_instruction = "Ця програма дозволить вам продіагностувати своє здоров'я.Першим етапом в\n пробі Руф'є є визначення частоти пульсу в стані спокою.Другий етап - фізичне\n навантаження,де ви повинні виконати 30 присідань за 45 секунд.Після серії з\n 30 присідань одразу ж проводиться вимірювання пульсу - частоти серцевих\n скорочень,а також вимірюється артеріальний тиск.Після чого дається перерва\n на кілька хвилин.Через одну - дві хвилини вимірюється частота серцевих\n скорочень.Якщо під час тесту вам стане зле варто звернутися до лікаря!" 
txt_title = "Test Ruf'e"
txt_name = " "
txt_hintname = "Введіть П.I.Б.:"
txt_hintage = "Повних років:"
txt_test1 = 'Ляжте на спину i заміряйте пульс за 15 секунд.Натисніть кнопку "Почати перший тест",шоб запустити таймер.\n Результат запишіть у відповідне поле.'
txt_test2 = 'Виконайте 30 присідань за 45 секунд.Для цього натисніть кнопку"Почати роботи присідання",щоб запустити лічильник присідань'
txt_test3 = 'Ляжте на спину i заміряйте пульс спочатку за перші 15 секунд хвилини,потім за остані 15 секунд.Хвилини без виміру пульсацій.Результати запишіть у відповідні поля'
txt_sendresults = 'Надіслати результати'
txt_hinttest1 = '0'
txt_hinttest2 = '0'
txt_hinttest3 = '0'
txt_starttest1 = 'Почати перший тест'
txt_starttest2 = 'Почати робити присідання'
txt_starttest3 = 'Почати фінальний тест'

txt_age = 'немає даних для такого віку'
txt_finalwin = 'Результати'
txt_index = "Індекс Руф'є:"
txt_workheart = 'Працездатність серця:'


txt_res1 = 'низька. Терміново зверніться до лікаря!'
txt_res2 = 'задовільна. Зверніться до лікаря!'
txt_res3 = 'середня. Можливо, варто додатково обстежитись у лікаря.'
txt_res4 = 'вище середнього'
txt_res5 = 'висока'


time = QTime(0,0,15)
timer_text = time.toString("hh:mm:ss")