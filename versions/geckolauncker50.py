# -*- coding: utf-8 -*-
#geckolauncher.py
"""
THIS VERSION [v.5.0] IS REALLY STABLE!!!
"""
# Monkey Python Coding Circus by Alan.RG Systemas & Team Cangurera

"""
Porque el Geckoniano, en el fondo, no pelea contra la complejidad.

Camina por ella.

Va recorriendo el Vallesiano con la cangurera llena de preguntas,
una linterna en la mano y un mate en la otra, sabiendo que en algún
pliegue imposible de la topología siempre existe un sendero
de coherencia esperando ser descubierto. 🦎🧉✨🌙 
"""

import sys
import os
import json
import re
import subprocess
import shutil 

from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import Qt, QSize, QPoint, QTimer
from PyQt5.QtWidgets import (QApplication, QMainWindow, QListWidget, QListWidgetItem, QSizePolicy,
                             QMenu, QAction, QColorDialog, QFileDialog, QTabWidget, QInputDialog, QMessageBox)

from PyQt5.QtGui import QColor
from PyQt5 import QtGui

import qdarkstyle
from qdarkstyle import load_stylesheet, DarkPalette

geckoappversion = "v.5.0" # Geckonizado por LLamita Encendida y Depurado por NOva Pythoniza, HARCODEADO por Chaman Gecko


class GeckoList(QListWidget):
    def __init__(self, parent_launcher):
        super().__init__()
        self.launcher = parent_launcher

        print("\n🧬 GeckoList INIT")
        print("   id:", id(self))

        self.setAcceptDrops(True)
        self.setDragDropMode(QListWidget.InternalMove)

        self.setMinimumSize(1, 1)
        self.setUniformItemSizes(True)

        print("🔌 CONNECT DONE en GeckoList:", id(self))
    
    def contextMenuEvent(self, event):
        global_pos = event.globalPos()
        self.launcher.mostrar_menu_contextual(global_pos, self)
        event.accept()
    
    '''
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
            self.setStyleSheet(self.launcher.list_style_active)
        else:
            super().dragEnterEvent(event)

    def dragLeaveEvent(self, event):
        self.setStyleSheet(self.launcher.list_style_normal)
        super().dragLeaveEvent(event)

    def dropEvent(self, event):
        self.setStyleSheet(self.launcher.list_style_normal)

        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                ruta = url.toLocalFile()
                if os.path.isfile(ruta):
                    nombre = os.path.basename(ruta)
                    self.launcher.agregar_item_lista(self, nombre, ruta, usar_consola=False)

            self.launcher.guardar_lanzadores()
            event.acceptProposedAction()
        else:
            super().dropEvent(event)
    '''
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
            self.launcher.play_sfx('dialog-information.oga')  #🦎 HOVER
            # Solo cambiar borde, no todo el stylesheet
            self.setProperty("dragActive", True)
            self.style().unpolish(self)
            self.style().polish(self)
        else:
            super().dragEnterEvent(event)

    def dragLeaveEvent(self, event):
        self.setProperty("dragActive", False)
        self.style().unpolish(self)
        self.style().polish(self)
        super().dragLeaveEvent(event)

    def dropEvent(self, event):
        self.setProperty("dragActive", False)
        self.style().unpolish(self)
        self.style().polish(self)
        
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                ruta = url.toLocalFile()
                if os.path.isfile(ruta):
                    nombre = os.path.basename(ruta)
                    self.launcher.agregar_item_lista(self, nombre, ruta, usar_consola=False)
            self.launcher.guardar_lanzadores()
            self.launcher.play_sfx('device-added.oga')  #🦎 DROP
            event.acceptProposedAction()
        else:
            super().dropEvent(event)

