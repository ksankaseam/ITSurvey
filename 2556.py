import plotly.plotly as py
from plotly.graph_objs import *

def create_plot():
 """Build Graph in year 2556"""
 #The graph shows percentage of Establishments by Form of Legal Organization
 py.sign_in('memiine2', 'zi5WaKnR3sQ3qJnY63XT')
 trace1 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['81.3', '83.4', '74.6', '74.9', '5.1'],
    hoverinfo='y+name',
    name='Individual proprietor ',
    uid='1ddf4b',
    xsrc='memiine:40:b52779',
    ysrc='memiine:40:15fb1d'
 )
 trace2 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['4.6', '2.6', '11', '3.5', '4.4'],
    hoverinfo='y+name',
    name=' Juristic partnership ',
    uid='aedcbe',
    xsrc='memiine:40:b52779',
    ysrc='memiine:40:b08e1e'
 )
 trace3 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['10.2', '6.6', '13.2', '20.1', '82.4'],
    hoverinfo='y+name',
    name='Company limited, Public company limited',
    uid='6abcd1',
    xsrc='memiine:40:b52779',
    ysrc='memiine:40:cf96b9'
 )
 trace4 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['3.9', '7.4', '1.2', '1.5', '8.2'],
    hoverinfo='y+name',
    name='other',
    uid='8b247a',
    xsrc='memiine:40:b52779',
    ysrc='memiine:40:acaa1e'
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
        range=[0, 87.78947368421053],
        title='percent',
        type='linear'
    )
 )
 fig = Figure(data=data, layout=layout)
 plot_url = py.plot(fig)

 #The graph shows Percentage of Establishments by Internet use
 py.sign_in('memiine2', 'zi5WaKnR3sQ3qJnY63XT')
 trace1 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['20.7', '10.1', '23.4', '15.6', '95.3'],
    hoverinfo='y+name',
    name='Use of the internet',
    uid='fbb0b6',
    xsrc='memiine:44:990f7c',
    ysrc='memiine:44:d1b7a2'
 )
 trace2 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['79.3', '89.9', '76.6', '84.4', '4.7'],
    hoverinfo='y+name',
    name='No use of the internet',
    uid='52a454',
    xsrc='memiine:44:990f7c',
    ysrc='memiine:44:b5677f'
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
        range=[0, 100.3157894736842],
        title='percent',
        type='linear'
    )
 )
 fig = Figure(data=data, layout=layout)
 plot_url = py.plot(fig)

 #the graph shows Percentage of Establishments  use of Internet by Type of External connection to the internet access
 py.sign_in('memiine2', 'zi5WaKnR3sQ3qJnY63XT')
 trace1 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['16.7', '16.2', '18.1', '15.6', '13.4'],
    hoverinfo='y+name',
    name='Dial line',
    uid='62eb6e',
    xsrc='memiine:48:36ba23',
    ysrc='memiine:48:7d45e4'
 )
 trace2 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['12.6', '11.2', '12.2', '4.3', '18.7'],
    hoverinfo='y+name',
    name='ISDN',
    uid='f57055',
    xsrc='memiine:48:36ba23',
    ysrc='memiine:48:822787'
 )
 trace3 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['47.7', '51.2', '52', '61.5', '68.5'],
    hoverinfo='y+name',
    name='xDSL',
    uid='a9cf08',
    xsrc='memiine:48:36ba23',
    ysrc='memiine:48:6913e0'
 )
 trace4 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['5.9', '8.4', '4.2', '4.9', '24.5'],
    hoverinfo='y+name',
    name='Leased Line',
    uid='64ffd4',
    xsrc='memiine:48:36ba23',
    ysrc='memiine:48:fc0d3c'
 )
 trace5 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['3.5', '5.4', '4.1', '3.3', '9.4'],
    hoverinfo='y+name',
    name='Cable modem',
    uid='2f2b95',
    xsrc='memiine:48:36ba23',
    ysrc='memiine:48:09af7d'
 )
 trace6 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['0.7', '1.2', '0.4', '2.7', '11.3'],
    hoverinfo='y+name',
    name='Other fixed connection',
    uid='08be9f',
    xsrc='memiine:48:36ba23',
    ysrc='memiine:48:b958e7'
 )
 trace7 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['18', '14.6', '21.8', '13.4', '30.2'],
    hoverinfo='y+name',
    name='Wireless connection',
    uid='5e01e4',
    xsrc='memiine:48:36ba23',
    ysrc='memiine:48:a95b52'
 )
 trace8 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['8.8', '9.2', '6.8', '4.2', '22.7'],
    hoverinfo='y+name',
    name='Mobile phone ',
    uid='d80c5f',
    xsrc='memiine:48:36ba23',
    ysrc='memiine:48:9702ba'
 )
 data = Data([trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8])
 layout = Layout(
    autosize=True,
    hovermode='closest',
    showlegend=True,
    title='Percentage of Establishments &nbsp;use of &nbsp;Internet <br>by Type of External connection to the internet access , Economic Activity , Size of Establishment and Region',
    xaxis=XAxis(
        autorange=True,
        range=[-0.5, 4.5],
        title='',
        type='category'
    ),
    yaxis=YAxis(
        autorange=True,
        range=[0, 72.10526315789474],
        title='percent',
        type='linear'
    )
 )
 fig = Figure(data=data, layout=layout)
 plot_url = py.plot(fig)

 #the graph shows Percentage of Establishments by Use of Web site and Category of Industry 
 py.sign_in('memiine2', 'zi5WaKnR3sQ3qJnY63XT')
 trace1 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['78.1', '81.2', '81.9', '91.2', '87.8'],
    hoverinfo='y+name',
    name='Own Web site ',
    uid='11061a',
    xsrc='memiine:50:6d8e8d',
    ysrc='memiine:50:f03013'
 )
 trace2 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['20.9', '17.4', '16.1', '8.8', '9.6'],
    hoverinfo='y+name',
    name='Other Web portal ',
    uid='2bd5dc',
    xsrc='memiine:50:6d8e8d',
    ysrc='memiine:50:15b943'
 )
 trace3 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['1', '1.5', '2', '', '2.6'],
    hoverinfo='y+name',
    name='Own Web site  Other Web portal ',
    uid='ec5e4d',
    xsrc='memiine:50:6d8e8d',
    ysrc='memiine:50:b539ff'
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
        range=[0, 96],
        title='percent',
        type='linear'
    )
 )
 fig = Figure(data=data, layout=layout)
 plot_url = py.plot(fig)

 #the graph shows Personnel in enterprise who have graduated in the field of ICT by level of education
 py.sign_in('memiine2', 'zi5WaKnR3sQ3qJnY63XT')
 trace1 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['5.40', '6.90', '3.20', '13.40', '1.20'],
    hoverinfo='y+name',
    name='Lower than Vocationl',
    uid='913d15',
    xsrc='memiine:52:f6923b',
    ysrc='memiine:52:ff2ecb'
 )
 trace2 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['21.50', '21.90', '19.60', '23.60', '13.30'],
    hoverinfo='y+name',
    name='Vocational',
    uid='612297',
    xsrc='memiine:52:f6923b',
    ysrc='memiine:52:588486'
 )
 trace3 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['66.60', '65.50', '73.30', '58.80', '78.00'],
    hoverinfo='y+name',
    name='Bachelor ',
    uid='2b2718',
    xsrc='memiine:52:f6923b',
    ysrc='memiine:52:868401'
 )
 trace4 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['6.50', '5.70', '3.90', '4.20', '7.50'],
    hoverinfo='y+name',
    name='Higher than Bachelor ',
    uid='ecb7e4',
    xsrc='memiine:52:f6923b',
    ysrc='memiine:52:678dda'
 )
 data = Data([trace1, trace2, trace3, trace4])
 layout = Layout(
    autosize=True,
    hovermode='closest',
    showlegend=True,
    title='&nbsp;Number of &nbsp;Personnel in enterprise who have graduated in the field of &nbsp;ICT &nbsp;<br>by &nbsp;&nbsp;level &nbsp;of &nbsp;education , Economic Activity , Size of Establishment and Region&nbsp;',
    xaxis=XAxis(
        autorange=True,
        range=[-0.5, 4.5],
        title='',
        type='category'
    ),
    yaxis=YAxis(
        autorange=True,
        range=[0, 82.10526315789474],
        title='percent',
        type='linear'
    )
 )
 fig = Figure(data=data, layout=layout)
 plot_url = py.plot(fig)
 create_plot()
