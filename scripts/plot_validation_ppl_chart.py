import matplotlib.pyplot as plt

FPATH = '../validation_ppl_table.md'

steps = []
baseline = []
prenorm = []
postnorm = []

with open(FPATH, 'r', encoding='utf-8') as f:
    # Skip the first two header line
    next(f)
    next(f)
    for line in f:
        line = line.strip()
        if not line or line.startswith('|---'):
            continue
        parts = line.split('|')
        step_val = int(parts[1].strip())
        base_val = float(parts[2].strip())
        pre_val = float(parts[3].strip())
        post_val = float(parts[4].strip())

        steps.append(step_val)
        baseline.append(base_val)
        prenorm.append(pre_val)
        postnorm.append(post_val)

#  Plotting the line chart
plt.figure(figsize=(10, 6))
plt.plot(steps, baseline,  label='Baseline', color='tab:blue')
plt.plot(steps, prenorm,   label='Prenorm',  color='tab:orange')
plt.plot(steps, postnorm,  label='Postnorm', color='tab:green')

plt.xlabel('Steps')
plt.ylabel('Validation PPL')
plt.title('Validation PPL over Steps for Different Models')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('../validation_ppl-chart.png', dpi=300)
plt.show()