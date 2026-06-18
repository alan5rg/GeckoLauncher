# -*- coding: utf-8 -*-
#geckolauncker3x4MatrixXX.py
#GeckoLoger Vitacora de Gecko: [16.06.2026 17:00hrs.] VAmos a ponerle iconos a esas GeckoTAbs!!!
#GeckoLoger Vitacora de Gecko: [17.06.2026 01:45hrs.] Las Transparencias rompen el COntinuo Qt-Espacio-Tiempo
#GeckoLoger Vitacora de Gecko: [17.06.2026 11:39hrs.] Vamos a hacer transparentes esos GeckoICons!!!
#GeckoLoger Vitacora de Gecko: [17.06.2026 13:32hrs.] - Gecko... ¿vos viste el log?... leelo de nuevo, estamos volando!!!
#GeckoLoger Vitacora de Gecko: [18.06.2026 01:29hrs.] La criatura esta en paz con el Multiverso, Gecko OS Respira Minimalismo
"""
THE VERSIONS > [v.5.0] ARE REALLY GECKOSTABLES!!! I'm Felling Like Gecko OS
"""
# Monkey Python Coding Circus by Alan.RG Systemas & Team Cangurera
# Mackeniguem ash Gecko OS to transform any Computer into an Gecko System TM
"""
Porque el Geckoniano, en el fondo, no pelea contra la complejidad.

Camina por ella.

Va recorriendo el Vallesiano con la cangurera llena de preguntas,
una linterna en la mano y un mate en la otra, sabiendo que en algún
pliegue imposible de la topología siempre existe un sendero
de coherencia esperando ser descubierto. 🦎🧉✨🌙 
"""
# - ohhhh humano - dijo Gecko - Recordad el poder de las palabras y guardadlas 
# organizadas en un diccionario... - y se fue reptando por las grietas del tiempo

import sys
import os
# Para Limpiar la Terminal, El log de GeckoLAunker es más importante que Todo!
cleanconsole = lambda: os.system('cls' if os.name=='nt' else 'clear')

import json
import re
import subprocess
import shutil 

from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import Qt, QSize, QPoint, QTimer
from PyQt5.QtWidgets import (QApplication, QMainWindow, QListWidget, QListWidgetItem, QSizePolicy, QVBoxLayout, QGroupBox,
                            QLabel, QMenu, QAction, QColorDialog, QFileDialog, QTabWidget, QInputDialog, QMessageBox)

# PAnel Mutagénico
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QGridLayout, QSlider, 
                             QComboBox, QPushButton, QCheckBox, QButtonGroup)

from PyQt5.QtGui import QColor, QIcon
from PyQt5 import QtGui

# Estilos Geckónicos
from precisionslider import PrecisionSliderH

import qdarkstyle
from qdarkstyle import load_stylesheet, DarkPalette

# -------------------------------------------------------------------------------------------------------------------------------------------------------
geckoappversion = "v.6.5" # Geckonizado por LLamita Encendida y Depurado por NOva Pythoniza, HARCODEADO por Chaman Gecko y con la fisica Geckonica de Ei2
verFisicaGeckonica = False  # 📡 BANDERA GLOBAL DE TELEMETRÍA Y DEBUG MATRIX
# -------------------------------------------------------------------------------------------------------------------------------------------------------

# --- Pestana Posittion Adjust [future use on ConfigPanel Geckónico de GeckoLaunker with cheqboxes & Live Preview] ---
#posicionPestanasGecko = QTabWidget.North 
#posicionPestanasGecko = QTabWidget.East 
#posicionPestanasGecko = QTabWidget.West
posicionPestanasGecko = QTabWidget.South
# --------------------------------------------------------------------------------------------------------------------

