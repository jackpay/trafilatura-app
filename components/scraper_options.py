from tools.webscraping import scrape_main_content
from state import State
from solara.lab import task
import solara

placeholder = "-- PleaseSelect --"
default_output = "html/text"
output_col = solara.reactive(default_output)
column = solara.reactive(placeholder)

"""
A component that houses the scraper options, processing and download fields
"""

@solara.component
def ScraperOptions(data):

    if data is not None:
        with solara.Card("Scrape", margin=1, elevation=1):
            solara.ProgressLinear(value=State.processing.value)
            with solara.Row():
                solara.Markdown('''
                    Select the column housing the html, select scrape and download the results.
                ''')
            with solara.Row():
                with solara.Column():
                    solara.Select("HTML column", values=data.columns.to_list(), value=column)
                    solara.InputText("Output column name", value=output_col)
            with solara.Row():
                with solara.Column():
                    if column.value != placeholder:
                        solara.Button("Scrape", on_click=scrape_content)
            with solara.Row(margin=3):
                if scrape_content.finished:
                    solara.FileDownload(get_data, label=f"Download {len(data):,} records", filename="selected.csv")

@task
def scrape_content():
    data = State.dataframe.value
    if data is not None and column.value is not placeholder:
        State.data_size.value = len(data)
        data[output_col.value] = data[column.value].apply(lambda x: scrape_main_content(x, update_progress))
    State.reset_progress()

def update_progress():
    State.processed.value = State.processed.value + 1
    progress = (State.processed.value/State.data_size.value) * 100
    State.processing.value = progress


def get_data():
    data = State.dataframe.value
    return data.to_csv(index=False)