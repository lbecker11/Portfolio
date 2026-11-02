import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

df = pd.read_csv(r"C:\Users\becke\Desktop\GitHub\MarketScreener\output\reports\yearly_summary.csv")

# Drop partial year
df = df[df['Year'] < 2026].copy()

years      = df['Year'].astype(int).tolist()
strategy   = df['Return (%)'].tolist()
sp500      = df['SP500 Return (%)'].tolist()

x     = np.arange(len(years))
width = 0.38

# ── Figure ────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(13, 5))
fig.patch.set_facecolor('#0c0c0c')
ax.set_facecolor('#0c0c0c')

bars_s = ax.bar(x - width / 2, strategy, width, color='#5a9e6f', label='Strategy', zorder=3)
bars_b = ax.bar(x + width / 2, sp500,    width, color='#a8c5da', alpha=0.6, label='S&P 500', zorder=3)

# Zero line
ax.axhline(0, color='#333333', linewidth=0.8, zorder=2)

# ── Labels & ticks ────────────────────────────────────────────────────────────
ax.set_xticks(x)
ax.set_xticklabels(years, rotation=45, ha='right',
                   color='#666666', fontfamily='monospace', fontsize=8)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f'{v:.0f}%'))
ax.tick_params(axis='y', colors='#666666', labelsize=9)
ax.tick_params(axis='x', length=0)

ax.set_ylabel('Return (%)', color='#666666', fontfamily='monospace', fontsize=10, labelpad=10)
ax.set_title('Yearly Returns  //  Strategy vs S&P 500',
             color='#e2e2e2', fontfamily='monospace', fontsize=11, pad=14)

# ── Grid ──────────────────────────────────────────────────────────────────────
ax.yaxis.grid(True, color='#1a1a1a', linewidth=0.7, zorder=1)
ax.set_axisbelow(True)

for spine in ax.spines.values():
    spine.set_visible(False)

# ── Legend ────────────────────────────────────────────────────────────────────
legend = ax.legend(frameon=False, labelcolor='#666666',
                   prop={'family': 'monospace', 'size': 9},
                   loc='upper right')

plt.tight_layout()
plt.savefig('yearly_returns.png', dpi=150, bbox_inches='tight', facecolor='#0c0c0c')
plt.show()
print('Saved: yearly_returns.png')
