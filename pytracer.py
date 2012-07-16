# pytracer.py
# Andrew Nguyen Jul 15 2012
# pytracer!

import camera as ca
import vector as vr
import scene  as sc
import light  as lt 
import raytracer as rt
import film as fm

FOVX = 45.0
FOVY = 45.0
PIXWIDTH = 130
PIXHEIGHT = 100


prims = [sc.make_sphere(vr.make_vector(0.0, 0.0, -4.0), 1.0),
         sc.make_sphere(vr.make_vector(-3.0, -1.0, -11.0), 2.0)]

lights = [lt.make_light(2.5, 4.0, 10.0, 7.0),]


eye = vr.make_vector(0.0, 0.0, 0.0)
up  = vr.make_vector(0.0, 1.0, 0.0)
center = vr.make_vector(0.0, 0.0, -1.0)
geo = ca.make_view_geometry(eye, up, center)
camera = ca.make_camera(eye, geo, PIXWIDTH, PIXHEIGHT, FOVX, FOVY)
film = fm.create_film(PIXWIDTH, PIXHEIGHT)

def pytracer():
    for j in range(PIXHEIGHT):
        for i in range(PIXWIDTH):
            ray = camera(i, j)
            color = int(rt.get_color(prims, lights, ray))
            fm.develop(film, i, j, color)
    fm.display(film)

if __name__ == "__main__":
    pytracer()

                         
                         







