# -*- coding: utf-8 -*-
##############################################################################
#
#    Mandate module for openERP
#    Copyright (C) 2018-TODAY Anubía, soluciones en la nube,SL
#                             (http://www.anubia.es)
#    @author: Juan Formoso Vasco <jfv@anubia.es>,
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Analytic Shortcut Button in Projects',
    'summary': 'Analytic account view shortcut added to projects view',
    'description': """Description in HTML file.
- Analytic Link Analytic
- Analytic Button Analytic
- Analytic Buttons Analytic
- Project Link Project
- Project Button Project
- Project Buttons Project
- Anubia Soluciones en la Nube, S.L.
""",
    'category': 'Analytic',
    'version': '0.1',
    'author': 'Anubía Soluciones en la Nube, S.L.',
    'maintainer': 'Anubía Soluciones en la Nube, S.L.',
    'contributors': [
        'Juan Formoso Vasco <jfv@anubia.es>',
    ],
    'website': 'http://www.anubia.es',
    'complexity': 'easy',
    'depends': [
        'analytic',
        'project',
    ],
    'data': [
        'views/project_view.xml',
    ],
    'demo': [],
    'test': [],
    'images': [
        'static/description/main_screenshot.png',
        'static/description/main_1.png',
        'static/description/main_2.png',
        'static/description/main_3.png',
        'static/description/main_4.png',
        'static/description/anubia-logo.png',
        'static/description/flags/france-flag.png',
        'static/description/flags/galicia-flag.png',
        'static/description/flags/germany-flag.png',
        'static/description/flags/italy-flag.png',
        'static/description/flags/portugal-flag.png',
        'static/description/flags/spain-flag.png',
        'static/description/flags/uk-flag.png',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'price': 0,
    'currency': 'EUR',
}
