#!/usr/bin/env python
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.plotly as py
from dash.dependencies import Input, Output, State
import base64
import io
import os
import pandas as pd


print(dcc.__version__) # 0.6.0 or above is required

app = dash.Dash()
colors = {
	'text': '#119DD2'
}
# Since we're adding callbacks to elements that don't exist in the app.layout,
# Dash will raise an exception to warn us that we might be
# doing something wrong.
# In this case, we're adding the elements through a callback, so we can ignore
# the exception.
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
	dcc.Location(id='url', refresh=False),
	html.Div(id='output-data-upload', style={'display': 'None'}),
	html.Div(id='csv-upload', style={'display':'None'}),
	html.Div(id='page-content')
])

#index_page = html.Div([
#		html.H1(
#			children='DiaControl',
#			style={
#				'textAlign': 'center',
#				'color': colors['text']
#			}
#		),
#		html.H5(
#			children='Welcome to DiaControl',
#		),
#		html.Br(),
#		html.Br(),
#		html.Br(),
#		html.Br(),
#		html.Br(),
#		html.Div([
#			html.A(html.Button('Health Provider', id='button1'), href='/page-1'),
#			html.A(html.Button('Patient', id='button2', style={'marginLeft':100}),href='/page-3'),
#			], style={'marginLeft':350}),
#])

#page_3_layout = html.Div([
#		dcc.Dropdown(
#			id='input1',
#			options=[{'label': i, 'value': i} for i in ['Doctor', 'Health provider', 'Patient']],
#		),
#		dcc.Link('Go back to home', href='/'),
#		html.Br(),
#		html.Label(
#			children='Your Age',
#			style={
#				'textAlign': 'center',
#			}
#		),
#    	dcc.Dropdown(
##			options=[{'label': i, 'value': i} for i in ['0-10','10-20','20-30','30-40','40-50', '50-60', '60-70', '70-80', '80-90', '90-100']],
#		),
#		html.Label(
#			children='Gender'
#		),
#		dcc.Dropdown(
##			options=[{'label': i, 'value': i} for i in ['Male', 'Female']],
#		),
##			children='Number of medicine taken',
#			style={
#              'textAlign': 'center',
#			}
#		),
#		dcc.Input(type='number', id='input3'),
#		dcc.Slider(
#			min=1,
#			max=50,
#			marks={i:' {}'.format(i) if i == 1 else 5*int(i) for i in range(0,11)},
#		),
#		html.Label(
#			children='How often(times) you visit doctor or go to hospital last year',
#		),
#		dcc.Input(type='number', id='input4'),
#		html.Label(
#			children='Do you have any other diseases beside diabete?'
#		),
#		dcc.Dropdown(
#			options=[
#				{'label': 'Circulatory', 'value':'C'},
#				{'label':'Respiratory', 'value':'R'},
#				{'label': 'Digestive', 'value':'D'},
##				{'label': 'Injury', 'value':'I'},
#				{'label': 'Musculoskeletal', 'value':'M'},
#				{'label': 'Genitourinary', 'value':'G'},
#				{'label': 'Neoplasms', 'value':'N'},
#				{'label': 'Others', 'value':'O'},
#				{'label': 'None', 'value': 'NO'},
#			],
#			value=[],
#			multi=True
#		),
#		html.Br(),
#		html.A(html.Button('Predict!',id='button3'), href='/page-4'),

#		html.Br(),
#		dcc.Link('Sumbit!', id ='button', href='/page-1'),
#])


