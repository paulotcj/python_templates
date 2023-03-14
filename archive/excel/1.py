from openpyxl import load_workbook

class AppComponentsExcel:
    local_filename = ""
    workbook = None
    metadata_sheet_name = ""
    appComponent_metadata = []
    appComponent_data = []
    
    #---------------------------------------------------------
    def __init__(self, fileName):
        local_filename = fileName
        
        #Read file
        self.workbook = load_workbook(filename=local_filename)
        # Check sheetnames
        # sheetnames = workbook.sheetnames
        # print(sheetnames)

    #---------------------------------------------------------
    def ReadMetadata(self, sheetName):
        self.metadata_sheet_name = sheetName
        #Read metadata
        sheet = self.workbook[self.metadata_sheet_name]

        for row_data in sheet.iter_rows(values_only=True, min_row=2):
            dict_row = {
                "table" : row_data[0],
                "order" : row_data[1],
                "column" : row_data[2],
                "column_type" : row_data[3],
                "data_type" : row_data[4]
            }
            self.appComponent_metadata.append(dict_row)

        return self.appComponent_metadata

    #end of def ReadMetadata(self, sheetName):    

    #---------------------------------------------------------   
    def ReadData(self, sheetName):
        #Read Data
        sheet = self.workbook[sheetName]

        for row_data in sheet.iter_rows(values_only=True, min_row=2, max_col=23):
            count = 0
            new_row = []
            if row_data[0] == None:
                continue
            #----
            for col in row_data:
                dict_row = {
                    "table" : self.appComponent_metadata[count]["table"],
                    "column" : self.appComponent_metadata[count]["column"],
                    "value" : col,
                    "column_type" : self.appComponent_metadata[count]["column_type"],
                    "data_type" : self.appComponent_metadata[count]["data_type"]
                }
                new_row.append(dict_row)
                count += 1
            #----
            self.appComponent_data.append(new_row)
        # end of for row_data in sheet

        return self.appComponent_data
    #end of def ReadData(self, sheetName):
    
    #---------------------------------------------------------

#end of class AppComponentsExcel
#---------------------------------------------------------
          



class AppComponentsSQL:

    inserts = ""

    def Inserts(self, appComponent_metadata, appComponent_data):
        #----
        columns = ""
        for row in appComponent_data[0]:
            if row["column_type"] == "column":
                columns += f'{ row["column"]}, '
        columns = f'( { str(columns).removesuffix(", ") } )'

        #----
        insert_body = ""
        for row in appComponent_data:
            insert_body_row = ""
            for col in row:

                if col["column_type"] == "column":
                    value = ""

                    if col["value"] == None:
                        value = "NULL"
                    elif col["data_type"] == "string":
                        temp = str(col["value"]).replace("\n","")
                        value = f'\'{  temp  }\''
                    elif col["data_type"] == "bool":
                        value = str(col["value"]).upper()
                    else:
                        value = str(col["value"])

                    insert_body_row += f'{ value }, '
                # end of if col["column_type"] == "column":
            #end of for col in row:         
            insert_body += f'( { str(insert_body_row).removesuffix(", ") } ),\n'
        #end of for row in appComponent_data:
        insert_body = insert_body.removesuffix(",\n")

        #----
                    

        insert_header = f'INSERT INTO TABLE { appComponent_metadata[0]["table"] }\n{ columns }\nVALUES'
        self.inserts = f'{insert_header}\n{insert_body}\nON CONFLICT DO NOTHING;'

        print(self.inserts)
        # print("len of inserts:", len(inserts))
        # print("len of insert_body:", len(insert_body))

        return self.inserts

    #end of Inserts
    #---------------------------------------------------------

#end of AppComponentsSQL
#---------------------------------------------------------    


obj_excel = AppComponentsExcel('xxxxxxxxxxxxxxxxxxx')
obj_excel.ReadMetadata('AppComponents_metadata')
obj_excel.ReadData('Appcomponents_data')


dbscripts = AppComponentsSQL()


# -----------------------------------------------
#Build inserts
# inserts should allow conflict

dbscripts.Inserts(obj_excel.appComponent_metadata, obj_excel.appComponent_data)

# with open('appcomponent_inserts.sql', 'w') as file:
#     file.write(dbscripts.inserts)

# -----------------------------------------------
#Build updates
#  updates should be straight forward, and they are not supposed to fail



# -----------------------------------------------
#Build migrations


quit()
