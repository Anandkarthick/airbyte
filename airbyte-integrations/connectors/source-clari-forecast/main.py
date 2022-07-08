#
# Copyright (c) 2022 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_clari_forecast import SourceClariForecast

if __name__ == "__main__":
    source = SourceClariForecast()
    launch(source, sys.argv[1:])
