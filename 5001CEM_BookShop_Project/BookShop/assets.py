#hackersandslackers.(2021).Organizing Flask Apps with Blueprints.
#https://hackersandslackers.com/flask-blueprints/

import os, sys
from flask import current_app as app
from flask_assets import Environment, Bundle

#Static file references outside of parent files 
#5001CEM_BookShop_Project/BookShop/Static

#Compilation of assets to be distributed from BookShop/static/dist/css
def compile_static_assets(assets):
    try:
        bookInformation_style_bundle = Bundle(
            'src/less/*.less',
            filters='less,cssmin',
            output='dist/css/theme.css',
            extra={'rel':'stylesheet/less'}
        )
        booksCatalog_style_bundle = Bundle(
            'src/less/*.less',
            filters="less,cssmin",
            output='dist/css/theme.css',
            extra={'rel':'stylesheet/less'}
        )
        indexScript_style_bundle = Bundle(
            'src/less/*.less',
            filters='less,cssmin',
            output='dist/css/theme.css',
            extra={'rel':'stylesheet/less'}
        )
        loginCredentials_style_bundle = Bundle(
            'src/css/*.less',
            filters='less,cssmin',
            output='dist/css/theme.css',
            extra={'rel':'stylesheet/less'}
        )
        registerCredentials_style_bundle = Bundle(
            'src/less/*.less',
            filters='less,cssmin',
            output='dist/css/theme.css',
            extra={'rel':'stylesheet/less'}
        )
        #Registering assets with Blueprints import
        assets.register('bookInformation_style_bundle',bookInformation_style_bundle)
        assets.register('booksCatalog_style_bundle',booksCatalog_style_bundle)
        assets.register('indexScript_style_bundle',indexScript_style_bundle)
        assets.register('loginCredentials_style_bundle',loginCredentials_style_bundle)
        assets.register('registerCredentials_style_bundle',registerCredentials_style_bundle)
        #Actioning static files to be used across website
        if app.config['FLASK_ENV'] == 'development':
            bookInformation_style_bundle.build()
            booksCatalog_style_bundle.build()
            indexScript_style_bundle.build()
            loginCredentials_style_bundle.build()
            registerCredentials_style_bundle.build()
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(e,exc_type, fname, exc_tb.tb_lineno)
        
        
        