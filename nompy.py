# -*- coding: utf-8 -*-

import sys
import re
from PyQt5 import QtCore, QtGui, QtWidgets
from nompy_interface import Ui_MainWindow
from nompy_about import Ui_aboutDialog
import nompy_core

class AboutWindow(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.aboutDialog = QtWidgets.QDialog
        self.ad = Ui_aboutDialog()
        self.ad.setupUi(self)
        self.ad.closeButton.clicked.connect(self.close)

"""
class dishAddedTableItemDelegate(QtWidgets.QItemDelegate):
    def __init__(self):
        QtWidgets.QItemDelegate.__init__(self)
    def QLineEdit(self):
        QtWidgets.QLineEdit.setMaxLength(3)
"""


class Interface(QtWidgets.QMainWindow):

    #changeQuantity = QtCore.pyqtSignal(int, int)

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.mainWindow = QtWidgets.QMainWindow
        self.about = AboutWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionQuit.triggered.connect(QtCore.QCoreApplication.instance().quit)
        self.ui.actionAbout.triggered.connect(lambda: self.about.exec_())
        self.ui.buttonAddDish.clicked.connect(self.addDish)
        self.ui.buttonAddDish.setEnabled(False)
        self.ui.buttonPlusQty.clicked.connect(self.buttonPlusQtyClicked)
        self.ui.buttonPlusQty.setEnabled(False)
        self.ui.buttonMinusQty.clicked.connect(self.buttonMinusQtyClicked)
        self.ui.buttonMinusQty.setEnabled(False)
        self.ui.buttonRemoveDish.clicked.connect(self.removeDish)
        self.ui.buttonRemoveDish.setEnabled(False)
        self.ui.searchBox.textEdited["QString"].connect(self.search)
        self.ui.dishIngredientTabWidget.currentChanged.connect(self.tabChanged)

        # Fill Dish list with names from dishes.json
        self._translate = QtCore.QCoreApplication.translate
        for self.index, self.dishName in enumerate(nompy_core.getDishNames()):
            self.ui.item = QtWidgets.QListWidgetItem()
            self.ui.dishList.addItem(self.ui.item)
            self.ui.item = self.ui.dishList.item(self.index)
            self.ui.item.setText(self._translate("MainWindow", self.dishName))
        self.ui.dishList.sortItems()
        self.ui.dishList.itemClicked.connect(self.dishListClicked)

        # Fill Ingredient list with names from ingredients.json
        for self.index, self.ingredientName in enumerate(nompy_core.getIngredientNames()):
            self.ui.item = QtWidgets.QListWidgetItem()
            self.ui.ingredientList.addItem(self.ui.item)
            self.ui.item = self.ui.ingredientList.item(self.index)
            self.ui.item.setText(self._translate("MainWindow", self.ingredientName))
        self.ui.ingredientList.sortItems()
        self.ui.ingredientList.itemClicked.connect(self.ingredientListClicked)

        self.ui.dishAddedTable.cellDoubleClicked.connect(self.dishAddedTableDoubleclicked)
        #self.changeQuantity.connect(self.editQuantity)
        self.ui.dishAddedTable.cellClicked.connect(self.dishAddedTableCellClicked)
        #self.dishAddedTableItemColumnDelegate = dishAddedTableItemDelegate()
        #self.ui.dishAddedTable.setItemDelegateForColumn(1, self.dishAddedTableItemColumnDelegate)


    def tabChanged(self, tabIndex):
        # Dish Tab
        if tabIndex == 0:
            self.ui.buttonAddDish.setText(self._translate("MainWindow", "Add Dish"))
        # Ingredient Tab
        if tabIndex == 1:
            self.ui.buttonAddDish.setText(self._translate("MainWindow", "Add Ingredient"))

    def dishAddedTableCellClicked(self):
        self.ui.buttonRemoveDish.setEnabled(True)
        self.ui.buttonPlusQty.setEnabled(True)
        self.ui.buttonMinusQty.setEnabled(True)

    def dishListClicked(self):
        self.ui.buttonAddDish.setEnabled(True)
        self.clickedDish = nompy_core.Dish(self.ui.dishList.currentItem().text())
        print(self.clickedDish.dishStats)

        # Dish stat output
        self.ui.dishBrowser.setHtml(self._translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Dish stats</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Calories: " + str(round(self.clickedDish.dishStats["calories"],1)) + "<br>Fat: " + str(round(self.clickedDish.dishStats["fat"],1)) + "<br>Sat. Fat: " + str(round(self.clickedDish.dishStats["saturatedFat"],1)) + "<br>Carbs: " + str(round(self.clickedDish.dishStats["carbs"],1)) + "<br>Fiber: " + str(round(self.clickedDish.dishStats["fiber"],1)) + "<br>Protein: " + str(round(self.clickedDish.dishStats["protein"],1)) + "<br>Salt: " + str(round(self.clickedDish.dishStats["salt"],1)) + "<br>Iron: " + str(round(self.clickedDish.dishStats["iron"],1)) + "</span></p></body></html>"))

    def unitAbbreviation(self):
        self.unitAbbreviationDict = {"gram": "g", "deciliter": "dl", "milliliter": "ml", "piece": "pc"}
        if self.clickedIngredient.stats["unit"] in self.unitAbbreviationDict.keys():
            return str(round(self.clickedIngredient.stats["amount"],1)) + self.unitAbbreviationDict[self.clickedIngredient.stats["unit"]]
        else:
            return str(round(self.clickedIngredient.stats["amount"],1)) + " " + self.clickedIngredient.stats["unit"]


    def ingredientListClicked(self):
        #self.ui.buttonAddDish.setEnabled(True)
        self.clickedIngredient = nompy_core.Ingredient(self.ui.ingredientList.currentItem().text())
        print(self.clickedIngredient.stats)

        unitOutput = self.unitAbbreviation()


        # Ingredient stat output
        self.ui.dishBrowser.setHtml(self._translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Ingredient stats</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Amount: " + unitOutput + "<br>Calories: " + str(round(self.clickedIngredient.stats["calories"],1)) + "<br>Fat: " + str(round(self.clickedIngredient.stats["fat"],1)) + "<br>Sat. Fat: " + str(round(self.clickedIngredient.stats["saturatedFat"],1)) + "<br>Carbs: " + str(round(self.clickedIngredient.stats["carbs"],1)) + "<br>Fiber: " + str(round(self.clickedIngredient.stats["fiber"],1)) + "<br>Protein: " + str(round(self.clickedIngredient.stats["protein"],1)) + "<br>Salt: " + str(round(self.clickedIngredient.stats["salt"],1)) + "<br>Iron: " + str(round(self.clickedIngredient.stats["iron"],1)) + "</span></p></body></html>"))

    def search(self):
        self.searchString = self.ui.searchBox.text()
        # making the string lowercase for case insensitivity
        self.searchString = self.searchString.lower()
        self.ui.dishList.clear()
        self.ui.buttonAddDish.setEnabled(False)
        # http://stackoverflow.com/questions/4843158/check-if-a-python-list-item-contains-a-string-inside-another-string
        self.matchingDishes = [s for s in nompy_core.getDishNames() if self.searchString in s.lower()]
        self.ui.dishList.addItems(self.matchingDishes)

    def getDishAddedTableItemCoordinates(self, searchString):
        matchingItems = self.ui.dishAddedTable.findItems(searchString, QtCore.Qt.MatchExactly)
        #print(self.ui.dishAddedTable.row(matchingItem))
        #print(self.ui.dishAddedTable.column(matchingItem))
        for item in matchingItems:
            row = self.ui.dishAddedTable.row(item)
            col = self.ui.dishAddedTable.column(item)
        return row, col

    def addDish(self):
        # If the dish is already in dishAddedTable, change its quantity instead
        if self.ui.dishAddedTable.findItems(self.ui.dishList.currentItem().text(), QtCore.Qt.MatchExactly):
            print("Dish already added to table, increasing Quantity instead.")
            self.increaseDishQuantity(self.ui.dishList.currentItem().text())
        else:
            # Add a dish to dishAddedTable
            self.ui.dishAddedTable.setRowCount(self.ui.dishAddedTable.rowCount() + 1)
            # Quantity first
            self.ui.item = QtWidgets.QTableWidgetItem()
            self.ui.item.setText("1x")
            self.ui.item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.ui.dishAddedTable.setItem(self.ui.dishAddedTable.rowCount() -1, 0,  self.ui.item)
            # Dish or ingredient name next
            self.ui.item = QtWidgets.QTableWidgetItem()
            self.ui.item.setText(self.ui.dishList.currentItem().text())
            self.ui.item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
            self.ui.dishAddedTable.setItem(self.ui.dishAddedTable.rowCount() -1, 1, self.ui.item)

        self.calculate()

    def increaseDishQuantity(self, dishName):
        row, col = self.getDishAddedTableItemCoordinates(dishName)
        newQuantity = int(self.numbersOnly(self.ui.dishAddedTable.item(row, col - 1).text()) + 1)
        self.ui.dishAddedTable.item(row, col - 1).setText(str(newQuantity) + "x")

    def decreaseDishQuantity(self, dishName):
        row, col = self.getDishAddedTableItemCoordinates(dishName)
        if int(self.numbersOnly(self.ui.dishAddedTable.item(row, col - 1).text())) == 1:
            self.removeDish()
        else:
            newQuantity = int(self.numbersOnly(self.ui.dishAddedTable.item(row, col - 1).text()) - 1)
            self.ui.dishAddedTable.item(row, col - 1).setText(str(newQuantity) + "x")
            self.calculate()

    def buttonPlusQtyClicked(self):
        self.increaseDishQuantity(self.ui.dishAddedTable.item(self.ui.dishAddedTable.currentRow(), 1).text())
        self.calculate()

    def buttonMinusQtyClicked(self):
        self.decreaseDishQuantity(self.ui.dishAddedTable.item(self.ui.dishAddedTable.currentRow(), 1).text())

    def dishAddedTableDoubleclicked(self, row, col):
        #row = self.ui.dishAddedTable.currentRow()
        #col = self.ui.dishAddedTable.currentCol()
        # When user doubleclicks Qty col
        if col == 0:
            print("User doubleclicked row col.")
            #print(self.ui.dishAddedTable.item(row, col).text() + " new qty value")
            #self.changeQuantity.emit(row, col)
            self.ui.dishAddedTable.cellChanged.connect(self.editQuantity)
        else:
            pass

    def editQuantity(self, row, col):
        self.ui.dishAddedTable.cellChanged.disconnect()
        if self.ui.dishAddedTable.item(row,col).text() == "":
            if self.ui.dishAddedTable.item(row, col + 1).text() in nompy_core.getDishNames():
                self.ui.dishAddedTable.item(row, col).setText("1x")
            else:
                pass
        else:
            # Cleans up everything but digits and dots. TODO: Alert dialogue if it contains more than one dot.
            self.newQuantity = re.sub("[^0123456789\.]", "", self.ui.dishAddedTable.item(row, col).text())
            print("Cleaned up Qty value " + self.ui.dishAddedTable.item(row, col).text() + " to " + self.newQuantity)
            if int(self.newQuantity) > 999:
                # Input greater than 999 will reset the value to 1 to avoid MemoryError
                # TODO: Alert Dialogue
                if self.ui.dishAddedTable.item(row, col + 1).text() in nompy_core.getDishNames():
                    self.ui.dishAddedTable.item(row, col).setText("1x")
                    self.calculate()
                else:
                    pass
            elif self.newQuantity == "0":
                self.removeDish()
            else:
                if self.ui.dishAddedTable.item(row, col + 1).text() in nompy_core.getDishNames():
                    self.ui.dishAddedTable.item(row, col).setText(self.newQuantity + "x")
                    self.calculate()
                else:
                    pass

    def removeDish(self):
        self.ui.dishAddedTable.removeRow(self.ui.dishAddedTable.currentRow())
        if self.ui.dishAddedTable.rowCount() == 0:
            self.ui.buttonRemoveDish.setEnabled(False)
            self.ui.buttonPlusQty.setEnabled(False)
            self.ui.buttonMinusQty.setEnabled(False)
            self.ui.outputBrowser.clear()
        else:
            self.calculate()

    # Cleans up everything but digits and dots. TODO: Alert dialogue if it contains more than one dot.
    def numbersOnly(self, content):
        self.cleanQuantity = float(re.sub("[^0123456789\.]", "", content))
        print("Cleaned up Qty value " + content + " to " + str(self.cleanQuantity) + " in numbersOnly function")
        return self.cleanQuantity

    def calculate(self):
        dishAddedItems = []
        for index in range(self.ui.dishAddedTable.rowCount()):
            if self.numbersOnly(self.ui.dishAddedTable.item(index, 0).text()) == 1:
                dishAddedItems.append(self.ui.dishAddedTable.item(index, 1).text())
            else:
                # TODO: Change this to avoid MemoryError when appending dishes in larger quantities
                # Current workaround this issue is in editQuantity function
                for quantity in range(int(self.numbersOnly(self.ui.dishAddedTable.item(index, 0).text()))):
                    dishAddedItems.append(self.ui.dishAddedTable.item(index, 1).text())
        print(str(dishAddedItems) + " Dishes Added")
        finalSum = nompy_core.getMultipleDishStats(dishAddedItems)

        # Output format
        self.ui.outputBrowser.setHtml(self._translate("MainWindow", "<b>Selected dishes contain:</b>" \
        " <p>Calories: {calories}<br> Fat: {fat}g <br> Saturated Fat: {saturatedFat}g <br>" \
        "Carbohydrates: {carbs}g <br> Fiber: {fiber}g <br> Protein: {protein}g <br> Salt: {salt}g " \
        "<br> Iron: {iron}g </p>".format(calories=str(round(finalSum["calories"],1)), fat=str(round(finalSum["fat"],1)),
        saturatedFat=str(round(finalSum["saturatedFat"],1)), carbs=str(round(finalSum["carbs"],1)),
        fiber=str(round(finalSum["fiber"],1)), protein=str(round(finalSum["protein"],1)),
        salt=str(round(finalSum["salt"],1)), iron=str(round(finalSum["iron"],1)))))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    nompy = Interface()
    nompy.show()
    sys.exit(app.exec_())
