import ipywidgets as widgets
from IPython.display import display, clear_output
from charts import Chart
import numpy as np
import matplotlib.pyplot as plt

class GraphUI:
    def __init__(self):
        self.chart = Chart()
        self.create_widgets()

    def create_widgets(self):
        """Crea los componentes de la interfaz."""
        self.function_input = widgets.Text(
            value='np.sin(x)',
            description='Función:',
            style={'description_width': 'initial'}
        )

        self.x_min = widgets.FloatText(
            value=0.0,
            description='X min:',
            style={'description_width': 'initial'}
        )

        self.x_max = widgets.FloatText(
            value=10.0,
            description='X max:',
            style={'description_width': 'initial'}
        )

        self.title_input = widgets.Text(
            value='Título del Gráfico',
            description='Título:',
            style={'description_width': 'initial'}
        )

        self.xlabel_input = widgets.Text(
            value='Eje X',
            description='Etiqueta X:',
            style={'description_width': 'initial'}
        )

        self.ylabel_input = widgets.Text(
            value='Eje Y',
            description='Etiqueta Y:',
            style={'description_width': 'initial'}
        )

        self.update_button = widgets.Button(
            description='Actualizar Gráfico',
            button_style='success',
            tooltip='Generar gráfico'
        )

        self.export_button = widgets.Button(
            description='Exportar a PDF',
            button_style='info',
            tooltip='Guardar gráfico como PDF'
        )

        self.output = widgets.Output()

        # Asignar eventos
        self.update_button.on_click(self.update_chart)
        self.export_button.on_click(self.export_chart)

    def display(self):
        """Muestra la interfaz al usuario."""
        input_widgets = widgets.VBox([
            self.function_input,
            widgets.HBox([self.x_min, self.x_max]),
            self.title_input,
            self.xlabel_input,
            self.ylabel_input,
            widgets.HBox([self.update_button, self.export_button])
        ])

        ui = widgets.HBox([input_widgets, self.output])
        display(ui)

    def run(self):
        """Ejecuta la aplicación."""
        self.display()

    def update_chart(self, _):
        """Actualiza el gráfico según los parámetros ingresados."""
        with self.output:
            clear_output(wait=True)
            x_min = self.x_min.value
            x_max = self.x_max.value
            x = np.linspace(x_min, x_max, 400)
            try:
                y = eval(self.function_input.value)
                self.chart.ax.clear()
                self.chart.plot(x, y)
                self.chart.set_title(self.title_input.value)
                self.chart.set_xlabel(self.xlabel_input.value)
                self.chart.set_ylabel(self.ylabel_input.value)
                self.chart.add_legend()
                plt.show()
            except Exception as e:
                print(f"Error al generar el gráfico: {e}")

    def export_chart(self, _):
        """Exporta el gráfico actual a un archivo PDF."""
        filename = 'grafico.pdf'
        self.chart.save(filename)
        print(f"Gráfico exportado como {filename}")