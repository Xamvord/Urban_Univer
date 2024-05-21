from colorama import init
init()
from colorama import Fore, Back, Style
import time

class User:
    def __init__(self, nickname='', password='', age=0):
        self.nickname = nickname
        self.password = hash(password)  # Хэшируем пароль
        self.age = age

    def __str__(self):
        return self.nickname

    def __eq__(self, other):
        return (self.nickname == other.nickname)

class Video:
    def __init__(self, title='', duration=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, login, password):
        for user in self.users:
            if user.nickname == login and user.password == hash(password):
                self.current_user = user
                print(f"Пользователь {login} вошел в систему")
                return
        print("Неверный логин или пароль")

    def register(self, nickname, password, age):
        new_user = User(nickname, password, age)
        for user in self.users:
            if user == new_user:
                print(f"Пользователь {nickname} уже существует")
                return
        self.users.append(new_user)
        self.current_user = new_user
        print(Fore.GREEN + "Пользователь {} успешно зарегистрирован".format(nickname) + Style.RESET_ALL)

    def log_out(self):
        self.current_user = None
        print("Пользователь вышел из системы")

    def add(self, *videos):
        for video in videos:
            if video.title not in [v.title for v in self.videos]:
                self.videos.append(video)
                print(Fore.CYAN + "Видео '{}' добавлено".format(video.title) + Style.RESET_ALL)
            else:
                print(f"Видео с названием '{video.title}' уже существует")

    def get_videos(self, keyword):
        found_videos = [video.title for video in self.videos if keyword.lower() in video.title.lower()]
        if found_videos:
            print(Fore.BLUE + "По запросу '{}' найдено:".format(keyword) + Style.RESET_ALL)
        return found_videos

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт чтобы смотреть видео")
            return
        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                print(Fore.YELLOW + "Воспроизведение видео '{}':".format(title) + Style.RESET_ALL)
                for second in range(video.duration):
                    print(second + 1, end=" ")
                    time.sleep(1)  # Пауза между выводами
                print("Конец видео")
                video.time_now = 0  # Сброс текущего времени воспроизведения
                return
        print(Fore.RED + "Видео не найдено" + Style.RESET_ALL)

# Проверка кода
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(Fore.BLUE + 'Текущий пользователь:' + Style.RESET_ALL)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
