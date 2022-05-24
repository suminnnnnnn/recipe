
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
  return render(request, 'base.html', {})

def home(request):
  return HttpResponse('Home')

from openpyxl import load_workbook
def excel(request):
  cnt = request.GET.get('cnt')
  
  load_wb = load_workbook('data.xlsx', data_only=True)
        
  # 시트 이름으로 불러오기
  load_ws = load_wb['Sheet1']

  # 셀 주소로 값 출력
  # print(load_ws['A1'].value)

  # 일단 리스트에 담기
  all_values = []
  for row in load_ws.rows:
      row_value = []
      for cell in row:
          row_value.append(cell.value)
      all_values.append(row_value)
  print(all_values)
  return render(request, 'excel.html', {'data': all_values})

