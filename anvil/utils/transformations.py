
def normalize_scale(nodes, desired_scale):
    for node in nodes:
        biggest_value = abs(max([max([abs(p) for p in points]) for points in node.boundingBox.get()]))
        normalized = max([desired_scale, biggest_value]) / min([desired_scale, biggest_value])
        node.scale_node([normalized] * 3)
