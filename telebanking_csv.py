"""
  Telebanking CSV
"""

import csv
import locale
from tkinter import *
from tkinter import ttk

# globals:
csv_lines = []


'''
0 IBAN;
1 Auszugsnummer;
2 Buchungsdatum;
3 Valutadatum;
4 Umsatzzeit;
5 Zahlungsreferenz;
6 Waehrung;
7 Betrag;
8 Buchungstext;
9 Umsatztext
'''

csv_col_indeces_to_use = [2, 5, 7, 8, 9]

categories = {
    'AU': 'Auto',
    'AO': 'Ä.o.Grenzen',
    'BM': 'Bankomat',
    'EK': 'Einkauf',
    'BG': 'Bankgebühren',
    'BK': 'Betriebskosten',
    'FR': 'Fahhrad',
    'FW': 'Fernwärme',
    'GB': 'Gebühren',
    'GH': 'Gehalt',
    'GP': 'Greenpeace',
    'GI': 'GIS',
    'CP': 'Handy',
    'IN': 'Internet',
    'KL': 'Kleidung',
    'KI': 'Kirchenbeitrag',
    'MI': 'Misc.',
    'OB': 'OEBB',
    'ST': 'Strom',
    'SP': 'Spenden',
    'WW': 'WWF',
    'WE': 'Wohnung',
    'VS': 'Versicherungen',
    'XX': '--'
};

categories_inverse = {v: k for k, v in categories.items()} 

# important set locale because amounts in CSV are like '1.234,56' 
locale.setlocale(locale.LC_ALL, 'de_DE.utf8')


def defaultKeyForUmsatzText(t):
    t = t.casefold()
    if 'alturos' in t:
        return 'GH'
    elif 'bankomat' in t or 'quick-l' in t:
        return 'BM'
    elif 'verkehrsverbund' in t:
        return 'OB'
    elif 'depot' in t:
        return 'BG'
    elif 'upc' in t:
        return 'IN'
    elif 'telekom' in t:
        return 'CP'
    elif 'at55zzz00000061802' in t:
        return 'IN'
    elif 'at53 2011 1291 1268' in t:
        return 'WW'
    elif 'rechtsschutz' in t:
        return 'DA'
    elif 'gurk' in t:
        return 'KI'
    elif 'kelag' in t:
        return 'ST'
    elif 'messtechnik' in t:
        return 'FW'
    elif 'dau000002' in t or 'dau000001' in t:
        return 'BK'
    elif 'ohne grenzen' in t:
        return 'AO'
    elif 'gis' in t:
        return 'GI'
    elif 'billa' in t or 'bipa' in t or 'spar dankt' in t:
        return 'EK'
    elif 'caritas' in t:
        return 'SP'		
    else:
        return 'XX'

def defaultValueForUmsatzText(t):
    return categories[defaultKeyForUmsatzText(t)]

category_selections = []
amounts = []

class Application(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.title = ttk.Label(self)
        self.title['text'] = 'Telebanking CSV'
        self.title.pack(side="top")
        self.table = ttk.Frame(self)
        self.table.pack(side='top')
        for i in range(0, len(csv_lines)):
            line = csv_lines[i]
            jj = 0;
            for j in csv_col_indeces_to_use:
                txt="{},{}".format(i,j)
                e = ttk.Label(self.table, text=csv_lines[i][j][0:100], justify='right')
                e.grid(row=i, column=jj, sticky='W')
                jj += 1
            if (i > 0):
                # amounts
                amounts.append(locale.atof(csv_lines[i][7]))
                # combobox:
                val = StringVar(value = defaultValueForUmsatzText(csv_lines[i][9]))
                category_selections.append(val)
                combo = ttk.Combobox(self.table, values=list(categories.values()), textvariable=val)
                combo.grid(row=i, column=jj, sticky='W')
                
        self.buttons_frame = ttk.Frame(self)
        self.buttons_frame.pack(side='top')
        self.button1 = ttk.Button(self.buttons_frame, text="Test", command=self.button1_clicked)
        self.button1.pack(side='top')

    def button1_clicked(*args):
        summary = calculate_summary()
        print_summary(summary)
        print_for_copypaste(summary)
            
def calculate_summary():
    for v in category_selections:
        print(v.get())
    print(amounts)
    summary = {}
    for i in range(0, len(amounts) - 1):
        category_key = categories_inverse[category_selections[i].get()]
        if not category_key in summary:
            summary[category_key] = []
        summary[category_key].append(amounts[i])
        print(summary)
    return summary


def print_summary(summary):
    for k, v in summary.items():
        print(f'{categories[k]}\t: {sum(v):.2f} EUR')


def print_for_copypaste(summary):
    print("Incomes:")
    if 'GH' in summary:
        print(f2s(sum(summary['GH'])))
    else:
        print(0)
    print("Expenses:")
    for cat in list(categories):
        if cat in summary and cat != 'GH':
            print(f2s(-1 * sum(summary[cat])))
        else:
            print(0)

def f2s(f):
    return locale.format_string('%.2f', f)

def read_csv(csv_file_name):
    print(f'Start processing \'{csv_file_name}\'')
    with open(csv_file_name, newline='') as  csvfile:
        reader = csv.reader(csvfile, delimiter = ';' )
        for row in reader:
            csv_lines.append(row)
    
def print_csv_lines():
    n_lines = len(csv_lines);
    ii=0
    for line in csv_lines:
        print("", ii, ":", line)
        ii += 1                  
        
        
# main:
# ToDo consider to use 'argparse'
csv_file_name = 'umsaetze0.csv'
##if (len(sys.argv) < 2):
##    print("Usage:" + __name__ + " <csv_file_name>")
##    exit()
##csv_file_name = sys.argv[1]
read_csv(csv_file_name)
print('---------------------------------------------------')
print_csv_lines()

# start App window
root = Tk()
root.title("Telebanking CSV")
app = Application(master=root)
app.mainloop()
