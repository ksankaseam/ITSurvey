import plotly.plotly as py
from plotly.graph_objs import *

def create_plot():
 """Build All Graph in year 2553"""

 #The graph shows percentage of Establishments by Form of Legal Organization
 py.sign_in('memiine', 'Gw463qUTJMpKC8aUVebo')
 trace1 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['75', '74.7', '60.4', '66.1', '4.7'],
    name='B',
    uid='7a0614',
    visible=True,
    xsrc='jokerlordz:8:f5e27b',
    ysrc='jokerlordz:8:bdbe11'
 )
 trace2 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['6.6', '3.1', '20.5', '8.9', '1.4'],
    name='Juristic partnership ',
    uid='836e80',
    visible=True,
    xsrc='jokerlordz:8:f5e27b',
    ysrc='jokerlordz:8:ce4fff'
 )
 trace3 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['12.4', '6.6', '18.5', '22.5', '21.5'],
    name='Company limited, Public company limited',
    uid='05276e',
    xsrc='jokerlordz:8:f5e27b',
    ysrc='jokerlordz:8:8eef87'
 )
 trace4 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['5.9', '15.5', '0.4', '2.6', '72.4'],
    hoverinfo='y+name',
    name='Other',
    uid='d7eab2',
    xsrc='jokerlordz:8:f5e27b',
    ysrc='jokerlordz:8:b204f0'
 )
 data = Data([trace1, trace2, trace3, trace4])
 layout = Layout(
    autosize=False,
    height=450,
    hovermode='closest',
    legend=Legend(
        x=1.0064590486735083,
        y=0.8064516129032258
    ),
    margin=Margin(
        r=250,
        b=40,
        l=90,
        pad=12
    ),
    showlegend=True,
    title='Number and Percentage of Establishments <br>by Form of Legal Organization , Economic Activity , Size of Establishment and Region',
    width=801.989,
    xaxis=XAxis(
        autorange=False,
        range=[-0.5377845279, 4.5],
        title='<br>',
        type='category',
        zeroline=True
    ),
    yaxis=YAxis(
        autorange=False,
        range=[0.00010000000000000021, 100],
        title='percent<br><br>',
        type='linear'
    )
 )
 fig = Figure(data=data, layout=layout)
 plot_url = py.plot(fig)

