import matplotlib.pyplot as plt
import networkx as nx

# Crear un grafo para representar la arquitectura
G = nx.DiGraph()

# Agregar nodos
nodes = {
    "main.py": "Orquesta todo el flujo del asistente",
    "settings.py": "Configuración básica (API, idioma, palabra clave)",
    "voice_input.py": "Captura de voz y detección de activación",
    "voice_output.py": "Convierte texto en voz y lo reproduce",
    "llm_integration.py": "Comunicación con ChatGPT",
    "dark_ui.py": "Pantalla oscura con línea oscilante (visualización)",
    "database.py": "Opcional: almacena consultas y respuestas",
}

# Relaciones (edges)
edges = [
    ("main.py", "voice_input.py"),
    ("voice_input.py", "llm_integration.py"),
    ("llm_integration.py", "voice_output.py"),
    ("voice_output.py", "dark_ui.py"),
    ("main.py", "settings.py"),
    ("main.py", "database.py"),
]

# Añadir nodos y aristas al grafo
for node, desc in nodes.items():
    G.add_node(node, description=desc)

G.add_edges_from(edges)

# Dibujar el grafo
plt.figure(figsize=(14, 8))
pos = nx.spring_layout(G, seed=42)  # Posiciones de los nodos
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="skyblue",
    node_size=3000,
    font_size=10,
    font_weight="bold",
    arrowsize=20,
)

# Agregar descripciones de nodos como etiquetas
node_labels = {node: f"{node}\n{desc}" for node, desc in nodes.items()}
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=8, font_color="black")

plt.title("Arquitectura del Proyecto Yarvis", fontsize=16)
plt.show()
