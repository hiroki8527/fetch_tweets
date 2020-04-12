import sys
sys.path.append('../script')
import common

def test_parse_date_at_1923():
    date = "Sat Apr 11 19:23:46 +0000 2020"
    assert common.parse_date(date) == "19:23 PM - Apr 2020"

def test_parse_date_0126():
    date = "Sat Apr 11 1:26:46 +0000 1920"
    assert common.parse_date(date) == "1:26 AM - Apr 1920"

def test_parse_date_at_1159():
    date = "Sat Apr 11 11:59:00 +0000 1920"
    assert common.parse_date(date) == "11:59 AM - Apr 1920"

def test_parse_date_at_1200():
    date = "Sat Apr 11 12:00:00 +0000 1920"
    assert common.parse_date(date) == "12:00 PM - Apr 1920"

def test_parse_date_at_1201():
    date = "Sat Apr 11 12:01:00 +0000 1920"
    assert common.parse_date(date) == "12:01 PM - Apr 1920"

def test_parse_date6_with_null():
    date = ""
    assert common.parse_date(date) == None
