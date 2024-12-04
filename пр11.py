import tkinter as tk
from tkinter import ttk, messagebox, filedialog

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = combo_operation.get()
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2 if num2 != 0 else "Ошибка: деление на ноль"

        label_result.config(text=f"Результат: {result}")
    except ValueError:
        label_result.config(text="Ошибка: введите корректные числа")


# Функция для чекбоксов
def show_selection():
    selected_options = []
    if var1.get():
        selected_options.append("Первый вариант")
    if var2.get():
        selected_options.append("Второй вариант")
    if var3.get():
        selected_options.append("Третий вариант")

    if selected_options:
        messagebox.showinfo("Выбор", f"Вы выбрали: {', '.join(selected_options)}")
    else:
        messagebox.showinfo("Выбор", "Ничего не выбрано")


# Функция для загрузки текста из файла
def load_text():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            text_content = file.read()
            text_box.delete(1.0, tk.END)  # Очистка текстового поля
            text_box.insert(tk.END, text_content)  # Вставка текста


# Создаем основное окно
root = tk.Tk()
root.title("Косьяненко В.А")

# Создаем вкладки
tab_control = ttk.Notebook(root)

# Первая вкладка - Калькулятор
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Калькулятор')

label_num1 = tk.Label(tab1)
label_num1.pack(pady=5)

entry_num1 = tk.Entry(tab1)
entry_num1.pack(pady=5)

label_num2 = tk.Label(tab1)
label_num2.pack(pady=5)

entry_num2 = tk.Entry(tab1)
entry_num2.pack(pady=5)

combo_operation = ttk.Combobox(tab1, values=['+', '-', '*', '/'])
combo_operation.pack(pady=5)
combo_operation.current(0)  # Устанавливаем значение по умолчанию

button_calculate = tk.Button(tab1, text="Посчитать", command=calculate)
button_calculate.pack(pady=5)

label_result = tk.Label(tab1, text="Результат:")
label_result.pack(pady=5)

# Вторая вкладка - Чекбоксы
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Чекбоксы')

var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()

check1 = tk.Checkbutton(tab2, text="Первый", variable=var1)
check1.pack(pady=5)

check2 = tk.Checkbutton(tab2, text="Второй", variable=var2)
check2.pack(pady=5)

check3 = tk.Checkbutton(tab2, text="Третий", variable=var3)
check3.pack(pady=5)

button_show_selection = tk.Button(tab2, text="Показать выбор", command=show_selection)
button_show_selection.pack(pady=5)
# Третья вкладка - Работа с текстом
tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text='Работа с текстом')
button_load_text = tk.Button(tab3, text="Загрузить текст из файла", command=load_text)
button_load_text.pack(pady=5)
text_box = tk.Text(tab3, wrap='word', width=90, height=10)
text_box.pack(pady=5)
# Упаковка и отображение вкладок
tab_control.pack(expand=1, fill='both')
# Запуск главного цикла приложения
root.mainloop()
