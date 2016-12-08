import plotly.plotly as py
from plotly.graph_objs import *

def create_plot():
 """Build graph in year 2558"""
 #The graph shows percentage of Establishments by Form of Legal Organization
 py.sign_in('memiine2', 'zi5WaKnR3sQ3qJnY63XT')
 trace1 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['65.6', '68.9', '23.1', '21.7', '3.4'],
    name='Individual proprietor ',
    uid='e12168',
    xsrc='latiez:38:2b307b',
    ysrc='latiez:38:61bb72'
 )
 trace2 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['6.6', '9.0', '11.2', '12.1', '-'],
    name='Juristic partnership ',
    uid='1981ec',
    xsrc='latiez:38:2b307b',
    ysrc='latiez:38:4b8936'
 )
 trace3 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['27.7', '22.0', '65.7', '66.2', '88.9'],
    name='Company limited, Public company limited',
    uid='bf0d81',
    xsrc='latiez:38:2b307b',
    ysrc='latiez:38:1956d5'
 )
 trace4 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['0.1', '0.1', '-', '-', '7.7'],
    name='Other',
    uid='57d06a',
    visible=True,
    xsrc='latiez:38:2b307b',
    ysrc='latiez:38:528339'
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
        range=[0, 93.57894736842105],
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
    y=['34.5', '33.2', '71.1', '59.1', '100'],
    name='Use of the internet',
    uid='f01c41',
    xsrc='latiez:42:c26a0f',
    ysrc='latiez:42:599eef'
 )
 trace2 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['65.5', '66.8', '28.9', '40.9', '-'],
    name='No use of the internet',
    uid='b749dc',
    xsrc='latiez:42:c26a0f',
    ysrc='latiez:42:247a6f'
 )
 data = Data([trace1, trace2])
 layout = Layout(
    autosize=True,
    hovermode='closest',
    showlegend=True,
    title='Number and Percentage of Establishments by <br> Internet use ,Economic Activity , Size of Establishment and Region',
    xaxis=XAxis(
        autorange=True,
        range=[-0.5, 4.5],
        title='',
        type='category'
    ),
    yaxis=YAxis(
        autorange=True,
        range=[0, 105.26315789473684],
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
    y=['0.2', '32.4', '18.9', '26.8', '8.7'],
    name='Dial line',
    uid='d7d58d',
    xsrc='latiez:46:0ad036',
    ysrc='latiez:46:298b42'
 )
 trace2 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['0.2', '23.1', '17.8', '21.1', '18.5'],
    name='ISDN',
    uid='0f3c45',
    xsrc='latiez:46:0ad036',
    ysrc='latiez:46:2272a0'
 )
 trace3 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['0.1', '7.8', '4.2', '11.3', '29.3'],
    name='xDSL',
    uid='4d927e',
    xsrc='latiez:46:0ad036',
    ysrc='latiez:46:aac430'
 )
 trace4 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['0.1', '14.3', '11.1', '20.1', '25.0'],
    name='Leased Line',
    uid='eaf055',
    xsrc='latiez:46:0ad036',
    ysrc='latiez:46:464e79'
 )
 trace5 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['2.9', '1.3', '2.8'],
    name='Cable modem',
    uid='ccf43c',
    xsrc='latiez:46:0ad036',
    ysrc='latiez:46:16bb22'
 )
 trace6 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['43.5', '41.0', '34.9', '42.1', '51.1'],
    name='Other fixed connection',
    uid='832bc3',
    xsrc='latiez:46:0ad036',
    ysrc='latiez:46:b37dc3'
 )
 trace7 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['1.0', '3.4', '2.7', '', '4.3'],
    name='Wireless connection',
    uid='30a22b',
    xsrc='latiez:46:0ad036',
    ysrc='latiez:46:d38a30'
 )
 trace8 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['27.3', '14.7', '17.5', '10.0', '23.9'],
    name='Mobile phone ',
    uid='629fd6',
    xsrc='latiez:46:0ad036',
    ysrc='latiez:46:17c1ee'
 )
 data = Data([trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8])
 layout = Layout(
    autosize=True,
    hovermode='closest',
    showlegend=True,
    title='Percentage of Establishments  use of  Internet by Type of<br> External connection to the internet access , Economic Activity , Size of Establishment and Region',
    xaxis=XAxis(
        autorange=True,
        range=[-0.5, 4.5],
        title='',
        type='category'
    ),
    yaxis=YAxis(
        autorange=True,
        range=[0, 53.78947368421053],
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
    y=['89.5', '88.7', '83.3', '80.9', '93.8'],
    name='Own Web site ',
    uid='fe1048',
    xsrc='latiez:48:eb4976',
    ysrc='latiez:48:03abf3'
 )
 trace2 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['9.9', '9.2', '16.2', '17.0', '2.1'],
    name='Other Web portal ',
    uid='36274e',
    xsrc='latiez:48:eb4976',
    ysrc='latiez:48:574c3b'
 )
 trace3 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['0.6', '2.1', '0.5', '2.2', '4.1'],
    name='Own Web site  Other Web portal ',
    uid='31c142',
    xsrc='latiez:48:eb4976',
    ysrc='latiez:48:09aaec'
 )
 data = Data([trace1, trace2, trace3])
 layout = Layout(
    autosize=True,
    hovermode='closest',
    showlegend=True,
    title='Number and Percentage of Establishments by <br>Use of Web site  and Category of  Industry',
    xaxis=XAxis(
        autorange=True,
        range=[-0.5, 4.5],
        title='',
        type='category'
    ),
    yaxis=YAxis(
        autorange=True,
        range=[0, 98.73684210526315],
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
    y=['65.6', '68.9', '23.1', '21.7', '3.4'],
    name='Individual proprietor ',
    uid='e12168',
    xsrc='latiez:38:2b307b',
    ysrc='latiez:38:61bb72'
 )
 trace2 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['6.6', '9.0', '11.2', '12.1', '-'],
    name='Juristic partnership ',
    uid='1981ec',
    xsrc='latiez:38:2b307b',
    ysrc='latiez:38:4b8936'
 )
 trace3 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['27.7', '22.0', '65.7', '66.2', '88.9'],
    name='Company limited, Public company limited',
    uid='bf0d81',
    xsrc='latiez:38:2b307b',
    ysrc='latiez:38:1956d5'
 )
 trace4 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['0.1', '0.1', '-', '-', '7.7'],
    name='Other',
    uid='57d06a',
    visible=True,
    xsrc='latiez:38:2b307b',
    ysrc='latiez:38:528339'
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
        range=[0, 93.57894736842105],
        title='percent',
        type='linear'
    )
 )
 fig = Figure(data=data, layout=layout)
 plot_url = py.plot(fig)
create_plot()
