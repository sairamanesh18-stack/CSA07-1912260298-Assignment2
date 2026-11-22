# CSA07 Assignment 2 - Computer Networks (CO2)

Name: Sai Ramanesh
Register number: 1912260298
OS: macOS 15.4.1
Python: 3.14.0
Simulation tool: Cisco Packet Tracer (not used for the submitted programs)

## Programs

| Question | Folder | Program | Screenshot |
|---|---|---|---|
| Q2 - Route summarisation | `Q2/` | `Q2/Q2_summarise.py` | `screenshots/CO2_Q2_Route_Summarisation.png` |
| Q4 - Distance-vector routing | `Q4/` | `Q4/Q4_distance_vector.py` | `screenshots/CO2_Q4_Distance_Vector.png` |

Each folder contains the Python program and the captured `output.txt`.

## How to run

    python3 Q2/Q2_summarise.py
    python3 Q4/Q4_distance_vector.py

## Results

- Q2: summary routes `172.18.24.0/22`, `172.18.24.0/21` and `10.4.0.0/22`; the output matches the expected result in the assignment.
- Q4: distance-vector tables converge after 3 rounds; P reaches Q via R at cost 3, and the output matches the expected result.

## Notes

The PDF provides Complete-the-Code programs only for Q2 (route summarisation) and Q4 (distance-vector). Q1, Q3, Q5, Q6 and Q7 are calculation, written-analysis or Packet Tracer tasks and have no Python program in the PDF. Q3 also requires a Cisco IOS floating static route configuration.
