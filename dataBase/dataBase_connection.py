import psycopg2

def address_connection():
    address = []

    url = input("Digite o endereço do Banco de Dados: ")
    url = url.replace("postgres://", "")

    user_password, host_database = url.split("@")
    user, password = user_password.split(":")
    host, database = host_database.split("/")

    address.append(database)
    address.append(user)
    address.append(password)
    address.append(host)
    address.append(5432)

    return address


def test_connection(address):
    try:
        conn = psycopg2.connect(
            database=address[0],
            user=address[1],
            password=address[2],
            host=address[3],
            port=address[4]
        )
        print("\nConexão bem-sucedida!")
        conn.close()

        return True
    
    except Exception as e:
        print("\nOcorreu um erro ao conectar:", e)
        return False

