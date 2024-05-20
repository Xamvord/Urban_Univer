from threading import Thread
import time

class Knight(Thread):
    def __init__(self, name, skill, *args, **kwargs):
        super(Knight, self).__init__(*args, **kwargs)
        self.name = name
        self.skill = skill
        self.remaining_enemies = 100

    def run(self):
        print(f"{self.name}: на нас напали!", flush=True)
        days = 0
        while self.remaining_enemies > 0:
            days += 1
            self.remaining_enemies -= self.skill
            print(f"{self.name} сражается {days}-й день... У него осталось {self.remaining_enemies} врагов.", flush=True)
            time.sleep(1)
        print(f"{self.name} одержал победу спустя {days} дней!", flush=True)

knight1 = Knight("Sir Lancelot", 10)
knight2 = Knight("Sir Galahad", 20)

knight1.start()
knight2.start()

print('Разгорелась кровавая битва...', flush=True)

knight1.join()
knight2.join()

print("Все битвы закончились!")
