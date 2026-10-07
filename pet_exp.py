exp = []
def add_exp():
    category = input("Категория(еда,транспорт,развлечения): ").strip()
    try:
        am = float(input("Сумма: "))
    except ValueError:
        print("Число введи придурок")
        return
    exp.append({"category": category, "amount": am})
    print(f"Добавлено: {category}-{am}")

def sh_all():
    if not exp:
        print("Нихуя нет")
        return
    for i, e in enumerate(exp, 1):
        print(f"{i}. {e['category']}: {e['amount']}")

def show_total():
    total = sum(e["amount"] for e in exp)
    print(f"wasted: {total} rub")

def show_by_category():
    if not exp:
        print("Нихуя нет")
        return
    cat = input("Введите категорию для фильтрации: ").strip()
    filtered = [e for e in exp if e["category"] == cat]
    if not filtered:
        print("В этой категории пусто")
        return
    for i, e in enumerate(filtered, 1):
        print(f"{i}. {e['category']}: {e['amount']}")

def main():
    menu = """
    1. + wast
    2. show all
    3. view sum
    4. category
    0. exit
    """
    while True:
        print(menu)
        ch = input("Choice: ").strip()
        if ch == "1":
            add_exp()
        elif ch == "2":
            sh_all()
        elif ch == "3":
            show_total()
        elif ch == "4":
            show_by_category()
        elif ch == "0":
            print("Go naxyi")
            break
        else:
            print("naxyi")

if __name__ == "__main__":
    main()
