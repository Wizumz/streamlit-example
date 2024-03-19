import pandas as pd
import streamlit as st
import dataretrieval.nwis as nwis

site = '410729073171701'

# get instantaneous values (iv)
df = nwis.get_record(sites=site, service='iv', start='2023-12-31', end='2024-03-18')

# get water quality samples (qwdata)
df2 = nwis.get_record(sites=site, service='qwdata', start='2023-12-31', end='2024-03-18')

# get basic info about the site
df3 = nwis.get_record(sites=site, service='site')
