#!/usr/bin/env python3
# Plots the indoor and outdoor temps
# Based pm: https://github.com/googleworkspace/python-samples/tree/master/sheets/quickstart
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START sheets_quickstart]
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import time, sys

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '194-6E4KGiKREfnmcSQmCroe3n_E5PvAD2LBzfRVB64I'
SAMPLE_RANGE_NAME = 'A2'

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            # creds = flow.run_local_server(port=0)
            creds = flow.run_console()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    
    import socket
    import sys
    import struct
    import time

    import re

    # print ("Opening socket")
    sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # print ("binding...")
    sock.bind(('', 9999))
    # print ("Setting opt")
    sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_MULTICAST_LOOP, True)
    mreq = struct.pack("16s15s".encode('utf-8'), socket.inet_pton(socket.AF_INET6, "ff02::1"), (chr(0) * 16).encode('utf-8'))
    # print ("JOIN_GROUP")
    sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_JOIN_GROUP, mreq)

    firstTime = True
    print("Starting...")
    while True:
        # output Nan if frst time to graphs will be disconnected.
        if firstTime:
            firstTime = False
            values = [ [time.time()/60/60/24+ 25569 - 5/24, "NaN", "NaN", "NaN"]]
            body = {'values': values}
            result = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                        range=SAMPLE_RANGE_NAME,
                                        valueInputOption='USER_ENTERED', 
                                        body=body
                                        ).execute()
    
        while True:
          # print ("Waiting for sensor")
          data, sender = sock.recvfrom(1024)
          # print (str(sender) + '  ' + repr(data))
          # print(data)
          # print(str(data))

          # Check for brightness
          r1 = re.findall(r"l:([\d\.]+)", str(data))
          if len(r1) > 0:
            lux = float(r1[0])
            # print(float(lux))

          # Check for humidity
          r1 = re.findall(r"h:([\d\.]+)", str(data))
          if len(r1) > 0:
            hum = float(r1[0])
            # print(float(hum))

          # Check for temp
          r1 = re.findall(r"t:([\d\.]+)", str(data))
          if len(r1) > 0:
            temp = float(r1[0])*9/5+32
            # print(float(temp))

            values = [ [time.time()/60/60/24+ 25569 - 5/24, lux, hum, temp]]
            # print(values)
            body = {'values': values}
            result = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME,
                                    valueInputOption='USER_ENTERED', 
                                    body=body
                                    ).execute()
           #  print(result)

						# Delete one row for very row added
            # https://developers.google.com/sheets/api/samples/rowcolumn#delete_rows_or_columns
            body = {'requests': [
              {
                "deleteDimension": {
									"range": {
										"dimension": "ROWS",
										"startIndex": 3,
										"endIndex": 4
									}
								}
							}
						]}
            result = sheet.batchUpdate(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    body=body
                                    ).execute()
            # print(result)

if __name__ == '__main__':
    main()
# [END sheets_quickstart]
