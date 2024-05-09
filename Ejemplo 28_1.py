# pythonCopy code
from jinja2 import Template

template = Template(open('Ejercicio28_1.tex').read())
data = {'title': 'Informe de Ventas', 'sales': [1000, 1500, 2000]}

with open('sales_report.tex', 'w') as f:
    f.write(template.render(data))