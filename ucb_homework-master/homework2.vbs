'Range("A2:A70926").AdvancedFilter Action:=xlFilterCopy, CopyToRange:=Range("I2"), Unique:=True

'Dim data(), unique As Variant, r As Long
'data = ws.Range("A2").Value

'Set unique = CreateObject("Scripting.Dictionary")
'For r = 1 To UBound(data)
'    unique(data(r, 9)) = Empty
'Next r

'CopyMassTickers copies the values of Column 1 to Column 9
'Sub CopyMassTickers()
 '   Sheets("A").Columns(1).Copy Destination:=Sheets("A").Columns(9)
'End Sub

'
''UniqueValues deletes duplicate values in Column 9 and names the Column as "Ticker" per the homework
'Sub UniqueValues()
'
'Dim ws As Worksheet
'Dim uniqueRng As Range
'Dim myCol As Long
'
'myCol = 9
'Set ws = ActiveSheet
'
'Set uniqueRng = GetUniqueValues(ws, myCol)
'
'Range("I1").Value = "Ticker"
'
'End Sub
'
'
'Function GetUniqueValues(ws As Worksheet, col As Long) As Range
'Dim firstRow As Long
'
'With ws
'    .Columns(col).RemoveDuplicates Columns:=Array(1), Header:=xlNo
'
'    firstRow = 1
'    If IsEmpty(.Cells(1, col)) Then firstRow = .Cells(1, col).End(xlDown).Row
'
'    Set GetUniqueValues = Range(.Cells(firstRow, col), .Cells(.Rows.Count, col).End(xlUp))
'End With
'
'End Function
'
'
'Sub TickerCounter()
'
'dim endOfColumn as integer
'endOfColumn = Worksheets("A").Range("A:A").Cells.SpecialCells(xlCellTypeConstants).Count
'
'dim stockA, stockAA as integer
'stockA, stockAA = 0
'
'for i = 2 to endOfColumn
'  if Cells(i, 1).Value = "A" Then
'    stockA = stockA + Cells(i, 7).Value
'  elseif Cells(i, 1).Value = "AA" Then
'    stockAA = stockAA + Cells(i, 7).Value
'  else MsgBox("test")
'  next i
'end for
'
'Range("I2").Value = stockA
'Range("I3").Value = stockAA
'
'end sub
'
'
'
'
'ticker = cells(2, 1).value // "A"

Sub Stocks()
  For Each ws in Worksheets
    ws.Activate
    dim stockTicker as string
    dim tickerCount as double
    tickerCount = 0
    dim tickerTable as integer
    tickerTable = 2
    dim rowsCount as double
    rowsCount = Cells(rows.Count, 1).End(xlUp).Row
    Range("I1").Value = "Ticker"
    Range("J1").Value = "Total Stock Volume"
    for i = 2 to rowscount
      if Cells(i + 1, 1).Value <> Cells(i, 1).Value then
        stockTicker = Cells(i, 1).Value
        tickerCount = tickerCount + Cells(i, 7).Value
        Range("I" & tickerTable).Value = stockTicker
        Range("J" & tickerTable).Value = tickerCount
        tickerTable = tickerTable + 1
        tickerCount = 0
      else
        tickerCount = tickerCount + Cells(i, 3).Value
      end if
    next i
  next ws
end sub



