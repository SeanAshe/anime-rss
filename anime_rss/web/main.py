from nicegui import ui

@ui.refreshable
@ui.page('/')
def ShowHomePage():
    ui.label('CONTENT')
    [ui.label(f'Line {i}') for i in range(100)]
    ##########################################
    
    # 头部
    with ui.header(elevated=True,bordered=True).style('background-color: #3874c8;height:100px').classes('items-center justify-between'):
        ui.label('HEADER')
    # 左边
    with ui.left_drawer(top_corner=True, bottom_corner=True).classes('w-[400px]'):
        ui.label('LEFT DRAWER')
