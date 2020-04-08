import matplotlib.pyplot as plt 
from matplotlib.widgets import Slider

g = 1.28

k = 0.004 # carrying capacity
def next(p, growth):
    return growth*p*(1-p/k)

def simulate(harvest, off_harvest, r):
    data = []
    p = 0.0001
    y = 50 
    period = harvest + off_harvest
    for i in range(y):
        data += [p]
        p = next(p, g - r if (i % period) < harvest else g)
    return range(y), data

config = {
"harvest" : 5, 
"off_harvest" : 2, 
"rate" : 0.7,
}

def updater(k, fig, p, ax):
    def update(v):
        config[k] = v
        xs, ys = simulate(config["harvest"], config["off_harvest"], config["rate"])
        p.set_ydata(ys)
        ax.set_ybound(0, max(ys)*1.1)
        fig.canvas.draw_idle()
    return update

fig, ax = plt.subplots()
ax.set_xlabel("Number of years")
ax.set_ylabel("Wolf density (n/sq. km)")
years, wolves = simulate(config["harvest"], config["off_harvest"], config["rate"])
plt.title("Wolf Density as a Function of Different Harvests")
plt.subplots_adjust(left = 0.2, bottom = 0.45)
p, = plt.plot(years, wolves, linewidth=2, color='blue')
# print(p)


slider_harvest = Slider(
    ax = plt.axes([0.2, 0.3, 0.7, 0.05]),
    label = "Harvest Years",
    valmin = 0,
    valmax = 12,
    valinit = config["harvest"],
    valstep = 1
    )
slider_harvest.on_changed(updater("harvest", fig, p, ax))

slider_off = Slider(
    ax = plt.axes([0.2, 0.2, 0.7, 0.05]),
    label = "Off years",
    valmin = 0,
    valmax = 12 ,
    valinit = config["off_harvest"],
    valstep = 1
    )
slider_off.on_changed(updater("off_harvest", fig, p, ax))

slider_rate = Slider(
    ax = plt.axes([0.2, 0.1, 0.7, 0.05]),
    label = "Cull",
    valmin = 0,
    valmax = 1,
    valinit = config["rate"]
    )
slider_rate.on_changed(updater("rate", fig, p, ax))

plt.show()

# plt.show()