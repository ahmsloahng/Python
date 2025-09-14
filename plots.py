# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 07:58:28 2025

@author: Amlan Ghosh
"""
import matplotlib.pyplot as plt

class Plot:
    
    def _init_(self,df):
        self.df = df
    
    '''1. Forest plot -> Matplotlib'''
    def forest_plot(self):
        
        '''Input: dataframe with columns Factors,AOR, Lower CI and Upper CI'''
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Plot Individual Variables
        for i in range(len(self.df)):
            variable_name = self.df['Factors'].iloc[i]
            aor = self.df['AOR'].iloc[i]
            lower_ci = self.df['Lower CI'].iloc[i]
            upper_ci = self.df['Upper CI'].iloc[i]
        
            # Plot the confidence interval as a horizontal line
            ax.hlines(y=variable_name, xmin=lower_ci, xmax=upper_ci, 
                      color='gray', linestyle='-')
            
            # Plot the adjusted odds ratio (AOR) as a marker
            ax.plot(aor, variable_name, 's', color='black', markersize=8)
        
        # Add Reference Line and Labels
        # Add a vertical reference line at 1.0 (no effect)
        ax.axvline(x=1.0, color='black', linestyle='--', label='No Effect Line')
        
        # Customize the Plot
        ax.set_title('Forest Plot of Variables', fontsize=16)
        ax.set_xlabel('Adjusted Odds Ratio (AOR)', fontsize=12)
        ax.tick_params(axis='x', labelsize=10)
        ax.tick_params(axis='y', labelsize=10)
        
        # Optional: Set x-axis limits
        ax.set_xlim(0.95, 2.43)
        
        # Show the plot
        plt.grid(axis='x', linestyle='--', alpha=0.7)
        plt.legend()
        plt.tight_layout()
        plt.show()