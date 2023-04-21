import gspread

GSP_USER_KEY_PATH = "./gspread_user_key.json"
GSP_NAME = "kyle_gsp"
SHEET_NAME = "kyle_wks"

gsp = gspread.service_account(GSP_USER_KEY_PATH)
wks = gsp.open(GSP_NAME).worksheet(SHEET_NAME)
