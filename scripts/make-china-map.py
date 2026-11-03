"""Build src/assets/china-map.svg from DataV province boundaries.

Usage:
  curl -o china.json https://geo.datav.aliyun.com/areas_v3/bound/100000_full.json
  python3 scripts/make-china-map.py china.json src/assets/china-map.svg

Albers projection, simplified outlines, Inner Mongolia (150000) highlighted, Baotou pinned,
South China Sea in an inset. After regenerating, the pin radii/label offset were enlarged by hand
(see git history of china-map.svg).
"""
import json, math, sys
src, out = sys.argv[1], sys.argv[2]
d = json.load(open(src))
# Albers equal-area conic for China
p1, p2, lat0, lon0 = map(math.radians, (25, 47, 0, 105))
n = (math.sin(p1) + math.sin(p2)) / 2
C = math.cos(p1) ** 2 + 2 * n * math.sin(p1)
r0 = math.sqrt(C - 2 * n * math.sin(lat0)) / n
def proj(lon, lat):
    lon, lat = math.radians(lon), math.radians(lat)
    r = math.sqrt(C - 2 * n * math.sin(lat)) / n
    t = n * (lon - lon0)
    return r * math.sin(t), r0 - r * math.cos(t)
def rdp(pts, eps):
    if len(pts) < 3: return pts
    (x1, y1), (x2, y2) = pts[0], pts[-1]
    dx, dy = x2 - x1, y2 - y1; L = math.hypot(dx, dy) or 1e-12
    dmax, idx = 0, 0
    for i in range(1, len(pts) - 1):
        x0, y0 = pts[i]
        dist = abs(dy * x0 - dx * y0 + x2 * y1 - y2 * x1) / L
        if dist > dmax: dmax, idx = dist, i
    if dmax > eps:
        return rdp(pts[:idx + 1], eps)[:-1] + rdp(pts[idx:], eps)
    return [pts[0], pts[-1]]
def rdp_ring(pts, eps):
    if len(pts) > 1 and pts[0] == pts[-1]: pts = pts[:-1]
    if len(pts) < 4: return pts
    far = max(range(len(pts)), key=lambda i: (pts[i][0]-pts[0][0])**2 + (pts[i][1]-pts[0][1])**2)
    a = rdp(pts[:far + 1], eps); b = rdp(pts[far:] + [pts[0]], eps)
    return a[:-1] + b[:-1]
def rings(geom):
    if geom['type'] == 'Polygon': return [geom['coordinates'][0]]
    if geom['type'] == 'MultiPolygon': return [p[0] for p in geom['coordinates']]
    if geom['type'] == 'MultiLineString': return geom['coordinates']
    return []
# main frame: lat >= 17.5 (mainland, Hainan, Taiwan); inset: South China Sea
W = 600
allpts = [proj(lo, la) for f in d['features'] if f['geometry'] for r in rings(f['geometry']) for lo, la in r if la >= 17.5]
minx = min(p[0] for p in allpts); maxx = max(p[0] for p in allpts)
miny = min(p[1] for p in allpts); maxy = max(p[1] for p in allpts)
s = W / (maxx - minx); H = (maxy - miny) * s
def tx(p): return ((p[0] - minx) * s, (maxy - p[1]) * s)
# inset: lon 105.5-125, lat 2.5-24.5 scaled into a box bottom-right
ib = (105.5, 125.0, 2.5, 24.5)
ip = [proj(ib[0], ib[2]), proj(ib[1], ib[2]), proj(ib[0], ib[3]), proj(ib[1], ib[3])]
iminx = min(p[0] for p in ip); imaxx = max(p[0] for p in ip); iminy = min(p[1] for p in ip); imaxy = max(p[1] for p in ip)
IW = W * 0.14; isc = IW / (imaxx - iminx); IH = (imaxy - iminy) * isc
WT = W + 44
ix0, iy0 = WT - IW - 2, H - IH - 2
def itx(p): return (ix0 + (p[0] - iminx) * isc, iy0 + (imaxy - p[1]) * isc)
def path(pts, closed=True):
    return 'M' + 'L'.join(f'{x:.1f},{y:.1f}' for x, y in pts) + ('Z' if closed else '')
main, imong, inset, dash = [], [], [], []
for f in d['features']:
    g = f['geometry']
    if not g: continue
    code = str(f['properties'].get('adcode'))
    for r in rings(g):
        if code == '100000_JD':
            pts = [itx(proj(lo, la)) for lo, la in r]
            dash.append(path(rdp_ring(pts, 0.15))); continue
        if all(la < 17.5 for lo, la in r):
            pts = [itx(proj(lo, la)) for lo, la in r]
            if len(pts) >= 3: inset.append(path(rdp_ring(pts, 0.05) if len(pts) > 4 else pts))
            continue
        pts = [tx(proj(lo, la)) for lo, la in r]
        simp = rdp_ring(pts, 0.6)
        if len(simp) < 4: continue
        (imong if code == '150000' else main).append(path(simp))
        # mainland shown faintly in the inset too
        if code in ('440000', '450000', '460000', '350000', '710000', '530000'):
            ipts = [itx(proj(lo, la)) for lo, la in r]
            inset.append(path(rdp_ring(ipts, 0.3)))
bx, by = tx(proj(109.84, 40.66))
svg = f'''<svg class="cmap" viewBox="0 0 {WT:.0f} {H:.0f}" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="cmap-t">
<title id="cmap-t">Map of China with Inner Mongolia outlined and Baotou marked</title>
<path class="cmap__land" d="{''.join(main)}"/>
<path class="cmap__nm" d="{''.join(imong)}"/>
<g class="cmap__inset"><rect x="{ix0:.1f}" y="{iy0:.1f}" width="{IW:.1f}" height="{IH:.1f}" rx="3"/><path class="cmap__land" d="{''.join(inset)}"/><path class="cmap__dash" d="{''.join(dash)}"/></g>
<g class="cmap__pin" transform="translate({bx:.1f} {by:.1f})"><circle class="cmap__halo" r="9"/><circle class="cmap__dot" r="4.5"/></g>
<text class="cmap__label" x="{bx + 12:.1f}" y="{by + 5:.1f}">Baotou 包头</text>
</svg>'''
open(out, 'w').write(svg)
print(f'{W}x{H:.0f}', len(svg), 'bytes')
