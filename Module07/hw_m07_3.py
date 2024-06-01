team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total

if score_1 > score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'

# Использование % для форматирования строк
result_str1 = "В команде Мастера кода участников: %d !" % team1_num
result_str2 = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)
print(result_str1)
print(result_str2)

# Использование метода format()
result_str3 = "Команда Волшебники данных решила задач: {} !".format(score_2)
result_str4 = "Волшебники данных решили задачи за {:.1f} с !".format(team2_time)
print(result_str3)
print(result_str4)

# Использование f-строк
result_str5 = f"Команды решили {score_1} и {score_2} задач."
result_str6 = f"Результат битвы: {challenge_result}"
result_str7 = f"Сегодня было решенно {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!."
print(result_str5)
print(result_str6)
print(result_str7)
