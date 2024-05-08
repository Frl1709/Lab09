import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.grafo = None

    def handleAnalizza(self, e):
        distance = int(self._view._txtIn.value)
        self.grafo = None
        self.grafo = self._model.buildGraph(distance)

        self._view._txt_result.clean()
        self._view._txt_result.controls.append(
            ft.Text(
                f"Numero di nodi del grafo: {len(self.grafo._node)} \nNumero di archi del grafo: {len(self.grafo.edges)}"))
        self._view.update_page()

        for edge in self.grafo.edges:
            self._view._txt_result.controls.append(
                ft.Text(f"({edge[0]}, {edge[1]}), peso: {self.grafo[edge[0]][edge[1]]['weight']:.2f}"))
            self._view.update_page()
