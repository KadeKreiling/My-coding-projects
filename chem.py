import math as m
import csv
import numpy as n

import sci
import stoich as st

PERIODIC_TABLE = []
with open('Periodic Table of Elements.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
      PERIODIC_TABLE.append(lines)



class Chem(sci.Science, st.Stoich):
    def __init__(self):
        self.pd = PERIODIC_TABLE
        self.agravado = 6.0221419947 * 10 ** 23

    def __str__(self):
        return """this class is used to solve all formulas for basic chemistry problem 
        - this class has the periodic table imported in as a csv file
        - molecular_function allows you to find the molecular mass of an molecule
           -input first element name, number of molecules for element 1..... and so on
           -up to 5 different elements 
        -molarity class allows you to find the molarity of a solution
           - input the sample mass, total mass, and volume in liters
        -multiply by avogadro class mutliplies anything by avogadros number.
           -returns answer in scientific notation
        """
    def molecular_mass(self, element1, num_molecules1, element2=None, num_molecules2=None, element3=None,
                       num_molecules3=None, element4=None, num_molecules4=None, element5=None, num_molecules5=None):
        # Capitalize the first element
        element1 = str(element1).capitalize()

        # Build list of elements based on provided input
        list_elements = [element1]
        if element2:
            list_elements.append(str(element2).capitalize())
        if element3:
            list_elements.append(str(element3).capitalize())
        if element4:
            list_elements.append(str(element4).capitalize())
        if element5:
            list_elements.append(str(element5).capitalize())

        # Create the molecule count list corresponding to the elements
        molecule_counts = [num_molecules1]
        if element2:
            molecule_counts.append(num_molecules2)
        if element3:
            molecule_counts.append(num_molecules3)
        if element4:
            molecule_counts.append(num_molecules4)
        if element5:
            molecule_counts.append(num_molecules5)

        # Initialize the element mass list
        element_mass_list = []

        # Loop over the elements and find their mass from self.pd
        for element in list_elements:
            found = False  # Track if element is found
            for elements in Chem().pd:
                if element == elements[2]:  # Assuming elements[2] holds element symbol/name
                    element_mass_list.append(float(elements[3]))
                    found = True
                    break

            # If element is not found, raise an appropriate error
            if not found:
                raise ValueError(f"Element '{element}' not found in the periodic data.")

        # Multiply the masses by the corresponding number of molecules
        for i in range(len(element_mass_list)):
            element_mass_list[i] *= molecule_counts[i]

        # Return the sum of the molecular masses
        return sum(element_mass_list)

    def molarity(self, sample_mass, total_mass, volume_liters):
        """
        Calculate the molarity of a solution.

        :param sample_mass: The mass of the sample (solute) in grams
        :param total_mass: The total mass of the solution (solute + solvent) in grams
        :param volume_liters: The volume of the solution in liters
        :return: The molarity of the solution
        """

        if total_mass == 0 or volume_liters == 0:
            raise ValueError("Total mass and volume of solute must be greater than zero.")

        # Calculate the molarity
        molarity_value = (sample_mass / total_mass) / volume_liters

        return molarity_value

    def multiply_by_agravado(self, other):
        return other * self.agravado

    def divide_by_agravado(self, other):
        return other / self.agravado