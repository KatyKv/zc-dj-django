# Приложение dj04_movies

Практика работы с моделями и формами в Django.

## Назначение

- Создание модели `Movies` (название фильма, отзыв, автор)
- Реализация формы добавления фильмов (`MovieForm`)
- Вывод данных из БД на страницу
- Навигация между фильмами: предыдущий / следующий
- Интеграция с общей структурой проекта (layout, меню, стиль)

## Функционал

Реализованы страницы:
- `/movies/` — главная страница с карточками фильмов
- `/movies/<int:pk>/` — детальная страница отзыва
- `/movies/add_movie/` — форма добавления нового фильма

Все данные выводятся через шаблоны и стили проекта

## Структура

```
dj04_movies/
├── migrations/                  ← Миграции БД (автоматически сгенерированные)
├── templates/                   ← HTML-шаблоны приложения
│   └── dj04_movies/
│       ├── base.html            ← Базовый шаблон с наследованием
│       ├── index.html           ← Главная страница с фильмами
│       ├── movie_detail.html    ← Детальная страница фильма
│       └── add_movie.html       ← Форма добавления отзыва о фильме
├── forms.py                     ← Форма MovieForm на основе модели
├── views.py                     ← Обработчики запросов (index, movie_detail, add_movie)
├── urls.py                      ← Настройка маршрутов (index, movie_detail, add_movie)
├── models.py                    ← Модель Movies (название, описание, отзыв, автор)
├── admin.py                     ← Регистрация модели в админке
├── apps.py
├── __init__.py
└── tests.py                     ← Для будущих тестов
```

## Особенности реализации

- Модель `Movies` создаётся отдельно и не зависит от `NewsPost`
- Навигация между фильмами организована через список объектов в памяти
- Используются общие шаблоны проекта (`layout.html`, `base.html`)
- Ошибки формы показываются пользователю

## Статус
✅ Завершено (базовая функциональность реализована, можно расширить редактированием)
