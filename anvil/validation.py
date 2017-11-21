from six import iteritems
from functools import wraps
import config
import runtime as rt


def verify_inputs(filterers=None, validators=None):
    filterers = filterers if isinstance(filterers, list) else [filterers]
    validators = validators if isinstance(validators, list) else [validators]
    filterers = filterers if filterers is not None else []
    validators = validators if validators is not None else []

    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            check_inputs = []
            for function_input in list(args) + [v for k, v in iteritems(kwargs)]:
                for filterer in filterers:
                    if filterer(function_input):
                        check_inputs.append(function_input)

            for check_input in check_inputs:
                for validator, filterer in zip(validators, filterers):
                    if filterer(check_input):
                        validator(check_input)

            return function(*args, **kwargs)

        return wrapper

    return decorator


def verify_class_method_inputs(filterers=None, validators=None):
    filterers = filterers if isinstance(filterers, list) else [filterers]
    validators = validators if isinstance(validators, list) else [validators]
    filterers = filterers if filterers is not None else []
    validators = validators if validators is not None else []

    def decorator(function):
        @wraps(function)
        def wrapper(self, *args, **kwargs):
            check_inputs = []
            for function_input in list(args) + [v for k, v in iteritems(kwargs)]:
                for filterer in filterers:
                    if filterer(function_input):
                        check_inputs.append(function_input)

            for check_input in check_inputs:
                for validator, filterer in zip(validators, filterers):
                    if filterer(check_input):
                        validator(check_input)

            return function(self, *args, **kwargs)

        return wrapper

    return decorator


def filter_list_type(query_input, chain_type):
    if not isinstance(query_input, list):
        query_input = [query_input]
    return all([rt.dcc.scene.is_types(node, [chain_type]) for node in query_input])


def filter_list_joints(query_input):
    return filter_list_type(query_input, config.JOINT_TYPE)


def filter_list_transforms(query_input):
    return filter_list_type(query_input, config.TRANSFORM_TYPE)


def verify_joint_chain_ready(joint_chain):
    non_zero = []
    attrs = ['scale', 'rotate']
    axes = ['x', 'y', 'z']

    for joint in joint_chain:
        for attr in attrs:
            desired = 1 if attr == 'scale' else 0
            for axis in axes:
                if getattr(joint, '%s%s' % (attr, axis.upper())).get() > desired:
                    if joint not in non_zero:
                        non_zero.append(joint)
                    break

        translate_attrs = ['.%s%s' % (attr, axis.upper()) for axis in axes for attr in ['translate']]
        if sum([getattr(joint, translate_attr) for translate_attr in translate_attrs]) > 1:
            raise ValueError('Joint %s should only have one non zeroed translation attribute' % (joint))

    raise ValueError('Joints %s were non-zeroed' % non_zero)


def verify_joint_chain_length(joint_chain):
    if len(joint_chain) < 3:
        raise ValueError('Need to input more than 3 joints.')


def verify_transform_skinned(transforms):
    for transform in transforms:
        if not transform.getShape() and transform.listHistory(type='skinCluster'):
            raise ValueError('Transform %s is not skinned' % transform)
