import os
import sys
import traci
from sumolib import checkBinary  # Do sprawdzenia binarki SUMO
import matplotlib.pyplot as plt

sumoBinary = checkBinary('sumo')
sumoCmd20 = [sumoBinary, "-c", "20/custom_20.sumocfg"]
sumoCmd30 = [sumoBinary, "-c", "30/custom_30.sumocfg"]
sumoCmd40 = [sumoBinary, "-c", "40/custom_40.sumocfg"]
sumoCmd50 = [sumoBinary, "-c", "50/custom_50.sumocfg"]
sumoCmd60 = [sumoBinary, "-c", "60/custom_60.sumocfg"]
sumoCmd70 = [sumoBinary, "-c", "70/custom_70.sumocfg"]


def get_statistics(sumoCmd):

    traci.start(sumoCmd)
    steps = []
    stopped_vehicles_counts = []
    stopped_at_red_counts = []

    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        vehicles = traci.vehicle.getIDList()
        stopped_count = sum(1 for v in vehicles if traci.vehicle.getSpeed(v) < 0.1)
        stopped_at_red_count = 0

        # Zliczanie pojazdów stojących na czerwonym świetle
        for tlsID in traci.trafficlight.getIDList():
            controlled_lanes = traci.trafficlight.getControlledLanes(tlsID)
            for lane in controlled_lanes:
                if 'r' in traci.trafficlight.getRedYellowGreenState(tlsID):
                    stopped_at_red_count += traci.lane.getLastStepHaltingNumber(lane)

        steps.append(traci.simulation.getTime())
        stopped_vehicles_counts.append(stopped_count)
        stopped_at_red_counts.append(stopped_at_red_count)

    traci.close()
    return steps, stopped_vehicles_counts, stopped_at_red_counts


def plot_vehicles(statistics, speed):
    plt.figure(figsize=(12, 6))

    plt.plot(statistics[0], statistics[1], linestyle='-', color='b', label='Stopped Vehicles')
    plt.plot(statistics[0], statistics[2], linestyle='--', color='r', label='Stopped at Red Light')

    plt.title(f'Number of Stopped Vehicles per Simulation Step for speed: {speed}km/h')
    plt.xlabel('Simulation Time (seconds)')
    plt.ylabel('Number of Stopped Vehicles')
    plt.legend()
    plt.grid(True)
    plt.ylim(0, 100)
    plt.show()


if __name__ == "__main__":
    statistics_20 = get_statistics(sumoCmd20)
    statistics_30 = get_statistics(sumoCmd30)
    statistics_40 = get_statistics(sumoCmd40)
    statistics_50 = get_statistics(sumoCmd50)
    statistics_60 = get_statistics(sumoCmd60)
    statistics_70 = get_statistics(sumoCmd70)
    plot_vehicles(statistics_20, "20")
    plot_vehicles(statistics_30, "30")
    plot_vehicles(statistics_40, "40")
    plot_vehicles(statistics_50, "50")
    plot_vehicles(statistics_60, "60")
    plot_vehicles(statistics_70, "70")
    # print(f"Statystyki dla 20km/h. Pojazdy stojące w miejscu: {statistics_20[0]}, pojazdy stojące na czerwonym świetle: {statistics_20[1]}")
    # print(f"Statystyki dla 30km/h. Pojazdy stojące w miejscu: {statistics_30[0]}, pojazdy stojące na czerwonym świetle: {statistics_30[1]}")
    # print(f"Statystyki dla 40km/h. Pojazdy stojące w miejscu: {statistics_40[0]}, pojazdy stojące na czerwonym świetle: {statistics_40[1]}")
    # print(f"Statystyki dla 50km/h. Pojazdy stojące w miejscu: {statistics_50[0]}, pojazdy stojące na czerwonym świetle: {statistics_50[1]}")
    # print(f"Statystyki dla 60km/h. Pojazdy stojące w miejscu: {statistics_60[0]}, pojazdy stojące na czerwonym świetle: {statistics_60[1]}")
    # print(f"Statystyki dla 70km/h. Pojazdy stojące w miejscu: {statistics_70[0]}, pojazdy stojące na czerwonym świetle: {statistics_70[1]}")
