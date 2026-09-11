import pyxel
import calculatrice

calc = calculatrice.Calculatrice()
pyxel.init(160, 120, title="Calculatrice Graphique")

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    if pyxel.btnp(pyxel.KEY_1):
        calc.ajouter_nombre(1)
    if pyxel.btnp(pyxel.KEY_2):
        calc.ajouter_nombre(2)
        
    if pyxel.btnp(pyxel.KEY_PLUS):
        calc.operateur = "+"
        calc.addition()
    if pyxel.btnp(pyxel.KEY_MINUS):
        calc.operateur = "-"
        calc.soustraction()
    if pyxel.btnp(pyxel.KEY_ASTERISK):
        calc.operateur = "*"
        calc.multiplication()
    if pyxel.btnp(pyxel.KEY_SLASH):
        calc.operateur = "/"
        calc.division()
    if pyxel.btnp(pyxel.KEY_P):
        calc.operateur = "**"
        calc.puissance()
    if pyxel.btnp(pyxel.KEY_R):
        calc.operateur = "sqrt"
        calc.racine_carree()

def draw():
    calc.draw()

pyxel.run(update, draw)