from state import State
from components.sidebar import Sidebar
from components.scraper_options import ScraperOptions
from solara.lab import task
from tools.webscraping import scrape_main_content
import solara

"""
The main landing page that calls all page components and sidebar
"""
@solara.component
def Page():

    icon, set_icon = solara.use_state(True)

    data = State.dataframe.value

    Sidebar()

    with solara.lab.Tabs():
        with solara.lab.Tab("Scraper", icon_name="mdi-home" if icon else None):
            solara.Markdown(
                f"""
                ## Web scraper

                Select the column you wish to scrape and download the results
                """
            )
            if data is not None:
                with solara.Columns([2,1]):
                    with solara.Column():
                        solara.DataFrame(data)
                    with solara.Column():
                        ScraperOptions(data)



