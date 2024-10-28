import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True  # Habilitar soporte para LaTeX

class Chart:
    def __init__(self):
        self.figure, self.ax = plt.subplots()
        self.elements = []

    def plot(self, x, y, label=None, **kwargs):
        """Agrega una línea al gráfico."""
        line, = self.ax.plot(x, y, label=label, **kwargs)
        self.elements.append(line)
        self.update()

    def set_title(self, title):
        """Establece el título del gráfico."""
        self.ax.set_title(title)
        self.update()

    def set_xlabel(self, xlabel):
        """Establece la etiqueta del eje X."""
        self.ax.set_xlabel(xlabel)
        self.update()

    def set_ylabel(self, ylabel):
        """Establece la etiqueta del eje Y."""
        self.ax.set_ylabel(ylabel)
        self.update()

    def add_legend(self):
        """Agrega una leyenda al gráfico."""
        self.ax.legend()
        self.update()

    def add_annotation(self, x, y, text):
        """Agrega una anotación al gráfico."""
        self.ax.annotate(text, (x, y))
        self.update()

    def update(self):
        """Actualiza el gráfico."""
        self.figure.canvas.draw()

    def save(self, filename):
        """Guarda el gráfico en un archivo."""
        with PdfPages(filename) as pdf:
            pdf.savefig(self.figure)