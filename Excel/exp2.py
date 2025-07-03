from openpyxl import Workbook

wb = Workbook()
sheet = wb.active
sheet.title = "UserData"

sheet.append(["Name", "Email", "Password"])
sheet.append(["Alice", "alice@test.com", "pass123"])
sheet.append(["Bob", "bob@test.com", "secure456"])

wb.save(r"C:\Users\Arcknight\Desktop\HCL_Testing_Training\Coding\Excel\data.xlsx")
print("data.xlsx created.")
