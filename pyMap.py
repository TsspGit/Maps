#!/usr/bin/python3
__author__ = '@Tssp'

from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
plt.rc('text',usetex=True)
plt.rc('font',family='serif')
plt.rcParams['xtick.labelsize']=13
plt.rcParams['ytick.labelsize']=13
plt.rcParams['axes.labelsize']=16
plt.rcParams['axes.titlesize']=16

class Map:
    '''Quick plot of a Map'''
    def __init__(self, lons, lats, EPSG, service='ESRI_Imagery_World_2D'):
        self.lons = lons
        self.lats = lats
        self.EPSG = EPSG
        self.service = service
        print( 'Longitudes: {}\nLatitudes: {}\nEPSG: {}\nService: {}'.format(self.lons, self.lats, self.EPSG, self.service) )
        print('\nObtain your epsg code from this web:\nhttps://epsg.io/3832')
        
    def createMap(self, res='l', proj='merc', xpix=1000, figsize=(10, 10)):
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_axes([0.1,0.1,0.8,0.8])
        m = Basemap(llcrnrlon=self.lons[0], llcrnrlat=self.lats[0], urcrnrlon=self.lons[1], urcrnrlat=self.lats[1],\
                resolution=res,projection=proj, epsg=self.EPSG)
        m.arcgisimage(service=self.service, xpixels=xpix, verbose= True)
        return m
    
    def plotMap(self, m, num='3', fontsize='14'):
        m.drawcountries()
        meridians = np.linspace(self.lons[0], self.lons[1], num=num)
        m.drawmeridians(meridians, labels=[0,0,1,1], linewidth=0, fontsize=14)
        parallels = np.linspace(self.lats[0], self.lats[1], num=num)
        m.drawparallels(parallels, labels=[1,1,0,0], linewidth=0, fontsize=14)
        plt.show()