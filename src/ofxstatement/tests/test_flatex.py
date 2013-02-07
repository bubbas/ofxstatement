import doctest

from ofxstatement.plugins.flatex import FlatexCsvStatementParser

def doctest_FlatexCsvStatementParser():
    """Test FlatexCsvStatementParser

    Open sample csv to parse
        >>> import os
        >>> csvfile = os.path.join(os.path.dirname(__file__),
        ...                        'samples', 'flatex.csv')

    Create parser object and parse:
        >>> fin = open(csvfile, 'r', encoding='iso-8859-1')
        >>> parser = FlatexCsvStatementParser(fin)
        >>> statement = parser.parse()

    Check what we've got:
        >>> statement.account_id
        >>> len(statement.lines)
        6
        >>> statement.start_balance
        >>> statement.start_date
        >>> statement.end_balance
        >>> statement.end_date
        >>> statement.currency
        'EUR'

    Check first line
        >>> l = statement.lines[0]
        >>> l.amount
        0.0
        >>> l.payee 
        >>> l.memo
        'Zinsabschluss 01.01.2012,- 31.03.2012,TA-Nr.: 123456789'
        >>> l.date
        datetime.datetime(2012, 4, 3, 0, 0)

    Check one more line:
        >>> l=statement.lines[2]
        >>> l.amount
        -33.31
        >>> l.memo
        'Ausführung ORDER Kauf,LU1234567892 12345678,TA-Nr.: 345678912'
        >>> l.date
        datetime.datetime(2012, 4, 8, 0, 0)

    Check one more line with payee:
        >>> l=statement.lines[5]
        >>> l.amount
        5000.0
        >>> l.payee
        >>> l.memo
        'PRIVATE ÜBERWEISUNG,TA-Nr.: 554466111'
        >>> l.date
        datetime.datetime(2013, 1, 12, 0, 0)
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

