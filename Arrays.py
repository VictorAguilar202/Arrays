Strongman = ["CBum", "Belcast", "Andoni", "Ronnie", "Arnold"]

Suplements = [
    ["Creatine", "Protein", "Pre-Workout"],
    ["Beta Alanine", "Citruline", "MultiVitaminic"],
    ["Amino acids", "Omega-3", "Burner"]
]


def mostrar_strongman():
    return Strongman


def agregar_strongman(nombre):
    Strongman.append(nombre)
    return Strongman


def eliminar_strongman(nombre):
    if nombre in Strongman:
        Strongman.remove(nombre)
    return Strongman


def mostrar_suplementos():
    return Suplements


def buscar_pre_workout():
    for fila in range(len(Suplements)):
        for columna in range(len(Suplements[fila])):
            if Suplements[fila][columna] == "Pre-Workout":
                return fila, columna
    return None


if __name__ == "__main__":
    print("Lista de Strongman:", mostrar_strongman())
    print("Suplementos:", mostrar_suplementos())
    print("Ubicación de Pre-Workout:", buscar_pre_workout())
