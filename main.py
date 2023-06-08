import os

def generate_card_template(name):
    template_path = "template.txt"
    with open(template_path, "r") as template_file:
        template = template_file.read()
        return template.replace("NAME", name)

def create_card_file(name):
    card_content = generate_card_template(name)
    file_name = f"christmasCards/{name}.txt"
    with open(file_name, "w") as card_file:
        card_file.write(card_content)

def generate_cards_from_employees_file(file_path):
    with open(file_path, "r") as employees_file:
        for line in employees_file:
            name = line.strip()
            create_card_file(name)

def create_christmas_cards():
    if not os.path.exists("christmasCards"):
        os.makedirs("christmasCards")

    employees_file_path = "employees.txt"
    generate_cards_from_employees_file(employees_file_path)


create_christmas_cards()
