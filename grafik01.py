import tkinter as tk

class MovingObjectApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Движение объекта")

        self.canvas = tk.Canvas(root, width=600, height=400, bg='white')
        self.canvas.pack()

        self.start_button = tk.Button(root, text="Запуск", command=self.start_movement)
        self.start_button.pack(pady=10)

        self.object = self.canvas.create_oval(10, 180, 50, 220, fill='blue')  # Создаем объект (круг)

        # Переменные для управления движением
        self.is_moving = False
        self.target_x = 550  # Целевая позиция по оси X

        # Привязываем клавишу Enter для запуска движения
        self.root.bind('<Return>', lambda event: self.start_movement())

    def start_movement(self):
        if not self.is_moving:
            self.is_moving = True
            self.move_object()

    def move_object(self):
        if self.is_moving:
            # Получаем текущие координаты объекта
            x1, y1, x2, y2 = self.canvas.coords(self.object)

            # Двигаем объект вправо
            if x2 < self.target_x:
                self.canvas.move(self.object, 5, 0)  # Двигаем на 5 пикселей вправо
                self.root.after(50, self.move_object)  # Повторяем через 50 мс
            else:
                # Когда объект достигнет целевой точки
                self.is_moving = False
                self.show_completion_message()

    def show_completion_message(self):
        message_label = tk.Label(self.root, text="Для завершения программы нажмите Enter...", font=("Arial", 14))
        message_label.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = MovingObjectApp(root)
    root.mainloop()