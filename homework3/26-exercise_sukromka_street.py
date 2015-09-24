#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Сосчитать всех кто живет на улице Сукромка

import sukromka_street.house1.room1
import sukromka_street.house1.room2
import sukromka_street.house2.room1
import sukromka_street.house2.room2

count = 0
inhabitants = sukromka_street.house1.room1.get_inhabitants()
count += len(inhabitants)

count += len(sukromka_street.house1.room2.get_inhabitants())

count += len(sukromka_street.house2.room1.get_inhabitants())

count += len(sukromka_street.house2.room2.get_inhabitants())

print u'Всего живет ...', count  # а через .format() ?

# ++ вывести полный список живущих на улице Сукромка
