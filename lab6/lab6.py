import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.filedialog import asksaveasfilename
import openpyxl
from docx import Document

# Пакет geometry с модулями rectangle, triangle, trapezoid
class Geometry:
    @staticmethod
    def rectangle_area(a, b):
        return a * b

    @staticmethod
    def rectangle_inscribed_radius(a, b):
        return min(a, b) / 2

    @staticmethod
    def rectangle_circumscribed_radius(a, b):
        return (a**2 + b**2)**0.5 / 2

    @staticmethod
    def triangle_area(a, b, c):
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c))**0.5

    @staticmethod
    def triangle_inscribed_radius(a, b, c):
        area = Geometry.triangle_area(a, b, c)
        return area / ((a + b + c) / 2)

    @staticmethod
    def triangle_circumscribed_radius(a, b, c):
        area = Geometry.triangle_area(a, b, c)
        return (a * b * c) / (4 * area)

    @staticmethod
    def trapezoid_area(a, b, h):
        return ((a + b) / 2) * h

    @staticmethod
    def trapezoid_inscribed_radius(a, b, h):
        if a == b:
            return h / 2
        return None

    @staticmethod
    def trapezoid_circumscribed_radius(a, b, h):
        return ((a**2 + b**2 + 2*h**2)**0.5) / 2


def save_results(data):
    file_type = [('Документ Word', '*.docx'), ('Таблица Excel', '*.xlsx')]
    file_path = asksaveasfilename(filetypes=file_type, defaultextension=file_type)

    if file_path.endswith('.docx'):
        doc = Document()
        doc.add_heading('Результаты вычислений', level=1)
        for key, value in data.items():
            doc.add_paragraph(f'{key}: {value}')
        doc.save(file_path)

    elif file_path.endswith('.xlsx'):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Результаты"
        for i, (key, value) in enumerate(data.items(), start=1):
            ws.cell(row=i, column=1, value=key)
            ws.cell(row=i, column=2, value=value)
        wb.save(file_path)

    messagebox.showinfo("Успех", "Результаты успешно сохранены!")


def calculate():
    shape = shape_var.get()
    try:
        if shape == "Прямоугольник":
            a = float(entry_a.get())
            b = float(entry_b.get())
            results = {
                "Площадь": Geometry.rectangle_area(a, b),
                "Радиус вписанной окружности": Geometry.rectangle_inscribed_radius(a, b),
                "Радиус описанной окружности": Geometry.rectangle_circumscribed_radius(a, b),
            }

        elif shape == "Треугольник":
            a = float(entry_a.get())
            b = float(entry_b.get())
            c = float(entry_c.get())
            results = {
                "Площадь": Geometry.triangle_area(a, b, c),
                "Радиус вписанной окружности": Geometry.triangle_inscribed_radius(a, b, c),
                "Радиус описанной окружности": Geometry.triangle_circumscribed_radius(a, b, c),
            }

        elif shape == "Трапеция":
            a = float(entry_a.get())
            b = float(entry_b.get())
            h = float(entry_h.get())
            results = {
                "Площадь": Geometry.trapezoid_area(a, b, h),
                "Радиус вписанной окружности": Geometry.trapezoid_inscribed_radius(a, b, h),
                "Радиус описанной окружности": Geometry.trapezoid_circumscribed_radius(a, b, h),
            }
        else:
            raise ValueError("Неверная фигура выбрана")

        results_text.set("\n".join([f"{k}: {v:.2f}" for k, v in results.items() if v is not None]))
        save_button.config(state=tk.NORMAL)

    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")


# GUI Setup
root = tk.Tk()
root.title("Калькулятор геометрии")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Shape selection
shape_var = tk.StringVar()
shape_label = ttk.Label(frame, text="Выберите фигуру:")
shape_label.grid(row=0, column=0, sticky=tk.W)
shape_menu = ttk.Combobox(frame, textvariable=shape_var, values=["Прямоугольник", "Треугольник", "Трапеция"], state="readonly")
shape_menu.grid(row=0, column=1, sticky=tk.W)
shape_menu.current(0)

# Input fields
entry_a = ttk.Entry(frame)
entry_b = ttk.Entry(frame)
entry_c = ttk.Entry(frame)
entry_h = ttk.Entry(frame)

def update_fields(event):
    for widget in [entry_a, entry_b, entry_c, entry_h]:
        widget.grid_remove()

    shape = shape_var.get()
    ttk.Label(frame, text="a:").grid(row=1, column=0, sticky=tk.W)
    entry_a.grid(row=1, column=1, sticky=tk.W)

    ttk.Label(frame, text="b:").grid(row=2, column=0, sticky=tk.W)
    entry_b.grid(row=2, column=1, sticky=tk.W)

    if shape == "Треугольник":
        ttk.Label(frame, text="c:").grid(row=3, column=0, sticky=tk.W)
        entry_c.grid(row=3, column=1, sticky=tk.W)

    if shape == "Трапеция":
        ttk.Label(frame, text="h:").grid(row=3, column=0, sticky=tk.W)
        entry_h.grid(row=3, column=1, sticky=tk.W)

shape_menu.bind("<<ComboboxSelected>>", update_fields)
update_fields(None)

# Results display
results_text = tk.StringVar()
results_label = ttk.Label(frame, textvariable=results_text, background="white", anchor=tk.W, relief=tk.SUNKEN, padding=5)
results_label.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E))

# Buttons
calculate_button = ttk.Button(frame, text="Рассчитать", command=calculate)
calculate_button.grid(row=5, column=0, sticky=tk.W)

save_button = ttk.Button(frame, text="Сохранить результаты", command=lambda: save_results(results_text.get().split("\n")), state=tk.DISABLED)
save_button.grid(row=5, column=1, sticky=tk.W)

root.mainloop()