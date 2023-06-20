"""
File: 
Name:
----------------------
TODO:


"""

from campy.graphics.gobjects import GOval, GRect, GLabel , GLine,GPolygon,GArc
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
window = GWindow(900, 500)


def main():
    """
    title: Whale shark
    I like diving. I think whale sharks are the cutest marine biology.
    """
    # onmouseclicked(pixel)
    background = GRect(900,500)
    background.filled = True
    background.fill_color = 'skyblue'
    background.color = 'skyblue'
    window.add(background)
    head = GOval(100, 120, x=114, y=144)
    head.filled = True
    head.fill_color = 'steelblue'
    head.color = 'steelblue'
    window.add(head)
    body = GPolygon()
    body.add_vertex((167, 144))
    body.add_vertex((167, 264))
    body.add_vertex((272, 278))
    body.add_vertex((345, 266))
    body.add_vertex((345, 142))
    body.add_vertex((306, 142))
    body.filled = True
    body.fill_color = 'steelblue'
    body.color = 'steelblue'
    window.add(body)
    body2 = GPolygon()
    body2.add_vertex((322, 149))
    body2.add_vertex((345, 142))
    body2.add_vertex((682, 194))
    body2.add_vertex((682, 221))
    body2.add_vertex((481, 240))
    body2.add_vertex((345, 266))
    body2.filled = True
    body2.fill_color = 'steelblue'
    body2.color = 'steelblue'
    window.add(body2)
    body3 = GPolygon()
    body3.add_vertex((151, 145))
    body3.add_vertex((127, 160))
    body3.add_vertex((120, 167))
    body3.add_vertex((114, 203))
    body3.filled = True
    body3.fill_color = 'steelblue'
    body3.color = 'steelblue'
    window.add(body3)
    caudal_fin = GPolygon()
    caudal_fin.add_vertex((681, 195))
    caudal_fin.add_vertex((760, 67))
    caudal_fin.add_vertex((761, 68))
    caudal_fin.add_vertex((736, 208))
    caudal_fin.add_vertex((681, 208))
    caudal_fin.filled = True
    caudal_fin.fill_color = 'steelblue'
    caudal_fin.color = 'steelblue'
    window.add(caudal_fin)
    caudal_fin2 = GPolygon()
    caudal_fin2.add_vertex((681, 208))
    caudal_fin2.add_vertex((736, 208))
    caudal_fin2.add_vertex((777, 281))
    caudal_fin2.add_vertex((681, 220))
    caudal_fin2.filled = True
    caudal_fin2.fill_color = 'steelblue'
    caudal_fin2.color = 'steelblue'
    window.add(caudal_fin2)
    dorsal_fin = GPolygon()
    dorsal_fin.add_vertex((368, 145))
    dorsal_fin.add_vertex((417, 121))
    dorsal_fin.add_vertex((471, 86))
    dorsal_fin.add_vertex((472, 95))
    dorsal_fin.add_vertex((475, 135))
    dorsal_fin.add_vertex((484, 166))
    dorsal_fin.filled = True
    dorsal_fin.fill_color = 'steelblue'
    dorsal_fin.color = 'steelblue'
    window.add(dorsal_fin)
    dorsal_fin2 = GPolygon()
    dorsal_fin2.add_vertex((541, 171))
    dorsal_fin2.add_vertex((572, 162))
    dorsal_fin2.add_vertex((601, 150))
    dorsal_fin2.add_vertex((605, 151))
    dorsal_fin2.add_vertex((618, 185))
    dorsal_fin2.filled = True
    dorsal_fin2.fill_color = 'steelblue'
    dorsal_fin2.color = 'steelblue'
    window.add(dorsal_fin2)
    pectoral_fin = GPolygon()
    pectoral_fin.add_vertex((271, 279))
    pectoral_fin.add_vertex((343, 347))
    pectoral_fin.add_vertex((370, 359))
    pectoral_fin.add_vertex((374, 359))
    pectoral_fin.add_vertex((380, 347))
    pectoral_fin.add_vertex((382, 338))
    pectoral_fin.add_vertex((369, 308))
    pectoral_fin.add_vertex((359, 260))
    pectoral_fin.filled = True
    pectoral_fin.fill_color = 'steelblue'
    pectoral_fin.color = 'steelblue'
    window.add(pectoral_fin)
    pelvic_fin = GPolygon()
    pelvic_fin.add_vertex((454, 243))
    pelvic_fin.add_vertex((483, 262))
    pelvic_fin.add_vertex((485, 260))
    pelvic_fin.add_vertex((490, 239))
    pelvic_fin.filled = True
    pelvic_fin.fill_color = 'steelblue'
    pelvic_fin.color = 'steelblue'
    window.add(pelvic_fin)
    pelvic_fin1 = GPolygon()
    pelvic_fin1.add_vertex((544, 232))
    pelvic_fin1.add_vertex((566, 249))
    pelvic_fin1.add_vertex((568, 251))
    pelvic_fin1.add_vertex((576, 229))
    pelvic_fin1.filled = True
    pelvic_fin1.fill_color = 'steelblue'
    pelvic_fin1.color = 'steelblue'
    window.add(pelvic_fin1)
    pelvic_fin2 = GPolygon()
    pelvic_fin2.add_vertex((589, 228))
    pelvic_fin2.add_vertex((608, 246))
    pelvic_fin2.add_vertex((610, 246))
    pelvic_fin2.add_vertex((616, 224))
    pelvic_fin2.filled = True
    pelvic_fin2.fill_color = 'steelblue'
    pelvic_fin2.color = 'steelblue'
    window.add(pelvic_fin2)
    gill = GArc(40, 40, 120, 150)
    gill.color = 'darkslategrey'
    window.add(gill, x=233, y=227)
    gill1= GArc(40,40,120,150)
    gill1.color = 'darkslategrey'
    window.add(gill1,x=240,y=227)
    gill2 = GArc(40, 40, 120, 150)
    gill2.color = 'darkslategrey'
    window.add(gill2, x=248, y=227)
    gill3 = GArc(40, 40, 120, 150)
    gill3.color = 'darkslategrey'
    window.add(gill3, x=255, y=227)
    gill4 = GArc(40, 40, 120, 150)
    gill4.color = 'darkslategrey'
    window.add(gill4, x=263, y=227)
    lateral_line = GLine(294,168,364,166)
    lateral_line.color = 'midnightblue'
    window.add(lateral_line)
    lateral_line1 = GLine(364, 166, 681, 200)
    lateral_line1.color = 'midnightblue'
    window.add(lateral_line1)
    lateral_line2 = GLine(279, 188, 365, 184)
    lateral_line2.color = 'midnightblue'
    window.add(lateral_line2)
    lateral_line3 = GLine(365, 184, 681, 204)
    lateral_line3.color = 'midnightblue'
    window.add(lateral_line3)
    lateral_line4 = GLine(322, 209, 380, 203)
    lateral_line4.color = 'midnightblue'
    window.add(lateral_line4)
    lateral_line5 = GLine(380, 203, 681, 207)
    lateral_line5.color = 'midnightblue'
    window.add(lateral_line5)
    lateral_line6 = GLine(376, 223, 681, 211)
    lateral_line6.color = 'midnightblue'
    window.add(lateral_line6)
    caudal_finw = GPolygon()
    caudal_finw.add_vertex((681, 194))
    caudal_finw.add_vertex((760, 66))
    caudal_finw.add_vertex((688, 191))
    caudal_finw.filled = True
    caudal_finw.fill_color = 'antiquewhite'
    caudal_finw.color = 'antiquewhite'
    window.add(caudal_finw)
    dorsal_finw = GPolygon()
    dorsal_finw.add_vertex((369, 145))
    dorsal_finw.add_vertex((469, 86))
    dorsal_finw.add_vertex((382, 147))
    dorsal_finw.filled = True
    dorsal_finw.fill_color = 'antiquewhite'
    dorsal_finw.color = 'antiquewhite'
    window.add(dorsal_finw)
    dorsal_finw1 = GPolygon()
    dorsal_finw1.add_vertex((541, 171))
    dorsal_finw1.add_vertex((572, 160))
    dorsal_finw1.add_vertex((603, 150))
    dorsal_finw1.add_vertex((559, 171))
    dorsal_finw1.filled = True
    dorsal_finw1.fill_color = 'antiquewhite'
    dorsal_finw1.color = 'antiquewhite'
    window.add(dorsal_finw1)
    dorsal_find = GPolygon()
    dorsal_find.add_vertex((471, 85))
    dorsal_find.add_vertex((476, 133))
    dorsal_find.add_vertex((485, 165))
    dorsal_find.add_vertex((469, 158))
    dorsal_find.filled = True
    dorsal_find.fill_color = 'midnightblue'
    dorsal_find.color = 'midnightblue'
    window.add(dorsal_find)
    dorsal_finl = GLine(367, 145, 392, 148)
    dorsal_finl.color = 'midnightblue'
    window.add(dorsal_finl)
    dorsal_find1 = GPolygon()
    dorsal_find1.add_vertex((605, 150))
    dorsal_find1.add_vertex((618, 184))
    dorsal_find1.add_vertex((606, 178))
    dorsal_find1.filled = True
    dorsal_find1.fill_color = 'midnightblue'
    dorsal_find1.color = 'midnightblue'
    window.add(dorsal_find1)
    dorsal_finl1 = GLine(541, 172, 568, 174)
    dorsal_finl1.color = 'midnightblue'
    window.add(dorsal_finl1)
    caudal_find = GPolygon()
    caudal_find.add_vertex((760, 68))
    caudal_find.add_vertex((737, 200))
    caudal_find.add_vertex((778, 282))
    caudal_find.add_vertex((722, 206))
    caudal_find.filled = True
    caudal_find.fill_color = 'midnightblue'
    caudal_find.color = 'midnightblue'
    window.add(caudal_find)
    head_d = GPolygon()
    head_d.add_vertex((155, 263))
    head_d.add_vertex((143, 259))
    head_d.add_vertex((131, 250))
    head_d.add_vertex((185, 262))
    head_d.add_vertex((259, 262))
    head_d.add_vertex((278, 274))
    head_d.add_vertex((341, 347))
    head_d.add_vertex((272, 281))
    head_d.filled = True
    head_d.fill_color = 'antiquewhite'
    head_d.color = 'antiquewhite'
    window.add(head_d)
    head_finl = GLine(248, 261, 277, 259)
    head_finl.color = 'midnightblue'
    window.add(head_finl)
    body_d = GPolygon()
    body_d.add_vertex((357, 250))
    body_d.add_vertex((683, 220))
    body_d.add_vertex((362, 265))
    body_d.filled = True
    body_d.fill_color = 'antiquewhite'
    body_d.color = 'antiquewhite'
    window.add(body_d)
    eye2 = GOval(12, 12)
    eye2.filled = True
    eye2.fill_color = 'gray'
    eye2.color = 'gray'
    window.add(eye2, x=178, y=141)
    eye = GOval(10, 10)
    eye.filled = True
    eye.fill_color = 'black'
    eye.color = 'gray'
    window.add(eye, x=179, y=142)
    eye3 = GOval(12, 12)
    eye3.filled = True
    eye3.fill_color = 'gray'
    eye3.color = 'gray'
    window.add(eye2, x=183, y=254)
    eye1 = GOval(10, 10)
    eye1.filled = True
    eye1.fill_color = 'black'
    eye1.color = 'gray'
    window.add(eye1, x=184, y=255)
    po = GOval(13,13)
    po.filled = True
    po.fill_color = 'lightsteelblue'
    po.color ='lightsteelblue'
    window.add(po,x=279,y=149)
    poli = GArc(180, 180, 15, 50)
    poli.color = 'lightsteelblue'
    window.add(poli, x=256, y=142)
    po1 = GOval(13, 13)
    po1.filled = True
    po1.fill_color = 'lightsteelblue'
    po1.color = 'lightsteelblue'
    window.add(po1, x=310, y=148)
    poli1 = GArc(180, 180, 15, 50)
    poli1.color = 'lightsteelblue'
    window.add(poli1, x=286, y=141)
    po2 = GOval(13, 13)
    po2.filled = True
    po2.fill_color = 'lightsteelblue'
    po2.color = 'lightsteelblue'
    window.add(po2, x=340, y=147)
    poli2 = GArc(180, 180, 13, 48)
    poli2.color = 'lightsteelblue'
    window.add(poli2, x=322, y=141)
    po3 = GOval(12, 12)
    po3.filled = True
    po3.fill_color = 'lightsteelblue'
    po3.color = 'lightsteelblue'
    window.add(po3, x=368, y=149)
    poli3 = GArc(180, 180, 13, 48)
    poli3.color = 'lightsteelblue'
    window.add(poli3, x=347, y=144)
    po4 = GOval(12, 12)
    po4.filled = True
    po4.fill_color = 'lightsteelblue'
    po4.color = 'lightsteelblue'
    window.add(po4, x=394, y=151)
    poli4 = GArc(180, 180, 10, 45)
    poli4.color = 'lightsteelblue'
    window.add(poli4, x=380, y=146)
    po5 = GOval(12, 12)
    po5.filled = True
    po5.fill_color = 'lightsteelblue'
    po5.color = 'lightsteelblue'
    window.add(po5, x=422, y=154)
    poli5 = GArc(180, 180, 10, 45)
    poli5.color = 'lightsteelblue'
    window.add(poli5, x=408, y=149)
    po6 = GOval(11, 11)
    po6.filled = True
    po6.fill_color = 'lightsteelblue'
    po6.color = 'lightsteelblue'
    window.add(po6, x=448, y=158)
    poli6 = GArc(180, 180, 10, 40)
    poli6.color = 'lightsteelblue'
    window.add(poli6, x=438, y=152)
    po7 = GOval(10, 10)
    po7.filled = True
    po7.fill_color = 'lightsteelblue'
    po7.color = 'lightsteelblue'
    window.add(po7, x=477, y=165)
    poli7 = GLine(494, 168, 496, 177)
    poli7.color = 'lightsteelblue'
    window.add(poli7)
    po8 = GOval(8, 8)
    po8.filled = True
    po8.fill_color = 'lightsteelblue'
    po8.color = 'lightsteelblue'
    window.add(po8, x=507, y=170)
    poli8 = GLine(522, 170, 525, 179)
    poli8.color = 'lightsteelblue'
    window.add(poli8)
    po9 = GOval(7, 7)
    po9.filled = True
    po9.fill_color = 'lightsteelblue'
    po9.color = 'lightsteelblue'
    window.add(po9, x=535, y=174)
    poli9 = GLine(553, 176, 555, 182)
    poli9.color = 'lightsteelblue'
    window.add(poli9)
    po10 = GOval(6, 6)
    po10.filled = True
    po10.fill_color = 'lightsteelblue'
    po10.color = 'lightsteelblue'
    window.add(po10, x=564, y=177)
    poli10 = GLine(577, 176, 580, 184)
    poli10.color = 'lightsteelblue'
    window.add(poli10)
    po11 = GOval(5.5, 5.5)
    po11.filled = True
    po11.fill_color = 'lightsteelblue'
    po11.color = 'lightsteelblue'
    window.add(po11, x=588, y=180)
    poli11 = GLine(602, 179, 605, 188)
    poli11.color = 'lightsteelblue'
    window.add(poli11)
    po12 = GOval(4, 4)
    po12.filled = True
    po12.fill_color = 'lightsteelblue'
    po12.color = 'lightsteelblue'
    window.add(po12, x=614, y=185)
    poli12 = GLine(628, 185, 628, 191)
    poli12.color = 'lightsteelblue'
    window.add(poli12)
    po13 = GOval(3, 3)
    po13.filled = True
    po13.fill_color = 'lightsteelblue'
    po13.color = 'lightsteelblue'
    window.add(po13, x=635, y=188)
    poli13 = GLine(645, 188, 645, 194)
    poli13.color = 'lightsteelblue'
    window.add(poli13)
    po14 = GOval(2.5, 2.5)
    po14.filled = True
    po14.fill_color = 'lightsteelblue'
    po14.color = 'lightsteelblue'
    window.add(po14, x=655, y=191)
    poli14 = GLine(665, 191, 665, 196)
    poli14.color = 'lightsteelblue'
    window.add(poli14)
    po15 = GOval(2, 2)
    po15.filled = True
    po15.fill_color = 'lightsteelblue'
    po15.color = 'lightsteelblue'
    window.add(po15, x=672, y=194)
    po20 = GOval(11.5, 11.5)
    po20.filled = True
    po20.fill_color = 'lightsteelblue'
    po20.color = 'lightsteelblue'
    window.add(po20, x=287, y=172)
    poli20 = GArc(180, 180, 12, 30)
    poli20.color = 'lightsteelblue'
    window.add(poli20, x=290, y=167)
    po21 = GOval(11.5, 11.5)
    po21.filled = True
    po21.fill_color = 'lightsteelblue'
    po21.color = 'lightsteelblue'
    window.add(po21, x=320, y=170)
    poli21 = GArc(180, 180, 12, 30)
    poli21.color = 'lightsteelblue'
    window.add(poli21, x=321, y=166)
    po22 = GOval(11, 11)
    po22.filled = True
    po22.fill_color = 'lightsteelblue'
    po22.color = 'lightsteelblue'
    window.add(po22, x=348, y=170)
    poli22 = GArc(180, 180, 12, 30)
    poli22.color = 'lightsteelblue'
    window.add(poli22, x=348, y=164)
    po23 = GOval(10, 10)
    po23.filled = True
    po23.fill_color = 'lightsteelblue'
    po23.color = 'lightsteelblue'
    window.add(po23, x=375, y=171)
    poli23 = GArc(180, 180, 8, 28)
    poli23.color = 'lightsteelblue'
    window.add(poli23, x=377, y=165)
    po24 = GOval(9, 9)
    po24.filled = True
    po24.fill_color = 'lightsteelblue'
    po24.color = 'lightsteelblue'
    window.add(po24, x=403, y=174)
    poli24 = GArc(180, 180, 8, 28)
    poli24.color = 'lightsteelblue'
    window.add(poli24, x=407, y=168)
    po25 = GOval(7.5, 7.5)
    po25.filled = True
    po25.fill_color = 'lightsteelblue'
    po25.color = 'lightsteelblue'
    window.add(po25, x=429, y=177)
    poli25 = GArc(180, 180, 8, 28)
    poli25.color = 'lightsteelblue'
    window.add(poli25, x=429, y=170)
    po26 = GOval(7, 7)
    po26.filled = True
    po26.fill_color = 'lightsteelblue'
    po26.color = 'lightsteelblue'
    window.add(po26, x=453, y=179)
    poli26 = GArc(180, 180, 0, 26)
    poli26.color = 'lightsteelblue'
    window.add(poli26, x=461, y=169)
    po27 = GOval(6, 6)
    po27.filled = True
    po27.fill_color = 'lightsteelblue'
    po27.color = 'lightsteelblue'
    window.add(po27, x=480, y=182)
    poli27 = GLine(497, 182, 497, 190)
    poli27.color = 'lightsteelblue'
    window.add(poli27)
    po28 = GOval(5, 5)
    po28.filled = True
    po28.fill_color = 'lightsteelblue'
    po28.color = 'lightsteelblue'
    window.add(po28, x=509, y=185)
    poli28 = GLine(525, 185, 525, 192)
    poli28.color = 'lightsteelblue'
    window.add(poli28)
    po29 = GOval(4, 4)
    po29.filled = True
    po29.fill_color = 'lightsteelblue'
    po29.color = 'lightsteelblue'
    window.add(po29, x=538, y=188)
    poli29 = GLine(555, 190, 555, 194)
    poli29.color = 'lightsteelblue'
    window.add(poli29)
    po210 = GOval(3, 3)
    po210.filled = True
    po210.fill_color = 'lightsteelblue'
    po210.color = 'lightsteelblue'
    window.add(po210, x=565, y=191)
    poli210 = GLine(580, 192, 580, 196)
    poli210.color = 'lightsteelblue'
    window.add(poli210)
    po211 = GOval(2.5, 2.5)
    po211.filled = True
    po211.fill_color = 'lightsteelblue'
    po211.color = 'lightsteelblue'
    window.add(po211, x=590, y=193)
    poli211 = GLine(605, 193, 605, 198)
    poli211.color = 'lightsteelblue'
    window.add(poli211)
    po212 = GOval(2, 2)
    po212.filled = True
    po212.fill_color = 'lightsteelblue'
    po212.color = 'lightsteelblue'
    window.add(po212, x=616, y=196)
    poli212 = GLine(628, 197, 628, 200)
    poli212.color = 'lightsteelblue'
    window.add(poli212)
    po213 = GOval(2, 2)
    po213.filled = True
    po213.fill_color = 'lightsteelblue'
    po213.color = 'lightsteelblue'
    window.add(po213, x=635, y=197)
    poli213 = GLine(645, 198, 645, 202)
    poli213.color = 'lightsteelblue'
    window.add(poli213)
    po214 = GOval(2, 2)
    po214.filled = True
    po214.fill_color = 'lightsteelblue'
    po214.color = 'lightsteelblue'
    window.add(po214, x=655, y=199)
    poli214 = GLine(665, 200, 665, 203)
    poli214.color = 'lightsteelblue'
    window.add(poli214)
    po215 = GOval(2, 2)
    po215.filled = True
    po215.fill_color = 'lightsteelblue'
    po215.color = 'lightsteelblue'
    window.add(po215, x=672, y=200)
    po30 = GOval(11, 11)
    po30.filled = True
    po30.fill_color = 'lightsteelblue'
    po30.color = 'lightsteelblue'
    window.add(po30, x=292, y=193)
    poli30 = GArc(180, 180, 3, 30)
    poli30.color = 'lightsteelblue'
    window.add(poli30, x=300, y=185)
    po31 = GOval(11, 11)
    po31.filled = True
    po31.fill_color = 'lightsteelblue'
    po31.color = 'lightsteelblue'
    window.add(po31, x=324, y=191)
    poli31 = GArc(180, 180, 3, 30)
    poli31.color = 'lightsteelblue'
    window.add(poli31, x=330, y=182)
    po32 = GOval(10.5, 10.5)
    po32.filled = True
    po32.fill_color = 'lightsteelblue'
    po32.color = 'lightsteelblue'
    window.add(po32, x=352, y=189)
    poli32 = GArc(180, 180, 0, 30)
    poli32.color = 'lightsteelblue'
    window.add(poli32, x=360, y=178)
    po33 = GOval(9, 9)
    po33.filled = True
    po33.fill_color = 'lightsteelblue'
    po33.color = 'lightsteelblue'
    window.add(po33, x=378, y=190)
    poli33 = GArc(180, 180, 0, 28)
    poli33.color = 'lightsteelblue'
    window.add(poli33, x=384, y=180)
    po34 = GOval(8, 8)
    po34.filled = True
    po34.fill_color = 'lightsteelblue'
    po34.color = 'lightsteelblue'
    window.add(po34, x=405, y=191)
    poli34 = GArc(180, 180, 0, 25)
    poli34.color = 'lightsteelblue'
    window.add(poli34, x=415, y=182)
    po35 = GOval(7, 7)
    po35.filled = True
    po35.fill_color = 'lightsteelblue'
    po35.color = 'lightsteelblue'
    window.add(po35, x=431, y=193)
    poli35 = GArc(180, 180, 0, 25)
    poli35.color = 'lightsteelblue'
    window.add(poli35, x=438, y=183)
    po36 = GOval(6.5, 6.5)
    po36.filled = True
    po36.fill_color = 'lightsteelblue'
    po36.color = 'lightsteelblue'
    window.add(po36, x=454, y=194)
    poli36 = GArc(180, 180, 0, 23)
    poli36.color = 'lightsteelblue'
    window.add(poli36, x=463, y=184)
    po37 = GOval(5.5, 5.5)
    po37.filled = True
    po37.fill_color = 'lightsteelblue'
    po37.color = 'lightsteelblue'
    window.add(po37, x=480, y=195)
    poli37 = GLine(497, 195, 496, 203)
    poli37.color = 'lightsteelblue'
    window.add(poli37)
    po38 = GOval(4.5, 4.5)
    po38.filled = True
    po38.fill_color = 'lightsteelblue'
    po38.color = 'lightsteelblue'
    window.add(po38, x=509, y=197)
    poli38 = GLine(525, 196, 524, 203)
    poli38.color = 'lightsteelblue'
    window.add(poli38)
    po39 = GOval(3.5, 3.5)
    po39.filled = True
    po39.fill_color = 'lightsteelblue'
    po39.color = 'lightsteelblue'
    window.add(po39, x=538, y=198)
    poli39 = GLine(555, 198, 554, 204)
    poli39.color = 'lightsteelblue'
    window.add(poli39)
    po310 = GOval(2.5, 2.5)
    po310.filled = True
    po310.fill_color = 'lightsteelblue'
    po310.color = 'lightsteelblue'
    window.add(po310, x=565, y=200)
    poli310 = GLine(580, 200, 579, 205)
    poli310.color = 'lightsteelblue'
    window.add(poli310)
    po311 = GOval(2, 2)
    po311.filled = True
    po311.fill_color = 'lightsteelblue'
    po311.color = 'lightsteelblue'
    window.add(po311, x=590, y=201)
    poli311 = GLine(605, 201, 604, 205)
    poli311.color = 'lightsteelblue'
    window.add(poli311)
    po312 = GOval(2, 2)
    po312.filled = True
    po312.fill_color = 'lightsteelblue'
    po312.color = 'lightsteelblue'
    window.add(po312, x=616, y=202)
    poli312 = GLine(628, 203, 628, 205)
    poli312.color = 'lightsteelblue'
    window.add(poli312)
    po313 = GOval(2, 2)
    po313.filled = True
    po313.fill_color = 'lightsteelblue'
    po313.color = 'lightsteelblue'
    window.add(po313, x=635, y=203)
    poli313 = GLine(645, 203, 645, 206)
    poli313.color = 'lightsteelblue'
    window.add(poli313)
    po314 = GOval(1.5, 1.5)
    po314.filled = True
    po314.fill_color = 'lightsteelblue'
    po314.color = 'lightsteelblue'
    window.add(po314, x=655, y=204)
    poli314 = GLine(665, 204, 665, 206)
    poli314.color = 'lightsteelblue'
    window.add(poli314)
    po315 = GOval(1.5, 1.5)
    po315.filled = True
    po315.fill_color = 'lightsteelblue'
    po315.color = 'lightsteelblue'
    window.add(po315, x=672, y=204)
    po40 = GOval(11, 11)
    po40.filled = True
    po40.fill_color = 'lightsteelblue'
    po40.color = 'lightsteelblue'
    window.add(po40, x=295, y=217)
    poli40 = GArc(480, 480, 355, 35)
    poli40.color = 'lightsteelblue'
    window.add(poli40, x=285, y=178)
    po41 = GOval(11, 11)
    po41.filled = True
    po41.fill_color = 'lightsteelblue'
    po41.color = 'lightsteelblue'
    window.add(po41, x=328, y=213)
    poli41 = GArc(480, 480, 355, 35)
    poli41.color = 'lightsteelblue'
    window.add(poli41, x=316, y=175)
    po42 = GOval(10, 10)
    po42.filled = True
    po42.fill_color = 'lightsteelblue'
    po42.color = 'lightsteelblue'
    window.add(po42, x=356, y=210)
    poli42 = GArc(450, 450, 0, 33)
    poli42.color = 'lightsteelblue'
    window.add(poli42, x=340, y=182)
    po43 = GOval(9, 9)
    po43.filled = True
    po43.fill_color = 'lightsteelblue'
    po43.color = 'lightsteelblue'
    window.add(po43, x=380, y=208)
    poli43 = GArc(200, 200, 0, 28)
    poli43.color = 'lightsteelblue'
    window.add(poli43, x=385, y=195)
    po44 = GOval(8, 8)
    po44.filled = True
    po44.fill_color = 'lightsteelblue'
    po44.color = 'lightsteelblue'
    window.add(po44, x=405, y=208)
    poli44 = GArc(180, 180, 0, 25)
    poli44.color = 'lightsteelblue'
    window.add(poli44, x=415, y=198)
    po45 = GOval(7, 7)
    po45.filled = True
    po45.fill_color = 'lightsteelblue'
    po45.color = 'lightsteelblue'
    window.add(po45, x=431, y=208)
    poli45 = GLine(446, 207, 445, 218)
    poli45.color = 'lightsteelblue'
    window.add(poli45)
    po46 = GOval(6, 6)
    po46.filled = True
    po46.fill_color = 'lightsteelblue'
    po46.color = 'lightsteelblue'
    window.add(po46, x=454, y=208)
    poli46 = GLine(469, 207, 467, 217)
    poli46.color = 'lightsteelblue'
    window.add(poli46)
    po47 = GOval(5.5, 5.5)
    po47.filled = True
    po47.fill_color = 'lightsteelblue'
    po47.color = 'lightsteelblue'
    window.add(po47, x=478, y=208)
    poli47 = GLine(494, 208, 491, 216)
    poli47.color = 'lightsteelblue'
    window.add(poli47)
    po48 = GOval(4.5, 4.5)
    po48.filled = True
    po48.fill_color = 'lightsteelblue'
    po48.color = 'lightsteelblue'
    window.add(po48, x=507, y=209)
    poli48 = GLine(523, 208, 521, 215)
    poli48.color = 'lightsteelblue'
    window.add(poli48)
    po49 = GOval(3.5, 3.5)
    po49.filled = True
    po49.fill_color = 'lightsteelblue'
    po49.color = 'lightsteelblue'
    window.add(po49, x=537, y=208)
    poli49 = GLine(553, 208, 552, 214)
    poli49.color = 'lightsteelblue'
    window.add(poli49)
    po410 = GOval(2.5, 2.5)
    po410.filled = True
    po410.fill_color = 'lightsteelblue'
    po410.color = 'lightsteelblue'
    window.add(po410, x=564, y=209)
    poli410 = GLine(579, 207, 578, 213)
    poli410.color = 'lightsteelblue'
    window.add(poli410)
    po411 = GOval(2, 2)
    po411.filled = True
    po411.fill_color = 'lightsteelblue'
    po411.color = 'lightsteelblue'
    window.add(po411, x=589, y=209)
    poli411 = GLine(604, 209, 603, 213)
    poli411.color = 'lightsteelblue'
    window.add(poli411)
    po412 = GOval(2, 2)
    po412.filled = True
    po412.fill_color = 'lightsteelblue'
    po412.color = 'lightsteelblue'
    window.add(po412, x=615, y=209)
    poli412 = GLine(628, 208, 627, 213)
    poli412.color = 'lightsteelblue'
    window.add(poli412)
    po413 = GOval(2, 2)
    po413.filled = True
    po413.fill_color = 'lightsteelblue'
    po413.color = 'lightsteelblue'
    window.add(po413, x=634, y=209)
    poli413 = GLine(644, 209, 644, 212)
    poli413.color = 'lightsteelblue'
    window.add(poli413)
    po414 = GOval(1.5, 1.5)
    po414.filled = True
    po414.fill_color = 'lightsteelblue'
    po414.color = 'lightsteelblue'
    window.add(po414, x=655, y=209)
    poli414 = GLine(665, 209, 665, 212)
    poli414.color = 'lightsteelblue'
    window.add(poli414)
    po415 = GOval(1.5, 1.5)
    po415.filled = True
    po415.fill_color = 'lightsteelblue'
    po415.color = 'lightsteelblue'
    window.add(po415, x=672, y=209)
    po50 = GOval(11, 11)
    po50.filled = True
    po50.fill_color = 'lightsteelblue'
    po50.color = 'lightsteelblue'
    window.add(po50, x=295, y=238)
    po51 = GOval(11, 11)
    po51.filled = True
    po51.fill_color = 'lightsteelblue'
    po51.color = 'lightsteelblue'
    window.add(po51, x=328, y=234)
    po52 = GOval(11, 11)
    po52.filled = True
    po52.fill_color = 'lightsteelblue'
    po52.color = 'lightsteelblue'
    window.add(po52, x=356, y=231)
    po53 = GOval(9, 9)
    po53.filled = True
    po53.fill_color = 'lightsteelblue'
    po53.color = 'lightsteelblue'
    window.add(po53, x=382, y=230)
    poli53 = GArc(200, 200, 355, 28)
    poli53.color = 'lightsteelblue'
    window.add(poli53, x=390, y=213)
    po54 = GOval(8, 8)
    po54.filled = True
    po54.fill_color = 'lightsteelblue'
    po54.color = 'lightsteelblue'
    window.add(po54, x=405, y=228)
    poli54 = GLine(423, 225, 422, 239)
    poli54.color = 'lightsteelblue'
    window.add(poli54)
    po55 = GOval(7, 7)
    po55.filled = True
    po55.fill_color = 'lightsteelblue'
    po55.color = 'lightsteelblue'
    window.add(po55, x=429, y=227)
    poli55 = GLine(444, 225, 443, 238)
    poli55.color = 'lightsteelblue'
    window.add(poli55)
    po56 = GOval(6, 6)
    po56.filled = True
    po56.fill_color = 'lightsteelblue'
    po56.color = 'lightsteelblue'
    window.add(po56, x=451, y=226)
    poli56 = GLine(464, 225, 462, 235)
    poli56.color = 'lightsteelblue'
    window.add(poli56)
    po57 = GOval(5.5, 5.5)
    po57.filled = True
    po57.fill_color = 'lightsteelblue'
    po57.color = 'lightsteelblue'
    window.add(po57, x=471, y=225)
    poli57 = GLine(488, 223, 484, 232)
    poli57.color = 'lightsteelblue'
    window.add(poli57)
    po58 = GOval(4.5, 4.5)
    po58.filled = True
    po58.fill_color = 'lightsteelblue'
    po58.color = 'lightsteelblue'
    window.add(po58, x=500, y=224)
    poli58 = GLine(519, 221, 514, 232)
    poli58.color = 'lightsteelblue'
    window.add(poli58)
    po59 = GOval(3.5, 3.5)
    po59.filled = True
    po59.fill_color = 'lightsteelblue'
    po59.color = 'lightsteelblue'
    window.add(po59, x=531, y=222)
    poli59 = GLine(550, 219, 546, 228)
    poli59.color = 'lightsteelblue'
    window.add(poli59)
    po510 = GOval(2.5, 2.5)
    po510.filled = True
    po510.fill_color = 'lightsteelblue'
    po510.color = 'lightsteelblue'
    window.add(po510, x=560, y=221)
    poli510 = GLine(576, 218, 571, 226)
    poli510.color = 'lightsteelblue'
    window.add(poli510)
    po511 = GOval(2.5, 2.5)
    po511.filled = True
    po511.fill_color = 'lightsteelblue'
    po511.color = 'lightsteelblue'
    window.add(po511, x=584, y=220)
    poli511 = GLine(600, 217, 595, 225)
    poli511.color = 'lightsteelblue'
    window.add(poli511)
    po512 = GOval(2.5, 2.5)
    po512.filled = True
    po512.fill_color = 'lightsteelblue'
    po512.color = 'lightsteelblue'
    window.add(po512, x=612, y=218)
    poli512 = GLine(627, 216, 626, 223)
    poli512.color = 'lightsteelblue'
    window.add(poli512)
    po513 = GOval(2.5, 2.5)
    po513.filled = True
    po513.fill_color = 'lightsteelblue'
    po513.color = 'lightsteelblue'
    window.add(po513, x=634, y=216)
    poli513 = GLine(644, 214, 642, 222)
    poli513.color = 'lightsteelblue'
    window.add(poli513)
    po514 = GOval(2, 2)
    po514.filled = True
    po514.fill_color = 'lightsteelblue'
    po514.color = 'lightsteelblue'
    window.add(po514, x=654, y=216)
    poli514 = GLine(665, 215, 664, 220)
    poli514.color = 'lightsteelblue'
    window.add(poli514)
    po515 = GOval(1.5, 1.5)
    po515.filled = True
    po515.fill_color = 'lightsteelblue'
    po515.color = 'lightsteelblue'
    window.add(po515, x=672, y=215)
    po60 = GOval(10, 10)
    po60.filled = True
    po60.fill_color = 'lightsteelblue'
    po60.color = 'lightsteelblue'
    window.add(po60, x=300, y=263)
    po61 = GOval(15, 15)
    po61.filled = True
    po61.fill_color = 'lightsteelblue'
    po61.color = 'lightsteelblue'
    window.add(po61, x=305, y=282)
    po62 = GOval(8, 8)
    po62.filled = True
    po62.fill_color = 'lightsteelblue'
    po62.color = 'lightsteelblue'
    window.add(po62, x=327, y=301)
    po63 = GOval(10, 10)
    po63.filled = True
    po63.fill_color = 'lightsteelblue'
    po63.color = 'lightsteelblue'
    window.add(po63, x=334, y=318)
    po64 = GOval(13, 13)
    po64.filled = True
    po64.fill_color = 'lightsteelblue'
    po64.color = 'lightsteelblue'
    window.add(po64, x=344, y=333)
    poli60 = GLine(318, 261, 371, 358)
    poli60.color = 'lightsteelblue'
    window.add(poli60)
    po65 = GOval(17,17)
    po65.filled = True
    po65.fill_color = 'lightsteelblue'
    po65.color = 'lightsteelblue'
    window.add(po65, x=328, y=259)
    po66 = GOval(7, 7)
    po66.filled = True
    po66.fill_color = 'lightsteelblue'
    po66.color = 'lightsteelblue'
    window.add(po66, x=338, y=281)
    po67 = GOval(10,10)
    po67.filled = True
    po67.fill_color = 'lightsteelblue'
    po67.color = 'lightsteelblue'
    window.add(po67, x=349, y=286)
    po68 = GOval(12, 12)
    po68.filled = True
    po68.fill_color = 'lightsteelblue'
    po68.color = 'lightsteelblue'
    window.add(po68, x=359, y=317)
    po69 = GOval(8, 8)
    po69.filled = True
    po69.fill_color = 'lightsteelblue'
    po69.color = 'lightsteelblue'
    window.add(po69, x=351, y=303)
    po70 = GOval(5, 5)
    po70.filled = True
    po70.fill_color = 'lightsteelblue'
    po70.color = 'lightsteelblue'
    window.add(po70, x=371, y=333)
    po71 = GOval(8, 8)
    po71.filled = True
    po71.fill_color = 'lightsteelblue'
    po71.color = 'lightsteelblue'
    window.add(po71, x=364, y=344)
    poli65 = GLine(348, 258, 369, 310)
    poli65.color = 'lightsteelblue'
    window.add(poli65)
    po72 = GOval(16, 16)
    po72.filled = True
    po72.fill_color = 'lightsteelblue'
    po72.color = 'lightsteelblue'
    window.add(po72, x=276, y=258)
    poli72 = GArc(580, 580, 0, 50)
    poli72.color = 'lightsteelblue'
    window.add(poli72, x=185, y=140)
    po73 = GOval(8, 8)
    po73.filled = True
    po73.fill_color = 'lightsteelblue'
    po73.color = 'lightsteelblue'
    window.add(po73, x=398, y=138)
    poli73 = GArc(200, 200, 0, 28)
    poli73.color = 'lightsteelblue'
    window.add(poli73, x=398, y=125)
    po74 = GOval(12, 12)
    po74.filled = True
    po74.fill_color = 'lightsteelblue'
    po74.color = 'lightsteelblue'
    window.add(po74, x=416, y=133)
    po75 = GOval(6, 6)
    po75.filled = True
    po75.fill_color = 'lightsteelblue'
    po75.color = 'lightsteelblue'
    window.add(po75, x=424, y=122)
    poli73 = GArc(300, 300, 0, 35)
    poli73.color = 'lightsteelblue'
    window.add(poli73, x=410, y=107)
    po76 = GOval(8, 8)
    po76.filled = True
    po76.fill_color = 'lightsteelblue'
    po76.color = 'lightsteelblue'
    window.add(po76, x=440, y=112)
    po77 = GOval(5, 5)
    po77.filled = True
    po77.fill_color = 'lightsteelblue'
    po77.color = 'lightsteelblue'
    window.add(po77, x=451, y=122)
    po78 = GOval(11, 11)
    po78.filled = True
    po78.fill_color = 'lightsteelblue'
    po78.color = 'lightsteelblue'
    window.add(po78, x=440, y=129)
    po79 = GOval(7, 7)
    po79.filled = True
    po79.fill_color = 'lightsteelblue'
    po79.color = 'lightsteelblue'
    window.add(po79, x=448, y=144)
    poli76 = GArc(450, 450, 0, 40)
    poli76.color = 'lightsteelblue'
    window.add(poli76, x=410, y=82)
    po80 = GOval(11, 11)
    po80.filled = True
    po80.fill_color = 'lightsteelblue'
    po80.color = 'lightsteelblue'
    window.add(po80, x=458, y=99)
    po81 = GOval(7, 7)
    po81.filled = True
    po81.fill_color = 'lightsteelblue'
    po81.color = 'lightsteelblue'
    window.add(po81, x=466, y=117)
    po82 = GOval(5, 5)
    po82.filled = True
    po82.fill_color = 'lightsteelblue'
    po82.color = 'lightsteelblue'
    window.add(po82, x=464, y=133)
    po83 = GOval(7, 7)
    po83.filled = True
    po83.fill_color = 'lightsteelblue'
    po83.color = 'lightsteelblue'
    window.add(po83, x=568, y=166)
    poli83 =  GArc(200, 200, 0, 28)
    poli83.color = 'lightsteelblue'
    window.add(poli83, x=565, y=152)
    po84 = GOval(5, 5)
    po84.filled = True
    po84.fill_color = 'lightsteelblue'
    po84.color = 'lightsteelblue'
    window.add(po84, x=582, y=166)
    po85 = GOval(7, 7)
    po85.filled = True
    po85.fill_color = 'lightsteelblue'
    po85.color = 'lightsteelblue'
    window.add(po85, x=592, y=159)
    po85 = GOval(3, 3)
    po85.filled = True
    po85.fill_color = 'lightsteelblue'
    po85.color = 'lightsteelblue'
    window.add(po85, x=590, y=172)
    poli84 = GArc(400, 400, 0, 30)
    poli84.color = 'lightsteelblue'
    window.add(poli84, x=575, y=132)
    po86 = GOval(3, 3)
    po86.filled = True
    po86.fill_color = 'lightsteelblue'
    po86.color = 'lightsteelblue'
    window.add(po86, x=681, y=197)
    po86 = GOval(6, 6)
    po86.filled = True
    po86.fill_color = 'lightsteelblue'
    po86.color = 'lightsteelblue'
    window.add(po86, x=684, y=205)
    po86 = GOval(4, 4)
    po86.filled = True
    po86.fill_color = 'lightsteelblue'
    po86.color = 'lightsteelblue'
    window.add(po86, x=683, y=214)
    poli86 = GArc(300, 300, 0, 40)
    poli86.color = 'lightsteelblue'
    window.add(poli86, x=658, y=177)
    po87 = GOval(4, 4)
    po87.filled = True
    po87.fill_color = 'lightsteelblue'
    po87.color = 'lightsteelblue'
    window.add(po87, x=693, y=196)
    po87 = GOval(14, 14)
    po87.filled = True
    po87.fill_color = 'lightsteelblue'
    po87.color = 'lightsteelblue'
    window.add(po87, x=697, y=180)
    po87 = GOval(8, 8)
    po87.filled = True
    po87.fill_color = 'lightsteelblue'
    po87.color = 'lightsteelblue'
    window.add(po87, x=700, y=206)
    po87 = GOval(11, 11)
    po87.filled = True
    po87.fill_color = 'lightsteelblue'
    po87.color = 'lightsteelblue'
    window.add(po87, x=699, y=221)
    po87 = GOval(7, 7)
    po87.filled = True
    po87.fill_color = 'lightsteelblue'
    po87.color = 'lightsteelblue'
    window.add(po87, x=707, y=166)
    po87 = GOval(9, 9)
    po87.filled = True
    po87.fill_color = 'lightsteelblue'
    po87.color = 'lightsteelblue'
    window.add(po87, x=721, y=156)
    po87 = GOval(5, 5)
    po87.filled = True
    po87.fill_color = 'lightsteelblue'
    po87.color = 'lightsteelblue'
    window.add(po87, x=719, y=176)
    po87 = GOval(12, 12)
    po87.filled = True
    po87.fill_color = 'lightsteelblue'
    po87.color = 'lightsteelblue'
    window.add(po87, x=725, y=136)
    po87 = GOval(6, 6)
    po87.filled = True
    po87.fill_color = 'lightsteelblue'
    po87.color = 'lightsteelblue'
    window.add(po87, x=737, y=116)
    po87 = GOval(4, 4)
    po87.filled = True
    po87.fill_color = 'lightsteelblue'
    po87.color = 'lightsteelblue'
    window.add(po87, x=714, y=186)
    po87 = GOval(8, 8)
    po87.filled = True
    po87.fill_color = 'lightsteelblue'
    po87.color = 'lightsteelblue'
    window.add(po87, x=718, y=206)
    po87 = GOval(6, 6)
    po87.filled = True
    po87.fill_color = 'lightsteelblue'
    po87.color = 'lightsteelblue'
    window.add(po87, x=719, y=223)
    po87 = GOval(14, 14)
    po87.filled = True
    po87.fill_color = 'lightsteelblue'
    po87.color = 'lightsteelblue'
    window.add(po87, x=728, y=236)
    po87 = GOval(5, 5)
    po87.filled = True
    po87.fill_color = 'lightsteelblue'
    po87.color = 'lightsteelblue'
    window.add(po87, x=748, y=248)
    po87 = GOval(6, 6)
    po87.filled = True
    po87.fill_color = 'lightsteelblue'
    po87.color = 'lightsteelblue'
    window.add(po87, x=757, y=260)
    poli87 = GArc(400, 400, 0, 45)
    poli87.color = 'lightsteelblue'
    window.add(poli87, x=655, y=161)
    head_po = GOval(10, 10)
    head_po.filled = True
    head_po.fill_color = 'lightsteelblue'
    head_po.color = 'lightsteelblue'
    window.add(head_po, x=256, y=173)
    head_po = GOval(10, 10)
    head_po.filled = True
    head_po.fill_color = 'lightsteelblue'
    head_po.color = 'lightsteelblue'
    window.add(head_po, x=262, y=156)
    head_po = GOval(8, 8)
    head_po.filled = True
    head_po.fill_color = 'lightsteelblue'
    head_po.color = 'lightsteelblue'
    window.add(head_po, x=242, y=148)
    head_po = GOval(9, 9)
    head_po.filled = True
    head_po.fill_color = 'lightsteelblue'
    head_po.color = 'lightsteelblue'
    window.add(head_po, x=267, y=193)
    head_po = GOval(10, 10)
    head_po.filled = True
    head_po.fill_color = 'lightsteelblue'
    head_po.color = 'lightsteelblue'
    window.add(head_po, x=266, y=213)
    head_po = GOval(11, 11)
    head_po.filled = True
    head_po.fill_color = 'lightsteelblue'
    head_po.color = 'lightsteelblue'
    window.add(head_po, x=276, y=233)
    head_po1 = GOval(7, 7)
    head_po1.filled = True
    head_po1.fill_color = 'lightsteelblue'
    head_po1.color = 'lightsteelblue'
    window.add(head_po1, x=236, y=163)
    head_po1 = GOval(8, 8)
    head_po1.filled = True
    head_po1.fill_color = 'lightsteelblue'
    head_po1.color = 'lightsteelblue'
    window.add(head_po1, x=246, y=187)
    head_po1 = GOval(6, 6)
    head_po1.filled = True
    head_po1.fill_color = 'lightsteelblue'
    head_po1.color = 'lightsteelblue'
    window.add(head_po1, x=236, y=207)
    head_po1 = GOval(9, 9)
    head_po1.filled = True
    head_po1.fill_color = 'lightsteelblue'
    head_po1.color = 'lightsteelblue'
    window.add(head_po1, x=254, y=227)
    head_po1 = GOval(8, 8)
    head_po1.filled = True
    head_po1.fill_color = 'lightsteelblue'
    head_po1.color = 'lightsteelblue'
    window.add(head_po1, x=226, y=152)
    head_po1 = GOval(6, 6)
    head_po1.filled = True
    head_po1.fill_color = 'lightsteelblue'
    head_po1.color = 'lightsteelblue'
    window.add(head_po1, x=226, y=177)
    head_po1 = GOval(8, 8)
    head_po1.filled = True
    head_po1.fill_color = 'lightsteelblue'
    head_po1.color = 'lightsteelblue'
    window.add(head_po1, x=216, y=197)
    head_po1 = GOval(8, 8)
    head_po1.filled = True
    head_po1.fill_color = 'lightsteelblue'
    head_po1.color = 'lightsteelblue'
    window.add(head_po1, x=246, y=187)
    head_po1 = GOval(4, 4)
    head_po1.filled = True
    head_po1.fill_color = 'lightsteelblue'
    head_po1.color = 'lightsteelblue'
    window.add(head_po1, x=248, y=247)
    head_po1 = GOval(9, 9)
    head_po1.filled = True
    head_po1.fill_color = 'lightsteelblue'
    head_po1.color = 'lightsteelblue'
    window.add(head_po1, x=229, y=221)
    head_po1 = GOval(8, 8)
    head_po1.filled = True
    head_po1.fill_color = 'lightsteelblue'
    head_po1.color = 'lightsteelblue'
    window.add(head_po1, x=216, y=241)
    head_po1 = GOval(6, 6)
    head_po1.filled = True
    head_po1.fill_color = 'lightsteelblue'
    head_po1.color = 'lightsteelblue'
    window.add(head_po1, x=201, y=147)
    head_po1 = GOval(8, 8)
    head_po1.filled = True
    head_po1.fill_color = 'lightsteelblue'
    head_po1.color = 'lightsteelblue'
    window.add(head_po1, x=212, y=162)
    head_po1 = GOval(4, 4)
    head_po1.filled = True
    head_po1.fill_color = 'lightsteelblue'
    head_po1.color = 'lightsteelblue'
    window.add(head_po1, x=189, y=183)
    head_po1 = GOval(7, 7)
    head_po1.filled = True
    head_po1.fill_color = 'lightsteelblue'
    head_po1.color = 'lightsteelblue'
    window.add(head_po1, x=206, y=187)
    head_po1 = GOval(10, 10)
    head_po1.filled = True
    head_po1.fill_color = 'lightsteelblue'
    head_po1.color = 'lightsteelblue'
    window.add(head_po1, x=199, y=217)
    head_po1 = GOval(12, 12)
    head_po1.filled = True
    head_po1.fill_color = 'lightsteelblue'
    head_po1.color = 'lightsteelblue'
    window.add(head_po1, x=176, y=232)
    head_po1 = GOval(5, 5)
    head_po1.filled = True
    head_po1.fill_color = 'lightsteelblue'
    head_po1.color = 'lightsteelblue'
    window.add(head_po1, x=196, y=243)
    head_po1 = GOval(6, 6)
    head_po1.filled = True
    head_po1.fill_color = 'lightsteelblue'
    head_po1.color = 'lightsteelblue'
    window.add(head_po1, x=149, y=241)
    head_po1 = GOval(8, 8)
    head_po1.filled = True
    head_po1.fill_color = 'lightsteelblue'
    head_po1.color = 'lightsteelblue'
    window.add(head_po1, x=174, y=209)
    head_po1 = GOval(8, 8)
    head_po1.filled = True
    head_po1.fill_color = 'lightsteelblue'
    head_po1.color = 'lightsteelblue'
    window.add(head_po1, x=246, y=187)
    head_po1 = GOval(5, 5)
    head_po1.filled = True
    head_po1.fill_color = 'lightsteelblue'
    head_po1.color = 'lightsteelblue'
    window.add(head_po1, x=159, y=228)
    head_po1 = GOval(8, 8)
    head_po1.filled = True
    head_po1.fill_color = 'lightsteelblue'
    head_po1.color = 'lightsteelblue'
    window.add(head_po1, x=132, y=229)
    head_po1 = GOval(8, 8)
    head_po1.filled = True
    head_po1.fill_color = 'lightsteelblue'
    head_po1.color = 'lightsteelblue'
    window.add(head_po1, x=192, y=161)
    head_po1 = GOval(10, 10)
    head_po1.filled = True
    head_po1.fill_color = 'lightsteelblue'
    head_po1.color = 'lightsteelblue'
    window.add(head_po1, x=145, y=205)
    head_po1 = GOval(7, 7)
    head_po1.filled = True
    head_po1.fill_color = 'lightsteelblue'
    head_po1.color = 'lightsteelblue'
    window.add(head_po1, x=169, y=192)
    head_po1 = GOval(6, 6)
    head_po1.filled = True
    head_po1.fill_color = 'lightsteelblue'
    head_po1.color = 'lightsteelblue'
    window.add(head_po1, x=122, y=213)
    head_po1 = GOval(6, 6)
    head_po1.filled = True
    head_po1.fill_color = 'lightsteelblue'
    head_po1.color = 'lightsteelblue'
    window.add(head_po1, x=174, y=171)
    head_po1 = GOval(8, 8)
    head_po1.filled = True
    head_po1.fill_color = 'lightsteelblue'
    head_po1.color = 'lightsteelblue'
    window.add(head_po1, x=147, y=180)
    head_po1 = GOval(6, 6)
    head_po1.filled = True
    head_po1.fill_color = 'lightsteelblue'
    head_po1.color = 'lightsteelblue'
    window.add(head_po1, x=158, y=158)
    head_po1 = GOval(4, 4)
    head_po1.filled = True
    head_po1.fill_color = 'lightsteelblue'
    head_po1.color = 'lightsteelblue'
    window.add(head_po1, x=128, y=166)
    head_po1 = GOval(8, 8)
    head_po1.filled = True
    head_po1.fill_color = 'lightsteelblue'
    head_po1.color = 'lightsteelblue'
    window.add(head_po1, x=132, y=192)


# def pixel(mouse):
#找座標
#     oval = GOval(1,1)
#     window.add(oval, x=mouse.x, y=mouse.y)
#     a = mouse.x
#     b = mouse.y
#     labelx = GLabel(a)
#     labely = GLabel(b)
#     labelx.font = '-10'
#     labelx.color = 'red'
#     labely.font = '-10'
#     window.add(labelx, x=a, y=b)
#     window.add(labely, x=a+10, y=b+10)



if __name__ == '__main__':
    main()
