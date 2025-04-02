import tkinter as tk

class BouncingBallApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Отскакивающий шарик")

        self.canvas = tk.Canvas(root, width=400, height=400, bg='white')
        self.canvas.pack()

        # Создаем шарик (круг)
        self.ball = self.canvas.create_oval(175, 0, 225, 50, fill='blue')

        # Переменные для управления движением
        self.gravity = 0.5  # Ускорение свободного падения
        self.velocity = 0   # Начальная скорость
        self.is_bouncing = False
        self.bounce_count = 5  # Количество отскоков

        # Кнопка для запуска падения
        self.start_button = tk.Button(root, text="Запустить", command=self.start_bouncing)
        self.start_button.pack(pady=10)

    def start_bouncing(self):
        if not self.is_bouncing:
            self.is_bouncing = True
            self.velocity = 0  # Сбрасываем скорость перед началом
            self.bounce()

    def bounce(self):
        if self.is_bouncing and self.bounce_count > 0:
            # Увеличиваем скорость под действием гравитации
            self.velocity += self.gravity

            # Получаем текущие координаты шарика
            x1, y1, x2, y2 = self.canvas.coords(self.ball)

            # Двигаем шарик вниз на текущую скорость
            if y2 < 400:  # Проверяем не вышел ли шарик за пределы окна
                self.canvas.move(self.ball, 0, self.velocity)
                self.root.after(20, self.bounce)  # Повторяем через 20 мс
            else:
                # Отскок: меняем направление скорости и уменьшаем её
                if abs(self.velocity) > 1:  # Проверяем минимальную скорость для отскока
                    self.velocity = -self.velocity * 0.7  # Отскок с потерей энергии (уменьшаем скорость)
                    self.bounce_count -= 1  # Уменьшаем количество оставшихся отскоков
                    # Двигаем шарик на уровень земли (чтобы не застревал)
                    self.canvas.move(self.ball, 0, -y2 + 400)
                    self.root.after(20, self.bounce)  # Продолжаем движение после отскока
                else:
                    # Останавливаем движение если скорость слишком мала
                    self.is_bouncing = False

if __name__ == "__main__":
    root = tk.Tk()
    app = BouncingBallApp(root)
    root.mainloop()