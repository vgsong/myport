import json
import os

import pandas as pd
import numpy as np

from dash import dcc, html
from pathlib import Path
from dotenv import load_dotenv


from django.http import JsonResponse
from django.shortcuts import render
from django_plotly_dash import DjangoDash
from django.templatetags.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required

from .models import BlogEntry, JobTrackerEntry, BookTrackerEntry
from .forms import JobTrackerEntryForm

import plotly.express as px
import plotly.graph_objects as go

load_dotenv()

MDIR = Path(os.getenv('MDIR'))
STATIC_DIR = Path(os.getenv('STATIC_DIR'))


# ----- plotly constructors ----
def coffeesales_chart():
    mdir = '/home/vsong/DJANGO/vsong/minato/static/minato/data/'
    data_filename = 'CoffeeShop_Sales.csv'

    df = pd.read_csv(os.path.join(mdir, data_filename), index_col='transaction_id')

    df['transaction_date'] = pd.to_datetime(df['transaction_date'])
    sales_cat = df.groupby('product_category')['transaction_qty'].sum()

    print(df)

    
    sales_cat = sales_cat.to_dict()

    print(sales_cat.keys())

    app = DjangoDash('coffee_salescat')

    app.layout = html.Div([
        dcc.Graph(
            id='coffee-graph',
            figure={
                'data':[
                    {'x': list(sales_cat.keys()), 'y': list(sales_cat.values()), 'type':'bar', 'name': 'cat sales'},
                    ],
                'layout':{
                    'title': 'Coffee Sales by Cat',
                    'autosize': False,
                    'justifyContent': 'center',
                    'alignItems': 'center',
                    },
                },
                config={'responsive': True},
            ),

            
        ])


    return app

# def catsales_chart():

#     app = DjangoDash('catsales')
#     df_path = os.path.join(MDIR, 'CoffeeShop_Sales.csv')
#     result = {}
#     df = pd.read_csv(df_path)
#     df['transaction_date'] = pd.to_datetime(df['transaction_date'])
#     print(df.columns)
#     salesqty_month = df.groupby(df['transaction_date'].dt.month)['transaction_qty'].sum()
#     catqty_month = df.groupby([df['product_category'], df['transaction_date'].dt.month])['transaction_qty'].sum()

#     cat_list = list(set([k[0] for k in catqty_month.keys()]))

#     for x in cat_list:
#         result[x] = []
#         for k, v in catqty_month.items():
#             if x in k[0]:
#                 result[x].append((k[1], v))
    
    
#     print(result)


#     app = DjangoDash('ex_two')

#     fig = go.Figure()

#     buttons = list()
    
#     for i, (k, v) in enumerate(result.items()):
#         fig.add_trace(go.Scatter(x=[*range(1,7)], y=[x[1] for x in result[k]], name=k, visible=True))
#         btn_boolean = [False] * len(cat_list)
#         btn_boolean[i] = True
#         buttons.append({
#                         'label': k,
#                         'method': 'update',
#                         'args': [{'visible': btn_boolean}, {'title': 'Viewing GRAPH'}],
#         })

    

#     fig.update_layout(
#         updatemenus=[
#             {
#                 "buttons": buttons,
#                 "direction": "down",
#                 "showactive": True,
#                 "x": 0.1,  # Horizontal position
#                 "y": 1.15  # Vertical position (above the plot)
#             }
#         ],
#         height=500  # Keeping it large enough to be visible
#     )
#     app.layout = html.Div([
#         dcc.Graph(id='my-graph', 
#                 figure=fig,
#                 style={'height': '500px'})
#     ])


#     return

# def weeklysales_chart():
#     app = DjangoDash('wper_sales')

