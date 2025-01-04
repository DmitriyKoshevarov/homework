from time import sleep

class User:
    def __init__(self,nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

    def hash_password(self, password):
        return hash(password)

    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = {}
        self.videos = []
        self.current_user = None

    def list_users(self):
        print('Список пользователей: ')
        for nickname, (password, age) in self.users.items():
            print(f'Никнейм: {nickname}, пароль в хэшированном виде: {password}, возраст: {age}')

    def log_in(self, nickname, password):
        login = input("Введите логин: ")
        password = input("Введите пароль: ")
        if nickname in self.users:
            if hash(password) == self.users[nickname][0]:
                self.current_user = nickname

    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f'Пользователь {nickname} уже существует')
        else:
            new_user = User(nickname, password, age)
            self.users[nickname] = [new_user.password, age]
            self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, search):
        search_result = [v.title for v in self.videos if search.lower() in v.title.lower()]
        return search_result

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео.")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста, покиньте страницу.")
                    return

                for time_now in range(1, video.duration + 1):
                    print(time_now, end=' ')
                    video.time_now += 1
                    sleep(1)
                print("Конец видео.")
                video.time_now = 0
                return

        print(f"Видео '{title}' не найдено.")


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

print(ur.current_user)



# Попытка воспроизведения несуществующего видео

ur.watch_video('Лучший язык программирования 2024 года!')