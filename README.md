# Проект "Турагентство"
### Склад команди:
- Ілля Шрамко [github.com/IllyaShramko](https://github.com/IllyaShramko)
- Єгор Галкін [github.com/EgorGalkinORG](https://github.com/EgorGalkinORG)
- Давид Петренко [github.com/Davidptn](https://github.com/Davidptn)
____
# Основна Інформація про проект:
Це простий сайт де ви можете зареєструватися та вибрати тур який вам сподобався, але поки це весь функціонал 
____
# Як правильно запустити проект:
1. Потрібно склонувати його до порожньої папки та написати команду для клонування:
```
git clone https://github.com/IllyaShramko/Meet_30_09.git
```
2. Перейти до цієї папки, яку ви склонували:
```
cd Meet_30_09
```
3. Створити віртуальне оточення:
В консолі Windows:
```
python -m venv venv
```
В терміналі MacOS/Linux:
```
python3 -m venv venv
```
4. Активувати віртуальне середовище:
В консолі Windows:
```
venv\Scripts\activate
```
В терміналі MacOS/Linux:
```
source venv/bin/activate
```
5. Якщо ви зробили усе правильно, то у вас повинно було з'явитися у терміналі (venv)
6. Встановити бібліотеки, які потрібні для роботи проекту:
```
pip install -r requirements.txt
```
7. Ініціалізувати базу-данних та зробити міграції
```
cd main
```

```
flask --app settings db init
```

```
flask --app settings db migrate
```

```
flask --app settings db upgrade
```
8. Якщо ви зробили все вірно, у вас повинна була бути створенна база данних instance/data.db. Тепер ви можете додати туди свої тури
# Структура проекту:
### Подивитись на структуру проекту можна на [FigJam](https://www.figma.com/board/YGLuz0PFqOzCFbCM6pwTz1/Untitled?node-id=0-1&t=ffaTwtJUVOH7nwFe-1)
____
# Висновок:
За допомогою цього проекту ми з командою згадали те, що призабули за час канікул.
Окрема подяка Єгорові та Давиду.