#The graph shows Percentage of Establishments by Internet use
 py.sign_in('memiine', 'Gw463qUTJMpKC8aUVebo')
 trace1 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['18.4', '8.4', '28', '18.9', '93.7'],
    name='Use of the internet',
    orientation='v',
    uid='ac2f9b',
    xsrc='jokerlordz:16:bc03ba',
    ysrc='jokerlordz:16:adc63d'
 )
 trace2 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['81.6', '91.6', '72', '81.1', '6.3'],
    name='No use of the internet',
    opacity=1,
    orientation='v',
    uid='cfb74e',
    xsrc='jokerlordz:16:bc03ba',
    ysrc='jokerlordz:16:4d433a'
 )
 data = Data([trace1, trace2])
 layout = Layout(
    autosize=False,
    bargap=0.5,
    barmode='group',
    height=450,
    hovermode='closest',
    legend=Legend(
        x=1,
        y=0.9
    ),
    showlegend=True,
    title='&nbsp;Number and Percentage of Establishments<br> by &nbsp;Internet use , Economic Activity , Size of Establishment and Region <br>',
    width=801.989,
    xaxis=XAxis(
        autorange=True,
        range=[-0.5, 4.5],
        title='<br>',
        type='category'
    ),
    yaxis=YAxis(
        autorange=True,
        range=[0, 98.63157894736842],
        title='percent',
        type='linear'
    )
 )
 fig = Figure(data=data, layout=layout)
 plot_url = py.plot(fig)
 
 #the graph shows Percentage of Establishments  use of  Internet by Type of External connection to the internet access
 py.sign_in('memiine', 'Gw463qUTJMpKC8aUVebo')
 trace1 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['19.10', '25.60', '23.10', '17.90', '9.50'],
    name='Dial up',
    uid='aabdab',
    xsrc='jokerlordz:20:e1d9ab',
    ysrc='jokerlordz:20:86fa5b'
 )
 trace2 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['12.3', '8.2', '11.9', '13.6', '10'],
    name='ISDN',
    uid='048458',
    xsrc='jokerlordz:20:e1d9ab',
    ysrc='jokerlordz:20:63b4c8'
 )
 trace3 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['57.8', '50.9', '55.8', '58.9', '83.6'],
    name='xDSL',
    uid='1fca2b',
    xsrc='jokerlordz:20:e1d9ab',
    ysrc='jokerlordz:20:f2d18f'
 )
 trace4 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['4', '9.4', '3.7', '4.2', '18.7'],
    name='Leased Line ',
    uid='38009a',
    xsrc='jokerlordz:20:e1d9ab',
    ysrc='jokerlordz:20:cd1e40'
 )
 trace5 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['3.2', '3.6', '4.1', '7.3', '6.4'],
    name='Cable Modem',
    uid='ef6af8',
    xsrc='jokerlordz:20:e1d9ab',
    ysrc='jokerlordz:20:cde709'
 )
 trace6 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['0.9', '1.5', '0.8', '0.7', '5.6'],
    name='Other Fixed',
    uid='f8d7c0',
    xsrc='jokerlordz:20:e1d9ab',
    ysrc='jokerlordz:20:38895d'
 )
 trace7 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['5.8', '8.2', '9.9', '7.4', '9.4'],
    name='Wireless ',
    uid='ea6f61',
    xsrc='jokerlordz:20:e1d9ab',
    ysrc='jokerlordz:20:0c24db'
 )
 data = Data([trace1, trace2, trace3, trace4, trace5, trace6, trace7])
 layout = Layout(
    autosize=False,
    height=450,
    hovermode='closest',
    legend=Legend(
        x=1.02,
        y=0.6
    ),
    margin=Margin(
        r=200,
        b=40,
        l=90,
        pad=12
    ),
    showlegend=True,
    title='Percentage of Establishments &nbsp;use of &nbsp;Internetby Type of<br> External connection to the internet access , Economic Activity , Size of Establishment and Region',
    width=801.989,
    xaxis=XAxis(
        autorange=False,
        range=[-0.5, 4.5],
        title='<br>',
        type='category',
        zeroline=True
    ),
    yaxis=YAxis(
        autorange=False,
        range=[0, 100],
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
    y=['77.1', '73.3', '78.3', '85.7', '68.6'],
    name='Own Website ',
    uid='51d810',
    visible=True,
    xsrc='jokerlordz:22:0e5529',
    ysrc='jokerlordz:22:37f6eb'
 )
 trace2 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['22.1', '24.2', '20.5', '13.8', '27.6'],
    name='Other  Web portal ',
    uid='a6c815',
    xsrc='jokerlordz:22:0e5529',
    ysrc='jokerlordz:22:32606c'
 )
 trace3 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['0.7', '2.4', '1.3', '0.4', '3.8'],
    name='Own Website  Other Web portal ',
    uid='c1aff9',
    xsrc='jokerlordz:22:0e5529',
    ysrc='jokerlordz:22:54c459'
 )
 data = Data([trace1, trace2, trace3])
 layout = Layout(
    autosize=False,
    bargap=0.4,
    height=450,
    hovermode='closest',
    legend=Legend(
        x=1.02,
        y=0.8
    ),
    showlegend=True,
    title='Number and Percentage of Establishments by Use of Web site &nbsp;and Category of &nbsp;Industry',
    width=801.989,
    xaxis=XAxis(
        autorange=True,
        range=[-0.5, 4.5],
        title='<br>',
        type='category'
    ),
    yaxis=YAxis(
        autorange=False,
        range=[0, 100],
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
    y=['10.40', '4.80', '5.20', '14.90', '5.20'],
    name='Lower than Vocationl',
    uid='230705',
    xsrc='jokerlordz:24:8ba8b3',
    ysrc='jokerlordz:24:ca308f'
 )
 trace2 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['28.30', '17.90', '19.80', '11.61', '17.50'],
    name='Vocational',
    uid='e1bebf',
    xsrc='jokerlordz:24:8ba8b3',
    ysrc='jokerlordz:24:7d8794'
 )
 trace3 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['57.20', '69.40', '69.30', '72.00', '68.40'],
    name='Bachelor',
    uid='080d99',
    xsrc='jokerlordz:24:8ba8b3',
    ysrc='jokerlordz:24:3acff9'
 )
 trace4 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['4.00', '7.80', '5.60', '1.50', '8.90'],
    hoverinfo='y+name',
    name='Higher than Bachelor',
    uid='a21e16',
    xsrc='jokerlordz:24:8ba8b3',
    ysrc='jokerlordz:24:01896d'
 )
 data = Data([trace1, trace2, trace3, trace4])
 layout = Layout(
    autosize=True,
    hovermode='closest',
    legend=Legend(
        x=1.02,
        y=0.8
    ),
    margin=Margin(
        pad=12
    ),
    showlegend=True,
    title='Number of &nbsp;Personnel in enterprise who have graduated <br>in the field of &nbsp;ICT &nbsp;by &nbsp;&nbsp;level &nbsp;of &nbsp;education , Economic Activity , Size of Establishment and Region',
    xaxis=XAxis(
        autorange=False,
        range=[-0.5, 4.5],
        title='<br>',
        type='category',
        zeroline=True
    ),
    yaxis=YAxis(
        autorange=False,
        range=[0, 100],
        title='percent',
        type='linear'
    )
 )
 fig = Figure(data=data, layout=layout)
 plot_url = py.plot(fig)

create_plot()
