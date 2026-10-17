
class Student:
    kilkist_studentiv = 0

    def __init__(self, imya, zrist, IQ):
        self.imya = imya
        self.zrist = zrist
        self.iq = IQ
        self.groshi = 1000
        self.znannya = 50
        self.energiya = 100
        self.shchastya = 50
        self.den = 0
        Student.kilkist_studentiv += 1

    def zrostaty(self, sm):
        self.zrist += sm

    def pratsyuvaty(self):
        self.groshi += 300
        self.energiya -= 20
        self.shchastya -= 5
        print(f"{self.imya} попрацював і заробив 300 грн.")

    def vidpochyvaty(self):
        if self.groshi >= 200:
            self.groshi -= 200
            self.energiya = min(100, self.energiya + 30)
            self.shchastya = min(100, self.shchastya + 20)
            print(f"{self.imya} відпочив і витратив 200 грн.")
        else:
            print(f"{self.imya} не вистачає грошей на відпочинок.")
            self.pratsyuvaty()

    def navchatysya(self):
        self.znannya = min(100, self.znannya + 15)
        self.energiya -= 15
        self.shchastya -= 5
        print(f"{self.imya} позаймався навчанням.")

    def prozhyty_den(self):
        self.den += 1
        self.energiya -= 5
        self.shchastya -= 2

        if self.groshi < 300:
            self.pratsyuvaty()

        if self.znannya < 40:
            self.navchatysya()

        if self.energiya < 40:
            self.vidpochyvaty()

        if self.shchastya < 30 and self.groshi >= 200:
            self.vidpochyvaty()

        self.energiya = max(0, min(100, self.energiya))
        self.shchastya = max(0, min(100, self.shchastya))

    def prozhyty_rik(self):
        for _ in range(365):
            self.prozhyty_den()

        print(f"\nРік життя {self.imya} завершено!")
        print(self)

    def __str__(self):
        return (
            f"Ім'я: {self.imya}\n"
            f"Прожито днів: {self.den}\n"
            f"Зріст: {self.zrist} см\n"
            f"Рівень IQ: {self.iq}\n"
            f"Гроші: {self.groshi} грн.\n"
            f"Знання: {self.znannya}/100\n"
            f"Енергія: {self.energiya}/100\n"
            f"Щастя: {self.shchastya}/100"
        )


тимофій = Student("Тимофій", 172, 333)
марія = Student("Марія", 160, 26)

тимофій.prozhyty_rik()
print()
марія.prozhyty_rik()
