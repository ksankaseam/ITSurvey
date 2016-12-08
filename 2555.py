import plotly.plotly as py
from plotly.graph_objs import *

def create_plot():
 """Build Graph in year 2555"""

 #The graph shows percentage of Establishments by Form of Legal Organization
 py.sign_in('memiine', 'Gw463qUTJMpKC8aUVebo')
 trace1 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['76.8', '74.7', '68.6', '72.9', '13.6'],
    hoverinfo='y+name',
    name='Individual proprietor ',
    uid='3186df',
    xsrc='memiine:26:a9db5b',
    ysrc='memiine:26:100e63'
 )
 trace2 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['5', '3.3', '14.7', '8.1', '6.9'],
    hoverinfo='y+name',
    name=' Juristic partnership ',
    uid='d0ca92',
    xsrc='memiine:26:a9db5b',
    ysrc='memiine:26:1540ba'
 )
 trace3 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['12.9', '8.9', '15.5', '18.7', '73.1'],
    hoverinfo='y+name',
    name='Company limited, Public company limited',
    uid='39368b',
    xsrc='memiine:26:a9db5b',
    ysrc='memiine:26:ec83cf'
 )
 trace4 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['5.4', '13.1', '1.2', '0.3', '6.4'],
    hoverinfo='y+name',
    name='other',
    uid='9a5804',
    xsrc='memiine:26:a9db5b',
    ysrc='memiine:26:9ab6ea'
 )
 data = Data([trace1, trace2, trace3, trace4])
 layout = Layout(
    autosize=True,
    hovermode='closest',
    showlegend=True,
    title='Number and Percentage of Establishments <br>by Form of Legal Organization , Economic Activity , Size of Establishment and Region',
    xaxis=XAxis(
        autorange=True,
        range=[-0.5, 4.5],
        title='',
        type='category'
    ),
    yaxis=YAxis(
        autorange=True,
        range=[0, 80.84210526315789],
        title='percent',
        type='linear'
    )
 )
 fig = Figure(data=data, layout=layout)
 plot_url = py.plot(fig)

 #The graph shows Percentage of Establishments by Internet use
 py.sign_in('memiine', 'Gw463qUTJMpKC8aUVebo')
 trace1 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['20.4', '11.8', '74.3', '12.6', '85.5'],
    hoverinfo='y+name',
    name='Use of the internet',
    uid='490bd0',
    xsrc='memiine:30:19790e',
    ysrc='memiine:30:508cd6'
 )
 trace2 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['79.4', '88.2', '25.7', '87.4', '13.5'],
    hoverinfo='y+name',
    name='No use of the internet',
    uid='cc3866',
    xsrc='memiine:30:19790e',
    ysrc='memiine:30:b163f4'
 )
 data = Data([trace1, trace2])
 layout = Layout(
    autosize=True,
    hovermode='closest',
    showlegend=True,
    title='&nbsp;Number and Percentage of Establishments <br>by &nbsp;Internet use , Economic Activity , Size of Establishment and Region',
    xaxis=XAxis(
        autorange=True,
        range=[-0.5, 4.5],
        title='',
        type='category'
    ),
    yaxis=YAxis(
        autorange=True,
        range=[0, 92.84210526315789],
        title='percent',
        type='linear'
    )
 )
 fig = Figure(data=data, layout=layout)
 plot_url = py.plot(fig)

 #the graph shows Percentage of Establishments  use of Internet by Type of External connection to the internet access
 py.sign_in('memiine', 'Gw463qUTJMpKC8aUVebo')
 trace1 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['12.7', '12', '17.1', '5.4', '8'],
    hoverinfo='y+name',
    name='dial up',
    uid='aa3ad5',
    xsrc='memiine:34:61920a',
    ysrc='memiine:34:03486b'
 )
 trace2 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['14', '9.1', '13.5', '25.1', '15.4'],
    hoverinfo='y+name',
    name='ISDN ',
    uid='b0380b',
    xsrc='memiine:34:61920a',
    ysrc='memiine:34:0a24f8'
 )
 trace3 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['3.3', '9.3', '3.5', '5.4', '20'],
    hoverinfo='y+name',
    name='Leased Line ',
    uid='d34d0a',
    xsrc='memiine:34:61920a',
    ysrc='memiine:34:4fd221'
 )
 trace4 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['3.8', '4', '5.2', '1.7', '4.3'],
    hoverinfo='y+name',
    name='Cable Modem ',
    uid='3bed57',
    xsrc='memiine:34:61920a',
    ysrc='memiine:34:7cdebe'
 )
 trace5 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['0.4', '1', '0.5', '7.4', '6.4'],
    hoverinfo='y+name',
    name='Other  Fixed ',
    uid='067e68',
    xsrc='memiine:34:61920a',
    ysrc='memiine:34:e47730'
 )
 trace6 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['14.6', '10.9', '14.8', '10.6', '21.6'],
    hoverinfo='y+name',
    name='Wireless connection',
    uid='58ca6a',
    xsrc='memiine:34:61920a',
    ysrc='memiine:34:df80a1'
 )
 trace7 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['6.8', '9.3', '8.9', '4.7', '7.7'],
    hoverinfo='y+name',
    name='Mobile phone ',
    uid='4f390e',
    xsrc='memiine:34:61920a',
    ysrc='memiine:34:d94f76'
 )
 data = Data([trace1, trace2, trace3, trace4, trace5, trace6, trace7])
 layout = Layout(
    autosize=True,
    hovermode='closest',
    showlegend=True,
    title='Percentage of Establishments &nbsp;use of &nbsp;Internet <br>by Type of External connection to the internet access , Economic Activity ,<br> Size of Establishment and Region',
    xaxis=XAxis(
        autorange=True,
        range=[-0.5, 4.5],
        title='',
        type='category'
    ),
    yaxis=YAxis(
        autorange=True,
        range=[0, 26.42105263157895],
        title='percent',
        type='linear'
    )
 )
 fig = Figure(data=data, layout=layout)
 plot_url = py.plot(fig)

 #the graph shows Percentage of Establishments by Use of Web site and Category of Industry 
 py.sign_in('memiine', 'Gw463qUTJMpKC8aUVebo')
 trace1 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['5.6', '2.8', '5.1', '6.3', '37.4'],
    hoverinfo='y+name',
    name='Own Web site ',
    uid='0e05a0',
    xsrc='memiine:36:95e12d',
    ysrc='memiine:36:86f9ef'
 )
 trace2 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['2.1', '1.5', '2.3', '1.3', '28.1'],
    hoverinfo='y+name',
    name='Other Web portal ',
    uid='5137ab',
    xsrc='memiine:36:95e12d',
    ysrc='memiine:36:c78271'
 )
 trace3 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['92.3', '95.7', '92.6', '92.4', '34.5'],
    hoverinfo='y+name',
    name='no Web site',
    uid='9384f4',
    xsrc='memiine:36:95e12d',
    ysrc='memiine:36:809711'
 )
 data = Data([trace1, trace2, trace3])
 layout = Layout(
    autosize=True,
    hovermode='closest',
    showlegend=True,
    title='&nbsp;Number and Percentage of Establishments <br>by Use of Web site &nbsp;and Category of &nbsp;Industry&nbsp;',
    xaxis=XAxis(
        autorange=True,
        range=[-0.5, 4.5],
        title='',
        type='category'
    ),
    yaxis=YAxis(
        autorange=True,
        range=[0, 100.73684210526316],
        title='percent',
        type='linear'
    )
 )
 fig = Figure(data=data, layout=layout)
 plot_url = py.plot(fig)

 #the graph shows Personnel in enterprise who have graduated in the field of ICT by level of education
 py.sign_in('memiine', 'Gw463qUTJMpKC8aUVebo')
 trace1 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['10.92', '1.89', '1.70', '0.77', '0.00'],
    hoverinfo='y+name',
    name='Lower than Vocationl',
    uid='149b32',
    xsrc='memiine:38:25fb31',
    ysrc='memiine:38:91fcf2'
 )
 trace2 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['8.40', '15.66', '21.25', '9.72', '7.86'],
    hoverinfo='y+name',
    name='Vocational',
    uid='26b725',
    xsrc='memiine:38:25fb31',
    ysrc='memiine:38:589fb7'
 )
 trace3 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['71.31', '72.56', '72.91', '85.17', '86.49'],
    hoverinfo='y+name',
    name='Bachelor ',
    uid='e1a60b',
    xsrc='memiine:38:25fb31',
    ysrc='memiine:38:d13cdf'
 )
 trace4 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['9.36', '9.89', '4.14', '4.35', '5.65'],
    hoverinfo='y+name',
    name='Higher than Bachelor ',
    uid='781bf5',
    xsrc='memiine:38:25fb31',
    ysrc='memiine:38:503ea2'
 )
 data = Data([trace1, trace2, trace3, trace4])
 layout = Layout(
    autosize=True,
    hovermode='closest',
    showlegend=True,
    title='Number of &nbsp;Personnel in enterprise who have graduated in the field of &nbsp;ICT &nbsp;<br>by &nbsp;&nbsp;level &nbsp;of &nbsp;education , Economic Activity , Size of Establishment and Region&nbsp;',
    xaxis=XAxis(
        autorange=True,
        range=[-0.5, 4.5],
        title='',
        type='category'
    ),
    yaxis=YAxis(
        autorange=True,
        range=[0, 91.0421052631579],
        title='percent',
        type='linear'
    )
 )
 fig = Figure(data=data, layout=layout)
 plot_url = py.plot(fig)
create_plot()
