import pandas as pd
import matplotlib.pyplot as plt

backtracking_df = pd.read_csv('backtracking_results.csv')
las_vegas_df = pd.read_csv('las_vegas_results.csv')

backtracking_df.columns = ['n', 'backtracking_attempts']
las_vegas_df.columns = ['n', 'lv_attempts']

combined_df = pd.merge(backtracking_df, las_vegas_df, on='n', how='outer')

print(combined_df)

plt.figure(figsize=(10, 6))

plt.plot(combined_df['n'], combined_df['backtracking_attempts'], marker='o', label='Backtracking', linestyle='-', color='blue')

plt.plot(combined_df['n'], combined_df['lv_attempts'], marker='o', label='Modified Las Vegas', linestyle='-', color='orange')
plt.title('N-Queens Problem: Attempts Comparison')
plt.xlabel('N (Board Size)')
plt.ylabel('Number of Attempts Board State Checked')
plt.xticks(combined_df['n']) 
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
plot_filename = 'nqueens_attempts_comparison.png' 
# plt.savefig(plot_filename)
# combined_df.to_csv('combined_nqueens_results.csv', index=False)

print("Combined results have been saved to 'combined_nqueens_results.csv'")