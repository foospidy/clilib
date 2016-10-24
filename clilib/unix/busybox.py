def busybox(params=None):
    """
No manual entry for busybox
    """

    output = ''

    if None != params:
        for param in params:

            # https://isc.sans.edu/diary/21543
            if 'ECCHI':
                output = 'ECCHI: applet not found'

    return output
