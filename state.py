from pandas import DataFrame
from typing import Optional, cast
import solara, pandas as pd, pickle

"""
Contains the program wide state; such as global variables and static (stateful) methods
"""

class State:

    data_size = solara.reactive(0)
    processed = solara.reactive(0)
    processing = solara.reactive(False)

    drag_placeholder = "Drag file here"

    ## Data upload fields
    path = solara.reactive(cast(Optional[str], drag_placeholder))
    upload_progress = solara.reactive(cast(Optional[int], 0))

    ## General data fields
    dataframe = solara.reactive(cast(Optional[DataFrame], None))
    chosen_column = solara.reactive(cast(Optional[str],None))
    error = solara.reactive(cast(Optional[str],None))

    @staticmethod
    def reset_progress():
        State.processing.value = False
        State.processed.value = 0
        State.data_size.value = 0

    @staticmethod
    def load_from_file(file):
        State.error.value = None
        df = None
        if file['name'].endswith('csv'):
            df = pd.read_csv(file["file_obj"])
        elif file['name'].endswith('.p'):
            df = pickle.load(file['file_obj'])
        else:
            State.error.value = "The uploading file-type needs to be csv or pickle .p"
        if df is not None:
            State.dataframe.set(df)

    @staticmethod
    def reset():
        State.path.value = State.drag_placeholder
        State.dataframe.set(None)

    @staticmethod
    def reset_column():
        State.chosen_column.set(None)
