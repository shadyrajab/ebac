import pandas as pd
import matplotlib.pyplot as plt
import os 
import sys

data = pd.read_csv('./SINASC_RO_2019.csv')

def analise_mensal(data, key, month, values, func, ylabel, xlabel):
  data[key] = pd.to_datetime(data[key])
  match month.upper():
    case 'JAN':
      month = 'January'
    case 'FER':
      month = 'February'
    case 'MAR':
      month = 'March'
    case 'ABR':
      month = 'April'
    case 'MAI':
      month = 'May'
    case 'JUN':
      month = 'June'
    case 'JUL':
      month = 'July'
    case 'AGO':
      month = 'August'
    case 'SET':
      month = 'September'
    case 'OUT':
      month = 'October'
    case 'NOV':
      month = 'November'
    case 'DEZ':
      month = 'December'

  os.makedirs(f'./ouput/{month}', exist_ok=True)

  mensal = data[data[key].dt.strftime('%B') == month]
  ax = pd.pivot_table(mensal, values=values, index=key, aggfunc=func).plot(figsize=[15,5])
  plt.ylabel(ylabel)
  plt.xlabel(xlabel)
  plt.savefig(f'./ouput/{month}/media_idade.png')
  mensal.to_csv(f'./ouput/{month}/analise.csv', index=False)
  return mensal, ax

sys.argv.pop(0)

for arg in sys.argv:
  analise_mensal(data, 'DTNASC', arg, ['IDADEMAE'], 'mean', 'Idade média das mães', 'Data de nascimento')