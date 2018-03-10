import plugins.dcc_plugin as dcc_plugin

dcc = dcc_plugin.DCCPlugin(dcc_plugin.get_current_dcc(return_module=True))


def swap_dcc(dcc_name_query):
    globals()['dcc'] = dcc_plugin.get_dcc(dcc_name_query)


__all__ = ['dcc']
