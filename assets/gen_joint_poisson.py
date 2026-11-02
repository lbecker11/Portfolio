import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from scipy.stats import poisson
from scipy.special import gammaln

# ── Parameters ────────────────────────────────────────────────────────────────
lambda_home = 1.5
lambda_away = 1.1
max_goals   = 5

goals = np.arange(max_goals + 1)

# Continuous extension of Poisson PMF via gamma function — gives a smooth surface
def poisson_cont(x, lam):
    return np.exp(-lam + x * np.log(lam) - gammaln(x + 1))

# Fine grid for the mountain surface
fine       = np.linspace(0, max_goals, 80)
Xf, Yf    = np.meshgrid(fine, fine)   # Xf = home goals, Yf = away goals
Zf        = poisson_cont(Xf, lambda_home) * poisson_cont(Yf, lambda_away)

# Discrete marginals for the wall curves
home_pmf   = poisson.pmf(goals, lambda_home)
away_pmf   = poisson.pmf(goals, lambda_away)

# ── Colors ────────────────────────────────────────────────────────────────────
cmap = mcolors.LinearSegmentedColormap.from_list('site', ['#1a2e22', '#5a9e6f'])

# ── Figure ────────────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(10, 7))
fig.patch.set_facecolor('#0c0c0c')
ax  = fig.add_subplot(111, projection='3d')
ax.set_facecolor('#0c0c0c')

# ── Mountain surface ──────────────────────────────────────────────────────────
ax.plot_surface(Xf, Yf, Zf, cmap=cmap, alpha=0.93,
                linewidth=0, antialiased=True, rcount=80, ccount=80)

# ── Marginal curves on walls ──────────────────────────────────────────────────
# Home Poisson — projected onto the y = 0 wall
ax.plot(goals.astype(float), np.zeros(len(goals)), home_pmf,
        color='#a8c5da', lw=2.5, zorder=10)
# vertical drops to baseline
for g, p in zip(goals, home_pmf):
    ax.plot([g, g], [0, 0], [0, p], color='#a8c5da', lw=0.8, alpha=0.35)

# Away Poisson — projected onto the x = 0 wall
ax.plot(np.zeros(len(goals)), goals.astype(float), away_pmf,
        color='#a8c5da', lw=2.5, zorder=10)
for g, p in zip(goals, away_pmf):
    ax.plot([0, 0], [g, g], [0, p], color='#a8c5da', lw=0.8, alpha=0.35)

# ── Axes & labels ─────────────────────────────────────────────────────────────
ax.set_xlabel('\nHome Goals', color='#666666', fontfamily='monospace', fontsize=10)
ax.set_ylabel('\nAway Goals', color='#666666', fontfamily='monospace', fontsize=10)
ax.set_zlabel('\nP(i, j)',    color='#666666', fontfamily='monospace', fontsize=10)

ax.set_xticks(goals)
ax.set_yticks(goals)
ax.set_xticklabels(goals, color='#e2e2e2', fontfamily='monospace', fontsize=9)
ax.set_yticklabels(goals, color='#e2e2e2', fontfamily='monospace', fontsize=9)
ax.tick_params(axis='z', colors='#666666', labelsize=8)

# ── Panes & grid ─────────────────────────────────────────────────────────────
for pane in (ax.xaxis.pane, ax.yaxis.pane, ax.zaxis.pane):
    pane.fill = False
    pane.set_edgecolor('#222222')

ax.xaxis._axinfo['grid']['color'] = '#1a1a1a'
ax.yaxis._axinfo['grid']['color'] = '#1a1a1a'
ax.zaxis._axinfo['grid']['color'] = '#1a1a1a'

# ── Title ─────────────────────────────────────────────────────────────────────
ax.set_title(
    f'Joint Poisson Distribution  //  λ_h = {lambda_home},  λ_a = {lambda_away}',
    color='#e2e2e2', fontfamily='monospace', fontsize=11, pad=20
)

ax.view_init(elev=28, azim=-55)

plt.tight_layout()
plt.savefig('joint_poisson_3d.png', dpi=150, bbox_inches='tight', facecolor='#0c0c0c')
plt.show()
print('Saved: joint_poisson_3d.png')
