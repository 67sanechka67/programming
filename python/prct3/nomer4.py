import random


class CrewMember:
    def __init__(self, name, role, skills, health=100):
        self.name = name
        self.role = role
        self.skills = skills  # Словарь вида: {"ремонт": 80, "пилотирование": 90}
        self.health = health

    def take_damage(self, amount):
        self.health = max(0, self.health - amount)
        print(f"Член экипажа {self.name} ({self.role}) получил {amount} урона. Здоровье: {self.health}%")

    def heal(self, amount):
        self.health = min(100, self.health + amount)
        print(f"Член экипажа {self.name} восстановил здоровье до {self.health}%.")

    def is_alive(self):
        return self.health > 0


class SpaceShip:
    def __init__(self, name, fuel=100, hull=100, speed=0):
        self.name = name
        self.fuel = fuel
        self.hull = hull
        self.speed = speed
        self.crew = []

    def add_crew_member(self, member):
        self.crew.append(member)
        print(f"{member.name} ({member.role}) зачислен на борт корабля '{self.name}'.")

    def fly(self, distance):
        fuel_needed = distance * 0.5
        if self.fuel >= fuel_needed:
            self.fuel -= fuel_needed
            self.speed = 50000
            print(f"Корабль '{self.name}' преодолел {distance} тыс. км. Остаток топлива: {self.fuel:.1f}%")
            return True
        else:
            print("Недостаточно топлива для продолжения полета!")
            self.speed = 0
            return False

    def take_damage(self, amount):
        self.hull = max(0, self.hull - amount)
        print(f"Корпус корабля '{self.name}' поврежден на {amount}%! Состояние корпуса: {self.hull}%")

    def repair(self):
        # Ищем живого инженера для ремонта
        engineers = [m for m in self.crew if m.role == "инженер" and m.is_alive()]
        if engineers:
            skill_bonus = engineers[0].skills.get("ремонт", 10) // 4
            self.hull = min(100, self.hull + skill_bonus)
            print(f"Инженер {engineers[0].name} починил корпус. Текущая прочность: {self.hull}%")
        else:
            print("Ремонт невозможен: на борту нет боеспособного инженера.")

    def is_operational(self):
        alive_crew = any(member.is_alive() for member in self.crew)
        return self.hull > 0 and self.fuel > 0 and alive_crew


class Mission:
    def __init__(self, goal, total_distance, reward_resources):
        self.goal = goal
        self.total_distance = total_distance
        self.reward_resources = reward_resources
        self.events = [
            "встреча с астероидами",
            "авария в двигательном отсеке",
            "спокойный космос",
            "найден дрейфующий топливный бак"
        ]

    def trigger_event(self, ship):
        event = random.choice(self.events)
        print(f"\n[СОБЫТИЕ]: {event.capitalize()}!")

        if event == "встреча с астероидами":
            # Проверяем навык пилота для уклонения
            pilots = [m for m in ship.crew if m.role == "пилот" and m.is_alive()]
            if pilots and pilots[0].skills.get("пилотирование", 0) > 75:
                print(f"Пилот {pilots[0].name} мастерски увел корабль от астероидов!")
            else:
                ship.take_damage(30)

        elif event == "авария в двигательном отсеке":
            ship.take_damage(20)
            if ship.crew:
                victim = random.choice([m for m in ship.crew if m.is_alive()])
                victim.take_damage(25)
            ship.repair()

        elif event == "найден дрейфующий топливный бак":
            ship.fuel = min(100, ship.fuel + 20)
            print(f"Запас топлива пополнен! Текущий уровень: {ship.fuel:.1f}%")

        else:
            print("Полет проходит в штатном режиме.")

    def start(self, ship):
        print(f"=== Старт миссии: '{self.goal}' (Дистанция: {self.total_distance} тыс. км) ===")
        step_distance = 50
        traveled = 0

        while traveled < self.total_distance:
            if not ship.is_operational():
                print("\n[ПРОВАЛ]: Корабль не может продолжать миссию.")
                return False

            if not ship.fly(step_distance):
                print("\n[ПРОВАЛ]: Закончилось топливо.")
                return False

            traveled += step_distance
            if traveled < self.total_distance:
                self.trigger_event(ship)

        if ship.is_operational():
            print(f"\n[УСПЕХ]: Миссия '{self.goal}' выполнена! Получены ресурсы: {self.reward_resources}")
            return True
        else:
            print("\n[ПРОВАЛ]: Корабль уничтожен на подлете к цели.")
            return False


# --- Демонстрация работы симулятора ---

# 1. Создаем корабль и команду
ship = SpaceShip("Аврора", fuel=100, hull=100)
pilot = CrewMember("Алекс", "пилот", {"пилотирование": 85})
engineer = CrewMember("Елена", "инженер", {"ремонт": 80})

ship.add_crew_member(pilot)
ship.add_crew_member(engineer)

# 2. Создаем и запускаем миссию
mars_mission = Mission("Доставка груза на Марс", total_distance=150, reward_resources="500 ед. титана")
mars_mission.start(ship)
