from question8 import HashTable

#constructor
def test_initEmpty():
    testTable = HashTable()
    assert testTable.table == [[],[]]

def test_initItemCountIsZero():
    testTable = HashTable()
    assert testTable.itemCount == 0

#insert
def test_insertItem_itemCount():
    testTable = HashTable()
    testTable.insert("Don Draper", "555-5555")
    assert testTable.itemCount == 1

def test_updateItem_itemCount():
    testTable = HashTable()
    testTable.insert("Don Draper", "555-5556")
    assert testTable.itemCount == 1

def test_insertItem_notEmpty():
    testTable = HashTable()
    testTable.insert("Don Draper", "555-5555")
    assert testTable.table != [[],[]]

#delete
def test_deleteItem_itemCount():
    testTable = HashTable()
    testTable.insert("Don Draper", "555-5555")
    testTable.delete("Don Draper")
    assert testTable.itemCount == 0

def test_deleteItem_emptyTable():
    testTable = HashTable()
    testTable.insert("Don Draper", "555-5555")
    testTable.delete("Don Draper")
    assert testTable.table == [[]]

#search
def test_search():
    testTable = HashTable()
    testTable.insert("Romeo", "333-3333")
    testTable.insert("Juliet", "444-4444")
    testTable.insert("RobinHood", "555-5555")
    assert testTable.search("Juliet") == "444-4444"

#grow
def test_tableGrows():
    testTable = HashTable()
    assert len(testTable.table) == 2
    testTable.insert("Romeo", "333-3333")
    testTable.insert("Juliet", "444-4444")
    assert len(testTable.table) == 4
    testTable.insert("RobinHood", "555-5555")
    testTable.insert("Don Draper", "555-5555")
    assert len(testTable.table) == 8

#shrink
def test_tableShrinks():
    testTable = HashTable()
    testTable.insert("Romeo", "333-3333")
    testTable.insert("Juliet", "444-4444")
    testTable.insert("Robin Hood", "555-5555")
    testTable.insert("Don Draper", "555-5555")
    testTable.insert("Roger Sterling", "777-7777")
    assert len(testTable.table) == 8
    testTable.delete("Roger Sterling") #4 items, 8 lists. do nothing
    assert len(testTable.table) == 8
    testTable.delete("Don Draper")     #3 items, 8 lists, shrink to 4 lists
    assert len(testTable.table) == 4
