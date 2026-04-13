import pandas as pd

data = {
    'State': ['Maharashtra', 'Rajasthan', 'Uttar Pradesh', 'Goa', 'Madhya Pradesh'],
    'Area': [307713, 342239, 240928, 3702, 308245],
    'Population': [112374333, 68548437, 199812341, 1458545, 72626809]
}

df_states = pd.DataFrame(data)

print("a) Complete Information of States:")
print(df_states.to_string(index=False))

largest_area_state = df_states.loc[df_states['Area'].idxmax(), 'State']
print(f"\nb) State with largest Area: {largest_area_state}")

largest_pop_state = df_states.loc[df_states['Population'].idxmax(), 'State']
print(f"c) State with largest Population: {largest_pop_state}")

df_states['Population_Density'] = df_states['Population'] / df_states['Area']
print("\nd) Population Density calculated:")
print(df_states[['State', 'Population_Density']].to_string(index=False))

highest_density_state = df_states.loc[df_states['Population_Density'].idxmax(), 'State']
print(f"\ne) State with highest Population Density: {highest_density_state}")
