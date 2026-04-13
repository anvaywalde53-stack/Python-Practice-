import pandas as pd
import matplotlib.pyplot as plt

# Load recruitment data
df_recruit = pd.read_csv('recruitments_data.csv')
# Sorting for better visualization in bar charts
df_sorted = df_recruit.sort_values(by='Recruits', ascending=False)

# a) Bar Chart
plt.bar(df_sorted['Company'], df_sorted['Recruits'], color='teal')
plt.xticks(rotation=45)
plt.ylabel('Number of New Recruits')
plt.title('Corporate Recruitment Drive Statistics')
plt.savefig('recruitments_bar.png')
plt.clf()

# b) Pie Chart
plt.pie(df_sorted['Recruits'], labels=df_sorted['Company'], autopct='%1.1f%%')
plt.title('Recruitment Distribution by Company')
plt.savefig('recruitments_pie.png')
plt.clf()

# c) Customized Pie Chart (Exploded and Shadowed)
# Highlighting IBM and Amdocs for comparison
explode_list = [0.15 if c in ['IBM', 'Amdocs'] else 0 for c in df_sorted['Company']]
plt.pie(df_sorted['Recruits'], labels=df_sorted['Company'], autopct='%1.1f%%', 
        explode=explode_list, shadow=True, startangle=140)
plt.title('Customized View: Recruitment Shares')
plt.savefig('recruitments_custom_pie.png')
plt.clf()

# d) Doughnut Chart
plt.pie(df_sorted['Recruits'], labels=df_sorted['Company'], autopct='%1.1f%%', 
        wedgeprops={'width': 0.4, 'edgecolor': 'w'})
plt.title('Recruitment Overview (Doughnut)')
plt.savefig('recruitments_doughnut.png')
plt.clf()

# Comparison: IBM & Amdocs
comp_df = df_recruit[df_recruit['Company'].isin(['IBM', 'Amdocs'])]
plt.bar(comp_df['Company'], comp_df['Recruits'], color=['navy', 'forestgreen'])
plt.ylabel('Recruits')
plt.title('Direct Comparison: IBM vs Amdocs')
plt.savefig('ibm_amdocs_comparison.png')
plt.clf()
