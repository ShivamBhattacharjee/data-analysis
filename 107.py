import pandas as pd
import csv
import plotly.express as px 
import plotly.graph_objects as go

df=pd.read_csv("pixelMaths.csv")
print(df.groupby("level")["attempt"].mean())
fig=go.Figure(go.Bar(
    x=df.groupby("level")["attempt"].mean(),
    y=["Level 1","Level 2","Level 3","Level 4"],
    orientation="h"
))
fig.show()

studentDf=df.loc[df["student_id"]=="TRL_abc"]
print(studentDf.groupby("level")["attempt"].mean())
fig=go.Figure(go.Bar(
    x=studentDf.groupby("level")["attempt"].mean(),
    y=["Level 1","Level 2","Level 3","Level 4"],
    orientation="h" 
))
fig.show()

#project
mean=df.groupby(["student_id","level"],as_index=False)["attempt"].mean()
fig2=px.scatter(mean,x="student_id",y="level",size="attempt",color="attempt")
fig2.show()

