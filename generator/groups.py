from comtypes.client import CreateObject
import os
from datetime import datetime

name_raw = datetime.now()

project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
try:
    try:
        os.remove(os.path.join(project_dir, "old_groups.xlsx"))
    except:
        pass
    old_file = os.path.join(project_dir, "groups.xlsx")
    new_file = os.path.join(project_dir, "old_groups.xlsx")
    os.rename(old_file, new_file)
except:
    pass
xl = CreateObject("Excel.Application")
xl.Visible = 1
wb = xl.Workbooks.Add()
group_name = ("group " + str(name_raw)[:-7])
for i in range(10):
    xl.Range["A%s" % (i + 1)].Value[()] = "%s_%s" % (group_name, i)
wb.SaveAs(os.path.join(project_dir, "groups.xlsx"))
xl.Quit()


# def new_data_for_test():
#     project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
#     try:
#         try:
#             os.remove(os.path.join(project_dir, "old_groups.xlsx"))
#         except:
#             pass
#         old_file = os.path.join(project_dir, "groups.xlsx")
#         new_file = os.path.join(project_dir, "old_groups.xlsx")
#         os.rename(old_file, new_file)
#     except:
#         pass
#     xl = CreateObject("Excel.Application")
#     xl.Visible = 1
#     wb = xl.Workbooks.Add()
#     group_name = ("group " + str(name_raw)[:-7])
#     for i in range(10):
#         xl.Range["A%s" % (i + 1)].Value[()] = "%s_%s" % (group_name, i)
#     wb.SaveAs(os.path.join(project_dir, "groups.xlsx"))
#     xl.Quit()
