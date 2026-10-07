exp = []
def add_exp():
    exp = input("Категория(еда,транспорт,развлечения)").strip
    try:
        am = float(input("Сумма: "))
    except ValueError:
        print("Число введи придурок")
        return
    exp.append({"category":exp,"amount":am})
    print(f"Добавлено: {exp}-{am}")
def sh_all():
    if not exp:
        print("Нихуя нет")
        return
    for i,e in enumerate(exp,1):
        print(f"{i}.{e["Category"]}: {e["rub"]}")
def show_total():
    total = sum(e["amount"] for e in exp)
    print(f"wasted:{total} rub")
def main():
    menu = """
    1. + wast
    2. show all
    3.view sum
    4. category
    0. exit
    """
    while True:
        print(menu)
        ch = input("Choice: ").strip()
        if ch == "1":
            add_exp()
        if ch == "2":
            sh_all()
        if ch == "3":
            show_total()
        elif ch =="0":
            print("Go naxyi")
            break
        else:
            print("naxyi")
if "__name__" == "__main__":
    main()