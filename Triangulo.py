import tkinter as tk

class TrianguloApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Triángulo en Tkinter")

        # Crear un canvas
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()

        # Coordenadas del triángulo (x1, y1, x2, y2, x3, y3)
        puntos = [100, 300, 200, 100, 300, 300]

        # Dibujar el triángulo con color plomo (gris)
        self.canvas.create_polygon(puntos, fill="gray", outline="black", width=2)

        # Agregar el texto dentro del triángulo
        self.canvas.create_text(200, 200, text="Hasta lurgo ingeniero\nse cuida\nAtte: el Lab3",
                                font=("Arial", 12, "bold"), fill="dimgray", justify="center")

if __name__ == "__main__":
    root = tk.Tk()
    app = TrianguloApp(root)
    root.mainloop()