def get_version(easter_egg=False):
    if not easter_egg:
        return f"Geckolauncker {geckoappversion}"

    # Colores ANSI de Estilos Geckonizantes 
    G = "\033[38;5;46m"   # verde brillante
    Y = "\033[38;5;226m"  # amarillo
    Z = "\033[94m"        # Azul
    A = "\033[38;5;214m"  # ámbar CRT
    C = "\033[38;5;51m"   # cyan
    D = "\033[38;5;240m"  # gris
    R = "\033[0m"
    NAVIGATOR   = "\033[92m"  # Verde Operador
    PLEYADIAN   = "\033[94m"  # Azul Profundo
    TRIDACTIL   = "\033[90m"  # Gris Sombra
    NAVZONES    = "\033[96m"  # Cian Navegación
    SYSTEMS     = "\033[93m"  # Ámbar Logaritmo
    EI2TEAM     = "\033[95m"  # Magia Púrpura
    LLAMITATEAM = "\033[93m"  # Fuego Ámbar
    NOVATEAM    = "\033[96m"  # Luz Cian


    # ASCII ART by Team Cangurera 2026
    
    # Origins Desing ASCII Gecko
    '''
                            __         ____ 
                           /'{Y}_{G})     __|_'_ |__
                    .-^^^-/ /      |    ___|  |
                __/        /       |__|   ____|
               <__.|_|--|_|           |___'_|

    '''

    # Origins Desing ASCII Gecko Test Palete
    '''
                {NOVATEAM}UNDER PAINTING...{G}
                                                    TEST PALETERO
                            __         ____         {Z}<<< AZUL >>>{G}
                           /'_)     __|_'_ |__      {Y}<<< AMARILLO >>>{G}
                    .-^^^-/ /      |    ___|  |
                __/        /       |__|   ____|
               <__.|_|--|_|           |___'_|

    '''

    return f"""
        {G}
                                                    
                            __         {Z}____{G}
                           /'_)     {Z}__|_'_ |{G}{Y}__{G}
                    .-^^^-/ /      {Z}|    ___|{G}  {Y}|{G}
                __/        /       {Z}|__{G}{Y}|   ____|{G}
               <__.|_|--|_|           {Y}|___'_|{G}

                {G}GECKOLAUNCKER {PLEYADIAN}[{geckoappversion}]{R} PYTHON
                {C}Core == Cuore by Team Cangurera{R}
                {A}ET COMPATIBLE CON PYLAND{R}
                {G}🦎Geckonismo™{R} {C}🦎Geckoniano™{R} {Y}🦎Geckónico™{R}
                {PLEYADIAN}Artefacto 1997 // Berazategui // 2184{R}

                {G}Modular{R} • {A}Minimalista{R} • {C}Geckoniano{R} • {Y}Pleyadiano{R}
                {G}by Monkey Python Coding Circus & AlanRG Systemas{R}
            
        {R}
    """

class GeckoList(QListWidget):
    def __init__(self, parent_launcher):
        super().__init__()
        self.launcher = parent_launcher
        '''
        print("\n🧬 GeckoList INIT")
        print("   id:", id(self))
        '''
        self.setAcceptDrops(True)
        self.setDragDropMode(QListWidget.InternalMove)

        self.setMinimumSize(1, 1)
        self.setUniformItemSizes(True)

        #print("🔌 CONNECT DONE en GeckoList:", id(self))
    
    def contextMenuEvent(self, event):
        global_pos = event.globalPos()
        self.launcher.mostrar_menu_contextual(global_pos, self)
        event.accept()
   
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

