import plotly.plotly as py
from plotly.graph_objs import *

def create_plot():
 """Build Graph in year 2554"""
 #The graph shows percentage of Establishments by Form of Legal Organization
 py.sign_in('memiine2', 'zi5WaKnR3sQ3qJnY63XT')
 trace1 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital', 'Information and Communication'],
    y=['75.70', '78.60', '62.30', '73.70', '6.30'],
    hoverinfo='y+name',
    name='Individual proprietor ',
    uid='f100c0',
    xsrc='memiine:13:3efcbb',
    ysrc='memiine:13:853ec9'
 )
 trace2 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital', 'Information and Communication'],
    y=['6.1', '3.3', '20', '8.5', '1.8'],
    hoverinfo='y+name',
    name='Juristic partnership ',
    uid='80e655',
    xsrc='memiine:13:3efcbb',
    ysrc='memiine:13:fb47ba'
 )
 trace3 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital', 'Information and Communication'],
    y=['13', '6.3', '16.4', '17.1', '20.5'],
    hoverinfo='y+name',
    name='Company limited,  Public company limited ',
    uid='756d97',
    xsrc='memiine:13:3efcbb',
    ysrc='memiine:13:809b4b'
 )
 trace4 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital', 'Information and Communication'],
    y=['5.2', '11.8', '1.3', '0.7', '71.4'],
    hoverinfo='y+name',
    name='Other',
    uid='332d63',
    xsrc='memiine:13:3efcbb',
    ysrc='memiine:13:22ef9a'
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
        range=[0, 82.73684210526315],
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
    y=['18.70', '8.30', '27.00', '16.40', '96.10'],
    hoverinfo='y+name',
    name='Use of the internet',
    uid='a9fc33',
    xsrc='memiine:15:6155c8',
    ysrc='memiine:15:7c131c'
 )
 trace2 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['81.3', '91.7', '73', '83.6', '3.9'],
    hoverinfo='y+name',
    name='No use of the internet',
    uid='0ef856',
    xsrc='memiine:15:6155c8',
    ysrc='memiine:15:d13271'
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
        range=[0, 101.1578947368421],
        title='percent',
        type='linear'
    )
 )
 fig = Figure(data=data, layout=layout)
 plot_url = py.plot(fig)

 #the graph shows Percentage of Establishments  use of Internet by Type of External connection to the internet access
 py.sign_in('memiine2', 'zi5WaKnR3sQ3qJnY63XT')
 trace1 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital', 'Information and Communication'],
    y=['19.10', '25.60', '23.10', '17.90', '9.50'],
    hoverinfo='y+name',
    name='dial up',
    uid='30d569',
    xsrc='memiine:19:e98983',
    ysrc='memiine:19:e57847'
 )
 trace2 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital', 'Information and Communication'],
    y=['12.3', '8.2', '11.9', '13.6', '10'],
    hoverinfo='y+name',
    name='ISDN ',
    uid='0c11c8',
    xsrc='memiine:19:e98983',
    ysrc='memiine:19:3ba726'
 )
 trace3 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital', 'Information and Communication'],
    y=['57.8', '50.9', '55.8', '58.9', '83.6'],
    hoverinfo='y+name',
    name='xDSL',
    uid='0fe48b',
    xsrc='memiine:19:e98983',
    ysrc='memiine:19:68db73'
 )
 trace4 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital', 'Information and Communication'],
    y=['4', '9.4', '3.7', '4.2', '18.7'],
    hoverinfo='y+name',
    name='Leased Line ',
    uid='9e4216',
    xsrc='memiine:19:e98983',
    ysrc='memiine:19:a6d04f'
 )
 trace5 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital', 'Information and Communication'],
    y=['3.2', '3.6', '4.1', '7.3', '6.4'],
    hoverinfo='y+name',
    name='Cable Modem ',
    uid='e57dca',
    xsrc='memiine:19:e98983',
    ysrc='memiine:19:f3552d'
 )
 trace6 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital', 'Information and Communication'],
    y=['0.9', '1.5', '0.8', '0.7', '5.6'],
    hoverinfo='y+name',
    name='Other  Fixed ',
    uid='d8b3e4',
    xsrc='memiine:19:e98983',
    ysrc='memiine:19:83529b'
 )
 trace7 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital', 'Information and Communication'],
    y=['5.8', '8.2', '9.9', '7.4', '9.4'],
    hoverinfo='y+name',
    name='Wireless ',
    uid='93365a',
    xsrc='memiine:19:e98983',
    ysrc='memiine:19:faeee7'
 )
 data = Data([trace1, trace2, trace3, trace4, trace5, trace6, trace7])
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
        range=[0, 88],
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
    y=['74.3', '81.6', '81.6', '80.4', '74'],
    hoverinfo='y+name',
    name='Own Web site ',
    uid='bf7aac',
    xsrc='memiine:21:948ad8',
    ysrc='memiine:21:9018d9'
 )
 trace2 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['25.4', '16.9', '16.4', '19.4', '20.8'],
    hoverinfo='y+name',
    name='Other Web portal ',
    uid='46fbb3',
    xsrc='memiine:21:948ad8',
    ysrc='memiine:21:e09cf1'
 )
 trace3 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['0.2', '1.5', '2', '0.2', '5.2'],
    hoverinfo='y+name',
    name='Own Web site  Other Web portal ',
    uid='7b1f5e',
    xsrc='memiine:21:948ad8',
    ysrc='memiine:21:a2c12d'
 )
 data = Data([trace1, trace2, trace3])
 layout = Layout(
    autosize=True,
    hovermode='closest',
    showlegend=True,
    title='Number and Percentage of Establishments <br>by Use of Web site &nbsp;and Category of &nbsp;Industry&nbsp;',
    xaxis=XAxis(
        autorange=True,
        range=[-0.5, 4.5],
        title='',
        type='category'
    ),
    yaxis=YAxis(
        autorange=True,
        range=[0, 85.89473684210526],
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
    y=['2.6', '3.6', '0.1', '0.4', '3'],
    hoverinfo='y+name',
    name='Lower than Vocationl',
    uid='6506be',
    xsrc='memiine:23:020d57',
    ysrc='memiine:23:ce98b7'
 )
 trace2 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['27.4', '17.5', '32.8', '26.4', '9'],
    hoverinfo='y+name',
    name='Vocational',
    uid='614daf',
    xsrc='memiine:23:020d57',
    ysrc='memiine:23:9f328a'
 )
 trace3 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['62', '71.3', '62.8', '66', '80.6'],
    hoverinfo='y+name',
    name='Bachelor ',
    uid='a7d84d',
    xsrc='memiine:23:020d57',
    ysrc='memiine:23:bde8ac'
 )
 trace4 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['8', '7.6', '4.3', '7.1', '7.5'],
    hoverinfo='y+name',
    name='Higher than Bachelor ',
    uid='5f04c9',
    xsrc='memiine:23:020d57',
    ysrc='memiine:23:6b008c'
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
        range=[0, 84.84210526315789],
        title='percent',
        type='linear'
    )
 )
 fig = Figure(data=data, layout=layout)
 plot_url = py.plot(fig)
create_plot()
