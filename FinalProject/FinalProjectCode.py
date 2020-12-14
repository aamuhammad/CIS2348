import csv
from datetime import date

ManufacturerDictionary = {}


class Inventory:
    def __init__(self, Manufacturer='none', ItemType='none'):
        self.Manufacturer = Manufacturer
        self.ItemType = ItemType

    def ManList(self):
        with open('ManufacturerList.csv', 'r') as ManList:
            Brand = csv.reader(ManList)
            for Manufacturer in Brand:
                ManufacturerDictionary[Manufacturer[0], Manufacturer[1], Manufacturer[2], Manufacturer[3]]
            return ManufacturerDictionary

    def PriceList(self):
        PriceDictionary = {}
        with open('PriceList.csv', 'r') as PriceList:
            Price = csv.reader(PriceList)
            for ItemPrice in Price:
                PriceDictionary[ItemPrice[0]] = [ItemPrice[1]]
            for Item in ManufacturerDictionary:
                if Item in PriceDictionary:
                    ManufacturerDictionary[Item] += PriceDictionary[Item]
            return ManufacturerDictionary

    def ServiceDateList(self):
        DatesDictionary = {}
        with open('ServiceDatesList.csv', 'r') as ServDate:
            Dates = csv.reader(ServDate)
            for ItemDate in Dates:
                DatesDictionary[ItemDate[0]] = [ItemDate[1]]
            for Item in ManufacturerDictionary:
                if Item in DatesDictionary:
                    ManufacturerDictionary[Item] += DatesDictionary[Item]
            return ManufacturerDictionary

    def FullInventory(self):
        with open('FullInventory.csv', 'w') as OutputFile:
            Inventory = csv.writer(OutputFile)
            for ID, Info in sorted(ManufacturerDictionary.Items(), key=lambda x: x[1]):
                Inventory.writerow([ID, Info[0], Info[1], Info[3], Info[4], Info[2]])

    def LaptopInventory(self):
        with open('LaptopInventory.csv', 'w') as OutputFile:
            Laptop = csv.writer(OutputFile)
            for ID, Info in sorted(ManufacturerDictionary.Items(), key=lambda x: x[0]):
                if Info[1] == 'laptop':
                    Laptop.writerow([ID, Info[0], Info[3], Info[4], Info[2]])

    def PastServiceDate(self):
        CurrentDate = str(date.today())
        CurrentDate = CurrentDate.split('-')
        with open('PastServiceDateInventory.csv', 'w') as OutputFile:
            PastDate = csv.writer(OutputFile)
            for ID, Info in sorted(ManufacturerDictionary.Items()):
                PastDate = Info[4]
                PastDate = PastDate.split('/')
                if int(CurrentDate[0]) >= int(PastDate[2]):
                    if int(CurrentDate[1]) > int(PastDate[0]):
                        PastDate.writerow([ID, Info[0], Info[1], Info[3], Info[4], Info[2]])
                    elif int(CurrentDate[1]) == int(PastDate[0]):
                        if int(CurrentDate[2]) > int(PastDate[1]):
                            PastDate.writerow([ID, Info[0], Info[1], Info[3], Info[4], Info[2]])

    def DamagedInventory(self):
        with open('DamagedInventory.csv', 'w') as OutputFile:
            Damaged = csv.writer(OutputFile)
            for ID, Info in sorted(ManufacturerDictionary.Items()):
                if Info[2] == 'damaged':
                    Damaged.writerow([ID, Info[0], Info[1], Info[3], Info[4]])

    def FindInventory(self):
        x = 0
        while x != 'q':
            self.Item = input('Enter manufacturer and item type: ')
            self.Item = self.Item.split()
            ItemList = self.Item
            for ID, Info in ManufacturerDictionary.Items():
                if Info[2] != 'damaged':
                    if Info[0] in ItemList:
                        if Info[1] in ItemList:
                            print('Your item is:', ID, Info[0], Info[1], '$' + Info[3])
                            break
            else:
                print('No such item in inventory')
            for ID, Info in ManufacturerDictionary.Items():
                if Info[2] != 'damaged':
                    if Info[1] in ItemList and Info[0] not in ItemList:
                        print('You may also consider:', ID, Info[0], Info[1], '$' + Info[3])
            print()
            x = input('Type any key to continue or type q to quit\n')


Inventory()
Inventory.ManList()
Inventory.PriceList()
Inventory.ServiceDateList()
Inventory.FullInventory()
Inventory.LaptopInventory()
Inventory.PastServiceDate()
Inventory.DamagedInventory()
Inventory.FindInventory()