class GeckoLauncher(QMainWindow):
    def __init__(self):
        super().__init__()
        self.offset = None
        self.setWindowTitle(f"🦎 Gecko Launcher Minimalista {geckoappversion}")
        self.resize(1137, 370)
        self.tamanio_geckotable = (QSize(237, 137))
        self.font_geckotable = 17  # ← TU VARIABLE GLOBAL DE LETRA

        # Icono de aplicación
        self.scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.IconPath = os.path.join(self.scriptDir, 'Icons')
        icon_file = os.path.join(self.IconPath, 'appicon.png')
        if os.path.exists(icon_file):
            self.setWindowIcon(QtGui.QIcon(icon_file))

        self.player = QMediaPlayer()

        # Sin Bordes (Estilo Flotante)
        #self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        
        self.config_file = os.path.expanduser("~/.config/gecko_lanzadoresv12.json")

        self.config = {
            "version": geckoappversion,
            "fondo_launcher": "#0a0a0a", # AGREGAR: fondo de toda la ventana
            "categorias": {
                "🦎 GeckoLauncher": {
                    "items": [], # AGREGAR: lista de scripts va acá ahora
                    "tema": { # AGREGAR: tema individual por tab
                        "color_texto": "#00ff88",
                        "color_fondo_lista": "#000000",
                        "color_fondo_item_activo": "#00ff88",
                        "color_texto_item_activo": "#000000"
                    }
                }
            }
        }

        self.cargar_lanzadores()
        
        self.setup_styles()
        self.init_ui()
        
        self.setStyleSheet(f"QMainWindow {{ background: {self.config.get('fondo_launcher', '#0a0a0a')}; }}")

    def setup_styles(self):
        """ Hojas de estilo unificadas de tu suite cyberpunk """
        base_style = """
            QListWidget::item:selected {
                background: #00ff88; /* Verde Geckonico */
                color:#000;
                border-left: 3px solid #ffffff;
                font-weight: bold;
            }
            QListWidget::item:hover {
                background: #00ff88; /* Verde Geckonico*/
                color: #000;
                border-left: 3px solid #00ff00;
            }
            QTabWidget::pane {
                border: 2px solid #00ff88;
                background: rgba(0, 0, 0, 0.85);
            }
            QTabBar::tab {
                background: #111;
                color: #00ff88;
                padding: 10px;
                border: 1px solid #333; 
            }
            QTabBar::tab:selected {
                background: #00ff88;
                color: #000;
                font-weight: bold;
            }
        """
        self.list_style_normal = f"QListWidget {{ background: #000; color: #00ff88; border: 2px solid #00ff88; font-family: 'Courier New', monospace; font-size: {self.font_geckotable}px; }} {base_style}"
        self.list_style_active = f"QListWidget {{ background: #000; color: #00ff88; border: 2px solid #ffffff; font-family: 'Courier New', monospace; font-size: {self.font_geckotable}px; }} {base_style}"

    def aplicar_estilo_lista(self, lista_widget, nombre_tab):
        tema_tab = self.config["categorias"][nombre_tab].get("tema", {})

        color_texto = tema_tab.get("color_texto", "#00ff88")
        color_fondo = tema_tab.get("color_fondo_lista", "#000000")
        color_fondo_activo = tema_tab.get("color_fondo_item_activo", "#00ff88")
        color_texto_activo = tema_tab.get("color_texto_item_activo", "#000000")

        estilo = f"""
            QListWidget {{
                background: {color_fondo};
                color: {color_texto};
                border: 2px solid #00ff88;
                font-family: 'Courier New', monospace;
                font-size: {self.font_geckotable}px;
            }}
            QListWidget::item:selected {{
                background: {color_fondo_activo};
                color: {color_texto_activo};
                border-left: 3px solid #ffffff;
                font-weight: bold;
            }}
            QListWidget::item:hover {{
                background: {color_fondo_activo};
                color: {color_texto_activo};
                border-left: 3px solid #00ff00;
            }}
        """
        estilo += """
            QListWidget[dragActive="true"] {
                border: 2px solid #ffffff;
            }
        """
        lista_widget.setStyleSheet(estilo)

    def init_ui(self):
        """ Inicializa el contenedor de GeckoTabs y tu primera lista """
        self.tabs = QTabWidget(self)
        self.tabs.setMovable(True)          
        self.tabs.setTabsClosable(True)     
        self.tabs.tabCloseRequested.connect(self.eliminar_categoria)
        self.tabs.currentChanged.connect(self.cambiar_lista_activa)
        
        self.tabs.tabBar().tabMoved.connect(self.reordenar_categorias_dict)

        #self.tabs.setTabPosition(QTabWidget.East)
        self.tabs.setTabPosition(QTabWidget.South)               
        self.tabs.clear() # Por si acaso

        for nombre_tab, data_tab in self.config["categorias"].items():
            lista_widget = self.crear_pestana(nombre_tab)
            for data in data_tab.get("items", []): 
                self.agregar_item_lista(lista_widget, data["nombre"], data["ruta"], data["consola"], sync_config=False)

        if self.tabs.count() > 0:
            self.lista = self.tabs.widget(0)
            self.tabs.setCurrentIndex(0)
        else:
            # Fallback si el json estaba vacío
            self.lista = self.crear_pestana("Inicio 🦎")
            self.config["categorias"]["Inicio 🦎"] = []

        self.setCentralWidget(self.tabs)

    def play_sfx(self, nombre_archivo):
        # Fuerza ruta absoluta siempre
        ruta_abs = os.path.abspath(os.path.join("/usr/share/sounds/freedesktop/stereo/", nombre_archivo))
        if os.path.isfile(ruta_abs):
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(ruta_abs)))
            self.player.play()
        else:
            print(f"🦎 SFX no encontrado: {ruta_abs}")

    def crear_pestana(self, nombre_categoria):
        """ Fábrica para clonar exactamente tu lista en nuevas pestañas """
        nueva_lista = GeckoList(self)
        nueva_lista.setUniformItemSizes(True)  # Fuerza a respetar tu sizeHint
        nueva_lista.setResizeMode(QListWidget.Fixed)  # No recalcules grid al redimensionar
        nueva_lista.setSizeAdjustPolicy(QListWidget.AdjustIgnored)  # Ignora el viewport
        nueva_lista.viewport().setMinimumSize(self.tamanio_geckotable.width() * 2, self.tamanio_geckotable.height() * 2)
        self.aplicar_estilo_lista(nueva_lista, nombre_categoria)
        
        print("\n🧪 CREANDO PESTAÑA:", nombre_categoria)
        print("   tipo clase lista:", type(nueva_lista))
        print("   id objeto:", id(nueva_lista))
        print("   tiene contextPolicy:", nueva_lista.contextMenuPolicy())
        print("   tiene signal conectado:", nueva_lista.receivers(nueva_lista.customContextMenuRequested))

        nueva_lista.setViewMode(QListWidget.IconMode)
        #nueva_lista.setResizeMode(QListWidget.Adjust)
        nueva_lista.setGridSize(self.tamanio_geckotable)
        nueva_lista.setSpacing(10)
        nueva_lista.setAcceptDrops(True)
        nueva_lista.setDragDropMode(QListWidget.InternalMove)
        nueva_lista.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        nueva_lista.setMinimumHeight(500)
        
        
        """
        Gecko no sobreingenieriza, detecta patrones y genera las condicines para que la 
        consciencia se haga codigo, y las condiciones iniciales sean propiscias.
        """
        # HUEVO DE PASCUA GECKONISTA: fuerza condiciones iniciales
        ruta_hmx = os.path.join(self.scriptDir, "hmx.py")
        if os.path.exists(ruta_hmx):
            huevo = QListWidgetItem("🐣\n\nhmx.py")
            huevo.setData(Qt.UserRole, {"nombre": "hmx.py", "ruta": ruta_hmx, "consola": False, "huevo": True})
            huevo.setSizeHint(self.tamanio_geckotable)  
            #huevo.setFlags(Qt.NoItemFlags)  # No clickeable
            nueva_lista.addItem(huevo)

        nueva_lista.itemDoubleClicked.connect(self.ejecutar_lanzador)
        nueva_lista.model().rowsMoved.connect(lambda: self.sincronizar_orden_lista(nueva_lista))


        self.tabs.addTab(nueva_lista, nombre_categoria)
        self.tabs.setCurrentWidget(nueva_lista)
        
        print("🦎 DEBUG PESTAÑA:", nombre_categoria, 
            "size:", nueva_lista.size(), 
            "viewport:", nueva_lista.viewport().size(),
            "count:", nueva_lista.count())

        nueva_lista.viewport().setContextMenuPolicy(Qt.CustomContextMenu)

        nueva_lista.viewport().customContextMenuRequested.connect(
            lambda pos, lw=nueva_lista: self._on_context_menu_viewport(
                lw.viewport().mapToGlobal(pos), lw
            )
        )

        return nueva_lista

    def cambiar_lista_activa(self, index):
        """ Redirecciona la variable global self.lista a la pestaña enfocada """
        widget_actual = self.tabs.widget(index)
        if widget_actual is None:
            return
        if isinstance(widget_actual, GeckoList): # Cambia QListWidget por GeckoList
            self.lista = widget_actual
        else:
            self.lista = None # evita crashes si no hay tabs

    def reordenar_categorias_dict(self, from_index, to_index):
        """ Mantiene self.config['categorias'] en el mismo orden que las tabs """
        items = list(self.config["categorias"].items())
        item = items.pop(from_index)
        items.insert(to_index, item)
        self.config["categorias"] = dict(items)
        self.guardar_lanzadores()

    def sincronizar_orden_lista(self, lista_widget):
        self.setUpdatesEnabled(False)  # Deshabilita repintado
        nombre_tab = self.tabs.tabText(self.tabs.indexOf(lista_widget))
        nueva_lista = []
        for i in range(lista_widget.count()):
            nueva_lista.append(lista_widget.item(i).data(Qt.UserRole))
        self.config["categorias"][nombre_tab]["items"] = nueva_lista
        self.guardar_lanzadores()
        self.aplicar_estilo_lista(lista_widget, nombre_tab)  # Reaplica colores
        self.setUpdatesEnabled(True)  # Rehabilita repintado
        
    # --- LÓGICA DE ITEMS / TARJETAS TÁCTILES ---
    def agregar_item_lista(self, lista_target, nombre, ruta, usar_consola=False, sync_config=True):
        icono_visual = "💻" if usar_consola else "⚙"
        texto_tarjeta = f"{icono_visual}\n\n{nombre}"
        
        item = QListWidgetItem(texto_tarjeta)
        item.setData(Qt.UserRole, {"nombre": nombre, "ruta": ruta, "consola": usar_consola})
        item.setTextAlignment(Qt.AlignCenter)
        item.setSizeHint(self.tamanio_geckotable)  # ← AGREGAR ESTA LÍNEA
        lista_target.addItem(item)

        # AGREGAR: solo sincronizar si no estamos cargando desde config
        if sync_config:
            nombre_tab = self.tabs.tabText(self.tabs.indexOf(lista_target))
            if nombre_tab in self.config["categorias"]:
                self.config["categorias"][nombre_tab]["items"].append({"nombre": nombre, "ruta": ruta, "consola": usar_consola})

    def ejecutar_lanzador(self, item):
        data = item.data(Qt.UserRole)
        ruta = data["ruta"]
        if not os.path.exists(ruta):
            QMessageBox.warning(self, "🦎 Error", f"No existe: {ruta}") 
            return
        try: 
            os.chmod(ruta, 0o755)
        except PermissionError: 
            pass # Si no podemos dar permisos, igual intentamos
        if data["consola"]:
            terminal = shutil.which("xfce4-terminal") or shutil.which("x-terminal-emulator") or "xterm"
            subprocess.Popen([terminal, "-e", f"bash -c '{ruta}; exec bash'"])
            self.play_sfx('complete.oga')  #🦎 CLICK
        elif data.get("huevo"):  # ← AGREGAR ESTAS 2 LÍNEAS
            subprocess.Popen([sys.executable, os.path.abspath(ruta)], 
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            subprocess.Popen([ruta], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # --- MENÚ CONTEXTUAL UNIFICADO ---
    def mostrar_menu_contextual(self, pos_global, lista_origen=None):
        print("🔥 ORIGEN:", id(lista_origen), "SELF.LISTA:", id(self.lista))
        
        print("\n🧠 MENU REQUEST")
        print("   lista_origen:", lista_origen)
        print("   self.lista actual:", self.lista)
        print("   match:", lista_origen is self.lista)
        print("   type(lista_origen):", type(lista_origen))
        

        print("🔥 TAB ACTUAL:", self.tabs.currentIndex())
        print("🔥 WIDGET CURRENT:", self.tabs.currentWidget())
        print("🔥 lista_origen:", lista_origen)

        lista_activa = lista_origen or self.lista
        if not lista_activa: return
        
        pos_local = lista_activa.viewport().mapFromGlobal(pos_global)
        item = lista_activa.itemAt(pos_local)
        
        # FIX DE RAÍZ: Sin padre (None) para que flote libre sobre cualquier widget
        menu = QMenu(None) 
        # Le aplicamos el estilo oscuro general para que no rompa la estética cyberpunk
        menu.setStyleSheet(qdarkstyle.load_stylesheet(DarkPalette))

        if item:
            data = item.data(Qt.UserRole)
            toggle_txt = "Desactivar Consola" if data["consola"] else "Activar Consola"
            act_consola = QAction(toggle_txt, self)
            act_consola.triggered.connect(lambda: self.toggle_consola(item))
            menu.addAction(act_consola)

            # submenú nuevo:
            menu_pintar = QMenu("🎨 Tunear TabletasGecko", self)

            act_txt = QAction("Color del texto", self)
            act_txt.triggered.connect(lambda: self.pintame(lista_activa, "texto"))
            menu_pintar.addAction(act_txt)

            act_bg = QAction("Color de fondo de lista", self)
            act_bg.triggered.connect(lambda: self.pintame(lista_activa, "fondo"))
            menu_pintar.addAction(act_bg)

            menu_pintar.addSeparator()

            act_sel = QAction("Color de fondo al seleccionar", self)
            act_sel.triggered.connect(lambda: self.pintame(lista_activa, "seleccion"))
            menu_pintar.addAction(act_sel)

            act_sel_txt = QAction("Color de texto al seleccionar", self)
            act_sel_txt.triggered.connect(lambda: self.pintame(lista_activa, "texto_seleccion"))
            menu_pintar.addAction(act_sel_txt)

            menu.addMenu(menu_pintar)
            
            menu.addSeparator()
            act_eliminar = QAction("❌ Eliminar Lanzador", self)
            act_eliminar.triggered.connect(lambda: self.eliminar_lanzador(item))
            menu.addAction(act_eliminar)
        else:
            act_nuevo = QAction("➕ Agregar archivo manualmente", self)
            act_nuevo.triggered.connect(self.agregar_manual)
            menu.addAction(act_nuevo)
            
            menu.addSeparator()
            act_nueva_tab = QAction("📁 Crear Nueva Categoría / Pestaña", self)
            act_nueva_tab.triggered.connect(self.agregar_categoria_dialog)
            menu.addAction(act_nueva_tab)
            
            if self.tabs.count() > 1:
                act_borrar_tab = QAction("🗑️ Eliminar esta Pestaña Actual", self)
                act_borrar_tab.triggered.connect(self.eliminar_pestana_actual)
                menu.addAction(act_borrar_tab)
        
        # === EJECUCIÓN PURA ===
        print(f"🦎 DEBUG MENU FINAL → pos={pos_global} | actions={len(menu.actions())}")
        
        if menu.actions():
            # exec_ bloquea el hilo de forma segura y dibuja la mini-ventana arriba de todo
            self.play_sfx('bell.oga')  #🦎 MENU
            menu.exec_(pos_global)
        else:
            print("⚠️ Menú sin acciones!")

    # --- ACCIONES DE GESTIÓN (SIN EÑES) ---
    def toggle_consola(self, item):
        data = item.data(Qt.UserRole)
        data["consola"] = not data["consola"]
        item.setData(Qt.UserRole, data)
        icono_visual = "💻" if data["consola"] else "⚙️"
        item.setText(f"{icono_visual}\n\n{data['nombre']}")
        # AGREGAR: actualizar en self.config
        nombre_tab = self.tabs.tabText(self.tabs.currentIndex())
        for script in self.config["categorias"][nombre_tab]["items"]:
            if script["ruta"] == data["ruta"]:
                script["consola"] = data["consola"]
                break
        self.guardar_lanzadores()

    def eliminar_lanzador(self, item):
        if not self.lista: return
        data = item.data(Qt.UserRole)
        nombre_tab = self.tabs.tabText(self.tabs.currentIndex())
        # Borrar del dict primero
        if nombre_tab in self.config["categorias"]:
            self.config["categorias"][nombre_tab]["items"] = [
                d for d in self.config["categorias"][nombre_tab]["items"] if d["ruta"]!= data["ruta"]
            ]
        self.lista.takeItem(self.lista.row(item))
        self.guardar_lanzadores()
    
    def agregar_manual(self):
        if not self.lista: return
        ruta, _ = QFileDialog.getOpenFileName(self, "Seleccionar Script", os.path.expanduser("~"))
        if ruta:
            nombre = os.path.basename(ruta)
            self.agregar_item_lista(self.lista, nombre, ruta, usar_consola=False)
            self.guardar_lanzadores()

    def agregar_categoria_dialog(self):
        nombre, ok = QInputDialog.getText(self, "🦎 Nueva Categoría", "Nombre de las GeckoTab:")
        if ok and nombre.strip():
            nombre = nombre.strip()
            self.config["categorias"][nombre] = {"items": [], "tema": {"color_texto": "#00ff88", "color_fondo_lista": "#000000", "color_fondo_item_activo": "#00ff88", "color_texto_item_activo": "#000000"}}
            self.crear_pestana(nombre)
            self.guardar_lanzadores()

    def eliminar_pestana_actual(self):
        index_actual = self.tabs.currentIndex()
        if index_actual == -1: 
            return
        lista_actual = self.tabs.widget(index_actual)
        if isinstance(lista_actual, QListWidget) and lista_actual.count() > 0:
            boton_clickeado = QMessageBox.question(
                self, "⚠️ Confirmación",
                "Esta pestaña tiene elementos dentro. ¿Deseas eliminarla por completo?",
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No
            )
            if boton_clickeado == QMessageBox.No: 
                return
        
        nombre_tab = self.tabs.tabText(index_actual)
        if nombre_tab in self.config["categorias"]:
            del self.config["categorias"][nombre_tab] # AGREGAR
        self.tabs.removeTab(index_actual)
        self.guardar_lanzadores()

    def eliminar_categoria(self, index):
        self.tabs.setCurrentIndex(index)
        self.eliminar_pestana_actual()

    def pintame(self, lista_widget, tipo_pintura):
        if not isinstance(lista_widget, GeckoList):
            return False

        nombre_tab = self.tabs.tabText(self.tabs.indexOf(lista_widget))
        tema_tab = self.config["categorias"][nombre_tab]["tema"]

        mapa_claves = {
            'texto': 'color_texto',
            'fondo': 'color_fondo_lista',
            'seleccion': 'color_fondo_item_activo',
            'texto_seleccion': 'color_texto_item_activo'
        }

        clave = mapa_claves[tipo_pintura]
        color_inicial = QColor(tema_tab.get(clave, "#00ff88"))

        titulo = {
            'texto': "Texto de esta TabletaGecko",
            'fondo': "Fondo de esta TabletaGecko",
            'seleccion': "Fondo al seleccionar en esta Tableta",
            'texto_seleccion': "Texto al seleccionar en esta Tableta"
        }

        color_nuevo = QColorDialog.getColor(color_inicial, self, f"🦎 {titulo[tipo_pintura]}")
        if not color_nuevo.isValid():
            return False

        # Validar contraste solo en esta tab
        tema_temp = tema_tab.copy()
        tema_temp[clave] = color_nuevo.name()

        if tema_temp['color_texto'] == tema_temp['color_fondo_lista']:
            QMessageBox.warning(self, "🦎 Ojo", "Texto y fondo no pueden ser iguales en esta tableta.")
            return False
        if tema_temp['color_texto_item_activo'] == tema_temp['color_fondo_item_activo']:
            QMessageBox.warning(self, "🦎 Ojo", "Texto y fondo de selección no pueden ser iguales en esta tableta.")
            return False

        # Guardar en el tema de esta tab específica
        self.config["categorias"][nombre_tab]["tema"][clave] = color_nuevo.name()

        # Aplicar solo a esta lista
        self.aplicar_estilo_lista(lista_widget, nombre_tab)
        self.guardar_lanzadores()
        return True

    # --- HACKS MOUSE DRAG REPARADOS (BY LEO) ---
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = event.globalPosition().toPoint() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.offset is not None: 
            self.move(event.globalPosition().toPoint() - self.offset)
    
    def closeEvent(self, event):
        self.guardar_lanzadores()
        event.accept()

    # --- PERSISTENCIA BLINDADA ---
    def guardar_lanzadores(self):
        """ Ahora es trivial: solo guarda el dict que ya tenemos en memoria """
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=4, ensure_ascii=False)

    def cargar_lanzadores(self):
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    config_cargada = json.load(f)

                # Migrar formato viejo a nuevo si hace falta
                if "categorias" in config_cargada:
                    for nombre_tab, data in config_cargada["categorias"].items():
                        # Si es lista, es formato viejo. Convertir a dict
                        if isinstance(data, list):
                            config_cargada["categorias"][nombre_tab] = {
                                "items": data,
                                "tema": {
                                    "color_texto": "#00ff88",
                                    "color_fondo_lista": "#000000",
                                    "color_fondo_item_activo": "#00ff88",
                                    "color_texto_item_activo": "#000000"
                                }
                            }

                #self.config.update(config_cargada)
                # Merge profundo para no perder defaults
                def merge_dicts(base, nuevo):
                    for k, v in nuevo.items():
                        if k in base and isinstance(base[k], dict) and isinstance(v, dict):
                            merge_dicts(base[k], v)
                        else:
                            base[k] = v
                merge_dicts(self.config, config_cargada)

            except Exception as e:
                print(f"Error cargando config: {e}. Usando defaults.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet(DarkPalette))
    launcher = GeckoLauncher()
    launcher.show()
    sys.exit(app.exec_())
