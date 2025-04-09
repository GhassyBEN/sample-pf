"""Module providing a function printing python version."""

import math
import os

import pandas as pd
import requests


class ProjectTimelines:
    """class representing a project timelines between dev/const/op"""

    def __init__(self, dsd, dp, cp, op, mpcod=1, mtcod=3):
        # have it a dataframe
        self.dsd = dsd
        self.dp = dp
        self.cp = cp
        self.op = op
        self.mpcod = mpcod
        self.mtcod = mtcod

    def get_url(self, url):
        """_summary_

        Args:
            url (_type_): _description_

        Returns:
            _type_: _description_
        """
        r = requests.get(
            url=url,
            timeout=10,
        )
        return r.status_code

    @property
    def df(self):
        """function calculaing the timelines dataframe inputs"""
        df = pd.DataFrame(
            index=["dsd", "dp", "cp", "op", "mpcod", "mtcod"],
            data=[self.dsd, self.dp, self.cp, self.op, self.mpcod, self.mtcod],
        )

        # function calculaing the Fiscal Close
        fc = 1

        # function calculaing the Commercial Operarting Date
        cod = 1

        # function calculaing the Decommissining Date
        dd = 1

        # function calculaing the ....
        mefy = 1

        # function calculaing the ....
        tppcod = 1

        # function calculaing the ..."""
        tpscod = 1

        df[
            "fc",
        ] = fc
        df["cod"] = cod
        df["dd"] = dd
        df["mefy"] = mefy
        df["tppcod"] = tppcod
        df["tpscod"] = tpscod

        return df
