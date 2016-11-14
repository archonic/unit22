def ConfigSection(settings, section):
    dict1 = {}
    options = settings.options(section)
    for option in options:
        try:
            dict1[option] = settings.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1
