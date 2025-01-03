import tkinter as tk
import random

def create_dark_ui():
    """
    Crea una interfaz gráfica simple con un fondo oscuro y una línea oscilante
    para visualizar el estado de actividad de Yarvis.
    """
    # Configurar la ventana principal
    root = tk.Tk()
    root.title("Yarvis")
    root.geometry("600x400")
    root.configure(bg="black")

    # Etiqueta para el texto de estado
    status_label = tk.Label(
        root, text="Escuchando...", font=("Arial", 18), fg="white", bg="black"
    )
    status_label.pack(pady=20)

    # Lienzo para la línea oscilante
    canvas = tk.Canvas(root, width=600, height=100, bg="black", highlightthickness=0)
    canvas.pack()

    # Dibujar la línea inicial
    line = canvas.create_line(0, 50, 600, 50, fill="green", width=2)

    def animate_line():
        """Anima la línea para simular oscilaciones."""
        canvas.delete(line)
        points = [
            (x, 50 + random.randint(-20, 20)) for x in range(0, 601, 20)
        ]
        flat_points = [coord for point in points for coord in point]
        canvas.create_line(flat_points, fill="green", width=2)
        root.after(100, animate_line)

    # Iniciar la animación
    animate_line()

    # Ejecutar la ventana
    root.mainloop()

if __name__ == "__main__":
    create_dark_ui()
