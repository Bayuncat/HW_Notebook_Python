class Notebook:  
      
    def __init__(self, subject, text, datetimeNow):
        self.subject = subject
        self.text = text
        self.datetimeNow = datetimeNow
         
    def display_notebook(self):  
        print('Заголовок: {}. \nСообщение: {}. \nДата/время: {}\n'.format(self.subject,  self.text, self.datetimeNow))
    
    def getSubject(self):
        return self.subject

    def getText(self):
        return self.text
    
    def getDatetime(self):
        return self.datetimeNow