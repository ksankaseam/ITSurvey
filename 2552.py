import plotly.plotly as py
from plotly.graph_objs import *

def create_plot():
 """Build All Graph in year 2552"""

 #The graph shows percentage of Establishments by Form of Legal Organization
 py.sign_in('memiine', 'Gw463qUTJMpKC8aUVebo')
 trace1 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['10.92', '1.89', '1.70', '0.77', '0.00'],
    hoverinfo='y+name',
    name='Lower than Vocationl',
    uid='2cb1c9',
    xsrc='memiine:11:34c0ff',
    ysrc='memiine:11:775dea'
 )
 trace2 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['8.40', '15.66', '21.25', '9.72', '7.86'],
    hoverinfo='y+name',
    name='Vocational',
    uid='00e139',
    xsrc='memiine:11:34c0ff',
    ysrc='memiine:11:1d3633'
 )
 trace3 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['71.31', '72.56', '72.91', '85.17', '86.49'],
    hoverinfo='y+name',
    name='Bachelor ',
    uid='91dd02',
    xsrc='memiine:11:34c0ff',
    ysrc='memiine:11:772557'
 )
 trace4 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['9.36', '9.89', '4.14', '4.35', '5.65'],
    hoverinfo='y+name',
    name='Higher than Bachelor ',
    uid='eb092d',
    xsrc='memiine:11:34c0ff',
    ysrc='memiine:11:d14d12'
 )
 data = Data([trace1, trace2, trace3, trace4])
 layout = Layout(
    autosize=True,
    hovermode='closest',
    showlegend=True,
    title='&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Number of Personnel in enterprise who have graduated in the field of ICT <br>by level of education , Economic Activity , Size of Establishment and Region',
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

 #The graph shows Percentage of Establishments by Internet use
 py.sign_in('memiine', 'Gw463qUTJMpKC8aUVebo')
 trace1 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['17.1', '9.3', '31.3', '16.6', '95.5'],
    hoverinfo='y+name',
    name='Use of the internet',
    uid='10df3a',
    xsrc='memiine:4:196d2d',
    ysrc='memiine:4:ab104f'
 )
 trace2 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['82.9', '90.7', '68.7', '83.4', '4.5'],
    hoverinfo='y+name',
    name='No use of the internet',
    uid='6813c9',
    xsrc='memiine:4:196d2d',
    ysrc='memiine:4:3a5555'
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
        title='<br>',
        type='category'
    ),
    yaxis=YAxis(
        autorange=True,
        range=[0, 100.52631578947368],
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
    y=['25.8', '24.1', '33.3', '22.5', '11.1'],
    hoverinfo='y+name',
    name='Dial line',
    uid='6bd463',
    xsrc='memiine:8:9ce246',
    ysrc='memiine:8:301013'
 )
 trace2 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['7', '7.3', '9.2', '4.7', '3.9'],
    hoverinfo='y+name',
    name='ISDN',
    uid='c52bba',
    xsrc='memiine:8:9ce246',
    ysrc='memiine:8:61c988'
 )
 trace3 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['60', '61.9', '49.3', '61.9', '82.1'],
    hoverinfo='y+name',
    name='xDSL',
    uid='37b6f3',
    xsrc='memiine:8:9ce246',
    ysrc='memiine:8:34cb52'
 )
 trace4 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['4.6', '9.3', '7.5', '3.7', '16.9'],
    hoverinfo='y+name',
    name='Leased Line',
    uid='c91460',
    xsrc='memiine:8:9ce246',
    ysrc='memiine:8:bf6b62'
 )
 trace5 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['4.7', '3.3', '4.3', '6.7', '6.6'],
    hoverinfo='y+name',
    name='Cable modem',
    uid='b21394',
    xsrc='memiine:8:9ce246',
    ysrc='memiine:8:2bbd12'
 )
 trace6 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['2.8', '0.9', '2', '2.9', '3.1'],
    hoverinfo='y+name',
    name='Other fixed connection',
    uid='455f68',
    xsrc='memiine:8:9ce246',
    ysrc='memiine:8:4e085a'
 )
 trace7 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['6', '4.4', '5.8', '4.1', '4'],
    hoverinfo='y+name',
    name='Wireless connection',
    uid='b7ba7b',
    xsrc='memiine:8:9ce246',
    ysrc='memiine:8:2c7600'
 )
 data = Data([trace1, trace2, trace3, trace4, trace5, trace6, trace7])
 layout = Layout(
    autosize=True,
    hovermode='closest',
    showlegend=True,
    title='Percentage of Establishments &nbsp;use of &nbsp;Internet <br>by Type &nbsp;of Communication Network , Economic Activity , Size of Establishment and Region&nbsp;',
    xaxis=XAxis(
        autorange=True,
        range=[-0.5, 4.5],
        title='',
        type='category'
    ),
    yaxis=YAxis(
        autorange=True,
        range=[0, 86.42105263157895],
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
    uid='124522',
    xsrc='memiine:9:d67dfe',
    ysrc='memiine:9:b1b444'
 )
 trace2 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['2.1', '1.5', '2.3', '1.3', '28.1'],
    hoverinfo='y+name',
    name='Other Web portal ',
    uid='e242d0',
    xsrc='memiine:9:d67dfe',
    ysrc='memiine:9:5e9d5d'
 )
 trace3 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['92.3', '95.7', '92.6', '92.4', '34.5'],
    hoverinfo='y+name',
    name='no Web site',
    uid='01de3b',
    xsrc='memiine:9:d67dfe',
    ysrc='memiine:9:e14644'
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
    uid='2cb1c9',
    xsrc='memiine:11:34c0ff',
    ysrc='memiine:11:775dea'
 )
 trace2 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['8.40', '15.66', '21.25', '9.72', '7.86'],
    hoverinfo='y+name',
    name='Vocational',
    uid='00e139',
    xsrc='memiine:11:34c0ff',
    ysrc='memiine:11:1d3633'
 )
 trace3 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['71.31', '72.56', '72.91', '85.17', '86.49'],
    hoverinfo='y+name',
    name='Bachelor ',
    uid='91dd02',
    xsrc='memiine:11:34c0ff',
    ysrc='memiine:11:772557'
 )
 trace4 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['9.36', '9.89', '4.14', '4.35', '5.65'],
    hoverinfo='y+name',
    name='Higher than Bachelor ',
    uid='eb092d',
    xsrc='memiine:11:34c0ff',
    ysrc='memiine:11:d14d12'
 )
 data = Data([trace1, trace2, trace3, trace4])
 layout = Layout(
    autosize=True,
    hovermode='closest',
    showlegend=True,
    title='&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Number of Personnel in enterprise who have graduated in the field of ICT <br>by level of education , Economic Activity , Size of Establishment and Region',
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