index_page = html.Div([
#	dcc.Link('Go back to home', href='/'),
	html.H3(
		children='DiaControl',
		style={
			'textAlign': 'center',
			'color': colors['text']
			}
	),
	html.H5(
		children='Welcome to DiaControl',
		),
	html.Br(),
#	html.H1('DragPatient info'),
	html.Label(['See more details about the uploaded files ', html.A('format.', href='/page-1')]),
	dcc.Upload(
		id='upload_data',
		children=html.Div([
			'Drag and Drop or ',
			html.A('Select Files')
		]),
		style={
			'width': '100%',
			'height': '60px',
			'lineHeight': '60px',
			'borderWidth': '1px',
			'borderStyle': 'dashed',
			'borderRadius': '5px',
			'textAlign': 'center',
			'margin': '10px'
		},
	),
	dcc.Link(html.Button('Get Result',id='button2'), href='/page-3'),
	html.Hr(),
	html.Label('or run one of our Demos'),
	dcc.Dropdown(
		id='patient',
		options=[
			{'label': 'Patient1', 'value': '40.34%'},
			{'label': 'Patient2', 'value': '60.82%'},
			{'label': 'Patient3', 'value': '30.64%'}
		],
	),

	html.Br(),
	html.Br(),
#	dcc.Link('Sumbit!', id ='button', href='/page-2'),
	dcc.Link(html.Button('Get Result',id='button3'), href='/page-2'),
	html.Br(),
	html.Br(),
	html.Br(),
	html.Label(['See more details on my ', html.A('github.', href='https://github.com/zhihuaqi/DiaControl')]),
	html.Label(['See my Demo on  ', html.A('Google Slides.', href='https://docs.google.com/presentation/d/1jLKRizbb2XR8uwX6hMMt4i7EgHHyGkDhHuJhzvh_E-E/edit#slide=id.p19')]),



#	def parse_contents(contents, filename, date):
#		content_type, content_string = contents.split(',')

#		decoded = base64.b64decode(content_string)
#		try:
#			if 'csv' in filename:
			# Assume that the user uploaded a CSV file
#				df = pd.read_csv(
#					io.StringIO(decoded.decode('utf-8')))
#			elif 'xls' in filename:
			# Assume that the user uploaded an excel file
#				df = pd.read_excel(io.BytesIO(decoded))
#		except Exception as e:
#			print(e)
#			return html.Div([
#				'There was an error processing this file.'
#			])

#		return html.Div([
#			html.H5(filename),
#			html.H6(datetime.datetime.fromtimestamp(date)),
#			# Use the DataTable prototype component:
#			# github.com/plotly/dash-table-experiments
#			dt.DataTable(rows=df.to_dict('records')),

#			html.Hr(),  # horizontal
#			# For debugging, display the raw contents provided by the web browser
#			html.Div('Raw Content'),
#			html.Pre(contents[0:200] + '...', style={
#				'whiteSpace': 'pre-wrap',
#				'wordBreak': 'break-all'
#			})
#		])

#@app.callback(Output('output-data-upload', 'children'),
#			[Input('upload-data', 'contents'),
#			Input('upload-data', 'filename'),
#			Input('upload-data', 'last_modified')])

#def update_output(list_of_contents, list_of_names, list_of_dates):
#	if list_of_contents is not None:
#		children = [
#			parse_contents(c, n, d) for c, n, d in
#			zip(list_of_contents, list_of_names, list_of_dates)]
#		return children
#	dcc.Dropdown(
#		id='page-1-dropdown',
#		options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
#		value='LA'
#	),
#	html.Div(id='page-1-content'),
#	html.Br(),
#	dcc.Link('Go to Page 2', href='/page-2'),

#	html.Label(
#		children='This diabetic patient has high risk of re-hospitalization.',
#		style={
#               'textAlign': 'center',
#		}
#	),
#	html.Label(
#		children='The top ten important features result in this high risk:'
#	),

#	dcc.Graph(
#		figure=go.Figure(
#			data=[
#				go.Bar(
#					y=['discharge_disposition_id', 'service_utilization', 'numMedchange', 'change', 'num_lab_procedures','gender', 'num_medications', 'time_in_hospital', 'c_diag1', 'number_diagnoses'],
#					x=[0.2694935547479033, 0.24813502895801992,0.08519110011224647,0.07428183331800338,0.04037994495504535,0.03217196877151764,0.030862258182392403,0.02907929990750847,0.02862744555068743,0.028162243553407733],
#					name='Rest of world',
#					orientation = 'h',
#					marker=go.Marker(
#						color='rgb(55, 83, 109)'
#					)
#				)
#			],
#			layout=go.Layout(
#				title='Most important features',
#				width=1000,
#				height=400,
#				margin=go.Margin(l=150, r=0, t=40, b=30)
#			)
#		),
#		style={'height': 300},
#		id='my-graph'
#),
	html.Br(),
])

@app.callback(Output('output-data-upload', 'children'),
              [Input('patient', 'value')])
def update_output(value):
    return html.Div([value], style={'padding-end': '60px','align': "center"})

@app.callback(Output('csv-upload', 'children'),
              [Input('upload_data', 'contents'),
               Input('upload_data', 'filename'),
               Input('upload_data', 'last_modified')])
def update_output2(contents, filename, date):
    if contents is not None:
        filename, df = parse_contents(contents, filename, date)
        # This is the key to the hidden div formatting
        return df.to_json(orient = 'split')

@app.callback(Output('output-container-button', 'children'),
              [Input('output-data-upload', 'children')])
