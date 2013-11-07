# -*- coding: utf-8 -*-
import bpy

def exposeNodeTreeInput(in_socket, name, default_value, node_input, group):
    t = len(node_input.outputs)-1
    i = node_input.outputs[t]
    group.links.new(in_socket, i)
    if default_value is not None:
        group.inputs[t].default_value = default_value
    group.inputs[t].name = name

def exposeNodeTreeOutput(out_socket, name, node_output, group):
    t = len(node_output.inputs)-1
    i = node_output.inputs[t]
    group.links.new(i, out_socket)
    group.outputs[t].name = name


def create_BackfaceCullingNode():
    bpy.context.scene.render.engine = 'BLENDER_RENDER'

    if 'MMDBackfaceCulling' in bpy.data.node_groups:
        return bpy.data.node_groups['MMDBackfaceCulling']

    group = bpy.data.node_groups.new(name='MMDBackfaceCulling', type='ShaderNodeTree')

    node_input = group.nodes.new('NodeGroupInput')
    node_output = group.nodes.new('NodeGroupOutput')

    geo = group.nodes.new('ShaderNodeGeometry')
    mul = group.nodes.new('ShaderNodeMath')
    mul.operation = 'MULTIPLY'

    group.links.new(mul.inputs[1], geo.outputs['Front/Back'])

    exposeNodeTreeInput(mul.inputs[0], 'Alpha', 1.0, node_input, group)
    exposeNodeTreeOutput(mul.outputs['Value'], 'Alpha', node_output, group)

    return group


def setupSimpleShader(material):
    if material.game_settings.use_backface_culling:
        material.use_nodes = True
        mat = material.node_tree.nodes.new('ShaderNodeMaterial')
        cul = material.node_tree.nodes.new('ShaderNodeGroup')
        out = material.node_tree.nodes.new('ShaderNodeOutput')
        mat.material = material
        cul.node_tree = create_BackfaceCullingNode()
        material.node_tree.links.new(out.inputs['Color'], mat.outputs['Color'])
        material.node_tree.links.new(cul.inputs['Alpha'], mat.outputs['Alpha'])
        material.node_tree.links.new(out.inputs['Alpha'], cul.outputs['Alpha'])
    else:
        material.use_nodes = False
