import doctest

from ofxstatement.plugins.bos_de import BosDeCsvStatementParser

def doctest_BosDeCsvStatementParser():
    """Test BosDeCsvStatementParser

    Open sample csv to parse
        >>> import os
        >>> csvfile = os.path.join(os.path.dirname(__file__),
        ...                        'samples', 'bos_de.CSV')

    Create parser object and parse:
        >>> fin = open(csvfile, 'r', encoding='iso-8859-1')
        >>> parser = BosDeCsvStatementParser(fin)
        >>> statement = parser.parse()

    Check what we've got:
        >>> statement.account_id
        '12345678'
        >>> len(statement.lines)
        10
        >>> statement.start_balance
        '11222.33'
        >>> statement.start_date
        '01.02.2012'
        >>> statement.end_balance
        >>> statement.end_date
        '07.02.2013'
        >>> statement.currency
        'EUR'

    Check first line
        >>> l = statement.lines[0]
        >>> l.amount
        1200.0
        >>> l.payee 
        >>> l.memo
        'Zahlungseingang:ÜBERWEISUNG AUF BOS:'
        >>> l.date
        datetime.datetime(2013, 2, 3, 0, 0)

    Check one more line:
        >>> l=statement.lines[1]
        >>> l.amount
        -1000.0
        >>> l.payee
        >>> l.memo
        'Überweisung:Übertrag Tagesgeld:'
        >>> l.date
        datetime.datetime(2013, 1, 2, 0, 0)

    Check one more line:
        >>> l=statement.lines[4]
        >>> l.amount
        -11.07
        >>> l.memo
        'Solidaritätszuschlag'

    Check last line:
        >>> l=statement.lines[9]
        >>> l.amount
        -1000.0
        >>> l.memo
        'Überweisung'
    """

def test_suite(*args):
    return doctest.DocTestSuite(optionflags=(doctest.NORMALIZE_WHITESPACE|
                                             doctest.ELLIPSIS|
                                             doctest.REPORT_ONLY_FIRST_FAILURE|
                                             doctest.REPORT_NDIFF
                                             ))
load_tests = test_suite

if __name__ == "__main__":
    doctest.testmod()

