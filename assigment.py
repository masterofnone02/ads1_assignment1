#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 19:19:32 2022

@author: akhilmathew
"""
import pandas as pd
import matplotlib.pyplot as plt

def read_data(name):
    """
    This function reads the data from excel and returns the dataframe

    Parameters
    ----------
    name : String
        Name of the excel file to be read.

    Returns
    -------
    excel_data : DataFrame
        Returns dataframe corresponding to file name.

    """
    excel_data = pd.read_excel(name)
    return excel_data

def netflix_revenue():
    """
    This function plots the Annual Netflix Return for the years 2018 - 2021

    Returns
    -------
    None.

    """
    plt.figure()
    netflix_revenue_data = read_data("Netflix_Revenue.xlsx")
    for i in range(regions.__len__()):
        plt.plot(netflix_revenue_data["Year"], netflix_revenue_data[regions[i]], label = regions[i])
        plt.legend(loc = "upper left")
    plt.xlabel("Years")
    plt.ylabel("Annual Revenue (in billions)")
    plt.title("Netflix Annual Revenue", size = 14)
    plt.xlim(0)
    plt.savefig('Netflix_Revenue')
    plt.show()

def player_comparison():
    """
    This function plots the bar graph which compares players
    based on goals scored

    Returns
    -------
    None.

    """
    plt.figure(figsize = (9,9))
    messi = read_data("Messi_data.xlsx")
    ronaldo = read_data("Ronaldo_data.xlsx")
    data = [messi , ronaldo]
    #Plotting the number of goals vs season for Messi and Ronaldo using Bar plot
    for i in range(data.__len__()):
        plt.bar(data[i]["Season"], data[i]["GO Goals"], label=playerName[i], alpha = 0.6)
        plt.legend()
    plt.xlabel("Season")
    plt.ylabel("Number of Goals")
    plt.title("Goal comparison per season", size = 14)
    #Setting xticks to 90 degree
    plt.xticks(rotation = 90)
    plt.savefig('Player_Comparison')
    plt.show()

def messi_stats():
    """
    This function produces a boxplot for goals and assists for
    a player

    Returns
    -------
    None.

    """
    plt.figure()
    #Excluding rows with number of games played = 0
    messi = read_data("Messi_data.xlsx")
    messi_avg = messi[0 : 18]
    #Plotting the number of goals and number of assists by Messi using Box plot
    plt.boxplot([messi_avg["GO Goals"], messi_avg["AS Assists"]],
            labels = ["Messi_Goals", "Messi_Assists"])
    plt.title("Messi goal and assist analysis", size = 14)
    plt.savefig('Messi_Statitics')
    plt.show()

def population_density():
    """
    This function plots a pie chart for population distribution over continents.

    Returns
    -------
    None.

    """
    plt.figure()
    population_density_data = read_data("Population_density.xlsx")
    plt.pie(population_density_data["World Population Share"], center = (0, 1))
    plt.title("World population distribution", size = 10, loc= "center")
    plt.legend(labels = population_density_data["Continent"], loc = "best",
               fontsize=8, bbox_to_anchor= (2.0, 1.0))
    plt.xlim(0)
    plt.savefig('Population_Distribution')
    plt.show()

#Declaring an array with the player names for labeling using for loop
playerName = ["Messi" , "Ronaldo"]

#Declaring an array with regions for labeling using for loop
regions = ["US & Canada" , "EMEA" , "Latin America" , "Asia-Pacific"]

#Calling funtion to plot Netflix Revenue
netflix_revenue()

#Calling function to plot Population Density
population_density()

#Calling function to plot Player Comparison
player_comparison()

#Calling function to plot Player Statistics
messi_stats()
