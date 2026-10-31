# Minimax y Poda Alfa-Beta

Laboratorio de Sistemas Inteligentes – Universidad César Vallejo (Ingeniería de Sistemas, tercera unidad).

## 1. Descripción del proyecto

Proyecto desarrollado en Python que implementa los algoritmos **Minimax** y **Poda Alfa-Beta** para la toma de decisiones en árboles de juego.

El objetivo es comparar ambos algoritmos considerando los valores obtenidos, los nodos evaluados y las ramas podadas.

## 2. Requisitos

- Python 3.12
- Git
- Visual Studio Code

## 3. Instalación

```bash
git clone https://github.com/moisescg18/alpha-beta-lab.git
cd alpha-beta-lab
python -m venv .venv
```

Activar el entorno virtual:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# Git Bash, Linux o Mac
source .venv/Scripts/activate   # Git Bash en Windows
source .venv/bin/activate       # Linux / Mac
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

## 4. Estructura del proyecto

```text
alpha-beta-lab/
├── src/
│   ├── __init__.py
│   ├── game_tree.py      # Árboles de ejemplo (listas anidadas)
│   ├── minimax.py        # Algoritmo Minimax
│   ├── alpha_beta.py     # Poda Alfa-Beta
│   └── main.py           # Comparación de ambos algoritmos
├── tests/
│   ├── __init__.py
│   └── test_algorithms.py
├── .github/workflows/ci.yml
├── .gitignore
├── requirements.txt
├── sonar-project.properties
└── README.md
```

## 5. Ejecución

```bash
python -m src.main
```

Salida esperada (resumen):

| Árbol | Valor Minimax | Nodos Minimax | Valor Alfa-Beta | Nodos Alfa-Beta | Ramas podadas |
|---|---|---|---|---|---|
| Sample Tree | 3 | 4 | 3 | 3 | 1 |
| Medium Tree | 7 | 12 | 7 | 8 | 3 |
| Ordered Tree | 8 | 12 | 8 | 8 | 2 |

En los tres casos ambos algoritmos devuelven **el mismo valor**, pero Alfa-Beta evalúa menos nodos.

## 6. Pruebas

Ejecutar pruebas unitarias:

```bash
pytest
```

Ejecutar pruebas con cobertura:

```bash
pytest --cov=src --cov-report=term-missing --cov-report=xml
```

## 7. Integración continua

El workflow `.github/workflows/ci.yml` ejecuta automáticamente las pruebas con cobertura en cada `push` o `pull request` hacia las ramas `main` y `develop`, usando GitHub Actions con Python 3.12.

## 8. Preguntas de análisis

**1. ¿Por qué Alfa-Beta obtiene el mismo resultado que Minimax si no evalúa todo el árbol?**
Porque solo descarta ramas que, matemáticamente, no pueden influir en la decisión final. Si un nodo MIN ya encontró un valor menor o igual al mejor que MAX tiene asegurado (alfa), MAX nunca elegirá ese camino sin importar los valores restantes. Por ejemplo, en el árbol `[[3, 5], [2, 9]]`, al ver el 2 en la segunda rama, MAX ya sabe que esa rama vale como máximo 2 y que tiene un 3 asegurado, por lo que el 9 no se evalúa. El resultado (3) es el mismo que el de Minimax.

**2. ¿Qué representa alpha dentro del algoritmo?**
Es el mejor valor (el más alto) que el jugador MAX ya tiene garantizado en el camino explorado hasta ese momento. Funciona como una cota inferior: MAX no aceptará nada peor que alpha. Inicia en −∞.

**3. ¿Qué representa beta dentro del algoritmo?**
Es el mejor valor (el más bajo) que el jugador MIN ya tiene garantizado en el camino explorado. Funciona como una cota superior: MIN no permitirá que MAX obtenga más que beta. Inicia en +∞. Cuando `beta <= alpha`, se poda el resto de las ramas de ese nodo.

**4. ¿En qué casos la Poda Alfa-Beta ahorra más trabajo?**
Cuando los árboles son profundos y anchos, y cuando los mejores movimientos se exploran primero. En el mejor caso, Alfa-Beta evalúa aproximadamente O(b^(d/2)) nodos en lugar de O(b^d), lo que permite buscar casi el doble de profundidad con el mismo costo. En los árboles pequeños del laboratorio el ahorro fue de 12 a 8 nodos (33 %) en el árbol mediano y de 4 a 3 en el árbol simple.

**5. ¿Por qué el orden de exploración afecta el rendimiento?**
Porque las podas dependen de qué tan pronto se encuentren valores buenos para alfa y beta. Si los mejores movimientos se evalúan primero, los límites se estrechan rápido y se podan muchas ramas. Si el árbol está mal ordenado (los mejores movimientos al final), alfa y beta casi no se actualizan a tiempo y Alfa-Beta puede evaluar tantos nodos como Minimax, aunque nunca más.

**6. ¿Qué pasaría si el rival no juega de manera racional?**
Minimax y Alfa-Beta asumen un oponente óptimo, por lo que el valor calculado es el mejor resultado *garantizado* en el peor caso. Si el rival juega mal, el agente igualmente obtendrá ese valor o uno mejor, pero puede desaprovechar oportunidades que una estrategia adaptada al rival sí explotaría. Para esos casos existen alternativas como Expectimax o el modelado del oponente.

**7. ¿Cómo se relaciona este algoritmo con los motores de ajedrez?**
Los motores de ajedrez clásicos (como Stockfish) se basan en Minimax con poda Alfa-Beta: exploran el árbol de jugadas hasta cierta profundidad, evalúan las posiciones con una función heurística y usan ordenamiento de movimientos y otras mejoras para podar más ramas. Este laboratorio es una versión simplificada de ese mecanismo, con hojas numéricas en lugar de una función de evaluación de tablero.

**8. ¿Qué limitaciones tiene este enfoque frente a redes neuronales o aprendizaje por refuerzo?**
- Requiere un modelo completo de las reglas del juego y un árbol explícito.
- Su costo crece de forma exponencial con la profundidad y el factor de ramificación, por lo que en juegos como Go es inviable.
- Depende de una función de evaluación diseñada a mano.
- Está pensado para juegos de dos jugadores, por turnos y de información perfecta.

Las redes neuronales y el aprendizaje por refuerzo pueden aprender la función de evaluación a partir de datos o autojuego (por ejemplo, AlphaZero), y manejan mejor espacios de estados muy grandes, aunque requieren más datos y cómputo de entrenamiento y son menos interpretables.

## 9. Tecnologías utilizadas

- Python 3.12
- Git y GitHub
- pytest y pytest-cov
- GitHub Actions
- SonarCloud (opcional)
- Visual Studio Code