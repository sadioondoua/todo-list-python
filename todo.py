import json

FILENAME = "tasks.json"


def load_tasks():
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


tasks = load_tasks()


def save_tasks():
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)


def add_task():
    title = input("Nom de la tâche : ")
    priority = input("Priorité (haute / moyenne / basse) : ")
    deadline = input("Date d'échéance (AAAA-MM-JJ ou vide) : ")

    task = {
    "title": title,
    "done": False,
    "priority": priority,
    "deadline": deadline
}

    tasks.append(task)
    save_tasks()
    print("Tâche ajoutée !")


def list_tasks():
    if len(tasks) == 0:
        print("Aucune tâche.")
        return

    priority_order = {
        "haute": 0,
        "moyenne": 1,
        "basse": 2
    }

    sorted_tasks = sorted(tasks, key=lambda task: priority_order.get(task["priority"], 99))

    for i, task in enumerate(sorted_tasks):
        status = "✅" if task["done"] else "❌"
        print("tache non termine")
        print(f"{i}- {status} {task['title']} [Priorité : {task['priority']}] [Deadline : {task.get('deadline', 'aucune')}]")

def complete_task():
    list_tasks()

    index = int(input("Numéro de la tâche terminée : "))

    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks()
        print("Tâche terminée !")


def delete_task():
    list_tasks()

    index = int(input("Numéro à supprimer : "))

    if 0 <= index < len(tasks):

        confirm = input("Es-tu sûr de vouloir supprimer ? (o/n) : ").lower()

        if confirm == "o":
            tasks.pop(index)
            save_tasks()
            print("Tâche supprimée !")
        else:
            print("Suppression annulée.")


def menu():
    while True:
        print("\n--- TO DO LIST ---")
        print("     TO DO LIST")
        print("====================")
        print("1. Ajouter")
        print("2. Lister")
        print("3. Terminer")
        print("4. Supprimer")
        print("5. Quitter")

        choice = input("Choisis : ")

        if choice == "1":
            add_task()

        elif choice == "2":
            list_tasks()

        elif choice == "3":
            complete_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            print("Au revoir !")
            break

       
    

        