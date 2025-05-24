from pipeline_diagram import Digraph

# Create a directed graph
dot = Digraph(comment='Data Cleaning Pipeline', format='png')

# Add nodes with labels
dot.node('A', 'Raw Logs\n(JSON/XML/CSV)', shape='box', style='filled', fillcolor='#f9f9f9')
dot.node('B', 'Null Removal\n(Missing Value Imputation)', shape='box')
dot.node('C', 'Encoding\n(Label/One-Hot)', shape='box')
dot.node('D', 'Scaling\n(MinMax / Z-Score)', shape='box')
dot.node('E', 'Outlier Removal\n(IQR / Z-Score)', shape='box')
dot.node('F', 'Clean Structured\nDataFrame / CSV', shape='box', style='filled', fillcolor='#d1f0d1')

# Add edges between nodes
dot.edges(['AB', 'BC', 'CD', 'DE', 'EF'])

# Save and render
dot.render('data_cleaning_pipeline', view=True)  # This saves as .png
