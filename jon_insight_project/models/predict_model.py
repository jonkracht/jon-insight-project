import matplotlib.pyplot as plt
import osmnx as ox
from descartes import PolygonPatch
from shapely.geometry import Polygon, MultiPolygon
ox.config(log_console=True, use_cache=True)
ox.__version__




# get the place shape
#gdf = ox.gdf_from_place('Portland, Maine')
gdf = ox.project_gdf(gdf)

# get the street network, with retain_all=True to retain all the disconnected islands' networks
G = ox.graph_from_place('Portland, Maine', network_type='drive', retain_all=True)
G = ox.project_graph(G)

fig, ax = ox.plot_graph(G, fig_height=10, show=False, close=False, edge_color='#777777')
plt.show()

plt.close()



# to this matplotlib axis, add the place shape as descartes polygon patches
for geometry in gdf['geometry'].tolist():
    if isinstance(geometry, (Polygon, MultiPolygon)):
        if isinstance(geometry, Polygon):
            geometry = MultiPolygon([geometry])
        for polygon in geometry:
            patch = PolygonPatch(polygon, fc='#cccccc', ec='k', linewidth=3, alpha=0.1, zorder=-1)
            ax.add_patch(patch)


# optionally set up the axes extents all nicely
margin = 0.02
west, south, east, north = gdf.unary_union.bounds
margin_ns = (north - south) * margin
margin_ew = (east - west) * margin
ax.set_ylim((south - margin_ns, north + margin_ns))
ax.set_xlim((west - margin_ew, east + margin_ew))
plt.show()

print('hi')