#     df = pd.read_csv(os.path.join(MDIR, 'CoffeeShop_Sales.csv'))
#     df['transaction_date'] = pd.to_datetime(df['transaction_date'])
#     print(df.columns)
#     salesqty_month = df.groupby(df['transaction_date'].dt.month)['transaction_qty'].sum()
#     catqty_month = df.groupby([df['product_category'], df['transaction_date'].dt.month])['transaction_qty'].sum()
#     df['WPER'] = df['transaction_date'] + pd.offsets.Week(weekday=5)

#     wpersales_month = df.groupby([df['product_category'], pd.Grouper(key='transaction_date', freq='W-SAT')])['transaction_qty'].sum()

#     print(wpersales_month)




#     return

# def twodrop_chart():

#     app = DjangoDash('MyTwoGraphApp') # Give it a unique name

#     app.layout = html.Div([
#         dcc.Dropdown(
#             id='my-dropdown',
#             options=[{'label': i, 'value': i} for i in ['Tech', 'Health', 'Finance']],
#             value='Tech'
#         ),
#         dcc.Graph(id='graph-one'),
#         dcc.Graph(id='graph-two')
#     ])


#     return




#  ----- main views -----------------------


def index(request):
    
    recent_posts = BlogEntry.objects.filter(status='final').order_by('-created_on')

    

    context = {
            'username' : 'vgs',
            'recent_posts' : recent_posts[:7],
            # 'line': dropdown_chart(),
    }

    return render(request, 'minato/index.html', context)

@login_required
def coffee_shop(request):
    coffeesales_chart()
    # dropdown_chart()
    # catsales_chart()
    # weeklysales_chart()
    # twodrop_chart()

    return render(request, 'minato/coffee_shop.html')


# ----- blog views --------------------------
def blog(request):

    recent_posts = BlogEntry.objects.filter(status='final').order_by('-created_on')

    context = {
               'recent_posts' : recent_posts
              }

    return render(request, 'minato/blog.html', context)

def blog_detail(request, detail_id):
    blog_entry = BlogEntry.objects.get(pk=int(detail_id))
    pic_filenames = []
    pic_dir = STATIC_DIR / 'blog' / str(detail_id).zfill(3)

    for x in pic_dir.iterdir():
        pic_filenames.append(Path('/', *x.parts[-2:]))

    print(pic_filenames)

    context = {
               'blog_entry' : blog_entry,
               'pic_filenames' : pic_filenames,
               }
               
    return render(request, 'minato/blog_detail.html', context)

@login_required
def jquery_learn(request):

    with open(os.path.join(MDIR, 'json_table_pract.csv'), 'r', encoding='utf-8-sig') as cf:
        data=[x.strip().split(',') for x in cf.readlines()]

    
    prog_list = sorted(list(set([x[0][:4] for x in data])))

    context = {
            'username' : 'vgs',
            # 'line': dropdown_chart(),
            'projlist': {'PROG': [x[0][:4] for x in data],
                         'PROJ': [x[0] for x in data],
                         'DESC': [x[1] for x in data],
            },
            'prog_list': prog_list,
        }
    return render(request, 'minato/jquery_learn.html', context)

@login_required
def job_tracker(request):

    applied_cat = [x[0] for x in JobTrackerEntry.STATUS_CHOICES]
    jobs_applied = JobTrackerEntry.objects.all().order_by('-applied_on')
    form = JobTrackerEntryForm()

    context = {
        'jobs_applied' : jobs_applied,
        'applied_cat' : applied_cat,
        'form': form,
    }

    return render(request, 'minato/job_tracker.html', context)

@login_required
def update_item_status(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        applied_id = data.get('id')
        new_status = data.get('status')
        print(new_status)
        item = JobTrackerEntry.objects.get(id=applied_id)
        item.status = new_status
        item.save()

        return JsonResponse({'success' : True})
    return JsonResponse({'success' : False}, status=400)

def profexp(request):
    return render(request, 'minato/profexp.html')

def reading(request):

    books_all = BookTrackerEntry.objects.all()

    context = {
        'books_all' : books_all,
    }

    return render(request, 'minato/reading.html', context)



