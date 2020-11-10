import unittest
import copy
from classAddress import Address as CA
from classCollection import CollectionAddress as CC
from classCollectionCaretaker import CollectionCaretaker
from programmingTask6 import *


class Tests(unittest.TestCase):

    def __test_collect():
        address1 = CA("Brodway", 45348, "opit", "uirute", "+380979085267", "+380939088267")
        address2 = CA("Kedrova", 22112, "UK", "London", "+380979488267", "+380973088267")
        address3 = CA("address", 12345, "Ukraine", "Lviv", "+380972088267", "+380975088267")
        address4 = CA("Addr", 54321, "Ukraine", "Kiev", "+380972088267", "+380979088467")
        address5 = CA("lomsd", 98766, "vcbx", "sdfs", "+380979080267", "+380979008267")
        address6 = CA("newAddress", 57564, "newCountry", "newCity", "+380979088967", "+380979089267")
        
        test_collect = CC()
        test_collect.insert(address1)
        test_collect.insert(address2)
        test_collect.insert(address3)
        test_collect.insert(address4)
        test_collect.insert(address5)
        test_collect.insert(address6)

        return test_collect

    def testWriteReadFile(self):
        test_collect = Tests.__test_collect()

        test_collect.writeJsonFile('testReadWrite.json')

        collect = CC()
        collect.readJsonFile('testReadWrite.json')
    
        self.assertEqual(collect, test_collect)

    def testSort(self):
        collect = CC()
        collect.readJsonFile('data.json')
        test_collect = copy.deepcopy(collect)

        for i in collect[0].getAttr():
            collect.sort(str(i))
            test_collect.bubbleSort(str(i))
            self.assertEqual(collect, test_collect)
        
        with self.assertRaises(AttributeError):
            collect.sort('attribute')
    
    def testSearch(self):
        collect = CC()
        collect.readJsonFile('data.json')

        searchResult = []

        # search 'Brodway'
        searchResult = collect.search('Brodway')
        self.assertEqual(len(searchResult), 1)           # only 1...
        self.assertEqual(searchResult[0], collect[0])

        # search uk
        searchResult = collect.search('uk')
        self.assertEqual(searchResult[0], collect[1])
        self.assertEqual(searchResult[1], collect[2])
        self.assertEqual(searchResult[2], collect[3])

        # search 'None' ...
        with self.assertRaises(AttributeError):
            collect.search('None')

    
    def testDelete(self):
        address1 = CA("Brodway", 45348, "opit", "uirute", "+380979085267", "+380939088267")
        address2 = CA("Kedrova", 22112, "UK", "London", "+380979488267", "+380973088267")
        address4 = CA("Addr", 54321, "Ukraine", "Kiev", "+380972088267", "+380979088467")
        address5 = CA("lomsd", 98766, "vcbx", "sdfs", "+380979080267", "+380979008267")
        address6 = CA("newAddress", 57564, "newCountry", "newCity", "+380979088967", "+380979089267")
        
        test_collect = CC()
        test_collect.insert(address1)
        test_collect.insert(address2)
        test_collect.insert(address4)
        test_collect.insert(address5)
        test_collect.insert(address6)

        collect = Tests.__test_collect()
        collect.deleteElem(2)

        self.assertEqual(collect, test_collect)


    def testAdd(self):
        collect = CC()
        arrSTR = ['newAddress', 'newCountry', 'newCity', '+380000000000', '+380000000000']
        arrINT = [11111]
        collect.addNewAddress(arrSTR, arrINT)

        newOBJ = CA('newAddress', 11111, 'newCountry', 'newCity', '+380000000000', '+380000000000')

        self.assertEqual(collect[0], newOBJ)


    def testEdite(self):
        newOBJ = CA('newAddress', 11111, 'newCountry', 'newCity', '+380000000000', '+380000000000')
        collect = CC()
        collect.insert(newOBJ)

        # address_line
        testOBJ = CA('editeAddress', 11111, 'newCountry', 'newCity', '+380000000000', '+380000000000')
        collect.editAddress(0, 'address_line', 'editeAddress')
        self.assertEqual(collect[0], testOBJ)

        # postal_code
        testOBJ = CA('editeAddress', 22222, 'newCountry', 'newCity', '+380000000000', '+380000000000')
        collect.editAddress(0, 'postal_code', 22222)
        self.assertEqual(collect[0], testOBJ)

        # country
        testOBJ = CA('editeAddress', 22222, 'editeCountry', 'newCity', '+380000000000', '+380000000000')
        collect.editAddress(0, 'country', 'editeCountry')
        self.assertEqual(collect[0], testOBJ)

        # city
        testOBJ = CA('editeAddress', 22222, 'editeCountry', 'editeCity', '+380000000000', '+380000000000')
        collect.editAddress(0, 'city', 'editeCity')
        self.assertEqual(collect[0], testOBJ)

        # fax_number
        testOBJ = CA('editeAddress', 22222, 'editeCountry', 'editeCity', '+380111111111', '+380000000000')
        collect.editAddress(0, 'fax_number', '+380111111111')
        self.assertEqual(collect[0], testOBJ)

        # phone_number
        testOBJ = CA('editeAddress', 22222, 'editeCountry', 'editeCity', '+380111111111', '+380111111111')
        collect.editAddress(0, 'phone_number', '+380111111111')
        self.assertEqual(collect[0], testOBJ)


    def testUndo(self):
        collect = Tests.__test_collect()
        test_collect = copy.deepcopy(collect)
        caretaker = CollectionCaretaker(collect)

        caretaker.backup()
        collect.deleteElem(0)
        collect.deleteElem(0)

        caretaker.undo()
        self.assertEqual(collect, test_collect)


    def testRedo(self):
        collect = Tests.__test_collect()
        caretaker = CollectionCaretaker(collect)

        caretaker.backup()
        collect.deleteElem(0)

        caretaker.backup()
        collect.deleteElem(0)
        test_collect = copy.deepcopy(collect)

        caretaker.backup()
        collect.deleteElem(0)

        caretaker.undo()
        caretaker.undo()
        caretaker.redo()
        self.assertEqual(collect, test_collect)


if __name__ == '__main__':
    unittest.main()
