#Для работы с GUI
import sys
from form import *
#Для открытие страниц в браузере
import webbrowser
#Для парсинга RSS
import feedparser
#Для создания БД
import sqlite3
#Для использования массивов и работы с ними
import numpy as np
#Для получение текста из html
import html2text
#Для обработки дат
from datetime import datetime

class App(QtWidgets.QMainWindow):
    
    data = list()
    crntdata = np.array([])
    
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.database = DataBase()
        self.loadFeedsFromDB()
        self.loadCurrentFeed()
        self.setEvents()
        
    #Загрузка данных с RSS каналов из БД
    def loadFeedsFromDB(self):
        with self.database.con:
            self.database.cursor.execute('select * from links')
            while True:
                record = self.database.cursor.fetchone()    
                if record == None:
                    break
                print('Parsing',record[0])
                self.downloadFeed(record[0])
    #Парсинг RSS канала по ссылке
    def downloadFeed(self, link):
        page = feedparser.parse(link)
        data = getData(page)
        print('Parsing',link,'completed')
        self.data.append(data)
        self.ui.ComboBoxFeed.addItem(page['feed']['title'])
        print('Feed', page['feed']['title'], 'loaded in array')
    #Загрузка контента содержимого текущего RSS канала в GUI
    def loadCurrentFeed(self):
        if self.ui.ComboBoxFeed.currentIndex() == -1:
            print('Trying to load unselected RSS feed')
            return None
        
        self.crntdata = self.data[self.ui.ComboBoxFeed.currentIndex()]
        
        self.ui.ListWidgetTitle.clear()
        self.ui.ListWidgetCategory.clear()
        self.ui.ListWidgetDate.clear()
        self.ui.ComboBoxCategory.clear()
        print('Widgets content cleared')
        
        self.categories = np.array([])
        
        for entry in self.crntdata:
            self.ui.ListWidgetTitle.addItem(entry['title'])
            self.ui.ListWidgetCategory.addItem(entry['category'])
            self.ui.ListWidgetDate.addItem(entry['published'])
            self.categories = np.append(self.categories, entry['category'])
            
        self.categories =  np.concatenate((['Category'], np.unique(self.categories)))
        self.ui.ComboBoxCategory.addItems(self.categories)
        print('Feed',self.ui.ComboBoxFeed.currentText(),'loaded in widgets')
    
    #Назначение событий элементам GUI
    def setEvents(self):
        #Нажатие на кнопку добавления нового RSS канала
        self.ui.ButtonAdd.clicked.connect(self.addNewFeed)
        #Поменялся в ComboBox текущий RSS канал
        self.ui.ComboBoxFeed.currentIndexChanged.connect(self.loadCurrentFeed)
        #Поменялась текущая запись в таблице
        self.ui.ListWidgetTitle.currentRowChanged.connect(self.displayCurrentEntry)
        #Двойной клик по записи в таблице
        self.ui.ListWidgetTitle.itemDoubleClicked.connect(self.openCurrentEntryInBrowser)
        self.ui.ListWidgetCategory.itemDoubleClicked.connect(self.openCurrentEntryInBrowser)
        self.ui.ListWidgetDate.itemDoubleClicked.connect(self.openCurrentEntryInBrowser)
        #Поменялась в ComboBox текущая категория
        self.ui.ComboBoxCategory.currentIndexChanged.connect(self.filterByCurrentCategory)
        #Нажата кнопка "поиск по ключевому слову"
        self.ui.ButtonSearch.clicked.connect(self.filterByKeyWord)
        #Объединение событий QListWidget под одну таблицу
        self.connectListWidgets()
    
    #Вызов диалогового окна для получения ссылки на RSS канал
    def inputDialogLinkInput(self):
        inp = QtWidgets.QInputDialog(self)
        inp.setInputMode(QtWidgets.QInputDialog.TextInput)
        inp.setFixedSize(560, 180)
        inp.setWindowTitle('Adding rss feed')
        inp.setLabelText('RSS feed link:')
        link = ''
        while  inp.exec_() == QtWidgets.QDialog.Accepted:
            if isLinkValid(inp.textValue()):
                link = inp.textValue()
                break
            else:
                inp.setWindowTitle('Adding rss feed***Link is`t valid***')
                
        inp.deleteLater()
        
        return link
    #Загрузка и добавление в БД нового RSS канала по ссылке
    def addNewFeed(self):
        link = self.inputDialogLinkInput()
        
        if link != '':
            with self.database.con:
                self.database.cursor.execute('select exists(select * from links where link = "' + link + '" limit 1)')
                existance = self.database.cursor.fetchone()[0]
            if existance == 0:
                with self.database.con:
                    self.database.cursor.execute('insert into links (link) values ("' + link + '")')
                    print('the link is added to DB')
                self.downloadFeed(link)
            else:
                print('This feed already exists')
    #Вывод заголовка и содержимго текущей записи в таблице
    def displayCurrentEntry(self):
        crntentry = self.ui.ListWidgetTitle.currentRow()
        print('Entry', crntentry + 1,'is displayed')
        if crntentry != -1:
            self.ui.LabelTitle_2.setText(self.crntdata[crntentry]['title'])
            self.ui.TextEditContent.setText(self.crntdata[crntentry]['summary'])
    #Открытие в браузере сайта по ссылке из текущей записи        
    def openCurrentEntryInBrowser(self):
        crntEntry = self.ui.ListWidgetTitle.currentRow()
        link = self.crntdata[crntEntry]['link']
        print('Followed the link', link)
        webbrowser.open(link)
    
    #Отображение в таблице записей с категорией соответствующей текущей  
    def filterByCurrentCategory(self):
        
        crntcategory = self.ui.ComboBoxCategory.currentText()
        
        if self.ui.ComboBoxFeed.currentIndex() == -1 or self.ui.ComboBoxCategory.currentIndex() == -1:
            print('Trying filter by unselected category')
            return None
        
        self.ui.ListWidgetTitle.clear()
        self.ui.ListWidgetCategory.clear()
        self.ui.ListWidgetDate.clear()
        self.crntdata = np.array([])
        
        data = self.data[self.ui.ComboBoxFeed.currentIndex()]
        i = 0
        for entry in data:
            if crntcategory == entry['category'] or crntcategory == 'Category':
                self.ui.ListWidgetTitle.addItem(entry['title'])
                self.ui.ListWidgetCategory.addItem(entry['category'])
                self.ui.ListWidgetDate.addItem(entry['published'])
                self.crntdata = np.append(self.crntdata, entry)
                i += 1
        print('filtering by category', crntcategory, 'is completed')
        
    #Отображение в таблице записей соответствующих ключевому слову  
    def filterByKeyWord(self):
        crntword = self.ui.EntrySearch.text()
        if crntword == '':
            self.filterByCurrentCategory()
            print('filtering by keyword reset')
        else:
            self.filterByCurrentCategory()
            
            data = np.array([])
            j = 0
            for i in range(self.ui.ListWidgetTitle.count())[::-1]:
                
                if self.ui.ListWidgetTitle.item(i).data(0).find(crntword) != -1:
                    data = np.append(data, self.crntdata[i])
                    j += 1
                    continue
                
                if self.crntdata[i]['summary'].find(crntword) != -1:
                    data = np.append(data, self.crntdata[i])
                    j += 1
                    continue
                
                else:
                    self.ui.ListWidgetTitle.takeItem(i)
                    self.ui.ListWidgetCategory.takeItem(i)
                    self.ui.ListWidgetDate.takeItem(i)
                   
            self.crntdata = data[::-1]
            print('filtering by category', crntword, 'is completed')
    #Связь событий QListWidget       
    def connectListWidgets(self):
        self.ui.ListWidgetTitle.verticalScrollBar().valueChanged.connect(self.ui.ListWidgetCategory.verticalScrollBar().setValue)
        self.ui.ListWidgetTitle.verticalScrollBar().valueChanged.connect(self.ui.ListWidgetDate.verticalScrollBar().setValue)
        
        self.ui.ListWidgetCategory.verticalScrollBar().valueChanged.connect(self.ui.ListWidgetTitle.verticalScrollBar().setValue)
        self.ui.ListWidgetCategory.verticalScrollBar().valueChanged.connect(self.ui.ListWidgetDate.verticalScrollBar().setValue)
        
        self.ui.ListWidgetDate.verticalScrollBar().valueChanged.connect(self.ui.ListWidgetTitle.verticalScrollBar().setValue)
        self.ui.ListWidgetDate.verticalScrollBar().valueChanged.connect(self.ui.ListWidgetCategory.verticalScrollBar().setValue)
        
        self.ui.ListWidgetTitle.currentRowChanged.connect(self.ui.ListWidgetCategory.setCurrentRow)
        self.ui.ListWidgetTitle.currentRowChanged.connect(self.ui.ListWidgetDate.setCurrentRow)
        
        self.ui.ListWidgetCategory.currentRowChanged.connect(self.ui.ListWidgetTitle.setCurrentRow)
        self.ui.ListWidgetCategory.currentRowChanged.connect(self.ui.ListWidgetDate.setCurrentRow)
        
        self.ui.ListWidgetDate.currentRowChanged.connect(self.ui.ListWidgetTitle.setCurrentRow)
        self.ui.ListWidgetDate.currentRowChanged.connect(self.ui.ListWidgetCategory.setCurrentRow)
        
    
