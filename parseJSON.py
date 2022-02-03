#!/usr/bin/env python3
false=False
test = {
   "spreadsheetId":"194-6E4KGiKREfnmcSQmCroe3n_E5PvAD2LBzfRVB64I",
   "properties":{
      "title":"connectDemo",
      "locale":"en_US",
      "autoRecalc":"ON_CHANGE",
      "timeZone":"America/New_York",
      "defaultFormat":{
         "backgroundColor":{
            "red":1,
            "green":1,
            "blue":1
         },
         "padding":{
            "top":2,
            "right":3,
            "bottom":2,
            "left":3
         },
         "verticalAlignment":"BOTTOM",
         "wrapStrategy":"OVERFLOW_CELL",
         "textFormat":{
            "foregroundColor":{
               
            },
            "fontFamily":"arial,sans,sans-serif",
            "fontSize":10,
            "bold":false,
            "italic":false,
            "strikethrough":false,
            "underline":false,
            "foregroundColorStyle":{
               "rgbColor":{
                  
               }
            }
         },
         "backgroundColorStyle":{
            "rgbColor":{
               "red":1,
               "green":1,
               "blue":1
            }
         }
      },
      "spreadsheetTheme":{
         "primaryFontFamily":"Arial",
         "themeColors":[
            {
               "colorType":"TEXT",
               "color":{
                  "rgbColor":{
                     
                  }
               }
            },
            {
               "colorType":"BACKGROUND",
               "color":{
                  "rgbColor":{
                     "red":1,
                     "green":1,
                     "blue":1
                  }
               }
            },
            {
               "colorType":"ACCENT1",
               "color":{
                  "rgbColor":{
                     "red":0.25882354,
                     "green":0.52156866,
                     "blue":0.95686275
                  }
               }
            },
            {
               "colorType":"ACCENT2",
               "color":{
                  "rgbColor":{
                     "red":0.91764706,
                     "green":0.2627451,
                     "blue":0.20784314
                  }
               }
            },
            {
               "colorType":"ACCENT3",
               "color":{
                  "rgbColor":{
                     "red":0.9843137,
                     "green":0.7372549,
                     "blue":0.015686275
                  }
               }
            },
            {
               "colorType":"ACCENT4",
               "color":{
                  "rgbColor":{
                     "red":0.20392157,
                     "green":0.65882355,
                     "blue":0.3254902
                  }
               }
            },
            {
               "colorType":"ACCENT5",
               "color":{
                  "rgbColor":{
                     "red":1,
                     "green":0.42745098,
                     "blue":0.003921569
                  }
               }
            },
            {
               "colorType":"ACCENT6",
               "color":{
                  "rgbColor":{
                     "red":0.27450982,
                     "green":0.7411765,
                     "blue":0.7764706
                  }
               }
            },
            {
               "colorType":"LINK",
               "color":{
                  "rgbColor":{
                     "red":0.06666667,
                     "green":0.33333334,
                     "blue":0.8
                  }
               }
            }
         ]
      }
   },
   "sheets":[
      {
         "properties":{
            "sheetId":0,
            "title":"Sheet1",
            "index":0,
            "sheetType":"GRID",
            "gridProperties":{
               "rowCount":8604,
               "columnCount":26
            }
         },
         "charts":[
            {
               "chartId":1874215023,
               "spec":{
                  "title":"Lux, Humidity and Temperature",
                  "basicChart":{
                     "chartType":"LINE",
                     "axis":[
                        {
                           "position":"BOTTOM_AXIS",
                           "title":"Date",
                           "format":{
                              "fontFamily":"Roboto"
                           },
                           "viewWindowOptions":{
                              
                           }
                        },
                        {
                           "position":"LEFT_AXIS",
                           "title":"Humidity and Temperature",
                           "format":{
                              "fontFamily":"Roboto"
                           },
                           "viewWindowOptions":{
                              "viewWindowMin":20
                           }
                        },
                        {
                           "position":"RIGHT_AXIS",
                           "title":"Lux",
                           "format":{
                              "fontFamily":"Roboto"
                           },
                           "viewWindowOptions":{
                              
                           }
                        }
                     ],
                     "domains":[
                        {
                           "domain":{
                              "sourceRange":{
                                 "sources":[
                                    {
                                       "startRowIndex":0,
                                       "endRowIndex":8592,
                                       "startColumnIndex":0,
                                       "endColumnIndex":1
                                    }
                                 ]
                              }
                           }
                        }
                     ],
                     "series":[
                        {
                           "series":{
                              "sourceRange":{
                                 "sources":[
                                    {
                                       "startRowIndex":0,
                                       "endRowIndex":8592,
                                       "startColumnIndex":1,
                                       "endColumnIndex":2
                                    }
                                 ]
                              }
                           },
                           "targetAxis":"RIGHT_AXIS",
                           "dataLabel":{
                              "type":"NONE",
                              "textFormat":{
                                 "fontFamily":"Roboto"
                              }
                           }
                        },
                        {
                           "series":{
                              "sourceRange":{
                                 "sources":[
                                    {
                                       "startRowIndex":0,
                                       "endRowIndex":8592,
                                       "startColumnIndex":2,
                                       "endColumnIndex":3
                                    }
                                 ]
                              }
                           },
                           "targetAxis":"LEFT_AXIS",
                           "dataLabel":{
                              "type":"NONE",
                              "textFormat":{
                                 "fontFamily":"Roboto"
                              }
                           }
                        },
                        {
                           "series":{
                              "sourceRange":{
                                 "sources":[
                                    {
                                       "startRowIndex":0,
                                       "endRowIndex":8592,
                                       "startColumnIndex":3,
                                       "endColumnIndex":4
                                    }
                                 ]
                              }
                           },
                           "targetAxis":"LEFT_AXIS",
                           "dataLabel":{
                              "type":"NONE",
                              "textFormat":{
                                 "fontFamily":"Roboto"
                              }
                           }
                        }
                     ],
                     "headerCount":1
                  },
                  "hiddenDimensionStrategy":"SKIP_HIDDEN_ROWS_AND_COLUMNS",
                  "titleTextFormat":{
                     "fontFamily":"Roboto"
                  },
                  "fontName":"Roboto"
               },
               "position":{
                  "overlayPosition":{
                     "anchorCell":{
                        "rowIndex":2,
                        "columnIndex":4
                     },
                     "offsetXPixels":77,
                     "offsetYPixels":19,
                     "widthPixels":600,
                     "heightPixels":371
                  }
               }
            },
            {
               "chartId":1931721731,
               "spec":{
                  "title":"Lux, Humidity and Temperature",
                  "basicChart":{
                     "chartType":"LINE",
                     "axis":[
                        {
                           "position":"BOTTOM_AXIS",
                           "title":"Date",
                           "format":{
                              "fontFamily":"Roboto"
                           },
                           "viewWindowOptions":{
                              
                           }
                        },
                        {
                           "position":"LEFT_AXIS",
                           "viewWindowOptions":{
                              "viewWindowMin":30
                           }
                        },
                        {
                           "position":"RIGHT_AXIS",
                           "viewWindowOptions":{
                              
                           }
                        }
                     ],
                     "domains":[
                        {
                           "domain":{
                              "sourceRange":{
                                 "sources":[
                                    {
                                       "startRowIndex":0,
                                       "endRowIndex":3,
                                       "startColumnIndex":5,
                                       "endColumnIndex":6
                                    }
                                 ]
                              }
                           }
                        }
                     ],
                     "series":[
                        {
                           "series":{
                              "sourceRange":{
                                 "sources":[
                                    {
                                       "startRowIndex":0,
                                       "endRowIndex":3,
                                       "startColumnIndex":6,
                                       "endColumnIndex":7
                                    }
                                 ]
                              }
                           },
                           "targetAxis":"RIGHT_AXIS",
                           "dataLabel":{
                              "type":"NONE",
                              "textFormat":{
                                 "fontFamily":"Roboto"
                              }
                           },
                           "pointStyle":{
                              "size":7
                           }
                        },
                        {
                           "series":{
                              "sourceRange":{
                                 "sources":[
                                    {
                                       "startRowIndex":0,
                                       "endRowIndex":3,
                                       "startColumnIndex":7,
                                       "endColumnIndex":8
                                    }
                                 ]
                              }
                           },
                           "targetAxis":"LEFT_AXIS",
                           "dataLabel":{
                              "type":"DATA",
                              "textFormat":{
                                 "fontFamily":"Roboto"
                              }
                           },
                           "pointStyle":{
                              "size":7
                           }
                        },
                        {
                           "series":{
                              "sourceRange":{
                                 "sources":[
                                    {
                                       "startRowIndex":0,
                                       "endRowIndex":3,
                                       "startColumnIndex":8,
                                       "endColumnIndex":9
                                    }
                                 ]
                              }
                           },
                           "targetAxis":"LEFT_AXIS",
                           "dataLabel":{
                              "type":"NONE",
                              "textFormat":{
                                 "fontFamily":"Roboto"
                              }
                           }
                        }
                     ],
                     "headerCount":1
                  },
                  "hiddenDimensionStrategy":"SKIP_HIDDEN_ROWS_AND_COLUMNS",
                  "titleTextFormat":{
                     "fontFamily":"Roboto"
                  },
                  "fontName":"Roboto"
               },
               "position":{
                  "overlayPosition":{
                     "anchorCell":{
                        "rowIndex":6,
                        "columnIndex":4
                     },
                     "offsetXPixels":77,
                     "offsetYPixels":2,
                     "widthPixels":418,
                     "heightPixels":304
                  }
               }
            }
         ]
      }
   ],
   "spreadsheetUrl":"https://docs.google.com/spreadsheets/d/194-6E4KGiKREfnmcSQmCroe3n_E5PvAD2LBzfRVB64I/edit"
}

print(test.keys())
print(test['sheets'][0]['charts'][0]['chartId'])