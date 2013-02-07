from ofxstatement.parser import CsvStatementParser
from ofxstatement.plugin import Plugin
from ofxstatement import statement
import csv
import re


class BosDeCsvStatementParser(CsvStatementParser):
    mappings = {"date": 0, "memo": 1, "amount": 3}
    date_format = "%d.%m.%Y"

    def split_records(self):
        return csv.reader(self.fin, delimiter=';')
 
    def parse_record(self, line):
        #Lines with no information
        if self.cur_record <= 4 or (self.cur_record >=8 and self.cur_record<=11) or (self.cur_record >=13 and self.cur_record<=15):
            return None

        if self.cur_record == 5:
            self.statement.account_id=line[1]
            return None
        if self.cur_record == 6:
            self.statement.currency=line[1]
            return None
        if self.cur_record == 7:
            self.statement.start_balance=line[1].replace('.','').replace(',','.')
            return None
        if self.cur_record == 12:
            re1='.*?'	# Non-greedy match on filler
            re2='((?:(?:[0-2]?\\d{1})|(?:[3][01]{1}))[-:\\/.](?:[0]?[1-9]|[1][012])[-:\\/.](?:(?:[1]{1}\\d{1}\\d{1}\\d{1})|(?:[2]{1}\\d{3})))(?![\\d])'

            rg = re.compile(re1+re2+re1+re2,re.IGNORECASE|re.DOTALL)
            m = rg.search(line[0])
            self.statement.start_date=m.group(1)
            self.statement.end_date=m.group(2)
            return None

        #Change decimalsign from , to .
        line[2]=line[2].replace('.','').replace(',','.')
        line[3]=line[3].replace('.','').replace(',','.')

        if line[2] != '0.00':
            line[3] = "-"+line[2]
            
        # fill statement line according to mappings
        sl = super(BosDeCsvStatementParser, self).parse_record(line)
        return sl    


class BosDePlugin(Plugin):
    name = "bos_de"
    def get_parser(self, fin):
        f = open(fin, "r",encoding='iso-8859-1')
        parser=BosDeCsvStatementParser(f)
        parser.statement.account_id = self.settings['account']
        parser.statement.currency = self.settings['currency']
        parser.statement.bank_id = self.settings.get('bank', 'Bank of Scotland') 
        return parser

