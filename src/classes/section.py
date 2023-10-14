class Section:
    def __init__(self, section):
        self.header = section.find('h2')
        self.table = None
        self.headings = []
        self.rows = []

        if section.find('table',{'class','sortable stats_table'}) != None:
            self.table = section.find('table',{'class','sortable stats_table'})
            for heading in self.table.find('thead').find('tr',{'class':None}).find_all('th'):
                self.headings.append(heading.text)
            for row in self.table.find('tbody').find_all('tr'):
                thisRow = []
                thisRow.append(row.find('th').text)
                for data in row.find_all('td'):
                    thisRow.append(data.text)
                self.rows.append(thisRow)

            
        else:
            self.table = None
        




