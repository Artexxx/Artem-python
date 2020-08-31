import seaborn as sns

cm = sns.light_palette("pink", as_cmap=True)


def hover(hover_color='#ffedf0'):
    """Подсвечивает строки (горизонталь)"""
    return dict(selector="tr:hover td", props=[("background-color", "%s" % hover_color)])


def hover2(hover_color="white"):
    """Подсвечивает индексы (слева)"""
    return dict(selector="tbody tr:hover th", props=[("background", "%s" % hover_color)])


def hover3(hover_color="#ffe2e7 !important"):
    """Подсвечивает каждую ячейку"""
    return dict(selector="th:hover, td:hover", props=[("background", "%s" % hover_color)])


th_props = [
    ('font-size', '11px'),
    ('text-align', 'center'),
    ('font-weight', 'bold'),
    ('color', '#2e2224'),
    ('background', '#fff3f5'),
]
td_props = [('font-size', '11px')]


def sprint(df,
           greenBars=[],
           orangeBars=[],
           redBars=[],
           format_in_percent=[],
           color_negative_red_set=[],
           redFlagValue=[],
           columnsNames=None,
           indexNames=None,
           ):
    sprint.redFlagValue = redFlagValue

    def color_negative_red(value, redFlagValue=sprint.redFlagValue):
        """!! Если текст всё-равно чёрный: проверьте тип колонки: >>> df.dtypes
        Если тип будет object: нужно передать параметр redFlagValue = ["No", "no", "false", "False"],
        слова из этого массива будут подсвечиваться красным, остальные зелёным.
        """
        if type(value) == int:
            if value < 0:
                color = 'red'
            elif value > 0:
                color = 'green'
            else:
                color = 'black'
        elif type(value) == bool or redFlagValue:
            if not value or value in redFlagValue:
                color = 'red'
            elif value:
                color = 'green'
            else:
                color = 'black'
        else:
            color = 'black'
        return 'color: %s' % color

    if "Series" in str(type(df)): df = df.to_frame()
    if columnsNames: df.columns = columnsNames
    if indexNames: df.index = indexNames

    int_type_names_columns_list = df.dtypes[df.dtypes != 'object'][df.dtypes != 'bool'].index

    cm_columns = [n for n in list(int_type_names_columns_list)
                  if n not in [*greenBars, *orangeBars, *redBars]]

    str_type_names_columns_list = set(n for n in list(df.dtypes[df.dtypes == 'bool'].index) + color_negative_red_set)

    styles = [hover(), hover2(), hover3(),
              dict(selector="th", props=th_props),
              dict(selector="td", props=td_props),
              ]

    return df.style.bar(subset=greenBars, color='lightgreen') \
        .bar(subset=redBars, color='#ee1f5f') \
        .bar(subset=orangeBars, color='#FFA07A') \
        .format({i: "{:.2%}" for i in format_in_percent}) \
        .applymap(color_negative_red, subset=list(str_type_names_columns_list)) \
        .set_table_styles(styles) \
        .background_gradient(cmap=cm, subset=cm_columns) \
        .highlight_max(color='#FFBCCF')
