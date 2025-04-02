import flet as ft

from database import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_analisi_vendite(self, e):
        #self._model.
        self._view.update_page()

    def handle_top_vendite(self, e):

        self._view.update_page()

    def get_anno(self):
        for c in DAO.get_anno():
            self._view.ddCodins.options.append(ft.dropdown.Option(c))

    def get_brand(self):
        return DAO.get_brand()

    def get_retailer(self):
        return DAO.get_retailer()
