import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch

fig, ax = plt.subplots(figsize=(11, 4))
fig.patch.set_facecolor('#0c0c0c')
ax.set_facecolor('#0c0c0c')
ax.set_xlim(0, 10)
ax.set_ylim(0, 4)
ax.axis('off')

# ── Node definitions: (x_center, y_center, line1, line2) ─────────────────────
nodes = [
    (1.0,  2.0, 'NHS Jobs',     'Site'),
    (3.0,  2.0, 'Playwright',   'Scraper'),
    (5.0,  2.0, 'GitHub',       'Actions'),
    (7.0,  2.0, 'Meta',         'API'),
    (9.0,  2.0, 'WhatsApp',     'Notification'),
]

box_w = 1.4
box_h = 0.9

for i, (x, y, l1, l2) in enumerate(nodes):
    # Alternate subtle accent on the comment-green for first and last
    edge_color = '#5a9e6f' if i in (0, 4) else '#2a2a2a'
    rect = mpatches.FancyBboxPatch(
        (x - box_w / 2, y - box_h / 2), box_w, box_h,
        boxstyle='round,pad=0.05',
        linewidth=1.2,
        edgecolor=edge_color,
        facecolor='#141414',
        zorder=3
    )
    ax.add_patch(rect)

    ax.text(x, y + 0.12, l1, ha='center', va='center',
            color='#e2e2e2', fontfamily='monospace', fontsize=10, fontweight='500', zorder=4)
    ax.text(x, y - 0.18, l2, ha='center', va='center',
            color='#666666', fontfamily='monospace', fontsize=9, zorder=4)

# ── Arrows between nodes ──────────────────────────────────────────────────────
arrow_props = dict(
    arrowstyle='->', color='#5a9e6f',
    linewidth=1.2,
    mutation_scale=14
)

for i in range(len(nodes) - 1):
    x1 = nodes[i][0] + box_w / 2
    x2 = nodes[i + 1][0] - box_w / 2
    y0 = nodes[i][1]
    ax.annotate('', xy=(x2, y0), xytext=(x1, y0),
                arrowprops=dict(arrowstyle='->', color='#5a9e6f',
                                lw=1.2, mutation_scale=14),
                zorder=2)

# ── Labels below arrows ───────────────────────────────────────────────────────
arrow_labels = [
    (2.0, 'scrapes'),
    (4.0, 'triggers'),
    (6.0, 'calls'),
    (8.0, 'sends'),
]
for x, label in arrow_labels:
    ax.text(x, 1.62, label, ha='center', va='center',
            color='#444444', fontfamily='monospace', fontsize=8, zorder=4)

# ── Cron badge above GitHub Actions node ─────────────────────────────────────
ax.text(5.0, 3.05, '// cron schedule', ha='center', va='center',
        color='#5a9e6f', fontfamily='monospace', fontsize=8, zorder=4)

# ── Title ─────────────────────────────────────────────────────────────────────
ax.set_title('Job Messenger  //  Architecture',
             color='#e2e2e2', fontfamily='monospace', fontsize=11, pad=14)

plt.tight_layout()
plt.savefig('job_messenger.png', dpi=150, bbox_inches='tight', facecolor='#0c0c0c')
plt.show()
print('Saved: job_messenger.png')
