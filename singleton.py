class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print(">> [Creando] Inicializando nueva conexión a la base de datos...")
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
        else:
            print(">> [Reutilizando] Conexión existente recuperada.")
        return cls._instance


if __name__ == "__main__":
    print("--- Intentando crear la primera conexión (db1) ---")
    db1 = DatabaseConnection()

    print("\n--- Intentando crear la segunda conexión (db2) ---")
    db2 = DatabaseConnection()

    print("\n--- Verificación ---")
    print(f"¿db1 y db2 son la misma instancia?: {db1 is db2}")