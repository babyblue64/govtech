#! /usr/bin/env python3

from database import Base, engine # Import your Base from models.py
from sqlalchemy_schemadisplay import create_schema_graph

# Directly use your existing metadata
graph = create_schema_graph(
    metadata=Base.metadata,
    engine=engine,
    show_datatypes=False,
    show_indexes=False,
    rankdir='LR'
)

graph.write_png('models_erd.png')
print("ERD generated as: models_erd.png")