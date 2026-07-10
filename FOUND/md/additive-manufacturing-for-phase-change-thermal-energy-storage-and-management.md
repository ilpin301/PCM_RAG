---
Title: "Additive Manufacturing for Phase Change Thermal Energy Storage and Management - Scholarly Commons"
Author: "Unknown"
Reference: "https://commons.erau.edu/cgi/viewcontent.cgi?params=/context/edt/article/1755/&path_info=Dissertation.pdf"
ContentType:
  - "pdf"
Created: 2026-06-17
Processed: true
tags:
  - "source"
---

https://lh3.googleusercontent.com/notebooklm/AKXwDQGSyPjMTSqbjiI4bPbXwk-sc5kHpCP2Uf75n1Wbn3YNApYF9EUE52U1CERjsuBfR-sRQz8f0UcPuZ0X5duCABcKtBbTCUSQKAKfI5cQHTmJ8urI9y2fcOob_a0baDmgeE8p4MZzcw=w1280-h299-v0
74a6cda9-a768-492a-a9c9-f9151d889f40
https://lh3.googleusercontent.com/notebooklm/AKXwDQFMJJM0nHJZq2uJSCMFyWEZ9sTjvzHzd8hi3PMchKiwzCFpSZYWz8D8a3zF8jIEwRCsFpA9RPFUdtADkdIE0nZB2b45FqGt5b_9YVL7tA-X5djw29Mjx-WwSZ2bY0YtJ_bf0-6aJQ=w540-h557-v0
a42a3354-7660-4fd6-86bf-cd6fbd16a7bd
Doctoral Dissertations and Master's Theses 
Spring 2023 
Additive Manufacturing for Phase Change Thermal Energy 
Storage and Management 
Thomas B. Freeman Embry-Riddle Aeronautical University, freemat1@my.erau.edu 
Follow this and additional works at: https://commons.erau.edu/edt 
 Part of the Energy Systems Commons, Heat Transfer, Combustion Commons, and the Polymer and 
Organic Materials Commons 
Scholarly Commons Citation Freeman, Thomas B., "Additive Manufacturing for Phase Change Thermal Energy Storage and Management" (2023). Doctoral Dissertations and Master's Theses. 733. https://commons.erau.edu/edt/733 
This Dissertation - Open Access is brought to you for free and open access by Scholarly Commons. It has been accepted for inclusion in Doctoral Dissertations and Master's Theses by an authorized administrator of Scholarly Commons. For more information, please contact commons@erau.edu. 
Additive Manufacturing for Phase Change Thermal Energy Storage and 
Management 
by 
Thomas B. Freeman 
A Dissertation Submitted to the College of Engineering Department of Mechanical 
Engineering in Partial Fulfillment of the Requirements for the Degree of 
Doctor of Philosophy in Mechanical Engineering 
Embry-Riddle Aeronautical University 
Daytona Beach, Florida 
May 2023
  
Additive Manufacturing for Phase Change Thermal Energy Storage and Management 
 
 
by 
 
 
Thomas B. Freeman 
 
 
 
This dissertation was prepared under the direction of the candidate’s Dissertation 
Committee Chair, Dr. Sandra K.S. Boetcher, Professor, Daytona Beach Campus, and 
Dissertation Committee Members Dr. Rafael M. Rodriguez, Professor, Daytona Beach 
Campus,  Dr. Mark A. Ricklick, Professor, Daytona Beach Campus, Dr. Eduardo A. Divo, 
Professor, Daytona Beach Campus, and Dr. Patrick N. Currier, Professor, Daytona Beach 
Campus,  and has been approved by the Dissertation Committee.  It was submitted to the 
Department of Mechanical Engineering in partial fulfillment of the requirements for the 
degree of Doctor of Philosophy in Mechanical Engineering 
 
 
 
Dissertation Review Committee: 
 
____________________________________ 
Sandra Boetcher, Ph.D. 
Committee Chair 
 
_________________________________ 
Rafael Rodriguez, Ph.D. 
Committee Member 
 
_________________________________ 
Eduardo Divo, Ph.D. 
Committee Member 
 
________________________________ 
Eric Coyle, Ph.D. 
Ph.D. Program Chair, 
Mechanical Engineering 
 
________________________________ 
James Gregory, Ph.D. 
Dean, College of Engineering 
 
    _______________________________ 
Mark Ricklick, Ph.D. 
Committee Member 
 
    _______________________________ 
Patrick Currier, Ph.D. 
Committee Member 
 
_______________________________ 
Patrick Currier, Ph.D. 
Department Chair, 
Mechanical Engineering  
 
_______________________________ 
Lon Moeller, J.D. 
Senior Vice President for Academic 
Affairs and Provost 
 
ABSTRACT 
Researcher: Thomas B. Freeman 
Title: Additive Manufacturing for Phase Change Thermal Energy 
Storage and Management 
Institution: Embry-Riddle Aeronautical University 
Degree: Doctor of Philosophy in Mechanical Engineering 
Year: 2023 
Phase change materials can enhance the performance of energy systems by time 
shifting or reducing peak thermal loads. Certain electronic devices such as batteries, 
laser systems, or electric vehicle power electronics are highly transient and require 
pulse heat dissipation. Heat sinks, or thermal management devices made of a 
phase change material can absorb large heat spikes while maintaining a constant 
temperature. Additive manufacturing techniques hold tremendous potential to 
enable co-optimization of material properties and device geometry, while potentially 
reducing material waste and manufacturing time. Recently, a few efforts have 
emerged that employ additive manufacturing techniques to integrate a phase change 
material thermal energy storage into geometrically complex designs for advanced 
thermal management. This work contributes to the emerging field of research by 
reporting on the production of composite thermoplastic/phase change material 
filaments for fused filament fabrication 3D-printing, and their subsequent use to 
3D-print advanced heat exchange topologies with intricate geometric features. 
3
TABLE OF CONTENTS 
ABSTRACT 3 
LIST OF FIGURES 11 
LIST OF TABLES 13 
NOMENCLATURE 14 
1 Introduction 1 
1.1 Review of Relevant Literature 3 
1.1.1 Fundamentals of PCMs 3 
1.1.2 Organic PCMs 4 
1.1.3 Inorganic PCMs 7 
1.1.4 Eutectic Mixtures 10 
1.1.5 Summary of PCM Types 10 
1.2 Applications of PCMS 13 
1.2.1 Building Applications 15 
1.2.2 Thermal Management 17 
1.2.3 Power Systems and Industrial Processes 18 
1.3 Advanced Manufacturing with Phase Change Materials 19 
1.4 Review of PCMs and Composites used in Additive Manufacturing 22 
1.4.1 PCMs and Matrix Materials Used in AM 22 
1.4.2 Thermal Conductivity Enhancement 29 
1.4.3 Advanced Manufacturing for Integrating PCMs into Devices 35 
1.5 Commercially Available Materials and Systems 37 
1.5.1 Phase Change Material Manufacturers 37 
1.5.2 Water-Based Systems 38 
1.5.3 PCMs for Heating Applications 39 
4
1.5.4 PCMs for Cooling Applications 40 
1.5.5 Wearable Technology 41 
1.5.6 Thermally Conductive Scaffolds 41 
1.6 Perspective on Future Directions 42 
1.7 Relevent Literature: PCM Modeling 45 
2 HDPE/PCM Composite Filament 49 
2.1 Materials and Manufacturing Methods 49 
2.1.1 Materials 49 
2.1.2 Filament Fabrication 49 
2.1.3 Additive Manufacturing 53 
2.1.4 Molding of Bulk Samples 56 
2.2 Experimental Methods 57 
2.2.1 Differential Scanning Calorimetry 57 
2.2.2 Thermal Conductivity Measurements 59 
2.3 Microscopy 60 
2.4 Results and Discussion 60 
2.4.1 Phase-Change Temperature and Latent Heat of Fusion 60 
2.4.2 Thermal Conductivity 62 
2.5 Microstructure Visualization 64 
3 Moisture affinity of HDPE/PCM composites 67 
3.1 Sample Preparation 67 
3.2 Microscopy 67 
3.3 Dynamic Vapor Sorption 68 
3.4 Steady-State Adsorption/Desorption Capacity 70 
3.5 Transient Adsorption/Desorption Analysis 71 
3.6 Results and Discussion 72 
5
4 Microencapsulated PCM and Thermoplastic Polyurethane Compos-
ites 76 
4.1 Characterization of MEPCM-TPU Pellets and Filaments 76 
4.1.1 Raw Materials 76 
4.1.2 Single Screw Extruded MEPCM-TPU Pellets 77 
4.1.3 Twin Screw Extruded MEPCM-TPU Pellets 78 
4.1.4 Extrusion of MEPCM-TPU pellets into Filament 80 
4.2 Characterization of MEPCM-TPU Powder and Filaments 83 
4.2.1 Raw Materials 83 
4.2.2 Single Screw Extusion of MEPCM-TPU Powder 83 
5 Numerical Modeling for PCM Melting 87 
5.1 Methodology 87 
5.2 Finite-Volume Numerical Simulations 87 
5.2.1 Physical Model 88 
5.2.2 Governing Equations 91 
5.2.3 Mesh and Time-Step Size 93 
5.3 Finite Difference Model 94 
5.3.1 Heat Transfer Coefficient 95 
5.4 Results 96 
5.4.1 Validation with imposed constant power 96 
5.4.2 Constant Inlet Temperature Condition 97 
6 Conclusions 105 
6.1 HDPE/PCM Composite 105 
6.2 MEPCM/TPU Composite 106 
6.3 Numerical Modeling 106 
REFERENCES 108 
6
LIST OF FIGURES 
Figure Page 
1.1 Characterization of thermal energy storage materials. 1 
1.2 Latent heat of fusion and energy density versus phase transition tem-
perature for the various PCM categories. 13 
1.3 Comparison of PCM properties. 14 
1.4 Common applications for PCMs across the temperature range of in-
terest and the ability of PCMs to provide benefits to said applications. 15 
1.5 Potential implementations of TES within building applications. 16 
1.6 The performance of a thermal energy storage component in terms 
of energy and power density with different levels of enhancement, 
attainable using additive manufacturing. Panels (a) and (b) show 
Ragone plots for a round tube surrounded by PCM. The black curve 
shows the baseline case with a pure PCM, and the (a) red and (b) 
blue curves show different levels of conductivity and geometric en-
hancement, respectively. The energy density at three different power 
density levels (shown on the y-axis in (a) and (b)) is plotted for dif-
ferent enhancement schemes in (c). Note – the energy density is 
shown on the x-axis in the Ragone plots and on the y-axis in (c). 
The dashed black line in all three plots represents the maximum pos-
sible energy density, which is simply the energy storage capacity of 
the material alone with no flow channels or conductive additives. 21 
7
1.7 Graphical depiction of common additive manufacturing methods; 
a) selective laser sintering (SLS), also known as selective laser melt-
ing (SLM); b) fused filament fabrication (FFF), also known as fused 
deposition modeling (FDM); c) stereolithography (SLA); and d) di-
rect ink writing (DIW). Varying forms of AM materials with different 
methods to incorporate PCMs into the matrix. 23 
1.8 Graphical timeline displaying major events in the commercialization 
of PCM and PCM-integrated products. 38 
1.9 Vision for the future of TES heat exchangers with respect to magni-
tude of length scales and surface-area-to-volume ratios. 44 
1.10 Energy density of various PCM categories with applications and 
DOE BTO target energy density. 45 
2.1 Comparison of filament with (a) a consistent diameter and (b) an 
inconsistent diameter. 51 
2.2 Filament diameter, utilizing optimum settings and a clean extruder 
screw, versus time for (a) pure HDPE and (b) the PCM42/HDPE 
composite. 52 
2.3 Optimal extruder settings for pure HDPE (200 ◦C and 5 RPM) and 
the PCM42/HDPE composite (190 ◦C and 4 RPM). 52 
2.4 Schematic diagram of the material deposition process. 53 
2.5 Curling causing layer separation and delamination of a print sample 
prior to implementation of the heated build environment. 55 
2.6 3D printer enclosed in an elevated-temperature environment. 56 
2.7 Images of the samples (25-mm diameter and 4-mm thick) showing 
(a) printed HDPE, (b) printed PCM42/HDPE composite, (c) molded 
HDPE, and (d) molded PCM42/HDPE composite. 57 
8
2.8 Heat flow versus temperature diagram illustrating latent heat of fu-
sion, onset, endset, and peak temperatures. The first peak represents 
the PCM42 phase change and the second peak represents the HDPE 
phase change. 58 
2.9 Hot Disk TPS operation setup. The Kapton sensor is sandwiched 
between two bulk PCM42/HDPE composite samples. 59 
2.10 Heatflow versus temperature for pure PCM42, pure HDPE, and the 
PCM42/HDPE composite filament. 61 
2.11 Thermal conductivity (average of each sample measured ten times) of 
the molded and printed samples. The error bars represent the stan-
dard deviation. 63 
2.12 PCM42/HDPE composite filament (a) scale bar 100 
µm 
and (b) 
scale bar 50 
µm. 
65 
2.13 Printed samples (a) PCM42/HDPE composite scale bar 500 
µm, 
(b) 
PCM42/HDPE composite scale bar 200 
µm, 
(c) HDPE scale bar 500 
µm, 
and (d) HDPE scale bar 200 
µm. 
66 
3.1 Microstructure visualization of HDPE with PureTemp 42 (50% PCM 
by mass) at 25 ◦C (a) image showing edge of filament, and (b) view 
showing HDPE (platelet-like structures) and PCM (lattice-like struc-
tures). 68 
3.2 Components of the experimental setup. 69 
3.3 Experimental procedure to establish adsorption/desorption isotherms. 70 
3.4 Transient experimental procedure to establish the diffusion coefficients. 71 
3.5 Adsorption/desorption isotherms for pure PCM at 25 and 35 ◦C. 73 
3.6 Adsorption/desorption isotherms for pure HDPE at 25, 35, and 45 ◦C. 73 
3.7 Adsorption/desorption isotherms for 50/50 composite at 25 and 35 ◦C. 74 
9
4.1 Micrographs of the MEPCM spheres showing the size distribution. 76 
4.2 Thermal decomposition profiles for (a) MEPCM and (b) 80A TPU 77 
4.3 SEM micrographs of TPU-MEPCM pellets produced from multiple 
compounding steps using a single screw extruder. (a) macroscopic 
image of 60 wt% MEPCM in TPU, (b-d) 80 wt% MEPCM in TPU 
emphasizing the encapsulated PCM. 78 
4.4 Thermal decomposition profiles for (a) 60 wt% MEPCM-TPU and 
(b) 80 wt% MEPCM-TPU produced from multiple compounding 
steps using a single screw extruder. 79 
4.5 SEM micrographs of MEPCM-TPU pellets produced using a twin 
screw extruder. (a,b) Images of 50 wt% MEPCM in TPU, (c,d) 60 
wt% MEPCM in TPU. 80 
4.6 Thermal decomposition profiles for (a) 50 wt% MEPCM-TPU and 
(b) 60 wt% MEPCM-TPU produced from one compounding step us-
ing a twin screw extruder. 81 
4.7 Extrusion profile for extruding TPU on a Precision 350 filament ex-
truder. 81 
4.8 Printed samples of MEPCM-TPU. (A-C) 50wt% MEPCM and (D-F) 
60wt%MEPCM 83 
4.9 Micrographs of (A) MEPCM and (B) TPU powder 84 
4.10 Extrusion profile for extruding MEPCM and TPU powder. 84 
4.11 Surface images of (A) 40wt% MEPCM, (B) 50wt% MEPCM, (C) 
60wt% MEPCM, and (D) 70wt% MEPCM 85 
4.12 Micrographs of 60wt% MEPCM Filament 85 
5.1 (a) 3D schematic of PCM test section with microchannel fluid array, 
(b) 2D domains and dimensions for FVM 89 
5.2 Tetradecane graphite matrix specific heat as a function of temperature 91 
10
5.3 Material Properties of 20% concentration of propylene glycol in water 
as a function of temperature. 92 
5.4 Outlet temperature for experiment, finite difference, and finite vol-
ume with the constant power setup 97 
5.5 Comparison of Matlab and Fluent model with contour plots of melt 
front and local wall and fluid data at 10 minutes. 98 
5.6 Comparison of Matlab and Fluent model with contour plots of melt 
front and local wall and fluid data at 35 minutes. 99 
5.7 Comparison of Matlab and Fluent model with contour plots of melt 
front and local wall and fluid data at 60 minutes. 100 
5.8 All local nusselt numbers for constant inlet temperature case in flu-
ent model. 101 
5.9 Illustration of inactive zone for melting of PCM. 101 
5.10 Local Nusselt number, wall temperature, bulk temperature, and 
wall heat flux from Fluent model with corresponding contour plot 
of PCM domain at time = 55 min. 102 
5.11 Local Nusselt number for various timesteps with contant wall tem-
perature and constant wall heat flux correlations, (a) timesteps at 
33min and below (pre-inactive zone), (b) timesteps at 35min and 
above (post-inactive zone) 103 
5.12 (a) Demonstrative figure for thermal boundary layer development 
with melt front spanning full length of fluid channel, (b) Demonstra-
tive figure for thermal boundary layer development with simultane-
ous movement of melt front and inactive zone 104 
11
LIST OF TABLES 
Table Page 
1.1 Advantages and disadvantages of organic and inorganic PCMs 4 
1.2 Paraffin PCMs for TES applications 5 
1.3 Organic Non-Paraffins for TES applications 6 
1.4 Salts for TES applications 8 
1.5 Salts hydrates for TES applications 9 
1.6 Salt-water solutions for low temperature TES application 10 
1.7 Metlas/Metal alloys for TES applications 11 
1.8 Organic-Organic eutectic mixtures for TES applications 11 
1.9 Inorganic-Inorganic eutectic mixtures for TES applications 12 
2.1 Print Settings 54 
2.2 Phase-change temperature and latent heat of fusion of the PCM42/HDPE 
composite filament. 60 
2.3 Thermal conductivity (average of each sample measured ten times) of 
the molded and printed samples. 63 
3.1 Adsorption/desorption diffusion coefficients. 75 
4.1 Summarized Thermal Transition Properties of MEPCM-TPU Pellets 78 
4.2 Summarized Thermal Transition Properties of MEPCM-TPU Pellets 
extruded on the 3devo. 82 
4.3 Print settings for MEPCM-TPU filament 82 
4.4 Summarized Thermal Transition Properties of MEPCM-TPU printed 
samples. 82 
4.5 DSC characterization of MEPCM ratios of powder mixtures, fila-
ments, and prints 86 
12
5.1 PCM Material Properties 90 
5.2 Aluminum Material Properties 90 
13
NOMENCLATURE 
c̄p 
Average Specific Heat [J/kgK] 
k̄ 
Average Thermal Conductivity [W/mK] 
N̄u 
Average Nusselt Number 
ṁ 
Mass Flow Rate [kg/sec] 
Q̇ 
Power [W] 
ρ 
Density [kg/m3] 
cp 
Specific Heat [J/kgK] 
Dh 
Hydraulic Diameter [m] 
H 
Height [m] 
h 
Enthalpy [J/kg] 
hsl 
Latent Heat of Fusion [J/kg] 
hsl 
Latent Heat of Fusion [kJ/kg] 
htc 
Heat Transfer Coefficient [W/m2K] 
k 
Thermal Conductivity [W/mK] 
k 
Thermal Conductivity [W/mK] 
L 
Length [m] 
Nu 
Nusselt Number 
P 
Pressure [Pa] 
q′′ 
Heat Flux [W/m2] 
14
R 
Resistance [K/W] 
T 
Temperature [K] 
t 
Thickness [m] 
v 
Velocity [m/s] 
W 
Width [m] 
15
https://lh3.googleusercontent.com/notebooklm/AKXwDQECfZ5z8Ck9F_Cv8eo2tuHxaICYeE8cTUPlS554skYuGddObWBD_FECnmsx6zW0fnt3LopLwGDEK55GKaXcNa0M2Ivh-e5GA83GzvrDWy4UIoEcZ7_tD_0lwd9WSZfkNd7nLcHf=w685-h475-v0
9060a20b-1a7a-496f-8d7f-087b1d8f534d
1 Introduction 
There is an urgent need to decarbonize our energy systems to mitigate the 
effects of climate change [1]. Doing so will require the rapid deployment of clean 
energy generation such as solar and wind [2]. However, the inherent intermittency 
of such sources requires co-deployment of scalable, affordable, and sustainable en-
ergy storage technologies [3]. Over the years, several methods to store large quan-
tities of energy have been developed, each at its own level of readiness, and set of 
advantages and drawbacks [4–7]. Of these options, thermal energy storage (TES) 
systems are of particular interest due to their potential for low cost and long life-
time. As shown in Figure 1.1, materials used for TES can be classified into three 
categories: materials that store heat sensibly, materials that store heat via a latent 
phase transformation, and materials that store heat via a thermochemical reaction. 
Many authors have presented comparisons as well as advantages and disadvantages 
of sensible [8], latent [9, 10], and thermochemical energy storage [11–13]. 
Figure 1.1 Characterization of thermal energy storage materials. 
Latent heat storage materials, also known as phase-change materials (PCMs) 
1
are a class of TES materials that have great potential for a variety of thermal man-
agement applications because of their ability to store latent heat over a near con-
stant temperature [14]. In these materials, heat can be stored using a variety of 
phase transitions, including gas-liquid, solid-gas, solid-solid, and solid-liquid. PCMs 
involving a gas phase are generally not of great interest to the thermal energy stor-
age community, as they suffer from very low energy density because the gaseous 
phase occupying a large volume[15]. Similarly, solid-solid phase transitions typically 
occur as a material undergoes a transition from one crystalline phase (polymorph) 
to another, or from a crystalline to amorphous phase, and consequently are also 
limited in energy density [16]. As such, solid-liquid PCMs are most compelling in 
terms of energy density and will be the primary focus of this review. 
The effectiveness of a PCM is defined by its energy and power density—the 
total available storage capacity (kWh) and how fast it can be accessed (kW). These 
are influenced by both material properties and device geometry; however, prior ef-
forts have primarily focused on improving material properties, namely, maximiz-
ing latent heat of fusion and increasing thermal conductivity [17–19]. The latter 
is often at the expense of the former, as most efforts attempt to improve thermal 
conductivity by combining a thermally conductive material with the PCM to cre-
ate a composite. The thermally conductive material does not participate in phase 
change, and thus displaces PCM volume. Advanced manufacturing techniques hold 
tremendous potential to enable co-optimization of material properties and device 
geometry, while potentially reducing material waste and manufacturing time. There 
is an emerging body of research focused on additive manufacturing of PCM com-
posites and devices for TES. The state-of-the art of solid-liquid PCMs with tran-
sition temperature between -50 °C to 400 °C, spanning a wide range of potential 
applications from refrigeration to concentrated solar power plants. Various classes 
of PCMs, their material properties, advantages/disadvantages are reviewed, and an 
2
overview of the application field of use for these materials is presented. Secondly, 
a comprehensive review of recent additive manufacturing (AM) enabled advances 
in latent heat TES, which has the potential to transform the field by enabling co-
optimization of material properties and device geometry. Lastly, a forward-looking 
perspective on potential future directions of advanced materials and manufacturing 
of PCM composites for TES and thermal management is provided. 
1.1 Review of Relevant Literature 
1.1.1 Fundamentals of PCMs 
Solid-liquid PCMs are either organic, inorganic, or a eutectic (combination) 
of two organic or inorganic PCMs. Organic PCMs include paraffins [20], sugar al-
cohols [21], and fatty acids along with their alcohol and ester derivatives [22]. In-
organic PCMs include salts [23], salt hydrates [24], and metals [25]. Eutectics are 
typically combinations of two or more organic and/or inorganic PCMs [26, 27]. In-
organic PCMs generally have higher energy density/specific energy, higher thermal 
conductivity, lower cost (except for metals), and are naturally occurring (except for 
metals). However, they are often corrosive, and tend to suffer from materials chal-
lenges such as supercooling [28, 29] and phase separation [29], which limit reliability 
in end-use. Except for sugar alcohols, organic PCMs do not supercool. They are 
also usually single-component materials which are not prone to phase separation. 
However, they are often petroleum or bio-derived which leads to higher costs and 
not bio-friendly. They typically have lower energy density/specific energy and are 
often flammable. In general, organic PCMs are easier to incorporate into AM work-
flows because they are easier to microencapsulate, are stable at higher temperatures 
(which is required by some AM processes), are not corrosive to metals, and do not 
run a risk of phase separating during AM processing. Some advantages and disad-
vantages of organic versus inorganic PCMs are shown in Table 1.1. For many ap-
plications, the PCM transition temperature may be the first/most important PCM 
3
selection criteria as some PCM types do not have a wide range of available tran-
sition temperatures. Salt hydrates, for example, are typically not available above 
transition temperatures of 100 °C. Sugar alcohols are typically not available below 
transition temperatures of 80 °C. 
Table 1.1 Advantages and disadvantages of organic and inorganic PCMs 
Organic Inorganic 
Advantages - Not corrosive - High energy density - Little-to-no supercooling - Higher thermal conductivity - Chemically and thermally stable - Lower cost - Wide range of transition temperature - Non-flammable 
- Naturally occurring Disadvantages - Low energy density - Prone to supercooling 
- Low thermal conductivity - Prone to phase separation - Often flammable - Often corrosive - Often petroleum based 
1.1.2 Organic PCMs 
This section covers a brief overview of the various organic PCMs within paraf-
fins and non-paraffins (esters, sugar alcohols, fatty acids, etc.). The most common 
characteristics of each of these groups will be discussed, along with a comprehen-
sive list of the phase transition temperatures, latent heats, and energy densities of 
the specific materials. Organic PCMs lend themselves well to processing via AM 
because they are available in microencapsulated forms, are stable at higher temper-
atures relative to salt-hydrates and salt-water solutions, and do not phase separate. 
Paraffins 
Paraffin waxes consist of a mixture of linear n-alkanes [CH3-(CH2)n-CH3] and 
are commonly defined by the number of carbon atoms in a single straight chain. 
The melt temperature and latent heat typically increase as the length of the chain 
increases. Paraffins are a popular choice for TES due to the wide range of tran-
sition temperatures in this sub-category. Other benefits of paraffins include pre-
dictable and repeatable phase transition, non-corrosiveness, congruent melting, and 
4
Table 1.2 Paraffin PCMs for TES applications 
Name Molecular Formula 
Melt Temperature [°C] 
Latent Heat of Fusion [kJ/kg] 
Energy Density [kWh/m3] 
Ref 
n-Tetradecane 
C14H30 
5.5 228 48.13 [33, 34] n-Pentadecane 
C15H32 
10 205 43.79 [34] n-Hexadecane 
C16H34 
16.7 237 50.89 [34, 35] n-Heptadecane 
C17H36 
21.7 213 46.03 [36] n-Octadecane 
C18H38 
28.0 244 52.66 [35, 36] n-Nonadecane 
C19H40 
32.0 159 34.72 [37] n-Eicosane 
C20H42 
36.7 246 53.92 [35] 
n-Henicosane 
C21H44 
40.2 200 44.00 [38] n-Docosane 
C22H46 
44.0 249 54.92 [39, 40] n-Tricosane 
C23H48 
47.5 232 50.20 [41] 
n-Tetracosane 
C24H50 
50.6 255 56.60 [42, 43] n-Pentacosane 
C25H52 
49.4 238 52.96 [44] n-Hexacosane 
C26H54 
56.3 256 55.32 [39, 45, 46] n-Heptacosane 
C27H56 
58.8 236 51.13 [47] n-Octacosane 
C28H58 
61.6 253 56.64 [38, 48, 49] 
n-Dotriacontane 
C32H66 
69.5 170 38.34 [50] n-Tritriacontane 
C33H68 
73.9 268 61.04 [51, 52] 
strong nucleating properties. Downsides of paraffins include low thermal conduc-
tivity, incompatibility with some types of plastic containers, high volume change 
during phase transition, volatility, and flammability [30–32]. A list of commonly 
used paraffins is shown in Table 1.2. 
Non-Paraffins 
Non-paraffins are a broad category of organic phase change materials that do 
not inherently share the same properties, unlike the paraffin waxes. Non-paraffins 
consist of various materials including esters, alcohols, glycols, and fatty acids. Non-
paraffins are known for their sharp phase transitions, reliable and repeatable melt-
ing and freezing, low supercooling (except for sugar alcohols), and high latent heats 
of fusion. Downsides of non-paraffins include low thermal conductivity, low flash 
points, instability at high temperatures, high flammability, toxicity, mild corrosive-
ness, and high cost [53–55]. A list of commonly used organic non-paraffin PCMs 
can be seen in Table 1.3. 
5
Table 1.3 Organic Non-Paraffins for TES applications 
Name Molecular Formula 
Melt Temperature [°C] 
Latent Heat of Fusion [kJ/kg] 
Energy Density [kWh/m3] 
Ref 
Alcohols Glycerin C3H8O3 17.9 198 69.30 [56] 
Lauryl Alcohol C12H26O 24 215 49.63 [57–60] Myristyl Alcohol C14H30O 38 151 34.56 [61] Cetyl Alcohol C16H34O 49.3 141 31.76 [60, 62–64] 
Sugar Alcohols Xylitol HO(CHOH)3OH 92 233 98.38 [21] Sorbitol C6H14O6 95.6 167 69.12 [21] Erythritol HO(CHOH)2OH 118.7 333 134.17 [21] Mannitol C6H14O6 165.6 284 119.56 [21] Dulcitol C6H14O6 187.2 330 121.33 [21] Inositol C6H12O6 224 249 134.72 [21] 
Polyethylene Glycols PEG 400 H(OC2H4)nOH 6 84 26.32 [54, 65–67] PEG 600 H(OC2H4)nOH 21 120 37.67 [67] PEG 1,000 H(OC2H4)nOH 39 152 50.67 [67] PEG 2,000 H(OC2H4)nOH 51 165 55.46 [68] PEG 10,000 H(OC2H4)nOH 67 197 65.67 [69] 
Esters Methyl Palmitate C17H34O2 29 205 48.52 [70–72] 
Tristearin (C17H35COO)3C3H5 56 191 45.73 [73] Fatty Acids 
Formic Acid HCOOH 7.8 247 83.71 [74] Acetic Acid CH3COOH 16.7 184 53.67 [75] Caprylic Acid CH(CH)COOH 16.3 149 37.66 [57, 62] Capric Acid CH3(CH2)8·COOH 23 152 37.70 [64, 76, 77] Lauric Acid CH3(CH2)10·COOH 49 178 43.51 [41, 59, 61, 70, 77–79] Myristic Acid CH3(CH2)12·COOH 58 199 47.65 [59, 76–78] Palmitic Acid CH3(CH2)14·COOH 55 163 38.62 [41, 59, 80–82] Stearic Acid CH3(CH2)16·COOH 69.4 199 52.02 [77, 79, 83–86] 
Others Phenol C6H5OH 41 120 35.67 [87] 
Camphene C10H16 50 238 55.67 [80, 83] Naphthalene C10H8 56.7 103 32.62 [88, 89] Bees Wax C15H31COOC30H61 61.8 177 47.45 [90] 
Glycolic Acid HOCH2CO2H 63 109 45.11 [91] Azobenzene C12H10N2 67.1 121 36.64 [92] Acrylic Acid C3H4O2 68 115 33.54 [91] 
Phenylacetic Acid C8H8O2 76.7 102 30.60 [93] Acetamide CH3CONH2 81 241 77.66 [94, 95] 
Glutaric Acid C5H8O4 97.5 156 61.92 [96] Acetanilide C8H9NO 118.9 222 75.23 [84, 97, 98] Benzoic Acid C7H6O2 121.7 143 50.45 [88, 97] 
Stilbene C14H12 124 167 45.04 [92] Benzamide C7H7NO 127 169 62.91 [86, 99] 
6
1.1.3 Inorganic PCMs 
This section provides an overview of inorganic PCMs, including salts, salt hy-
drates, salt-water solutions, and metals. The commonly known characteristics of 
each group will be discussed, along with a comprehensive list of the phase tran-
sition temperatures, latent heats, and energy densities of the specific materials. 
With the exception of metallic PCMs, inorganic PCMs are challenging to incorpo-
rate into AM workflows for several reasons. Salt based PCMs are corrosive to many 
metals and can damage AM processing equipment. Also, many AM approaches re-
quire processing at elevated temperatures, which is incompatible with salt-hydrate 
and salt-water PCMs, as elevated temperatures can cause some of the water in the 
PCMs to evaporate, altering the PCM composition and increasing the risk of phase 
separation. Inorganic PCMs are also challenging to microencapsulate. At the time 
of writing, the authors are not aware of any efforts in the literature where inorganic 
PCMs are processed using AM techniques. 
Salts 
Salts such as nitrates and chlorides are being widely investigated for their use 
in high temperature thermal energy storage applications 
(>250 
°C). In terms of 
usable PCMs at high temperatures, salts and metals are the few that can be used 
reliably. Some of the benefits of salts include being cost-effective and having a very 
high latent heat of fusion. The disadvantages of salts are their corrosiveness, su-
percooling , low thermal conductivity, and poor thermal stability [100]. Research is 
being focused on improving salts as a thermal energy storage material, since with 
high temperature applications the amount of PCMs that are stable becomes limited 
to only salts [101–104]. A list of salts used for thermal energy storage applications 
(<400 
°C) can be seen in Table 1.4. 
7
Table 1.4 Salts for TES applications 
Name Molecular Formula 
Melt Temperature [°C] 
Latent Heat of Fusion [kJ/kg] 
Energy Density [kWh/m3] 
Ref 
Aluminum Chloride AlCl3 192 280 192.89 [105] Lithium Nitrate LiNO3 250 370 244.61 [105] Sodium Nitrate NaNO3 307 172 107.98 [105] 
Potassium Nitrate KNO3 333 266 155.91 [105] Sodium Peroxide Na2O2 360 314 244.22 [105] 
Potassium Hydroxide KOH 380 150 88.33 [105] 
Salt Hydrates 
Salt hydrates are inorganic compounds containing salt and water molecules in 
an explicit ratio to form a defined crystal structure [29]. Salt hydrates are a popu-
lar PCM for a wide range of thermal energy storage applications. The actual phase 
change transition for salt hydrates is not a traditional solid-liquid transition. A salt 
hydrate goes between a hydrated and dehydrated state of the salt, but this pro-
cess resembles a melting and freezing process thermodynamically. During a melt-
ing/freezing process, the salt will release stored water molecules becoming a salt 
hydrate with fewer moles of water, 
AB 
· 
nH2O ↔ AB ·mH2O 
+ 
(n−m)H2O 
or in the anhydrous form of the salt 
AB 
· 
nH2O ↔ AB 
+ 
nH2O 
Salt hydrates generally suffer from poor nucleation properties, resulting in super-
cooling (or subcooling) [24]. This means that upon cooling to release stored ther-
mal energy, a salt hydrate may not nucleate and crystallize until it is supercooled 
well below its phase change temperature, which causes problems in practical appli-
cations. The fundamentals of the kinetics of crystal nucleation are well described in 
prior literature [106–108]. Phase segregation is another phenomenon plaguing salt 
hydrate PCMs where salt and water can separate after melt/freeze cycling, gravity 
acts on density differences and causes the two phases to physically separate, ren-
dering the PCM ineffective[109–112]. Whether a given salt hydrate will suffer from 
8
Table 1.5 Salts hydrates for TES applications 
Name Molecular Formula 
Melt Temperature [°C] 
Latent Heat of Fusion [kJ/kg] 
Energy Density [kWh/m3] 
Ref 
Lithium Chlorate Trihydrate LiClO3·3H2O 8 253 129.31 [113] Potassium Fluoride Tetrahydrate KF·4H2O 19 231 93.04 [114, 115] 
Manganese (II) Nitrate Hexahydrate Mn(NO3)2·6H2O 25.3 126 56.00 [116] Calcium Chloride Hexahydrate CaCl2·6H2O 28-30 190-200 97.50 [114–116] Lithium Nitrate Trihydrate LiNO3·3H2O 30 256 104.04 [116] Sodium Sulfate Decahydrate Na2SO4·10H2O 34 256 105.96 [116] 
Sodium Carbonate Decahydrate Na2CO3·10H2O 33 247 98.80 [113] Sodium Acetate Trihydrate NaCH3COO·3H2O 55.6-56.5 237-243 96.67 [117] 
Calcium Bromide Hexahydrate CaBr2·6H2O 34 116 48.98 [115] Disodium Hydrogen Phosphate Dodecahydrate Na2HPO4·12H2O 35-45 280 118.22 [115] 
Zinc Nitrate Tetrahydrate Zn(NO3)2·4H2O 45.5 [107] Zinc Nitrate Dihydrate Zn(NO3)2·2H2O 54 [107] 
Sodium Thiosulfate Pentahydrate Na2S2O3·5H2O 48-55 201 97.15 [115] Cadmium Nitrate Tetrahydrate Cd(NO3)2·4H2O 59.5 [113] Sodium Tetraborate Decahydrate Na2B4O7·10H2O 68.1 [113] Sodium Phosphate Dodecahydrate NaPO4·12H2O 69 [113] Barium Hydroxide Octahydrate Ba(OH)2·8H2O 78 266 161.08 [113] Magnesium Nitrate Hexahydrate Mg(NO3)2·6H2O 89.3 150 68.17 [113] 
phase segregation depends on its phase diagram and whether it melts congruently, 
semi-congruently, or incongruently. This is explained in detail in [107]. Despite 
these downsides, salt hydrates have several advantages including high energy den-
sity (energy per unit volume), higher thermal conductivity (almost double that of 
organic PCMs), lower cost (relative to organic PCMs), non-flammability, and small 
volume changes during melt/freezing. A table of commonly used salt hydrates can 
be seen in Table 1.5. 
Salt-Water Solutions 
Salt-water solutions are a mixture of salt and water that results in a PCM 
with phase transition temperatures below 0 °C, which makes them a prime candi-
date for refrigeration applications [30, 118]. Salt-water solutions are inherently simi-
lar to salt-hydrates and share many advantages and disadvantages. The advantages 
include the high energy density, lower cost, and non-flammability. The disadvan-
tages include phase separation, subcooling, and high corrosiveness [118]. A list of 
salt-water solutions can be found in Table 1.6. 
Metals 
Low-temperature metals 
(<400 
C) and metal alloys can be used as PCMs; 
however, they are not a popular choice for thermal storage applications due to two 
9
Table 1.6 Salt-water solutions for low temperature TES application 
Name Molecular Formula 
Melt Temperature [°C] 
Latent Heat of Fusion [kJ/kg] 
Energy Density [kWh/m3] 
Ref 
Aluminum Nitrate + H2O 30.5% Al(NO3)3 + 69.5% H2O -30.6 131.5 44.55 [119, 120] Ammonium Fluoride + H2O 32.3% NH4F + 67.7% H2O -28.1 199.1 55.48 [119] Potassium Fluoride + H2O 21.5% KF + 78.5% H2O -21.6 225.2 82.46 [119] Sodium Chloride + H2O 22.4% NaCl + 77.6% H2O -21.2 222 77.69 [120] 
Ammonium Chloride + H2O 21.5% NH4Cl + 78.5% H2O -16 289 89.43 [120] Ammonium Sulfate + H2O 39.7% (NH4)SO4 + 60.3% H2O -18.5 269 97.56 [119] 
Dipotassium phosphate + H2O 36.8% K2HPO4 + 63.2% H2O -13.5 189 80.32 [119] Barium Chloride + H2O 22.1% BaCl2 + 77.9% H2O -7.7 102 46.24 [120] 
Zinc Sulfate + H2O 27.2% ZnSO4 + 72.8% H2O -6.5 208 97.7 [120] Magnesium Sulfate + H2O 18.63% MgSO4 + 81.37% H2O -4.8 84.96 30.9 [120] Sodium Fluoride + H2O 3.9% NaF + 96.1% H2O -3.5 309.2 91.11 [120] Sodium Carbonate + H2O 5.9% Na2CO3 + 94.1% H2O -2.1 281 85.15 [119] Potassium Sulfate + H2O 6.49% K2SO4 + 93.51% H2O -1.55 268.8 82.71 [120] 
main reasons: low latent heat of fusion [121] and high cost. This means that any 
device having the same thermal capacity will be considerably heavier and more ex-
pensive when compared to other popular PCMs (paraffins and salt hydrates). If 
weight is not a concern, metal PCMs leverage their much higher densities to have a 
competitive energy density (energy per unit volume). Metal PCMs also have a nat-
urally high thermal conductivity compared to alternative materials. A list of metal 
PCMs and metal alloys can be seen in Table 1.7. 
1.1.4 Eutectic Mixtures 
Eutectics involve the homogenous mixing of multiple PCMs that melts and 
solidifies at a single temperature that is lower than the melting point of the base 
constituents [26, 100, 129, 130]. This combining of PCMs requires precise control 
of the relative concentration of each constituent PCM to achieve congruent melt-
ing of a proper eutectic. Without proper mixing ratios, the mixture will segregate 
during cycling and fall out of eutectic [9, 53]. Eutectic mixtures have been explored 
for organic-organic, inorganic-inorganic, and in some cases inorganic-organic PCMs 
[131]. A list of various organic-organic and inorganic-inorganic eutectic mixtures 
can be seen in Table 1.8 and Table 1.9, respectively. 
1.1.5 Summary of PCM Types 
Figure 1.2 shows the volumetric energy density and latent heat of the PCMs 
reported in Tables 2-9 plotted against their transition temperature. Salts have high 
10
Table 1.7 Metlas/Metal alloys for TES applications 
Metal/Metal Alloy Melt 
Temperature [°C] Latent Heat 
of Fusion [kJ/kg] Energy Density 
[kWh/m3] Ref 
73.5% Ga – 15.4% In – 11.1% Sn 10.6 69 119.5 [121, 122] 78.4% Ga – 14.9% In – 6.7% Sn 10.9 71.2 121.98 [121, 122] 
83.5% Ga – 16.5% In 15 71.7 121.34 [121, 122] 91.6% Ga – 8.4% Sn 19.8 78.3 131.02 [121, 122] 95% Ga – 5% Sn 19.9 79.2 131.49 [121, 122] 
97.9% Ga – 2.1% Al 26.5 82.6 133.99 [121, 122] Cesium (Cs) 28.7 16.4 8.18 [121, 123] Gallium (Ga) 29.8 80.2 131.59 [121, 123] Rubidium (Rb) 38.9 25.7 10.49 [121, 123] 
44.7% Bi – 22.6% Pb – 19.1% In – 8.3% Sn – 5.3% Cd 47 36.8 93.64 [121, 123] 35.5% Bi – 64.5% In 54.1 30.8 68.53 [121, 122] 
49% Bi – 21% In – 18% Pb – 12% Sn 58 28.9 72.33 [121, 123] 38.7% Bi – 16.7% Sn – 14.4% Pb – 30.2% In 58.3 29 70.54 [121, 122] 
32% Bi – 51.2% In – 16.8% Sn 60.8 25.4 56.15 [121, 124] 41.8% Bi – 58.2% In 61.4 29.9 67.97 [121, 124] 
Potassium (K) 63.2 59.6 10.99 [121, 123] 50% Bi – 26.7% Pb – 13.3% Sn – 10% Cd 70 39.8 105.91 [121, 123] 
41.6% Bi – 19.4% Sn – 23.2% Pb – 15.8% Cd 71.7 24.5 64.48 [121, 122] 21.8% Bi – 78.2% In 73.1 22.5 47.7 [121, 122] 
38.5% Bi – 22.2% Sn – 25.3% Pb – 14% In 75 25.4 65.13 [121, 122] 40.5% Bi – 28.5% Sn – 16.3% Pb – 14.7% In 75.7 21.7 53.76 [121, 122] 
53.8% Bi – 27% In – 19.2% Sn 76.6 32.6 77.58 [121, 125] 42.5% Bi – 35.2% In – 22.3% Sn 79.2 36.9 84.7 [121, 122] 9.5% Sn – 56% Bi – 34.5% Pb 90.8 19.5 54.55 [121, 126] 
71.2% Bi – 28.8% Pb 94.9 29 82.34 [121, 122] 52% Bi – 30% Pb – 18% Sn 96 34.7 92.53 [121, 123] 
Sodium (Na) 97.8 113.2 29.15 [121, 123] 55% Bi – 43% Pb – 2% Zn 127 20.4 58.83 [121, 126] 48% Sn – 50% Bi – 2% Zn 135 47.6 112.94 [121, 126] 
58% Bi – 42% Sn 138 44.8 106.52 [121, 123] Indium (In) 157 28.6 55.85 [121, 123] 
73.5% Sn – 22% Pb – 4.5% Zn 172 59.8 135.72 [121, 126] Lithium (Li) 186 433.8 62.06 [121, 123] 
91% Sn – 9% Zn 199 32.5 65.63 [121, 123] Tin (Sn) 232 60.5 122.68 [121, 123] 
Bismuth (Bi) 271 53.3 144.95 [121, 123] Lead (Pb) 327 23 68.11 [127] 
Cadmium (Cd) 321 55.2 122.61 [128] 
Table 1.8 Organic-Organic eutectic mixtures for TES applications 
Name Mixture Formula Melt 
Temperature [°C] Latent Heat 
of Fusion [kJ/kg] Energy Density 
[kWh/m3] Ref 
85% Caprylic Acid – 15% Cetyl Alcohol 85% CH(CH)COH – 15% CH3(CH2)15OH 10 154 38.29 [62] 60% Camphene – 40% Stearic Acid 60% C10H16 – 40% CH3(CH2)16·COOH 3.5 156 38.2 [83] 54.9% Erythritol – 45.1% Urea 54.9% C4H10O4 – 45.1% CO(NH2)2 81.1 248 95.85 [132] 
50% Camphene – 50% Palmitic Acid 50% C10H16 – 50% CH3(CH2)14·COOH 70.9 210 49.44 [80] 66% Lauric Acid – 34% Myristic Acid 66% CH3(CH2)10·COOH – 34% CH3(CH2)12·COOH 34.2 167 40.54 [78] 29% Lauric Acid – 71% Lauryl Alcohol 29% CH3(CH2)10·COOH – 71% C12H26O 17 175 41.09 [59] 17% Myristic Acid – 83% Lauryl Alcohol 17% CH3(CH2)12·COOH – 83% C12H26O 18.4 181 42.05 [59] 10% Palmitic Acid – 90% Lauryl Alcohol 10% CH3(CH2)14·COOH – 90% C12H26O 20.1 191 44.21 [59] 75.7% Stearic Acid – 24.3% Benzamide 75.7% CH3(CH2)16·COOH – 24.3% C7H7NO 65.9 200 57.66 [86] 46.2% Stearic Acid – 53.8% Hexanamide 46.2% CH3(CH2)16·COOH – 53.8% C6H13NO 58 177 45.18 [85] 81% Stearic Acid – 19% Acetanilide 81% CH3(CH2)16·COOH – 19% C8H9NO 69.3 220 60.75 [84] 70% Benzoic Acid – 30% Acetanilide 70% C7H6O2 – 30% C8H9NO 75.6 194 67.63 [97] 
40% Lauric Acid – 60% Methyl Palmitate 40% CH3(CH2)10·COOH – 60% CH(CH)COOH 25.6 205 49.09 [70] 70% Capric Acid – 30% Cetyl Alcohol 70% CH3(CH2)8·COOH – 30% CH3(CH2)15OH 22.9 145 34.98 [64] 67% Capric Acid – 33% Lauric Acid 67% CH3(CH2)8·COOH – 33% CH3(CH2)10·COOH 22.8 154 38.02 [77] 72% Capric Acid – 28% Myristic Acid 72% CH3(CH2)8·COOH – 28% CH3(CH2)12·COOH 25.4 139 34.14 [77] 77% Capric Acid – 23% Stearic Acid 77% CH3(CH2)8·COOH – 23% CH3(CH2)16·COOH 27.8 123 30.89 [77] 58% Lauric Acid – 42% Myristic Acid 58% CH3(CH2)10·COOH – 42% CH3(CH2)12·COOH 35.2 162 39.26 [77] 
70% Caprylic Acid – 30% Lauryl Alcohol 70% CH(CH)COH – 30% C12H26O 6.5 171 42.1 [57] 40% Lauric Acid – 60% Myristyl Alcohol 40% CH3(CH2)10·COOH – 60% C14H30O 24.3 161 38.82 [61] 
11
Table 1.9 Inorganic-Inorganic eutectic mixtures for TES applications 
Name Mixture Formula Melt 
Temperature [°C] Latent Heat 
of Fusion [kJ/kg] Energy Density 
[kWh/m3] Ref 
45% Calcium Chloride Hexahydrate - 55% Calcium 
Bromide Hexahydrate 
45% CaCl2·6H2O -55% CaBr2·6H2O 14.7 140 101.64 [53] 
66.6% Calcium Chloride Hexahydrate – 33.3% Magnesium 
Chloride Hexahydrate 
66.6% CaCl2·6H2O -33.3% MgCl2·6H2O 25 127 58.5 [133] 
50% Calcium Chloride – 50% Magnesium 
Chloride Hexahydrate 
50% CaCl2 -50% MgCl2·6H2O 25 95 48.95 [53] 
47% Calcium Nitrate Tetrahydrate – 53% Magnesium 
Nitrate Hexahydrate 
47% Ca(NO3)2·4H2O -53% Mg(NO3)2·6H2O 30 136 61.55 [53] 
61.5% Magnesium Nitrate + 38.5% Ammonium Nitrate 
61.5% Mg(NO3)2·6H2O -38.5% NH4NO3 
52 125 54.17 [53] 
58.7% Magnesium Nitrate Hexahydrate – 41.3% Magnesium 
Chloride Hexahydrate 
58.7% Mg(NO3)2·6H2O -41.3% MgCl2·6H2O 59 132 55.05 [53] 
53% Magnesium Nitrate Hexahydrate – 47% Aluminum 
Nitrate Nonahydrate 
53% Mg(NO3)2·6H2O -47% Al(NO3)2·9H2O 61 148 58.88 [53] 
59% Magnesium Nitrate Hexahydrate – 41% Magnesium 
Bromide Hexahydrate 
59% Mg(NO3)2·6H2O -41% MgBr2·6H2O 66 168 78.47 [53] 
14% Lithium Nitrate – 86% Magnesium 
Nitrate Hexahydrate 
14% LiNO3 -86% Mg(NO3)2·6H2O 72 180 79.44 [133] 
energy density and latent heat but are only available at high transition tempera-
tures. Metallic PCMs span a broad range of transition temperatures, however, their 
latent heat of fusion is low, making them unsuitable for weight constrained appli-
cations. They are also cost prohibitive for many applications. Salt/water solutions 
have mid-to-high latent heat, but moderate energy density, and are only suitable 
for applications requiring subzero transition temperature. The other PCM types are 
clustered around the 0 °C to 100 °C transition temperature range, with moderate 
energy density and latent heat. 
Figure 1.3 depicts a comparison of the properties of different PCM types based 
on their material properties: latent heat by volume, latent heat by mass, cyclability, 
thermal conductivity, density, corrosiveness, and nucleation ability (i.e., susceptibil-
ity to supercooling). The comparison is relative, meaning the PCM type having the 
best performance for a given property is scored at 100% (exterior of circle), while 
the PCM type having the worst relative performance for that property is scored 
lower and towards the interior of the circle. For example, metallic PCMs have very 
12
https://lh3.googleusercontent.com/notebooklm/AKXwDQHd1h7pyyNL5pdogfm95meAiuzejg3IfXFLvrRDQV4kLdqO-HAb0myF-NdwBQ6-OCVnr7CmYBcESz111ZAoNR14QwtJO1bTie_Y3Ly9ewrS6va2TeFMjfaxKs2LHRJa3POY29-6kA=w1280-h557-v0
401bfd03-6517-4e33-af2e-416c4cd80a2e
Figure 1.2 Latent heat of fusion and energy density versus phase transition temperature for the various PCM categories. 
high thermal conductivity, while the other PCMs have lower thermal conductivity, 
with salt-hydrates being moderate, followed by salt/water solutions, salts, and then 
organic PCMs (paraffins and non-paraffins). Metals as PCMs do not supercool or 
corrode, have high density and thermal conductivity and high cycle life. However, 
their latent heat is typically quite low. Organic PCMs (paraffins and non-paraffins) 
also have strong nucleating ability (do not supercool), have high cycle life, and de-
cent latent heat of fusion by mass. However, they have low thermal conductivity, 
density, and volumetric latent heat. Salt based PCMs typically have high latent 
heat (by mass and volume), density, and higher thermal conductivity than organic 
PCMs. However, they are corrosive, prone to supercooling, and can have poor cycle 
life due to phase separation. 
1.2 Applications of PCMS 
Thermal energy plays a central role in many engineering applications, from 
generating power to conditioning living spaces. Any application that involves gen-
erating or transferring thermal energy is a potential application for PCMs. Depend-
ing on the application, implementation of PCMs can result in one or more benefits, 
13
https://lh3.googleusercontent.com/notebooklm/AKXwDQHqzwyYD_Bnur_w24IqOHg20GGdyYVPKodNukQdWL_jEBeRdDXeH66Wd8LbQlEfnNKt3hB8atssrXC8nyIXHv2WKjuDawql_vnBM6nYgqpa711ImWh4CmIa5rj9HJhFJrCIOTro3w=w1029-h617-v0
25a0001f-a89d-4027-a15b-e9d034383e53
Figure 1.3 Comparison of PCM properties. 
including energy efficiency (EE), emissions reduction (ER), load shaving/shifting 
(LS/S), and thermal management (TM), where TM is the ability of the PCM to 
prevent operation outside a system’s safe or comfortable operating temperature 
range. Figure 1.4 lists common applications in the temperature range between –50 
°C to 400 °C as well as a measure of the potential of PCMs to provide EE, ER, 
LS/S, and TM benefits for each of the listed applications. For example, incorporat-
ing PCMs in building air-conditioning systems provides a LS/S benefit and could 
potentially provide EE and ER benefits depending on system configuration and cli-
mate [3], but would not provide a TM benefit. Whereas incorporating PCMs into 
textiles or cooling fabrics worn by humans provides comfort thermal management 
and could potentially LS/S building loads if worn by enough occupants but is un-
likely to provide EE or ER benefits. To further organize these applications, we have 
identified three major groupings: Building Applications, Thermal Management, and 
Power Systems and Industrial Processes. 
14
https://lh3.googleusercontent.com/notebooklm/AKXwDQH57JXOpMv9e9pqN_KDJU8RNLIKxifQLDeZCbjgHPQ3czZwLcdkIsor2JWkr2hBRpuTbUBG-82njclfAsuIgyh972zRGkvBVYe-biW-MFcY95hjBzZV51qgsjoV3nSnv_58hFZe=w1280-h683-v0
11eb8d38-8a8b-464e-ac12-d3c342a3e460
Figure 1.4 Common applications for PCMs across the temperature range of interest and the ability of PCMs to provide benefits to said applications. 
1.2.1 Building Applications 
As depicted in Figure 1.5, integration of PCMs into buildings appears in a va-
riety of methods, that can be organized into two primary categories, passive and ac-
tive [134–136]. Passive applications typically involve the addition of PCM to exist-
ing building materials or structures to increase thermal mass [137, 138]. The most 
common method for this is adding a PCM layer in the building wall [139]. When 
incorporated into a building structure, PCMs are typically included in macro-encapsulated 
layers, plaster/paste composites, or shape stabilized composites [137, 138, 140]. 
There are potential synergies with the growth of additive manufacturing concrete 
structures and materials research integrating PCMs in cement [141, 142]. PCMs 
have also been added to solar chimneys, a building feature that helps induce nat-
ural ventilation by utilizing solar radiation to heat the air. The addition of PCM 
helps reduce performance fluctuation by offsetting intermittency of solar radiation 
[143]. This implementation is also used in solar heating applications [144]. In an-
other implementation, researchers found that the use of a PCM layer with solar 
15
https://lh3.googleusercontent.com/notebooklm/AKXwDQGjqhsPCL4Eau174X-2V04WdE-bQyqfKOODWSeGxVIntDvxCCF4Yt1RnVLsgmag6kyhsMytRYv6yodMtSQDBMtlAwvdS4flByyAkudK4o2zE3z0obxLPBM0buH3ByIWDj6cav_C=w901-h446-v0
0ae4ed55-30ee-4d07-837d-e9f2209b3176
photovoltaic panels on roofs helped reduce overall building thermal loads [145]. 
Figure 1.5 Potential implementations of TES within building applications. 
Active applications typically use PCMs in a dynamic way where the PCM is 
combined with an air-side or fluid-side heat exchanger and integrated into electric-
driven thermal equipment or appliances. A common active application is the use of 
campus-scale cold storage, typically using large chillers with water as the PCM. For 
cold storage in smaller systems, different PCMs with warmer melting temperatures 
are required due to equipment restrictions. This implementation has been investi-
gated and tested for single-building HVAC systems [146–150]. Studies have often 
identified the power density (charge/discharge rate) and the heat exchanger as key 
limitations. Heat exchangers in HVAC applications have been a growing area of re-
search for additive manufacturing, utilizing traditional advantages of polymer heat 
exchangers such as low-cost and corrosion resistance combined with the optimized 
designs enabled by AM [151]. PCM integration has been studied for other building 
thermal loads such as refrigeration and heating [152, 153]. PCMs have also been 
added to refrigeration systems both in container walls to provide additional thermal 
mass and integrated with the evaporator coil [154]. These methods help shave/shift 
electricity consumption, smooth out fluctuations in cooling load, and increase coeffi-
16
cient of performance, thereby reducing electricity consumption. 
Active heating systems integrated with PCM have been investigated in two 
major forms, building integrated heating and domestic hot water heating [155]. 
Building integrated heating is similar to passive PCM integration, utilizing added 
thermal mass to condition a space with additional control of using active heating 
systems such as hot water or electric heating to charge the TES [156–158]. Do-
mestic hot water uses macro-encapsulated PCM containers within the water heater 
tank either fixed at the top or floating with water level to help reduce thermal strat-
ification [159–161]. Some systems have also investigated dedicated TES heat ex-
changers to heat the water using just PCMs as an alternative to large hot water 
tanks [162–164]. This use of TES as a separate storage device has been specifically 
coupled with heat pump systems, both for space heating and water heating, show-
ing large potential electricity savings [149, 150, 165]. 
1.2.2 Thermal Management 
Many products and systems such as vaccines or electronics must stay below a 
maximum allowable temperature. PCMs have been proposed in these applications 
as a passive form of thermal management. One of the most studied applications 
of PCMs for thermal management is for electronics [166]. The lifetime, reliability, 
and performance of electronic devices and packages are dependent on maintaining 
safe operating temperatures. PCMs are suitable for this task, especially for high-
power electronics, photovoltaics, and battery thermal management, due to the high 
energy capacity and passive nature of PCM-based solutions [167–170]. Spacecraft 
systems are also a suitable application due to the need for low or no moving parts 
[171]. Batteries, photovoltaics, and space systems are suitable for PCMs due to the 
periodic nature of the loads, allowing for natural time for PCM to be recharged 
[166, 172]. Implementation in these cases typically includes either some thermal 
spreader such as heat pipes or a heat sink, or thermal conductivity enhancement in 
17
the PCM. Most PCMs have low thermal conductivity and are dependent on natu-
ral convection to absorb heat. The addition of thermal conductivity enhancement 
or extended surfaces helps ensure adequate heat transfer between the heat source 
and the PCM. This has been an area of research for additive manufacturing, which 
excel at creating optimized extended surfaces for both traditional and PCM based 
heat sinks [173, 174]. 
The cold chain also utilizes PCMs in containers for temperature sensitive 
goods such as vaccines allowing for more flexibility in transportation [175, 176]. 
Similarly, PCM has been added to packaging for temperature-sensitive foods [177, 
178]. Biomedical applications overlap heavily with cold chain for products such as 
vaccines and medicines, but they also include thermotherapy and medical dressings 
[179]. Here, PCM packaged with hot/cold pads or wound into different fabrics with 
microencapsulated composites are used to maintain temperature [180]. Integration 
into textiles also has a variety of uses for human comfort such as sportswear or bed-
ding materials [181]. 
1.2.3 Power Systems and Industrial Processes 
High transition temperature PCMs can be used in power systems and indus-
trial processes. One area of opportunity is waste heat recovery for industrial pro-
cess heat. One study found that heat recovery utilizing PCM thermal energy stor-
age resulted in 50-70% energy savings related to heating an industrial batch process 
[182]. The importance of high storage discharge rates was a notable requirement 
and the lack of commercially available PCMs in the 120 °C to 200 °C transition 
range was noted as well. High heat transfer rates are of importance in many in-
dustrial processes and are a driving factor for development of AM heat exchanger 
designs [183]. There have also been studies exploring use of PCM TES to trans-
port waste heat from industrial sources to demand locations such as hospitals [184]. 
Vehicle systems can benefit from the use of PCMs for thermal management also, 
18
allowing for buffering of peak thermal loads and for energy storage to improve cold 
start performance [185–187]. Concentrated solar power (CSP) plants can make use 
of PCM as an energy storage media for thermal electricity generation, typically uti-
lizing PCMs with transition temperature greater than 300 °C, however, some stud-
ies have investigated temperatures as low as 120 °C for CSP applications [188, 189]. 
Another power intensive process that can be improved with the use of PCMs is wa-
ter desalination. The addition of PCM into the basin of solar desalination devices 
can improve yield and overall efficiency [190]. 
1.3 Advanced Manufacturing with Phase Change Materials 
The effectiveness of a PCM device is defined by its energy and power den-
sity—the total available storage capacity (kWh) and how fast it can be accessed 
(i.e., heat transfer rate) (kW). Although many PCMs have high latent heats of 
fusion, which provides high storage capacity, most have low thermal conductiv-
ity, which can potentially limit how quickly and effectively the latent heat in the 
PCM can be accessed. This presents an issue when attempting to disperse heat 
through large blocks of PCM. To mitigate this issue, researchers have turned to ei-
ther (a) increasing the thermal conductivity of the PCM through additives such as 
expanded graphite [191], carbon fibers [192], and/or metallic particles [193] or (b) 
utilizing metal fin structures [194] and/or metallic foams [195] to diffuse heat more 
effectively. However, adding material, either through additional thermal-conductivity-
enhancing particles or metal structures, displaces PCM which reduces the available 
thermal energy storage density. 
The Ragone plot, originally developed to analyze the performance of batteries, 
can be applied to thermal energy storage heat exchangers [196–198]. Ragone plots 
quantify the energy (kWh) versus power (kW) for PCM heat exchangers. A typical 
Ragone plot is shown in Figure 1.6(a). The general goal of TES heat exchanger de-
sign is to maximize available energy (energy storage) and power (rate of heat trans-
19
fer). In a Ragone plot these goals push the knee in the curve in Figure 1.6(a) fur-
ther up and to the right. High energy and power densities requires low thermal re-
sistances between the heat source or sink and the PCM phase front. Additive man-
ufactured TES heat exchangers can achieve this in two ways – by increasing the 
effective thermal conductivity of the PCM with conductive scaffolding or by modi-
fying the geometry to increase surface area and reduce heat transfer length scales. 
Examples of how conductivity and geometry impact Ragone curves is shown in Fig-
ure 1.6(a-b). These results were obtained using a 2-D discretized model of a PCM 
heat exchanger, assuming all heat flow through the PCM is governed by conduc-
tion [198]. Increasing thermal conductivity lowers the resistance, which can increase 
the achievable power density from the baseline pure PCM curve (black) to the red 
curves that contain 2.5, 5 and 10% of a thermally conductive additive by volume. 
However, conductivity enhancements come at the cost of reducing the volumetric 
storage capacity since any scaffolding material displaces some of the active PCM. 
These effects must be considered together to achieve the optimal energy density for 
the desired charge or discharge rate (power), as shown in Figure 1.6(c). The opti-
mal point will be a function of the application, which is discussed in more detail in 
Section 3. For example, a cold chain or building application may require relatively 
low power densities, meaning the PCM will discharge over a log period (4 or more 
hours). For these situations, only a relatively small increase in thermal conductivity 
may be enough. Conversely, thermal management applications often call for high 
power densities (discharge rates on the order of minutes or seconds). In these cases, 
there are significant benefits to increasing the thermal conductivity, as shown in the 
third panel of Figure 1.6(c). 
Additive manufacturing can also leverage novel geometries to pass fluid through 
a PCM heat exchanger in intricate flow paths. This can decrease the heat trans-
fer length scale and increase the surface area, which both reduce internal resis-
20
https://lh3.googleusercontent.com/notebooklm/AKXwDQGIN5kHAZHlx-rmAaqd-zvJqacajONKRa3X6U2igvIkaJXObHR1ZxwU98GBRP62FGZ97eHWkXpbWXzbFCszE23gHFYj9zvmjGkwh6e6QK1HMLKv6av7-mlT-ZXgvUq1N7fzk7R1=w858-h760-v0
9b584475-a755-4362-9970-b33801225ee9
Figure 1.6 The performance of a thermal energy storage component in terms of energy and power density with different levels of enhancement, attainable using additive manufacturing. Panels (a) and (b) show Ragone plots for a round tube surrounded by PCM. The black curve shows the baseline case with a pure PCM, and the (a) red and (b) blue curves show different levels of conductivity and 
geometric enhancement, respectively. The energy density at three different power density levels (shown on the y-axis in (a) and (b)) is plotted for different 
enhancement schemes in (c). Note – the energy density is shown on the x-axis in the Ragone plots and on the y-axis in (c). The dashed black line in all three plots represents the maximum possible energy density, which is simply the energy storage 
capacity of the material alone with no flow channels or conductive additives. 
tances. An example of how geometry can impact the Ragone curve is shown in 
Figure 1.6(b). These results specifically look at reducing the diameter of the fluid 
channel and increasing the total length, simulating a case where the fluid channels 
serpentine through the PCM. Although the geometry isn’t optimized, in Figure 
1.6(c) the results show that modifying the geometry can improve performance at 
all power levels. It is expected that topology optimized TES heat exchangers will 
21
make large gains to improve overall charge and discharge efficiencies. 
Ideally, with the advent of additive manufacturing for TES heat exchangers, 
both the energy density and the power density can be co-maximized. AM allows 
for creation of ultra-compact high-surface-area-to-volume heat exchangers that re-
duce overall weight while maximizing PCM volume and heat transfer surface area 
on both the PCM side and fluid side. AM can also enable thinner walls, further 
reducing thermal resistance [199]. These geometry-enabled advancements are not 
possible with traditional manufacturing techniques. Furthermore, as discussed later 
in this article, recent research has shown the ability to directly 3D-print functional 
composite filament with PCM directly incorporated into the structural wall mate-
rial [200–205]. 
1.4 Review of PCMs and Composites used in Additive Manufacturing 
1.4.1 PCMs and Matrix Materials Used in AM 
All AM PCM components contain two key elements – the PCM itself and a 
matrix to contain and potentially enhance the properties of the PCM. The nature 
of the matrix material selected is directly related to the AM method in which it is 
processed. These matrix materials are used to develop (1) filaments, (2) resins, (3) 
inks, and (4) powders shown schematically in Figure 1.7 that are then assembled 
in a layer-by-layer fashion using thermal, evaporative, and light-based processing. 
As the AM PCM field has evolved, so has the relationship between the matrix and 
the PCM. In the most common efforts, a device is fabricated via AM and backfilled 
with a PCM. Increasingly, material and printing advancements have enabled direct 
incorporation of PCMs into the matrix material through physical blending, parti-
cle dispersion, coaxial extrusion, or chemical grafting, and in select cases, directly 
printing the PCM without a supporting matrix. 
22
https://lh3.googleusercontent.com/notebooklm/AKXwDQGLzLxgL4dNAtFkYxee9qZcaocCqgk-Ih6XiIufOH_R9C3jCGDiLowQdDSagSvTobX2CrPGWNPseLvpxQ1NDYX2HoRJaLsDIEFQ1jAtGuv0fZk8F_Y4rIU8tUGwnXnziMiyHcqkyg=w1092-h444-v0
40d5a859-af50-451e-a2bd-6a03d9c220e2
Figure 1.7 Graphical depiction of common additive manufacturing methods; a) selective laser sintering (SLS), also known as selective laser melting (SLM); b) fused filament fabrication (FFF), also known as fused deposition modeling (FDM); c) stereolithography (SLA); and d) direct ink writing (DIW). Varying forms of AM 
materials with different methods to incorporate PCMs into the matrix. 
PCMs used in AM 
The PCMs targeted in AM applications are largely organic in nature, due to 
low corrosivity, high latent heats of transition, limited supercooling and thermal 
stability at elevated temperatures required for some AM processes. Most PCMs 
used in AM applications exhibit solid-liquid transition behavior, which generally 
have higher latent heats compared to solid-solid transitions. 
Commonly utilized PCMs for AM applications are (1) paraffins [206–216], 
(2) alkanes [211, 216–223], and (3) polyethylene glycols (PEGs) [224–226]. Other 
PCMs used include a sugar alcohol, fatty alcohol, fatty acid, and water [227–231]. 
Commercialized PCMs are routinely utilized due to the variety of transition tem-
peratures and are available both in neat [200, 201, 232–248] and microencapsulated 
forms [204, 233, 249]. In an example of a metal PCM, researchers capitalized on the 
solid-stated transition of a nickel titanium alloy from monoclinic Martensite con-
figurations to a cubic Austenite lattice for AM metallic parts [250]. Another case 
of metal PCMs used a printed aluminum-tin alloy where tin was the PCM due to 
23
its comparatively low melting temperature [251]. Other niche PCMs include a thio-
lated octadecane derivative and stearyl acrylates, which are derivatives of the fatty 
acid stearic acid intended for chemical grafting and polymerization [207, 252–254]. 
Filament Materials 
Filament-based AM is one of the most widely used forms of AM due to its 
low equipment and material cost, limited post processing requirements, and diver-
sity in availability of materials. Compared with other AM techniques, filament-
based processes have lower layer resolution, weak inter-layer adhesion, and may 
require support structures for complex parts. Due to the ease of filament acces-
sibility and processing, incorporation of PCMs has taken several forms, (1) neat 
PCM blending, (2) dispersion of microencapsulated PCMs (MEPCMs), and (3) 
copolymerization. All filaments that encapsulate PCMs have been polymers like 
high density polyethylene (HDPE) [200, 201], polycaprolactone (PCL) [233], ther-
moplastic polyurethanes (TPU) [225, 249], acrylonitrile-butadiene-styrene (ABS) 
[241, 248, 255], and nylon [204]. 
For filaments incorporating neat PCM, encapsulation relies on solubility and 
uptake of the PCM into the filament material that remains upon extrusion and 
printing [200, 201, 233]. Addition of commercial PCMs to matrix materials has 
been done in the solution phase with PCL as well as mechanical mixing in the melt 
state prior to extrusion with HDPE [200, 201, 233]. Using HDPE as a matrix, 40 
wt% of PCM was mixed in with good filament extrusion properties and a transi-
tion enthalpy of 64 J/g [201, 202]. Using PCL as a matrix, PCM additions up to 60 
wt% were made, but only 20 wt% PCM filaments were printed, reducing the PCM 
transition enthalpy from 25 J/g to 10 J/g in the printed state [233]. 
MEPCMs have been incorporated into nylon, TPU, and PCL filament types. 
Methods of integration can be divided into (A) powder mixing and (B) solution 
dispersion. In two examples, MEPCMs were mixed with polymer powders and ex-
24
truded directly into filament achieving MEPCM contents between 30–50 wt% and 
exhibited melt enthalpies in the range of 46–70 J/g for the printed parts [204, 249]. 
Using solution processes, PCL was dissolved in chloroform and 60 wt% MEPCM 
was dispersed in the solution prior to drying and breaking up into pellets that had 
a melt enthalpy around 40 J/g [233]. 
Along with using MEPCMs to prevent PCM leakage from filaments, direct 
covalent bonding of the PCM with the filament matrix material has been shown 
to be an effective method to achieve TES in a printable material without leakage. 
Yang et al., capitalized on the hydroxyl end groups of PEG 8000 to copolymerize 
with an isocyanate-terminated TPU precursor to form domains of PEG that could 
melt and crystallize while tethered to the matrix materials, exhibiting a quasi-solid-
solid phase transition with a transition enthalpy of 65 J/g, which did not diminish 
even after 
>2000 
cycles [225]. 
Resin Materials 
Resin-based AM relies on crosslinking photocurable chemical groups with 
a laser at each layer. This process, stereolithography (SLA), produces high res-
olution objects at a relatively rapid rate. Compared with other AM techniques, 
resins can be costly and hazardous, and the printed parts can require extensive 
post-processing, and support material cannot be reused. The types of resin mate-
rials that have been combined with PCMs include: acrylamides [231], acrylic esters 
[224], siloxanes [207, 252], and stearyl acrylates [254]. An important limitation of 
resin approaches is that any material mixed into the resin must not optically in-
terfere with the light source which initiates photocuring. As such, dark or highly 
opaque materials must be avoided. 
When integrating PCMs into resin-based systems, researchers have blended 
neat PCM into resins as well as covalently linked PCMs into the resin matrix. With 
PCMs blended into resins, the PCM domains would ideally be locked into the crosslinked 
25
structure with curing. Wang et al., mixed two PEG PCMs into an acrylic ester 
resin and printed a simple rectangular prism (5 x 5 x 35 mm) with layer resolu-
tions of 50 
µm. 
At temperatures above PCM melting, PEG seeped to the surface 
of the print. The PEG seepage, coupled with a low latent heat, 7.2 J/g indicates 
substantial durability issues with the composite [224]. Gogoi et al., used water as 
the PCM absorbed into a flexible, SLA printed acrylamide-alginate hydrogel sup-
ported by PDMS at a size of 30 x 30 x 60 mm. In this example, water is supported 
through secondary intermolecular interactions and the flexibility of the hydrogel-
PDMS system accommodates the volumetric changes with water during phase tran-
sitions [231]. 
A few efforts have used derivatives of solid-liquid PCMs that can be grafted 
to polymer backbones or directly polymerized into a brush configuration. Singly 
tethered ends of attached PCMs restrict mobility and inhibit leakage while leaving 
the other end free to undergo crystallization and melt events exhibiting a quasi-
solid-solid phase transition. Ma, et al. used thiolated derivatives of octadecane as 
a PCM with the ability to be grafted to siloxane matrix materials and achieved 
transition enthalpies in the range of 25-125 J/g with print sizes around 30 x 30 x 
5 mm [207, 252]. Utilizing a macromonomer approach, Mao, et al., used an acry-
late derivative of stearic acid along with an acrylamide monomer and crosslinker. 
These were copolymerized during the printing process to form a polymer network 
that had a transition enthalpy around 70 J/g [254]. 
Ink Materials (Direct Ink Writing) 
Ink based materials in the AM context refer to liquids or slurries that are 
directly extruded in a layer-by-layer fashion in a process called direct ink writing 
(DIW). As the ink is deposited, solidification of each layer can occur through ther-
mal curing, photocuring, solvent evaporation, or reactions with the solvent [256]. 
Because ink-based AM can accommodate numerous curing processes and can be 
26
performed at low temperatures, there is large diversity in material selection, which 
is advantageous over other, more restrictive techniques. A notable disadvantage 
of ink-based AM includes the high degree of control required over the rheologi-
cal properties to achieve high resolution, cohesive prints. Matrix materials that 
have been targeted for DIW of PCM composites include siloxane [207], cements 
[230, 257–259], graphene oxide [223], and a commercial UV curable resin [211]. The 
thiolated octadecane grafted to a siloxane matrix material developed by Ma et al. 
discussed in the previous section was demonstrated to be able to be processed via 
DIW utilizing a high temperature UV curing step after printing [207]. 
In an example of coaxial DIW, Yang et al., demonstrated a thermally conduc-
tive graphene oxide ink printed as a sheath around a pulsed octadecane core that 
demonstrated a composite transition enthalpy and thermal conductivity of 190 J/g 
and 1.67 W/mK, respectively [223]. The pulsations of the PCM core created iso-
lated “beans” within the graphene oxide sheath that mitigated leakage in the event 
of localized damage to the print not resulting in the total leakage of the PCM. Us-
ing a similar process of creating localized regions of PCM within the matrix, Wei 
et al., created small waxy beads using emulsion processes and suspended the beads 
in a commercial resin typically used for SLA printing. Because the ink could be ex-
truded and each layer UV cured at temperatures below the 60 ◦C melting point of 
the paraffin PCM, the matrix was cured around the PCM beads in the solid state 
and prevented leakage from the print to achieve a transition enthalpy of 102 J/g. 
An innovative development in ink-based AM utilizes electrostatic potentials 
to deposit 
<10 µm 
diameter minuscule droplets of paraffin on a substrate with ex-
tremely high resolution in a process deemed electrohydrodynamic (EHD) 3D print-
ing. While not focused on TES and PCM applications, the demonstration of high-
resolution methods of paraffin ink printing has potential for advanced PCM com-
posite fabrication with spatially selective deposition of PCMs at resolutions 
<10 
27
µm 
[260–262]. 
An emerging field of DIW TES composites is focused on PCM incorporation 
into cementitious materials for building-scale thermal management [230, 257–259]. 
In these materials, PCMs are dispersed in cement slurries that are then deposited 
in a layer-by-layer fashion. The highest transition enthalpy achieved in an AM 
cement-PCM composite was 40 J/g using a neat paraffin PCM [257]. 
Powder Materials 
Fabrication of AM structures via powder processing utilizes a laser to selec-
tively melt or sinter particles into a cohesive structure. These powder-based pro-
cesses are known in the AM community as selective laser sintering (SLS), powder 
bed fusion, and direct laser metal sintering. Powder-based AM can yield high res-
olution parts with high interlayer strength and moveable components without the 
need for printed supports. However, powder-based AM processes can be slower 
than other AM techniques and the required hardware can be expensive. 
The materials space of powder-based AM is largely dominated by metal pow-
ders. Metallic materials for AM offer high thermal conductivities but often at the 
expense of cost, corrosion resistance, and weight. In AM PCM devices, aluminum-
silicon alloys, commonly containing magnesium, have been the most widely used 
due to their high strength-to-weight ratio, corrosion resistance, and ease of pow-
der processing through laser sintering. The most common alloy is AlSi10Mg [206, 
212, 213, 217, 219, 222, 226–228, 232, 236, 238, 246, 247, 263], but other aluminum-
silicon formulations [220, 221, 234, 240] as well as other aluminum alloys [214, 215, 
235, 237, 243–245, 251, 262] have also been used. Other metals printed for PCM 
applications have included copper alloys [216, 245], steel alloys [242, 245], nickel al-
loys [250], and titanium alloys [245]. These efforts produce metal structures that 
are generally fabricated to be porous for backfilling with PCM and focus on op-
timizing geometries that encourage rapid charging/discharging of the PCM [206, 
28
212–222, 226–229, 232, 234–248, 255, 262, 263]. The backfilling of metallic AM 
devices with bulk PCM capitalizes on high thermal conductivities, leak resistant 
structures, and considerable PCM volumes for high energy capacity. A few AM 
metallic structures have sought to use the metal as the PCM. Sharar et al. exam-
ined the solid-solid phase transition of a nickel titanium alloy, achieving a transition 
enthalpy of 16 J/g at 25 ◦C [250]. In a solid-liquid transition of a metal PCM, Con-
falonieri et al. capitalized on the low miscibility of tin within aluminum and the 
lower melting temperature of tin to achieve a transition enthalpy of 24 J/g at 230 
C [251]. 
Some special cases of powder based PCM composites exist where organic 
PCMs act as the binder during the powder fusion process. In a series of studies car-
ried out by Nofal, et al., paraffin was used both as the PCM and the binder in com-
bination with expanded graphite (EG) for laser sintering into multilayer composites 
in a variety of shapes that were 80% paraffin by weight and exhibited transition en-
thalpy of 155 J/g and thermal conductivity of 0.85 W/m K [208–210]. Using laser 
sintering methods for EG-PCM composite fabrication circumvented traditionally 
lengthy and wasteful processing like press-soak manufacturing that rely on PCM in-
filtration into EG powder prior to compaction [40, 169]. In another organic powder-
based AM precursor, the derivative of the PCM stearic acid, stearyl acrylate, was 
polymerized via both suspension and solution polymerization to yield particles of 
variable size that would allow for adequate coalescence during the powder fusion 
process. The parts fabricated using powdered poly(stearyl acrylate) exhibited a 
transition enthalpy of 82 J/g [253]. 
1.4.2 Thermal Conductivity Enhancement 
Thermal conductivity is an important property of PCMs and thermal energy 
storage systems, as the thermal conductivity of PCMs affects the charging and dis-
charging time of the material. Due to low heat transfer rates of some PCMs (i.e., 
29
organic PCMs), thermal conductivity enhancement has been utilized as a means 
of enhancing the rate of charging and discharging heat. Moreover, base polymeric 
materials used in AM often suffer from low thermal conductivity. Additives are 
thereby incorporated to increase the heat transfer rate of the composite material. 
Additives utilized for thermal conductivity enhancement are typically materials 
with inherently high thermal conductivity. Of note, thermal conductivities of ad-
ditives and their effect on TES devices can be highly variable depending on factors 
such as particle size, filler volume, crystallinity, and orientation within the com-
posite [264]. Shemelya et al., show that anisotropic thermal conductivity for 3D 
printed structures is related to the print direction and filler morphology, meaning 
that thermal conductivity can be controlled through a combination of print raster 
direction and material design [265]. Therefore, further optimization techniques for 
AM components can be employed to improve the thermal conductivity. 
During FFF (or FDM) anisotropy of the filament occurs due to the differ-
ing degrees of interdiffusion in the in-plane and out-of-plane directions of the fila-
ment and incongruent layering between the filament [266]. Studies primarily focus 
on the mechanical properties of AM components; however anisotropic characteris-
tics of the AM components can significantly vary along the print direction [267]. 
Anisotropy occurs due a discontinuity of material across the print layers. Control 
over anisotropy can be achieved by modifying the polymer matrix and adjusting 
the print parameters [268, 269]. The particles or fillers used to enhance thermal 
conductivity provide conductive pathways within raster direction of the composite 
when they are aligned in the proper orientation. 
Improving heat transfer in AM objects can be controlled before, during, and 
after manufacturing utilizing appropriate design optimization principles, material 
selection, and post-processing of the AM component. There are three parameters 
that can be tailored to improve the heat transfer of AM components: (1) mate-
30
rial selection and incorporation, (2) fabrication parameter optimization, and (3) 
post-processing techniques to improve thermal conductivity. Selection of the ap-
propriate TC enhancing additive, matrix material, and mixing ratio are crucial for 
good heat transfer and cohesive prints. During AM fabrication, an optimized de-
sign of the 3D model is generated, printing directions are chosen, and other printing 
parameters are determined to increase the adhesion between the printing bed and 
printed parts. The fabrication step also includes tailoring the surface roughness of 
the AM components based on printing conditions and slicing strategy to reduce 
the staircase effect [270, 271], and controlling local thermal conditions through mi-
crostructure (i.e., grain nucleation in metal AM components) [272, 273]. The post-
processing treatment includes mechanical polishing and thermal or vapor annealing 
that can be directly applied to the surface of the printed part [274]. 
Thermal conductivity in AM components is generally lower than its parent 
material with the reduction most pronounced in the build direction [275–277]. The 
reduction in the thermal conductivity and the inherent anisotropy of AM compo-
nents is due, in part, to incomplete fusing and substantial thermal contact resis-
tance between the layers [275]. Certain AM processes lend to better interlayer ad-
hesion and mitigate reductions in thermal conductivity. 
Material Additives for High Thermal Conductivity 
Materials development can be utilized with fundamental design principles for 
enhanced thermal conductivity. These composites often consist of a base polymer 
and a thermally conductive filler (e.g., graphene, boron nitride, aluminum oxide) 
[278]. For a thorough review of material parameters the reader is referred to Al-
muallim et al. [273]. The thermal conductivity of the base polymers is often on 
the order of 0.04-0.36 W/m K [279]. High thermal conductivity fillers, like carbon 
derivatives, metals, or ceramics are added to polymer-based composites to enhance 
the overall thermal conductivity of the composite. 
31
Additives based on carbon derivatives are available in a variety of allotropes 
and commonly include carbon fibers and nanotubes, graphene, and carbon black 
have been widely studied for their effect on improving the thermal conductivity of 
polymer composites, as well as mechanical properties [280–282]. Carbon-based ad-
ditives have advantages of high thermal conductivity, chemical stability, and low 
density ( 2 g/cm3) [283, 284]. Thermal conductivity measured at ambient condi-
tions (25 °C) of expanded graphite (EG) can range from 4-400 W/mK [285], carbon 
nanotubes (CNT) 2000-6000 W/mK [286], and carbon black (CB) 30-170 W/mK 
[287]. In carbon-based additives, geometry (i.e., how the carbon additive is ori-
ented within the material) plays a role in the improvement of thermal conductiv-
ity. Alignment of conductive fillers or fibers in the print direction can assist in the 
direction of heat flow through the printed material. Liao et al., showed that as the 
carbon fiber content increased above 4 wt.%, the thermal conductivity rapidly in-
creased from 0.221 W/mk to 0.835 W/mk, which may be due to carbon fibers in 
the matrix establishing a continuous heat-channel to efficiently enhance the conduc-
tivity, resulting from the preferentially alignment of the carbon fibers in the print 
direction [288]. Wang et al. utilized CNTs to prepare a composite aerogel, via melt 
deposition of the initial hydrogel, that exhibited anisotropic thermal conductivity of 
0.025 W/mK in the axial direction and 0.302 W/mK in the radial direction as the 
CNT filler ratio increased [289]. Shemelya et al. showed key thermal conductivity 
results for ABS/graphite composites, where the thermal conductivity was measured 
in the z-plane to be 0.25 W/mK and the x-y plane at 0.37 W/mK [265]. It was 
noted that the ABS/graphite composite exhibited noticeable thermal anisotropy 
due to the as-printed alignment of the graphite flakes. 
Ceramic fillers such as boron nitride, silicon carbide, aluminum nitride, and 
silicon carbide are used for their high thermal conductivity, low coefficient of ther-
mal expansion, and electrical resistance [273]. Among these fillers, aluminum ni-
32
tride has the highest thermal conductivity (140-180 W/mK), followed by silicon 
carbide (120 W/mK) [290], and boron nitride (30 W/mK) [291]. Other niche ad-
ditives include, metal organic frameworks (MOFs), titanium dioxide foam, and 
nickel foam [292]. Li et al. investigated the particle size of hexagonal boron nitride 
(h-BN) with a fixed filler content on composite properties of FFF printed compo-
nents using isotactic polypropylene [293]. Their results show that the particle size 
of the h-BN filler had a significant effect on the thermal conductivity, with com-
posites exhibiting 2.02 W/mK parallel to the print direction. They concluded that 
the heat conduction formed by the aligned h-BN particles contributed to the im-
proved thermal conductivity along the print direction. Sonsalla et al., tested Zn-SiC 
(zinc-silicon carbide) composites and determined that the addition of Zn-SiC im-
proved thermal conductivity from 0.20 W/mK in the horizontal direction for the 
ABS control to 0.42 W/mK and further enhancement of 0.60 W/mK in the vertical 
direction due to alignment with the filament print direction [294]. 
Ongoing research and development studies indicate that the challenges of the 
improving the thermal conductivity of PCMs focus on the aspects of clarifying the 
phonon scattering mechanism in PCMs, increasing the number of thermal conduc-
tivity chains and broadening the thermal transmission channels [292]. Further-
more, increasing the thermal conductivity of AM composites with additives that 
have higher thermal conductivity than the parent matrix is affected by size, shape, 
and filler amount, which can play a role in the phonon transport properties of the 
matrix [273]. High contents of additives reduce the thermal storage capacity (i.e., 
latent heat). It is important to consider not only additives but relative amounts 
when improving thermal conductivity. 
Fabrication Parameters for Improved Thermal Conductivity 
Outside of materials development, improving thermal conductivity in AM 
components can be done through to optimization of printing parameters. Printed 
33
geometries can be utilized such as lattice structure geometries can be printed to in-
crease the thermal conductivity in an AM component [213]. Many studies report 
on the print parameters (e.g., layer height, fill density, print speed, nozzle diame-
ter) for improvements in mechanical properties, but few report on the printer set-
tings for thermal conductivity of 3D printed components. In optimizing the print-
ing parameter, a study by Sonsalla et al., determined that the thermal conductiv-
ity of a 3-D printed structure was directly affected by fill density, layer height, and 
print speed. Nozzle diameter was found to be negligible in its effect on thermal con-
ductivity [294]. An increase in the thermal conductivity was observed with an in-
crease in the fill density. Additionally, they demonstrated optimal layer height of 
0.4 mm and fill density of 100% to achieve the highest thermal conductivity for a 
3-D printed object fabricated with a homogenous material printed in a horizontal 
orientation. 
In another study by Elkholy et al., the effect of layer height and raster width 
and results showed that increasing the layer height and width causes a deteriora-
tion in the thermal conductivity up to 65% when compared to the pure polymer 
[295]. They also found that decreasing the fill ratio decreases the thermal conduc-
tivity and that adding a carbon fiber filler improved the thermal conductivity in 
the z and y direction by 26% and 162%, respectively [295]. They determined that 
the effect of raster width was more significant that the layer height in reducing the 
thermal conductivity in all directions due to porosity generation [295]. 
While optimization of printing parameters is important, this approach can be 
limited due to the process parameters and can negatively impact the production 
capacity (i.e., lower extrusion speeds reduce the output). 
Post-Processing for Improved Thermal Conductivity 
Post-processing of AM components has been shown to improve the thermal 
conductivity in extruded components via, thermal annealing [277]. In traditional 
34
metal manufacturing thermal annealing is used to improve the grain structure and 
contact resistance [296]. The thermal contact resistance that exists between the 
layers of the AM components is often hard to show due to difficulties in experi-
mental measurements and is not reported widely in the literature [275]. Thermal 
contact resistance occurs in the z-direction due to the interfaces between the lay-
ers and may impede the heat flow and mechanical strength when compared to the 
x-direction [275, 297]. Prajapati et al. showed that strong interfacial thermal con-
tact resistance in the build direction was the cause of anisotropy, and that air gaps 
in the microstructure cause a reduction in the thermal conductivity in the mea-
sured raster direction [275]. They showed significant improvements in the thermal 
conductivity were observed when the polymers, ABS and ULTEM thermoplastic 
materials, were annealed at 135 °C for 96 h [275]. 
Vapor finishing techniques are used to smooth outer surfaces of the printed 
parts and serve to help lower thermal contact resistance with adjacent components 
at the surface; however, it is unclear if there is a significant impact on the interior 
geometry and thus the effective thermal conductivity of the printed parts [295]. 
1.4.3 Advanced Manufacturing for Integrating PCMs into Devices 
3D-Printed Scaffolds for Thermal Batteries 
One of the most common methods of combining PCMs with advanced manu-
facturing is by generating scaffolds that are then backfilled with various materials. 
By utilizing materials with high levels of thermal conductivity to build the scaf-
folds, these structures are capable of generating thermal batteries that can more 
quickly be charged and discharged relative to encapsulated PCMs alone. Further-
more, the ability to utilize computer aided design (CAD) software to produce intri-
cate scaffolds with high levels of surface area allows for optimized advanced man-
ufacturing. For instance, Qureshi et al. utilized aluminum AlSi10Mg gas-atomized 
powder to 3D print metal scaffolds via laser powder bed fusion , which produced in-
35
tricate structures with high levels of surface area and thermal conductivity. With 
85-90% porosity, the structures were then back-filled with molten paraffin wax-
based PCM to generate thermal batteries [238]. 
Similarly, Guo et al. developed metal printed scaffolds from AlSi10Mg through 
selective laser melting and back-filled them with n-tetradecane, resulting in a PCM 
thermal energy storage device with 13 times greater thermal conductivity than 
the selected PCM for faster charging/discharging [298]. Yazdani et al. 3D printed 
an aluminum silicon alloy (AlSi10Mg) grid as an extended surface on a flat plate 
heat exchanger using a selective laser melting process. The heat exchanger was 
tested with different grid designs charging/discharging paraffin wax and myristic 
acid. The proposed application was cooling high power 5G electronics and using 
the waste heat for other applications such as space heating [227]. A parametric 
2D FEM simulation was used for the design of an additively manufactured ther-
mal storage device. Several designs were printed out of AlSi10Mg using direct laser 
metal sintering (DLMS) and tested in a coolant loop with paraffin wax as the PCM 
[206]. Additionally, a maraging steel two-phase heat exchanger was manufactured 
using DLMS by Kabir et al. that was then backfilled with a commercial bio-based 
PCM, PureTemp25. The heat exchanger was designed for use as a thermal capaci-
tor or thermal storage in spacecraft thermal management systems, using methanol 
driven by capillary pumping pressure within the wick structure [242]. 
PCM-Integrated Materials for Wearable Technology 
One unique application space for advanced manufactured PCM devices that 
has received much study is wearable technology. For example, the acrylamide-alginate 
hydrogels developed by Gogoi et al. were designed as a wearable technology in-
tended for cooling athletes during training and competitions. These composite 
prints possess a high level of wear resistance and mechanical stability suitable for 
this application. This technology is being explored for commercial use under the 
36
name CoolPak Hydrogel [231]. In another study for wearable technology that in-
corporates PCMs, the octadecane grafted siloxane composites developed by Ma 
et al. deposited their SSPCM on carbon fiber cloth, enabling temperature regu-
lation for the wearer [252]. They demonstrated the cooling potential with surface 
skin temperature reductions from 46 ◦C to 38 ◦C over 20 minutes. The crosslinked 
stearyl acrylate gel developed by Mao et al. were printed on fabrics such as cotton 
and demonstrated a prolonged equilibration time with the hot/cold stage indicating 
thermal regulation capabilities. The authors propose that this PCM-integrated gel 
on fabric may be applicable to the wearable technology market [254]. The PEG-
TPU copolymer created by Yang et al. utilized single-walled carbon nanotubes 
(SWNT) to facilitate heat transfer to solid-solid PCM that was 3D printed into 
flexible sheets for cooling fabrics. At 1 wt.% SWNT, these sheets possessed a ther-
mal conductivity of 0.52 W/m-K and demonstrated rapid thermal regulation from 
30 ◦C to 60 ◦C and back to 30 ◦C in just 2 minutes. latent heat of 65 J/g. 
1.5 Commercially Available Materials and Systems 
This section will outline a few specific examples of PCMs being utilized in 
commercial products. See the recent work by Mehling et al. for a comprehensive re-
view of the state of PCM-based products across multiple industries [299]. A graph-
ical timeline of major developments in the commercial development and implemen-
tation of PCMs is outlined in Figure 1.8. 
1.5.1 Phase Change Material Manufacturers 
Several companies have developed PCMs with a range of chemistries includ-
ing paraffin, bio-based, and salt hydrate based PCMs. These companies, listed 
alphabetically, include (but are not limited to) Axiotherm [300], Boyd Corpora-
tion [301], Climator Sweden AB [302], Crodatherm [303], Eastex [304], ExxonMobil 
[305], Henkel Electronics Materials [306], Honeywell Electronic Materials [307], In-
solcorp [308], Laird (DuPont) [309], Microtek Laboratories [310], Phase Change So-
37
https://lh3.googleusercontent.com/notebooklm/AKXwDQHKNOgj3URFR-w3XmI9qsG05EatOvTc190fIhOGKY4cbb5cH-s9YfoBX0OLlwA3PemrOTgD1Nb1kfCAgDBLyThT5mJbBBs5GEO9oYFAEuYXPUsz_5ndwPha5UUcU6_bei0FIpfZdA=w803-h615-v0
ed897653-6639-460f-8a7b-74e5865732b7
Figure 1.8 Graphical timeline displaying major events in the commercialization of PCM and PCM-integrated products. 
lutions [311], Pluss Advanced Technologies [312], PureTemp [313], Rubitherm [314], 
Sasol Limited [315], Sunamp [316], and Tempered Entropy [317]. While PCMs have 
an extensive history of application research, the transition to commercially avail-
able products has been somewhat limited. Reasons for lack of industrial adoption 
include cost as well as limitations in thermal conductivity, latent heat, and charg-
ing/discharging, though these properties have experienced significant improvement 
over the last few decades. PCMs have traditionally been most successfully incor-
porated into thermal management devices for cooling electronics and in cold chain 
applications for temperature-controlled transportation of goods. 
1.5.2 Water-Based Systems 
Historically, ice has been the most used PCM given its abundance and low 
cost relative to other PCMs. Water-based systems have been implemented across 
38
different geographies over the last few decades. This technology aims to store ther-
mal energy in large-scale ice tanks that can be stored indoors or outdoors. The 
ice then undergoes solid-to-liquid phase change at times of need for building space 
cooling, typically through a secondary loop flowing a glycol-water solution. Compa-
nies like Baltimore Aircoil [318], Calmac [319], and Evapco [320] produce ice-based 
thermal storage systems that aim to reduce greenhouse gas emissions and save 
money on cooling costs in commercial buildings such as schools, hospitals, malls, 
and more. 
1.5.3 PCMs for Heating Applications 
Due to advancements in material properties and cost reductions, PCMs are 
now being used for thermal energy storage in both water and air heating appli-
cations. For example, in addition to manufacturing and selling their own PCM 
under the Plentigrade tradename, Sunamp develops TES devices utilizing PCMs 
for heating water and air. Sunamp claims their Thermino thermal battery can be 
charged by air-source heat pumps, ground-source heat pumps, photovoltaics, grid 
electricity and boilers [321]. Phase Change Solutions manufactures a wide range of 
biobased PCMs, some of which remain solid through their phase transition tem-
perature. In addition to these products, Phase Change Solutions also offers a de-
vice named ENRG that is reported to save a 25,000 ft2 facility 81,000 kWh of en-
ergy annually. This “blanket” consists of PCM placed between two polymer and/or 
aluminum films that can be placed in the ceilings, roofs, or walls for load shav-
ing/shifting and thermal buffering [322]. Axiotherm produces both organic and 
inorganic PCMs across a wide range of temperatures, as well as products incorpo-
rating their macroencapsulated PCMs into both water-based (HeatSel) [323] and 
air-based (HeatStraxx) [324] energy storage devices. Ephex markets and sells a to-
tal PCM-integrated system for water heating applications [325]. This system uti-
lizes solar panels that collect thermal energy during the day and then uses flowing 
39
water beneath the panels to transfer the energy to a salt based PCM thermal bat-
tery located near the facility’s hot water tank. The tank then pulls thermal energy 
from the battery at times of need to meet domestic hot water needs of the facility. 
PCM Technology manufactures floor/ceiling panels that integrate PCM for heating 
and cooling for both homes and office spaces, in addition to PCM-based solutions 
to cooling data centers and improving energy efficiency [326]. 
1.5.4 PCMs for Cooling Applications 
In cooling applications, PCM are used to produce cold packs for transport-
ing food, pharmaceuticals, temperature-based therapies, for cooling electronics, and 
for air-conditioning in buildings. In this space, Cold Chain Technologies produces 
low phase transition temperature PCM gel and foam packs for use in keeping prod-
ucts cold during shipping [327]. Similarly, Sonoco encapsulates low temperature 
PureTemp PCM gel within metal-lined bagging to produce cold packs [328]. Several 
companies also produce smaller portable coolers that incorporate either ice packs 
or PCM-lined walls, which are intended for everyday consumer use. In electronics 
cooling, AllCell’s Phase Change Composite technology absorbs and conducts heat 
away from lithium-ion batteries for increased power density and battery life [329]. 
Advanced Cooling Technologies has produced PCM-integrated heat sinks that are 
utilized in military and aerospace applications, specifically to replace complex ther-
mal management systems already implemented. These devices utilize thermal mod-
eling coupled with advanced manufacturing to develop optimal geometries for high 
performance heat sinks [326]. Viking Cold is another company that combines intel-
ligent controls and monitoring software in conjunction with PCM thermal batteries 
to provide cold chain solutions to food transport and long-term storage. These bat-
teries utilize PCM in the range of –28 to 0 ºC that are encapsulated within high 
density polyethylene (HDPE) packs that Viking Cold claims absorbs 50-85% of 
heat infiltration into cold storage spaces [330]. PLUSS Technologies develops both 
40
hydrated salt and organic PCMs, in addition to several products utilizing these 
materials. These products include a solar-powered cold-room (HimaCool) and a 
portable freezer (PronGO) that implement cold storage thermal batteries to main-
tain setpoint temperatures [331]. 
1.5.5 Wearable Technology 
Wearable technology that incorporates PCMs for thermal management of the 
human body has seen considerable research in recent years, with several products 
reaching the market. For instance, GlacierTek develops PCM-integrated cooling 
vests that utilize PureTemp’s materials [332], while Inuteq produces a similar cool-
ing wearable technology that uses materials from CrodaTherm [333]. Both products 
use macroencapsulated PCM as a means of pulling heat away from the body, which 
can improve performance in athletics or for safety in certain professions such as fire-
fighting or nursing where overheating can occur. For sleeping applications, Out-
last Technologies GmbH produces composite polyester fibers blended with PCMs 
called ThermoCules that can be utilized in comforters and sleeping bags for keeping 
bodies thermally comfortable during rest [334]. In a similar application, companies 
such as Rubitherm have produced sheets filled with PCMs for wearing during heat 
therapeutic treatments [335]. 
1.5.6 Thermally Conductive Scaffolds 
Several companies are investigating ways of producing thermally conduc-
tive structures via advanced manufacturing that can serve as scaffolds for PCM-
integrated thermal batteries. The most common method of producing thermally 
conductive scaffolds is through metal printing. Several companies manufacture 
3D printers capable of 3D printing metal, which, listed alphabetically, include 3D 
Systems, Desktop Metal, Digital Metal, EOS, Fabrisonic, Formalloy, GE Addi-
tive, Markforged, Pollen AM, Renishaw, SLM Solutions, SPEE3D, TRIDITIVE, 
TRUMPF, Velo3d, Xact Metal, and XJet. These systems largely rely on laser sin-
41
tering of metal powder that fuses together particles and forms a solid structure, 
though some like Markforged’s Metal X printer use a metal-infused polymer fila-
ment that is printed normally and then placed in a kiln to burn off any non-metal 
components and fuse the metal particles together. However, these printing methods 
can often be cost prohibitive, with printers from the above-mentioned manufactur-
ers costing anywhere between $100k-$750k, in addition to necessary add-ons like 
furnaces for sintering. Outside of metal printing, TCPoly is a company that man-
ufacturers polymer filament with a thermal conductivity of 5.0-8.0 W/mK, which 
is about 20x greater than that of neat polymeric materials [336]. These polymer 
composites are not as thermally conductive as metal-based materials, but they are 
comparatively cheaper, use more accessible equipment to print, corrosion resistant, 
and require no post processing steps. With either technology, scaffolds can be back-
filled with a variety of PCMs and encapsulated, allowing for applications to thermal 
battery systems that require rapid charging/discharging. 
1.6 Perspective on Future Directions 
There are many potential applications of PCMs - ranging from heating and 
cooling equipment to thermal management of electronic devices. Each application 
will have its own constraints, which will impact how the PCM should be integrated. 
In devices used for heating and cooling, PCM TES incorporation allows for load 
shifting and peak shaving, reducing stress on the electrical grid and facilitating re-
newables integration. Certain power electronic equipment is highly transient and 
requires pulse heat dissipation. A heat sink, or thermal management device, made 
of PCM can absorb large heat spikes while maintaining a constant temperature. 
Additive manufacturing for thermal management systems utilizing PCM al-
lows for the development of novel, thermally conductive scaffolding that cannot be 
produced by subtractive manufacturing. As mentioned previously, several compa-
nies are beginning to use metal 3D printing to make structures for PCM-integrated 
42
thermal batteries. Furthermore, technology to directly print relatively high con-
ductivity composite PCM and polymer composites is emerging. One of the main 
advantages of the ability to 3D print heat sinks (particularly extrusion-based) is in 
situations where fast, easy, cost-effective manufacturing is necessary, such as the 
ability to manufacture replacement parts on demand while away from fabrication 
facilities (e.g., while in orbit in space or in a field location). 
Currently, commercial TES, which allows for peak shaving and load shifting, 
results in energy and cost savings for businesses. However, the widespread adop-
tion of TES, including extension to residential customers, will further aid in reduc-
ing the demand on the aging and unstable electrical grid. TES can be extended to 
manage waste-heat and waste-cool recovery, further enhancing the energy and cost-
savings benefits. It is expected that advanced manufacturing will play an important 
role in advancing the design of the heat exchanger form for TES systems. 
The current state-of-the-art of many latent heat TES systems is large PCM-
filled tanks with immersed heat exchanger tubing with length scales on the order 
of 10-40 mm, see Figure 1.9. Since in many lower-temperature HVAC-type appli-
cations the PCM is water, expansion and contraction during the phase change has 
historically, due to both mechanical stresses and the ability to maintain contact 
between the water/ice and the heat exchanger surfaces, prevented smaller chan-
nels and PCM length scales from being utilized for more effective heat exchanger 
designs. However, with the advent of utilizing newer, higher-energy-density, cost-
effective PCMs (with lower coefficients of expansion), the design of next-generation 
thermal energy storage units can take advantage of additive manufacturing pro-
cesses to produce compact heat exchangers with very high surface-area-to-volume 
(length scales on the order of 1-3 mm, see Figure1.9) that incorporate novel heat-
transfer-enhancing elements, such as complex fins or flow geometries, not possible 
with traditional manufacturing. In addition to manufacturing novel geometrical 
43
https://lh3.googleusercontent.com/notebooklm/AKXwDQEfb9T1prTCm2bsjZfHq-Mk4aCK7OgTgD5KrMhszjlfb_Wl2UmD9rGJKbQUo97MR8A-uyCjolJ_N1Qem75CYJKqaBz3P8K0fEeyFZXMCW6U3uHR2QQ6tL84q3bjNCiMccphK1GlKw=w818-h499-v0
12970f02-9127-4b06-b8f3-4898e60c5271
features, additive manufacturing precipitates the use of alternative heat exchanger 
construction materials, such as composite polymers comprising PCM or thermal-
conductivity-enhancing additives. 
Figure 1.9 Vision for the future of TES heat exchangers with respect to magnitude of length scales and surface-area-to-volume ratios. 
Currently, there is a dearth in PCMs with high energy density and phase-
change temperatures in room-temperature range for building applications as seen 
in Figure 1.10. Although water has an energy density of 92 kWh/m3, exceeding the 
BTO target of 80 kWh/m3, alternative eco-friendly materials with higher phase-
change temperatures are needed. Salt-hydrate-based PCMs are promising; how-
ever, remedies for supercooling and separation issues continue to be explored by re-
searchers. Furthermore, innovation in advanced manufacturing techniques is needed 
to incorporate salt-hydrate-based PCMs into composite 3D printing. 
For additively manufactured TES to become competitive with traditional 
manufacturing techniques, the ability to scale-up the technology from small form 
factors is imperative. Many 3D printers are prohibitively slow and can only produce 
very small footprints, making large heat exchangers that can be produced quickly 
nearly impossible. However, as additive manufacturing advances, the ability to pro-
44
https://lh3.googleusercontent.com/notebooklm/AKXwDQGKvCH7DDTIqSekPUczDKAxhLLJa1pFRIoQJqyQkN0JRglkxpt6RdAgw0crOfQu0k7WevZGaEyGBLbrVeW1UluqxLVcPyvchoNlKXEVndC0zE01LsHImW6xQKZxswYYFlVkpP_r=w739-h569-v0
8c957981-2701-4a32-93c4-119e2de64fe3
Figure 1.10 Energy density of various PCM categories with applications and DOE BTO target energy density. 
duce compact, modular heat exchangers becomes more of a reality. 
1.7 Relevent Literature: PCM Modeling 
There is a need to decarbonize the growing energy systems in the world to 
help mitigate the effects of climate change [1]. This requires the rapid development 
of clean energy solutions such as solar and wind energy to help reduce current and 
future emissions [2]. To achieve these clean energy solutions, co-deployment of scal-
able, affordable, and sustainable energy storage technologies need to be explored 
[3]. Several methods of storing large quantities of energy have been developed at 
different levels of readiness and their own set of pros and cons [4–7]. Thermal en-
ergy storage (TES) systems are of great interest due to the low cost and reliability. 
Materials used for TES can be classified into three categories: sensible heat, latent 
heat via phase change, and thermochemical reactions. Authors have presented com-
45
parisons as well as advantages and disadvantages of sensible [8], latent [9, 10], and 
thermochemical energy storage materials [11–13]. Of the three energy storage mate-
rial categories, latent heat via phase change has become the area of interest in TES 
research. To properly design and implement latent heat TES systems, the phase 
change materials (PCMs) need to be modeled properly and effectively. 
When it comes to modeling PCMs, more specifically understanding the math-
ematics of a moving boundary separating two different phases of a material, this 
work began in the 1800’s. The first known instance of these types of problem sets 
was by Lame and Clapeyron in 1831[337], shortly followed by a lecture from Neu-
mann on moving boundary problems[338], and lastly a series of papers by Stefan in 
the late 1800’s[339, 340] that is now famously referred to as the Stefan problems. 
Due to the time period of these discoveries, only simplified closed form analytical 
solutions were developed due to the lack of numerical computational capabilities. 
It wasn’t until the 1970’s, when the Neumann-Lame-Clapeyron-Stefan Prob-
lems could be revisited with the intention of using numerical solutions to further 
advance these problem sets. This first known numerical work was done by researchers 
Bonacina et al.[341], Meyer[342], and Shamsundar and Sparrow[343, 344]. From 
these works, the handling of the phase change process was done using conduction 
as the primary form of heat transfer throughout the solid and liquid phase of the 
PCM. In 1977, Sparrow et al. concluded that the natural convection that occurs 
in the liquid region of the phase change could not be ignored and has a signifi-
cant impact on the interactions at the phase boundary between the solid and liq-
uid regions[345]. This conclusion was further emphasized and proven since then by 
various researchers performing numerical calculations and experiments [346–352]. 
From the countless work done over the past decades, the modeling of phase 
change processes are handled numerically by various techniques and methods[353, 
354]. One of the main and most important assumptions made to determine which 
46
method to use when modeling a PCM is to decide if natural convection within the 
liquid region can be neglected or not. In many scenarios, natural convection is ne-
glected to help reduce computational intensity despite enough evidence to believe 
that natural convection would be present and significant within the PCM. Improper 
use of the assumption on natural convection can lead to large error in the modeling 
of PCM. 
The most appropriate time to neglect the effects of natural convection and 
model the PCM only with conduction, is when the PCM is shape-stabilized. A 
shape-stabilized PCM, is a PCM that is formed into a composite material that 
maintains its overall shape while the PCM undergoes a phase change from a solid 
to liquid phase. A PCM can be shape-stabilized by being mixed with a polymer 
(HDPE [200, 201], PCL [233], TPU [225, 249], ABS [241, 248, 255], Nylon [204]) 
or impregnated into and expanded porous material (expanded graphite [355–357], 
metal foam [358–360], polymer foam [361]). With these shape-stable PCMs, the ef-
fects of natural convection are greatly reduced as the large liquid region that forms 
during a phase change process is broken up into smaller micro cavities. This reduc-
tion in natural convection effects causes conduction to be the primary form of heat 
transfer during the melting process [362, 363]. Therefore, the use of a conduction 
based modeling method, like the enthalpy method is very appropriate when used 
for shape-stabilized PCMs. 
When modeling a phase change process with a heat transfer fluid to exchange 
energy with the PCM, a major assumption is made to estimate the heat transfer 
coefficient at the heat transfer boundary. In the literature, a heat transfer coef-
ficient is estimated by using correlations available for constant wall temperature 
and constant wall heat flux boundary conditions [364–369]. None of the correlations 
used account for the dynamic transient effects at the boundary when the melt front 
of the PCM is moving. In the present study, a closer examination of the coupled re-
47
lationship between the transient melting of a shape-stabilized PCM and the forced 
convection of a heat transfer fluid is explored and a comparison is made with heat 
transfer coefficients from the literature. 
48
2 HDPE/PCM Composite Filament 
In this chapter, the fabrication and characterization of a composite PCM fil-
ament was developed for fused filament fabrication (FFF). The filament consist 
of the composition of high density polyethylene (HDPE) with an organic PCM 
(PureTemp) through the use of a single screw extruder. Characterization includes 
thermal storage capacity and thermal conductivity of both the filament and 3D 
printed samples. The contents of this chapter contributed to the publication in the 
Journal of Additive Manufacturing [205]. 
2.1 Materials and Manufacturing Methods 
2.1.1 Materials 
HDPE pellets (PPR-HDPE01) with a specific gravity of 0.955 and a melt 
flow rate of 20 g/10 min (190 ◦C and 2.16 kg) were supplied from Premier Plastic 
Resins (Lake Orion, MI). The PCM, PureTemp 42 (henceforth known as PCM42), 
was supplied from PureTemp (Minneapolis, MN). The data sheet from PureTemp 
reports that PCM42 has a phase-change temperature of 42 ◦C and latent heat of 
fusion 
(hsl) 
of 218 kJ/kg. The latent heat of fusion is the energy absorbed or re-
leased during a constant-temperature phase change from a solid to a liquid.The 
data sheet provided by the manufacturer also reports that when PCM42 is in the 
solid phase, it has a density 
(ρ) 
equal to 940 kg/m3 and a thermal conductivity 
(k) 
equal to 0.25 W/mK. When PCM42 is in the liquid phase, it has a density equal to 
850 kg/m3 and a thermal conductivity equal to 0.15 W/mK. 
2.1.2 Filament Fabrication 
Mixtures of HDPE and PCM42 were prepared by pre-melting and mixing the 
two materials together for specific mass ratios. The thermal storage capacity corre-
lates to the PCM percentage within the composite; however, too much PCM con-
tent can diminish the structural integrity. The mass content of the PCM42 in the 
mixture was varied between 20% and 60%, in increments of 10%, in order to deter-
49
mine the maximum amount of PCM42 that can be mixed with HDPE to produce 
filament suitable for FFF. The mixtures were observed for consistency of filament 
diameter during the extrusion process and their ability to remain flexible enough 
for printing (i.e., could physically be handled without breaking). If the percentage 
of PCM42 in the mixture was too high, then an inconsistent diameter was observed 
during the process, and the resultant filament would break easily when handled. It 
was found that the 40% PCM42 mixture contained the maximum amount of PCM 
while still maintaining the criteria for printable filament; therefore, this composi-
tion is the focus of the current study. The DSC was used to examine the filament 
by testing the latent heats of fusion and melt temperatures of both the PCM42 
and the HDPE in the composite. As will be discussed later, the DSC results were 
also used to hypothesize the amount of PCM loss due to the extrusion process (e.g., 
leaking). 
The PCM42/HDPE mixture was pelletized using a shredder (SHR3D IT, 
3devo, Utrecht, Netherlands) and extruded into 1.75-mm-diameter functional com-
posite filament using a filament extruder (Next 1.0, 3devo, Utrecht, Netherlands) 
with a 4-mm-diameter nozzle. The extruder has four equally spaced independent 
heating elements and a single screw to help promote better mixing. At the noz-
zle outlet of the extruder, there are two adjustable directional fans for air cooling. 
During the extrusion process, the filament diameter was affected by a number of 
factors, such as the cleanliness of the extruder screw, heating element tempera-
tures, the speed of the screw, and nozzle diameter. Therefore, an initial set of ex-
periments was conducted to optimize the extruder settings for pure HDPE and 
the PCM42/HDPE composite. The heater temperatures, screw speed, and fila-
ment diameter were monitored throughout each extrusion process. Filament with 
a consistent diameter for FFF is compared to that with an inconsistent diameter 
in Figure 2.1. Consistent-diameter filament was produced using optimal settings 
50
https://lh3.googleusercontent.com/notebooklm/AKXwDQFW6dR7hPtVwvgkQ2fNzOXlXXAIOWDoP_ZNElUbER_aaJKaEnNFyLDkxWZh7DfwrylKci3GCNrXUgpuMZKC_8828iRVlo2V_2CpQGE--L9hnek7s98-EjqhvRvnrq5eHbcz6yES6w=w1054-h790-v0
142c4cce-1c74-4e44-8e8e-e0c2c119135d
(discussed below) after starting with an extruder that had been purged with spe-
cialized cleaning materials (HDPE Flush, Devoclean Purge, 3devo, Utrecht, Nether-
lands). Inconsistent-diameter filament typically arose from any combination of not 
using optimal settings, starting with an uncleaned extruder screw, and/or too much 
PCM42 in the mixture (discussed earlier). As a reference, the filament diameter 
of pure HDPE and the composite was measured over a ten-minute time period, as 
shown in Figure 2.2. The composite had slightly more variance in filament diameter 
than pure HDPE, which could cause inconsistencies within the print, but was still 
useable for FFF purposes. 
Figure 2.1 Comparison of filament with (a) a consistent diameter and (b) an inconsistent diameter. 
Common extrusion practice requires a balance between the temperature of 
the material and flow through the nozzle. The amount of PCM content can affect 
the settings required to produce the desired filament diameter. Heater tempera-
tures were kept between 170 and 210 ◦C to ensure the filament properly melted, 
but did not burn, and screw speeds were set between 3 and 6 RPM to adequately 
move material. Adjustments were made based on the analysis of the filament di-
51
https://lh3.googleusercontent.com/notebooklm/AKXwDQHd1AJN3Sclubg-_kYrsu9cnrnZsivyenavBv726RQZjZ9RanJdfSvZdIh_klH3EP9_BSnuOGhPmScs4jwUmMY6Vu3fDSUN5jSuJ88yDOebHSERRlrezuDyoybxl7ID1mGexq4ZRw=w1280-h464-v0
2c88e182-bcec-452a-bb34-9954cdf5dad2
https://lh3.googleusercontent.com/notebooklm/AKXwDQEB_a-qQrzD3BLSSBBqOlr-V7LWcSjaPwYELWMu04trdYICrxkx5zWhmaFB7ef5j34qZOnZrQUBI_JtaRlH5WfYZ1ZRJWAHlziS-dthTQ5hZOQsyTdoCieU1y7ROrJmPHRMOhYN=w1119-h280-v0
42520c8f-350e-44a9-b6b5-99129f946321
Figure 2.2 Filament diameter, utilizing optimum settings and a clean extruder screw, versus time for (a) pure HDPE and (b) the PCM42/HDPE composite. 
ameter. From this analysis, the settings that produced the most consistent filament 
diameters for pure HDPE and the composite studied here are shown in Figure 2.3, 
which conveys the screw speed, heater temperatures, and nozzle diameter. Due to 
the incorporation of PCM42, the composite settings are ideal at the lower heater 
temperatures (190 ◦C) and screw speed (4 RPM), whereas the pure HDPE extrudes 
best at the higher ranges (200 ◦C and 5 RPM). Additional factors, such as block-
ages within the extruder and heavy directional cooling (from the cooling fans), can 
influence the consistency and shape of the filament. From the optimal parameters 
provided, the settings can be altered further depending on the response of the ma-
terial at the specific time of extrusion. 
Figure 2.3 Optimal extruder settings for pure HDPE (200 ◦C and 5 RPM) and the PCM42/HDPE composite (190 ◦C and 4 RPM). 
52
https://lh3.googleusercontent.com/notebooklm/AKXwDQEm3vYbB45DPikY_Rneryo-jfeKyOh7bCV3rDA3VJ5na2ZjLnO3NtQJXVzwCX3Jmy5vCMi30cCZQvwX4S_WP7FCIbUmyBIr4-NppZyTLgoY1O-1MabusaxFzPiIDucbsg-Xy50Dag=w720-h601-v0
e6001ce1-6749-4022-82d0-5ca75126caea
2.1.3 Additive Manufacturing 
Pure HDPE and shape-stabilized PCM42/HDPE composite samples were 
3D printed using a MakerGear M3-ID (Beachwood, OH) with Gcode sliced using 
Simplify3D software. The print settings are shown in Table 2.1, and the general 
pathing of the G-code for the samples is shown in Figure 2.4. When printing HDPE 
using FFF, adhesion and detachment is difficult due to the high shrinkage of the 
material. Schirmeister et al. [57] evaluated several types of build plates for use in 
printing HDPE, and good adhesion was found either using SEBS (Kraton FG1901 
G) or roughened HDPE. However, they found that detachment from the heated 
SEBS build plate was much easier than from the heated roughened HDPE build 
plate. In both instances,the build plate was heated to a temperature of 60 ◦C. 
Figure 2.4 Schematic diagram of the material deposition process. 
In the current study, a heated HDPE build plate was also used; however, 
a smooth build plate provided excellent adhesion with minimal curling for pure 
HDPE filament, so roughening or a SEBS build plate was not necessary. Delam-
ination between the layers and curling was observed during the printing of larger 
53
Table 2.1 Print Settings 
Setting Value Nozzle Diameter 0.35 mm 
Nozzle Temperature 240 ◦C First Layer Height 0.18 mm Layer Thickness 0.20 mm Line Width 0.42 mm 
Fill Percentage 100% Material Flow 1.00 
Build-Plate Temperature 60 ◦C Filling Pattern Lines, 45◦Offset Alternating 
First Layer Printing Speed 550 mm/min Printing Speed 1100 mm/min 
HDPE samples, as seen in Figure 2.5. The delamination and subsequent curling 
was caused by the temperature disparity between the extruded material ( 240 ◦C) 
and the ambient printing environment (25 ◦C). Similar problems have been de-
scribed by Choi et al. [61] when printing with ABS. Choi et al. [370] noted that 
as the build-plate temperature increased, print results near the build plate im-
proved; however, layers farther away from the build plate still showed delamination. 
To mitigate the delamination issue in the print farther away from the heated build 
plate, an elevated-temperature environment, similar to Zawaski and Williams [371], 
was implemented(see Figure 2.6). Successful printing was observed for heated-environment 
temperatures between 60 ◦C and 65 ◦C. The elevated temperature significantly im-
proved the bonding of the layers and reduced curling and delamination, thereby 
reducing the frequency of failed prints. 
Although the heated HDPE build plate was successful in promoting good ad-
hesion, the print became difficult to remove since the first layer was fused to the 
build plate.In the present study, initial prints resulted in the bottom of each sam-
ple being destroyed during the removal process. Therefore, a design modification 
was implemented to resolve this issue by simply adding extra depth to the sample 
disks, and, when required, the final surface was sanded until a desired surface finish 
54
https://lh3.googleusercontent.com/notebooklm/AKXwDQH-UrQKVKpLV16orgkydJZpSE_856QkWmcKoLityEJvBy42u5GtGxayzmhT5YF19mTRGbISwbOR8YTW3pLGU_Lfa3QER7Y23Thw3Vzilzrgh2ejxjNet8vSKPfA6Xixhxv4riQASA=w606-h496-v0
8870f5ca-7cd0-434d-aa93-d51a535c8d34
Figure 2.5 Curling causing layer separation and delamination of a print sample prior to implementation of the heated build environment. 
and/or dimension was attained. 
It was found that the shape-stabilized functional composite prints had notice-
ably less curling and were easier to remove from the build plate than pure HDPE 
prints, which suggests that the PCM reduced the effect of these issues. Any print-
ing problems with the composite typically stemmed from inconsistent filament qual-
ity or issues introduced by the heated enclosure, which caused either obstructions in 
the nozzle or under-extrusion of the sample. These issues were resolved by visually 
screening the filament before use and increasing the material flow when the diame-
ter was significantly below the nominal 1.75mm. 
In the heated environment, the composite feedstock would become slick with 
PCM since the ambient temperature inside of the heated enclosure was greater 
than the phase-change temperature (42 ◦C). Despite the aforementioned difficulties, 
multiple disk samples (25-mm diameter and 4-mm thick) were successfully printed, 
which can be seen in Figure 2.7(a) and 2.7(b). The slick filament occasionally cre-
ated extruder clogs, but a slower print speed reduced the frequency of this issue. 
55
https://lh3.googleusercontent.com/notebooklm/AKXwDQFQxAVz29sgcoQ1YxYfLI8P4uVMrXtS56Vy8b70USR87sKgsY67SjnOKDeBygPIxGHQxITEHJbyDrU26jfSdeJlzP-wudp6OTgyJw-Pn3RSQaCJ8FccVS4VfTNaeXW5Gvo6rpVK=w610-h622-v0
a7466ff7-9d1b-4add-85ac-dcc4eb25259d
Figure 2.6 3D printer enclosed in an elevated-temperature environment. 
2.1.4 Molding of Bulk Samples 
A custom machined mold was used to create the bulk material samples used 
as the baseline for the thermal characteristics of the printed samples. The bulk 
material samples were made to have the same dimensions as the 3D printed sam-
ples. The PCM 42/HDPE composite filament, pure HDPE, and pure PCM42 were 
melted down and compression molded into 25-mm-diameter and 4-mm-thick disks. 
Processing temperatures for the pure HDPE and composite were around 200 ◦C. 
Resultant molded samples for both the HDPE and the composite are shown in Fig-
ures 2.7(c) and 2.7(d). 
56
https://lh3.googleusercontent.com/notebooklm/AKXwDQEkh7MY-z8V9pz8D8cixZy4R8Wj3ld2brMT94AhPs7xlFSjgEJ9asA3ovkFPHA_UK3udxKhhSN6BnZiedbeO4_DHEETH619H0FqiINpe7LF99mnnBv74H6P2nFtbfL2grQOIFmmZA=w811-h723-v0
10f3f846-0603-4e03-82ae-f75ff1d995aa
Figure 2.7 Images of the samples (25-mm diameter and 4-mm thick) showing (a) printed HDPE, (b) printed PCM42/HDPE composite, (c) molded HDPE, and (d) 
molded PCM42/HDPE composite. 
2.2 Experimental Methods 
2.2.1 Differential Scanning Calorimetry 
The latent heat of fusion and phase-change temperature of the PCM42/HDPE 
composite filament was measured using a DSC (DSC 3 STARe, Mettler Toldeo, 
Columbus, OH). The masses of five random samples from the filament were mea-
sured using a balance (XS105DU, Mettler Toledo, Columbus, OH). The samples,ranging 
in mass between6 and 18mg, were placed in 
40-µl 
aluminum crucibles. The temper-
ature of each sample was initially held at 10 ◦C for 10min and then heated from 10 
to 200 ◦C at 2 ◦C/min. Each sample was held at 200 ◦C for 10min and then cooled 
at 2 ◦C/min until it reached a temperature of 10 ◦C. Temperature and heatflow 
were recorded every one second. The heating and cooling cycle was performed at 
least two times because each sample needed to be melted down once to make good 
thermal contact with the bottom of the crucible before the actual measurement. 
57
https://lh3.googleusercontent.com/notebooklm/AKXwDQFgZRxG89_jtoZI08F4hs5Li5boJKASmlH6_Zl0r-yO-LaQmyz2zJvzpjo9LQO2D4NSx9YU5_wQX3-cf7LbGIGHeKY0DQt_jnZsSX_Q4n_308lsf6p0tQ22Yc0ymaHJlmi0EH1kZw=w891-h648-v0
eca983f0-ad68-4927-8474-89075718483a
Since PCM42 is not a pure substance,the phase change happens over a range 
of temperatures and not just over a single temperature (as is observed in a pure 
substance). The melting temperature range of the composite was calculated based 
upon the onset and endset temperatures from the heatflow versus temperature 
graph as shown in Figure 2.8. The onset and endset temperatures are the temper-
atures where the material begins and ends the melting phase, respectively. These 
temperatures are defined as the intersections of the inflectional tangents of the lead-
ing and trailing edges of the peak and the extrapolated tangent of the baseline. 
The latent heat of fusion is calculated by the area under the peak of the heatflow 
versus time curve. 
Figure 2.8 Heat flow versus temperature diagram illustrating latent heat of fusion, onset, endset, and peak temperatures. The first peak represents the PCM42 phase 
change and the second peak represents the HDPE phase change. 
58
https://lh3.googleusercontent.com/notebooklm/AKXwDQH7W2mQBxLA-GIrI82SMygbXLu4__5jLIKDQ0tq9aZ9_tQXsjbF8RkHTLFX5sS3et0DEBNdQmFmis6dH7LBOrXJqhl1c5x7lNriLWvrvT_f0gFyvQin-wOPYptdkRnIanvHB_ozFw=w526-h658-v0
0170fd9f-20dc-402b-8f40-d5858e0da8fb
2.2.2 Thermal Conductivity Measurements 
A thermal constants analyzer (Transient Plane Source (TPS) 2500S, Hot Disk, 
Gothenburg, Sweden) was used to measure the thermal conductivity of the PCM42/HDPE 
composite bulk material and the printed samples. The isotropic module with a 
4-mm-diameter Kapton sensor (C7577, Hot Disk, Gothenburg,Sweden), which in-
cludes both a resistive heater and a temperature sensor, was used. The sensor was 
sandwiched between two matching 25-mm-diameter and 4-mm-thick samples made 
of the same material and identically manufactured (see Figure 2.9). Joule heating 
was applied, which produced a dynamic temperature field in the sample and sensor. 
The temperature response of the sensor was monitored, and the thermal conductiv-
ity of the sample was determined from a model. A power of 50mW and time of 10s 
was used. For statistical significance, ten tests were performed for each sample to 
obtain an average thermal conductivity and standard deviation. 
Figure 2.9 Hot Disk TPS operation setup. The Kapton sensor is sandwiched between two bulk PCM42/HDPE composite samples. 
59
Table 2.2 Phase-change temperature and latent heat of fusion of the PCM42/HDPE composite filament. 
PCM42 HDPE Tpeak (◦C) Tonset (◦C) Tendset (◦C) 
hsl(kJ/kg) 
Tpeak (◦C) Tonset (◦C) Tendset (◦C) hsl (kJ/kg) 
Pure 44.47 40.36 46.28 200.00 133.33 125.95 136.75 191.68 Sample 1 40.70 37.67 42.51 59.94 124.59 118.38 126.54 116.42 Sample 2 40.58 37.68 42.49 60.02 124.50 118.66 126.37 118.27 Sample 3 40.55 37.63 42.43 62.68 124.43 118.36 126.39 123.30 Sample 4 40.61 37.61 42.48 63.28 124.44 118.41 126.50 122.91 Sample 5 40.58 37.82 42.66 72.40 123.78 117.79 126.67 117.87 
Sample Average 40.60 37.68 42.51 63.66 124.35 118.32 126.29 119.75 Sample St.D 0.06 0.08 0.09 5.11 0.32 0.32 0.36 3.14 
2.3 Microscopy 
The microstructures of the PCM42/HDPE composite filament and resultant 
prints were visualized using a scanning electron microscope (SEM, Quanta 650, 
ThermoFisher Scientific, Hillsboro, OR). To allow for high-vacuum setting used for 
visualization, the samples were coated in gold (Sputter Coater 108, Cressington Sci-
entific Instruments, Watford, UK). An accelerating voltage between 15kV and 20kV 
was used, and the vacuum pressure was between 3.5 and 8 × 10 6 Torr. To observe 
the cross section of the filament and printed samples, liquid nitrogen was used to 
freeze the samples before shattering. 
2.4 Results and Discussion 
2.4.1 Phase-Change Temperature and Latent Heat of Fusion 
The PCM42/HDPE composite filament was extruded and samples were taken 
from five randomly selected regions throughout the extrusion process. Results are 
shown in Table 2.2 for each of the five samples that were tested in the DSC to mea-
sure the average and standard deviation of the phase-change peak temperature 
(Tpeak), 
onset temperature 
(Tonset), 
and endset temperature 
(Tendset). 
Values of 
the five samples and the standard deviation show that the material composition 
is fairly consistent. 
The phase-change peaks for pure PCM42, pure HDPE, and the composite fil-
ament are shown in Figure 2.10. In the figure, the first peak represents the phase 
change of PCM42 around 42 ◦C, and the second peak represents the phase change 
60
https://lh3.googleusercontent.com/notebooklm/AKXwDQFSt16BieSr_9hJawiF5uuHlbjOb454NpIu6LYGvMvzxrbRTWcg_uiN7nX7Gd5XZW8Aad5-EU-jEotVWcqnMDq1NTw6uxvW0MBi9zNoJWtQMWMnRJK3ZzCp2bOnnREjqYQtA-J_dA=w865-h651-v0
d30e529c-2404-4da7-bf39-8dec026309c5
of the HDPE around 130 ◦C. Effective latent heats of fusion 
(hsl) 
for both the PCM42 
and HDPE in the composite were also calculated by integrating the area under the 
peaks with respect to time in Figure 2.10. Baseline samples for pure PCM42 and 
pure HDPE are represented in the table as Pure. 
Figure 2.10 Heatflow versus temperature for pure PCM42, pure HDPE, and the PCM42/HDPE composite filament. 
The latent heat of fusion for the pure PCM42 is approximately 9% lower than 
the published value of the manufacturer,which is 218 kJ/kg. It is interesting to note 
that the latent heats of fusion for both the pure PCM42 and the pure HDPE are 
very close in value, where the HDPE latent heat of fusion is approximately 5% less 
than the PCM42 value. Based upon the results in Table 2.2, the composite filament 
has an average effective 
hsl 
for PCM42 of 63.66 kJ/kg. This value is only 31.8% of 
the latent heat of fusion of 200.00 kJ/kg for pure PCM42. It is hypothesized that 
if there is 40% of the PCM42in the filament, the effective 
hsl 
should be 40% of 200 
kJ/kg, which is 80 kJ/kg. The difference between the true value and the hypothe-
sized value may be due to multiple factors, such as material loss during the mixing 
and extrusion processes involved in the fabrication of the composite filament, the 
61
chemistry of mixing the materials, or a combination of both. Regardless, the ther-
mal energy storage capability of the composite filament effectively acts as if there is 
31.8% of the pure PCM42 in the composite. 
According to the results(Table 2.2 and Figure 2.10), the composite filament 
causes the peak, onset, and endset temperatures to decrease. The peak melting 
temperature for pure PCM42 is 44.47 ◦C, compared to the average peak melting 
temperature of 40.60 ◦C for the PCM42 in the composite. An even greater decrease 
in melt temperature for the HDPE in the composite is observed, with pure HDPE 
having a peak melting temperature of 133.33 ◦C, and the HDPE in the composite 
having an average peak melting temperature of 124.35 ◦C. This phenomenon can 
help explain why the composite required lower temperatures during the extrusion 
process as compared to the extrusion temperatures of the pure HDPE (see Figure 
2.3). 
2.4.2 Thermal Conductivity 
Each sample was measured ten times to determine an average thermal con-
ductivity (k) and standard deviation, and the results can be seen in Table 2.3. Fig-
ure 2.11 displays the information in a bar graph for comparison purposes. In the 
figure, the error bars represent the standard deviation. The pure PCM42 does not 
have a print value due to the inability to print pure PCM42 without a shape stabi-
lizer. Based upon the results,it can be seen that pure HDPE and pure PCM42 in 
their bulk forms have a measured thermal conductivity of 0.576 W/mK and 0.276 
W/mK, respectively. The thermal conductivity value for pure PCM42 is 10.4% 
higher than the values provided by the manufacturer, which is 0.25W/mK. The 
thermal conductivity of the molded bulk PCM42/HDPE composite was measured 
to be 0.413 W/mK. This value corresponds to a 28.3% decrease in the original ther-
mal conductivity of the HDPE, which shows that the addition of the PCM42 mixed 
into the HDPE causes the overall thermal conductivity to be lower than the value 
62
https://lh3.googleusercontent.com/notebooklm/AKXwDQFvSjqB5lgABUkSufHtWLc8xAT0pUjlvRWG-PaWjO1vri4uHvBHUx24vpZzgne2Mn5kByPnDRz0MKlqDXDPFlEX4HKwCjyT2OeEwbGmmNpHYcddZH1cmQ-H6rf_UihYTz2Bqj2B=w874-h613-v0
3e365589-99c4-4bd8-8c8c-5a5706bafdd1
Table 2.3 Thermal conductivity (average of each sample measured ten times) of the molded and printed samples. 
Sample k [W/mK] St.D Bulk Pure HDPE 0.576 0.001 
Bulk PCM42/HDPE Composite 0.413 0.013 Bulk Pure PCM42 0.276 0.005 Printed Pure HDPE 0.435 0.026 
Printed PCM42/HDPE Composite 0.365 0.024 
of pure HDPE. 
Figure 2.11 Thermal conductivity (average of each sample measured ten times) of the molded and printed samples. The error bars represent the standard deviation. 
The printed pure HDPE and printed PCM42/HDPE composite were mea-
sured to have thermal conductivities of 0.435 W/mK and 0.365 W/mK, respec-
tively. These values are noticeably lower than the respective thermal conductivi-
ties of the bulk materials. The reason that the printed materials have a lower ther-
mal conductivity than their bulk counterparts is because of the air gaps that are 
formed within the printed part from the actual printing process. The small air gaps 
cause thermal contact resistance between the layers. Based upon the current state 
63
of FFF, air gaps within the printed part will always be present, although some re-
cent efforts have been made to reduce this effect [275, 277]. The thermal conduc-
tivity of the printed part will change based upon the size and quantity of these air 
gaps, which are highly dependent on print settings. The printed HDPE was 24.5% 
lower than that of the bulk value, and the printed composite was 11.6% lower than 
the bulk composite. The smaller difference in thermal conductivity between the 
bulk and printed composite compared to the pure HDPE bulk and printed samples 
may be due to PCM42 filling in the air gaps during the printing process. Evidence 
of this is shown in the microstructure visualization results. 
Another reason for the decrease in thermal conductivity for the printed mate-
rial may come from the surface quality of the printed part versus that of a molded 
version of the same material. Similar to the reasons for why the air gaps are formed 
within the material, the FFF process results in a poor surface finish depending 
upon the printing parameters. A poor surface finish leads to poor thermal contact 
with the respective heating source (Kapton sensor) used to make the measurement, 
which inherently lowers the overall measured thermal conductivity. Without any 
post processing,such as sanding,the printed samples had a noticeably rougher sur-
face finish than the molded samples, which can be seen in Figure 2.7. 
2.5 Microstructure Visualization 
A cross-sectional view of the extruded PCM42/HDPE composite filament 
(before FFF) is shown in Figure 2.12. Figure 2.12(a) shows the filament with the 
edge visible,and Figure 2.12(b) shows a closer view of the center of the filament. 
Microstructure images of the pure materials are shown to be clearly differentiated 
in [200, 203] where pure extruded HDPE has a platelet-like structure, and PCM42 
has a cloud-like structure. In Figure 2.12, the structure of the HDPE is clearly seen 
with the PCM encapsulated in between the platelets. Based upon visual inspection, 
the mixing of the two materials appears to have produced homogeneous filament. 
64
https://lh3.googleusercontent.com/notebooklm/AKXwDQF12eomnzrzN3lIa-Z6x1ommSjf7FcAPHAjcweBcnE3OYeoHoLTSFd2rbAFI1x9E5L5YulgN-9-fdncRMBUxGAP-kazGLLQen1jsYebg1UxYKClbxKR9U1zi-2H0OhVLpNGJdnrbA=w1280-h576-v0
bb961c10-a48d-4877-a838-fbd464a636e4
Figure 2.12 PCM42/HDPE composite filament (a) scale bar 100 
µm 
and (b) scale bar 50 
µm. 
The fracture surface (cross-sectional view) of both the composite and pure 
HDPE printed samples at different magnifications can be seen in Figure 2.13. While 
Figure 2.13(a) and 2.13(b) show the printed composite for different magnifications, 
Figure 2.13(c) and 2.13(d) show the printed pure HDPE for corresponding simi-
lar magnifications. It is interesting that the composite material retained its basic 
microstructures(as seen in Figure 2.12) after the second extrusion of the material 
during the FFF process. 
Also in Figure 2.13, the print directions and print patterns can be clearly ob-
served, and noticeable air gaps, formed by the printing process between parallel 
beads of material, can be seen. Despite having an infill percentage of 100% for both 
samples, small air gaps are still present within the printed material. The air gaps 
are one of the main reasons for the reduction in thermal conductivity in the printed 
samples when compared to the bulk material thermal conductivity. The presence 
of air gaps causes a decrease in thermal contact from one layer to the next, there-
fore causing a decrease in overall thermal conductivity. As the amount and size of 
small air gaps increases for a given print, the thermal conductivity is expected to 
also decrease. 
65
https://lh3.googleusercontent.com/notebooklm/AKXwDQFpYqHX57VIy48lsSkhzcCn0JQuHHfJ5fNlLgTHFnuzl33lXKGA1zHFsrlOMLycW3z2dXv9yL-xG2Sc1sX69iqSU4wKAv_iCPjc37yjE45SVCZHeQl_R8o75tSUo6dTWu4BEcLe-w=w951-h859-v0
a10ed394-ad7c-43df-87ed-e0b9be92dd4d
Figure 2.13 Printed samples (a) PCM42/HDPE composite scale bar 500 
µm, 
(b) PCM42/HDPE composite scale bar 200 
µm, 
(c) HDPE scale bar 500 
µm, 
and (d) 
HDPE scale bar 200 
µm. 
It can be observed in Figure 2.13(a) and 2.13(b), that when the composite fil-
ament is printed, the air gaps becomepartially filled with PCM42.This leads to a 
reduction in air-gap size, which in turn leads to less of a decrease in thermal con-
ductivity. The air gaps formed when printing pure HDPE can be seen in Figure 
2.13(c) and 2.13(d), and when compared to the printed composite, appear to be 
more prominent. The relative effect of the air gaps can also be observed in Figure 
2.11, which shows that the difference in thermal conductivity between the bulk ma-
terial and the printed material is greater for the pure HDPE than it is for the com-
posite. 
66
3 Moisture affinity of HDPE/PCM composites 
In this chapter, the further characterization of the HDPE/PCM composite is 
performed to characterize the materials moisture affinity. Characterization includes 
the steady-state and transient adsorption and desorption of the composite material, 
along with the the base constituents that comprise of the composite. The adsorp-
tion and desorption characterization of a material helps with the understanding of a 
materials response when exposed to humid environments. The work in this chapter 
contributed to the publication in the Royal Society of Chemistry Advances Journal 
[202]. 
3.1 Sample Preparation 
PureTemp 42 (PureTemp, Minneapolis, MN), an organic PCM which changes 
phase at 42 ◦C and has a latent heat of fusion of 218 kJ/kg, was heated and mixed 
with HDPE (PPR-HDPE01, Premier Plastics Resins, Lake Orion, MI). A mixture 
of 50% PureTemp 42 and 50% HDPE by mass (50/50) was prepared. The mix-
ture was then formed into pellets utilizing a shredder (SHR3D IT, 3devo, Utrecht, 
Netherlands). The pellets were then fed into the hopper of a filament extruder 
(next 1.0, 3devo, Utrecht, Netherlands) to fabricate 1.75 mm diameter filament. 
3.2 Microscopy 
Filament samples were frozen using liquid nitrogen and then subsequently 
shattered to examine the interior of the filament. The samples were gold coated 
(Sputter Coater 108, Cressington Scientific Instruments, Watford, UK) for visual-
izing with a scanning electron microscope (SEM, Quanta 650, ThermoFisher Scien-
tific, Hillsboro, OR). 
Figure 3.1 shows SEM images of the extruded filament containing HDPE 
and PureTemp 42. Prior work examined the microstructures of both pure HDPE 
and pure PureTemp 42 [12,13]. The platelet-like structure of the HDPE is clearly 
seen with the lattice-like structure of the PCM embedded in between the platelets. 
67
Upon visual inspection of Figure 3.1 and other similar SEM images, the dispersion 
of PCM appears to be homogeneous. 
Figure 3.1 Microstructure visualization of HDPE with PureTemp 42 (50% PCM by mass) at 25 ◦C (a) image showing edge of filament, and (b) view showing HDPE 
(platelet-like structures) and PCM (lattice-like structures). 
3.3 Dynamic Vapor Sorption 
Both equilibrium (steady-state) and transient adsorption and desorption be-
haviour of the materials are important to characterize the affinity of water. While 
the steady-state isotherms establish the total moisture adsorption capacity, the dif-
fusion coefficient determines the response of the material (i.e., how quickly water 
can be adsorbed or desorbed). A dynamic vapor sorption apparatus (DVS Advan-
68
https://lh3.googleusercontent.com/notebooklm/AKXwDQGEORLcFfFP9D7vl2AMFNWOKywY2orukQWS9DyzpNzg5z4Ryu_yG8x6DAONcIu_a0BhvBeVw6-Suz9a5pG08-JDHwkxnOu90pzDS05KFCgV_iVJmpHnxriJBMWmhvlTc-uA9Q63=w1161-h610-v0
867c4fc7-b95a-4663-8716-8aa40bc6f7e4
tage, Surface Measurement System, UK) has been used to conduct the steady-state 
and transient experiments [14,15]. 
Figure 3.2 shows the DVS experimental setup. The relative humidity is con-
trolled by mixing wet and dry nitrogen gas (N2). A vapor sensor is used to measure 
the relative humidity. Water vapor, with a known concentration, flows over a sam-
ple that is suspended from an ultra-fine microbalance, which is used to measure 
the change in weight of the sample due to adsorption or desorption of the vapor 
molecules. The sample mass for various experiments varied between 1–3 mg. It is 
worth noting that regardless of the variation of dry sample mass, the percentage in 
mass is an indication of potential for moisture for various samples and provides the 
relative comparison independent of the sample mass. 
Figure 3.2 Components of the experimental setup. 
Temperature is an important factor for moisture adsorption and desorption 
potential. Prior studies have shown that, in general, the moisture adsorption capac-
ity of the material increases with temperature while the response time decreases, 
indicating higher diffusion coefficients [372]. 
In the current study, the samples were suddenly exposed to a dry or humid 
environment and the weight change due to moisture adsorption and desorption was 
measured as a function of time. The data was then used to calculate the steady-
69
https://lh3.googleusercontent.com/notebooklm/AKXwDQGPyGfF_m2mMEnTEWdU8ZoNG1QDMrqSiRqpqIgVvoFxuOysvG3yrAoeyRREJdHQf4V8FtV-6syi8a5_Qs8XazDNVonbWUWLsKm2pcxr2aCqf3whMWJ8JxQCca5z-s54OkYW2-JsSA=w1280-h686-v0
bf55436c-c2f3-4596-98b7-f28da74e5b37
state capacity and diffusion coefficients. 
3.4 Steady-State Adsorption/Desorption Capacity 
Steady-state experiments have been conducted to investigate the moisture 
adsorption capacity of the materials. The experimental procedure is presented in 
Figure 3.3. A sample, with a known initial mass, is exposed to a series of moisture 
levels, and the change-in-mass response is recorded. The experiments are conducted 
for both adsorption and desorption modes for a set temperature. The entire process 
is repeated for various temperatures, and the steady-state mass gain at respective 
humidity conditions is recorded to establish the moisture adsorption/desorption 
isotherms at specified temperatures. The relative error in measurement is less than 
1 mg. The average variation in relative humidity and temperature is noted as ± 1% 
and ± 0.25 ◦C, respectively. Prior to the beginning of the test, each sample was ex-
posed to a completely dry-air condition (0% RH) for sufficient time to ensure that 
the sample had no initial moisture content at the beginning of the test. The same 
drying test has been repeated for different temperatures. 
Figure 3.3 Experimental procedure to establish adsorption/desorption isotherms. 
70
https://lh3.googleusercontent.com/notebooklm/AKXwDQGUJHkl6w4s5UNcyTJwM7vK5XwqaBMZjcONmScAG3hlAuKuBV-aHb50O4Wv8Mb6UpBFGAJMkyI33tHza61MrMmzS1rTyzo1VqgQjgNp7VEx3z9u8237M5aQQhjkqn3XQBAEfkw4aQ=w1280-h706-v0
14374c86-6e5a-4873-8bb5-d87a0f4bf2bb
3.5 Transient Adsorption/Desorption Analysis 
The transient response of the sample is established by evaluating the time re-
sponse of the sample when the ambient moisture content is changed as a step func-
tion, and the mass of the sample continues to change until it reaches the steady-
state condition. Two types of experiments were performed: (i) small incremental 
change in moisture content (10%), and (ii) large incremental change in moisture 
content (70% and 90%). Figure 3.4 presents representative data for the second type 
of test. As can be noted, the relative humidity in the chamber was increased from 
0% to 90% and then decreased back to 0%. Once the sample was completely dry, 
another cycle with 70% RH was initiated. 
Figure 3.4 Transient experimental procedure to establish the diffusion coefficients. 
The one-dimensional transient diffusion equation can be solved to extract the 
bulk diffusion coefficients (Equation 4.1) for the samples under consideration using 
appropriate initial and boundary conditions (Equation 4.2). The diffusion coeffi-
cient is obtained by curve fitting the solution while minimizing the error in pre-
dicted and measured values [14,15]. 
71
∂ρ 
∂t 
= 
D 
( 
∂2ρ 
∂r2 
+ 
1 
r 
∂ρ 
∂r 
) (3.1) 
Initial and boundary conditions. 
ρ(r, t 
= 0) = 0 (3.2a) 
ρ(r 
= 
1, t) 
= 
ρ∞ 
(3.2b) 
∂ρ 
∂r (r 
= 
0, t) 
= 0 (3.2c) 
3.6 Results and Discussion 
Samples of HDPE, PureTemp 42, and a 50/50 (by mass) composition were 
prepared and subjected to the experimental procedures outlined in the preceding 
sections. The steady-state isothermal experiments were performed for multiple tem-
perature settings (25, 35, and 45 ◦C). For pure PCM and the composite sample, 
the 45 ◦C experiments were excluded since the melting temperature for PCM is 42 
C. Figures 3.5 - 3.7 show the adsorption and desorption isotherms for pure PCM, 
HDPE, and the composite sample, respectively. It also can be noted that the rel-
ative hysteresis is negligible except at relatively higher humidity values, and the 
capacity is increased slightly with increase in temperature for both types of materi-
als. 
The most important observation is the total capacity. Pure PCM can adsorb 
about 30% more moisture at higher humidity values. Similarly, the composite sam-
ples adsorb almost twice the amount of moisture adsorbed by the pure materials, 
which can be explained in terms of potential voids created during the mixing pro-
cess. Regardless, the overall change in the sample mass is negligible due to a very 
small amount of moisture adsorption. It is concluded that the material has very 
little affinity for moisture. 
72
https://lh3.googleusercontent.com/notebooklm/AKXwDQGf_b34xSpGK1uElKEtEL1XXHOZ_gddLIGO9Twn85ZRqEY8GGFMBs1AoVF6hXknFshlm_miZ2P4z3pJHKSI9QtMINASK0LvXsAwFJvHZ42e9LufsLKU2veMWrOAfBCvhGzGjecpUQ=w1102-h795-v0
1c27d836-f663-4c8f-b2e2-72a958184eee
https://lh3.googleusercontent.com/notebooklm/AKXwDQHJVEGNesp01a5SsHMLrKw_k0MjX7rLeZQG4YvjRLFOsxVi9KCVE1Mj-b8zBDrVIS-M4yAJu_2tLUwyIi0QEt4JuTw49r0Ak1QKCb9Ec7r928Jd7JVBgbCSEzJUuVXmoRb3xd9RyQ=w1090-h691-v0
ef0f0eea-cd79-43b6-be73-b6fad8af3fe4
Figure 3.5 Adsorption/desorption isotherms for pure PCM at 25 and 35 ◦C. 
Figure 3.6 Adsorption/desorption isotherms for pure HDPE at 25, 35, and 45 ◦C. 
The transient performance of the samples has been established in terms of 
bulk diffusion coefficients, as shown in Table 3.1. The diffusivity is determined for 
both the adsorption and desorption processes to observe any noticeable differences 
in the mechanism. Also, the temperature of the operation has been varied to estab-
73
https://lh3.googleusercontent.com/notebooklm/AKXwDQFUtvx2m-h48VmPEbO7AyBvfPpsqfYUgsHMZinLV3CZhwUEHobQ9lzxNQhhN8YXh0LIrMGMEdlIJ3fAfGZK-E1Xsx3Yq4tQqI35rEl10-zuQKKFd2b_bXNLQGEuV-SmO-cr3uQ8BA=w1092-h768-v0
153967f0-3e65-4cad-9f28-697009806ca2
Figure 3.7 Adsorption/desorption isotherms for 50/50 composite at 25 and 35 ◦C. 
lish the impact of temperature. As with the steady-state experiments, the 45 ◦C 
temperature was not reported for pure PCM and the composite sample since the 
PCM starts melting at 42 ◦C. Based on the established values (± 5% uncertainty), 
it can be concluded that relative moisture diffusivity for pure PCM and the com-
posite (50/50 by mass) is around 10 and 3 times higher, respectively, compared to 
the pure HDPE. Furthermore, the mass diffusivity for moisture is independent of 
adsorption or desorption processes as well as the temperature. The relatively small 
variation in predictions can be justified in terms of errors in measurements. 
74
Table 3.1 Adsorption/desorption diffusion coefficients. 
Material Composition 
Temperature (◦C) 
Adsorption Diffusivity 
m2/s (x10−7) 
Desorption Diffusivity 
m2/s (x10−7) Pure PCM 25 10.12 10.34 
35 11.95 11.19 Pure HDPE 25 1.25 1.29 
35 1.33 1.34 45 1.45 1.41 
50-50% HDPE + PCM 25 4.23 4.12 35 3.95 3.98 
75
https://lh3.googleusercontent.com/notebooklm/AKXwDQGhFm-3m5uhVz4lM8Rx66kEtOfoUpEkQp0dnOrRJdm14KUpBlPf2gKa6dWp4xuDJ43tXOJTp2U6A7n4QtbJx2JAT9Jkc2aSbJ-ZGGcpN4EpiJfPzw1aymAk3Ce0o9oKayv8mNpC2Q=w1126-h427-v0
5701b24b-da2a-484e-94d1-c6182cd1279f
4 Microencapsulated PCM and Thermoplastic Polyurethane 
Composites 
In this chapter, the fabrication and characterization of a new composite fila-
ment material comprising of a microencapsulated PCM (MEPCM) and a polymer 
for 3D printing. This composite material is a new alternative to the work described 
in Chapter 2. The composite material in this chapter uses a MEPCM where the 
microcapsules fully encapsulate the PCM and the polymer is used as a binding ma-
trix to combine the microcapsules into a homogoenous material. Characterization 
of the material includes thermal decomposition, thermal storage capacity, and tran-
sition temperatures. 
4.1 Characterization of MEPCM-TPU Pellets and Filaments 
4.1.1 Raw Materials 
The raw materials comprising the MEPCM-TPU Pellets were 80A TPU as 
the base material with inclusion of 24D microencapsulated PCM (MEPCM) spheres. 
Scanning electron microscopy (SEM) was used to image the MEPCM shown in Fig-
ure 4.1. There was a notable size distribution of particle sizes with some as small as 
5 
µm. 
Figure 4.1 Micrographs of the MEPCM spheres showing the size distribution. 
Thermal decomposition of the MEPCM and TPU was determined using ther-
mogravimetric analysis (TGA), with decomposition profiles shown in Figure 4.2. 
76
https://lh3.googleusercontent.com/notebooklm/AKXwDQGcQskGdH5o16Y4MVSoMRRaYVfOvboVxHHsQ6gaTiGWrGQxLapPzKPpm-rsvkfonu4I9TnGFXGfmpZOs7iVQng1WJiqrk0K5pQXO6sRLzktoVYDaSqeYXpH2slW12SfO1p_R0hZkg=w1280-h503-v0
5e977e64-b606-4acd-acc6-a2322424a341
The PCM decomposed rapidly at 407 ◦C, off-gassing to the extent that the sample 
exerted a downward force on the pan causing a spike in weight percentage to nearly 
150%. Two replicates of PCM were tested to ensure consistency of decomposition 
and are overlayed in Figure 4.2a. Thermal decomposition of the TPU occurred in 
two stages indicated by the derivative curve in red with an initial onset of 346 ◦C. 
Figure 4.2 Thermal decomposition profiles for (a) MEPCM and (b) 80A TPU 
4.1.2 Single Screw Extruded MEPCM-TPU Pellets 
MEPCM spheres were compounded with a single screw extrusion process in 
increments of 20 wt% to achieves 60 wt% and 80 wt% MEPCM in TPU. SEM mi-
crographs of the pellets show the aggregation of MEPCM in the TPU. Figure 4.3a 
shows the cross section of an extruded pellet and Figure 4.3b shows the density of 
sphere packing. There was observable damage imparted from the compounding pro-
cess shown by broken MEPCM shell fragments and surface denting of the spheres 
in Figure 4.3c and 4.3d, respectively. 
Thermal decomposition for both 60 and 80 wt% MEPCM exhibited similar 
bimodal decomposition as the virgin 80A TPU between 300 and 500 ◦C and are 
shown in Figure 4.4. There was mass loss at lower temperatures between 100 and 
250 ◦C which were attributed to volatilization of free paraffin PCM that was liber-
ated from the MEPCM shells during the compounding process. 
77
https://lh3.googleusercontent.com/notebooklm/AKXwDQHnKOSfulNv06eSQ-D_ZInu4sxjQYeWwB8u7OQum1OHTVYmPvHbS7pOLbgIqR4s96AmVex0gs-hqbXsq8Oxh36JZL9S6HnLszrzgPK7WtRDh4_IMG2QCRNjH0LPqPleRgbny-dEhA=w955-h703-v0
f8f8855e-0ec7-42fd-805d-0830b5e34920
Figure 4.3 SEM micrographs of TPU-MEPCM pellets produced from multiple compounding steps using a single screw extruder. (a) macroscopic image of 60 wt% MEPCM in TPU, (b-d) 80 wt% MEPCM in TPU emphasizing the encapsulated 
PCM. 
Transition properties of the single screw compounded MEPCM-TPU were ad-
versely affected by MEPCM shell breakage but melt enthalpies for the 60 and 80 
wt% MEPCM-TPU were 78.2 and 72.3 J/g, respectively. Full results are summa-
rized in Table 4.1. Transition temperatures were not affected, indicating that the 
PCM was still responsive to temperature changes. 
Table 4.1 Summarized Thermal Transition Properties of MEPCM-TPU Pellets 
Sample Name Extrusion Method (# extrusions) 
Onset 
Tm 
(◦C) 
∆Hm 
(J/g) Onset 
Tc 
(◦C) 
∆Hm 
(J/g) 24D PCM Powder n/a 19.2 171.3 22.3 169.0 60wt% MEPCM Single Screw (3x) 19.0 ± 0.2 78.2 ± 9.5 22.4 ± 1.4 72.1 ± 9.0 80 wt% MEPCM Single Screw (4x) 19.1 ± 0.3 71.3 ± 8.9 22.2 ± 1.5 60.8 ± 8.2 50 wt% MEPCM Twin Screw (1x) 19.6 ± 0.2 60.7 ± 15.8 22.8 ± 0.1 59.0 ± 15.5 60 wt% MEPCM Twin Screw (2x) 19.4 ± 0.3 42.5 ± 3.0 22.6 ± 0.2 36.3 ± 2.2 
4.1.3 Twin Screw Extruded MEPCM-TPU Pellets 
MEPCM-TPU pellets were also produced using a twin screw extruder with 
one compounding step to achieve 50 and two compounding steps to achieve 60 wt% 
78
https://lh3.googleusercontent.com/notebooklm/AKXwDQF7L_iz52A2erTT9FeLHX4_1NUaeM-0YTfXCpvAVVu47HClMTs26jrb2OWtkPyUHrcx4YhBeHRo99bbADD7py_lxrxEmt5KJVPQ_fL_DPSisbR7si_SIzVR2t__hVNBHywLgxhGEw=w1280-h484-v0
09380f54-0211-4bfa-a7df-1835bb4b87a5
Figure 4.4 Thermal decomposition profiles for (a) 60 wt% MEPCM-TPU and (b) 80 wt% MEPCM-TPU produced from multiple compounding steps using a single 
screw extruder. 
MEPCM to TPU. Reducing the amount of compounding steps led to reduced shell 
breaking as observed by SEM in Figure 4.5. There was evidence of a pock-marked 
void structure where MEPCM particles were removed after the fracture of a pel-
let in Figure 4.5a. The TPU texture was tackier from this process, shown by TPU 
bridging gaps induced by tensile forces in Figure 4.5b, which was not observed for 
the single screw extruded processing. 
Thermal decomposition of these pellets was similar to the single screw ex-
truded MEPCMs, where there was an initial loss from free PCM in the 100 and 250 
C region followed by the bimodal decomposition of the TPU between 250 and 500 
C. These results in Figure 4.6 indicate that some shell breakage did occur allowing 
for free paraffin to volatilize from the pellet. 
Transition properties of the twin screw compounded MEPCM-TPU are shown 
in Table 4.1 where transition temperatures were not affected by the compounding 
process. Notably, across 4 random samplings from the pellets, the 50 wt% MEPCM-
TPU appeared to have higher transition enthalpies and higher variability than the 
60 wt% MEPCM. The higher variability in the 50 wt% sample was likely from re-
duced mixing during the extrusion process. 
79
https://lh3.googleusercontent.com/notebooklm/AKXwDQE8CO8F-p8U7pDFEgG2RmOEj2ozokx_dssMhWRFIVJY7Sbe6a-w8IJxnCypZ3Cpf2kLEB8OaFAzbzXjsGVZH6unQQbSRNoYEmzylgunFX8fOOvGM9f9eddWARbveFbahxAoqEoISA=w870-h649-v0
1881617f-8d0d-4ab8-bbba-d51ca29d6cf4
Figure 4.5 SEM micrographs of MEPCM-TPU pellets produced using a twin screw extruder. (a,b) Images of 50 wt% MEPCM in TPU, (c,d) 60 wt% MEPCM in 
TPU. 
4.1.4 Extrusion of MEPCM-TPU pellets into Filament 
Compounded MEPCM-TPU from both the single screw (60 and 80 wt%) and 
the twin screw (50 and 60 wt%) were extruded into 2.85mm diameter filament on 
a Precision 350 filament extruder (3devo, Utrecht, Netherlands). The Precision 350 
extruder is a single screw extruder with four heating stages and a variable speed 
screw. The extrusion profile chosen can be seen in Figure 4.7. 
MEPCM-TPU material was dried at 80 ◦C for 4 hours before extrusion. Sam-
ples of material were taken after the drying period and melt enthalpies were an-
alyzed to determine if any loose PCM is lost in the drying period. Results show 
there were negligible loss in melt enthalpies from drying. After drying, each weight 
percentage were extruded only once into 2.85mm diameter filament. At the end of 
each extrusion, a substantial amount of liquid material was found in the hopper of 
80
https://lh3.googleusercontent.com/notebooklm/AKXwDQECF-GK6M8Hu7oiOjcqFFQGPNzXaNrjzqVQXM1PUbFKHtCIWcTbECSi9xX8oieH_dGk_JUlwbZ2caCwA_4_KdIEAlLYoRrwg3r2a7IyH4vOHy4j4rXwMmkPt9kxCpbOVlE_CyjTJw=w1280-h471-v0
9669b7b6-7675-410b-b01f-396af516f9f9
https://lh3.googleusercontent.com/notebooklm/AKXwDQFYXMsiZv1cbFfvmacAGdMVDY_juop999PMY7ql4O2TG5AgPE0eQ_cBgvQs1tviaqZEvQYc9OjMBqyUxPCGpBHyMsCby9cuvlJ8ssUhUTrURN4FSDZLp1vZZO8ERmI8UncmTwpLaA=w1167-h291-v0
3a964e45-24a6-4fa3-b2df-a3296fdbe6b5
Figure 4.6 Thermal decomposition profiles for (a) 50 wt% MEPCM-TPU and (b) 60 wt% MEPCM-TPU produced from one compounding step using a twin screw 
extruder. 
Figure 4.7 Extrusion profile for extruding TPU on a Precision 350 filament extruder. 
the extruder. This liquid is considered PCM that is loss from the material due to 
broken capsules. This loss of PCM can be seen in the loss of melt enthalpy when 
compared to the material before filament extrusion in Table 4.2. Samples taken 
from the filament for analysis were taken near the beginning and end of the fila-
ment length. 
The 50 and 60 wt% of MEPCM that was compound using a twin screw ex-
truder and extruded into filament was used to 3D print samples to quantify any 
potential PCM loss from the temperatures experienced in the printing process. The 
2.85mm diameter filament was printed using an Ultimaker S3 with printing param-
eters common for standard printing TPU. The print settings can be seen in Ta-
ble 4.3. Three samples from both weight percentages were printed and three sam-
81
Table 4.2 Summarized Thermal Transition Properties of MEPCM-TPU Pellets extruded on the 3devo. 
Sample Name Extrusion Method (# extrusions) 
Onset 
Tm 
(◦C) 
∆Hm 
(J/g) Onset 
Tc 
(◦C) 
∆Hm 
(J/g) 24D PCM Powder n/a 19.2 171.3 22.3 169.0 60wt% MEPCM Single Screw (3x) 19.0 ± 0.2 78.2 ± 9.5 22.4 ± 1.4 72.1 ± 9.0 60wt% MEPCM 3Devo Single Screw (1x) 19.4 ± 0.1 55.7 ± 1.3 22.7 ± 0.1 46.0 ± 1.1 80 wt% MEPCM Single Screw (4x) 19.1 ± 0.3 71.3 ± 8.9 22.2 ± 1.5 60.8 ± 8.2 80 wt% MEPCM 3Devo Single Screw (1x) 19.4 ± 0.1 51.8 ± 2.1 23.0 ± 0.1 38.7 ± 1.1 50 wt% MEPCM Twin Screw (1x) 19.6 ± 0.2 60.7 ± 15.8 22.8 ± 0.1 59.0 ± 15.5 50 wt% MEPCM 3Devo Single Screw (1x) 19.5 
±0.1 
36.9 ± 2.5 20.1 ± 0.2 28.1 ± 1.1 60 wt% MEPCM Twin Screw (2x) 19.4 ± 0.3 42.5 ± 3.0 22.6 ± 0.2 36.3 ± 2.2 60 wt% MEPCM 3Devo Single Screw (1x) 19.5 ± 0.1 32.8 ± 1.9 22.9 ± 0.1 22.0 ± 1.0 
ples were taken from each print to quantify the melt enthalpies after printing. The 
printed samples were found to print similarly to standard TPU and the quality of 
each sample and melt enthalpy for each weight percentage can be seen in Figure 4.8 
and Table 4.4, respectively. 
Table 4.3 Print settings for MEPCM-TPU filament 
Nozzle Temperature [◦C] 225 Bed Temperature [◦C] 60 Print Speed [mm/sec] 25 Nozzle Diameter [mm] 0.4 Layer Height [mm] 0.2 
# Layers 5 
Table 4.4 Summarized Thermal Transition Properties of MEPCM-TPU printed samples. 
Sample name Onset 
Tm 
( C) 
∆Hm 
(J/g) Onset 
Tc 
( C) 
∆Hc 
(J/g) 50 wt% MEPCM 19.4 ± 0.1 38.2 ± 0.2 20.8 ± 0.1 24.7 ± 0.2 60 wt% MEPCM 19.3 ± 0.1 35.1 ± 1.0 21.1 ± 0.2 20.5 ± 0.2 
82
https://lh3.googleusercontent.com/notebooklm/AKXwDQFVpIV4RBwEhl5SzAoxkHxTP2rgMAuIc494tQXol58c8jZWZco76G9SzHaFIxBncHn48gHeM09oO15vYV7gyQE1GLA1oSh8zhIBo2W9pBb7JwDG0J7mlR0bIyMegvKXhWt9Ypt8=w898-h585-v0
7e381ff2-3c3d-42e4-8ed3-4666d713c14b
Figure 4.8 Printed samples of MEPCM-TPU. (A-C) 50wt% MEPCM and (D-F) 60wt%MEPCM 
4.2 Characterization of MEPCM-TPU Powder and Filaments 
4.2.1 Raw Materials 
In this section, the composition and characterization of MEPCM with TPU 
powder is explored. The raw materials comprising the compound is 43D MEPCM 
from Microtek and TPU powder from STS inks. The MEPCM powder consist of 
particle sizes between 5 
µ 
and 30 
µ, 
while the TPU powder consist of particle sizes 
between 100 
µ 
and 200 
µ. 
SEM images of the individual particles can be seen in 
Figure 4.9 
4.2.2 Single Screw Extusion of MEPCM-TPU Powder 
MEPCM were compounded with a single screw exturder (3Devo 350 Preci-
sion) in weight percentages of 40wt%, 50wt%, 60wt%, and 70wt% of MEPCM in 
TPU powder. The extursion profile used can be seen in Figure 4.10. Images of 
filament surfaces can be seen in Figure 4.11. It can be seen in Figure 4.11(A-C) 
that surface of the filament is smooth at the surface, while in Figure 4.11(D) shows 
70wt% of MEPCM leads to a rough surface quality. 
83
https://lh3.googleusercontent.com/notebooklm/AKXwDQF1vtiUa_b465fTcDldw9zznmDr21qx5fiu2DyDklbPAWheVQk-G0fgR9E_G6zQLg7QYznIx7YChMV3EvknPQ-Knj_bqkdB9rxI-SKbWKYGREcdUehmUvzfp1QurdvHog8hKAKW=w964-h373-v0
4be86169-f9ab-4b2c-b2fb-bf0736faa9a2
https://lh3.googleusercontent.com/notebooklm/AKXwDQHlNonSSTTa1rp7zn3iey5ebFI9s_-1rQ_mG2i9-6FnjWRk4neB4LP9V-ngrdWhb027xSIkje3wFj4QzML31knuFW_t7VEm1ahBFCxSg3ikETBLXNgsP_DMIsgWa5_9b59YJltR=w811-h228-v0
438acd92-ebe9-4867-bb41-231b2e59072c
Figure 4.9 Micrographs of (A) MEPCM and (B) TPU powder 
Figure 4.10 Extrusion profile for extruding MEPCM and TPU powder. 
In Figure 4.12, the cross section of the 60wt% MEPCM filament can be seen. 
In the SEM image, the microcapsules can be seen packed together in the filament. 
Majoriety of the shells can be seen deformed from the contact with the other shells, 
but are mostly still intact. Compared to the micrographs of the extrusion with 
TPU pellets, it can be seen that the major contributor to the breaking of microcap-
sules can be attributed to the particle size of the polymer. If the particle size of the 
polymer is within the order of magnitude of the MEPCM particles, the MEPCM 
shell is less likely to rupture due to collison forces. 
DSC data for the MEPCM powder, powder mixtures of MEPCM and TPU, 
the filament ratios, and printed samples can be seen in Table 4.5. Samples were 
taken 5 times for each material to get an average and standard deviation. It can be 
seen that the MEPCM powder has a base latent heat of fusion of 217 J/g ± 2.89 
84
https://lh3.googleusercontent.com/notebooklm/AKXwDQFjmaURaYKlUXfZ4TEVUzLNxbR6qNCOX8TyptnFzAo-Wv--GLB-x8HnEDKmMAnP3s1Qbwgk9twf1xZHknl6WF2izvFKLxPuV4mNEklL8OirUHnI_tgffKPeP1B2uoEvfu-y84lr=w438-h460-v0
80b5e267-2f54-4914-a191-2f630816ea11
https://lh3.googleusercontent.com/notebooklm/AKXwDQHPcu-SzVjG3F5bnOx96v1a-95yIgaPsd-hMYwJSfle0BWPyLwxjW1BWKeVO00nPEuTrSItz85z3rA3W-FDXlts3ehymZIwp9Yhn2Kc0KskTpKeU31pRV0hKONlWNcxgsUrhJBAQw=w957-h370-v0
ba822c78-9895-4315-9138-1d4acd6330d1
Figure 4.11 Surface images of (A) 40wt% MEPCM, (B) 50wt% MEPCM, (C) 60wt% MEPCM, and (D) 70wt% MEPCM 
Figure 4.12 Micrographs of 60wt% MEPCM Filament 
J/g. The ratios of powder mixtures and compounded filaments are compared to 
the base latent heat of fusion of the MEPCM powder. It can be seen that the pow-
der mixtures have latent heat values very close to the measured weight percent-
85
Table 4.5 DSC characterization of MEPCM ratios of powder mixtures, filaments, and prints 
Sample name 
Tonset 
(◦C) Delta 
Hm 
(J/g) 
Theo. wt% based on Delta 
Hm 
43D MEPCM Powder 39.83 ± 0.77 217.10 ± 2.89 n/a Powder Mixtures 
40 wt% 43D MEPCM 40.39 ± 0.46 85.88 ± 2.86 39.6% 50 wt% 43D MEPCM 39.82 ± 0.29 108.14 ± 2.30 49.8% 60 wt% 43D MEPCM 39.48 ± 0.23 132.71 ± 5.00 61.1% 70 wt% 43D MEPCM 39.52 ± 0.10 151.92 ± 4.89 69.9% 
Filament 40 wt% 43D MEPCM 39.24 ± 0.11 84.91 ± 2.55 39.1% 50 wt% 43D MEPCM 38.90 ± 0.10 107.83 ± 1.69 49.6% 60 wt% 43D MEPCM 38.84 ± 1.1 131.97 ± 0.13 60.8% 70 wt% 43D MEPCM 39.82 ± 0.62 149.65 ± 2.89 68.9% 
Printed 40 wt% 43D MEPCM 39.85 ± 0.72 82.79 ± 1.41 38.1% 50 wt% 43D MEPCM 39.60 ± 0.12 105.09 ± 3.34 48.4% 60 wt% 43D MEPCM 39.21 ± 0.18 127.02 ± 1.51 58.8% 70 wt% 43D MEPCM n/a n/a n/a 
ages. This can be expected, since the powder mixtures are not heated and do not 
have significant mechanical loading that could lead to broken microcapsules. The 
compounded filaments can be seen to have a minor decrease in latent heat values 
with losses of PCM at 1% or less. This is expected since the heating and shear ef-
fects of the single screw extruder can lead to the breaking of some microcapsules. 
Once the filament is printed, the latent heat values can be seen to slightly decrease 
again across all the ratios. This is also expected, since the printing process is an-
other heated process with shear stress that can further break microcapsules. 
86
5 Numerical Modeling for PCM Melting 
In this chapter, the modeling and analysis of a shape-stabilized PCM is ex-
plored to observe the transient local heat transfer effects between a forced convec-
tion heat transfer fluid and the wall of a melting PCM. The transient local Nusselt 
is calculated using the transient wall temperature, wall heat flux, and bulk fluid 
temperature as the PCM is melting on the opposite side of the wall. These obser-
vations of transient local heat transfer can lead to a better understanding of how 
phase change processes can be better modeled, rather than relying on past heat 
transfer correlations that don’t account for the phase change process effects at the 
wall. 
5.1 Methodology 
A PCM melting setup is modeled using two different schemes and boundary 
conditions along with a validation experiment. The setup involves the melting of 
two slabs of PCM sandwiching a microchannel fluid array. One model is a sim-
plified model that incorporates a finite difference method (FDM), while the other 
model uses a commercial finite volume method (FVM). Both models were run using 
a constant power condition and a constant inlet temperature condition. The con-
stant power condition involves the maintaining of a constant temperature difference 
across the test section, while the constant inlet temperature condition involves a 
traditional inlet temperature that is held constant. The validation experiment was 
run only in the constant power condition to validate the two models. 
5.2 Finite-Volume Numerical Simulations 
The numerical solutions were conducted using ANSYS FLUENT v2021 R2. 
The pressure–velocity coupling was solved with the SIMPLE scheme, PRESTO! for 
pressure, and second-order upwind for both momentum and energy. Least squares 
cell based for gradient was used for spatial discretization. The transient formulation 
utilized first-order upwind. The residuals for the convergence criteria were set to 1 
87
× 10−6 for continuity, 1 × 10−6 for velocity, and 1 × 10−12 for energy. The under-
relaxation factors were set to 0.3 for pressure, 1 for density, 1 for body forces, 0.7 
for momentum, 0.9 for local liquid fraction, and 1 for energy. 
5.2.1 Physical Model 
An experimental setup was performed to validated the finite difference model 
and that data is used to validate the finite volume model[198]. In the experiment, 
rectangular slabs of tetradecane impregnated into a graphite matrix were placed on 
either side of a microchannel fluid array. The slabs were 45.7 cm in length, 25.4 cm 
in width, and 3.12 cm thick. The microchannel array was 45.7 cm in length, 25.4 
cm in width, and a thickness of 0.30 cm. The wall thickness of the microchannel 
array was also 0.035 cm. These PCM slabs and microchannel array were insulated 
on all sides exposed to ambient air. A schematic of the experiment can be seen in 
Figure 5.1(a). Assumptions were made to simplify the physical model. 
1. Three-dimensional effects are neglected. 
2. The effects of natural convection in the PCM is negligible. 
3. The PCM volume change is neglected. 
4. The liquid and solid phases of the PCM have identical densities. 
5. Contact resistance between the PCM and the fluid wall is not neglected. 
6. The fluid flow is hydrodynamically developed, laminar and incompressible. 
7. Microchannel fluid array is treated as a single square duct with the same wall 
thickness. 
The boundaries between the different domains is handled as a conjugate bound-
ary condition with a coupled relationship at the walls. The conjugate wall also has 
88
https://lh3.googleusercontent.com/notebooklm/AKXwDQF3wBtPNuGZjVSpFqzjUfVDdyaR66bY-ozFfjKDX87NmaFRFJVBl0OvotfSYWfXqhB6sUG03ZRKFgL1b4aH6CuB0dj3Ps31xRu9aB-s1Jdi4xrYd00aLxIQ5NM9updxPdwaLtNu1A=w924-h805-v0
a71e8a60-7d14-40aa-b55b-6c6aa607cd16
added resistance of 1.6e−3 Km2/W at the boundaries between the PCM and alu-
minum wall domains to better replicate the contact resistances that was experi-
enced during the experiment. The location and dimensions of the domains can be 
seen in Figure 5.1(b), where the representative width is 0.254 meters. 
Figure 5.1 (a) 3D schematic of PCM test section with microchannel fluid array, (b) 2D domains and dimensions for FVM 
The inlet velocity is 0.0264 m/s and the inlet temperature is 285.15 K (12 
C). No-slip and/or adiabatic conditions are applied to all boundaries except for 
the boundaries between the fluid/solid domains and between the two solid domains. 
The initial temperature of all domains were set to 273.15 K (0 ◦C). The initial pres-
sure and velocities were set to 0 Pa and 0 m/s, respectively. 
89
Material Properties 
The PCM domain was modeled after a tetradecane graphite composite[198]. 
The tetradecane is impregnated into an expanded graphite matrix and has anisotropic 
thermal conductivity. The material properties for the PCM can be seen in Table 
5.1. 
Table 5.1 PCM Material Properties 
Property Value 
kxx 
[W/mK] 18 
kyy 
[W/mK] 10 
ρs 
[kg/m 3] 836 
hsl 
[J/kg] 167978 
cpl 
[J/kgK] 1888 
cps 
[J/kgK] 1424 
Tm 
[K] 277.75 
Ton 
[K] 277.5 
Tend 
[K] 278 
Tref 
[K] 278.25 
href 
[J/kg] 387731.18 
The specific heat of the PCM was applied to the Fluent model through the 
linear discretization of the specific heat versus temperature curve, represented in 
Figure 5.2. 
The solid domain representing the wall between the fluid and PCM domain 
was modeled using standard aluminum properties. The material properties for the 
aluminum can be seen in Table 5.2. 
Table 5.2 Aluminum Material Properties 
90
https://lh3.googleusercontent.com/notebooklm/AKXwDQECS8FOJ-lI0bTf65FAa0c2BL70OCSE-34SnK-VmGjafapj8ehxQOwteTnvEbKNKMppyrLhM92ueUUluevP-6E10Az9TE8mS67R_lrHT5SzdEFy9pdBdJXE1TJYrKnIMcLr4srKHg=w814-h646-v0
9ca5c763-5990-4626-961e-803137584092
Figure 5.2 Tetradecane graphite matrix specific heat as a function of temperature 
Property Value 
cp,w 
[J/kgK] 890 
ρw 
[kg/m3] 2710 
kw 
[W/mK] 200 
The fluid domain was modeled based upon the material properties of a 20 
percent concentration of propylene glycol in water. The fluid properties used in the 
fluid governing equations were modeled as a function of temperature using a dis-
cretized piece-wise linear function (similar to the specific heat of the PCM domian) 
and can be seen in Figure 5.3. 
5.2.2 Governing Equations 
In the present study, the governing equations used to model the fluid domain 
for 2D, laminar, incompressible flow of a Newtonian fluid with no additional source 
terms. The continuity equation is, 
∇ 
· 
−→vf 
= 0 (5.1) 
91
https://lh3.googleusercontent.com/notebooklm/AKXwDQEeIpxdcoNvFsHljo5EWNgTQ6xPptc4ssIPh0atXXWcrR4Zl3mGmSMxMFRs8Kptlo8g1EgtKfcrQ5Nn6n5GQxyYXCPFI1QDQiSH7VwLNvbENk6v8gQLZ6jwZ2OW2AOM52Pt3hRO-w=w1280-h731-v0
c84cb6a3-e98b-4698-ae9a-d181939a5869
Figure 5.3 Material Properties of 20% concentration of propylene glycol in water as a function of temperature. 
where, 
−→vf 
is the 2-D velocity vector for the fluid domain. 
The momentum equations for transient flow with no gravitational or external 
forces can be seen as, 
ρ 
( 
∂−→vf ∂t 
+ 
(−→vf 
· 
∇)−→vf 
) 
= 
−∇p+ µf∇2−→vf 
(5.2) 
where, 
−→vf 
is the 2-D velocity vector, p is the static pressure, 
ρ 
is the density, 
and 
µf 
is the viscosity of the fluid. 
The energy equation is solved separately for both the fluid and solid domains. 
The energy equation for the fluid domain is, 
ρfcpf DTf 
Dt 
= 
kf∇2Tf 
(5.3) 
where, 
ρf 
, 
cpf 
, and 
kf 
are the density, specific heat, and thermal conductivity 
of the fluid domain, respectively. 
Tf 
is the temperature in the fluid domain. 
The energy equation for the solid domains is, 
92
ρs ∂h 
∂t 
= 
∇ 
· 
(keff∇Ts) 
(5.4) 
where, 
ρs 
is the density of the solid, 
∂h 
∂t 
is the transient change in enthalpy of 
the solid, and 
∇ 
· 
(keff∇T 
) represent the conduction in the solid domain. In the 
conduction term, 
keff 
is the anisotropic thermal conductivity that is defined as, 
keff 
= 
kij 
= 
kxx kxy 
kyx kyy 
 (5.5) 
where, 
kxx 
and 
kyy 
are the parallel 
(kpara) 
and perpendicular 
(kperp) 
thermal 
conductivity, respectively. In Fluent, the enthalpy is defined as, 
h 
= 
∫ T 
Tref 
cps dT 
+ 
href 
(5.6) 
where, 
href 
is the reference enthalpy at a reference temperature 
Tref 
, and 
cp,s 
is the specific heat of the solid. The specific heat of the PCM is defined in Fluent 
using a piecewise-linear function with respect to temperature. 
cp,s(T 
) = 
cpn 
+ 
cpn+1 
− 
cpn Tn+1 
− 
Tn 
(T 
− 
Tn) 
(5.7) 
The specific heat for the aluminum solid domain uses a constant specific heat 
and isotropic thermal conductivity, while the PCM solid domain uses the piece-wise 
linear specific heat and anisotropic thermal conductivity. 
5.2.3 Mesh and Time-Step Size 
The mesh was created using Pointwise v18.0 with 2D structured cells for all 
the domains. The mesh had a total cell count of 1,971,919 cells with xy node di-
mensions of 4572x350 (1,595,279 cell count) for the PCM domain, 4562x30 (132,559 
cell count) for the fluid domain, 4572x10 (41,139 cell count) for the aluminum wall 
domain, and 3500x30 (101,471 cell count) for both the upstream and downstream 
93
fluid domains. Additional mesh sizes with a total cell count of 5,000,000 and 10,000,000 
were evaluated and the outlet temperature with respect to time for all three cases 
were less than 1% difference. The total cell count of 1,971,919 cell was used for 
the final solution. The timestep was set to 0.1 seconds and a max iterations per 
timestep of 25. Additional timestep sizes were evaluated at 0.05 and 0.01 seconds. 
The outlet temperature with respect to time for all three timesteps were less than 
1% difference and the final timestep size of 0.1 seconds was used for the final solu-
tion. 
5.3 Finite Difference Model 
The finite difference model used is a simplified melting and solidification model 
that solves the transient temperature and enthalpy response of a 2D PCM domain 
along with a 1D fluid domain[198]. The 2D PCM domain is discretized with a nodal 
map of 40 equidistant nodes in the x direction and 10 equidistant nodes in the y di-
rection. The 1D fluid domain is discretized with nodes consisting of 40 equidistant 
nodes in the x direction. The amount of nodes for both the PCM domain and the 
fluid domain can be increased or decreased depending on the resolution required to 
be mesh independent and the amount of nodes in the PCM domain and the fluid 
domain were proven to be adequate based on validation to the experimental setup. 
The change in enthalpy of the PCM domain nodes is calculated using Equa-
tion 1. This equation calculates the change in enthalpy for each timestep ( 
dhi,j 
dt 
) 
using a central difference scheme at each node based upon the temperature of the 
surrounding nodes. 
dhi,j 
dt 
= 
W 
mpcm 
[ 
kpara∆y 
∆x (Ti,j−1 
+ 
Ti,j+1 
− 
2Ti,j) 
+ 
kperp∆x 
∆y (Ti−1,j 
+ 
Ti+1,j 
− 
2Ti,j) 
] (5.8) 
The total power 
(Q̇i,1) 
into or out of each of the PCM nodes at the wall ad-
94
jacent to the the fluid is calculated using Equation 2. This equation uses the tem-
perature of the fluid node and the PCM node that share the same x position, along 
with a calculated thermal resistance 
(Rf−PCM) 
that can be seen in Equation 3. 
Q̇i,1 
= 
Tf,i 
− 
Tw,i 
Rf−PCM 
(5.9) 
Rf−PCM 
= 
∆y 
2kperpW∆x 
+ 
Rcontact 
W∆x 
+ 
twall 
kwW∆x 
+ 
1 
htcfW∆x 
(5.10) 
The first term in the resistance equation (Equation 3) is the conduction through 
the PCM. The second term is the contact resistance between the PCM and the 
wall. The third term is the conduction resistance through the wall material that 
is existent in the experiment to separate the PCM and fluid. The fourth term is the 
convective resistance from the fluid to the wall. Any other resistances that are not 
shown in the equation are considered negligible. 
The temperature at each fluid node for each timestep is calculated using Equa-
tion 4. This equation calculates the temperature change at each fluid node based 
upon the temperature of the fluid before and after the node, along with power 
(Q̇i) 
into or out of the PCM. 
dTf,i 
dt 
= 
1 
c̄pf ṁf 
[ 
ṁf c̄pf (Tf,in 
− 
Tf,i)− 2Q̇i 
+ 
k̄f (HfW 
) 
Tf,i+1 
− 
Tf,i 
∆x 
] (5.11) 
5.3.1 Heat Transfer Coefficient 
The local heat transfer coefficient that is used in the resistance equation (Equa-
tion 3) is determined through the use of Nusselt number correlations. 
htcf 
= 
N̄u kf Dh 
(5.12) 
95
where 
htcf 
is the local heat transfer coefficient, 
kf 
is the thermal conductiv-
ity of the fluid, 
Dh 
is the hydraulic diameter of the fluid channel, and 
¯Nus 
is the 
average Nusselt number. 
The average Nusselt number is determined by taking the average between the 
Nusselt number for a constant wall temperature 
(NusT 
) and constant wall heat flux 
(NusH) 
condition, as seen in Equation 6. 
N̄u 
= 
NuT +NuH 
2 (5.13) 
The Nusselt number for a constant wall temperature and constant wall heat 
flux in a square duct for all four walls is defined using the approximation equation 
in the Handbook of single-phase convective heat transfer[373] can be seen in Equa-
tion 14 and 15, 
NuT 
= 
7.541 
[ 1− 
2.610 
( 
Hf 
W 
) + 
4.970 
( 
Hf 
W 
)2 
− 
5.119 
( 
Hf 
W 
)3 
+ 
2.702 
( 
Hf 
W 
)4 
− 
0.548 
( 
Hf 
W 
)5 ] 
(5.14) 
NuH 
= 
8.235 
[ 1− 
2.042 
( 
Hf 
W 
) + 
3.085 
( 
Hf 
W 
)2 
− 
2.477 
( 
Hf 
W 
)3 
+ 
1.058 
( 
Hf 
W 
)4 
− 
0.186 
( 
Hf 
W 
)5 ] 
(5.15) 
where 
Hf 
is the height of the fluid channel and 
W 
is the width of the fluid 
channel. 
5.4 Results 
5.4.1 Validation with imposed constant power 
The comparison of outlet temperatures between the experimental setup, the 
finite difference model and the finite volume model can be seen in Figure 5.4. These 
outlet temperatures are from the constant power cases to better compare with the 
experiment that was under constant power. The finite volume model is 6.45% dif-
ference of the finite difference model and 11.97% difference from the experimen-
96
https://lh3.googleusercontent.com/notebooklm/AKXwDQGjkrJlWAvHvhKOIvpJ31FDKTnKXbaG71YJayrzaKDn-XYBYeApMPFO3gQwzU7JHlg1jxZfftr6ikl68MUPzpvQNCIgEufYf2vGf2CvnaRw8mgqnA-s6OkYQpYEZPK16MvaOJrP=w1280-h853-v0
5a1a3c26-5083-477b-bc79-9f5f5ff963e4
tal data. This will serve as the validation for the finite volume model in both the 
constant temperature difference case and the constant inlet temperature case. Dif-
ferences between the experiment and both numerical models outlet temperatures 
can be attributed to the assumptions made to the numerical models to simplify the 
computational intensity. 
Figure 5.4 Outlet temperature for experiment, finite difference, and finite volume with the constant power setup 
5.4.2 Constant Inlet Temperature Condition 
It can be seen in Figures 5.5-5.7 contour plots early in the melt (Figure 5.5), 
middle of the melt (Figure 5.6), and near the end of the melt (Figure 5.7). In these 
figures a comparison can be seen between the finite difference model and the fi-
nite volume model, for both the contour plots of the melt front and local temper-
atures/wall heat flux for the fluid side. The wall temperatures, bulk temperatures, 
and wall heat fluxes show very similar compliance between both models early and 
in the middle of the melt. Near the end of the melt shows the temperatures and 
wall heat fluxes start to separate as the melt front start to differ between the two 
models. It can also be seen that early and near the middle of the melt, the fluent 
97
https://lh3.googleusercontent.com/notebooklm/AKXwDQESSW0f-qt2RWLj__hfk3oGreU5DciRbnRmDtLG6OAmu913ISR8HPl0DlAcfQph_ZvOLhn_jBldGRN8kM8ye4ZeGVNBnPI8x4gxqHEy_5bPjxQmG1lDYdcidxRalOKDILcjyId4=w1280-h958-v0
4d99e14c-f6b9-477e-b378-e9edde6345ab
model is melting faster closer to X/L=0, while the finite difference model is melt-
ing faster closer to X/L=1. This becomes more obvious near the end of the melt, 
when the amount of solid PCM is only near X/L=1. This causes the finite differ-
ence model to start melting faster than the finite volume model near the end of the 
melt. 
Figure 5.5 Comparison of Matlab and Fluent model with contour plots of melt front and local wall and fluid data at 10 minutes. 
The local Nusselt numbers throughout various timesteps for the entire melt 
can be seen in Figure 5.8. In this figure you can see the local Nusselt number early 
in the melt that gradually increases in value towards the middle of the melt, when 
the melt front is moving away from the fluid wall. Once the melt front reaches the 
far wall around 33 mins, the start of the inactive zone begins. The inactive zone 
can be defined as the region of the PCM that is fully liquid for all y locations in a 
given region of x. This starts at X/L=0, when the melt front reaches Y/L=1 and 
98
https://lh3.googleusercontent.com/notebooklm/AKXwDQHAprfwcllao8jQEIyV5LOKuh8pLD9xerxWR2Rimk8J5yQ5EuPf0oAiJiFYgFd3dwNHKTr3PYRunVgO4ltDI41JH75uzE5amIVBrqrIObRjmAm-OKEMdejQmb5IB0Oxx4M5uaIcNg=w1280-h958-v0
020b0508-dad1-4145-9abb-40704daec502
Figure 5.6 Comparison of Matlab and Fluent model with contour plots of melt front and local wall and fluid data at 35 minutes. 
begins to grow downstream until the PCM is fully melted. A demonstrative fig-
ure can be seen in Figure 5.9. Within the inactive zone, the bulk fluid tempera-
ture, wall temperature and also the liquid PCM begin to reach isothermal temper-
atures equal to the inlet temperature. Also, at the inactive zone, the wall heat flux 
decreases to a near zero heat flux along with the wall and bulk temperatures be-
coming equal. As the inactive zone grows and the amount of solid PCM decreases, 
these effects can be more clearly seen in Figure 5.7. 
After the inactive zone begins, a sudden increase in the local Nusselt number 
can be seen and a new maximum Nusselt number can be seen around a value of 10. 
In Figure 5.10, it can be seen that the sudden change from a high to low local Nus-
selt number occurs near the boundary of the inactive zone and the melt front. As 
the melt front moves and the inactive zone grows, this sudden change in local Nus-
99
https://lh3.googleusercontent.com/notebooklm/AKXwDQHnjrQHLRMWyXkt7iVxzjYGS6Fvx9ubBgtptupSVFLwfA-gip3ZpFOiW1sSen7o_H7-mCNob0FwqFNUeEAYw-sVBPvPPZnCbSunGHckFCKxYVUgavIv0NIZdE8ewWdNz8IF8uqrMQ=w1280-h958-v0
3d34bd7b-e267-4701-b240-bfc39759fabe
Figure 5.7 Comparison of Matlab and Fluent model with contour plots of melt front and local wall and fluid data at 60 minutes. 
selt number will move accordingly with that boundary. Despite the sudden increase 
in local Nusselt number left of the melt front, the amount of heat transfer occurring 
at the wall is rapidly decreasing based upon the bulk temperature, wall tempera-
ture, and wall heat flux in that area. Therefore, the higher local Nusselt number 
left of the melt front is more likely a mathematical error with the difference in the 
bulk and wall temperatures and the wall heat flux approaching zero in that area. 
It can be seen in Figure 5.11, the local Nusselt numbers for the various timesteps 
in comparison to the corresponding Nusselt number correlations given in Equations 
14 and 15. In Figure 5.11(a), the timesteps associated with the melting of PCM 
before the formation on an inactive zone. These timesteps show an increase of the 
local Nusselt number as time progresses, which is associated with the movement of 
the melt front away from the wall the heat transfer fluid. The local Nusselt num-
100
https://lh3.googleusercontent.com/notebooklm/AKXwDQHATmYFJnvgBFYM_Cw-GzLCqmsB-ftYFvpIolsrGDEu_puhUYfM04rmPoY1nft-lXjE2lCzA-lZK0nMlZtpNV8KN9SVLYH5gKcuOHB0Iiyyz_2KKWfkgxLH_e0pyidcIZX6pliC=w1280-h853-v0
7b52acdc-1a23-48c1-b9fb-dcce25b4c4f3
https://lh3.googleusercontent.com/notebooklm/AKXwDQFx_AjEe03lY0xn0O4f3Jlbq8--AEgsKQRJvJxx_wLcnEBVMCM682AfneWMp6ZaR274KTVirE5-ncsIfoFB5fxNlRkEZ-glnIpXV6ZumH8iCQcNkg-qH2EPyjAT-eNd1zaadFU-=w955-h346-v0
d47529d2-1ce2-4cc5-b986-75dcb0f22259
Figure 5.8 All local nusselt numbers for constant inlet temperature case in fluent model. 
Figure 5.9 Illustration of inactive zone for melting of PCM. 
bers within these timesteps show the same shape as a local Nusselt number with a 
developing and fully developed region, first starting near the constant wall temper-
ature correlation and progressing up toward the constant wall heat flux correlation. 
101
https://lh3.googleusercontent.com/notebooklm/AKXwDQFPSPNXs2z1jPUGdlg6Rt67GPORqGDmLk887mYCGBQA19rPx9q3QX9GVjQ30LG2lvR6LWJdhCMyNUd6n83R9cwKawtNzEUNIjSAbFwEicBwva7zYa7hoFVLfIah8zLO1f7C-BON=w897-h583-v0
f3aacdc8-69a3-432e-a6b7-b35165d8b4da
Figure 5.10 Local Nusselt number, wall temperature, bulk temperature, and wall heat flux from Fluent model with corresponding contour plot of PCM domain at 
time = 55 min. 
As the timesteps increase, the local Nusselt number appears to be converging to 
one location. Once the inactive zone begins (after time = 33min), in Figure 5.11(b) 
the local Nusselt number can be seen to change shape drastically. This change can 
be directly attributed to the formation of an inactive zone and the final stages of 
the PCM melt front. 
To the right of the inactive zone where solid PCM is still melting, the local 
Nusselt number is similar to the trend for a constant wall heat flux condition as if 
the start of a thermal boundary layer begins near the boundary of the inactive zone 
and the melt front. A demonstration of this effect can be seen illustrated in Figure 
5.12. One explanation for this complex local Nusselt number is a potential super-
position of two different thermal boundary layers. One thermal boundary layer that 
has a traditional starting position at the inlet of the fluid section and another ther-
mal boundary layer that is progressively moving with the growth of inactive zone. 
102
https://lh3.googleusercontent.com/notebooklm/AKXwDQGQnIYRe1FzWcG9_y9TQHrByoD8mDNAJI_cM4BZaDuWox5IemsUwZidJVhP_cEv0vyPpp_h7KVmqq37Z7jiJ3zmUebRXkk-e2arUHig3kb2CStj7LT0q6IQPJvtasTb909YnMHKLw=w1280-h472-v0
8ee3e51d-c329-40cc-afd3-a1ce90038e92
Figure 5.11 Local Nusselt number for various timesteps with contant wall temperature and constant wall heat flux correlations, (a) timesteps at 33min and below (pre-inactive zone), (b) timesteps at 35min and above (post-inactive zone) 
The first thermal boundary layer at the entrance to the fluid region is more sub-
tle as the temperature gradients in that region are progressively reaching a more 
isothermal state. The second thermal boundary layer that is moving, has more sig-
nificant temperature gradients that would be seen in a stationary boundary layer. 
The movement and transient change in temperature gradients can be directly at-
tributed to the influence of the melt front in that region that is actively moving as 
more PCM melts. 
103
https://lh3.googleusercontent.com/notebooklm/AKXwDQHOUgbJMjs3pHG5tedj_nWpMv6Mx5I1zvFv5mE5om9rFGYYppdjNucmLkoFrHpRMib-UsK4bCmaE62BUzRg34PSdp5TfV7RXRJe9Pbb6DTUrgwCxZRiAlLVwWnKx8k-UzSMIkfFrw=w786-h703-v0
cab145a7-ee84-4b81-b4b1-fa709b9d52cd
Figure 5.12 (a) Demonstrative figure for thermal boundary layer development with melt front spanning full length of fluid channel, (b) Demonstrative figure for 
thermal boundary layer development with simultaneous movement of melt front and inactive zone 
104
6 Conclusions 
6.1 HDPE/PCM Composite 
A shape-stabilized PCM/HDPE functional composite has been printed using 
FFF for the first time. A composite comprising 40% PCM42 by mass was mixed 
with HDPE and extruded to make filament that is capable of thermal energy stor-
age. It was determined through DSC testing that the thermal storage capability 
of the resultant filament effectively behaved as if there was 31.8% of the PCM42 
in the composite. Furthermore, the filament was printed into sample specimens for 
further thermal testing. Utilizing SEM, the microstructures of the PCM42/HDPE 
composite material were investigated after the first extrusion(filament making) and 
after the second extrusion (printing), and it was found that the material retained 
the same form after multiple extrusions. A heated HDPE build plate and heated 
enclosure were used to improve the print process of HDPE and the composite. Al-
though there are many known difficulties in printing pure HDPE, the added PCM 
helped make the process easier. Phase-change temperature, effective latent heat of 
fusion, and thermal conductivity were measured and reported. 
The results are promising, especially since the ability to directly print PCM, 
”encapsulated” in a polymer, can potentially revolutionize the manufacturing of 
thermal energy storage and management systems. Further work needs to be done 
to evaluate thermal cycling for long-term stability and leakage issues. In general, it 
has been shown that HDPE and PCM have the potential for long-term compatibil-
ity, and leakage issues can hopefully be mitigated with epoxy coatings. In addition, 
mechanical property testing including, but not limited to, tensile and flexure testing 
of specimens extracted from 3D printed samples of different raster orientations will 
be conducted in future work. 
To show that an organic-based PCM shape stabilized with HDPE has very 
little affinity for moisture (i.e., they are extremely non-hygroscopic materials). Dif-
105
ferent compositions of the samples have been prepared to determine if the composi-
tion can impact the steady-state and transient moisture adsorption and desorption 
behaviour. While some distinction between the various compositions and operat-
ing temperatures was observed, the moisture adsorption and desorption diffusivities 
indicate that the materials will not be impacted by the presence of moisture. This 
is a highly promising outcome since it helps justify the use of these materials in 
various thermal energy storage applications where the presence of moisture is antic-
ipated. 
6.2 MEPCM/TPU Composite 
The results of the composition of a microencapsulated PCM with a powder 
TPU polymer shows outstanding retention of PCM by relying on the microencap-
sulation of the PCM for sealing and using the polymer as a binding matrix for 3D 
printing. Successful compounding of MEPCM into a polymer relies on the poly-
mer particle size be smaller than the typical polymer pellet size of around 2mm. 
Large particle size of polymer leads to the destruction of microcapsules during the 
extrusion process, while using powder polymer leads to successful compounding of 
MEPCM and polymer. Up to 60wt.% of MEPCM was successfully compounded in 
TPU with excellent filament quality and less than 1% loss of PCM after filament 
extrusion. After 3D printing, the total loss of PCM was less than 2%. Characteriza-
tion of filaments and prints were performed using DSC for thermal storage capacity 
and at 60wt.% of MEPCM, the thermal storage capacity was measured to be about 
130 J/g. Further characterization in the future includes thermal conductivity and 
mechanical strength of compounded materials and prints. 
6.3 Numerical Modeling 
A transient finite volume model was used to explore the coupled heat transfer 
effects at the wall boundary between a shape-stabilized PCM and a laminar forced 
convection heat transfer fluid. It was found that the local Nusselt number is di-
106
rectly influenced by the location of the melt front within the PCM. Early in the 
melting of the PCM, the local Nusselt number is close to the local Nusselt num-
ber for the same fluid geometry with a constant wall temperature condition. As the 
melt front progresses away from the wall of the heat transfer fluid, the local Nusselt 
number transitions from a constant wall temperature condition towards the local 
Nusselt number for a constant wall heat flux condition. Later in the melt, the lo-
cal Nusselt number greatly changes when an inactive zone starts to develop. This 
causes the local heat transfer within the inactive zone at the wall to transition to 
an isothermal condition and causes a movement of the thermal development length 
to follow the remaining solid PCM that is melting. This discovery can lead to a 
better understanding of the heat transfer effects that occur at the heat transfer sur-
face during the melting of PCM. 
107
REFERENCES 
[1] Garimella, S., Lockyear, K., Pharis, D., El Chawa, O., Hughes, M. T., and 
Kini, G., “Realistic pathways to decarbonization of building energy sys-
tems,” Joule, Vol. 6, No. 5, 2022, pp. 956–971. https://doi.org/10.1016/j. 
joule.2022.04.003, URL https://www.sciencedirect.com/science/article/pii/ 
S2542435122001416. 
[2] Henry, A., Prasher, R., and Majumdar, A., “Five thermal energy grand chal-
lenges for decarbonization,” Nature Energy, Vol. 5, No. 9, 2020, pp. 635–637. 
https://doi.org/10.1038/s41560-020-0675-9, URL https://www.nature.com/ 
articles/s41560-020-0675-9, number: 9 Publisher: Nature Publishing Group. 
[3] Odukomaiya, A., Woods, J., James, N., Kaur, S., Gluesenkamp, K. R., Ku-
mar, N., Mumme, S., Jackson, R., and Prasher, R., “Addressing energy stor-
age needs at lower cost via on-site thermal energy storage in buildings,” 
Energy & Environmental Science, Vol. 14, No. 10, 2021, pp. 5315–5329. 
https://doi.org/10.1039/D1EE01992A, URL https://pubs.rsc.org/en/content/ 
articlelanding/2021/ee/d1ee01992a, publisher: The Royal Society of Chem-
istry. 
[4] Akhmetov, B., Georgiev, A., Kaltayev, A., Dzhomartov, A., Popov, R., 
and Tungatarova, M., “Thermal energy storage systems - Review,” Bul-
garian Chemical Communications, Vol. 48, 2016, pp. 31–40. URL https: 
//www.scopus.com/inward/record.uri?eid=2-s2.0-85063556109&partnerID= 
40&md5=52ca41805263dc0b3d6bb09605afc024. 
[5] Al-Abidi, A., Bin Mat, S., Sopian, K., Sulaiman, M., Lim, C., and Th, A., 
“Review of thermal energy storage for air conditioning systems,” Renew-
able and Sustainable Energy Reviews, Vol. 16, No. 8, 2012, pp. 5802–5819. 
https://doi.org/10.1016/j.rser.2012.05.030, URL https://www.scopus.com/ 
108
inward/record.uri?eid=2-s2.0-84864521197&doi=10.1016%2fj.rser.2012.05. 
030&partnerID=40&md5=dedefc015b1e302ec9466e44b4708451. 
[6] Alkilani, M., Sopian, K., Alghoul, M., Sohif, M., and Ruslan, M., “Review 
of solar air collectors with thermal storage units,” Renewable and Sustain-
able Energy Reviews, Vol. 15, No. 3, 2011, pp. 1476–1490. https://doi.org/ 
10.1016/j.rser.2010.10.019, URL https://www.scopus.com/inward/record.uri? 
eid=2-s2.0-78651078966&doi=10.1016%2fj.rser.2010.10.019&partnerID=40& 
md5=dd8bfec2773e9513b0084f453bd8efaf. 
[7] Ben Romdhane, S., Amamou, A., Ben Khalifa, R., Säıd, N., Younsi, Z., and 
Jemni, A., “A review on thermal energy storage using phase change materials 
in passive building applications,” Journal of Building Engineering, Vol. 32, 
2020. https://doi.org/10.1016/j.jobe.2020.101563, URL https://www.scopus. 
com/inward/record.uri?eid=2-s2.0-85091553858&doi=10.1016%2fj.jobe.2020. 
101563&partnerID=40&md5=c6ff89b408fac37603908afb5436f5cc. 
[8] Koçak, B., Fernandez, A. I., and Paksoy, H., “Review on sensible ther-
mal energy storage for industrial solar applications and sustainability as-
pects,” Solar Energy, Vol. 209, 2020, pp. 135–169. https://doi.org/10.1016/ 
j.solener.2020.08.081, URL https://www.sciencedirect.com/science/article/ 
pii/S0038092X20309208. 
[9] Pielichowska, K., and Pielichowski, K., “Phase change materials for ther-
mal energy storage,” Progress in Materials Science, Vol. 65, 2014, pp. 67– 
123. https://doi.org/10.1016/j.pmatsci.2014.03.005, URL https://www. 
sciencedirect.com/science/article/pii/S0079642514000358. 
[10] Fallahi, A., Guldentops, G., Tao, M., Granados-Focil, S., and Van Des-
sel, S., “Review on solid-solid phase change materials for thermal energy 
109
storage: Molecular structure and thermal properties,” Applied Thermal 
Engineering, Vol. 127, 2017, pp. 1427–1441. https://doi.org/10.1016/j. 
applthermaleng.2017.08.161, URL https://www.sciencedirect.com/science/ 
article/pii/S1359431117329939. 
[11] Carrillo, A. J., González-Aguilar, J., Romero, M., and Coronado, J. M., “So-
lar Energy on Demand: A Review on High Temperature Thermochemical 
Heat Storage Systems and Materials,” Chemical Reviews, Vol. 119, No. 7, 
2019, pp. 4777–4816. https://doi.org/10.1021/acs.chemrev.8b00315, URL 
https://doi.org/10.1021/acs.chemrev.8b00315, publisher: American Chemical 
Society. 
[12] Scapino, L., Zondag, H. A., Van Bael, J., Diriken, J., and Rindt, C. C. M., 
“Sorption heat storage for long-term low-temperature applications: A review 
on the advancements at material and prototype scale,” Applied Energy, Vol. 
190, 2017, pp. 920–948. https://doi.org/10.1016/j.apenergy.2016.12.148, URL 
https://www.sciencedirect.com/science/article/pii/S0306261916319316. 
[13] Solé, A., Martorell, I., and Cabeza, L. F., “State of the art on gas–solid ther-
mochemical energy storage systems and reactors for building applications,” 
Renewable and Sustainable Energy Reviews, Vol. 47, 2015, pp. 386–398. 
https://doi.org/10.1016/j.rser.2015.03.077, URL https://www.sciencedirect. 
com/science/article/pii/S1364032115002300. 
[14] Yang, T., King, W. P., and Miljkovic, N., “Phase change material-based ther-
mal energy storage,” Cell Reports Physical Science, Vol. 2, No. 8, 2021, p. 
100540. https://doi.org/10.1016/j.xcrp.2021.100540, URL https://www. 
sciencedirect.com/science/article/pii/S2666386421002514. 
[15] Hirano, S., “Thermal Energy Storage and Transport,” Handbook of Climate 
110
Change Mitigation, edited by W.-Y. Chen, J. Seiner, T. Suzuki, and M. Lack-
ner, Springer US, New York, NY, 2012, pp. 669–700. https://doi.org/10.1007/ 
978-1-4419-7991-9 20, URL https://doi.org/10.1007/978-1-4419-7991-9 20. 
[16] Leffler, A. J., and Weinstein, D. I., “CONSIDERATIONS IN THE USE 
OF SOLID-SOLID PHASE TRANSITIONS FOR THERMAL ENERGY 
STORAGE,” Sun: Mankind’s Future Source of Energy, edited by F. de Win-
ter and M. Cox, Pergamon, 1978, pp. 507–510. https://doi.org/10.1016/ 
B978-1-4832-8407-1.50099-4, URL https://www.sciencedirect.com/science/ 
article/pii/B9781483284071500994. 
[17] Fukai, J., Hamada, Y., Morozumi, Y., and Miyatake, O., “Effect of carbon-
fiber brushes on conductive heat transfer in phase change materials,” In-
ternational Journal of Heat and Mass Transfer, Vol. 45, No. 24, 2002, pp. 
4781–4792. https://doi.org/10.1016/S0017-9310(02)00179-5, URL https: 
//www.sciencedirect.com/science/article/pii/S0017931002001795. 
[18] Mhike, W., Focke, W. W., Mofokeng, J. P., and Luyt, A. S., “Thermally 
conductive phase-change materials for energy storage based on low-density 
polyethylene, soft Fischer–Tropsch wax and graphite,” Thermochimica Acta, 
Vol. 527, 2012, pp. 75–82. https://doi.org/10.1016/j.tca.2011.10.008, URL 
https://www.sciencedirect.com/science/article/pii/S0040603111005077. 
[19] Yang, X., Yang, X., Ding, J., Shao, Y., Qin, F. G. F., and Jiang, R., “Cri-
teria for performance improvement of a molten salt thermocline storage sys-
tem,” Applied Thermal Engineering, Vol. 48, 2012, pp. 24–31. https://doi. 
org/10.1016/j.applthermaleng.2012.04.046, URL https://www.sciencedirect. 
com/science/article/pii/S135943111200289X. 
[20] Sarier, N., and Onder, E., “Organic phase change materials and their textile 
111
applications: An overview,” Thermochimica Acta, Vol. 540, 2012, pp. 7–60. 
https://doi.org/10.1016/j.tca.2012.04.013, URL https://www.sciencedirect. 
com/science/article/pii/S0040603112001773. 
[21] Tomassetti, S., Aquilanti, A., Muciaccia, P. F., Coccia, G., Mankel, C., Koen-
ders, E. A. B., and Di Nicola, G., “A review on thermophysical properties 
and thermal stability of sugar alcohols as phase change materials,” Jour-
nal of Energy Storage, Vol. 55, 2022, p. 105456. https://doi.org/10.1016/ 
j.est.2022.105456, URL https://www.sciencedirect.com/science/article/pii/ 
S2352152X22014487. 
[22] Rozanna, D., Chuah, T. G., Salmiah, A., Choong, T. S. Y., and Sa’ari, 
M., “Fatty Acids as Phase Change Materials (PCMs) for Thermal En-
ergy Storage: A Review,” International Journal of Green Energy, Vol. 1, 
No. 4, 2005, pp. 495–513. https://doi.org/10.1081/GE-200038722, URL 
https://doi.org/10.1081/GE-200038722, publisher: Taylor & Francis eprint: 
https://doi.org/10.1081/GE-200038722. 
[23] Li, Q., Li, C., Du, Z., Jiang, F., and Ding, Y., “A review of performance in-
vestigation and enhancement of shell and tube thermal energy storage device 
containing molten salt based phase change materials for medium and high 
temperature applications,” Applied Energy, Vol. 255, 2019, p. 113806. https: 
//doi.org/10.1016/j.apenergy.2019.113806, URL https://www.sciencedirect. 
com/science/article/pii/S030626191931493X. 
[24] Xie, N., Huang, Z., Luo, Z., Gao, X., Fang, Y., and Zhang, Z., “Inorganic Salt 
Hydrate for Thermal Energy Storage,” Applied Sciences, Vol. 7, No. 12, 2017, 
p. 1317. https://doi.org/10.3390/app7121317, URL http://www.mdpi.com/ 
2076-3417/7/12/1317. 
112
[25] Shamberger, P. J., and Bruno, N. M., “Review of metallic phase change ma-
terials for high heat flux transient thermal management applications,” Ap-
plied Energy, Vol. 258, 2020, p. 113955. https://doi.org/10.1016/j.apenergy. 
2019.113955, URL https://www.sciencedirect.com/science/article/pii/ 
S0306261919316423. 
[26] Singh, P., Sharma, R. K., Ansu, A. K., Goyal, R., Sarı, A., and Tyagi, 
V. V., “A comprehensive review on development of eutectic organic phase 
change materials and their composites for low and medium range thermal 
energy storage applications,” Solar Energy Materials and Solar Cells, Vol. 
223, 2021, p. 110955. https://doi.org/10.1016/j.solmat.2020.110955, URL 
https://www.sciencedirect.com/science/article/pii/S0927024820305493. 
[27] Wieckowski, M., and Królikowski, M., “Designing and Characterization of 
Low-Temperature Eutectic Phase Change Materials Based on Alkanes,” Jour-
nal of Chemical & Engineering Data, Vol. 67, No. 3, 2022, pp. 727–738. 
https://doi.org/10.1021/acs.jced.1c00783, URL https://doi.org/10.1021/acs. 
jced.1c00783, publisher: American Chemical Society. 
[28] Safari, A., Saidur, R., Sulaiman, F. A., Xu, Y., and Dong, J., “A review on 
supercooling of Phase Change Materials in thermal energy storage systems,” 
Renewable and Sustainable Energy Reviews, Vol. 70, 2017, pp. 905–919. https: 
//doi.org/10.1016/j.rser.2016.11.272, URL https://www.sciencedirect.com/ 
science/article/pii/S136403211631053X. 
[29] Mohamed, S. A., Al-Sulaiman, F. A., Ibrahim, N. I., Zahir, M. H., Al-Ahmed, 
A., Saidur, R., Yılbaş, B. S., and Sahin, A. Z., “A review on current status 
and challenges of inorganic phase change materials for thermal energy stor-
age systems,” Renewable and Sustainable Energy Reviews, Vol. 70, 2017, 
113
pp. 1072–1089. https://doi.org/10.1016/j.rser.2016.12.012, URL https: 
//www.sciencedirect.com/science/article/pii/S1364032116310632. 
[30] He, B., Martin, V., and Setterwall, F., “Phase transition temperature ranges 
and storage density of paraffin wax phase change materials,” Energy, Vol. 29, 
No. 11, 2004, pp. 1785–1804. https://doi.org/10.1016/j.energy.2004.03.002, 
URL https://www.sciencedirect.com/science/article/pii/S0360544204000775. 
[31] He, B., and Setterwall, F., “Technical grade paraffin waxes as phase change 
materials for cool thermal storage and cool storage systems capital cost es-
timation,” Energy Conversion and Management, Vol. 43, No. 13, 2002, pp. 
1709–1723. https://doi.org/10.1016/S0196-8904(01)00005-X, URL https: 
//www.sciencedirect.com/science/article/pii/S019689040100005X. 
[32] HIMRAN, S., SUWONO, A., and MANSOORI, G. A., “Characteriza-
tion of Alkanes and Paraffin Waxes for Application as Phase Change En-
ergy Storage Medium,” Energy Sources, Vol. 16, No. 1, 1994, pp. 117– 
128. https://doi.org/10.1080/00908319408909065, URL https://doi. 
org/10.1080/00908319408909065, publisher: Taylor & Francis eprint: 
https://doi.org/10.1080/00908319408909065. 
[33] Fang, G., Li, H., Yang, F., Liu, X., and Wu, S., “Preparation and charac-
terization of nano-encapsulated n-tetradecane as phase change material for 
thermal energy storage,” Chemical Engineering Journal, Vol. 153, No. 1, 
2009, pp. 217–221. https://doi.org/10.1016/j.cej.2009.06.019, URL https: 
//www.sciencedirect.com/science/article/pii/S1385894709004525. 
[34] Kalaiselvam, S., Veerappan, M., Arul Aaron, A., and Iniyan, S., “Experimen-
tal and analytical investigation of solidification and melting characteristics 
of PCMs inside cylindrical encapsulation,” International Journal of Ther-
114
mal Sciences, Vol. 47, No. 7, 2008, pp. 858–874. https://doi.org/10.1016/j. 
ijthermalsci.2007.07.003, URL https://www.sciencedirect.com/science/article/ 
pii/S1290072907001688. 
[35] Vélez, C., Khayet, M., and Ortiz de Zárate, J. M., “Temperature-dependent 
thermal properties of solid/liquid phase change even-numbered n-alkanes: n-
Hexadecane, n-octadecane and n-eicosane,” Applied Energy, Vol. 143, 2015, 
pp. 383–394. https://doi.org/10.1016/j.apenergy.2015.01.054, URL https: 
//www.sciencedirect.com/science/article/pii/S0306261915000707. 
[36] Sarı, A., Alkan, C., and Karaipekli, A., “Preparation, characterization 
and thermal properties of PMMA/n-heptadecane microcapsules as novel 
solid–liquid microPCM for thermal energy storage,” Applied Energy, Vol. 87, 
No. 5, 2010, pp. 1529–1534. https://doi.org/10.1016/j.apenergy.2009.10.011, 
URL https://www.sciencedirect.com/science/article/pii/S0306261909004395. 
[37] Li, H., Liu, X., and Fang, G., “Preparation and characteristics of n-
nonadecane/cement composites as thermal energy storage materials in build-
ings,” Energy and Buildings, Vol. 42, No. 10, 2010, pp. 1661–1665. https: 
//doi.org/10.1016/j.enbuild.2010.04.009, URL https://www.sciencedirect. 
com/science/article/pii/S0378778810001386. 
[38] Sarı, A., Alkan, C., and Biçer, A., “Thermal energy storage charac-
teristics of micro-nanoencapsulated heneicosane and octacosane with 
poly(methylmethacrylate) shell,” Journal of Microencapsulation, Vol. 33, 
No. 3, 2016, pp. 221–228. https://doi.org/10.3109/02652048.2016.1144820, 
URL https://doi.org/10.3109/02652048.2016.1144820, publisher: Taylor & 
Francis eprint: https://doi.org/10.3109/02652048.2016.1144820. 
[39] Alkan, C., “Enthalpy of melting and solidification of sulfonated paraffins as 
115
phase change materials for thermal energy storage,” Thermochimica Acta, 
Vol. 451, No. 1, 2006, pp. 126–130. https://doi.org/10.1016/j.tca.2006.09.010, 
URL https://www.sciencedirect.com/science/article/pii/S0040603106004928. 
[40] Sarı, A., and Karaipekli, A., “Thermal conductivity and latent heat thermal 
energy storage characteristics of paraffin/expanded graphite composite as 
phase change material,” Applied Thermal Engineering, Vol. 27, No. 8, 2007, 
pp. 1271–1277. https://doi.org/10.1016/j.applthermaleng.2006.11.004, URL 
https://www.sciencedirect.com/science/article/pii/S1359431106004030. 
[41] Weng, Y.-C., Cho, H.-P., Chang, C.-C., and Chen, S.-L., “Heat pipe with 
PCM for electronic cooling,” Applied Energy, Vol. 88, No. 5, 2011, pp. 1825– 
1833. https://doi.org/10.1016/j.apenergy.2010.12.004, URL https://www. 
sciencedirect.com/science/article/pii/S0306261910005118. 
[42] Sarı, A., Alkan, C., Döğüşcü, D. K., and Kızıl, , “Micro/nano encapsulated n-
tetracosane and n-octadecane eutectic mixture with polystyrene shell for low-
temperature latent heat thermal energy storage applications,” Solar Energy, 
Vol. 115, 2015, pp. 195–203. https://doi.org/10.1016/j.solener.2015.02.035, 
URL https://www.sciencedirect.com/science/article/pii/S0038092X1500105X. 
[43] Naikwadi, A. T., Samui, A. B., and Mahanwar, P. A., “Melamine-
formaldehyde microencapsulated n-Tetracosane phase change material for 
solar thermal energy storage in coating,” Solar Energy Materials and So-
lar Cells, Vol. 215, 2020, p. 110676. https://doi.org/10.1016/j.solmat. 
2020.110676, URL https://www.sciencedirect.com/science/article/pii/ 
S0927024820302774. 
[44] Dhandayuthabani, M., Jegadheeswaran, S., Vijayan, V., and Antony, A. G., 
“Investigation of latent heat storage system using graphite micro-particle en-
116
hancement,” Journal of Thermal Analysis and Calorimetry, Vol. 139, No. 3, 
2020, pp. 2181–2186. https://doi.org/10.1007/s10973-019-08625-7, URL 
https://doi.org/10.1007/s10973-019-08625-7. 
[45] Huang, J., Wang, T., Wang, C., and Rao, Z., “Molecular Dynamics Simula-
tions of Melting Behaviour of n-Hexacosane as Phase Change Material for 
Thermal Energy Storage,” Asian Journal of Chemistry, Vol. 25, No. 4, 2013, 
pp. 1839–1841. https://doi.org/10.14233/ajchem.2013.13180, URL http: 
//www.asianjournalofchemistry.co.in/User/ViewFreeArticle.aspx?ArticleID= 
25 4 17. 
[46] Paneliya, S., Khanna, S., Utsav, Makani, N. H., Banerjee, R., and Mukhopad-
hyay, I., “Highly stable n-hexacosane loaded exfoliated graphite nanosheets 
for enhanced thermal energy storage application,” Journal of Energy Stor-
age, Vol. 48, 2022, p. 103903. https://doi.org/10.1016/j.est.2021.103903, URL 
https://www.sciencedirect.com/science/article/pii/S2352152X21015681. 
[47] Yatağanbaba, A., and Kurtbaş, , “Effect of Heating Position on Ther-
mal Energy Storage in Cavity With/Without Open-cell Metallic Foams,” 
Experimental Heat Transfer, Vol. 29, No. 3, 2016, pp. 355–377. 
https://doi.org/10.1080/08916152.2014.989376, URL https://doi.org/ 
10.1080/08916152.2014.989376, publisher: Taylor & Francis eprint: 
https://doi.org/10.1080/08916152.2014.989376. 
[48] Sarı, A., Alkan, C., Karaipekli, A., and Uzun, O., “Microencapsulated n-
octacosane as phase change material for thermal energy storage,” Solar 
Energy, Vol. 83, No. 10, 2009, pp. 1757–1763. https://doi.org/10.1016/j. 
solener.2009.05.008, URL https://www.sciencedirect.com/science/article/pii/ 
S0038092X09001157. 
117
[49] Zhu, Y., Chi, Y., Liang, S., Luo, X., Chen, K., Tian, C., Wang, J., and 
Zhang, L., “Novel metal coated nanoencapsulated phase change materials 
with high thermal conductivity for thermal energy storage,” Solar Energy 
Materials and Solar Cells, Vol. 176, 2018, pp. 212–221. https://doi.org/ 
10.1016/j.solmat.2017.12.006, URL https://www.sciencedirect.com/science/ 
article/pii/S0927024817306542. 
[50] Fang, Y., Liu, X., Liang, X., Liu, H., Gao, X., and Zhang, Z., “Ultrasonic 
synthesis and characterization of polystyrene/n-dotriacontane compos-
ite nanoencapsulated phase change material for thermal energy storage,” 
Applied Energy, Vol. 132, 2014, pp. 551–556. https://doi.org/10.1016/j. 
apenergy.2014.06.056, URL https://www.sciencedirect.com/science/article/ 
pii/S0306261914006382. 
[51] Pawar, V. R., and Sobhansarbandi, S., “CFD modeling of a thermal energy 
storage based heat pipe evacuated tube solar collector,” Journal of Energy 
Storage, Vol. 30, 2020, p. 101528. https://doi.org/10.1016/j.est.2020.101528, 
URL https://www.sciencedirect.com/science/article/pii/S2352152X20301195. 
[52] Pawar, V. R., and Sobhansarbandi, S., “Performance Optimization of 
Thermal Energy Storage Based Solar Collector,” American Society of Me-
chanical Engineers Digital Collection, 2021. https://doi.org/10.1115/ 
POWER2021-64127, URL https://asmedigitalcollection.asme.org/POWER/ 
proceedings/POWER2021/85109/V001T12A005/1115981. 
[53] Sharma, A., Tyagi, V. V., Chen, C. R., and Buddhi, D., “Review on thermal 
energy storage with phase change materials and applications,” Renewable and 
Sustainable Energy Reviews, Vol. 13, No. 2, 2009, pp. 318–345. https://doi. 
org/10.1016/j.rser.2007.10.005, URL https://www.sciencedirect.com/science/ 
article/pii/S1364032107001402. 
118
[54] Pielichowski, K., and Flejtuch, K., “Differential scanning calorimetry stud-
ies on poly(ethylene glycol) with different molecular weights for ther-
mal energy storage materials,” Polymers for Advanced Technologies, 
Vol. 13, No. 10-12, 2002, pp. 690–696. https://doi.org/10.1002/pat.276, 
URL https://onlinelibrary.wiley.com/doi/abs/10.1002/pat.276, eprint: 
https://onlinelibrary.wiley.com/doi/pdf/10.1002/pat.276. 
[55] Pielichowski, K., and Flejtuch, K., “Binary blends of polyethers with fatty 
acids: A thermal characterization of the phase transitions,” Journal of Ap-
plied Polymer Science, Vol. 90, No. 3, 2003, pp. 861–870. https://doi.org/10. 
1002/app.12775, URL https://onlinelibrary.wiley.com/doi/10.1002/app.12775. 
[56] Nguyen, X. V., “Fabrication and Performance Evaluation of Cold Thermal 
Energy Storage Tanks Operating in Water Chiller Air Conditioning System,” 
Energies, Vol. 14, No. 14, 2021, p. 4159. https://doi.org/10.3390/en14144159, 
URL https://www.mdpi.com/1996-1073/14/14/4159, number: 14 Publisher: 
Multidisciplinary Digital Publishing Institute. 
[57] Zuo, J., Li, W., and Weng, L., “Thermal performance of caprylic acid/1-
dodecanol eutectic mixture as phase change material (PCM),” Energy and 
Buildings, Vol. 43, No. 1, 2011, pp. 207–210. https://doi.org/10.1016/j. 
enbuild.2010.09.008, URL https://www.sciencedirect.com/science/article/pii/ 
S037877881000318X. 
[58] Ali Memon, S., Yiu Lo, T., Shi, X., Barbhuiya, S., and Cui, H., “Prepa-
ration, characterization and thermal properties of Lauryl alcohol/Kaolin 
as novel form-stable composite phase change material for thermal energy 
storage in buildings,” Applied Thermal Engineering, Vol. 59, No. 1, 2013, 
pp. 336–347. https://doi.org/10.1016/j.applthermaleng.2013.05.015, URL 
https://www.sciencedirect.com/science/article/pii/S1359431113003633. 
119
[59] Kumar, R., Vyas, S., and Dixit, A., “Fatty acids/1-dodecanol binary eu-
tectic phase change materials for low temperature solar thermal applica-
tions: Design, development and thermal analysis,” Solar Energy, Vol. 155, 
2017, pp. 1373–1379. https://doi.org/10.1016/j.solener.2017.07.082, URL 
https://www.sciencedirect.com/science/article/pii/S0038092X17306679. 
[60] Philip, N., Raam Dheep, G., and Sreekumar, A., “Cold thermal energy stor-
age with lauryl alcohol and cetyl alcohol eutectic mixture: Thermophys-
ical studies and experimental investigation,” Journal of Energy Storage, 
Vol. 27, 2020, p. 101060. https://doi.org/10.1016/j.est.2019.101060, URL 
https://www.sciencedirect.com/science/article/pii/S2352152X1931120X. 
[61] Zuo, J., Li, W., and Weng, L., “Thermal properties of lauric acid/1-
tetradecanol binary system for energy storage,” Applied Thermal Engi-
neering, Vol. 31, No. 6, 2011, pp. 1352–1355. https://doi.org/10.1016/j. 
applthermaleng.2011.01.008, URL https://www.sciencedirect.com/science/ 
article/pii/S1359431111000172. 
[62] Ayaz, H., Chinnasamy, V., Jeon, Y., and Cho, H., “Thermo-physical studies 
and corrosion analysis of caprylic acid–cetyl alcohol binary mixture as novel 
phase change material for refrigeration systems,” Energy Reports, Vol. 8, 
2022, pp. 7143–7153. https://doi.org/10.1016/j.egyr.2022.05.239, URL 
https://www.sciencedirect.com/science/article/pii/S235248472201085X. 
[63] Aydın, A. A., and Aydın, A., “High-chain fatty acid esters of 1-hexadecanol 
for low temperature thermal energy storage with phase change materials,” 
Solar Energy Materials and Solar Cells, Vol. 96, 2012, pp. 93–100. https: 
//doi.org/10.1016/j.solmat.2011.09.013, URL https://www.sciencedirect.com/ 
science/article/pii/S0927024811004995. 
120
[64] Veerakumar, C., and Sreekumar, A., “Preparation, Thermophysi-
cal Studies, and Corrosion Analysis of a Stable Capric Acid/Cetyl 
Alcohol Binary Eutectic Phase Change Material for Cold Ther-
mal Energy Storage,” Energy Technology, Vol. 6, No. 2, 2018, pp. 
397–405. https://doi.org/10.1002/ente.201700540, URL https:// 
onlinelibrary.wiley.com/doi/abs/10.1002/ente.201700540, eprint: 
https://onlinelibrary.wiley.com/doi/pdf/10.1002/ente.201700540. 
[65] Han, S., Kim, C., and Kwon, D., “Thermal/oxidative degradation and sta-
bilization of polyethylene glycol,” Polymer, Vol. 38, No. 2, 1997, pp. 317– 
323. https://doi.org/10.1016/S0032-3861(97)88175-X, URL https://www. 
sciencedirect.com/science/article/pii/S003238619788175X. 
[66] Karaman, S., Karaipekli, A., Sarı, A., and Biçer, A., “Polyethylene glycol 
(PEG)/diatomite composite as a novel form-stable phase change material 
for thermal energy storage,” Solar Energy Materials and Solar Cells, Vol. 95, 
No. 7, 2011, pp. 1647–1653. https://doi.org/10.1016/j.solmat.2011.01.022, 
URL https://www.sciencedirect.com/science/article/pii/S0927024811000365. 
[67] Paberit, R., Rilby, E., Göhl, J., Swenson, J., Refaa, Z., Johansson, P., and 
Jansson, H., “Cycling Stability of Poly(ethylene glycol) of Six Molecular 
Weights: Influence of Thermal Conditions for Energy Applications,” ACS 
Applied Energy Materials, Vol. 3, No. 11, 2020, pp. 10578–10589. https: 
//doi.org/10.1021/acsaem.0c01621, URL https://pubs.acs.org/doi/10.1021/ 
acsaem.0c01621. 
[68] Kou, Y., Wang, S., Luo, J., Sun, K., Zhang, J., Tan, Z., and Shi, Q., “Ther-
mal analysis and heat capacity study of polyethylene glycol (PEG) phase 
change materials for thermal energy storage applications,” The Journal of 
Chemical Thermodynamics, Vol. 128, 2019, pp. 259–274. https://doi.org/ 
121
10.1016/j.jct.2018.08.031, URL https://linkinghub.elsevier.com/retrieve/pii/ 
S0021961418304294. 
[69] Wang, Y., Tang, B., and Zhang, S., “Single-Walled Carbon Nan-
otube/Phase Change Material Composites: Sunlight-Driven, Re-
versible, Form-Stable Phase Transitions for Solar Thermal Energy 
Storage,” Advanced Functional Materials, Vol. 23, No. 35, 2013, pp. 
4354–4360. https://doi.org/10.1002/adfm.201203728, URL https: 
//onlinelibrary.wiley.com/doi/abs/10.1002/adfm.201203728, eprint: 
https://onlinelibrary.wiley.com/doi/pdf/10.1002/adfm.201203728. 
[70] Saeed, R. M., Schlegel, J. P., Castano, C., Sawafta, R., and Kuturu, V., 
“Preparation and thermal performance of methyl palmitate and lauric acid 
eutectic mixture as phase change material (PCM),” Journal of Energy Stor-
age, Vol. 13, 2017, pp. 418–424. https://doi.org/10.1016/j.est.2017.08.005, 
URL https://www.sciencedirect.com/science/article/pii/S2352152X16301621. 
[71] Zhang, H., Zhang, L., Li, Q., Huang, C., Guo, H., Xiong, L., and Chen, X., 
“Preparation and characterization of methyl palmitate/palygorskite com-
posite phase change material for thermal energy storage in buildings,” Con-
struction and Building Materials, Vol. 226, 2019, pp. 212–219. https://doi. 
org/10.1016/j.conbuildmat.2019.07.152, URL https://www.sciencedirect.com/ 
science/article/pii/S0950061819318252. 
[72] Hekimoğlu, G., Sarı, A., Kar, T., Keleş, S., Kaygusuz, K., Tyagi, V. V., 
Sharma, R. K., Al-Ahmed, A., Al-Sulaiman, F. A., and Saleh, T. A., “Walnut 
shell derived bio-carbon/methyl palmitate as novel composite phase change 
material with enhanced thermal energy storage properties,” Journal of Energy 
Storage, Vol. 35, 2021, p. 102288. https://doi.org/10.1016/j.est.2021.102288, 
URL https://www.sciencedirect.com/science/article/pii/S2352152X21000529. 
122
[73] Yıldırım, A., “An Ionic Liquid Promoted Clean and Direct Conver-
sion of Triglycerides into Bio-Based Thermal Energy Storage Mate-
rials,” European Journal of Lipid Science and Technology, Vol. 124, 
No. 6, 2022, p. 2200032. https://doi.org/10.1002/ejlt.202200032, URL 
https://onlinelibrary.wiley.com/doi/abs/10.1002/ejlt.202200032, eprint: 
https://onlinelibrary.wiley.com/doi/pdf/10.1002/ejlt.202200032. 
[74] Salman, M., Girault, Y., Balbi, N., and Elegant, L., “Calorimetric study of 
the reaction between formic acid and N,N,N,N-tetramethylethylenediamine 
from the aspect of thermal energy storage,” Journal of thermal analysis, 
Vol. 37, No. 10, 1991, pp. 2389–2394. https://doi.org/10.1007/BF01913740, 
URL https://doi.org/10.1007/BF01913740. 
[75] Elegant, L., Salman, M., and Schwob, Y., “Calorimetric study of some car-
boxylic acids lewis-bases complexes in view of thermal energy storage,” Ther-
mochimica Acta, Vol. 130, 1988, pp. 149–154. https://doi.org/10.1016/ 
0040-6031(88)87060-6, URL https://www.sciencedirect.com/science/article/ 
pii/0040603188870606. 
[76] Karaipekli, A., and Sarı, A., “Capric–myristic acid/vermiculite compos-
ite as form-stable phase change material for thermal energy storage,” So-
lar Energy, Vol. 83, No. 3, 2009, pp. 323–332. https://doi.org/10.1016/j. 
solener.2008.08.012, URL https://www.sciencedirect.com/science/article/pii/ 
S0038092X08002089. 
[77] Wang, L., and Meng, D., “Fatty acid eutectic/polymethyl methacrylate com-
posite as form-stable phase change material for thermal energy storage,” Ap-
plied Energy, Vol. 87, No. 8, 2010, pp. 2660–2665. https://doi.org/10.1016/ 
j.apenergy.2010.01.010, URL https://www.sciencedirect.com/science/article/ 
pii/S0306261910000127. 
123
[78] Keleş, S., Kaygusuz, K., and Sarı, A., “Lauric and myristic acids eu-
tectic mixture as phase change material for low-temperature heat-
ing applications,” International Journal of Energy Research, Vol. 29, 
No. 9, 2005, pp. 857–870. https://doi.org/10.1002/er.1111, URL 
https://onlinelibrary.wiley.com/doi/abs/10.1002/er.1111, eprint: 
https://onlinelibrary.wiley.com/doi/pdf/10.1002/er.1111. 
[79] Lv, Y., Jin, W., Yang, Y., Zhang, H., Zhang, X., Ding, F., and Zhou, W., 
“Experimental thermal storage research of organic binary phase change ma-
terials in building environment,” International Journal of Green Energy, 
Vol. 14, No. 11, 2017, pp. 916–924. https://doi.org/10.1080/15435075.2017. 
1339042, URL https://doi.org/10.1080/15435075.2017.1339042, publisher: 
Taylor & Francis eprint: https://doi.org/10.1080/15435075.2017.1339042. 
[80] Genc, Z. K., Canbay, C. A., Acar, S. S., Sekerci, M., and Genc, M., “Prepa-
ration and thermal properties of heterogeneous composite phase change ma-
terials based on camphene–palmitic acid,” Journal of Thermal Analysis and 
Calorimetry, Vol. 120, No. 3, 2015, pp. 1679–1688. https://doi.org/10.1007/ 
s10973-015-4478-3, URL https://doi.org/10.1007/s10973-015-4478-3. 
[81] Hoseini, Z., and Nikje, M. M. A., “The Preparation of Novel Microcapsules 
Based on Palmitic Acid Core and Waterborne Polyurethane/Silane Shell as 
Phase Change Materials for Thermal Energy Storage,” Journal of Polymers 
and the Environment, Vol. 29, No. 3, 2021, pp. 821–828. https://doi.org/10. 
1007/s10924-020-01916-3, URL https://doi.org/10.1007/s10924-020-01916-3. 
[82] Jaya Krishna, D., and Kochar, S., “The Metallographic Study of Corrosion 
of Metals with Latent Heat Storage Materials Suitable for Solar Hot Water 
System,” Transactions of the Indian Ceramic Society, Vol. 76, No. 2, 2017, 
pp. 133–141. https://doi.org/10.1080/0371750X.2016.1268072, URL https:// 
124
doi.org/10.1080/0371750X.2016.1268072, publisher: Taylor & Francis eprint: 
https://doi.org/10.1080/0371750X.2016.1268072. 
[83] Canbay, C. A., Genc, Z. K., Acar, S. S., Sekerci, M., and Genc, M., “Prepa-
ration and Thermodynamic Properties of Camphene/Stearic Acid Compos-
ites as Phase-Change Materials in Buildings,” International Journal of Ther-
mophysics, Vol. 35, No. 8, 2014, pp. 1526–1537. https://doi.org/10.1007/ 
s10765-014-1724-z, URL https://doi.org/10.1007/s10765-014-1724-z. 
[84] Ma, G., Wang, Z., Xie, S., Sun, J., Jia, Y., Jing, Y., and Du, G., 
“Preparation and Properties of Stearic Acid–Acetanilide Eutectic 
Mixture/Expanded Graphite Composite Phase-Change Material for 
Thermal Energy Storage,” Energy Technology, Vol. 6, No. 1, 2018, 
pp. 153–160. https://doi.org/10.1002/ente.201700352, URL https: 
//onlinelibrary.wiley.com/doi/abs/10.1002/ente.201700352, eprint: 
https://onlinelibrary.wiley.com/doi/pdf/10.1002/ente.201700352. 
[85] Ma, G., Sun, J., Zhang, Y., Jing, Y., and Jia, Y., “A novel low-temperature 
phase change material based on stearic acid and hexanamide eutectic mixture 
for thermal energy storage,” Chemical Physics Letters, Vol. 714, 2019, pp. 
166–171. https://doi.org/10.1016/j.cplett.2018.11.003, URL https://www. 
sciencedirect.com/science/article/pii/S0009261418309175. 
[86] Ma, G., Sun, J., Zhang, Y., Jing, Y., and Jia, Y., “Preparation and thermal 
properties of stearic acid-benzamide eutectic mixture/expanded graphite 
composites as phase change materials for thermal energy storage,” Pow-
der Technology, Vol. 342, 2019, pp. 131–140. https://doi.org/10.1016/j. 
powtec.2018.09.074, URL https://www.sciencedirect.com/science/article/pii/ 
S0032591018308015. 
125
[87] Mishra, A. K., Lahiri, B. B., and Philip, J., “Thermal conductivity enhance-
ment in organic phase change material (phenol-water system) upon addition 
of Al2O3, SiO2 and TiO2 nano-inclusions,” Journal of Molecular Liquids, 
Vol. 269, 2018, pp. 47–63. https://doi.org/10.1016/j.molliq.2018.08.001, URL 
https://www.sciencedirect.com/science/article/pii/S0167732218327831. 
[88] Ganapathi, G. B., and Wirz, R., “High Density Thermal Energy Storage 
With Supercritical Fluids,” American Society of Mechanical Engineers Dig-
ital Collection, 2013, pp. 699–707. https://doi.org/10.1115/ES2012-91008, 
URL https://turbomachinery.asmedigitalcollection.asme.org/ES/proceedings/ 
ES2012/44816/699/232235. 
[89] Yang, L., Peng, H., Ling, X., and Dong, H., “Numerical analysis on perfor-
mance of naphthalene phase change thermal storage system in aluminum 
plate-fin unit,” Heat and Mass Transfer, Vol. 51, No. 2, 2015, pp. 195–207. 
https://doi.org/10.1007/s00231-014-1400-7, URL https://doi.org/10.1007/ 
s00231-014-1400-7. 
[90] Dinker, A., Agarwal, M., and Agarwal, G. D., “Modelling and Simulation of 
Helical Coil Embedded Heat Storage Unit Using Beeswax/Expanded Graphite 
Composite as Phase Change Material,” Mathematical Modeling, Computa-
tional Intelligence Techniques and Renewable Energy, edited by M. Sahni, 
J. M. Merigó, B. K. Jha, and R. Verma, Springer, Singapore, 2021, pp. 411– 
423. https://doi.org/10.1007/978-981-15-9953-8 36. 
[91] Wang, J., Han, W., Ge, C., Guan, H., Yang, H., and Zhang, X., “Form-stable 
oxalic acid dihydrate/glycolic acid-based composite PCMs for thermal energy 
storage,” Renewable Energy, Vol. 136, 2019, pp. 657–663. https://doi.org/ 
10.1016/j.renene.2019.01.063, URL https://www.sciencedirect.com/science/ 
article/pii/S0960148119300631. 
126
[92] Lennartson, A., Roffey, A., and Moth-Poulsen, K., “Designing photoswitches 
for molecular solar thermal energy storage,” Tetrahedron Letters, Vol. 56, 
No. 12, 2015, pp. 1457–1465. https://doi.org/10.1016/j.tetlet.2015.01.187, 
URL https://www.sciencedirect.com/science/article/pii/S0040403915002373. 
[93] Raam Dheep, G., and Sreekumar, A., “Thermal reliability and corrosion 
characteristics of an organic phase change materials for solar space heat-
ing applications,” Journal of Energy Storage, Vol. 23, 2019, pp. 98–105. 
https://doi.org/10.1016/j.est.2019.03.009, URL https://www.sciencedirect. 
com/science/article/pii/S2352152X19300520. 
[94] Wang, A., Chen, C., and Xu, G., “Silica/Acetamide Composite as Form-
Stable Phase Change Material for Latent Heat Thermal Energy Storage,” 
Journal of Advanced Microscopy Research, Vol. 7, No. 4, 2012, pp. 286–291. 
https://doi.org/10.1166/jamr.2012.1128. 
[95] Xia, L., and Zhang, P., “Thermal property measurement and heat transfer 
analysis of acetamide and acetamide/expanded graphite composite phase 
change material for solar heat storage,” Solar Energy Materials and So-
lar Cells, Vol. 95, No. 8, 2011, pp. 2246–2254. https://doi.org/10.1016/j. 
solmat.2011.03.031, URL https://www.sciencedirect.com/science/article/pii/ 
S092702481100184X. 
[96] Dheep, G. R., and Sreekumar, A., “Investigation on thermal reliability 
and corrosion characteristics of glutaric acid as an organic phase change 
material for solar thermal energy storage applications,” Applied Thermal 
Engineering, Vol. 129, 2018, pp. 1189–1196. https://doi.org/10.1016/j. 
applthermaleng.2017.10.133, URL https://www.sciencedirect.com/science/ 
article/pii/S1359431117317337. 
127
[97] Purohit, K., Murty, V. V. S., Dixit, R. C., and Sharma, A., “Development 
of an acetanilide/benzoic acid eutectic phase change material based ther-
mal energy storage unit for a passive water heating system,” Bulletin of 
Materials Science, Vol. 42, No. 3, 2019, p. 119. https://doi.org/10.1007/ 
s12034-019-1731-6, URL https://doi.org/10.1007/s12034-019-1731-6. 
[98] Saini, G., Singh, H., Saini, K., and Yadav, A., “Experimental investiga-
tion of the solar cooker during sunshine and off-sunshine hours using the 
thermal energy storage unit based on a parabolic trough collector,” In-
ternational Journal of Ambient Energy, Vol. 37, No. 6, 2016, pp. 597– 
608. https://doi.org/10.1080/01430750.2015.1023836, URL https://doi. 
org/10.1080/01430750.2015.1023836, publisher: Taylor & Francis eprint: 
https://doi.org/10.1080/01430750.2015.1023836. 
[99] Raam Dheep, G., and Sreekumar, A., “Influence of accelerated thermal charg-
ing and discharging cycles on thermo-physical properties of organic phase 
change materials for solar thermal energy storage applications,” Energy Con-
version and Management, Vol. 105, 2015, pp. 13–19. https://doi.org/10.1016/ 
j.enconman.2015.07.040, URL https://www.sciencedirect.com/science/article/ 
pii/S0196890415006913. 
[100] Myers, P. D., and Goswami, D. Y., “Thermal energy storage using chloride 
salts and their eutectics,” Applied Thermal Engineering, Vol. 109, 2016, pp. 
889–900. https://doi.org/10.1016/j.applthermaleng.2016.07.046, URL https: 
//www.sciencedirect.com/science/article/pii/S1359431116311759. 
[101] Jiang, Y., Liu, M., and Sun, Y., “Review on the development of high tem-
perature phase change material composites for solar thermal energy stor-
age,” Solar Energy Materials and Solar Cells, Vol. 203, 2019, p. 110164. 
128
https://doi.org/10.1016/j.solmat.2019.110164, URL https://linkinghub. 
elsevier.com/retrieve/pii/S0927024819304933. 
[102] Jiang, Y., Sun, Y., Liu, M., Bruno, F., and Li, S., “Eutectic Na2CO3–NaCl 
salt: A new phase change material for high temperature thermal storage,” 
Solar Energy Materials and Solar Cells, Vol. 152, 2016, pp. 155–160. https: 
//doi.org/10.1016/j.solmat.2016.04.002, URL https://linkinghub.elsevier.com/ 
retrieve/pii/S0927024816300149. 
[103] Liu, M., Gomez, J., Turchi, C., Tay, N., Saman, W., and Bruno, F., “De-
termination of thermo-physical properties and stability testing of high-
temperature phase-change materials for CSP applications,” Solar Energy 
Materials and Solar Cells, Vol. 139, 2015, pp. 81–87. https://doi.org/10. 
1016/j.solmat.2015.03.014, URL https://linkinghub.elsevier.com/retrieve/pii/ 
S0927024815001257. 
[104] Kenisarin, M. M., “High-temperature phase change materials for thermal en-
ergy storage,” Renewable and Sustainable Energy Reviews, Vol. 14, No. 3, 
2010, pp. 955–970. https://doi.org/10.1016/j.rser.2009.11.011, URL https: 
//linkinghub.elsevier.com/retrieve/pii/S1364032109002731. 
[105] Hasnain, S. M., “Review on sustainable thermal energy storage technolo-
gies, Part I: heat storage materials and techniques,” Energy Conversion and 
Management, Vol. 39, No. 11, 1998, pp. 1127–1138. https://doi.org/10.1016/ 
S0196-8904(98)00025-9, URL https://www.sciencedirect.com/science/article/ 
pii/S0196890498000259. 
[106] Beaupere, N., Soupremanien, U., and Zalewski, L., “Nucleation triggering 
methods in supercooled phase change materials (PCM), a review,” Ther-
129
mochimica Acta, Vol. 670, 2018, pp. 184–201. https://doi.org/10.1016/j.tca. 
2018.10.009. 
[107] Belton, G., and Ajami, F., “Thermochemistry of salt hydrates,” Tech. rep., 
United States, May 1973. URL https://www.osti.gov/biblio/5102836. 
[108] Günther, E., Mehling, H., and Werner, M., “Melting and nucleation temper-
atures of three salt hydrate phase change materials under static pressures 
up to 800 MPa,” Journal of Physics D: Applied Physics, Vol. 40, No. 15, 
2007, pp. 4636–4641. https://doi.org/10.1088/0022-3727/40/15/042, URL 
https://iopscience.iop.org/article/10.1088/0022-3727/40/15/042. 
[109] Ryu, H. W., Woo, S. W., Shin, B. C., and Kim, S. D., “Prevention of su-
percooling and stabilization of inorganic salt hydrates as latent heat stor-
age materials,” Solar Energy Materials and Solar Cells, Vol. 27, No. 2, 
1992, pp. 161–172. https://doi.org/10.1016/0927-0248(92)90117-8, URL 
https://www.sciencedirect.com/science/article/pii/0927024892901178. 
[110] Byung Chul Shin, Sang Done Kim, and Won-Hoon, P., “Phase separation and 
supercooling of a latent heat-storage material,” Energy, Vol. 14, No. 12, 1989, 
pp. 921–930. https://doi.org/10.1016/0360-5442(89)90047-9, URL https:// 
www.sciencedirect.com/science/article/pii/0360544289900479. 
[111] Li, M., Wang, W., Zhang, Z., He, F., Yan, S., Yan, P.-J., Xie, R., Ju, X.-J., 
Liu, Z., and Chu, L.-Y., “Monodisperse Na 2 SO 4 ·10H 2 O@SiO 2 Micropar-
ticles against Supercooling and Phase Separation during Phase Change for 
Efficient Energy Storage,” Industrial & Engineering Chemistry Research, 
Vol. 56, No. 12, 2017, pp. 3297–3308. https://doi.org/10.1021/acs.iecr. 
7b00231, URL https://pubs.acs.org/doi/10.1021/acs.iecr.7b00231. 
[112] Marks, S., “An investigation of the thermal energy storage capacity of 
130
Glauber’s salt with respect to thermal cycling,” Solar Energy, Vol. 25, No. 3, 
1980, pp. 255–258. https://doi.org/10.1016/0038-092X(80)90332-1, URL 
https://www.sciencedirect.com/science/article/pii/0038092X80903321. 
[113] Naumann, R., and Emons, H.-H., “Results of thermal analysis for investi-
gation of salt hydrates as latent heat-storage materials,” Journal of Ther-
mal Analysis, Vol. 35, No. 3, 1989, pp. 1009–1031. https://doi.org/10.1007/ 
BF02057256. 
[114] Khudhair, A. M., and Farid, M. M., “A review on energy conservation in 
building applications with thermal storage by latent heat using phase change 
materials,” Energy Conversion and Management, Vol. 45, No. 2, 2004, pp. 
263–275. https://doi.org/10.1016/S0196-8904(03)00131-6, URL https: 
//www.sciencedirect.com/science/article/pii/S0196890403001316. 
[115] PARIS, J., FALARDEAU, M., and VILLENEUVE, C., “Thermal Storage 
by Latent Heat: A Viable Option for Energy Conservation in Buildings,” 
Energy Sources, Vol. 15, No. 1, 1993, pp. 85–93. https://doi.org/10.1080/ 
00908319308909014, URL https://doi.org/10.1080/00908319308909014, pub-
lisher: Taylor & Francis eprint: https://doi.org/10.1080/00908319308909014. 
[116] Nagano, K., Mochida, T., Takeda, S., Domański, R., and Rebow, M., “Ther-
mal characteristics of manganese (II) nitrate hexahydrate as a phase change 
material for cooling systems,” Applied Thermal Engineering, Vol. 23, No. 2, 
2003, pp. 229–241. https://doi.org/10.1016/S1359-4311(02)00161-8, URL 
https://www.sciencedirect.com/science/article/pii/S1359431102001618. 
[117] Cabeza, L. F., Svensson, G., Hiebler, S., and Mehling, H., “Thermal per-
formance of sodium acetate trihydrate thickened with different materials as 
phase change energy storage material,” Applied Thermal Engineering, Vol. 23, 
131
No. 13, 2003, pp. 1697–1704. https://doi.org/10.1016/S1359-4311(03)00107-8, 
URL https://www.sciencedirect.com/science/article/pii/S1359431103001078. 
[118] Medrano, M., Yilmaz, S., Sheth, F. K., Martorell, I., Paksoy, H. O., and 
Cabeza, L. F., “Salt Water Solutions as PCM for Cooling Applications,” Pro-
ceedings of the EuroSun 2010 Conference, International Solar Energy Society, 
Graz, Austria, 2010, pp. 1–8. https://doi.org/10.18086/eurosun.2010.16.20, 
URL http://proceedings.ises.org/citation?doi=eurosun.2010.16.20. 
[119] Mo, S., Chen, Y., Jia, L., and Luo, X., “Reduction of supercooling of wa-
ter by TiO2 nanoparticles as observed using differential scanning calorime-
ter,” Journal of Experimental Nanoscience, Vol. 8, No. 4, 2013, pp. 533– 
539. https://doi.org/10.1080/17458080.2011.572085, URL https://doi. 
org/10.1080/17458080.2011.572085, publisher: Taylor & Francis eprint: 
https://doi.org/10.1080/17458080.2011.572085. 
[120] Lee, J.-H., Hwang, K. S., Jang, S. P., Lee, B. H., Kim, J. H., Choi, S. U. S., 
and Choi, C. J., “Effective viscosities and thermal conductivities of aqueous 
nanofluids containing low volume concentrations of Al2O3 nanoparticles,” 
International Journal of Heat and Mass Transfer, Vol. 51, No. 11, 2008, pp. 
2651–2656. https://doi.org/10.1016/j.ijheatmasstransfer.2007.10.026, URL 
https://www.sciencedirect.com/science/article/pii/S0017931007006680. 
[121] Zhu, S., Nguyen, M. T., and Yonezawa, T., “Micro- and nano-encapsulated 
metal and alloy-based phase-change materials for thermal energy storage,” 
Nanoscale Advances, Vol. 3, No. 16, 2021, pp. 4626–4645. https://doi.org/10. 
1039/D0NA01008A, URL http://xlink.rsc.org/?DOI=D0NA01008A. 
[122] Pan, A., Wang, J., and Zhang, X., “Prediction of Melting Temperature and 
Latent Heat for Low-melting Metal PCMs,” Rare Metal Materials and En-
132
gineering, Vol. 45, No. 4, 2016, pp. 874–880. https://doi.org/10.1016/ 
S1875-5372(16)30091-1, URL https://www.sciencedirect.com/science/article/ 
pii/S1875537216300911. 
[123] Ge, H., Li, H., Mei, S., and Liu, J., “Low melting point liquid metal as a new 
class of phase change material: An emerging frontier in energy area,” Renew-
able and Sustainable Energy Reviews, Vol. 21, No. C, 2013, pp. 331–346. URL 
https://ideas.repec.org/a/eee/rensus/v21y2013icp331-346.html, publisher: El-
sevier. 
[124] Su, W., Darkwa, J., and Kokogiannakis, G., “Review of solid-liquid phase 
change materials and their encapsulation technologies,” Faculty of Engi-
neering and Information Sciences - Papers: Part A, 2015, pp. 373–391. 
https://doi.org/10.1016/j.rser.2015.04.044, URL https://ro.uow.edu.au/ 
eispapers/3985. 
[125] Manasijević, I., Balanović, L., Grgurić, T. H., Minić, D., and Gorgievski, 
M., “Study of Microstructure and Thermal Properties of the Low Melt-
ing Bi-In-Sn Eutectic Alloys,” Materials Research, Vol. 21, 2018. https: 
//doi.org/10.1590/1980-5373-MR-2018-0501, URL http://www.scielo.br/ 
j/mr/a/5dqMfGQGmqvvvyzzbMNgt3F/?lang=en, publisher: ABM, ABC, 
ABPol. 
[126] Wang, Q.-M., Cheng, X.-M., Li, Y.-Y., Yu, G.-M., and Liu, Z., “Microstruc-
tures and thermal properties of Sn–Bi–Pb–Zn alloys as heat storage and 
transfer materials,” Rare Metals, Vol. 38, No. 4, 2019, pp. 350–358. 
https://doi.org/10.1007/s12598-019-01206-5, URL https://doi.org/10.1007/ 
s12598-019-01206-5. 
133
[127] “Lead, Pb,” , ????. URL https://www.matweb.com/search/DataSheet.aspx? 
MatGUID=ebd6d2cdfdca4fc285885cc4749c36b1&ckck=1. 
[128] “Cadmium, Cd,” , ????. URL https://www.matweb.com/search/datasheet. 
aspx?matguid=ca862f5c59594be3b9a2d250460d2dba&n=1. 
[129] Raud, R., Jacob, R., Bruno, F., Will, G., and Steinberg, T. A., “A criti-
cal review of eutectic salt property prediction for latent heat energy stor-
age systems,” Renewable and Sustainable Energy Reviews, Vol. 70, 2017, pp. 
936–944. https://doi.org/10.1016/j.rser.2016.11.274, URL https://www. 
sciencedirect.com/science/article/pii/S1364032116310553. 
[130] Hadiya, J., and Shukla, A. K. N., “Thermal energy storage using phase 
change materials: a way forward,” International Journal of Global Energy 
Issues, Vol. 41, No. 1-4, 2018, pp. 108–127. https://doi.org/10.1504/IJGEI. 
2018.092311, URL https://www.inderscienceonline.com/doi/abs/10.1504/ 
IJGEI.2018.092311, publisher: Inderscience Publishers. 
[131] Li, D., Wu, Y., Wang, B., Liu, C., and Arıcı, M., “Optical and thermal per-
formance of glazing units containing PCM in buildings: A review,” Construc-
tion and Building Materials, Vol. 233, 2020, p. 117327. https://doi.org/ 
10.1016/j.conbuildmat.2019.117327, URL https://www.sciencedirect.com/ 
science/article/pii/S0950061819327795. 
[132] Diarce, G., Quant, L., Campos-Celador, , Sala, J. M., and Garćıa-Romero, A., 
“Determination of the phase diagram and main thermophysical properties of 
the erythritol–urea eutectic mixture for its use as a phase change material,” 
Solar Energy Materials and Solar Cells, Vol. 157, 2016, pp. 894–906. https: 
//doi.org/10.1016/j.solmat.2016.08.016, URL https://www.sciencedirect.com/ 
science/article/pii/S0927024816303075. 
134
[133] Heckenkamp, J., and Baumann, H., “Latentwärmespeicher,” Sonderdruck Aus 
Nachrichten, Vol. 11, 1997, pp. 1075–1081. 
[134] Bland, A., Khzouz, M., Statheros, T., and Gkanas, E. I., “PCMs for Residen-
tial Building Applications: A Short Review Focused on Disadvantages and 
Proposals for Future Development,” Buildings, Vol. 7, No. 3, 2017, p. 78. 
https://doi.org/10.3390/buildings7030078, URL https://www.mdpi.com/ 
2075-5309/7/3/78, number: 3 Publisher: Multidisciplinary Digital Publish-
ing Institute. 
[135] Kalnæs, S. E., and Jelle, B. P., “Phase change materials and products for 
building applications: A state-of-the-art review and future research oppor-
tunities,” Energy and Buildings, Vol. 94, 2015, pp. 150–176. https://doi.org/ 
10.1016/j.enbuild.2015.02.023, URL https://www.sciencedirect.com/science/ 
article/pii/S0378778815001188. 
[136] Mavrigiannaki, A., and Ampatzi, E., “Latent heat storage in building ele-
ments: A systematic review on properties and contextual performance fac-
tors,” Renewable and Sustainable Energy Reviews, Vol. 60, 2016, pp. 852–866. 
https://doi.org/10.1016/j.rser.2016.01.115, URL https://www.sciencedirect. 
com/science/article/pii/S1364032116001453. 
[137] Akeiber, H., Nejat, P., Majid, M. Z. A., Wahid, M. A., Jomehzadeh, F., 
Zeynali Famileh, I., Calautit, J. K., Hughes, B. R., and Zaki, S. A., “A re-
view on phase change material (PCM) for sustainable passive cooling in 
building envelopes,” Renewable and Sustainable Energy Reviews, Vol. 60, 
2016, pp. 1470–1497. https://doi.org/10.1016/j.rser.2016.03.036, URL 
https://www.sciencedirect.com/science/article/pii/S1364032116002719. 
[138] Paranjothi, G., Odukomaiya, A., Cui, S., and Bulk, A., “Evaluation of 
135
phase change plaster/paste composites for building envelopes,” Energy and 
Buildings, Vol. 253, 2021, p. 111372. https://doi.org/10.1016/j.enbuild. 
2021.111372, URL https://www.sciencedirect.com/science/article/pii/ 
S0378778821006563. 
[139] Arumugam, P., Ramalingam, V., and Vellaichamy, P., “Effective PCM, in-
sulation, natural and/or night ventilation techniques to enhance the ther-
mal performance of buildings located in various climates – A review,” En-
ergy and Buildings, Vol. 258, 2022, p. 111840. https://doi.org/10.1016/j. 
enbuild.2022.111840, URL https://www.sciencedirect.com/science/article/ 
pii/S0378778822000111. 
[140] Mukram, T. A., and Daniel, J., “A review of novel methods and current 
developments of phase change materials in the building walls for cooling 
applications,” Sustainable Energy Technologies and Assessments, Vol. 49, 
2022, p. 101709. https://doi.org/10.1016/j.seta.2021.101709, URL https: 
//www.sciencedirect.com/science/article/pii/S2213138821007232. 
[141] Buswell, R. A., Leal de Silva, W. R., Jones, S. Z., and Dirrenberger, J., “3D 
printing using concrete extrusion: A roadmap for research,” Cement and 
Concrete Research, Vol. 112, 2018, pp. 37–49. https://doi.org/10.1016/j. 
cemconres.2018.05.006, URL https://www.sciencedirect.com/science/article/ 
pii/S0008884617311924. 
[142] Gencel, O., Sarı, A., Kaplan, G., Ustaoglu, A., Hekimoğlu, G., Bayraktar, 
O. Y., and Ozbakkaloglu, T., “Properties of eco-friendly foam concrete con-
taining PCM impregnated rice husk ash for thermal management of build-
ings,” Journal of Building Engineering, Vol. 58, 2022, p. 104961. https: 
//doi.org/10.1016/j.jobe.2022.104961, URL https://www.sciencedirect.com/ 
science/article/pii/S235271022200972X. 
136
[143] Omara, A. A. M., Mohammed, H. A., Al Rikabi, I. J., Abuelnour, M. A., 
and Abuelnuor, A. A. A., “Performance improvement of solar chimneys us-
ing phase change materials: A review,” Solar Energy, Vol. 228, 2021, pp. 
68–88. https://doi.org/10.1016/j.solener.2021.09.037, URL https://www. 
sciencedirect.com/science/article/pii/S0038092X21007945. 
[144] Teamah, H. M., and Teamah, M., “Integration of phase change material in 
flat plate solar water collector: A state of the art, opportunities, and chal-
lenges,” Journal of Energy Storage, Vol. 54, 2022, p. 105357. https://doi. 
org/10.1016/j.est.2022.105357, URL https://www.sciencedirect.com/science/ 
article/pii/S2352152X22013512. 
[145] Kośny, J., Biswas, K., Miller, W., and Kriner, S., “Field thermal performance 
of naturally ventilated solar roof with PCM heat sink,” Solar Energy, Vol. 86, 
No. 9, 2012, pp. 2504–2514. https://doi.org/10.1016/j.solener.2012.05.020, 
URL https://www.sciencedirect.com/science/article/pii/S0038092X12001983. 
[146] Tan, P., Lindberg, P., Eichler, K., Löveryd, P., Johansson, P., and Kalaga-
sidis, A. S., “Thermal energy storage using phase change materials: Techno-
economic evaluation of a cold storage installation in an office building,” Ap-
plied Energy, Vol. 276, 2020, p. 115433. https://doi.org/10.1016/j.apenergy. 
2020.115433, URL https://www.sciencedirect.com/science/article/pii/ 
S0306261920309454. 
[147] Goyal, A., Kozubal, E., Woods, J., Nofal, M., and Al-Hallaj, S., “Design 
and performance evaluation of a dual-circuit thermal energy storage mod-
ule for air conditioners,” Applied Energy, Vol. 292, 2021, p. 116843. https: 
//doi.org/10.1016/j.apenergy.2021.116843, URL https://www.sciencedirect. 
com/science/article/pii/S030626192100338X. 
137
[148] Cui, S., Odukomaiya, A., and Vidal, J., “Materials research and development 
needs to enable efficient and electrified buildings,” MRS Bulletin, Vol. 46, 
No. 12, 2021, pp. 1176–1186. https://doi.org/10.1557/s43577-021-00241-x, 
URL https://doi.org/10.1557/s43577-021-00241-x. 
[149] Aljehani, A., Razack, S. A. K., Nitsche, L., and Al-Hallaj, S., “Design and 
optimization of a hybrid air conditioning system with thermal energy storage 
using phase change composite,” Energy Conversion and Management, Vol. 
169, 2018, pp. 404–418. https://doi.org/10.1016/j.enconman.2018.05.040, 
URL https://www.sciencedirect.com/science/article/pii/S019689041830517X. 
[150] Ding, Z., Wu, W., and Leung, M., “Advanced/hybrid thermal energy storage 
technology: material, cycle, system and perspective,” Renewable and Sustain-
able Energy Reviews, Vol. 145, 2021, p. 111088. https://doi.org/10.1016/j. 
rser.2021.111088, URL https://www.sciencedirect.com/science/article/pii/ 
S1364032121003762. 
[151] Rasouli, E., Fricke, E., and Narayanan, V., “High efficiency 3-D printed mi-
crochannel polymer heat exchangers for air conditioning applications,” Sci-
ence and Technology for the Built Environment, Vol. 28, No. 3, 2022, pp. 
289–306. https://doi.org/10.1080/23744731.2022.2026693, URL https:// 
doi.org/10.1080/23744731.2022.2026693, publisher: Taylor & Francis eprint: 
https://doi.org/10.1080/23744731.2022.2026693. 
[152] Wang, F., Maidment, G., Missenden, J., and Tozer, R., “The novel use of 
phase change materials in refrigeration plant. Part 1: Experimental inves-
tigation,” Applied Thermal Engineering, Vol. 27, No. 17, 2007, pp. 2893– 
2901. https://doi.org/10.1016/j.applthermaleng.2005.06.011, URL https: 
//www.sciencedirect.com/science/article/pii/S1359431105001948. 
138
[153] Barzin, R., Chen, J. J. J., Young, B. R., and Farid, M. M., “Application of 
PCM underfloor heating in combination with PCM wallboards for space 
heating using price based control system,” Applied Energy, Vol. 148, 2015, 
pp. 39–48. https://doi.org/10.1016/j.apenergy.2015.03.027, URL https: 
//www.sciencedirect.com/science/article/pii/S0306261915003116. 
[154] Arsana, M. E., Temaja, I. W., Widiantara, I. B. G., and Sukadana, I. B. P., 
“Corn oil phase change material (PCM) in frozen food cooling machine to 
improve energy efficiency,” Journal of Physics: Conference Series, Vol. 1450, 
No. 1, 2020, p. 012107. https://doi.org/10.1088/1742-6596/1450/1/012107, 
URL https://dx.doi.org/10.1088/1742-6596/1450/1/012107, publisher: IOP 
Publishing. 
[155] Nair, A. M., Wilson, C., Huang, M. J., Griffiths, P., and Hewitt, N., “Phase 
change materials in building integrated space heating and domestic hot water 
applications: A review,” Journal of Energy Storage, Vol. 54, 2022, p. 105227. 
https://doi.org/10.1016/j.est.2022.105227, URL https://www.sciencedirect. 
com/science/article/pii/S2352152X22012269. 
[156] Faraj, K., Faraj, J., Hachem, F., Bazzi, H., Khaled, M., and Castelain, C., 
“Analysis of underfloor electrical heating system integrated with coconut 
oil-PCM plates,” Applied Thermal Engineering, Vol. 158, 2019, p. 113778. 
https://doi.org/10.1016/j.applthermaleng.2019.113778, URL https://www. 
sciencedirect.com/science/article/pii/S1359431119309779. 
[157] Zhou, G., and He, J., “Thermal performance of a radiant floor heating system 
with different heat storage materials and heating pipes,” Applied Energy, Vol. 
138, 2015, pp. 648–660. https://doi.org/10.1016/j.apenergy.2014.10.058, URL 
https://www.sciencedirect.com/science/article/pii/S0306261914011088. 
139
[158] Lu, S., Xu, B., and Tang, X., “Experimental study on double pipe PCM floor 
heating system under different operation strategies,” Renewable Energy, Vol. 
145, 2020, pp. 1280–1291. https://doi.org/10.1016/j.renene.2019.06.086, URL 
https://www.sciencedirect.com/science/article/pii/S0960148119309255. 
[159] Cabeza, L. F., Ibáñez, M., Solé, C., Roca, J., and Nogués, M., “Experimen-
tation with a water tank including a PCM module,” Solar Energy Materials 
and Solar Cells, Vol. 90, No. 9, 2006, pp. 1273–1282. https://doi.org/10.1016/ 
j.solmat.2005.08.002, URL https://www.sciencedirect.com/science/article/pii/ 
S0927024805002461. 
[160] Mehling, H., Cabeza, L. F., Hippeli, S., and Hiebler, S., “PCM-module to im-
prove hot water heat stores with stratification,” Renewable Energy, Vol. 28, 
No. 5, 2003, pp. 699–711. https://doi.org/10.1016/S0960-1481(02)00108-8, 
URL https://www.sciencedirect.com/science/article/pii/S0960148102001088. 
[161] Wang, Z., Zhang, H., Dou, B., Zhang, G., Wu, W., and Zhou, L., “An ex-
perimental study for the enhancement of stratification in heat-storage tank 
by equalizer and PCM module,” Journal of Energy Storage, Vol. 27, 2020, 
p. 101010. https://doi.org/10.1016/j.est.2019.101010, URL https://www. 
sciencedirect.com/science/article/pii/S2352152X19303718. 
[162] Long, J.-Y., and Zhu, D.-S., “Numerical and experimental study on heat 
pump water heater with PCM for thermal storage,” Energy and Build-
ings, Vol. 40, No. 4, 2008, pp. 666–672. https://doi.org/10.1016/j.enbuild. 
2007.05.001, URL https://www.sciencedirect.com/science/article/pii/ 
S0378778807001508. 
[163] da Cunha, J. P., and Eames, P., “Compact latent heat storage decarbon-
isation potential for domestic hot water and space heating applications in 
140
the UK,” Applied Thermal Engineering, Vol. 134, 2018, pp. 396–406. 
https://doi.org/10.1016/j.applthermaleng.2018.01.120, URL https://www. 
sciencedirect.com/science/article/pii/S135943111733586X. 
[164] Fadl, M., and Eames, P. C., “An experimental investigation of the heat 
transfer and energy storage characteristics of a compact latent heat thermal 
energy storage system for domestic hot water applications,” Energy, Vol. 
188, 2019, p. 116083. https://doi.org/10.1016/j.energy.2019.116083, URL 
https://www.sciencedirect.com/science/article/pii/S0360544219317785. 
[165] Gluesenkamp, K. R., and Sultan, S., “Heat Pumping Technologies Maga-
zine - The State of Art of Heat-Pump integrated Thermal Energy Storage 
for Demand Response,” 2021. https://doi.org/10.23697/62TR-NT79, 
URL https://heatpumpingtechnologies.org/publications/ 
the-state-of-art-of-heat-pump-integrated-thermal-energy-storage-for-demand-response/, 
publisher: Heat Pump Centre. 
[166] Ling, Z., Zhang, Z., Shi, G., Fang, X., Wang, L., Gao, X., Fang, Y., Xu, 
T., Wang, S., and Liu, X., “Review on thermal management systems us-
ing phase change materials for electronic components, Li-ion batteries and 
photovoltaic modules,” Renewable and Sustainable Energy Reviews, Vol. 31, 
2014, pp. 427–438. https://doi.org/10.1016/j.rser.2013.12.017, URL https: 
//www.sciencedirect.com/science/article/pii/S1364032113008319. 
[167] E. Green, C., G. Fedorov, A., and K. Joshi, Y., “Time scale matching of dy-
namically operated devices using composite thermal capacitors,” Microelec-
tronics Journal, Vol. 45, No. 8, 2014, pp. 1069–1078. https://doi.org/10.1016/ 
j.mejo.2014.05.013, URL https://www.sciencedirect.com/science/article/pii/ 
S0026269214001724. 
141
[168] Babu Sanker, S., and Baby, R., “Phase change material based thermal man-
agement of lithium ion batteries: A review on thermal performance of var-
ious thermal conductivity enhancers,” Journal of Energy Storage, Vol. 50, 
2022, p. 104606. https://doi.org/10.1016/j.est.2022.104606, URL https: 
//www.sciencedirect.com/science/article/pii/S2352152X22006223. 
[169] Mills, A., Farid, M., Selman, J. R., and Al-Hallaj, S., “Thermal conductiv-
ity enhancement of phase change materials using a graphite matrix,” Applied 
Thermal Engineering, Vol. 26, No. 14, 2006, pp. 1652–1661. https://doi.org/ 
10.1016/j.applthermaleng.2005.11.022, URL https://www.sciencedirect.com/ 
science/article/pii/S1359431105004072. 
[170] Mathew, J., and Krishnan, S., “A Review on Transient Thermal Management 
of Electronic Devices,” Journal of Electronic Packaging, Vol. 144, No. 1, 2021. 
https://doi.org/10.1115/1.4050002, URL https://doi.org/10.1115/1.4050002. 
[171] Humphries, W. R., and Griggs, E. I., “A design handbook for phase change 
thermal control and energy storage devices,” , Nov. 1977. URL https://ntrs. 
nasa.gov/citations/19780007491, nTRS Author Affiliations: NASA Marshall 
Space Flight Center NTRS Report/Patent Number: NASA-TP-1074 NTRS 
Document ID: 19780007491 NTRS Research Center: Legacy CDMS (CDMS). 
[172] Xu, J., Tarau, C., Ellis, M., and Alvarez-Hernandez, A., “Design of an Ad-
ditively Manufactured Vapor Chamber Heat Exchanger for Space Applica-
tions,” 2021 20th IEEE Intersociety Conference on Thermal and Thermome-
chanical Phenomena in Electronic Systems (iTherm), 2021, pp. 1091–1097. 
https://doi.org/10.1109/ITherm51669.2021.9503233, iSSN: 2694-2135. 
[173] Nafis, B. M., Whitt, R., Iradukunda, A.-C., and Huitink, D., “Additive Man-
ufacturing for Enhancing Thermal Dissipation in Heat Sink Implementa-
142
tion: A Review,” Heat Transfer Engineering, Vol. 42, No. 12, 2021, pp. 967– 
984. https://doi.org/10.1080/01457632.2020.1766246, URL https://doi. 
org/10.1080/01457632.2020.1766246, publisher: Taylor & Francis eprint: 
https://doi.org/10.1080/01457632.2020.1766246. 
[174] Ho, J. Y., See, Y. S., Leong, K. C., and Wong, T. N., “An experimental in-
vestigation of a PCM-based heat sink enhanced with a topology-optimized 
tree-like structure,” Energy Conversion and Management, Vol. 245, 2021, 
p. 114608. https://doi.org/10.1016/j.enconman.2021.114608, URL https: 
//www.sciencedirect.com/science/article/pii/S0196890421007846. 
[175] Zhao, Y., Zhang, X., Xu, X., and Zhang, S., “Development of composite 
phase change cold storage material and its application in vaccine cold stor-
age equipment,” Journal of Energy Storage, Vol. 30, 2020, p. 101455. 
https://doi.org/10.1016/j.est.2020.101455, URL https://www.sciencedirect. 
com/science/article/pii/S2352152X20304564. 
[176] Huang, L., and Piontek, U., “Improving Performance of Cold-Chain Insulated 
Container with Phase Change Material: An Experimental Investigation,” 
Applied Sciences, Vol. 7, No. 12, 2017, p. 1288. https://doi.org/10.3390/ 
app7121288, URL https://www.mdpi.com/2076-3417/7/12/1288, number: 
12 Publisher: Multidisciplinary Digital Publishing Institute. 
[177] Alehosseini, E., and Jafari, S. M., “Micro/nano-encapsulated phase change 
materials (PCMs) as emerging materials for the food industry,” Trends in 
Food Science & Technology, Vol. 91, 2019, pp. 116–128. https://doi.org/10. 
1016/j.tifs.2019.07.003, URL https://www.sciencedirect.com/science/article/ 
pii/S0924224418307179. 
[178] Prakash, R., Ravindra, M. R., Pushpadass, H. A., Sivaram, M., Jeyaku-
143
mar, S., and Rao, K. J., “Milk chilling using nanoparticle enhanced phase 
change material capsuled inside a jacketed cylindrical module: A numerical 
and experimental study,” Innovative Food Science & Emerging Technologies, 
Vol. 81, 2022, p. 103112. https://doi.org/10.1016/j.ifset.2022.103112, URL 
https://www.sciencedirect.com/science/article/pii/S1466856422001977. 
[179] Ma, K., Zhang, X., Ji, J., Han, L., Ding, X., and Xie, W., “Application and 
research progress of phase change materials in biomedical field,” Biomateri-
als Science, Vol. 9, No. 17, 2021, pp. 5762–5780. https://doi.org/10.1039/ 
D1BM00719J, URL https://pubs.rsc.org/en/content/articlelanding/2021/bm/ 
d1bm00719j, publisher: The Royal Society of Chemistry. 
[180] Salaün, F., Devaux, E., Bourbigot, S., and Rumeau, P., “Development of 
Phase Change Materials in Clothing Part I: Formulation of Microencapsu-
lated Phase Change,” Textile Research Journal, Vol. 80, No. 3, 2010, pp. 195– 
205. https://doi.org/10.1177/0040517509093436, URL https://doi.org/10. 
1177/0040517509093436, publisher: SAGE Publications Ltd STM. 
[181] Iqbal, K., Khan, A., Sun, D., Ashraf, M., Rehman, A., Safdar, F., Basit, A., 
and Maqsood, H. S., “Phase change materials, their synthesis and application 
in textiles—a review,” The Journal of The Textile Institute, Vol. 110, No. 4, 
2019, pp. 625–638. https://doi.org/10.1080/00405000.2018.1548088, URL 
https://doi.org/10.1080/00405000.2018.1548088, publisher: Taylor & Francis 
eprint: https://doi.org/10.1080/00405000.2018.1548088. 
[182] De Boer, R., Smeding, S. F., Bach, P. W., and De Joode, G., “Heat storage 
systems for use in an industrial batch process. (Results of) a case study,” 
2006. URL https://www.osti.gov/etdeweb/biblio/20838416. 
[183] Arie, M. A., Shooshtari, A. H., Tiwari, R., Dessiatoun, S. V., Ohadi, M. M., 
144
and Pearce, J. M., “Experimental characterization of heat transfer in an ad-
ditively manufactured polymer heat exchanger,” Applied Thermal Engineer-
ing, Vol. 113, 2017, pp. 575–584. https://doi.org/10.1016/j.applthermaleng. 
2016.11.030, URL https://www.sciencedirect.com/science/article/pii/ 
S1359431116330630. 
[184] Ma, Q., Luo, L., Wang, R. Z., and Sauce, G., “A review on transportation 
of heat energy over long distance: Exploratory development,” Renewable and 
Sustainable Energy Reviews, Vol. 13, No. 6, 2009, pp. 1532–1540. https://doi. 
org/10.1016/j.rser.2008.10.004, URL https://www.sciencedirect.com/science/ 
article/pii/S136403210800169X. 
[185] Jankowski, N. R., and McCluskey, F. P., “A review of phase change materials 
for vehicle component thermal buffering,” Applied Energy, Vol. 113, 2014, pp. 
1525–1561. https://doi.org/10.1016/j.apenergy.2013.08.026, URL https:// 
www.sciencedirect.com/science/article/pii/S0306261913006612. 
[186] Kim, K.-b., Choi, K.-w., Kim, Y.-j., Lee, K.-h., and Lee, K.-s., “Feasibil-
ity study on a novel cooling technique using a phase change material in 
an automotive engine,” Energy, Vol. 35, No. 1, 2010, pp. 478–484. https: 
//doi.org/10.1016/j.energy.2009.10.015, URL https://www.sciencedirect.com/ 
science/article/pii/S0360544209004484. 
[187] LaClair, T. J., Gao, Z., Abdelaziz, O., Wang, M., Wolfe, E., and Craig, 
T., “Thermal Storage System for Electric Vehicle Cabin Heating - Com-
ponent and System Analysis,” SAE Technical Paper 2016-01-0244, SAE 
International, Warrendale, PA, Apr. 2016. https://doi.org/10.4271/ 
2016-01-0244, URL https://www.sae.org/publications/technical-papers/ 
content/2016-01-0244/, iSSN: 0148-7191, 2688-3627. 
145
[188] Du, K., Calautit, J., Wang, Z., Wu, Y., and Liu, H., “A review of the ap-
plications of phase change materials in cooling, heating and power gen-
eration in different temperature ranges,” Applied Energy, Vol. 220, 2018, 
pp. 242–273. https://doi.org/10.1016/j.apenergy.2018.03.005, URL https: 
//www.sciencedirect.com/science/article/pii/S0306261918303349. 
[189] Liu, M., Saman, W., and Bruno, F., “Review on storage materials and 
thermal performance enhancement techniques for high temperature phase 
change thermal storage systems,” Renewable and Sustainable Energy Re-
views, Vol. 16, No. 4, 2012, pp. 2118–2132. https://doi.org/10.1016/j. 
rser.2012.01.020, URL https://www.sciencedirect.com/science/article/pii/ 
S1364032112000214. 
[190] Chauhan, V. K., Shukla, S. K., and Rathore, P. K. S., “A systematic review 
for performance augmentation of solar still with heat storage materials: A 
state of art,” Journal of Energy Storage, Vol. 47, 2022, p. 103578. https://doi. 
org/10.1016/j.est.2021.103578, URL https://www.sciencedirect.com/science/ 
article/pii/S2352152X21012573. 
[191] Ma, C., Zhang, Y., Chen, X., Song, X., and Tang, K., “Experimental Study of 
an Enhanced Phase Change Material of Paraffin/Expanded Graphite/Nano-
Metal Particles for a Personal Cooling System,” Materials, Vol. 13, No. 4, 
2020, p. 980. https://doi.org/10.3390/ma13040980, URL https://www.mdpi. 
com/1996-1944/13/4/980. 
[192] Frusteri, F., Leonardi, V., Vasta, S., and Restuccia, G., “Thermal con-
ductivity measurement of a PCM based storage system containing carbon 
fibers,” Applied Thermal Engineering, Vol. 25, No. 11, 2005, pp. 1623–1633. 
https://doi.org/10.1016/j.applthermaleng.2004.10.007, URL https://www. 
sciencedirect.com/science/article/pii/S1359431104002984. 
146
[193] Wang, J., Li, Y., Zheng, D., Mikulčić, H., Vujanović, M., and Sundén, B., 
“Preparation and thermophysical property analysis of nanocomposite phase 
change materials for energy storage,” Renewable and Sustainable Energy Re-
views, Vol. 151, 2021, p. 111541. https://doi.org/10.1016/j.rser.2021.111541, 
URL https://www.sciencedirect.com/science/article/pii/S1364032121008194. 
[194] Khademi, A., Shank, K., Mehrjardi, S. A. A., Tiari, S., Sorrentino, G., Said, 
Z., Chamkha, A. J., and Ushak, S., “A brief review on different hybrid meth-
ods of enhancement within latent heat storage systems,” Journal of Energy 
Storage, Vol. 54, 2022, p. 105362. https://doi.org/10.1016/j.est.2022.105362, 
URL https://linkinghub.elsevier.com/retrieve/pii/S2352152X22013561. 
[195] Aramesh, M., and Shabani, B., “Metal foams application to enhance the 
thermal performance of phase change materials: A review of experimen-
tal studies to understand the mechanisms,” Journal of Energy Storage, 
Vol. 50, 2022, p. 104650. https://doi.org/10.1016/j.est.2022.104650, URL 
https://www.sciencedirect.com/science/article/pii/S2352152X22006648. 
[196] Barako, M. T., Lingamneni, S., Katz, J. S., Liu, T., Goodson, K. E., and 
Tice, J., “Optimizing the design of composite phase change materials for high 
thermal power density,” Journal of Applied Physics, Vol. 124, No. 14, 2018, p. 
145103. https://doi.org/10.1063/1.5031914, URL http://aip.scitation.org/doi/ 
10.1063/1.5031914. 
[197] Yazawa, K., Shamberger, P. J., and Fisher, T. S., “Ragone Relations for 
Thermal Energy Storage Technologies,” Frontiers in Mechanical Engineer-
ing, Vol. 5, 2019, p. 29. https://doi.org/10.3389/fmech.2019.00029, URL 
https://www.frontiersin.org/article/10.3389/fmech.2019.00029/full. 
[198] Woods, J., Mahvi, A., Goyal, A., Kozubal, E., Odukomaiya, A., and Jack-
147
son, R., “Rate capability and Ragone plots for phase change thermal en-
ergy storage,” Nature Energy, Vol. 6, No. 3, 2021, pp. 295–302. https:// 
doi.org/10.1038/s41560-021-00778-w, URL http://www.nature.com/articles/ 
s41560-021-00778-w. 
[199] Boetcher, S. K. S., “Cool Thermal Energy Storage: Water and Ice to Alter-
native Phase Change Materials,” Solid-Liquid Thermal Energy Storage, CRC 
Press, 2022. Num Pages: 14. 
[200] Freeman, T. B., Spitzer, D., Currier, P. N., Rollin, V., and Boetcher, S. K., 
“Phase-Change Materials/HDPE Composite Filament: A First Step Toward 
Use With 3D Printing for Thermal Management Applications,” Journal of 
Thermal Science and Engineering Applications, Vol. 11, No. 5, 2019. https: 
//doi.org/10.1115/1.4042592, URL https://doi.org/10.1115/1.4042592. 
[201] Freeman, T. B., Messenger, M. A., Troxler, C. J., Nawaz, K., Rodriguez, 
R. M., and Boetcher, S. K., “Fused filament fabrication of novel phase-
change material functional composites,” Additive Manufacturing, Vol. 39, 
2021, p. 101839. https://doi.org/10.1016/j.addma.2021.101839, URL https: 
//linkinghub.elsevier.com/retrieve/pii/S221486042100004X. 
[202] Nawaz, K., Freeman, T. B., Rodriguez, R. M., and Boetcher, S. K. S., “Mois-
ture affinity of HDPE/phase-change material composites for thermal en-
ergy storage applications,” RSC Advances, Vol. 11, No. 49, 2021, pp. 30569– 
30573. https://doi.org/10.1039/D1RA03618A, URL https://pubs.rsc.org/en/ 
content/articlelanding/2021/ra/d1ra03618a, publisher: The Royal Society of 
Chemistry. 
[203] Freeman, T. B., Nabutola, K., Spitzer, D., Currier, P. N., and Boetcher, 
S. K. S., “3D-Printed PCM/HDPE Composites for Battery Thermal Man-
148
agement,” Volume 8B: Heat Transfer and Thermal Engineering, American 
Society of Mechanical Engineers, Pittsburgh, Pennsylvania, USA, 2018, p. 
V08BT10A041. https://doi.org/10.1115/IMECE2018-86081, URL https: 
//asmedigitalcollection.asme.org/IMECE/proceedings/IMECE2018/52125/ 
Pittsburgh,%20Pennsylvania,%20USA/275475. 
[204] Singh, P., Odukomaiya, A., Smith, M. K., Aday, A., Cui, S., and Mahvi, A., 
“Processing of phase change materials by fused deposition modeling: Toward 
efficient thermal energy storage designs,” Journal of Energy Storage, Vol. 55, 
2022, p. 105581. https://doi.org/10.1016/j.est.2022.105581, URL https:// 
linkinghub.elsevier.com/retrieve/pii/S2352152X22015699. 
[205] Freeman, T. B., Nawaz, K., Rodriguez, R. M., Boetcher, S. K. S., and Mang-
lik, R. M., “Additively Manufactured Polymer- Encapsulated Phase-Change 
Material Heat Exchangers for Residential Thermal Energy Storage,” 2021 
ASHRAE Annual Conference, 2021, pp. 400–408. 
[206] Moon, H., Miljkovic, N., and King, W. P., “High power density thermal en-
ergy storage using additively manufactured heat exchangers and phase change 
material,” International Journal of Heat and Mass Transfer, Vol. 153, 2020, 
p. 119591. https://doi.org/10.1016/j.ijheatmasstransfer.2020.119591, URL 
https://www.sciencedirect.com/science/article/pii/S0017931019359526. 
[207] Ma, J., Ma, T., Cheng, J., and Zhang, J., “Polymer Encapsulation Strategy 
toward 3D Printable, Sustainable, and Reliable Form-Stable Phase Change 
Materials for Advanced Thermal Energy Storage,” ACS Applied Materials 
& Interfaces, Vol. 14, No. 3, 2022, pp. 4251–4264. https://doi.org/10.1021/ 
acsami.1c23972, URL https://pubs.acs.org/doi/10.1021/acsami.1c23972. 
[208] Nofal, M., Pan, Y., and Al-Hallaj, S., “Selective Laser Sintering of Phase 
149
Change Materials for Thermal Energy Storage Applications,” Procedia Manu-
facturing, Vol. 10, 2017, pp. 851–865. https://doi.org/10.1016/j.promfg.2017. 
07.071, URL https://linkinghub.elsevier.com/retrieve/pii/S2351978917302536. 
[209] Nofal, M., Al-Hallaj, S., and Pan, Y., “Experimental investigation of phase 
change materials fabricated using selective laser sintering additive manufac-
turing,” Journal of Manufacturing Processes, Vol. 44, 2019, pp. 91–101. https: 
//doi.org/10.1016/j.jmapro.2019.05.043, URL https://www.sciencedirect. 
com/science/article/pii/S1526612518302196. 
[210] Nofal, M., Al-Hallaj, S., and Pan, Y., “Thermal management of lithium-
ion battery cells using 3D printed phase change composites,” Applied Ther-
mal Engineering, Vol. 171, 2020, p. 115126. https://doi.org/10.1016/j. 
applthermaleng.2020.115126, URL https://www.sciencedirect.com/science/ 
article/pii/S1359431119323956. 
[211] Wei, P., Cipriani, C. E., and Pentzer, E. B., “Thermal energy regulation with 
3D printed polymer-phase change material composites,” Matter, Vol. 4, No. 6, 
2021, pp. 1975–1989. https://doi.org/10.1016/j.matt.2021.03.019, URL https: 
//www.sciencedirect.com/science/article/pii/S2590238521001260. 
[212] Hatakenaka, R., Sugita, H., Kinjo, T., Saitoh, M., and Yamamoto, T., “Heat-
transfer Characteristics of a Light-weight, Fin- integrated PCM Unit manu-
factured by Additive Manufacturing,” 2017, p. 11. 
[213] Wild, D., Schrezenmeier, J., Czupalla, M., and Förstner, M., “Thermal Char-
acterization of additive manufactured Integral Structures for Phase Change 
Applications,” 2020. URL https://ttu-ir.tdl.org/handle/2346/86394. 
[214] Zhang, Y., Ma, G., Wang, J., Liu, S., and Kang, S., “Numerical and exper-
imental study of phase-change temperature controller containing graded 
150
cellular material fabricated by additive manufacturing,” Applied Thermal 
Engineering, Vol. 150, 2019, pp. 1297–1305. https://doi.org/10.1016/j. 
applthermaleng.2019.01.066, URL https://linkinghub.elsevier.com/retrieve/ 
pii/S135943111835141X. 
[215] Cao, M., Huang, J., and Liu, Z., “The Enhanced Performance of Phase-
Change Materials via 3D Printing with Prickly Aluminum Honeycomb for 
Thermal Management of Ternary Lithium Batteries,” Advances in Materi-
als Science and Engineering, Vol. 2020, 2020, pp. 1–11. https://doi.org/10. 
1155/2020/8167386, URL https://www.hindawi.com/journals/amse/2020/ 
8167386/. 
[216] Hirano, S., and Kawanami, T., “Thermal Characteristics and Development 
of a Phase Change Material for Thermal Energy Storage Media as Thermo-
Functional Fluids,” Tetsu-to-Hagane, Vol. 106, No. 8, 2020, pp. 581–590. 
https://doi.org/10.2355/tetsutohagane.TETSU-2019-127, URL https://www. 
jstage.jst.go.jp/article/tetsutohagane/106/8/106 TETSU-2019-127/ article/ 
-char/ja/. 
[217] Qureshi, Z. A., Al-Omari, S. A. B., Elnajjar, E., Al-Ketan, O., and Abu Al-
Rub, R., “Nature-inspired triply periodic minimal surface-based structures in 
sheet and solid configurations for performance enhancement of a low-thermal-
conductivity phase-change material for latent-heat thermal-energy-storage 
applications,” International Journal of Thermal Sciences, Vol. 173, 2022, p. 
107361. https://doi.org/10.1016/j.ijthermalsci.2021.107361, URL https:// 
linkinghub.elsevier.com/retrieve/pii/S1290072921005184. 
[218] Dong, Y., Wang, F., Zhang, Y., Shi, X., Zhang, A., and Shuai, Y., “Experi-
mental and numerical study on flow characteristic and thermal performance 
of macro-capsules phase change material with biomimetic oval structure,” En-
151
ergy, Vol. 238, 2022, p. 121830. https://doi.org/10.1016/j.energy.2021.121830, 
URL https://linkinghub.elsevier.com/retrieve/pii/S0360544221020788. 
[219] Zhou, H., Zhang, X., Zeng, H., Yang, H., Lei, H., Li, X., and Wang, Y., 
“Lightweight structure of a phase-change thermal controller based on lat-
tice cells manufactured by SLM,” Chinese Journal of Aeronautics, Vol. 32, 
No. 7, 2019, pp. 1727–1732. https://doi.org/10.1016/j.cja.2018.08.017, URL 
https://linkinghub.elsevier.com/retrieve/pii/S1000936118302851. 
[220] Tamraparni, A., Hoe, A., Deckard, M., Zhang, C., Elwany, A., Shamberger, 
P. J., and Felts, J. R., “Experimental Validation of Composite Phase Change 
Material Optimized for Thermal Energy Storage,” 2021 20th IEEE Interso-
ciety Conference on Thermal and Thermomechanical Phenomena in Elec-
tronic Systems (iTherm), IEEE, San Diego, CA, USA, 2021, pp. 551–555. 
https://doi.org/10.1109/ITherm51669.2021.9503204, URL https://ieeexplore. 
ieee.org/document/9503204/. 
[221] Tamraparni, A., Hoe, A., Deckard, M., Zhang, C., Malone, N., Elwany, A., 
Shamberger, P. J., and Felts, J., “Design and Optimization of Composite 
Phase Change Material for Cylindrical Thermal Energy Storage,” SSRN 
Electronic Journal, 2022. https://doi.org/10.2139/ssrn.4172028, URL 
https://www.ssrn.com/abstract=4172028. 
[222] Guo, Y., Yang, H., Fu, W., Bai, L., and Miao, J., “Temperature control of 
star sensor baffle using 3D printing and PCM thermal energy storage tech-
nology,” International Journal of Heat and Mass Transfer, Vol. 165, 2021, 
p. 120644. https://doi.org/10.1016/j.ijheatmasstransfer.2020.120644, URL 
https://linkinghub.elsevier.com/retrieve/pii/S0017931020335808. 
[223] Yang, Z., Jia, S., Niu, Y., Lv, X., Fu, H., Zhang, Y., Liu, D., Wang, B., and 
152
Li, Q., “Bean-Pod-Inspired 3D-Printed Phase Change Microlattices for Solar-
Thermal Energy Harvesting and Storage,” Small, Vol. 17, No. 30, 2021, p. 
2101093. https://doi.org/10.1002/smll.202101093, URL https://onlinelibrary. 
wiley.com/doi/10.1002/smll.202101093. 
[224] Wang, C., and Liu, C., “Additive Manufacturing of Shape-Stabilized Compos-
ite Phase Change Materials Via Ultraviolet Curing,” SSRN Electronic Jour-
nal, 2022. https://doi.org/10.2139/ssrn.4173655, URL https://www.ssrn.com/ 
abstract=4173655. 
[225] Yang, Z., Ma, Y., Jia, S., Zhang, C., Li, P., Zhang, Y., and Li, Q., “3D-
Printed Flexible Phase-Change Nonwoven Fabrics toward Multifunctional 
Clothing,” ACS Applied Materials & Interfaces, Vol. 14, No. 5, 2022, pp. 
7283–7291. https://doi.org/10.1021/acsami.1c21778, URL https://pubs.acs. 
org/doi/10.1021/acsami.1c21778. 
[226] Yang, W., Zhou, F., Chen, X., and Zhang, Y., “Performance analysis of axial 
air cooling system with shark-skin bionic structure containing phase change 
material,” Energy Conversion and Management, Vol. 250, 2021, p. 114921. 
https://doi.org/10.1016/j.enconman.2021.114921, URL https://linkinghub. 
elsevier.com/retrieve/pii/S0196890421010979. 
[227] Yazdani, M. R., Laitinen, A., Helaakoski, V., Farnas, L. K., Kukko, K., Saari, 
K., and Vuorinen, V., “Efficient storage and recovery of waste heat by phase 
change material embedded within additively manufactured grid heat ex-
changers,” International Journal of Heat and Mass Transfer, Vol. 181, 2021, 
p. 121846. https://doi.org/10.1016/j.ijheatmasstransfer.2021.121846, URL 
https://www.sciencedirect.com/science/article/pii/S0017931021009510. 
[228] Vargas, A., Huitink, D., Iradukunda, A.-C., and Eddy, C., “Topology Opti-
153
mized Phase Change Material Integrated Heat sinks and Validation,” 2020 
19th IEEE Intersociety Conference on Thermal and Thermomechanical Phe-
nomena in Electronic Systems (ITherm), IEEE, Orlando, FL, USA, 2020, 
pp. 703–707. https://doi.org/10.1109/ITherm45881.2020.9190539, URL 
https://ieeexplore.ieee.org/document/9190539/. 
[229] Iradukunda, A.-C., “Transient thermal performance using phase change mate-
rial integrated topology optimized heat sinks,” Applied Thermal Engineering, 
2020, p. 8. https://doi.org/https://doi.org/10.1016/j.applthermaleng.2020. 
115723. 
[230] Gasca-Tirado, J., Manzano-Ramı́rez, A., Velázquez-Castillo, R. R., Gómez-
Luna, B., Nava-Mendoza, R., López-Romero, J., Apátiga-Castro, L. M., 
and Rivera-Muñoz, E. M., “Porous geopolymer as a possible template for a 
phase change material,” Materials Chemistry and Physics, Vol. 236, 2019, 
p. 121785. https://doi.org/10.1016/j.matchemphys.2019.121785, URL 
https://linkinghub.elsevier.com/retrieve/pii/S0254058419305759. 
[231] Gogoi, P., Li, Z., Guo, Z., Khuje, S., An, L., Hu, Y., Chang, S., Zhou, C., and 
Ren, S., “Ductile cooling phase change material,” Nanoscale Advances, Vol. 2, 
No. 9, 2020, pp. 3900–3905. https://doi.org/10.1039/D0NA00465K, URL 
https://pubs.rsc.org/en/content/articlelanding/2020/na/d0na00465k, pub-
lisher: RSC. 
[232] Righetti, G., Doretti, L., Zilio, C., Longo, G. A., and Mancin, S., “Experi-
mental investigation of phase change of medium/high temperature paraffin 
wax embedded in 3D periodic structure,” International Journal of Thermoflu-
ids, Vol. 5-6, 2020, p. 100035. https://doi.org/10.1016/j.ijft.2020.100035, URL 
https://linkinghub.elsevier.com/retrieve/pii/S2666202720300227. 
154
[233] Salgado-Pizarro, R., Padilla, J. A., Xuriguera, E., Barreneche, C., and 
Fernández, A. I., “Novel Shape-Stabilized Phase Change Material with Cas-
cade Character: Synthesis, Performance and Shaping Evaluation,” Energies, 
Vol. 14, No. 9, 2021, p. 2621. https://doi.org/10.3390/en14092621, URL 
https://www.mdpi.com/1996-1073/14/9/2621. 
[234] Ayat, S., Daguse, B., and Khazaka, R., “Design Considerations of Windings 
formed with Hollow Conductors Cooled with Phase Change Material,” 2019 
IEEE Energy Conversion Congress and Exposition (ECCE), IEEE, Balti-
more, MD, USA, 2019, pp. 5652–5658. https://doi.org/10.1109/ECCE.2019. 
8912762, URL https://ieeexplore.ieee.org/document/8912762/. 
[235] ElIdi, M., Karkri, M., AbdouTankari, M., and Vincent, S., “Hybrid cooling 
based battery thermal management using composite phase change materials 
and forced convection,” Journal of Energy Storage, Vol. 41, 2021, p. 102946. 
https://doi.org/10.1016/j.est.2021.102946, URL https://linkinghub.elsevier. 
com/retrieve/pii/S2352152X21006629. 
[236] Righetti, G., Zilio, C., Doretti, L., Longo, G. A., and Mancin, S., “On the 
design of Phase Change Materials based thermal management systems 
for electronics cooling,” Applied Thermal Engineering, Vol. 196, 2021, p. 
117276. https://doi.org/10.1016/j.applthermaleng.2021.117276, URL https: 
//linkinghub.elsevier.com/retrieve/pii/S1359431121007122. 
[237] Ge, R., “Additive manufacturing of a topology-optimised multi-tube energy 
storage device Experimental tests and numerical analysis,” Applied Ther-
mal Engineering, 2020, p. 12. https://doi.org/https://doi.org/10.1016/j. 
applthermaleng.2020.115878. 
[238] Qureshi, Z. A., Al Omari, S. A. B., Elnajjar, E., Mahmoud, F., Al-Ketan, O., 
155
and Al-Rub, R. A., “Thermal characterization of 3D-Printed lattices based 
on triply periodic minimal surfaces embedded with organic phase change 
material,” Case Studies in Thermal Engineering, Vol. 27, 2021, p. 101315. 
https://doi.org/10.1016/j.csite.2021.101315, URL https://www.sciencedirect. 
com/science/article/pii/S2214157X21004780. 
[239] Almonti, D., Mingione, E., Tagliaferri, V., and Ucciardello, N., “Design and 
analysis of compound structures integrated with bio-based phase change 
materials and lattices obtained through additive manufacturing,” The In-
ternational Journal of Advanced Manufacturing Technology, Vol. 119, No. 
1-2, 2022, pp. 149–161. https://doi.org/10.1007/s00170-021-08110-2, URL 
https://link.springer.com/10.1007/s00170-021-08110-2. 
[240] Dudon, J. P., Bosse, J., Atinsounon, P., Raynaud, M., Valentini, D., Ferrier, 
M., and Blanc, G., “Optimized Phase Change Material Module for Thermal 
Regulation of Cycled Dissipative Units,” 49th International Conference on 
Environmental Systems, 2019, p. 17. 
[241] Kumar, N., and Banerjee, D., “Experimental Validation of Numerical Predic-
tions for the Transient Performance of a Simple Latent Heat Storage Unit 
(LHSU) Utilizing Phase Change Material (PCM) and 3-D Printing,” Vol-
ume 1: Aerospace Heat Transfer; Computational Heat Transfer; Education; 
Environmental Heat Transfer; Fire and Combustion Systems; Gas Turbine 
Heat Transfer; Heat Transfer in Electronic Equipment; Heat Transfer in En-
ergy Systems, American Society of Mechanical Engineers, Bellevue, Washing-
ton, USA, 2017, p. V001T09A017. https://doi.org/10.1115/HT2017-5045, 
URL https://asmedigitalcollection.asme.org/HT/proceedings/HT2017/57885/ 
Bellevue,%20Washington,%20USA/289358. 
[242] Kabir, M., Gemeda, T., Preller, E., and Xu, J., “Design and Development 
156
of a PCM-Based Two-Phase Heat Exchanger Manufactured Additively for 
Spacecraft Thermal Management Systems,” International Journal of Heat 
and Mass Transfer, Vol. 180, 2021, p. 121782. https://doi.org/10.1016/j. 
ijheatmasstransfer.2021.121782, URL https://www.sciencedirect.com/science/ 
article/pii/S0017931021008875. 
[243] Hu, X., and Gong, X., “Experimental study on the thermal response of 
PCM-based heat sink using structured porous material fabricated by 3D 
printing,” Case Studies in Thermal Engineering, Vol. 24, 2021, p. 100844. 
https://doi.org/10.1016/j.csite.2021.100844, URL https://linkinghub.elsevier. 
com/retrieve/pii/S2214157X21000071. 
[244] Ge, R., Li, Q., Li, C., and Liu, Q., “Evaluation of different melting perfor-
mance enhancement structures in a shell-and-tube latent heat thermal en-
ergy storage system,” Renewable Energy, Vol. 187, 2022, pp. 829–843. https: 
//doi.org/10.1016/j.renene.2022.01.097, URL https://linkinghub.elsevier.com/ 
retrieve/pii/S0960148122001082. 
[245] Hu, X., and Gong, X., “Experimental and numerical investigation on thermal 
performance enhancement of phase change material embedding porous metal 
structure with cubic cell,” Applied Thermal Engineering, Vol. 175, 2020, p. 
115337. https://doi.org/10.1016/j.applthermaleng.2020.115337, URL https: 
//linkinghub.elsevier.com/retrieve/pii/S1359431119384388. 
[246] Diani, A., Moro, L., and Rossetto, L., “Melting of Paraffin Waxes Embed-
ded in a Porous Matrix Made by Additive Manufacturing,” Applied Sciences, 
Vol. 11, No. 12, 2021, p. 5396. https://doi.org/10.3390/app11125396, URL 
https://www.mdpi.com/2076-3417/11/12/5396. 
[247] Righetti, G., “Experimental study of phase change material (PCM) embedded 
157
in 3D periodic structures realized via additive manufacturing,” International 
Journal of Thermal Sciences, 2020, p. 12. https://doi.org/https://doi.org/10. 
1016/j.ijthermalsci.2020.106376. 
[248] Sharma, S., Micheli, L., Chang, W., Tahir, A., Reddy, K., and Mallick, T., 
“Nano-enhanced Phase Change Material for thermal management of BICPV,” 
Applied Energy, Vol. 208, 2017, pp. 719–733. https://doi.org/10.1016/j. 
apenergy.2017.09.076, URL https://linkinghub.elsevier.com/retrieve/pii/ 
S0306261917313582. 
[249] Rigotti, D., Dorigato, A., and Pegoretti, A., “3D printable thermoplastic 
polyurethane blends with thermal energy storage/release capabilities,” Mate-
rials Today Communications, Vol. 15, 2018, pp. 228–235. https://doi.org/10. 
1016/j.mtcomm.2018.03.009, URL https://linkinghub.elsevier.com/retrieve/ 
pii/S2352492818300606. 
[250] Sharar, D. J., Wilson, A. A., Leff, A., Smith, A., Atli, K. C., Elwany, A., Ar-
royave, R., and Karaman, I., “Additively Manufacturing Nitinol as a Solid-
State Phase Change Material,” 2020 19th IEEE Intersociety Conference on 
Thermal and Thermomechanical Phenomena in Electronic Systems (ITherm), 
IEEE, Orlando, FL, USA, 2020, pp. 821–826. https://doi.org/10.1109/ 
ITherm45881.2020.9190336, URL https://ieeexplore.ieee.org/document/ 
9190336/. 
[251] Confalonieri, C., and Gariboldi, E., “Al-Sn Miscibility Gap Alloy produced by 
Power Bed Laser Melting for application as Phase Change Material,” Jour-
nal of Alloys and Compounds, Vol. 881, 2021, p. 160596. https://doi.org/10. 
1016/j.jallcom.2021.160596, URL https://linkinghub.elsevier.com/retrieve/ 
pii/S0925838821020053. 
158
[252] Ma, J., Ma, T., Cheng, J., and Zhang, J., “3D Printable, Recyclable and Ad-
justable Comb/Bottlebrush Phase Change Polysiloxane Networks toward Sus-
tainable Thermal Energy Storage,” Energy Storage Materials, Vol. 39, 2021, 
p. 11. https://doi.org/doi.org/10.1016/j.ensm.2021.04.033. 
[253] Wilts, E. M., “Structure-Property-Processing Relationships Between Poly-
meric Solutions and Additive Manufacturing for Biomedical Applications,” 
Ph.D. thesis, Virginia Polytechnic Institute, Blacksburg, VA, Sep. 2020. 
[254] Mao, Y., Miyazaki, T., Sakai, K., Gong, J., Zhu, M., and Ito, H., “A 3D 
Printable Thermal Energy Storage Crystalline Gel Using Mask-Projection 
Stereolithography,” Polymers, Vol. 10, No. 10, 2018, p. 1117. https://doi.org/ 
10.3390/polym10101117, URL https://www.ncbi.nlm.nih.gov/pmc/articles/ 
PMC6404010/. 
[255] Kiziroglou, M. E., Becker, T., Wright, S. W., Yeatman, E. M., Evans, J. W., 
and Wright, P. K., “Three-Dimensional Printed Insulation For Dynamic Ther-
moelectric Harvesters With Encapsulated Phase Change Materials,” IEEE 
Sensors Letters, Vol. 1, No. 4, 2017, pp. 1–4. https://doi.org/10.1109/LSENS. 
2017.2720960, URL http://ieeexplore.ieee.org/document/7961248/. 
[256] Saadi, M. A. S. R., Maguire, A., Pottackal, N. T., Thakur, M. S. H., Ikram, 
M. M., Hart, A. J., Ajayan, P. M., and Rahman, M. M., “Direct Ink Writ-
ing: A 3D Printing Technology for Diverse Materials,” Advanced Materials, 
Vol. 34, No. 28, 2022, p. 2108855. https://doi.org/10.1002/adma.202108855, 
URL https://onlinelibrary.wiley.com/doi/10.1002/adma.202108855. 
[257] Hao, L., Xiao, J., Sun, J., Xia, B., and Cao, W., “Thermal conductivity of 3D 
printed concrete with recycled fine aggregate composite phase change ma-
terials,” Journal of Cleaner Production, Vol. 364, 2022, p. 132598. https: 
159
//doi.org/10.1016/j.jclepro.2022.132598, URL https://linkinghub.elsevier. 
com/retrieve/pii/S0959652622021977. 
[258] Cui, H., Yu, S., Cao, X., and Yang, H., “Evaluation of Printability and Ther-
mal Properties of 3D Printed Concrete Mixed with Phase Change Materials,” 
Energies, Vol. 15, No. 6, 2022, p. 1978. https://doi.org/10.3390/en15061978, 
URL https://www.mdpi.com/1996-1073/15/6/1978. 
[259] Wu, Z., Xu, Y., and Šavija, B., “Mechanical Properties of Lightweight Ce-
mentitious Cellular Composites Incorporating Micro-Encapsulated Phase 
Change Material,” 2021, p. 24. 
[260] Wei, C., and Dong, J., “Development and Modeling of Melt 
Electrohydrodynamic-Jet Printing of Phase-Change Inks for High-Resolution 
Additive Manufacturing,” Journal of Manufacturing Science and Engineering, 
Vol. 136, No. 6, 2014, p. 061010. https://doi.org/10.1115/1.4028483, URL 
https://asmedigitalcollection.asme.org/manufacturingscience/article/doi/10. 
1115/1.4028483/377619/Development-and-Modeling-of-Melt. 
[261] Han, Y., Wei, C., and Dong, J., “Droplet formation and settlement of phase-
change ink in high resolution electrohydrodynamic (EHD) 3D printing,” 
Journal of Manufacturing Processes, Vol. 20, 2015, pp. 485–491. https: 
//doi.org/10.1016/j.jmapro.2015.06.019, URL https://www.sciencedirect. 
com/science/article/pii/S152661251500064X. 
[262] Hubert, R., Bou Matar, O., Foncin, J., Coquet, P., Tan, D., Li, H., Teo, E. 
H. T., Merlet, T., and Pernod, P., “An effective thermal conductivity model 
for architected phase change material enhancer: Theoretical and experimental 
investigations,” International Journal of Heat and Mass Transfer, Vol. 176, 
160
2021, p. 121364. https://doi.org/10.1016/j.ijheatmasstransfer.2021.121364, 
URL https://linkinghub.elsevier.com/retrieve/pii/S0017931021004671. 
[263] Diani, A., Nonino, C., and Rossetto, L., “Melting of phase change mate-
rials inside periodic cellular structures fabricated by additive manufac-
turing: Experimental results and numerical simulations,” Applied Ther-
mal Engineering, Vol. 215, 2022, p. 118969. https://doi.org/10.1016/j. 
applthermaleng.2022.118969, URL https://linkinghub.elsevier.com/retrieve/ 
pii/S1359431122009073. 
[264] Han, Z., and Fina, A., “Thermal conductivity of carbon nanotubes and their 
polymer nanocomposites: A review,” Progress in Polymer Science, Vol. 36, 
No. 7, 2011, pp. 914–944. https://doi.org/10.1016/j.progpolymsci.2010.11.004, 
URL https://www.sciencedirect.com/science/article/pii/S0079670010001243. 
[265] Shemelya, C., De La Rosa, A., Torrado, A. R., Yu, K., Domanowski, J., 
Bonacuse, P. J., Martin, R. E., Juhasz, M., Hurwitz, F., Wicker, R. B., Con-
ner, B., MacDonald, E., and Roberson, D. A., “Anisotropy of thermal con-
ductivity in 3D printed polymer matrix composites for space based cube 
satellites,” Additive Manufacturing, Vol. 16, 2017, pp. 186–196. https: 
//doi.org/10.1016/j.addma.2017.05.012, URL https://www.sciencedirect.com/ 
science/article/pii/S2214860417302324. 
[266] Chen, J., Liu, X., Tian, Y., Zhu, W., Yan, C., Shi, Y., Kong, L. B., 
Qi, H. J., and Zhou, K., “3D-Printed Anisotropic Polymer Materials 
for Functional Applications,” Advanced Materials, Vol. 34, No. 5, 2022, 
p. 2102877. https://doi.org/10.1002/adma.202102877, URL https: 
//onlinelibrary.wiley.com/doi/abs/10.1002/adma.202102877, eprint: 
https://onlinelibrary.wiley.com/doi/pdf/10.1002/adma.202102877. 
161
[267] Ibrahim, Y., Elkholy, A., Schofield, J. S., Melenka, G. W., and Kempers, R., 
“Effective thermal conductivity of 3D-printed continuous fiber polymer com-
posites,” Advanced Manufacturing: Polymer & Composites Science, Vol. 6, 
No. 1, 2020, pp. 17–28. https://doi.org/10.1080/20550340.2019.1710023, URL 
https://doi.org/10.1080/20550340.2019.1710023, publisher: Taylor & Francis 
eprint: https://doi.org/10.1080/20550340.2019.1710023. 
[268] Jäger, A., Johannesmann, S., Claes, L., Webersen, M., Henning, B., and Kup-
nik, M., “Evaluating the influence of 3D-printing parameters on acoustic ma-
terial properties,” 2017 IEEE International Ultrasonics Symposium (IUS), 
2017, pp. 1–4. https://doi.org/10.1109/ULTSYM.2017.8092398, iSSN: 1948-
5727. 
[269] Manoj Prabhakar, M., Saravanan, A. K., Haiter Lenin, A., Jerin leno, I., 
Mayandi, K., and Sethu Ramalingam, P., “A short review on 3D printing 
methods, process parameters and materials,” Materials Today: Proceedings, 
Vol. 45, 2021, pp. 6108–6114. https://doi.org/10.1016/j.matpr.2020.10.225, 
URL https://www.sciencedirect.com/science/article/pii/S2214785320378317. 
[270] Delfs, P., Tows, M., and Schmid, H. J., “Optimized build orientation of ad-
ditive manufactured parts for improved surface quality and build time,” Ad-
ditive Manufacturing, Vol. 12, 2016, pp. 314–320. https://doi.org/10.1016/j. 
addma.2016.06.003, URL https://www.sciencedirect.com/science/article/pii/ 
S2214860416301142. 
[271] Arnold, C., Monsees, D., Hey, J., and Schweyen, R., “Surface Quality of 3D-
Printed Models as a Function of Various Printing Parameters,” Materials, 
Vol. 12, No. 12, 2019, p. 1970. https://doi.org/10.3390/ma12121970, URL 
https://www.mdpi.com/1996-1944/12/12/1970, number: 12 Publisher: Multi-
disciplinary Digital Publishing Institute. 
162
[272] Wang, Z., Liu, P., Xiao, Y., Cui, X., Hu, Z., and Chen, L., “A Data-Driven 
Approach for Process Optimization of Metallic Additive Manufacturing Under 
Uncertainty,” Journal of Manufacturing Science and Engineering, Vol. 141, 
No. 8, 2019. https://doi.org/10.1115/1.4043798, URL https://doi.org/10. 
1115/1.4043798. 
[273] Almuallim, B., Harun, W. S. W., Al Rikabi, I. J., and Mohammed, H. A., 
“Thermally conductive polymer nanocomposites for filament-based additive 
manufacturing,” Journal of Materials Science, Vol. 57, No. 6, 2022, pp. 3993– 
4019. https://doi.org/10.1007/s10853-021-06820-2, URL https://doi.org/10. 
1007/s10853-021-06820-2. 
[274] Nguyen, T. K., and Lee, B.-K., “Post-processing of FDM parts to improve 
surface and thermal properties,” Rapid Prototyping Journal, Vol. 24, No. 7, 
2018, pp. 1091–1100. https://doi.org/10.1108/RPJ-12-2016-0207, URL https: 
//doi.org/10.1108/RPJ-12-2016-0207, publisher: Emerald Publishing Limited. 
[275] Prajapati, H., Ravoori, D., Woods, R. L., and Jain, A., “Measurement of 
anisotropic thermal conductivity and inter-layer thermal contact resistance 
in polymer fused deposition modeling (FDM),” Additive Manufacturing, 
Vol. 21, 2018, pp. 84–90. https://doi.org/10.1016/j.addma.2018.02.019, URL 
https://www.sciencedirect.com/science/article/pii/S2214860417305456. 
[276] Ravoori, D., Alba, L., Prajapati, H., and Jain, A., “Investigation of process-
structure-property relationships in polymer extrusion based additive man-
ufacturing through in situ high speed imaging and thermal conductivity 
measurements,” Additive Manufacturing, Vol. 23, 2018, pp. 132–139. https: 
//doi.org/10.1016/j.addma.2018.07.011, URL https://www.sciencedirect.com/ 
science/article/pii/S2214860418301210. 
163
[277] Prajapati, H., Chalise, D., Ravoori, D., Taylor, R. M., and Jain, A., “Im-
provement in build-direction thermal conductivity in extrusion-based polymer 
additive manufacturing through thermal annealing,” Additive Manufactur-
ing, Vol. 26, 2019, pp. 242–249. https://doi.org/10.1016/j.addma.2019.01.004, 
URL https://www.sciencedirect.com/science/article/pii/S2214860418308716. 
[278] Raza, G., Shi, Y., and Deng, Y., “Expanded graphite as thermal conductiv-
ity enhancer for paraffin wax being used in thermal energy storage systems,” 
2016 13th International Bhurban Conference on Applied Sciences and Tech-
nology (IBCAST), 2016, pp. 1–12. https://doi.org/10.1109/IBCAST.2016. 
7429846, iSSN: 2151-1411. 
[279] Huang, X., Jiang, P., and Tanaka, T., “A review of dielectric polymer com-
posites with high thermal conductivity,” IEEE Electrical Insulation Magazine, 
Vol. 27, No. 4, 2011, pp. 8–16. https://doi.org/10.1109/MEI.2011.5954064, 
conference Name: IEEE Electrical Insulation Magazine. 
[280] Wencke, Y. L., Kutlu, Y., Seefeldt, M., Esen, C., Ostendorf, A., and Luinstra, 
G. A., “Additive manufacturing of PA12 carbon nanotube composites with 
a novel laser polymer deposition process,” Journal of Applied Polymer Sci-
ence, Vol. 138, No. 19, 2021, p. 50395. https://doi.org/10.1002/app.50395, 
URL https://onlinelibrary.wiley.com/doi/abs/10.1002/app.50395, eprint: 
https://onlinelibrary.wiley.com/doi/pdf/10.1002/app.50395. 
[281] Tekinalp, H. L., Kunc, V., Velez-Garcia, G. M., Duty, C. E., Love, L. J., 
Naskar, A. K., Blue, C. A., and Ozcan, S., “Highly oriented carbon 
fiber–polymer composites via additive manufacturing,” Composites Sci-
ence and Technology, Vol. 105, 2014, pp. 144–150. https://doi.org/10.1016/ 
j.compscitech.2014.10.009, URL https://www.sciencedirect.com/science/ 
article/pii/S0266353814003716. 
164
[282] Caminero, M. , Chacón, J. M., Garćıa-Plaza, E., Núñez, P. J., Reverte, J. M., 
and Becar, J. P., “Additive Manufacturing of PLA-Based Composites Using 
Fused Filament Fabrication: Effect of Graphene Nanoplatelet Reinforcement 
on Mechanical Properties, Dimensional Accuracy and Texture,” Polymers, 
Vol. 11, No. 5, 2019, p. 799. https://doi.org/10.3390/polym11050799, URL 
https://www.mdpi.com/2073-4360/11/5/799, number: 5 Publisher: Multidis-
ciplinary Digital Publishing Institute. 
[283] “Carbon Black - Materials Handled - Flexicon Corporation,” , ????. URL 
https://www.flexicon.com/Materials-Handled/Carbon-Black.html. 
[284] Elements, A., “Carbon Nanotubes,” , ???? URL https://www. 
americanelements.com/carbon-nanotubes-308068-56-6. 
[285] Karaipekli, A., Sarı, A., and Kaygusuz, K., “Thermal conductivity improve-
ment of stearic acid using expanded graphite and carbon fiber for energy 
storage applications,” Renewable Energy, Vol. 32, No. 13, 2007, pp. 2201– 
2210. https://doi.org/10.1016/j.renene.2006.11.011, URL https://www. 
sciencedirect.com/science/article/pii/S0960148106003351. 
[286] Kumanek, B., and Janas, D., “Thermal conductivity of carbon nanotube 
networks: a review,” Journal of Materials Science, Vol. 54, No. 10, 2019, 
pp. 7397–7427. https://doi.org/10.1007/s10853-019-03368-0, URL https: 
//doi.org/10.1007/s10853-019-03368-0. 
[287] Colla, L., Fedele, L., Mancin, S., Danza, L., and Manca, O., “Nano-PCMs 
for enhanced energy storage and passive cooling applications,” Applied Ther-
mal Engineering, Vol. 110, 2017, pp. 584–589. https://doi.org/10.1016/j. 
applthermaleng.2016.03.161, URL https://www.sciencedirect.com/science/ 
article/pii/S1359431116304707. 
165
[288] Liao, G., Li, Z., Cheng, Y., Xu, D., Zhu, D., Jiang, S., Guo, J., Chen, X., Xu, 
G., and Zhu, Y., “Properties of oriented carbon fiber/polyamide 12 composite 
parts fabricated by fused deposition modeling,” Materials & Design, Vol. 139, 
2018, pp. 283–292. https://doi.org/10.1016/j.matdes.2017.11.027, URL https: 
//www.sciencedirect.com/science/article/pii/S0264127517310584. 
[289] Wang, F., Yang, Z., Hu, X., Pan, Y., Lu, Y., and Jiang, M., “Coaxial 3D 
printed anisotropic thermal conductive composite aerogel with aligned hier-
archical porous carbon nanotubes and cellulose nanofibers,” Smart Materi-
als and Structures, Vol. 31, No. 4, 2022, p. 045002. https://doi.org/10.1088/ 
1361-665X/ac4e4e, URL https://dx.doi.org/10.1088/1361-665X/ac4e4e, pub-
lisher: IOP Publishing. 
[290] “Silicon Carbide SiC Material Properties,” , ????. URL http://accuratus. 
com/silicar.html. 
[291] “Boron Nitride | BN Material Properties,” , ????. URL http://accuratus. 
com/boron.html. 
[292] Wu, S., Yan, T., Kuai, Z., and Pan, W., “Corrigendum to: “Thermal con-
ductivity enhancement on phase change materials for thermal energy stor-
age: A review”,” Energy Storage Materials, Vol. 33, 2020, p. 503. https: 
//doi.org/10.1016/j.ensm.2020.06.019, URL https://www.sciencedirect.com/ 
science/article/pii/S2405829720302397. 
[293] Li, J., Leng, J., Jiang, Y., and Zhang, J., “Experimental characterization 
of 3D printed PP/h-BN thermally conductive composites with highly ori-
ented h-BN and the effects of filler size,” Composites Part A: Applied Sci-
ence and Manufacturing, Vol. 150, 2021, p. 106586. https://doi.org/10.1016/ 
166
j.compositesa.2021.106586, URL https://www.sciencedirect.com/science/ 
article/pii/S1359835X21003067. 
[294] Sonsalla, T., Moore, A. L., Meng, W. J., Radadia, A. D., and Weiss, L., “3-D 
printer settings effects on the thermal conductivity of acrylonitrile butadiene 
styrene (ABS),” Polymer Testing, Vol. 70, 2018, pp. 389–395. https://doi.org/ 
10.1016/j.polymertesting.2018.07.018, URL https://www.sciencedirect.com/ 
science/article/pii/S0142941818305919. 
[295] Elkholy, A., Rouby, M., and Kempers, R., “Characterization of the 
anisotropic thermal conductivity of additively manufactured components 
by fused filament fabrication,” Progress in Additive Manufacturing, Vol. 4, 
No. 4, 2019, pp. 497–515. https://doi.org/10.1007/s40964-019-00098-2, URL 
https://doi.org/10.1007/s40964-019-00098-2. 
[296] Wu, H., Li, Q., Bu, X., Liu, W., Cao, G., Li, X., and Wang, X., “Gas sensing 
performance of graphene-metal contact after thermal annealing,” Sensors and 
Actuators B: Chemical, Vol. 282, 2019, pp. 408–416. https://doi.org/10.1016/ 
j.snb.2018.11.066, URL https://www.sciencedirect.com/science/article/pii/ 
S0925400518320215. 
[297] Torrado, A. R., and Roberson, D. A., “Failure Analysis and Anisotropy Eval-
uation of 3D-Printed Tensile Test Specimens of Different Geometries and 
Print Raster Patterns,” Journal of Failure Analysis and Prevention, Vol. 16, 
No. 1, 2016, pp. 154–164. https://doi.org/10.1007/s11668-016-0067-4, URL 
https://doi.org/10.1007/s11668-016-0067-4. 
[298] Guo, Y., Yang, H., Lin, G., Jin, H., Shen, X., He, J., and Miao, J., “Ther-
mal performance of a 3D printed lattice-structure heat sink packaging phase 
change material,” Chinese Journal of Aeronautics, Vol. 34, No. 5, 2021, pp. 
167
373–385. https://doi.org/10.1016/j.cja.2020.07.033, URL https://www. 
sciencedirect.com/science/article/pii/S1000936120303551. 
[299] Mehling, H., Brütting, M., and Haussmann, T., “PCM products and their 
fields of application - An overview of the state in 2020/2021,” Journal of 
Energy Storage, Vol. 51, 2022, p. 104354. https://doi.org/10.1016/j.est. 
2022.104354, URL https://www.sciencedirect.com/science/article/pii/ 
S2352152X22003784. 
[300] “Axiotherm PCM - products | Axiotherm GmbH - Innovative thermal 
storage systems,” , ????. URL https://www.axiotherm.de/en/produkte/ 
axiotherm-pcm/. 
[301] “Phase Change Material | Boyd,” , ????. URL https://www.boydcorp.com/ 
thermal/conduction-cooling/phase-change-interface-materials.html. 
[302] “PCM-ClimSel,” , ????. URL https://www.climator.com/en/pcm-climsel. 
[303] “Thermal energy storage | Energy Technologies,” , ????. URL https://www. 
crodaenergytechnologies.com/en-gb/applications/thermal-energy-storage. 
[304] “PCM Technology Applications,” , ????. URL https://www.pcmtechnology. 
eu/en/applications/for-homes. 
[305] “Parvan at ExxonMobil,” , ????. URL https://www.exxonmobil.com/en/ 
wax/wax-types/fully-refined-paraffin-wax. 
[306] “Henkel Phase Change Materials,” , ????. URL https://www. 
henkel-adhesives.com/us/en/products/thermal-management-materials/ 
phase-change-material.html. 
[307] “Honeywell Phase Change Materials,” , ????. URL https: 
168
//thermalmanagement.honeywell.com/us/en/products/ 
thermal-interface-materials/phase-change-materials. 
[308] “Insolcorp Phase Change Materials,” , ????. URL https://insolcorp.com/ 
services/. 
[309] “Laird Phase Change Materials,” , ????. URL https://www.laird.com/ 
products/thermal-interface-materials/phase-change. 
[310] “Microtek Phase Change Materials,” , ????. URL https://www.microteklabs. 
com/phase-change-materials/. 
[311] “Technology – BioPCM – Phase Change Solutions,” , ????. URL https:// 
phasechange.com/biopcm/. 
[312] “savE® PCMs Product Range – PLUSS®,” , ????. URL https://pluss.co. 
in/save-pcms-product-range/. 
[313] PureTemp, “PureTemp,” , ???? URL https://puretemp.com/?page id=173. 
[314] “Rubitherm GmbH,” , ????. URL https://www.rubitherm.eu/en/ 
productcategory/makroverkaspelung-w%C3%A4rmekissen. 
[315] “Sasol Phase Change Materials,” , ????. URL https://www. 
sasolnorthamerica.com/products/phase-change-materials-1/. 
[316] “Sunamp | Global - World leading thermal storage technologies,” , ????. URL 
https://sunamp.com/hot-water-thermino-overview/. 
[317] “PCM Solutions - Tempered Entropy,” , Nov. 2018. URL https://www. 
pcmgel.com/pcm-solutions/. 
169
[318] “Ice Thermal Storage | Thermal Energy Storage | Baltimore Aircoil 
Company,” , ????. URL https://baltimoreaircoil.com/products/ 
ice-thermal-storage. 
[319] “CALMAC® global leader in energy storage,” , ????. URL http://www. 
calmac.com/. 
[320] “Evapco Thermal Ice Storage,” , Sep. 2016. URL http://www.evapco.com/ 
products/product-featuresextras/thermal-ice-storage. 
[321] “Sunamp | Global - World leading thermal storage technologies,” , ????. URL 
https://sunamp.com/plentigrade/. 
[322] “Products – ENRG Blanket – Phase Change Solutions,” , ????. URL https: 
//phasechange.com/enrgblanket/. 
[323] “HeatSels® - products | Axiotherm GmbH - Innovative thermal storage sys-
tems,” , ????. URL https://www.axiotherm.de/en/produkte/heatsels%C2% 
AE/. 
[324] “HeatStaxx® Air - products | Axiotherm GmbH - Innovative thermal storage 
systems,” , ????. URL https://www.axiotherm.de/en/produkte/heatstaxx% 
C2%AE-air/. 
[325] peschel, “Collector with plastic cover,” , Jun. 2016. URL https://www. 
sunwindenergy.com/solar-thermal/collector-plastic-cover. 
[326] “PCM Heat Sinks Manufacturer | Custom Copper Heat Sink Design | 
Two Phase Heatsink,” , ????. URL https://www.1-act.com/products/ 
pcm-heat-sinks/. 
[327] “Koolit Refrigerants,” , ????. URL https://www.coldchaintech.com/ 
koolit-refrigerants/. 
170
[328] “Foam Bricks, Gel Packs, & Refrigerant Mats | Refrigerants | ThermoSafe,” , 
????. URL https://www.thermosafe.com/products/refrigerants/. 
[329] “PCC Technology,” , ????. URL https://www.allcelltech.com/pcc. 
[330] “Cold Storage,” , ????. URL https://www.vikingcold.com/cold-storage/. 
[331] “Technology – PLUSS®,” , ????. URL https://pluss.co.in/technology/. 
[332] “Glacier Tek | Cooling Vests & Products,” , ????. URL https://glaciertek. 
com/. 
[333] “Inuteq - Keep your head cool,” , ????. URL https://inuteq.com/ 
bodycool-smart. 
[334] “Outlast pcm material technology comfort climate heat management,” , ????. 
URL https://www.outlast.com/en/. 
[335] “Rubitherm GmbH,” , ????. URL https://www.rubitherm.eu/en/ 
productcategory/organische-pcm-rt. 
[336] “Purchase Ice9™ Materials - TCPoly - Xpanels,” , Feb. 2022. URL https: 
//tcpoly.com/purchase-ice9-materials/. 
[337] Lamé, G., and Clapeyron, B., “Mémoire sur la solidification par refroidisse-
ment d’un globe liquide,” 1831, pp. 250–256. Issue: 1831. 
[338] Carslaw, H. S., and Jaeger, J. C., “Conduction of heat in solids,” Conduction 
of heat in solids, 1947. 
[339] Stefan, J., “Über einige probleme der theorie der wärmeleitung,” Sitzungber., 
Wien, Akad. Mat. Natur, Vol. 98, 1889, pp. 473–484. 
[340] Stefan, J., “Ueber die Theorie der Eisbildung, insbesondere über die 
Eisbildung im Polarmeere,” Annalen der Physik, Vol. 278, No. 2, 1891, 
171
pp. 269–286. https://doi.org/10.1002/andp.18912780206, URL https: 
//onlinelibrary.wiley.com/doi/abs/10.1002/andp.18912780206, eprint: 
https://onlinelibrary.wiley.com/doi/pdf/10.1002/andp.18912780206. 
[341] Bonacina, C., Comini, G., Fasano, A., and Primicerio, M., “Numerical so-
lution of phase-change problems,” International Journal of Heat and Mass 
Transfer, Vol. 16, No. 10, 1973, pp. 1825–1832. https://doi.org/10.1016/ 
0017-9310(73)90202-0, URL https://www.sciencedirect.com/science/article/ 
pii/0017931073902020. 
[342] Meyer, G. H., “Multidimensional Stefan Problems,” SIAM Journal on Nu-
merical Analysis, Vol. 10, No. 3, 1973, pp. 522–538. URL https://www.jstor. 
org/stable/2156119, publisher: Society for Industrial and Applied Mathemat-
ics. 
[343] Shamsundar, N., and Sparrow, E. M., “Storage of Thermal Energy by Solid-
Liquid Phase Change—Temperature Drop and Heat Flux,” Journal of Heat 
Transfer, Vol. 96, No. 4, 1974, pp. 541–544. https://doi.org/10.1115/1. 
3450242, URL https://doi.org/10.1115/1.3450242. 
[344] Shamsundar, N., and Sparrow, E. M., “Analysis of Multidimensional Con-
duction Phase Change Via the Enthalpy Model,” Journal of Heat Transfer, 
Vol. 97, No. 3, 1975, pp. 333–340. https://doi.org/10.1115/1.3450375, URL 
https://doi.org/10.1115/1.3450375. 
[345] Sparrow, E. M., Patankar, S. V., and Ramadhyani, S., “Analysis of Melt-
ing in the Presence of Natural Convection in the Melt Region,” Journal of 
Heat Transfer, Vol. 99, No. 4, 1977, pp. 520–526. https://doi.org/10.1115/1. 
3450736, URL https://doi.org/10.1115/1.3450736. 
[346] Smith, R. N., Ebersole, T. E., and Griffin, F. P., “Heat Exchanger Perfor-
172
mance in Latent Heat Thermal Energy Storage,” Journal of Solar Energy 
Engineering, Vol. 102, No. 2, 1980, pp. 112–118. https://doi.org/10.1115/1. 
3266128, URL https://doi.org/10.1115/1.3266128. 
[347] Buddhi, D., Bansal, N. K., Sawhney, R. L., and Sodha, M. S., “So-
lar thermal storage systems using phase change materials,” In-
ternational Journal of Energy Research, Vol. 12, No. 3, 1988, pp. 
547–555. https://doi.org/10.1002/er.4440120318, URL https: 
//onlinelibrary.wiley.com/doi/abs/10.1002/er.4440120318, eprint: 
https://onlinelibrary.wiley.com/doi/pdf/10.1002/er.4440120318. 
[348] Dantzig, J. A., “Modelling liquid–solid phase changes with melt convec-
tion,” International Journal for Numerical Methods in Engineering, Vol. 28, 
No. 8, 1989, pp. 1769–1785. https://doi.org/10.1002/nme.1620280805, URL 
https://onlinelibrary.wiley.com/doi/abs/10.1002/nme.1620280805, eprint: 
https://onlinelibrary.wiley.com/doi/pdf/10.1002/nme.1620280805. 
[349] Farid, M. M., and Husian, R. M., “An electrical storage heater using the 
phase-change method of heat storage,” Energy Conversion and Man-
agement, Vol. 30, No. 3, 1990, pp. 219–230. https://doi.org/10.1016/ 
0196-8904(90)90003-H, URL https://www.sciencedirect.com/science/article/ 
pii/019689049090003H. 
[350] Bellecci, C., and Conti, M., “Phase change thermal storage: transient be-
haviour analysis of a solar receiver/storage module using the enthalpy 
method,” International Journal of Heat and Mass Transfer, Vol. 36, No. 8, 
1993, pp. 2157–2163. https://doi.org/10.1016/S0017-9310(05)80146-2, URL 
https://www.sciencedirect.com/science/article/pii/S0017931005801462. 
[351] Lacroix, M., and Duong, T., “Experimental improvements of heat transfer in 
173
a latent heat thermal energy storage unit with embedded heat sources,” En-
ergy Conversion and Management, Vol. 39, No. 8, 1998, pp. 703–716. https: 
//doi.org/10.1016/S0196-8904(97)10011-5, URL https://www.sciencedirect. 
com/science/article/pii/S0196890497100115. 
[352] Lamberg, P., Lehtiniemi, R., and Henell, A.-M., “Numerical and experi-
mental investigation of melting and freezing processes in phase change ma-
terial storage,” International Journal of Thermal Sciences, Vol. 43, No. 3, 
2004, pp. 277–287. https://doi.org/10.1016/j.ijthermalsci.2003.07.001, URL 
https://www.sciencedirect.com/science/article/pii/S1290072903001303. 
[353] AL-Saadi, S. N., and Zhai, Z. J., “Modeling phase change materials embedded 
in building enclosure: A review,” Renewable and Sustainable Energy Reviews, 
Vol. 21, 2013, pp. 659–673. https://doi.org/10.1016/j.rser.2013.01.024, URL 
https://www.sciencedirect.com/science/article/pii/S1364032113000555. 
[354] Souayfane, F., Fardoun, F., and Biwole, P. H., “Different mathematical mod-
els of convection during phase change,” 2016 3rd International Conference 
on Renewable Energies for Developing Countries (REDEC), 2016, pp. 1–8. 
https://doi.org/10.1109/REDEC.2016.7577543. 
[355] Py, X., Olives, R., and Mauran, S., “Paraffin/porous-graphite-matrix com-
posite as a high and constant power thermal storage material,” Interna-
tional Journal of Heat and Mass Transfer, Vol. 44, No. 14, 2001, pp. 2727– 
2737. https://doi.org/10.1016/S0017-9310(00)00309-4, URL https://www. 
sciencedirect.com/science/article/pii/S0017931000003094. 
[356] Wu, S., Li, T. X., Yan, T., Dai, Y. J., and Wang, R. Z., “High performance 
form-stable expanded graphite/stearic acid composite phase change ma-
terial for modular thermal energy storage,” International Journal of Heat 
174
and Mass Transfer, Vol. 102, 2016, pp. 733–744. https://doi.org/10.1016/j. 
ijheatmasstransfer.2016.06.066, URL https://www.sciencedirect.com/science/ 
article/pii/S0017931016301909. 
[357] Galazutdinova, Y., Vega, M., Grágeda, M., Cabeza, L. F., and Ushak, 
S., “Preparation and characterization of an inorganic magnesium chlo-
ride/nitrate/graphite composite for low temperature energy storage,” So-
lar Energy Materials and Solar Cells, Vol. 175, 2018, pp. 60–70. https: 
//doi.org/10.1016/j.solmat.2017.09.046, URL https://www.sciencedirect.com/ 
science/article/pii/S092702481730541X. 
[358] Gao, D., Chen, Z., Shi, M., and Wu, Z., “Study on the melting process of 
phase change materials in metal foams using lattice Boltzmann method,” 
Science China Technological Sciences, Vol. 53, No. 11, 2010, pp. 3079–3087. 
https://doi.org/10.1007/s11431-010-4074-5, URL https://doi.org/10.1007/ 
s11431-010-4074-5. 
[359] Yang, Z., and Garimella, S. V., “Melting of Phase Change Materials With 
Volume Change in Metal Foams,” Journal of Heat Transfer, Vol. 132, No. 6, 
2010. https://doi.org/10.1115/1.4000747, URL https://doi.org/10.1115/1. 
4000747. 
[360] Dukhan, N., and Bodke, S., “An improved PCM heat storage technology 
utilizing metal foam,” 2010 12th IEEE Intersociety Conference on Thermal 
and Thermomechanical Phenomena in Electronic Systems, 2010, pp. 1–7. 
https://doi.org/10.1109/ITHERM.2010.5501364, iSSN: 1087-9870. 
[361] Lafdi, K., Mesalhy, O., and Elgafy, A., “Merits of Employing Foam En-
capsulated Phase Change Materials for Pulsed Power Electronics Cooling 
175
Applications,” Journal of Electronic Packaging, Vol. 130, No. 2, 2008. 
https://doi.org/10.1115/1.2912185, URL https://doi.org/10.1115/1.2912185. 
[362] Li, W. Q., Guo, S. J., Tan, L., Liu, L. L., and Ao, W., “Heat transfer en-
hancement of nano-encapsulated phase change material (NEPCM) using 
metal foam for thermal energy storage,” International Journal of Heat 
and Mass Transfer, Vol. 166, 2021, p. 120737. https://doi.org/10.1016/j. 
ijheatmasstransfer.2020.120737, URL https://www.sciencedirect.com/science/ 
article/pii/S0017931020336735. 
[363] Palomo Del Barrio, E., Dauvergne, J. L., and Morisson, V., “A Simple Ex-
perimental Method for Thermal Characterization of Shape-Stabilized Phase 
Change Materials,” Journal of Solar Energy Engineering, Vol. 131, No. 4, 
2009. https://doi.org/10.1115/1.3197838, URL https://doi.org/10.1115/1. 
3197838. 
[364] Brousseau, P., and Lacroix, M., “Numerical simulation of a multi-layer la-
tent heat thermal energy storage system,” International Journal of En-
ergy Research, Vol. 22, No. 1, 1998, pp. 1–15. https://doi.org/10.1002/ 
(SICI)1099-114X(199801)22:1⟨1::AID-ER334⟩3.0.CO;2-L, 
URL https: 
//onlinelibrary.wiley.com/doi/abs/10.1002/%28SICI%291099-114X% 
28199801%2922%3A1%3C1%3A%3AAID-ER334%3E3.0.CO%3B2-L, 
eprint: https://onlinelibrary.wiley.com/doi/pdf/10.1002/%28SICI%291099-
114X%28199801%2922%3A1%3C1%3A%3AAID-ER334%3E3.0.CO%3B2-L. 
[365] Okada, M., “Characteristics of a Plate-Fin Heat Exchanger with Phase 
Change Materials,” Journal of Enhanced Heat Transfer, Vol. 2, No. 4, 
1995. https://doi.org/10.1615/JEnhHeatTransf.v2.i4.30, URL https: 
//www.dl.begellhouse.com/journals/4c8f5faa331b09ea,7f83fab45ff69f39, 
05ab23a408232810.html, publisher: Begel House Inc. 
176
[366] Majumdar, P., and Saidbakhsh, A., “A heat transfer model for phase change 
thermal energy storage,” Heat Recovery Systems and CHP, Vol. 10, No. 5, 
1990, pp. 457–468. https://doi.org/10.1016/0890-4332(90)90196-Q, URL 
https://www.sciencedirect.com/science/article/pii/089043329090196Q. 
[367] Benkaddour, A., and Faraji, M., “Numerical Investigation of a Phase Change 
Material Building Integrating Solar Thermal Collector PCM-BST,” Journal 
of Thermal Science and Engineering Applications, Vol. 14, No. 8, 2022. https: 
//doi.org/10.1115/1.4053057, URL https://doi.org/10.1115/1.4053057. 
[368] Merlin, K., Delaunay, D., Soto, J., and Traonvouez, L., “Heat transfer en-
hancement in latent heat thermal storage systems: Comparative study of dif-
ferent solutions and thermal contact investigation between the exchanger and 
the PCM,” Applied Energy, Vol. 166, 2016, pp. 107–116. https://doi.org/10. 
1016/j.apenergy.2016.01.012, URL https://www.sciencedirect.com/science/ 
article/pii/S0306261916000313. 
[369] Bastida, H., Ugalde-Loo, C. E., Abeysekera, M., and Jenkins, N., “Dynamic 
modelling of ice-based thermal energy storage for cooling applications,” IET 
Energy Systems Integration, Vol. 4, No. 3, 2022, pp. 317–334. https://doi.org/ 
10.1049/esi2.12061, URL https://onlinelibrary.wiley.com/doi/10.1049/esi2. 
12061. 
[370] Choi, Y.-H., Kim, C.-M., Jeong, H.-S., and Youn, J.-H., “Influence of Bed 
Temperature on Heat Shrinkage Shape Error in FDM Additive Manufacturing 
of the ABS-Engineering Plastic,” World Journal of Engineering and Tech-
nology, Vol. 4, No. 3, 2016, pp. 186–192. https://doi.org/10.4236/wjet.2016. 
43D022, URL http://www.scirp.org/Journal/Paperabs.aspx?paperid=71339, 
number: 3 Publisher: Scientific Research Publishing. 
177
[371] Zawaski, C., and Williams, C., “Design of a low-cost, high-temperature 
inverted build environment to enable desktop-scale additive manufactur-
ing of performance polymers,” Additive Manufacturing, Vol. 33, 2020, p. 
101111. https://doi.org/10.1016/j.addma.2020.101111, URL https://www. 
sciencedirect.com/science/article/pii/S2214860419318184. 
[372] Nawaz, K., Schmidt, S. J., and Jacobi, A. M., “Effect of catalyst used in 
the sol-gel process on the microstructure and adsorption/desorption perfor-
mance of silica aerogels,” International Journal of Heat and Mass Transfer, 
Vol. 74, 2014, pp. 25–34. https://doi.org/10.1016/j.ijheatmasstransfer.2014. 
03.003, URL http://www.scopus.com/inward/record.url?scp=84897080819& 
partnerID=8YFLogxK. 
[373] Kakaç, S., Shah, R. K., and Aung, W., Handbook of single-phase convective 
heat transfer, J. Wiley and sons, New York Chichester Brisbane, 1987. 
178
