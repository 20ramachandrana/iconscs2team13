import numpy as np
import matplotlib.pyplot as plt

#### Global Variables ####
#mainly used by functions as initial conditions/constants
start_year = 2021
end_year = 2030

#For determining Energy -- increase in MWhr / year
slope_E = 6.92*10**6

## inital conditions for determining percentages ##

#format for arrays is [<Coal>, <Natural Gas>, <Solar>, <Wind>, <Nuclear>, <Winter NG>]
initial_percentages = np.array([19.3, 53.6, 0.9, 17.5, 8.7, 0])

derivative_sources = np.array([-1.89, 0, 0.0976, 1.29, -0.116, 0])
#note - NG will be taken as slack in calculation, so value is NA
#rate for winter NG is zero by default

sec_derivative_sources = np.zeros(6)
#all zero by default











#### Functions ####
#naming convention -- mix of underscore and camal case
#array/matrix indicated by "a" followed by the the quantity in camal case


def get_aYear(start_year=start_year, end_year=end_year, size=1000):
    '''returns an array for the time in years with default of 1000 samples'''
    return np.linspace(start_year, end_year, size)


def get_aEnergy(aYear, dirE=slope_E):
    '''returns an array for the energy production each year, uses default slope from trendline'''
    #compute size of array
    size = len(aYear)

    #use formula generate array
    aEnergy = dirE*aYear - 1.35*10**10
    return aEnergy


def get_aPercentSources(aYear, initial_percentages=initial_percentages, derivative_sources=derivative_sources, sec_derivative_sources=sec_derivative_sources):
    '''returns a matrix for the percentages of the 6 sources (coal, NG, solar, wind, nuclear, winter NG), based on years and initial conditions
    initial conditions are by default: 2nd derivative set to zero, inital percentages from 2019, 1st derivatives from linear trends'''
    size = (len(aYear),6) #size will be matrix with rows equal to samples in years, columns for each source
    aPercentSources = np.zeros(size) #initalize matrix
    P = initial_percentages #initalize sub-array which will be used calculate percentages in each row
    
    #interatve over all time samples in aYear
    for i in range(len(aYear)):
        #determine sub-array value
        P = 0.5*(sec_derivative_sources)*aYear[i]**2 + derivative_sources*aYear[i] + initial_percentages

        #first check if percentage for NG will stay positive
        if 100-np.sum(P) >= 0:
            aPercentSources[i,:] = P
        
            #determine NG as slack
            

        else: #set this row to previous value (i.e. keep P constant)
        


def get_aReliability(aYear, aEnergy, aPercentSources):
    '''returns array for the reliability score for a given set of years, energy production, and percent distribution of sources'''





#### Test of Module ####



if __name__ == "__main__":
