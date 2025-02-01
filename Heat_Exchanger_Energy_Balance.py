def heat_transfer(m, Cp, T_in, T_out):
    """Calculates heat transfer in a heat exchanger."""
    return m * Cp * (T_out - T_in)

# Example usage:
mass_flow_rate = 45.93  # kg/s
specific_heat = 44.92 # kJ/kg·K 
T_in = 20  # °C
T_out = 80  # °C

Q = heat_transfer(mass_flow_rate, specific_heat, T_in, T_out)
print(f"Heat Transferred: {Q:.2f} kJ/s")