def update_graph(value):
	return html.H3([value], style={'color':'red'})

@app.callback(Output('output-container-button2', 'children'),
              [Input('csv-upload', 'children')])
def update_graph2(json):
	df = pd.read_json(json, orient='split')
	number = 0.13*float(df['value'][0]) + 1.3*float(df['value'][2]) + 0.42*float(df['value'][4]) + 0.51*float(df['value'][5]) + 1.70*float(df['value'][6]) + 0.03*float(df['value'][7]) + 1.23*float(df['value'][8]) + 0.03*float(df['value'][9])
	return html.H3([str(round(number,2)) + '%'], style={'color':'red'})

@app.callback(Output('page-content', 'children'),
			[Input('url', 'pathname')])
def display_page(pathname):
	if pathname == '/page-1':
		return page_1_layout
	elif pathname == '/page-2':
		return page_2_layout
	elif pathname == '/page-3':
		return page_3_layout
	else:
		return index_page

page_1_layout= html.Div([
	dcc.Link('Go back to home', href='/'),
	html.Br(),
	html.H5('please list the following info, with comma as separator'), 
	html.Div('age,50'),
	html.Div('gender,Female'),
	html.Div('time_in_hospital,10'),
	html.Div('discharege_type:(go home/tranfer to another center),0'),
	html.Div('num_lab_procedures,20'),
	html.Div('num_medications,10'),
	html.Div('num_diagnoses,5'),
	html.Div('primary_diagnosis,3'),
	html.Div('num_inpatient_visits_last_year,10'),
	html.Div('num_emergency_visits_last_year,12'),
	
])

page_2_layout= html.Div([
		html.Br(),
	#	dcc.Link('Go to Previous Page', href='/page-1'),
		html.Br(),
		dcc.Link('Go back to home', href='/'),
		html.Br(),
		html.H3('Prediction result'),
		html.Div('The probability of readmission for this patient is:'),
		html.Div(id='output-container-button', style={'color':'red'}),
		html.Label(children='The top ten risk factors result in high risk of readmission:'
		),

		dcc.Graph(
			figure=go.Figure(
				data=[
					go.Bar(
						y=['Procedures', 'Primary diagnose','Emergency visits', 'Age', 'Lab procedures', 'Medications', 'Diagnoses','Days in hospital', 'Inpatient visits','Discharge type', ],
						x=[0.021496400917561036,0.027687083825592086,0.029005390831124116,0.03223161538922079,0.04201952491618829,0.0518058968526597,0.07011070337973416,0.0937897856647737,0.23261467689073614,0.3120002693792342],
						name='Rest of world',
						orientation = 'h',
						marker=go.Marker(
							color='rgb(55, 83, 109)'
						)
					)
				],
				layout=go.Layout(
					title='Most important risk factors',
					width=1000,
					height=400,
					margin=go.Margin(l=150, r=0, t=40, b=30)
				)
			),
			style={'height': 300},
			id='my-graph'
		),

	])

page_3_layout = html.Div([
		html.Br(),
	#	dcc.Link('Go to Previous Page', href='/page-1'),
		html.Br(),
		dcc.Link('Go back to home', href='/'),
		html.Br(),
		html.H3('Prediction result'),
		html.Div('The probability of readmission for this patient is:'),
		html.Div(id='output-container-button2', style={'color':'red'}),
		html.Label(children='The top ten risk factors result in high risk of readmission:'
		),

		dcc.Graph(
			figure=go.Figure(
				data=[
					go.Bar(
						y=['Procedures', 'Primary diagnose','Emergency visits', 'Age', 'Lab procedures', 'Medications', 'Diagnoses','Days in hospital', 'Inpatient visits','Discharge type', ],
						x=[0.021496400917561036,0.027687083825592086,0.029005390831124116,0.03223161538922079,0.04201952491618829,0.0518058968526597,0.07011070337973416,0.0937897856647737,0.23261467689073614,0.3120002693792342],
						name='Rest of world',
						orientation = 'h',
						marker=go.Marker(
							color='rgb(55, 83, 109)'
						)
					)
				],
				layout=go.Layout(
					title='Most important risk factors',
					width=1000,
					height=400,
					margin=go.Margin(l=150, r=0, t=40, b=30)
				)
			),
			style={'height': 300},
			id='my-graph'
		),

	])

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')
    print("hey: {}, {}, {}, {}".format(filename, date, content_string, content_type))
    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            print("csv!")
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
            print(df)
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return filename,df

