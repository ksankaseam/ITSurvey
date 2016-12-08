import plotly.plotly as py
from plotly.graph_objs import *

def create_plot():
 """Build graph in year 2557"""
 #The graph shows percentage of Establishments by Form of Legal Organization
 py.sign_in('memiine2', 'zi5WaKnR3sQ3qJnY63XT')
 trace1 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['62.3', '63.1', '17.1', '16.1', '-'],
    name='Individual proprietor ',
    uid='50b10e',
    xsrc='latiez:52:e4b98e',
    ysrc='latiez:52:4b79ab'
 )
 trace2 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['6.6', '9.0', '13.6', '21.8', '9.4'],
    name='Juristic partnership ',
    uid='b028ee',
    xsrc='latiez:52:e4b98e',
    ysrc='latiez:52:d7c244'
 )
 trace3 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['31.1', '27.9', '69.3', '62.1', '90.6'],
    name='Company limited, Public company limited',
    uid='f255c2',
    xsrc='latiez:52:e4b98e',
    ysrc='latiez:52:e452fa'
 )
 trace4 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['1.4', '0.4', '-', '-', '15.9'],
    name='other',
    uid='0013c0',
    xsrc='latiez:52:e4b98e',
    ysrc='latiez:52:559243'
 )
 data = Data([trace1, trace2, trace3, trace4])
 layout = Layout(
    autosize=True,
    hovermode='closest',
    showlegend=True,
    title='Number and Percentage of Establishments by<Br> Form of Legal Organization , Economic Activity , Size of Establishment and Region',
    xaxis=XAxis(
        autorange=True,
        range=[-0.5, 4.5],
        title='B',
        type='category'
    ),
    yaxis=YAxis(
        autorange=True,
        range=[0, 95.36842105263158],
        title='A',
        type='linear'
    )
 )
 fig = Figure(data=data, layout=layout)
 plot_url = py.plot(fig)

 #The graph shows Percentage of Establishments by Internet use
 py.sign_in('memiine2', 'zi5WaKnR3sQ3qJnY63XT')
 trace1 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['32.7', '31.8', '76.8', '47.8', '95.3'],
    name='Use of the internet',
    uid='695aa1',
    xsrc='latiez:56:3265b2',
    ysrc='latiez:56:1f5073'
 )
 trace2 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['67.3', '68.2', '23.2', '52.2', '4.7'],
    name='No use of the internet',
    uid='03cfb9',
    xsrc='latiez:56:3265b2',
    ysrc='latiez:56:8b9706'
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
    y=['46.9', '48.8', '58.6', '59.3', '65.3'],
    name='lan',
    uid='bd3e98',
    xsrc='latiez:59:1e4228',
    ysrc='latiez:59:e9abb2'
 )
 trace2 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['26.3', '25.5', '42.3', '36.5', '59.8'],
    name='internet',
    uid='6429fb',
    xsrc='latiez:59:1e4228',
    ysrc='latiez:59:bb8233'
 )
 trace3 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['13.9', '9.7', '10.3', '15.0', '8.0'],
    name='extranet',
    uid='b2518b',
    xsrc='latiez:59:1e4228',
    ysrc='latiez:59:aa5497'
 )
 data = Data([trace1, trace2, trace3])
 layout = Layout(
    autosize=True,
    hovermode='closest',
    showlegend=True,
    title='Percentagef Establishments  use of  Internet by Type of External<br> connection to the internet access , Economic Activity , Size of Establishment and Region',
    xaxis=XAxis(
        autorange=True,
        range=[-0.5, 4.5],
        title='',
        type='category'
    ),
    yaxis=YAxis(
        autorange=True,
        range=[0, 61.15789473684211],
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
    y=['84.1', '87.0', '84.8', '83.9', '93.4'],
    name='Own Web site ',
    uid='cbf9c9',
    xsrc='latiez:61:857af0',
    ysrc='latiez:61:6936f5'
 )
 trace2 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['14.6', '11.6', '14.7', '14.9', '4.4'],
    name='Other Web portal ',
    uid='8ddd1f',
    xsrc='latiez:61:857af0',
    ysrc='latiez:61:496ba2'
 )
 trace3 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['1.3', '1.3', '0.6', '1.3', '2.2'],
    name='Own Web site  Other Web portal ',
    uid='405c63',
    xsrc='latiez:61:857af0',
    ysrc='latiez:61:702878'
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
        range=[0, 98.31578947368422],
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
    y=['16.4', '9.4', '9.6', '6.4', '9.5'],
    name='Lower  than Vocationl',
    uid='e1e125',
    xsrc='latiez:63:1d6089',
    ysrc='latiez:63:c5d436'
 )
 trace2 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['17.6', '16.7', '13.5', '16.5', '39.3'],
    name='Vocational',
    uid='a354d7',
    xsrc='latiez:63:1d6089',
    ysrc='latiez:63:4423a7'
 )
 trace3 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['60.2', '67.6', '74.0', '69.3', '48.6'],
    name='Bachelor ',
    uid='d59045',
    xsrc='latiez:63:1d6089',
    ysrc='latiez:63:352c72'
 )
 trace4 = Bar(
    x=['Business Trade and Services', 'Manufacturing', 'Construction', 'Land Transport and Storage', 'Private Hospital'],
    y=['5.8', '6.2', '2.9', '7.8', '2.7'],
    name='Higher than Bachelor ',
    uid='29a395',
    xsrc='latiez:63:1d6089',
    ysrc='latiez:63:d947a4'
 )
 data = Data([trace1, trace2, trace3, trace4])
 layout = Layout(
    autosize=True,
    hovermode='closest',
    showlegend=True,
    title='Number of Personnel in enterprise who have graduated in the field of  ICT by  <br> level  of  education , Economic Activity , Size of Establishment and Region',
    xaxis=XAxis(
        autorange=True,
        range=[-0.5, 4.5],
        title='',
        type='category'
    ),
    yaxis=YAxis(
        autorange=True,
        range=[0, 77.89473684210526],
        title='percent',
        type='linear'
    )
 )
 fig = Figure(data=data, layout=layout)
 plot_url = py.plot(fig)
 
create_plot()