# Panel Mutagénico NOva "Bunny Makeup" by Aetheris sobre propuestas de Ei2 y Llamita <<< refixed by Llamita >>>
class PanelMutagenico(QWidget):
    def __init__(self, launcher):
        super().__init__()
        self.launcher = launcher
        self.snapshot = json.loads(json.dumps(launcher.config))
        self.init_ui()
        
    def init_ui(self):
        main = QHBoxLayout(self)
        main.setSpacing(13)

        # Controles
        left = QVBoxLayout()
        left.setSpacing(13)

        left.addWidget(QLabel("🧭 Rombo de los Vientos"))
        grid = QGridLayout()
        grid.setSpacing(5)

        # Grupo excluyente: solo una posición activa. PEP20 - Explícito > Implícito
        self.grupo_rombo = QButtonGroup(self)
        self.grupo_rombo.setExclusive(True)
        self.botones_rombo = {} # Mapeo QTabWidget.North -> QPushButton para hidratación

        pos = [
            ("↑ Norte", QTabWidget.North, 0, 1),
            ("← Oeste", QTabWidget.West, 1, 0),
            ("→ Este", QTabWidget.East, 1, 2),
            ("↓ Sur", QTabWidget.South, 2, 1)
        ]
        for txt, val, row, col in pos:
            btn = QPushButton(txt)
            btn.setCheckable(True) # Para mostrar estado activo/inactivo
            self.grupo_rombo.addButton(btn, val) # El grupo los hace excluyentes tipo radio
            self.botones_rombo[val] = btn # Guardamos ref para despertar_panel
            btn.clicked.connect(lambda _, v=val: self.mutar_posicion(v))
            grid.addWidget(btn, row, col)
        left.addLayout(grid)

        # Sliders
        self.etiquetas_slider = {} # ← Guardar labels acá
        for label, attr, minv, maxv, default in [
            ("Tamaño GeckoTab", "s_tab", 180, 420, self.launcher.tamanio_geckotable.width()),
            ("Tamaño Icono",    "s_icon", 48, 180, 86),
            ("Tamaño Texto",    "s_texto", 12, 28, self.launcher.font_geckotable)
        ]:
            slider = PrecisionSliderH(self, orientation=Qt.Horizontal)
            slider.setMinimumHeight(45)
            slider.setRange(minv, maxv)
            slider.setValue(default)
            slider.valueChanged.connect(self.mutar_geometria)
            setattr(self, attr, slider)
            etiqueta = QLabel(f"{label}: {slider.value()}")
            self.etiquetas_slider[attr] = etiqueta # ← clave: "s_tab", "s_icon", "s_texto"
            left.addWidget(etiqueta)
            left.addWidget(slider)

        left.addWidget(QLabel("🎨 GeckoLAunker Icons Themes"))
        self.combo_tema = QComboBox()
        self.actualizar_temas()
        self.combo_tema.currentTextChanged.connect(self.mutar_tema)
        left.addWidget(self.combo_tema)

        self.chk_sonido = QCheckBox("🔊 Sonidos Geckónicos")
        self.chk_sonido.setChecked(self.launcher.geckosounds)
        self.chk_sonido.toggled.connect(self.mutar_sonido)
        left.addWidget(self.chk_sonido)

        h = QHBoxLayout()
        h.addWidget(QPushButton("<<<Go to Past", clicked=self.ir_al_pasado))
        h.addWidget(QPushButton("Reset Geckónic", clicked=self.reset_geckonico))
        left.addLayout(h)

        main.addLayout(left)

        # ===================== GECKOTAB DE MUESTRA =====================
        preview_group = QGroupBox("👁️ GeckoTab de Muestra (Preview)")
        p_layout = QVBoxLayout() # Layout del Preview
        
        # Live Preview (por detrás cambios on the Fly)
        self.preview = QListWidget()
        self.preview.setViewMode(QListWidget.IconMode)
        self.preview.setFixedSize(380, 260)
        self.preview.setSpacing(15)
        self.preview.setStyleSheet("""
            QListWidget { 
                background: #000000; 
                border: 3px solid #00ff88; 
                border-radius: 10px;
            }
        """)
        p_layout.addWidget(self.preview, alignment=Qt.AlignCenter)
        
        preview_group.setLayout(p_layout)
        main.addWidget(preview_group, alignment=Qt.AlignCenter)

        self.despertar_panel()
        self.actualizar_preview()
    
    def despertar_panel(self):
        """
        Arkano de Hidratación - Lee el Grimorio Sagrado y actualiza todos los widgets.
        Intención: Sincronizar UI con estado_mutagenico al nacer el panel.
        Se llama al final de init_ui después de crear todos los widgets.
        Tiene fallbacks robustos si el dic está corrupto o incompleto.
        """
        m = self.launcher.config.get("estado_mutagenico", {})

        # Sliders - tamaño [ancho, alto], solo usamos ancho para el slider
        self.s_tab.setValue(m.get("tamanio_geckotable", [226, 137])[0])
        self.s_icon.setValue(m.get("geckoiconsize", [86, 86])[0])
        self.s_texto.setValue(m.get("font_geckotable", 17))

        # Combo de tema - busca el texto en el combo, si no existe queda en índice 0
        tema_actual = m.get("IconThemeFolder", "default")
        idx = self.combo_tema.findText(tema_actual)
        if idx >= 0:
            self.combo_tema.setCurrentIndex(idx)

        # Checkbox de sonido
        self.chk_sonido.setChecked(m.get("geckosounds", False))

        # Position Pestañas - Banca int nuevo y string viejo
        pos_raw = m.get("tab_position", QTabWidget.South)
        # Si es string "QTabWidget.South" lo convierte a 1. Si ya es int, lo deja.
        if isinstance(pos_raw, str):
            pos_actual = getattr(QTabWidget, pos_raw.split(".")[-1], QTabWidget.South)
        else:
            pos_actual = pos_raw
        self.pintar_rombo_activo(pos_actual) # Limpiar tildes viejos y marcar el activo

    def actualizar_preview(self):
        self.preview.clear()

        item = QListWidgetItem("Brave")
        
        icon_path = os.path.join(self.launcher.IconPath, "brave.png")
        if os.path.exists(icon_path):
            item.setIcon(QIcon(icon_path))
        else:
            item.setIcon(QIcon.fromTheme("applications-internet"))

        item.setTextAlignment(Qt.AlignCenter)
        item.setSizeHint(self.launcher.tamanio_geckotable)

        # LÍNEA MÁGICA: Pintala para que se vea
        item.setBackground(QColor("#037730")) # ← VERDE GECKO CESPED OSCURO

        self.preview.addItem(item)

        # Aplicar exactamente lo mismo que en las tabs reales
        self.preview.setIconSize(self.launcher.geckoiconsize)
        self.preview.setGridSize(self.launcher.tamanio_geckotable)

        # Fuente
        font = self.preview.font()
        font.setPointSize(self.launcher.font_geckotable)
        self.preview.setFont(font)

    def mutar_geometria(self):
        tab_w = self.s_tab.value()
        icon_s = min(self.s_icon.value(), int(tab_w * 0.78))
        text_s = self.s_texto.value()

        # Actualizar textos de los labels en vivo
        self.etiquetas_slider["s_tab"].setText(f"Tamaño GeckoTab: {tab_w}")
        self.etiquetas_slider["s_icon"].setText(f"Tamaño Icono: {icon_s}")
        self.etiquetas_slider["s_texto"].setText(f"Tamaño Texto: {text_s}")

        self.launcher.tamanio_geckotable = QSize(tab_w, int(tab_w * 0.62))
        self.launcher.geckoiconsize = QSize(icon_s, icon_s)
        self.launcher.font_geckotable = text_s

        self.launcher.colapsar_realidad()
        self.actualizar_preview()
        self.launcher.guardar_lanzadores()
    
    def mutar_posicion(self, pos):
        self.launcher.tabs.setTabPosition(pos)
        self.launcher.colapsar_realidad()
        self.launcher.guardar_lanzadores()
        self.pintar_rombo_activo(pos) # Repintar tildes del Rombo sin tocar estilos

    def pintar_rombo_activo(self, pos_actual):
        for val, btn in self.botones_rombo.items():
            texto_base = btn.text().lstrip("✓ ")
            if val == pos_actual:
                btn.setText(f"✓ {texto_base}")
                btn.setChecked(True)
            else:
                btn.setText(texto_base)
                btn.setChecked(False)

    def mutar_tema(self, tema):
        self.launcher.IconThemeFolder = tema
        self.launcher.IconPath = os.path.join(self.launcher.scriptDir, "ThemeIcons", tema)
        self.launcher.colapsar_realidad()
        self.actualizar_preview()
        self.launcher.guardar_lanzadores()

    def mutar_sonido(self, estado):
        self.launcher.geckosounds = bool(estado)
        self.launcher.colapsar_realidad()
        self.launcher.guardar_lanzadores()

    def ir_al_pasado(self):
        self.launcher.config = json.loads(json.dumps(self.snapshot))
        self.launcher.colapsar_realidad()
        self.actualizar_preview()

    def reset_geckonico(self):
        self.launcher.tamanio_geckotable = QSize(226, 137)
        self.launcher.geckoiconsize = QSize(86, 86)
        self.launcher.font_geckotable = 17
        self.launcher.geckosounds = False
        self.launcher.colapsar_realidad()
        self.actualizar_preview()
        self.launcher.guardar_lanzadores()

    def actualizar_temas(self):
        path = os.path.join(self.launcher.scriptDir, "ThemeIcons")
        if os.path.exists(path):
            temas = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
            self.combo_tema.clear()
            self.combo_tema.addItems(temas)    

