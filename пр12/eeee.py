import tkinter as tk
from tkinter import messagebox
import requests
import json


def fetch_repos_by_username():
    username = entry.get()

    if not username:
        messagebox.showerror("Ошибка", "Введите никнейм пользователя.")
        return

    # Получаем список репозиториев пользователя
    repos_url = f"https://api.github.com/users/{username}/repos"
    repos_response = requests.get(repos_url)

    if repos_response.status_code == 200:
        repos_data = repos_response.json()

        if not repos_data:
            messagebox.showerror("Ошибка", "У пользователя нет репозиториев.")
            return

        # Берем первый репозиторий из списка
        repo = repos_data[0]
        repo_info = {
            'company': repo.get('owner', {}).get('company', None),
            'created_at': repo.get('created_at'),
            'email': repo.get('owner', {}).get('email', None),
            'id': repo.get('id'),
            'name': repo.get('name'),
            'url': repo.get('owner', {}).get('url')
        }

        # Запись в JSON файл
        with open('repo_info.json', 'w') as outfile:
            json.dump(repo_info, outfile, indent=4)

        messagebox.showinfo("Успех", "Информация о первом репозитории сохранена в repo_info.json.")
    else:
        messagebox.showerror("Ошибка", "Не удалось получить информацию о пользователе. Проверьте никнейм.")


# Создание GUI
root = tk.Tk()
root.title("GitHub User Repo Info Fetcher")

label = tk.Label(root, text="Введите никнейм пользователя GitHub:")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

button = tk.Button(root, text="Получить информацию", command=fetch_repos_by_username)
button.pack(pady=20)

root.mainloop()
