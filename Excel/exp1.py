from openpyxl import Workbook

wb = Workbook()
sheet = wb.active
sheet.title = "CityData"

sheet.append(["From", "To"])
sheet.append(["BOM", "MAA"])
sheet.append(["DEL", "CCU"])
sheet.append(["BLR", "HYD"])
sheet.append(["PNQ", "AMD"])
sheet.append(["JAI", "GOI"])

wb.save("cities.xlsx")
print("cities.xlsx created.")
