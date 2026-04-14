import pandas as pd

# Load IPL data
deliveries = pd.read_csv('deliveries.csv')

print("Column names found:")
print(deliveries.columns.tolist()[:10]) 

print("\n📊 Dataset info:")
print(f"Rows: {len(deliveries):,}, Columns: {len(deliveries.columns)}")

# Find batting-related columns automatically
batting_cols = [col for col in deliveries.columns if any(x in col.lower() for x in ['bat', 'strike', 'player'])]
print(f"\nBatting columns: {batting_cols}")

# Safe top performers analysis
if 'striker' in deliveries.columns:
    top_batsmen = deliveries.groupby('striker')['runs_off_bat'].sum().sort_values(ascending=False).head(10)
    print("\n🏏 Top Batsmen:")
    print(top_batsmen)
elif 'batsman' in deliveries.columns:
    top_batsmen = deliveries.groupby('batsman')['runs_off_bat'].sum().sort_values(ascending=False).head(10)
    print("\n🏏 Top Batsmen:")
    print(top_batsmen)
else:
    print("\nNo standard batsman column found. Check batting_team above.")

print("\n✅ Ready for full IPL analysis!")



import matplotlib.pyplot as plt
top_batsmen.plot(kind='bar', title='Top 10 IPL Batsmen')
plt.tight_layout()
plt.savefig('top_batsmen.png')
plt.show()