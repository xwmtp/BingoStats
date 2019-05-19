import dash_table

def get_bingo_table(player, colors):

    df = player.get_pandas_table()

    table = dash_table.DataTable(
        id = 'table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),

        style_table = {
                'maxHeight' : 500
        },
        n_fixed_rows=1,
        style_header={'backgroundColor': colors['background'],
                     'color': 'white',
                      'font-family': 'Calibri'
                    },
        style_cell = {'backgroundColor' : colors['background'],
                      'color' : 'white',
                      'textAlign' : 'left',
                      'minWidth' : '100px',
                      'font-family': 'Calibri'
        },
        style_cell_conditional=[
            {
                'if': {'column_id': c},
                'minWidth': '70px'
            } for c in ['Rank', 'Entrants']

        ],

        style_as_list_view=True,

        sorting = True,

        pagination_mode = False
    )

    return table