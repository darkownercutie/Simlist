import pandas as pd

simpsons_episodes_list = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes')[0]

simpsons_episodes_list.to_csv('simlist.csv')