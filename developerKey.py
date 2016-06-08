#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Get permission from app.

:param key: key from app
:return: keys from the apps founds.
"""
from tacyt import TacytApp
from maltego.MaltegoTransform import *
from APIManagement import Tacyt
from maltego.Entities import TacytEntities as te

api = TacytApp.TacytApp(Tacyt.APP_ID, Tacyt.SECRET_KEY)
m = MaltegoTransform()

app = sys.argv[1]


try:
    result = api.get_app_details(app)
    data = result.get_data()

    if 'result' in data and data['result'] is not None:
        details = data['result']

        if 'developerName' in details:
            m.addEntity(te.FIELD, str(details['developerName']), te.FIELD_NAME, 'developerName')

        if 'developerPrivacy' in details:
            m.addEntity(te.FIELD, str(details['developerPrivacy']), te.FIELD_NAME, 'developerPrivacy')

        if 'developerWeb' in details:
            m.addEntity(te.DOMAIN, str(details['developerWeb']), te.FIELD_NAME, 'developerWeb')

        if 'developerEmail' in details:
            m.addEntity(te.EMAIL, str(details['developerEmail']), te.FIELD_NAME, 'developerEmail')

        m.returnOutput()

    else:
        m.addException("The search returns null results")
        m.throwExceptions()

except Exception as e:
    m.addException(str(e))
    m.throwExceptions()