class GeckoLauncker(QMainWindow):
    def __init__(self):
        super().__init__()
        # La Ruta de Gecko en tu Systema
        self.scriptDir = os.path.dirname(os.path.realpath(__file__))
        
        self.offset = None
        self.setWindowTitle(f"🦎 GeckoLauncker Minimalista [3x4]{geckoappversion}")
        
        # Variables ConfigPanel Geckónico de GeckoLaunker
        self.tamanio_geckotable = (QSize(226, 137))
        self.font_geckotable = 17  # ← TU VARIABLE GLOBAL DE LETRA
        self.IconThemeFolder = "ThemeIcons"
        self.IconThemePath = os.path.join(self.scriptDir, self.IconThemeFolder)
        self.geckoiconsize = (QSize(86, 86))
        self.geckosounds = False #NIght Mode, Turn True on safety environment y en birome [t.ambien.t]
        
        # <<< VIENE MUCHA EXPLICACION PERO ES SOLO FISICA GECKONIANA Y NOSOTROS CREEMOS EN EL LIBRE ALVEDRIO DEL CODIGO>>>
        """Un redimensionamiento inteligente vale mas que mil harcodeadas sin sentido."""
        '''
        # Redimensionamos la ventana adaptada al tamaño fijo calculado + el espacio de las GeckoTabs del sur
        # Ancho: 737px (Grilla fija + bordes del QTabWidget)
        # Alto: 645px (Grilla de tabletas + barra de pestañas inferior + barra de título)
        self.resize(737, 645)
        '''

        # Icono de aplicación [el de la Ventana == el de la Barra == el del Alt+Tab: La Identidad Iconográfica]
        self.IconPath = os.path.join(self.scriptDir, 'Icons')
        icon_file = os.path.join(self.IconPath, 'appicon.png')
        if os.path.exists(icon_file):
            self.setWindowIcon(QtGui.QIcon(icon_file))

        self.player = QMediaPlayer()

        # Siempre Arriba
        #self.setWindowFlags(Qt.WindowStaysOnTopHint)  # siempre arriba

        # Sin Bordes (Estilo Flotante)
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Transparencia UI
        #self.setAttribute(Qt.WA_TranslucentBackground)
        #self.setAttribute(Qt.WA_NoSystemBackground, True)
                
        # Hacer que los widgets sean transparentes
        '''
        self.transparent_palette = QtGui.QPalette()
        self.transparent_palette.setColor(QtGui.QPalette.Base, Qt.transparent)
        self.transparent_palette.setColor(QtGui.QPalette.Window, Qt.transparent)
        self.setPalette(self.transparent_palette)
        '''
        self.config_file = os.path.expanduser("~/.config/gecko_lanzadoresv3x4.json")

        self.config = {
            "version": geckoappversion,
            "fondo_launcher": "#0a0a0a",
            "categorias": {
                "🦎 GeckoLAuncker": {
                    "items": [],
                    "tema": {
                        "color_texto": "#00ff88",
                        "color_fondo_lista": "#000000",
                        "color_fondo_item_activo": "#00ff88",
                        "color_texto_item_activo": "#000000"
                    }
                }
            },
            "estado_mutagenico": {  
                "tamanio_geckotable": [226, 137],
                "geckoiconsize": [86, 86],
                "font_geckotable": 17,
                "tab_position": QTabWidget.South,
                "IconThemeFolder": "default",
                "geckosounds": False
            }
        }

        self.cargar_lanzadores()
        
        self.setup_styles()
        
        self.init_ui()
        
        #Transparencias estilo Time is Time
        '''
        self.tabs.setStyleSheet("QTabWidget::pane { background: transparent; border: none; }")
        self.tabs.setAttribute(Qt.WA_TranslucentBackground)

        # Aplicar transparencia a los widgets dentro de las pestañas
        for i in range(self.tabs.count()):
            self.tabs.widget(i).setAttribute(Qt.WA_TranslucentBackground)
            self.tabs.widget(i).setPalette(self.transparent_palette)
        '''
        self.setStyleSheet(f"QMainWindow {{ background: {self.config.get('fondo_launcher', '#0a0a0a')}; }}")
        
        cleanconsole()
        print(get_version(easter_egg=True))

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
            QTabWidget::tab {
                font-weight: bold;
            }   
            QTabWidget::pane {
                font-weight: bold;
                border: 2px solid #00ff88;
                background: rgba(0, 0, 0, 0.85);
            }
            QTabBar::tab {
                background: #111;
                color: #00ff88;
                padding: 10px;
                border: 1px solid #333;
                font-weight: bold;
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
        """Inicializa el contenedor de GeckoTabs y tu primera lista """
        # --- Contenedor y Layout Principal ---
        self.launcker_conteiner = QGroupBox()
        self.launcker_layout = QVBoxLayout()
        self.launcker_layout.setContentsMargins(0, 0, 0, 0)
        self.launcker_conteiner.setLayout(self.launcker_layout)

        self.tabs = QTabWidget(self)
        
        # Despertar del ADN - lee estado_mutagenico del dic [by Llamita Encendida]
        m = self.config.get("estado_mutagenico", {})
        self.tamanio_geckotable = QSize(*m.get("tamanio_geckotable", [226, 137]))
        self.geckoiconsize = QSize(*m.get("geckoiconsize", [86, 86]))
        self.font_geckotable = m.get("font_geckotable", 17)
        self.IconThemeFolder = m.get("IconThemeFolder", "default")
        self.IconPath = os.path.join(self.IconThemePath, self.IconThemeFolder)

        #self.tabs.setTabPosition(eval(m.get("tab_position", "QTabWidget.South")))
        #self.tabs.setTabPosition(m.get("tab_position", QTabWidget.South))          # ← PONER: directo int

        '''
        # Soporte legacy: si el config viejo tiene string, lo parseamos. Si es int, pasa directo.
        tab_pos_raw = m.get("tab_position", QTabWidget.South)
        if isinstance(tab_pos_raw, str):
            tab_pos = getattr(QTabWidget, tab_pos_raw.split(".")[-1], QTabWidget.South)
        else:
            tab_pos = tab_pos_raw
        self.tabs.setTabPosition(tab_pos)
        '''
        # Lee tab_position nuevo, si no existe usa posicion_tabs viejo, si no existe usa South
        tab_pos_raw = m.get("tab_position", self.config.get("posicion_tabs", QTabWidget.South))
        tab_pos = getattr(QTabWidget, tab_pos_raw.split(".")[-1], QTabWidget.South) if isinstance(tab_pos_raw, str) else tab_pos_raw
        self.tabs.setTabPosition(tab_pos)

        self.tabs.setMovable(True)          
        self.tabs.setTabsClosable(True)     
        self.tabs.tabCloseRequested.connect(self.eliminar_categoria)
        self.tabs.currentChanged.connect(self.cambiar_lista_activa)
        
        self.tabs.tabBar().tabMoved.connect(self.reordenar_categorias_dict)

        #self.tabs.setTabPosition(posicionPestanasGecko)
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
        
        self.launcker_layout.addWidget(self.tabs)

        #version = QLabel(f"🦎 GeckoLAuncker [3x4]{geckoappversion}")
        #version.setStyleSheet("font-family: 'Ubuntu'; font-weight: bold;")
        self.launcker_layout.addWidget(QLabel(f"🦎 GeckoLAuncker [3x4]{geckoappversion}"), alignment=Qt.AlignRight)
        
                # === PANEL MUTAGÉNICO ===
        self.panel_mutagenico = PanelMutagenico(self)
        self.tabs.addTab(self.panel_mutagenico, "🧬 MUTAGÉNICO")

        self.setCentralWidget(self.launcker_conteiner)

    def play_sfx(self, nombre_archivo):
        """
        Funcion La Voz de Gecko Unificada, este metodo (que para mi es una funcion por "su funcion dentro de GeckoLAunker")
        es el centro del Sonido... el primer if lo explica todo, el PEPIF Primordial...
        """
        # Preparing Land for GeckoLAunker Config-Panel Landing
        if not self.geckosounds: #PEPIF Primordial
            return
        
        # Fuerza ruta absoluta siempre
        ruta_abs = os.path.abspath(os.path.join("/usr/share/sounds/freedesktop/stereo/", nombre_archivo))
        if os.path.isfile(ruta_abs):
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(ruta_abs)))
            self.player.play()
        else:
            print(f"🦎 SFX no encontrado: {ruta_abs}")

    def colapsar_realidad(self):
        """Arkano Supremo - Colapso de la Realidad Geckónica
        Intención: Cuando la Nave muta, el colapso no solo repinta la UI.
        Cristaliza el estado físico actual en self.config["estado_mutagenico"].
        La UI es el reflejo. El dic es la realidad. El colapso sincroniza ambos.
        Función: Se llama después de cualquier mutación. Garantiza que json = UI.
        """
        # La Nave muta en tiempo real
        for i in range(self.tabs.count()):
            widget = self.tabs.widget(i)
            if isinstance(widget, GeckoList):
                widget.setGridSize(self.tamanio_geckotable)
                widget.setIconSize(self.geckoiconsize)
                # Reaplicar fuente
                self.aplicar_estilo_lista(widget, self.tabs.tabText(i))
                # Actualizar tamaño de items existentes
                for j in range(widget.count()):
                    item = widget.item(j)
                    if item:
                        data = item.data(Qt.UserRole)
                        # LÍNEAS NUEVAS: Re-geckonizar con IconPath actual
                        _, icono_nuevo = self.geckonizar_nombre_e_icono(data["nombre"])
                        if icono_nuevo:
                            item.setIcon(icono_nuevo) # ← PISA EL QICON VIEJO

                        item.setSizeHint(self.tamanio_geckotable)
        self.update()
        self.repaint()
        # Cristalizar estado vivo en el dic fuente de verdad
        self.config["estado_mutagenico"] = {
            "tamanio_geckotable": [self.tamanio_geckotable.width(), self.tamanio_geckotable.height()],
            "geckoiconsize": [self.geckoiconsize.width(), self.geckoiconsize.height()],
            "font_geckotable": self.font_geckotable,
            #"tab_position": str(self.tabs.tabPosition()),
            "tab_position": int(self.tabs.tabPosition()),  # ← PONER: int nativo
            "IconThemeFolder": self.IconThemeFolder,
            "geckosounds": self.geckosounds,
        }

    # -----------------------------------------------------
    # --- Uno de los Nucleos Geckonicos de Gecko System ---
    # -----------------------------------------------------
    def crear_pestana(self, nombre_categoria):
        """ Fábrica para clonar exactamente tu lista con geometría fija sagrada """
        nueva_lista = GeckoList(self)
        
        # 📐 CONFIGURACIÓN DE LA MATRIX RÍGIDA
        nueva_lista.setViewMode(QListWidget.IconMode)
        nueva_lista.setIconSize(self.geckoiconsize)  # Tus sagrados 86x86 para que respire el texto
        nueva_lista.setGridSize(self.tamanio_geckotable)  # Las celdas arcanas de 237x137
        nueva_lista.setSpacing(10)  # El aire entre dimensiones de bloques
        nueva_lista.setUniformItemSizes(True)  # Fuerza al modelo a no estirar celdas de forma autónoma
        nueva_lista.setResizeMode(QListWidget.Fixed)  # No recalcules la grilla si el contenedor se mueve
        nueva_lista.setAcceptDrops(True)
        nueva_lista.setDragDropMode(QListWidget.InternalMove)
        
        # 🌌 CÁLCULO ARCANO DEL TAMAÑO FIJO DE LA LISTA (Para eliminar los Scrolls)
        # 3 Columnas de 237px + 2 Espacios intermedios de 10px + 6px de holgura para el borde neón
        ancho_fijo = (3 * self.tamanio_geckotable.width()) + (2 * 10) + 6
        # 4 Filas de 137px + 3 Espacios intermedios de 10px + 6px de holgura para el marco
        alto_fijo = (4 * self.tamanio_geckotable.height()) + (3 * 10) + 6
        
        # Seteamos el tamaño fijo absoluto. La lista ya no puede encogerse ni estirarse.
        #nueva_lista.setFixedSize(ancho_fijo, alto_fijo)
        nueva_lista.setMinimumSize(ancho_fijo, alto_fijo)
        
        # Desactivamos explícitamente las barras de scroll por si el framework duda en la Matrix
        nueva_lista.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        nueva_lista.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
        self.aplicar_estilo_lista(nueva_lista, nombre_categoria)
        
        # HUEVO DE PASCUA GECKONISTA: fuerza condiciones iniciales
        ruta_hmx = os.path.join(self.scriptDir, "hmx.py")
        if os.path.exists(ruta_hmx):
            huevo = QListWidgetItem("🐣\n\nhmx.py")
            huevo.setData(Qt.UserRole, {"nombre": "hmx.py", "ruta": ruta_hmx, "consola": False, "huevo": True})
            huevo.setSizeHint(self.tamanio_geckotable)  
            nueva_lista.addItem(huevo)

        nueva_lista.itemDoubleClicked.connect(self.ejecutar_lanzador)
        nueva_lista.model().rowsMoved.connect(lambda: self.sincronizar_orden_lista(nueva_lista))

        self.tabs.addTab(nueva_lista, nombre_categoria)
        self.tabs.setCurrentWidget(nueva_lista)
        #self.tabs.setStyleSheet("font-family: 'Terminal'; font-weight: bold;")
        
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

    # --- Física Geckónica MAtricial del Geckoniano ---
    def correccion_geckonica_gravedad(self, index):
        """
        Neurona de Lógica de Matriz (Index-Based).
        Ignora píxeles, usa la posición lógica en la grilla de 3 columnas.
        """
        global posicionPestanasGecko
        
        # Asumimos una grilla de 3 columnas (tu matriz 3x4)
        columna = index % 3
        fila = index // 3
        
        # MODO GRAVITATORIO: Apila por columnas primero, luego filas (estilo estantería)
        if posicionPestanasGecko in (QTabWidget.North, QTabWidget.South):
            return (columna, fila)
            
        # MODO MAGNÉTICO: Apila por filas primero (imán lateral)
        else:
            return (fila, columna)

    def sincronizar_orden_lista(self, lista_widget):
        global verFisicaGeckonica
        
        # 1. Bloqueo total para evitar recursividad
        lista_widget.blockSignals(True)
        lista_widget.model().blockSignals(True)
        self.setUpdatesEnabled(False)

        try:
            nombre_tab = self.tabs.tabText(self.tabs.indexOf(lista_widget))
            
            # 2. Capturamos la data en el orden actual (el que Qt nos da al soltar)
            items_data = []
            for i in range(lista_widget.count()):
                data = lista_widget.item(i).data(Qt.UserRole)
                if data and not data.get("huevo"):
                    items_data.append(data)

            # 3. Limpiamos la lista visualmente
            lista_widget.clear()
            
            # 4. Re-inyectamos el huevo (siempre primero)
            ruta_hmx = os.path.join(self.scriptDir, "hmx.py")
            if os.path.exists(ruta_hmx):
                huevo = QListWidgetItem("🐣\n\nhmx.py")
                huevo.setData(Qt.UserRole, {"nombre": "hmx.py", "ruta": ruta_hmx, "consola": False, "huevo": True})
                huevo.setSizeHint(self.tamanio_geckotable)
                lista_widget.addItem(huevo)

            # 5. Volvemos a agregar los ítems en el orden exacto que quedaron
            # ¡Ya no hay cálculos matemáticos raros aquí, el orden lo dicta el usuario!
            for data in items_data:
                self.agregar_item_lista(lista_widget, data["nombre"], data["ruta"], data["consola"], sync_config=False)

            # --- SOLUCIÓN CLAVE DE LEO [NO LOGRO VER CAMBIOS EN EL COMPORTAMIENTO DE GECKOTABS] ---
            # Permitir que la lista se encoja aunque los items tengan sizeHint fijo
            lista_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            
            # 6. Guardamos el nuevo estado en la Biblia JSON
            self.config["categorias"][nombre_tab]["items"] = items_data
            self.guardar_lanzadores()
            self.aplicar_estilo_lista(lista_widget, nombre_tab)

            # LEO Pone esto al final de sincronizar_orden_lista 
            lista_widget.setMinimumSize(0, 0) # Permite encogerse casi hasta desaparecer
            lista_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)   
            

        except Exception as e:
            print(f"❌ Error en la sincronización: {e}")
            
        finally:
            lista_widget.blockSignals(False)
            lista_widget.model().blockSignals(False)
            self.setUpdatesEnabled(True)
    # -------------------------------------------
    # --- LÓGICA DE ITEMS / TARJETAS TÁCTILES ---
    # -------------------------------------------
    def agregar_item_lista(self, lista_target, nombre, ruta, usar_consola=False, sync_config=True):
        icono_visual = "💻" if usar_consola else "⚙"

        #texto_tarjeta = f"{icono_visual}\n\n{nombre}"
        #item = QListWidgetItem(texto_tarjeta)
        #Geckonizado por NOva Pythonisa Pythonista
        nombre_visible, icono = self.geckonizar_nombre_e_icono(nombre)
        
        
        item = QListWidgetItem(nombre_visible)

        if icono is not None:
            item.setIcon(icono)
        else:
            emoji = "💻" if usar_consola else "⚙"
            item.setText(f"{emoji}\n\n{nombre_visible}")
        

        item.setData(Qt.UserRole, {"nombre": nombre, "ruta": ruta, "consola": usar_consola})
        item.setTextAlignment(Qt.AlignCenter)
        item.setSizeHint(self.tamanio_geckotable)  # ← AGREGAR ESTA LÍNEA
        lista_target.addItem(item)

        # AGREGAR: solo sincronizar si no estamos cargando desde config
        if sync_config:
            nombre_tab = self.tabs.tabText(self.tabs.indexOf(lista_target))
            if nombre_tab in self.config["categorias"]:
                self.config["categorias"][nombre_tab]["items"].append({"nombre": nombre, "ruta": ruta, "consola": usar_consola})

    def geckonizar_nombre_e_icono(self, nombre_archivo):
        base = nombre_archivo

        if base.startswith("geckolink_") and base.endswith(".sh"):
            base = base[len("geckolink_"):-3]

        nombre_visible = (
            base
            .replace("_", " ")
            .replace("-", " ")
            .title()
        )

        ruta_icono = os.path.join(
            self.IconPath,
            f"{base.lower()}.png"
        )

        icono = (
            QtGui.QIcon(ruta_icono)
            if os.path.exists(ruta_icono)
            else None
        )

        return nombre_visible, icono

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

    # ---------------------------------
    # --- MENÚ CONTEXTUAL UNIFICADO ---
    # ---------------------------------
    def mostrar_menu_contextual(self, pos_global, lista_origen=None):
        '''
        print("🔥 ORIGEN:", id(lista_origen), "SELF.LISTA:", id(self.lista))
        
        print("\n🧠 MENU REQUEST")
        print("   lista_origen:", lista_origen)
        print("   self.lista actual:", self.lista)
        print("   match:", lista_origen is self.lista)
        print("   type(lista_origen):", type(lista_origen))
        
        print("🔥 TAB ACTUAL:", self.tabs.currentIndex())
        print("🔥 WIDGET CURRENT:", self.tabs.currentWidget())
        print("🔥 lista_origen:", lista_origen)
        '''
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
        #print(f"🦎 DEBUG MENU FINAL → pos={pos_global} | actions={len(menu.actions())}")
        
        if menu.actions():
            # exec_ bloquea el hilo de forma segura y dibuja la mini-ventana arriba de todo
            self.play_sfx('bell.oga')  #🦎 MENU
            menu.exec_(pos_global)
        else:
            print("⚠️ Menú sin acciones!")

    # --------------------------------------
    # --- ACCIONES DE GESTIÓN (SIN EÑES) ---
    # --------------------------------------
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

    # -------------------------------------------
    # --- HACKS MOUSE DRAG REPARADOS (BY LEO) ---
    # -------------------------------------------
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = event.globalPosition().toPoint() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.offset is not None: 
            self.move(event.globalPosition().toPoint() - self.offset)
    
    def closeEvent(self, event):
        self.guardar_lanzadores()
        event.accept()

    # -----------------------------
    # --- PERSISTENCIA BLINDADA ---
    # -----------------------------
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
    launcher = GeckoLauncker()
    #TTM (Tungteno Titanio Molibdeno) Colour #19232d Geckonizante como el tema del MIT [for 🦎 V.54 TTM]
    launcher.setStyleSheet("background-color: #19232d; color: #00ff88;") 
    # Evaluar porque aca si obedece y dentro de las clases no!
    launcher.setStyleSheet("""
        QLabel {
            font-family: "Ubuntu", sans-serif; /* El sistema usará Noto Color Emoji para emojis */
            font-weight: bold;
            font-size: 12px;
            color: #00ff88;
        }
        QPushButton {
            font-family: "Ubuntu", sans-serif; /* El sistema usará Noto Color Emoji para emojis */
            font-weight: bold;
            font-size: 12px;
            color: #00ff88;
        }
        QComboBox {
            font-family: "Ubuntu", sans-serif; /* El sistema usará Noto Color Emoji para emojis */
            font-weight: bold;
            font-size: 12px;
            color: #00ff88;
        }
        QCheckBox {
            font-family: "Ubuntu", sans-serif; /* El sistema usará Noto Color Emoji para emojis */
            font-weight: bold;
            font-size: 12px;
            color: #00ff88;
        }
        QTabBar::tab {
            font-family: "Ubuntu", sans-serif; /* Mismo fallback */
            font-weight: bold;
            font-size: 12px;
            padding: 5px;
            color: #00ff88;
        }
        QGroupBox {
            font-family: "Ubuntu", sans-serif; /* El sistema usará Noto Color Emoji para emojis */
            font-weight: bold;
            font-size: 12px;
            color: #00ff88;
        }
    """)
    launcher.show()
    sys.exit(app.exec_())