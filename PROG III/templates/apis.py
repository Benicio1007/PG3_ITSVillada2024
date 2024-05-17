import requests
from prettytable import PrettyTable
from flask import Flask, render_template

app = Flask(__name__)
API_URL = "https://jsonplaceholder.typicode.com/posts"


def show_menu():
    print("Menú:")
    print("1: Crear publicación")
    print("2: Actualizar publicación")
    print("3: Búsqueda por ID")
    print("4: Búsqueda lógica")
    print("5: Mostrar tabla de publicaciones")
    print("6: Salir")


def create_post():
    title = input("Ingrese el título de la nueva publicación: ")
    body = input("Ingrese el contenido de la nueva publicación: ")
    user_id = input("Ingrese el ID del usuario para la nueva publicación: ")
    post_data = {
        'title': title,
        'body': body,
        'userId': int(user_id)
    }
    response = requests.post(API_URL, json=post_data)
    if response.status_code == 201:
        print("La publicación se creó exitosamente.")
    else:
        print("Hubo un error al crear la publicación.")


def update_post():
    post_id = input("Ingrese el ID de la publicación que desea actualizar: ")
    title = input("Ingrese el nuevo título para la publicación: ")
    body = input("Ingrese el nuevo contenido para la publicación: ")
    put_data = {
        'id': int(post_id),
        'title': title,
        'body': body,
    }
    response = requests.put(f"{API_URL}/{post_id}", json=put_data)
    if response.status_code == 200:
        print("La publicación se actualizó exitosamente.")
    else:
        print("Hubo un error al actualizar la publicación.")


def search_by_id():
    post_id = input("Ingrese el ID de la publicación que desea buscar: ")
    response = requests.get(f"{API_URL}/{post_id}")
    if response.status_code == 200:
        post_data = response.json()
        print("Publicación encontrada:")
        print("ID:", post_data['id'])
        print("Título:", post_data['title'])
        print("Contenido:", post_data['body'])
        print("UserID:", post_data['userId'])
    else:
        print("No se encontró ninguna publicación con ese ID.")


def search_logical():
    keyword = input("Ingrese la palabra clave para la búsqueda lógica: ")
    response = requests.get(API_URL)
    if response.status_code == 200:
        posts = response.json()
        filtered_posts = [post for post in posts if keyword.lower() in post['title'].lower() or keyword.lower() in post['body'].lower()]
        if filtered_posts:
            print(f"Publicaciones que contienen la palabra clave '{keyword}':")
            for post in filtered_posts:
                print("+------+----------+---------------------------------------------------------------------------------+")
                print("|   ID |   UserID | Title                                                                           |")
                print("+======+==========+=================================================================================+")
                print("|{:>6} |{:>10} | {:<77}|".format(post['id'], post['userId'], post['title']))
                print("+------+----------+---------------------------------------------------------------------------------+")
        else:
            print("No se encontraron publicaciones que contengan la palabra clave especificada.")
    else:
        print("Hubo un error al recuperar las publicaciones.")


def show_table():
    response = requests.get(API_URL)
    if response.status_code == 200:
        posts = response.json()
        table = PrettyTable(['ID', 'UserID', 'Title'])
        for post in posts:
            table.add_row([post['id'], post['userId'], post['title']])
        print("Tabla de publicaciones:")
        print(table)
    else:
        print("Hubo un error al recuperar las publicaciones.")


@app.route('/')
def index():
    response = requests.get(API_URL)
    if response.status_code == 200:
        posts = response.json()
        return render_template('index.html', posts=posts)
    else:
        return "Hubo un error al recuperar las publicaciones."


def main():
    while True:
        show_menu()
        option = input("Seleccione una opción \n >>> ")
        if option == '1':
            create_post()
        elif option == '2':
            update_post()
        elif option == '3':
            search_by_id()
        elif option == '4':
            search_logical()
        elif option == '5':
            show_table()
        elif option == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    app.run()
