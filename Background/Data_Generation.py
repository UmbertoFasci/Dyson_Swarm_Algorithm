# Generate sphere data for the background

import bpy
import bmesh
import mathutils
from mathutils import Vector

# Create a new mesh
mesh = bpy.data.meshes.new("Sphere")
obj = bpy.data.objects.new("Sphere", mesh)
bpy.context.scene.objects.link(obj)
bpy.context.scene.objects.active = obj
bm = bmesh.new()
bmesh.ops.create_uvsphere(bm, u_segments=32, v_segments=16, diameter=1)
bm.to_mesh(mesh)
bm.free()
obj.location = bpy.context.scene.cursor_location