#БД хранящая ссылки RSS каналов
class DataBase:

    def __init__(self):
        self.con = sqlite3.connect('LINKS.db')
        self.cursor = self.con.cursor()
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS links (
            link text primary key)''')
        self.con.commit()  
#Проверка, что это действительная ссылка на RSS канал
def isLinkValid(link):
    page = feedparser.parse(link)
    try:
        page['feed']['title']
        return True
    except:
        return False
#Сбор данных     
def getData(page):
    
    data = np.array([])
    
    decoder = html2text.HTML2Text()
    decoder.body_width = False
    decoder.ignore_images = True
    decoder.ignore_links = True

    
    for i, entry in enumerate(page['entries']):
        
        data = np.append(data, dict())
        data[i]['title'] = entry['title'].replace('&quot;','"')
        data[i]['link'] = entry['link']
        data[i]['summary'] = decoder.handle('<HTML><BODY>' + entry['summary'] + '</BODY></HTML>')
        
        try:
            entry['category']
            data[i]['category'] = entry['category']
        except:
            data[i]['category'] = 'None'
            
        try:
            entry['published']

            date = datetime.strptime(entry['published'][:-9],'%a, %d %b %Y %H:%M')
            if date.date() == datetime.today().date():
                data[i]['published'] = datetime.strftime(date,'%H:%M')
            else:
                data[i]['published'] = datetime.strftime(date,'%H:%M %d.%m.%Y')
            
        except:
            data[i]['published'] = None
            
    return data

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = App()
    myapp.show()
    sys.exit(app.exec_())