#page_4_layout = html.Div([
#	html.Br(),
#	dcc.Link('Go to Previous Page', href='/page-1'),
#	html.Br(),
#	dcc.Link('Go back to home', href='/'),
#	html.Br(),
#	html.H1('Prediction result'),
#	html.Label(children='Congratulation, You will in good condiction by your control of Diabetes!!'),
#   html.Br(),
#	html.Label(children='Here are some helful cateloies of tips, you can see more details by clicking on them:'),
#	dcc.Tabs(tabs=[
#			{'label': 'Reduce portion sizes', 'value': 1},
#			{'label': 'Be physically active', 'value': 2},
#			{'label': 'Make healthy food choices', 'value': 3},
#			{'label': 'Stress reduction/ mental health', 'value': 4},
#	],id='tabs'),
#	html.Div(id='tab-output')
#])

#tab_1_layout= html.Div([
#	html.Br(),
#	html.Label(children='1.Drink a large glass of water 10 minutes before your meal to feel less hungry.'),
#	html.Br(),
#	html.Label(children='2.Keep meat, chicken, turkey and fish portions to about 3 ounces.'),
#	html.Br(),
#	html.Label(children='3.Make less food look like more by serving your meal on a salad or breakfast plate.'),
#	html.Br(),
#	html.Label(children='4.Eat slowly. It takes 20 minutes for your stomach to send a signal to your brain that you are full.'),
#	html.Br(),
#	html.Label(children='5.Listen to music while you eat instead of watching TV (people tend to eat more while watching TV).'),
#])

#tab_2_layout= html.Div([
#	html.Br(),
#	html.Label(children='1.Turn up the music and jam while doing household chores.'),
#	html.Br(),
#	html.Label(children='2.Work out with a video that shows you how to get active.'),
#	html.Br(),
#	html.Label(children='3.Deliver a message in person to a co-worker instead of sending an e-mail.'),
#	html.Br(),
#	html.Label(children='4.Catch up with friends during a walk instead of by phone.'),
#	html.Br(),
#	html.Label(children='5.Get off the bus one stop early and walk the rest of the way home or to work if it is safe.'),
#])

#tab_3_layout= html.Div([
#	html.Br(),
#	html.Label(children='1.Buy a mix of vegetables when you go food shopping.'),
#	html.Br(),
#	html.Label(children='2.Choose veggie toppings like spinach, broccoli, and peppers for your pizza.'),
#	html.Br(),
#	html.Label(children='3.Avoid getting too hungry by eating a healthy snack between meals.'),
#	html.Br(),
#	html.Label(children='4.Serve your favorite vegetable and a salad with low-fat macaroni and cheese.'),
#	html.Br(),
#	html.Label(children='5.Try different recipes for baking or broiling meat, chicken, and fish.'),
#])

#tab_4_layout= html.Div([
#	html.Br(),
#	html.Label(children='1.Find ways to relax. Try deep breathing, taking a walk, yoga, or listening to your favorite music.'),
#	html.Br(),
#	html.Label(children='2.Pamper yourself. Read a book, take a long bath, or meditate.'),
#	html.Br(),
#	html.Label(children='3.Think before you eat. Try not to eat when you are bored, upset, or unhappy.'),
#	html.Br(),
#	html.Label(children='4.Don’t get discouraged if you have a bad day. If you get off track, start again and keep at it.'),
#	html.Br(),
#	html.Label(children='5.You don’t have to prevent diabetes alone. Ask your friends and family to help you out, and involve them in your activities.'),
#])
#@app.callback(
#	Output('tab-output', 'children'),
#	[Input('tabs', 'value')])
#def show_content(value):
#	if value == 1:
#		return tab_1_layout
#	elif value == 2:
#		return tab_2_layout
#	elif value == 3:
#		return tab_3_layout
#	else:
#		return tab_4_layout


# Update the index

# You could also return a 404 "URL not found" page here

external_css = ["https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
                "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                "https://fonts.googleapis.com/css?family=Work+Sans",
                "https://bootswatch.com/3/paper/bootstrap.css"]
                #'https://codepen.io/chriddyp/pen/bWLwgP.css']

for css in external_css:
    app.css.append_css({"external_url": css})

if 'DYNO' in os.environ:
    app.scripts.append_script({
        'external_url': 'https://cdn.rawgit.com/chriddyp/ca0d8f02a1659981a0ea7f013a378bbd/raw/e79f3f789517deec58f41251f7dbb6bee72c44ab/plotly_ga.js'
    })


if __name__ == '__main__':
		app.run_server(host="0.0.0.0",debug=True)
