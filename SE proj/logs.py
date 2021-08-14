import xlsxwriter


address = ""
def getAddress():
    address=input("")

# Workbook() takes one, non-optional, argument
# which is the filename that we want to create.

workbook = xlsxwriter.Workbook(address+'hello.xlsx')
# The workbook object is then used to add new
# worksheet via the add_worksheet() method.
worksheet = workbook.add_worksheet()

# Use the worksheet object to write
# data via the write() method.
worksheet.write('A1', 'TIME')
worksheet.write('B1', 'CAM NO.')
worksheet.write('C1', 'CAM NAME')
worksheet.write('D1', 'OBJECT TYPE')
worksheet.write('E1', 'ALERT SMS')
worksheet.write('F1', 'SMS NO.')

# Finally, close the Excel file
# via the close() method.
workbook.close()


def call():
    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)

    client.calls.create(
        url='http://demo.twilio.com/docs/voice.xml',
        to='+9177371xxxxx',
        from_='+1917791xxxx'
    )