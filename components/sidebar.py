from state import *
import solara

"""
Contains the program wide sidebar definition
e.g. data upload etc...
"""

@solara.component
def Sidebar():
    data = State.dataframe.value
    with solara.AppBar():
        solara.lab.ThemeToggle()
    with solara.Sidebar():
        with solara.Card("Data upload", margin=1, elevation=1):
            with solara.Row(margin=3):
                if 0 < State.upload_progress.value < 100:
                    solara.ProgressLinear(value=State.upload_progress.value)
                else:
                    solara.ProgressLinear(False)
            with solara.Column():
                with solara.Row():
                    solara.Button("Clear datasets", color="primary", text=True, outlined=True, on_click=State.reset, disabled=data is None)
                solara.FileDrop(on_file=State.load_from_file, on_total_progress=State.upload_progress.set, label=State.path.value)
