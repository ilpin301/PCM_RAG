---
Title: "1-D CHALCOGENIDE NANOMATERIALS FOR ELECTRONICS: PHASE- CHANGE MEMORY AND TOPOLOGICAL INSULATORS A DISSERTATION SUBMITTED TO THE - Stacks are the Stanford"
Author: "Unknown"
Reference: "https://stacks.stanford.edu/file/druid:vh072qq0446/Dissertation,%20Stefan%20Meister-augmented.pdf"
ContentType:
  - "pdf"
Created: 2026-06-17
Processed: true
tags:
  - "source"
---

1-D CHALCOGENIDE NANOMATERIALS FOR ELECTRONICS: PHASE-
CHANGE MEMORY AND TOPOLOGICAL INSULATORS 
 
 
A DISSERTATION 
SUBMITTED TO 
THE DEPARTMENT OF MATERIALS SCIENCE AND ENGINEERING 
AND THE COMMITTEE ON GRADUATE STUDIES 
OF STANFORD UNIVERSITY 
IN PARTIAL FULFILLMENT OF THE REQUIREMENTS 
FOR THE DEGREE OF 
DOCTOR OF PHILOSOPHY 
 
 
 
Stefan Meister 
August 2010 
  
 
 
 
 
 
 
 
 
 
 
 
                                                      http://creativecommons.org/licenses/by-nc/3.0/us/ 
 
 
 
This dissertation is online at: http://purl.stanford.edu/vh072qq0446 
 
© 2010 by Stefan Meister. All Rights Reserved. 
Re-distributed by Stanford University under license with the author. 
This work is licensed under a Creative Commons Attribution-Noncommercial 3.0 United States License. 
I certify that I have read this dissertation and that, in my opinion, it is fully adequate in scope and quality as a dissertation for the degree of Doctor of Philosophy. 
Yi Cui, Primary Adviser 
I certify that I have read this dissertation and that, in my opinion, it is fully adequate in scope and quality as a dissertation for the degree of Doctor of Philosophy. 
David Goldhaber-Gordon 
I certify that I have read this dissertation and that, in my opinion, it is fully adequate in scope and quality as a dissertation for the degree of Doctor of Philosophy. 
Paul McIntyre 
Approved for the Stanford University Committee on Graduate Studies. 
Patricia J. Gumport, Vice Provost Graduate Education 
This signature page was generated electronically upon submission of this dissertation in electronic format. An original signed hard copy of the signature page is on file in University Archives. 
 iv 
Abstract 
 Chalcogenides are ubiquitous in academia and industry. We focus on 
chalcogenides for phase-change memory and topological insulators. Phase change 
memory (PCM) utilizes the resistivity contrast between the crystalline and amorphous 
phases of certain chalcogenides to store information. Industry is making progress in 
PCM, which could someday compete with flash memory due to its superior scalability, 
fast switching and high endurance. In contrast, the field of topological insulators is 
very young. Topological insulators, bulk insulators with conductive surface states, 
have attracted great attention since their discovery five years ago. They have exotic 
properties and are exciting for both fundamental studies and potential applications. 
Our studies of chalcogenide nanomaterials for PCM and topological insulators 
provided new insights into these fascinating materials. 
We developed a method to switch PCM cells inside a transmission electron 
microscope (TEM), allowing direct correlation of electrical behavior with structural 
changes. Using this technique, we found that the electrical behavior of Ge2Sb2Te3 
lateral phase-change cells depends strongly on the highly variable microstructure of 
the amorphous domain. In search of new PCM materials, we developed the VLS 
synthesis of GeTe and Sb2Te3 phase-change nanowires. In situ TEM observation of 
these nanowires revealed a new switching mechanism via the opening and closing of 
voids.  We also synthesized single-crystalline topological insulator nanoribbons, 
whose large surface to bulk conduction ratio increases the relative contribution of the 
surface states.  We successfully measured Aharonov-Bohm oscillations in the 
nanoribbons, thereby observing one of the first electrical signatures of the topological 
states in this material system. 
 
 v 
Acknowledgements 
First of all, I am grateful to my advisor Professor Yi Cui for his contagious 
enthusiasm, valuable guidance and constant support throughout my graduate years. 
I’m glad to have been one of his first students; the opportunity to help set up the lab 
and see the group grow was a tremendous learning experience. Next, I would like to 
thank the members of my reading committee, Professors David Goldhaber-Gordon 
and Paul McIntyre, for their valuable input into this dissertation as well as for serving 
on my defense committee along with Professor William Nix and defense chair 
Professor Yoshio Nishi. Finally, I am grateful for the support and kindness of 
Professors Robert Huggins, Xiao-Liang Qi, Zhi-Xun Shen, Philip Wong, and Shou-
Cheng Zhang during my time at Stanford. 
I am grateful to SangBum Kim and David Schoen for the fruitful collaboration 
on the phase-change memory project. I am also thankful for the exciting collaboration 
on topological insulators with Hailin Peng, Desheng Kong, Keji Lai, Judy Cha and 
Yulin Chen.  The group dynamic and team spirit were the best I have ever experienced.  
Being part of the Cui group has been both enjoyable and exciting; I am thankful to 
have had the opportunity to work with these great people and I value the friendships 
that we have formed. 
Finally, I am grateful for the loving support of my wife, family and friends. 
 vi 
Table of Contents 
Abstract ........................................................................................................................ iv 
Acknowledgements .......................................................................................................v 
1 Introduction ..........................................................................................................1 
1.1 Background and motivation ...........................................................................1 
1.2 Outline of dissertation ....................................................................................2 
1.3 Phase-change materials for memory ..............................................................3 
1.3.1 Introduction ............................................................................................3 
1.3.2 The phase-change mechanism................................................................5 
1.3.3 Threshold switching ...............................................................................7 
1.3.4 Common phase-change memory cells....................................................9 
1.3.5 Materials ...............................................................................................10 
1.4 In situ TEM...................................................................................................14 
1.4.1 Introduction and motivation .................................................................14 
1.4.2 In situ TEM holder ...............................................................................15 
1.4.3 TEM window manufacturing ...............................................................16 
1.4.4 History and challenges of in situ TEM technique ................................18 
1.5 Vapor-liquid-solid growth ............................................................................20 
1.5.1 Introduction ..........................................................................................20 
1.5.2 Growth parameters ...............................................................................22 
1.6 Topological insulators ..................................................................................24 
1.6.1 Introduction ..........................................................................................24 
1.6.2 Materials ...............................................................................................26 
2 In situ transmission electron microscopy of phase-change memory .............28 
2.1 Introduction ..................................................................................................28 
2.2 Method..........................................................................................................30 
2.2.1 Device fabrication ................................................................................30 
2.2.2 TEM characterization of sputtered GST films .....................................31 
2.2.3 Electrical testing and TEM observation ...............................................32 
 vii 
2.3 Switching experiments .................................................................................33 
2.3.1 Demonstration of in situ switching.......................................................33 
2.3.2 Two types of amorphous phases...........................................................35 
2.3.3 Dependence of phase transition on voltage pulse.................................36 
2.4 Threshold field measurements......................................................................40 
2.4.1 Significance of threshold field..............................................................40 
2.4.2 Measurements.......................................................................................41 
2.4.3 Discussion.............................................................................................45 
2.5 Control of quenching rate via device geometry ...........................................47 
2.6 Conclusions ..................................................................................................49 
3 Synthesis and characterization of GeTe phase-change nanowires ................51 
3.1 Introduction ..................................................................................................51 
3.1.1 Motivation and overview......................................................................51 
3.1.2 Background...........................................................................................51 
3.1.3 Materials ...............................................................................................52 
3.2 Synthesis.......................................................................................................53 
3.3 Characterization............................................................................................54 
3.3.1 Scanning electron microscopy..............................................................54 
3.3.2 Transmission electron microscopy .......................................................57 
3.4 Sb2Te3 nanowires..........................................................................................59 
3.5 Recent developments and future outlook .....................................................59 
3.6 Conclusion....................................................................................................61 
4 Electrical characterization and in-situ TEM of phase-change nanowires ....62 
4.1 Introduction ..................................................................................................62 
4.1.1 Background and motivation .................................................................62 
4.1.2 Device fabrication ................................................................................64 
4.1.3 Instruments and measurements.............................................................66 
4.2 Conventional (black-box) switching experiment .........................................67 
4.2.1 Electrical characterization ....................................................................67 
4.2.2 Nanowire switching..............................................................................69 
 viii 
4.2.3 Investigation of high resistance in off state via SPM ...........................70 
4.3 Direct TEM Observation of NWs during switching.....................................71 
4.3.1 TEM observation of off state................................................................71 
4.3.2 Real-time observation of dynamic behavior: opening and closing of 
voids 76 
4.4 Conclusion....................................................................................................80 
5 Topological insulator nanoribbons ...................................................................82 
5.1 Introduction and motivation .........................................................................82 
5.2 Synthesis of topological insulator nanoribbons............................................83 
5.3 Electrical characterization of nanoribbons ...................................................87 
5.4 Aharonov-Bohm interference in topological insulator nanoribbons ............92 
5.4.1 Introduction to Aharonov-Bohm effect ................................................92 
5.4.2 Aharonov-Bohm measurement.............................................................94 
5.4.3 Discussion and conclusion ...................................................................95 
5.5 Conclusion....................................................................................................96 
6 Conclusion ...........................................................................................................97 
 ix 
List of Figures 
 
Figure  1.1: Schematic of two phases of phase-change materials. The amorphous phase 
has a high resistivity with typical resistances in the MΩ range.  The crystalline 
phase has a low resistivity with typical resistances in the kΩ range.  Switching 
between the two phases is accomplished via crystallization and melt-quenching. ....4 
Figure  1.2: Schematic of the temperature of the active region in a phase-change cell as 
a function of time.  During the RESET operation, the device must exceed the 
melting temperature for a short time and then be quenched rapidly to freeze the 
atoms in place.  During the SET operation the temperature must be raised above the 
crystallization temperature for sufficient time for crystallization to take place.  The 
cool-down rate is for the SET operation is not important for the phase transition to 
occur. ..........................................................................................................................6 
Figure  1.3: Schematic of the IV response of a typical phase-change memory cell.  The 
graph is for a current scan showing typical snapback behavior. ................................8 
Figure  1.4: Schematic of vertical (left) and horizontal (right) phase-change memory 
cells.  The light red shows the approximate region where the phase-transition occurs. 
..................................................................................................................................10 
Figure  1.5: Ternary phase-diagram for Ge, Te, and Sb showing important 
compositions.............................................................................................................13 
Figure  1.6: Schematic comparison between conventional PCM measurements that 
treat the memory element as a black box and in situ TEM measurements that supply 
detailed information on microstructural changes during switching. ........................14 
Figure  1.7: Photograph of custom electrical biasing holder and SEM images of TEM 
Si3N4 window used in the holder.  The light squares in the SEM image are gold pads 
for making electrical contact via wire bonding. .......................................................16 
Figure  1.8: Schematic of silicon nitride membrane on silicon substrate.  a. Cross-
section of silicon substrate.  b. Top-view of substrate with gold pads. ....................17 
Figure  1.9: Design challenges for in situ TEM PCM cells...........................................19 
 x 
Figure  1.10: Schematic of VLS growth furnace and plot of temperature distribution 
inside furnace............................................................................................................21 
Figure  1.11: SEM of early growth stage of GeTe NWs (left: top view; right: side view) 
..................................................................................................................................22 
Figure  1.12: Schematic of major growth parameters.  The growth only works if the 
parameters are all in a “target range” indicated by the blue ellipsoid. .....................23 
Figure  1.13: Schematic of simplified topological insulator band diagram. .................25 
Figure  1.14:  Schematic showing crystal structure of Bi2Se3 .......................................27 
Figure  2.1: Device schematic showing silicon substrate with 50nm silicon nitride 
membrane suspended at the center and GST bridge that is fabricated on the 
membrane. ................................................................................................................29 
Figure  2.2: Schematic of device cross-section (left) and SEM image of complete 
device (right). Cross section is taken along the dotted line. .....................................30 
Figure  2.3: TEM characterization of annealed GST 225 film after sputter deposition. a, 
b. Bright-field TEM images of as-deposited GST225 film after annealing on hot 
plate at 180ºC for 1 min. c. SAD of GST225 film could be accurately indexed to 
face-centered cubic phase of GST225.  No other phase was observed. ...................31 
Figure  2.4: Table summarizes measured and theoretical d-spacings of cubic phase of 
GST225.....................................................................................................................32 
Figure  2.5: TEM images and SAD of switching between crystalline and amorphous 
phase. a, b. TEM image showing a bridge in the (a) crystalline phase and (b) 
amorphous phase. Typical resistance values for crystalline and amorphous phases 
are 10-100 kΩ and 1-8 MΩ respectively.  The red circles indicate the approximate 
size and location of the selected area diffraction aperture in (c) and (d) c, d. Selected 
area diffraction confirming the poly-crystalline (c) and amorphous (d) nature of the 
bridge........................................................................................................................34 
Figure  2.6:  TEM images of two-phase amorphous/crystalline (left) and single-phase 
amorphous (right) domain.  The coloring is provided to give an estimate of where 
the material is amorphous.........................................................................................35 
 xi 
Figure  2.7:  Schematic of typical PCM resistance as a function of applied voltage 
pulse.  The crystal structure between crystalline and amorphous is unknown.........36 
Figure  2.8: Study of crystalline to amorphous transition. a. Resistance as a function of 
applied 400 ns voltage pulse. TEM images (b), (c), (d) correspond to labeled points 
in the graph.  The red line connects the average resistance values.  b-d. TEM images 
of phase-change memory bridge.  Red ellipses show examples of crystals that 
survived the amorphization process.  Yellow circles point out small differences in 
microstructure that accompany resistance change from 62 kΩ to 150 kΩ.  Green 
dashed lines surround areas that are predominantly amorphous. .............................38 
Figure  2.9: TEM images and corresponding SADs of bridge in various states of 
crystallization. a-c. Resistance of bridge in (a), (b), and (c) is 29 kΩ, 115 kΩ and 
3.5 MΩ, respectively.  The SADs (approximate size and location of SAD aperture 
indicated by red circles) confirm the crystallinity of the states.  In (a), the bridge is 
essentially completely crystalline as indicated by spot pattern and absence of diffuse 
ring. In (b), the bridge has some amorphous background, but the SAD still shows 
significant crystallinity.  In (c), the bridge is predominantly amorphous with several 
crystals remaining embedded in the amorphous matrix. ..........................................39 
Figure  2.10: Current spikes and destructive switching due to high threshold field. 
Voltage response graph indicating the point at which breakage can occur (left). 
TEM image of a sample broken during crystallization attempt (right). ...................41 
Figure  2.11: Measurement of threshold switching in high-resistance bridges. a. IV 
curve showing 120 μA current scan to crystallize the bridge in (c) and to measure 
the threshold voltage. This bridge exhibits complicated switching behavior. b. IV 
curve showing 100 μA current scan to crystallize the bridge in (d) and to measure 
the threshold voltage. This bridge exhibits clean switching behavior. c. TEM image 
of two-phase bridge before current scan (a).  The approximate amorphous domain 
has been colored blue to assist with visualization. d. TEM image of single-phase 
amorphous bridge before current scan (b).  The approximate amorphous domain has 
been colored red to assist with visualization. ...........................................................42 
 xii 
Figure  2.12: Measurement of threshold switching in high-resistance bridges. a. IV 
curve showing 120 μA current scan to crystallize the bridge in (c) and to measure 
the threshold voltage. This bridge exhibits complicated switching behavior, because 
it is in a mixed phase consisting of nanocrystals interspersed in an amorphous 
matrix resulting from repeated switching. b. IV curve showing 100 μA current scan 
to crystallize the bridge in (d) and to measure the threshold voltage. This bridge 
exhibits complicated switching behavior, because it consists of nanocrystals 
interspersed in an amorphous matrix. c. TEM image of mixed phase bridge before 
current scan (a). d.  TEM image of bridge before current scan (b). The bridge 
consists of nanocrystals that are due to annealing the as-deposited GST225 film 
after sputtering at 180°C for 10 min.  Despite the high density of nanocrystals, the 
resistance of the bridge is still very high indicating that no connected current paths 
exist. The nanocrystals appear as dark dots in TEM images due to the diffraction 
contrast.  Amorphous regions exhibit uniform contrast. ..........................................44 
Figure  2.13: Dependence of threshold voltage on amorphous region parameters. a. 
Threshold voltage as a function of the size of the amorphous region. b. Threshold 
voltage as a function of resistance in the amorphous state.  We observe two different 
behaviors depending on the microstructure of the amorphous phase.......................45 
Figure  2.14: Switching of high-aspect-ratio bridge with lower cooling rate. a. 
Crystalline bridge obtained after 60μA current scan; resistance is 18 kΩ.  The red 
circles show examples of large crystals embedded inside the bridge. b. The same 
bridge after applying a 2V, 300ns pulse. The red circles show that the crystals in (a) 
disappeared, indicating that the bridge melted completely as a result of the pulse.  
However, the bridge did not turn completely amorphous but re-crystallized due to 
the lower cooling rate.  c. The same bridge after 60μA current scan; resistance is 29 
kΩ. ............................................................................................................................47 
Figure  2.15: Repeated switching of high-aspect-ratio bridge with lower cooling rate. 
The figure shows TEM micrographs of the bridge after repeated switching.  60 μA 
current scans were used for crystallization and various voltage pulses were applied 
to achieve a high-resistance state.  The series of TEM images with the resistance 
 xiii 
shows that the bridge could not be turned completely amorphous by a 2V, 300ns 
pulse.  Increasing the pulse further resulted in the bridge breaking. ........................48 
Figure  2.16: TEM micrograph of a short bridge that can achieve a single-phase 
amorphous domain without crystalline residue due to its fast cooling-rate. ............49 
Figure  3.1: Quasi-binary phase diagram between Au and GeTe (Sb2Te3).  The shape of 
the drawing represents the phase diagram between Au and GeTe.  However, the 
general shape for Au and Sb2Te3 is very similar and the diagram can be used for 
showing the temperature values and general shape..................................................52 
Figure  3.2: SEM image of as-grown GeTe nanowires, showing high density and a 
wide size distribution with diameters ranging from roughly 20-300 nm. ................54 
Figure  3.3: SEM image of long GeTe nanowires.........................................................55 
Figure  3.4:  SEM image of as-grown GeTe helical and straight NWs (top).  The 
nanowires can randomly change from straight to helical growth (bottom)..............56 
Figure  3.5:  TEM image of a straight GeTe NW. The dark spot at the tip corresponds 
to a gold nanoparticles.  Insets show a high resolution image of the lattice fringes 
and SAD pattern. ......................................................................................................57 
Figure  3.6:  TEM Energy Dispersive X-ray Spectroscopy of GeTe NW.....................58 
Figure  3.7: SEM image of as-grown Sb2Te3 NW.........................................................59 
Figure  3.8: Schematic of phase-change memory that is based on NWs.  The phase-
change NW is grown on top of a p-n junction for selective addressing...................60 
Figure  4.1: Device fabrication steps outlined with SEM micrographs. .......................64 
Figure  4.2: SEM micrographs of GeTe NW with Pt contacts deposited by FIB .........65 
Figure  4.3: Four point probe GeTe nanowires device with corresponding measurement 
results........................................................................................................................ 67 
Figure  4.4: TEM image of GeTe NWs during heating experiment..............................68 
Figure  4.5: Cycling behavior. Nanowires were switched to a high resistance state with 
a 10 V, 200 ns pulse, and switched back to the low resistance state with a 100 mV/s 
scan up to 5 V. ..........................................................................................................69 
 xiv 
Figure  4.6: SEM, AFM, and EFM images of the same single nanowire device in a high 
resistance state. There is a 2 V difference between the light and dark color in the 
EFM image. ..............................................................................................................71 
Figure  4.7: Low-magnification SEM image of a silicon nitride membrane (dark) with 
gold contact pads (light). ..........................................................................................72 
Figure  4.8: Nanowire before (lower left inset) and after pulsing (main panel); the 
switching mechanism is identified as void formation at the top contact (upper right 
inset). ........................................................................................................................ 72 
Figure  4.9: a.  TEM image of nanowire after a 3.5V, 200ns pulse shows only minor 
changes including a bulge and small pinhole evaporation. b. Higher magnification 
image of bulge and pin hole c. Higher magnification image of pinhole close to 
contact.......................................................................................................................74 
Figure  4.10: a. Low-magnification TEM image of nanowire after a long low 
magnitude pulse. b. Banded planar defect structure. c. Void and amorphous region 
formation. Area I is amorphous and Area II, like the rest of the wire, is crystalline 
(SAED inset). ...........................................................................................................74 
Figure  4.11: Pulse applied to NW shown in Figure 4.10a; blue is the applied voltage, 
and red is the current through the device (left). EDS spectrum of areas I and II from 
Figure 4.10c (right)...................................................................................................75 
Figure  4.12: a. Voltage scan on a single nanowire device (inset). The blue square in 
the inset shows the location of the TEM observation in (b). b. TEM images taken in 
situ during the voltage scan in panel, at times I, II, III, and IV. Note the correlation 
of resistance with void size.......................................................................................76 
Figure  4.13:  TEM micrographs showing void formation via voltage pulse................77 
Figure  4.14:  In situ TEM observation showing closing of void and corresponding 
voltage scan. .............................................................................................................78 
Figure  4.15:  Material movement in void induced switching.  a. SEM after multiple 
cycles.  b. Schematic showing the movement of material inside the NW................79 
Figure  5.1:  Schematic of (a) bulk sample of Bi2Se3 and corresponding (b) band 
diagram. ....................................................................................................................82 
 xv 
Figure  5.2:  Schematic of topological insulator nanoribbon ........................................83 
Figure  5.3:  SEM of as-synthesized Bi2Se3 nanoribbons. ............................................84 
Figure  5.4: SEM and AFM of Bi2Se3 NR device. Graph shows height measurement of 
AFM cross section....................................................................................................85 
Figure  5.5: SEM and AFM of Bi2Se3 NR device.  Graph shows height measurement of 
AFM cross section....................................................................................................86 
Figure  5.6: Schematic of NR device.  Setup allows for 4-point probe (green V-) and 
Hall (blue V-) measurement  on the same ribbon.....................................................87 
Figure  5.7: SEM of Bi2Se3 NR device at 30° rotation.  Even though the NR appears 
bent it is lying flat on the substrate and the contacts are on top. ..............................88 
Figure  5.8:  Resistance as a function of temperature for Bi2Se3 NR. ...........................89 
Figure  5.9: SEM Bi2Se3 NR device.  This setup allows for 4-point probe and Hall 
measurements on the same device............................................................................90 
Figure  5.10: Hall measurements of two different devices showing different behaviors. 
..................................................................................................................................91 
Figure  5.11: Schematic of double slit experiment........................................................92 
Figure  5.12: Schematic of Aharonov-Bohm experiment. ............................................93 
Figure  5.13: Magnetoresistance and SEM of Bi2Se3 NR .............................................94 
Figure  5.14: Fourier transform of dR/dB data derived from Figure 5.X......................95 
 1 
1 Introduction 
1.1 Background and motivation 
Chalcogenide materials are chemical compounds that combine at least one 
chalcogen with at least one more electropositive element.  The term chalcogen 
generally refers to an element from group 16 (O, S, Se, Te, Po) of the periodic table.  
Since oxides are usually treated separately and polonium is rare and highly radioactive, 
chalcogenides commonly refer to sulfides, selenides and tellurides only.  These 
ubiquitous materials have been studied for many years, because they showed promise 
for many applications including solar cells1, 2, wave-guides3-5, photonic crystals6, 
terahertz detectors7, 8 and emitters8, thermoelectrics9, 10 and phase-change memory11, 12. 
In 2005 a new class of materials called topological insulators13-17 was 
discovered.  These materials attract much attention because they exhibit exotic 
electronic surface states that are interesting on a fundamental level and for potential 
future applications.  Interestingly, with the exception of BixSb1-x, the first predicted 
topological insulators18 (HgTe, Bi2Se3, Bi2Te3, Sb2Te3) are all chalcogenides.  Hence, 
it should come as no surprise that chalcogenides are still receiving significant attention 
in academic and industrial research today. 
The synthesis of Silicon and Germanium nanowires19 in 1998 caused a 
resurgence of interest in the vapor-liquid-solid (VLS) growth20 as a universal method 
for producing a wide variety of semiconducting NWs.  These nanostructures have 
shown interesting properties such as quantum confinement21, 22, a high thermoelectric 
 2 
conversion efficiency23, 24, usefulness in sensors25, 26 and batteries27, and interesting 
phase transformations28.  Further, nanowires are ideal candidates for fundamental 
studies due to their simplicity and compatibility with techniques such as electron 
microscopy and scanning probe microscopy29, 30. 
In this dissertation we use the vapor-liquid-solid growth to synthesize 
nanowires for technologically interesting materials, namely phase-change materials 
and topological insulators.  We exploit nanostructure geometries to allow in situ 
transmission electron microscopy (TEM) studies on phase-change memory cells and 
to measure Aharonov-Bohm interference in topological insulators, a signature of the 
surface states.  A short introduction to these materials, the in situ TEM technique, and 
the vapor-liquid-solid growth is provided in the following sections. 
1.2 Outline of dissertation 
 In this dissertation, we first give an introduction to phase-change memory, the 
in situ TEM technique employed in chapter 2 and 3, the vapor-liquid-solid growth, and 
topological insulators.  In chapter 2, we describe an in situ TEM study of a 
conventional lateral phase-change memory cell31.  The TEM observation allows for a 
direct correlation between microstructure and switching behavior.  We find that PCM 
devices with similar resistances can exhibit distinct threshold switching behaviors due 
to the different initial distribution of nanocrystalline and amorphous domains, 
explaining the variability of switching behaviors of PCM cells in the literature.  In 
chapter 3, we discuss the VLS synthesis and characterization of GeTe and Sb2Te3 
phase-change nanowires as new materials for phase-change memory.  Chapter 4 
 3 
covers our TEM observations of switching in phase-change nanowires.  Instead of a 
crystalline-amorphous transformation, we observed that the dominant switching 
mechanism during multiple cycling appears to be the opening and closing of voids in 
the nanowires due to material migration.  In Chapter 5 we discuss the VLS synthesis 
of Bi2Se3 topological insulator nanostructures, and in chapter 6 we show transport 
evidence of topological surface states through Aharonov-Bohm oscillations32 in VLS-
synthesized Bi2Se3 nanoribbons. 
1.3 Phase-change materials for memory 
1.3.1 Introduction 
Phase-change materials are materials that can exist in at least two different 
structural states: amorphous and crystalline (with possibly multiple crystalline states).  
While many materials can exist in these two states, only a few satisfy the stringent 
requirements for use in memory applications33, 34 (discussed in section 1.3.5).  In order 
for a memory element to be useful, a read operation must be able to unambiguously 
differentiate between the two states.  In the case of PCM, there is a large contrast in 
conductivity and reflectivity between the crystalline and amorphous state.  While the 
difference in reflectivity has been exploited for optical storage media35, such as 
rewritable DVDs, phase-change memory relies entirely on the difference in 
conductivity.  Figure 1.1 shows a schematic of the two phases, with typical resistance 
values of actual cells and basic nomenclature.  Switching from the amorphous phase to 
the crystalline phase, or crystallizing the amorphous phase, is referred to as the SET 
operation.  Switching from the crystalline to the amorphous phase, called the RESET 
https://lh3.googleusercontent.com/notebooklm/AKXwDQESmqajHpBgrYsXB7hQCmAF2A53RUyarOuP3gno0oPwPKBwVh0Y7_U21o-s1snydmDvgwF4rWtWJTX5L60d5Cw5lBzso-n4kwCzsS5dhXLQcAk6ShCPGl7gEXrw91QeRXyUTrw8=w647-h412-v0
47135389-d673-4dd4-ae4c-17e9ae78a82d
 4 
operation, is accomplished by melt-quenching the material.  Resistances in typical 
devices are in the MΩ range and kΩ range for amorphous and crystalline states, 
respectively. 
 
Figure  1.1: Schematic of two phases of phase-change materials. The amorphous phase has a high resistivity with typical resistances in the MΩ range.  The crystalline phase has a low resistivity with typical resistances in the kΩ range.  Switching between the two phases is accomplished via crystallization and melt-quenching.  
The first electrical switching between two states in chalcogenide materials was 
performed in 1968 by Stanford Ovshinsky36.  However, phase change memory has 
only recently generated great interest as a non-volatile memory solution, since flash 
memory has dominated the non-volatile memory market over the past 20 years.  
Continued scaling resulting in better performance and favorable economies of scale in 
flash memory made it difficult for competing memory technologies to enter the market.  
Only in recent years has the scaling of flash encountered fundamental problems that 
rekindled research into several other non-volatile memory technologies37, 38.  These 
technologies include magnetoresistive RAM39 (MRAM), ferroelectric RAM40, 41 
(FeRAM), other resistive RAM42 (RRAM) types, and phase-change memory. 
 5 
Applications for non-volatile memory are ubiquitous.  The wide use of 
portable electronics such as mobile phones, MP3 players, personal multimedia players, 
e-book readers, navigational devices and advanced laptops contribute to the growing 
market for non-volatile memory and push developers to make memory cheaper, faster 
and denser while consuming less power at the same time.  Indeed, with the recent 
advances there is hope for a universal memory that has all the attributes for an ideal 
memory and can replace current non-volatile and volatile memory technologies.  
Phase-change memory is believed to be a candidate for such universal memory43. 
  Today, phase-change materials are widely used in optical storage technologies 
such as rewritable CDs and DVDs.  Though, it is not clear which memory technology 
will prevail for future non-volatile memory applications.  However, on April 28th 2010, 
Samsung announced shipment of the industry’s “First Multi-chip Package with a 
PRAM Chip for Handsets” claiming that they use an alloy of germanium, antimony 
and tellurium, which “provides three-times faster data storage performance per word 
than NOR chips.”  The device has a capacity of 512 megabit.  This entrance of PCM 
into the market place is an important step towards future memory technologies that are 
not based on flash.  It also demonstrates the maturity that PCM has reached at this 
point and its potential for the future given that industry is already heavily invested in 
its development. 
1.3.2 The phase-change mechanism 
 Switching between the two phases is accomplished via Joule heating by a 
voltage pulse44.  In order to switch from the stable crystalline phase to the metastable 
https://lh3.googleusercontent.com/notebooklm/AKXwDQHY8p6fMY92ejPzrUOe2PMN0pHzw0Ia4CcyPNgv81ToCgI1k34zl2TKK3TKrgQq6p3NFuaVPgPSzXICxImV6Xgxu9tYIDBb--3AMknBrs8E2kY3_Yhh3KaLNbj8UuYZpINWyNrxsA=w726-h468-v0
8da40e6c-aa36-4cf0-88b7-af12edee13d5
 6 
amorphous phase, the material is melted and rapidly quenched, freezing the atoms in 
place before they have time to re-crystallize.  For the reverse transformation, from 
amorphous to crystalline, the material is heated above its crystallization temperature 
for a sufficient time.  Figure 1.2 depicts a schematic of typical temperature vs. time 
behavior that induces switching in a PCM cell.  While the RESET operation generally 
requires higher power, the SET operation is the time-limiting step (and hence data rate 
limiting), because it requires significantly more time to switch.  Although the SET 
operation tends to be the slower step, crystallization times faster than 1ns have been 
reported45 providing a positive future outlook for very fast memory switching. 
 
Figure  1.2: Schematic of the temperature of the active region in a phase-change cell as a function of time.  During the RESET operation, the device must exceed the melting temperature for a short time and then be quenched rapidly to freeze the atoms in place.  During the SET operation the temperature must be raised above the crystallization temperature for sufficient time for crystallization to take place.  The cool-down rate is for the SET operation is not important for the phase transition to occur.  
The impressive speed at which phase-change materials can crystallize has been a topic 
of great interest and will be briefly discussed in section 1.3.5 on phase-change 
 7 
materials.  Section 1.3.5 will also cover the atomic arrangements of the crystalline and 
amorphous phase for typical phase-change materials. 
1.3.3 Threshold switching 
 Depending on device geometry and size, a typical phase-change cell needs 
hundreds to thousands of μA of current to melt or switch from crystalline to 
amorphous46-50.  Since the typical resistance range of the amorphous phase is in the 
MΩs, one may wonder how it is possible to supply sufficient current for the RESET 
operation.  If the resistance behavior was strictly linear, hundreds to thousands of volts 
would be required to achieve the necessary current.  It turns out that despite the high 
resistivity of the amorphous phase, crystallization can be achieved by a relatively 
small voltage pulse because PCM materials exhibit threshold switching51-53.   
 Threshold switching occurs when a critical electric field is applied across the 
amorphous region resulting in conductive filaments that can facilitate sufficient 
heating to induce crystallization. 
https://lh3.googleusercontent.com/notebooklm/AKXwDQG8aF1Is_a6J4r8IUHCZ2bHc0eHzPtJHCDRAi97UvQ0mic_T1iro1LRZoXomehiEG07FcXKX76_XD5sK7xw6_1I4h3QnI2bzsth4ROXIg6s0YIrLi0S5Yt3zwzurmAbXfvvy7pS=w761-h525-v0
4b7bcc4d-ef5a-45fc-b8c5-7466d6ded310
 8 
 
Figure  1.3: Schematic of the IV response of a typical phase-change memory cell.  The graph is for a current scan showing typical snapback behavior. 
 
Figure 1.3 shows a schematic of an IV curve for a typical PCM cell for a current scan 
for a cell that is initially in the amorphous state.  Even though the voltage is the 
dependent variable, it is customary to plot it on the horizontal axis.  As the current is 
increased, the required voltage scales nearly linearly until a certain threshold voltage 
(Vth) is reached.  At this point, the IV curve shows a typical snapback behavior 
indicative of a sudden decrease in resistance. The resistance drops on the order of 
nanoseconds, much faster than the typical crystallization process, which takes 10s to 
100s of nanoseconds.   At this point the cell is in a dynamic ‘on state’ in which the 
resistance is very similar to the resistance in the crystalline state.  However, it is a 
volatile phenomena and the cell is still amorphous.  As the current is further increased, 
the cell temperature increases above the crystallization temperature due to joule 
heating and permanent crystallization (switching) occurs.  For clarity, Figure 1.3 
 9 
shows the current scan extending into the temperature region where melting occurs.  
However, to SET the cell, the current must only be large enough to cause heating 
above the crystallization temperature (Figure 1.2).  To read the state of the cell, a 
voltage (Vread) that is smaller than the threshold voltage is necessary to obtain an 
unambiguous response and to avoid inadvertent switching.  Applying a voltage that is 
larger than Vth typically results in sufficient current for crystallization. 
 The mechanism of threshold switching is not yet completely understood. It is 
thought that threshold switching is due to carrier multiplication through inelastic 
scattering as a result of the electric field53. There have been several theoretical 
studies52, 54-56 of threshold switching, but they do not agree on the exact details of this 
mechanism.  
1.3.4 Common phase-change memory cells 
 There are several different designs for phase-change memory cells, but they 
roughly fall into two categories: horizontal57, 58 and vertical31, 46-48 cells.  Figure 1.4 
shows a schematic for a basic vertical and horizontal cell.  In one kind of horizontal 
cell, often called a “T-cell” (left in Figure 1.4), a thin film of phase-change material is 
contacted by a bottom electrode, the heater.  During the phase-change, current is sent 
through the heater causing localized heating and phase-change in the active material.  
Similarly, the vertical cell forces the current through a narrow neck to localize the 
phase transition. 
https://lh3.googleusercontent.com/notebooklm/AKXwDQF5cR2Yvqwzh61LGbWe9wOYgNrLnCAzBQbPDN3pe0dunYOHDg0Jq5YIWJDp3Vs0_EODwNRHICS33iBVu1TZfk32SoP1w6CwZSohhRIY1i2UnmPVTX1UKOfZSK8vGZUZg_a9coHhMw=w797-h419-v0
39efd1a4-8372-40a7-9d76-ab35ba2d6722
 10 
  
Figure  1.4: Schematic of vertical (left) and horizontal (right) phase-change memory cells.  The light red shows the approximate region where the phase-transition occurs.  
Vertical cells are standard in industry, because they require significantly less 
area on the wafer.  However, horizontal cells have received significant attention due to 
their ease of manufacture and low power consumption, because heating is confined to 
the phase-change material only.  In this dissertation, we focus on horizontal cells, 
because they allow for a direct observation with the TEM and scanning probe 
microscopy without destroying the cell.  In fact, one of the main accomplishments of 
this dissertation is the development of a horizontal line cell that can be switched in situ 
the TEM repeatedly to study the details of the microstructural changes during 
switching (Chapter 2). 
1.3.5 Materials 
Phase-change materials are one of the most important aspects of PCM, because 
they dictate switching speed, power consumption, scalability and endurance.  Thus, 
finding the best possible phase-change materials will be a decisive factor in the 
 11 
success of PCM.  In the past, the discovery of new phase-change materials was mostly 
driven by optical storage applications.  However, the requirements that define a good 
phase-change material are similar for optical and electronic applications.  It turns out 
that the most popular materials for optical applications also show exceptional 
electronic performance.  However, it is not clear that these materials will have 
optimum performance for PCM. 
So what makes an excellent phase-change material for PCM?  Speed, long data 
retention, and endurance are critical in any memory technology. Since the SET 
operation is the time limiting step as discussed in section 1.3.2, a fast crystallization 
speed is paramount for overall performance.  For PCM to be competitive in the 
marketplace, the crystallization time needs to be on the order of nanoseconds to 10s of 
ns.  It should be noted that most materials that crystallize quickly do so because of a 
large driving force that is due to the difference in their Gibb’s free energy.  
Unfortunately, this also means that the amorphous phase is metastable, which brings 
us to the second requirement: the metastable amorphous phase must show sufficient 
data retention. Specifically, it must stay in the amorphous phase for 10 years at 85ºC. 
The conflict between fast crystallization and data retention helps explain why so few 
materials are well suited for PCM. While the latter requires a relatively stable 
amorphous phase, the former means that phase-change materials are inherently bad 
glass formers: in order to switch to the amorphous phase a cooling-rate on the order of 
1010 K/s has to be achieved. Additional requirements for PCM materials relate to 
device endurance. For one, PCM materials must be chemically inert with the 
surrounding materials.  The RESET operation, which requires melting, is particularly 
 12 
prone to induce chemical reactions and mixing with surrounding materials (i.e. the 
contacts or encapsulation) severely reducing the endurance of the device.  Since 
several phase-change materials are binary or ternary materials, another requirement for 
long endurance is that the material must not phase-segregate during re-solidification.  
Phase-change materials have shown endurance over 109 cycles59, but 106 cycles is 
more common in many cells.  Few materials meet these stringent requirements. 
The exceptional properties of phase-change materials typically arise from 
structural properties that are shared between several of the most popular materials.  
Unlike most other semiconductors, which tend to share the same short range order 
present in their crystalline states with their amorphous phases, phase change materials 
usually have widely different local bonding orders in each of their phases60. Typically, 
the crystalline state is an octahedral arrangement characterized by a high vacancy 
concentration and resonance bonding61, while the amorphous state is a more 
covalently bonded, tetrahedrally coordinated arrangement. This difference in local 
bonding order is responsible for the large optical contrast between the crystalline and 
amorphous phases12. 
 
 
https://lh3.googleusercontent.com/notebooklm/AKXwDQHvrHbLnmlKtiivR109zsHhszNXVRm5_Xwm4U40KEFygtJdHcgd8K6vlL_vVFVSiZMttB7rstg_Y7Gg4iwrf5KsR0Fc4J9uGm8lsDRztKHE01MWBna-KMXl1sjoCsgNK2JD83hw=w634-h506-v0
4d639fe5-1271-4926-9d4d-cfdc0b609457
 13 
 
Figure  1.5: Ternary phase-diagram for Ge, Te, and Sb showing important compositions.  
The most widely used phase-change materials come from the Germanium-
Antimony-Tellurium (GST) family; Ge2Sb2Te5 (GST225) is most popular.  Figure 1.5 
shows a ternary phase-diagram between Ge-Sb-Te to illustrate some of the most 
important compositions. The green oval indicates a range of material composition that 
is used for rewritable optical storage disks in industry, and the red line shows 
compositions used for PCM. While most stable compositions in the GST family are 
phase-change materials, the pseudo-binary line between GeTe and Sb2Te3 has shown 
fast switching and little phase-segregation upon repeated switching.  Hence, for our 
study we focus on GST225 for its superior properties and on GeTe and Sb2Te3 for 
their simplicity and significance as the building blocks of GST225.  
https://lh3.googleusercontent.com/notebooklm/AKXwDQEcwQnz0WUiZnIk_OlboTYCcz_Mvaw2UXRumZE6Pi2bS_ZioTuOhQfK1NiYCnsrXcujPY65lgLCkBHI2EC0xJB9DLiGvOZGSR7qEQq-aCnPLTMik3JkSbTBek-kXl2KoyNsznYWXg=w735-h498-v0
01a735bf-9498-4446-a56f-28cc8b42ee46
 14 
1.4 In situ TEM 
1.4.1 Introduction and motivation 
Common electronic measurements on phase-change memory treat PCM cells 
as black boxes; microstructural changes inside the devices remain hidden (Figure 1.6).  
In situ TEM has been shown to be a powerful tool to understand the microstructure 
evolution during dynamic processes such as electroplating62, nanowire63-65 and 
nanocrystal66 growth.  Indeed, with its high resolution, selected area diffraction and 
other attachments such as energy dispersive X-ray spectroscopy, the TEM seems to be 
an ideal research platform to study the details of the phase-change. 
 
 
Figure  1.6: Schematic comparison between conventional PCM measurements that treat the memory element as a black box and in situ TEM measurements that supply detailed information on microstructural changes during switching.  
 15 
We have developed an in situ TEM technique enabling direct correlation 
between microstructural changes and electrical behavior.  To make these in situ 
measurements possible, we obtained a custom made in situ electrical biasing holder 
(section 1.4.2), manufactured TEM windows (section 1.4.3), and designed and 
manufactured PCM cells compatible with in situ TEM (discussed in sections 1.4.4 and 
2.2). 
1.4.2 In situ TEM holder 
The in situ TEM experiments presented in this dissertation were performed at 
two locations with two different customized electrical biasing in situ holders:  The 
study on GeTe NWs (Chapter 3) was done at the National Center for Electron 
Microscopy at Lawrence Berkeley National Laboratory using their equipment, and the 
study on conventional GST225 cells was done at the Stanford Nanocharacterization 
Laboratory (SNL) with a custom e-biasing holder purchased from Hummingbird 
Scientific. 
https://lh3.googleusercontent.com/notebooklm/AKXwDQEGigppcEcQvvJhCGnKuzcjzvT_1LRSrYPLQrV82-18w1o6PY-EW7agtCkUgjAl4jf-yjlMWf8PeWS5YXSpH7EdMh9-jSijbZo1dTUD5dRsnPbG8bi6KYUuYCrYZyk7AE3cjyA-=w461-h722-v0
0738fa27-fa81-429c-baa9-29edc3ee2483
 16 
 
Figure  1.7: Photograph of custom electrical biasing holder and SEM images of TEM Si3N4 window used in the holder.  The light squares in the SEM image are gold pads for making electrical contact via wire bonding.  
Figure 1.7 shows a photograph of the holder used at SNL.  It has 5 co-axial 
feedthroughs and one common ground.  The TEM window that contains the PCM 
cells is glued into an epoxy breadboard and then wire bonded to the contacts. 
1.4.3 TEM window manufacturing 
Silicon nitride TEM membranes can be purchased directly (i.e., Structure 
Probe, Inc.) or fabricated via standard semiconductor fabrication processes67-70.  (Note: 
David Schoen performed this part of the fabrication at the Stanford Nanofabrication 
https://lh3.googleusercontent.com/notebooklm/AKXwDQFun3g5ZtY66wxMJeY9EdWOXro_ETT-IkLvHOmtesrN4KV7fI0aykkhGsSeaOoSR-SK18ERU0NnMXX70XdNI_dMNBG6ylQs3pNkNLAwamlf96DnE6_24F59WAAIXilZE3dD5D30dQ=w407-h470-v0
e8bec23d-f476-4242-ac43-816dd45f9e03
 17 
Facility.)  For the in-house fabrication, a low stress 50nm silicon nitride film is 
deposited on the front of the wafer.  This film acted as the TEM transparent membrane 
after the Si substrate was removed via a KOH etch.  Figure 1.8 shows a schematic of 
the finished membrane. 
 
Figure  1.8: Schematic of silicon nitride membrane on silicon substrate.  a. Cross-section of silicon substrate.  b. Top-view of substrate with gold pads. 
 
To define where the KOH will etch, a second silicon nitride film is deposited on the 
backside of the wafer.  Part of the silicon nitride film is removed so that the remainder 
can act as an etching mask for the KOH etch.  KOH results in a highly anisotropic etch 
for silicon leading to the geometry depicted in Figure 1.8 for a silicon (100) wafer.  
The Au electrodes for electrical contact (Figure 1.8b) are deposited directly onto the 
50 nm thin SiNx. 
 18 
1.4.4 History and challenges of in situ TEM technique 
 Despite the appeal of in situ TEM techniques for studying the microstructural 
details of the phase-change mechanism, there have been relatively few efforts in this 
direction.  The reason for the lack of in situ studies may be the inherent difficulties 
that arise.  Before discussing these challenges later in this section, we will briefly 
mention the prior work that has been done. 
 An interesting in situ TEM study was presented by Samsung Group at the 9th 
Annual Non-Volatile Memory Technology Symposium in Pacific Grove, November 
2008.  They used a focused ion beam (FIB) to cut a conventional, vertical PCM cell 
out of a wafer and observed it in situ TEM while applying voltage pulses with a 
specialized scanning tunneling microscope tip.  Using this method the group could 
observe the reversible phase-transition, but no major findings were reported in the 
literature.  A problem with this technique is that the Gallium beam used in the FIB can 
short out the cell and thereby significantly change its properties. Finally, cutting 
individual cells out of a wafer with a FIB is difficult, so the throughput is low.  
Besides the work by Samsung, it is difficult to find further reports on in situ switching.  
However, it should be noted that other researchers have used the FIB to cut individual 
cells from a wafer before and after switching71.  This allowed them to obtain snapshots 
in time of the cell during its life-cycle. 
 For an in situ TEM study, the more natural geometry is a horizontal PCM cell, 
because it allows for direct observation with the TEM as long as the substrate is 
transparent.  No further modification to the cell is necessary.  However, the challenges 
for making an in situ TEM cell are numerous.  The fabrication process (outlined in 
https://lh3.googleusercontent.com/notebooklm/AKXwDQGov3oad1MyOgO5AasSmETij7RvAxYKUYgKFCV3rTO8RCGp6ezh66ffCAPPk4J8-AnZJEFDT-OXS175sI0wy6vi5w_asV7nnuQnyzDP7_FIWfnB1N1xcKGhljySVPdsUk8D0R6w3w=w782-h467-v0
d8a22721-a271-41ab-a4d5-65054f1c747c
 19 
section 2.2.1) requires electron beam lithography (EBL), which is relatively difficult 
to do on 50nm thick membranes because they are very fragile.  The finished TEM 
chips are very small and need to be handled repeatedly for EBL, lift-off, gluing into 
the carrier, and wirebonding.  The fragile nature of the membranes means that a low 
yield is to be expected and must be accounted for by making extra devices.  Once the 
devices are wire bonded and ready to be inserted into the TEM, they become very 
prone to electro-static discharge which also leads to immediate breakage.  This can be 
overcome by trying to keep the contacts grounded at all times before pulses are 
applied. 
 
Figure  1.9: Design challenges for in situ TEM PCM cells.  
Finally, there are several requirements for a working PCM cell that lead to 
design constraints (Figure 1.9).  For one, the repeated melting and high temperatures 
during the RESET operation require a strong encapsulation.  Otherwise, the material 
can evaporate and/or ball up, breaking the cell.  Hence, the simplest structure would 
 20 
consist of a TEM membrane, a phase-change layer and an encapsulation layer.  This 
stack needs to be transparent to the electron beam which means the maximum total 
thickness should be kept to less than approximately 200nm.  To maximize the TEM 
contrast, it is advisable to maximize the thickness of the phase-change material with 
respect to the other layers.  However, to achieve sufficient cooling rates, the thickness 
of the phase-change layer must be kept to a minimum.  To increase the cooling rate, 
we can add lateral contacts that act as a heat sink and an electrical contact.  The final 
PCM cell design that we chose to satisfy all these requirements is discussed in Section 
2.2.1.  
1.5 Vapor-liquid-solid growth 
1.5.1 Introduction 
 The VLS growth20 is a fairly simple method to produce a wide variety of 
nanowires.  Figure 1.10 shows a schematic of the basic VLS growth set-up employed 
in this dissertation. 
https://lh3.googleusercontent.com/notebooklm/AKXwDQERYfq8HBTMYVnw6hyMAULJPre9hRRIfVKE3mCHMuTw4GtTaLLvS5abAwNOF1twsnB89bgWughtL-AJ89uK8cEenPETwg8qNmLHs11iX7asktaQtrTjjc8x_VBViT3iq8oosbfx=w1250-h675-v0
61553ad7-66f1-4b82-b734-fb973f1e362e
 21 
 
Figure  1.10: Schematic of VLS growth furnace and plot of temperature distribution inside furnace  
We used a 1 inch horizontal tube furnace (Lindberg/Blue M) that has a non-uniform 
temperature profile.   We measured the temperature profile (Figure 1.10) for various 
setpoints ranging from 900ºC to 400ºC.  While the temperature in the center is close to 
the set point, the temperature decreases with distance away from the center.  This is 
ideal for the VLS growth, because it enables us to evaporate the source material at the 
set point and allows us to finely tune the temperatures at the growth substrates simply 
by varying the position.  With the source material (i.e. GeTe or Bi2Se3) placed in the 
hot center region, we flow argon carrier gas through the furnace to transport the source 
vapor to the growth substrates.  The growth substrates are typically Silicon. They are 
prepared with Au nano-particles, which have been shown to be a universal VLS 
catalyst for many material systems. 
https://lh3.googleusercontent.com/notebooklm/AKXwDQGWTEBL9iFWlYpdRBUtJz-WD7duSAMNvu4ZYuAkPkfO_31mJrPFo1hVJBpAFXlSPw4MDXCYP6tFjVKDW_cWwv1vBLO7mSUI9dE2rH05AhyrB9FPlpUxj-NOPqnTkFAlEUcL_JEBIg=w423-h634-v0
6c9bd426-c4a2-4341-95e5-f592ffa760ae
https://lh3.googleusercontent.com/notebooklm/AKXwDQGZS2I9BFGvqcAiO1BdjYmn9J_m3YVVhkCTEILWpAsO9XSsUVBZYMnnV9ZFjwTLl_2AkfyGgB-I3vc8Uk2kVpspbm8uHdDUY2PHhyJz1SRrqjaK5eEQvmqQJVte7XEdsiPGmzN8cw=w421-h633-v0
4a050e97-600a-4f24-81b2-f871f9e34c23
 22 
 For the VLS mechanism to work, the source material must have a eutectic 
point with gold.  As the vapor streams over the gold catalysts, it is absorbed and 
incorporated into the particle.  When the composition changes, the catalyst turns to 
liquid.  As the amount of source material in the liquid increases, the nanowire begins 
to nucleate and grow.   
 
Figure  1.11: SEM of early growth stage of GeTe NWs (left: top view; right: side view)  
Figure 1.11 shows an SEM of the early growth stages of GeTe NWs with the gold 
particles at the tip and the base of the wires extending from the substrate.  The gold 
particle remains at the tip during the whole growth process and NWs can grow up to 
100s of micrometer long. 
1.5.2 Growth parameters 
 The growth parameters used for each synthesis will be discussed in the 
corresponding chapters (Sections 3.2 and 5.2).  Here, we briefly describe general 
500 500 
 23 
considerations regarding the growth parameters for VLS growth.  The major growth 
parameters include temperature (of source material and substrates), pressure and flow 
rate of the carrier gas. 
Temperature 
Pres su 
re Fl 
ow  ra 
te Fl 
ow  ra 
te 
 
Figure  1.12: Schematic of major growth parameters.  The growth only works if the parameters are all in a “target range” indicated by the blue ellipsoid.  
Generally speaking, there is a certain range for these parameters where growth can 
occur successfully (indicated by blue ellipsoid in Figure 1.12).  If the parameters are 
outside this narrow range, VLS growth will not work: the catalyst may not be active 
enough, insufficient (or excessive) material may reach the catalyst, the temperature 
may be too hot or cold, leading to evaporation of the nanowire or thin film deposition 
of material everywhere, and so forth. 
Interestingly, the reported growth conditions for a given system vary widely 
between groups.  The reason for this is probably the presence of many other 
parameters that are typically not discussed in detail because of their complexity and 
unknown contribution to growth.  These parameters include the flow dynamics inside 
the furnace (they are influenced by the geometry of the furnace and position of 
substrates, etc.), substrates (cleanliness, oxide quality, etc.), catalysts (size distribution, 
https://lh3.googleusercontent.com/notebooklm/AKXwDQEinN4d8l2MbpAKXtDsnLLoUJ7j6dKO0bnnsDs6GvXXul0m6GLt7eSDRoUqwSXciW4cE-9eB0j0sDJxxgp3PWvTJHoDsRoql-9IxBXPzE0mqTxPIc4x32yb8Y89l_hjU7pZbQjJAA=w230-h218-v0
0a678da0-06f7-443b-afed-33a9102574c6
 24 
quality, etc.), precursor (amount, quality, condition, etc.), and even the “seasoning” of 
the growth chamber (for example, possible residues from prior growth).  We will not 
discuss the effect of these parameters in detail, but the reader should be aware of their 
importance. 
1.6 Topological insulators 
1.6.1 Introduction 
Topological insulators are materials that are insulators in the bulk but have 
conducting surface states.  Figure 1.13 shows a schematic representing the band 
diagram of a general topological insulator.  The diagram looks similar to that of a 
regular semiconductor in that the Fermi level is located in the band gap between the 
conduction and valence bands. However, topological insulators also have surface (in 
3D) or edge (in 2D) states as described by the blue and red lines inside the band gap.  
These surface states are due to strong spin-orbit coupling, and exhibit extraordinary 
properties such as dissipationless current and the quantum spin Hall effect. A more 
detailed explanation of topological insulators is beyond the scope of this dissertation 
and we refer the reader to several excellent papers72-78. 
https://lh3.googleusercontent.com/notebooklm/AKXwDQFHbhPXtK2WiN8v5gMYcsqNidhngJy9N5X-C5zHL3AT46Phl6SKOT_rM5-bKKgOuMjjImudte9fjuMnfDpITO1-Cd6PCkHpMaLPAWnnl8zIDnWvcLbVhzJ9wU9gQ9q6QRFmYc0tuw=w320-h483-v0
d093650e-b194-4ac7-bd7a-e4fe138e80b2
 25 
 
Figure  1.13: Schematic of simplified topological insulator band diagram.  
The short history of topological insulators has been interesting and impressive 
in many ways.  While most major findings in solid state physics were discovered 
experimentally, topological insulators were first conceived theoretically in 2005, and 
quickly became one of the hottest topics in physics.  Science Magazine voted 
topological insulators a runner-up breakthrough of the year.  Philip Anderson 
(Princeton, 1977 Nobel Prize in physics) believes that “as a technical achievement, or 
a series of physics achievements alone, it is pretty spectacular.”  Thomas Rieker 
(program director for the National Science Foundation's Materials Research Science 
and Engineering Center) claims that “this discovery has the potential to transform 
electronics, data storage and computing.”  Hari C. Manoharan (Associate Professor of 
Physics at Stanford) states that work on topological insulators “could lead to 
breakthroughs in areas as diverse as spintronics, quantum information and even 
particle physics — theorists have predicted that an exotic type of particle that is its 
 26 
own antiparticle (a Majorana particle) might be observed in topological insulators79.” 
Stanford Professor of Physics Shoucheng Zhang believes that topological insulators 
have the potential to replace the standard CMOS transistors that power today’s 
integrated circuits with more efficient switches that dissipate significantly less power. 
These statements from leading experts demonstrate the tremendous potential that 
topological insulators offer in electronics and other areas.  However, the field is still 
very young and it is not certain where or when topological insulators will have the 
greatest impact.   
1.6.2 Materials 
 While the research for this dissertation was underway, only a handful of 
topological insulators were known (BixSb1-x, HgTe, Bi2Se3, Bi2Te3, Sb2Te3).  Since 
then many other materials80, 81 have been predicted to show topological insulator 
behavior.  Of the five initial materials, Bi2Se3 was the best choice for our study due to 
its fairly simple band structure with the Dirac point located at the Г-point, and its 
relatively large band gap of 0.3 eV18, 82, possibly allowing interesting observations at 
room temperature.  Figure 1.14 shows the crystal structure of Bi2Se3. 
https://lh3.googleusercontent.com/notebooklm/AKXwDQFxaMIEGPDyW1UkE-r4GhY23jxYA0TtcbeISTA36ZwRVkXP3xe7rI095pU1bh4NVxVoy6-k4s80yBgtr6uOSpErjoe1HE0xPXvvMQTFQMMIz8UIFhkBYJBxEbCvcjE_2vWwTToh=w420-h834-v0
abf5e8d3-63e6-474d-942c-cee2948a2170
 27 
 
Figure  1.14:  Schematic showing crystal structure of Bi2Se3 
 
It is a layered material that has a rhombohedral phase with the space group 
D3d 
5 (R-3m)83 consisting of planar, covalently bonded quintuple layers linked 
predominantly by van der Waals interactions.  Each quintuple layer is made up of a 
Se-Bi-Se-Bi-Se stack and is approximately 1 nm thick. 
1nm
 28 
2 In situ transmission electron microscopy of phase-
change memory  
2.1 Introduction  
Phase-change memory (PCM) has been researched extensively as a promising 
alternative to flash memory.  Important studies have focused on its scalability46-48, 84, 85, 
switching speed46, 86, 87, endurance46, 48, 87 and new materials46, 86-88.  Still, reliability 
issues and inconsistent switching in PCM devices motivate further study of its 
fundamental properties.  However, many studies treat PCM cells as black boxes; 
microstructural changes inside the devices remain hidden.  Here, using in situ 
transmission electron microscopy (TEM), we observe real-time microstructural 
changes in lateral Ge2Sb2Te5 (GST) PCM bridges during switching.  We find that 
PCM devices with similar resistances can exhibit distinct threshold switching 
behaviors due to the different initial distribution of nanocrystalline and amorphous 
domains, explaining the variability in switching behaviors of PCM cells in the 
literature.  Our findings show a direct correlation between microstructure and 
switching behavior, providing important guidelines for the design and operation of 
future PCM devices with improved endurance and lower variability. 
While the atomistic mechanisms involved in the phase transition have been 
studied in great detail89-94, few experiments show what the microstructures of the 
amorphous or crystalline regions look like before and after switching.  However, 
knowing the detailed microstructure is important because it relates directly to 
https://lh3.googleusercontent.com/notebooklm/AKXwDQGC2TeYHyZtX7Qo9x-lpQms36LySEu7ihP504r24vdHCen42L0rmJF2oxJHM0XpBSDfAft7Vzo0RKvSypnu6g-uW2MywiY_QdECwY7jrQnCD4lK6FMUebTtM614GmAyesxJz_m9VQ=w519-h241-v0
3511b305-a0a8-42fd-9c55-1619509fd48a
 29 
electrical properties such as the electric field required to induce threshold switching, 
sources of variability in switching and the origin of resistance drift95, 96, a common 
problem with PCM in which the resistance of the amorphous phase increases over 
time.  In an effort to study the microstructure, researchers have obtained TEM images 
by cutting individual PCM cells out of a chip with a focused ion beam71, 97, 98.  This 
technique provides a snapshot in time of individual cells, but it does not allow for a 
direct correlation between microstructure and electrical behavior during repeated 
switching. A variety of in situ TEM techniques have been shown to be very powerful 
for understanding the microstructure evolution during dynamic processes such as 
electroplating62, nanowire63-65 and nanocrystal66 growth.  
 
Figure  2.1: Device schematic showing silicon substrate with 50nm silicon nitride membrane suspended at the center and GST bridge that is fabricated on the membrane.  
We have developed a fabrication process for making single nanostructure 
electrical devices on TEM membranes29, 99. In our effort to study the detailed 
microstructure during repeated switching, we fabricated 50 nm thick lateral GST 
phase-change memory bridge devices on 50 nm thick Si3N4 electron transparent 
membranes (Figure 2.1) allowing us to directly correlate electrical behavior with 
structural changes by in situ TEM. This geometry forces the current through a narrow 
https://lh3.googleusercontent.com/notebooklm/AKXwDQFjqs5CgHVIWcK_57oW79dSn0DHALQYs92qryY69FzQNndPs0eHSPkRTgUjCQwPIB_rjzoaSxwoX_YuDQ5kmfRuWPahILat4sXlqXUQyt22Ui4Rs1c5i8PKh1hKvYazbwR96_Sy=w770-h315-v0
7174a184-f227-4b36-856d-76da465116d2
 30 
region of GST so that sufficient heating to induce the phase change occurs in the 
bridge only, while the rest of the device remains crystalline at all times. 
2.2 Method 
2.2.1 Device fabrication 
We used standard 50nm low stress silicon nitride membranes on 200μm silicon 
frames as substrates (described in Section 1.4.3).  Photo-lithographically patterned 
100nm gold contacts were evaporated onto the substrates to allow contact to be made 
between the in situ electrical biasing holder and the PCM bridges (Figure 2.1).  We 
used electron beam lithography and a lift-off technique to pattern the TiN contacts and 
Ge2Sb2Te5 cells.  Both films were sputtered from stoichiometric targets in an AJA 
sputtering system.  After lift-off, the devices were encapsulated by a 20nm layer of 
sputtered SiO2 (Figure 2.2). 
 
Figure  2.2: Schematic of device cross-section (left) and SEM image of complete device (right). Cross section is taken along the dotted line.  
The as-sputtered Ge2Sb2Te5 layer is amorphous leading to a prohibitively high 
threshold voltage that can lead to destructive switching.  In order to allow repeated 
https://lh3.googleusercontent.com/notebooklm/AKXwDQHrrJBFgR2OGRJUfcrbVXAlzNk8pGwVa54-c9dLyZ8wFOv34cg2N4lgQ9v-tru4OpihJPygijjDMyiytjuiu_fBjZRECQZwfF6vRao1FMTrvQjRIrshH0Oy2F1gD_nlE981XNW5SA=w1006-h276-v0
815f2759-3096-4dbc-a5cd-dd640f6f986d
 31 
switching, the devices have to be annealed initially to achieve full crystallization.  In 
later switching, the amorphous region will be confined to the bridge region only, 
resulting in smaller threshold voltages.  To achieve initial crystallization, we heated 
the completed devices on a hot plate at 180ºC for 10 minutes. 
2.2.2 TEM characterization of sputtered GST films 
To confirm the composition of our films and characterize their crystal structure 
we performed careful energy dispersive x-ray spectroscopy (EDS) and diffraction 
analysis of sputtered GST films that were annealed on a hot plate at 180°C for 10 min. 
 
Figure  2.3: TEM characterization of annealed GST 225 film after sputter deposition. a, b. Bright-field TEM images of as-deposited GST225 film after annealing on hot plate at 180ºC for 1 min. c. SAD of GST225 film could be accurately indexed to face-centered cubic phase of GST225.  No other phase was observed.  
Figure 2.3 shows bright-field TEM images of the sputtered GST225 film after 
annealing it on a hot plate at 180°C for 1 min.  The grain size shows a distribution that 
ranges from a few nanometers to 10s of nanometers.  The EDS analysis indicated an 
elemental composition of 21, 21, 58 at.% of Ge, Sb, Te respectively.  GST225 has a 
nominal composition of 22, 22, 56 at.%, so the data agrees with GST225 to within the 
experimental error of ~2%.  We also took selected area diffraction (Figure 2.3c).  The 
rings could be accurately indexed to the cubic phase of GST225.  Figure 2.4 
https://lh3.googleusercontent.com/notebooklm/AKXwDQH8QgkERq1Wt5hiqUODfx2Nypi-TmNTuKgxBoq4UqFdhVOWDP1vG2M4ya1KaCPhUH6pmLlNOyiuy9jaR6HS5UR71ooNRB1Y6w0c9G74brVd9AmDWBt7fAAvkkLnrtf29lrpZiDVZw=w847-h437-v0
971b174f-87f5-423d-98be-163607ec276f
 32 
summarizes the d-spacings calculated from the measured ring diameters and compares 
our values to the theoretically predicted values. 
 
Figure  2.4: Table summarizes measured and theoretical d-spacings of cubic phase of GST225 
 
Each ring agrees very nicely with theory to within approximately 1%.  The rings 
corresponding to the (331), (531), and (533) planes could not be observed, because 
they either had low intensity or due to their close proximity to a different, brighter ring. 
Besides the cubic phase of GST225, no other phase was observed.  The EDS and SAD 
analysis corroborates a composition of Ge2Sb2Te5 to within approximately 2 atomic 
percent experimental error. 
2.2.3 Electrical testing and TEM observation 
The completed devices were glued with carbon paste into a custom electrical 
biasing holder.  Electrical contact was established via wire bonding between the holder 
and the gold pads on the substrate.  We used a FEI Tecnai G2 F20 X-TWIN TEM 
 33 
operating at 200kV for in situ observation.  Pulsing and IV measurements were 
performed with a B1500A parameter analyzer (Agilent Technologies) equipped with a 
B1525A semiconductor pulse generator unit.  For amorphization pulses, the rise and 
fall times were 20ns; for crystallization pulses, the rise and fall times were 500ns.  
Resistances were measured at a bias of 0.1V.  To ensure that the switching 
measurements were not influenced by the TEM’s electron beam, we performed several 
control experiments in which we switched repeatedly with the column valve closed 
(i.e. electron beam blocked by the column valve).  We did not find any significant 
difference in switching behavior with the column valve closed or open and conclude 
that the electron beam plays no significant role in our measurements 
2.3 Switching experiments 
2.3.1 Demonstration of in situ switching 
To demonstrate the feasibility of in situ switching, we applied short voltage 
pulses to devices in the crystalline state inside the TEM.  Figure 2.5a shows an 
example of a crystalline bridge with typical resistances ranging from 20 kΩ to 80 kΩ.  
The bridge consists of a large number of micro-crystalline grains with different 
orientation resulting in a granular contrast in the TEM.  After applying a 5 V, 400 ns 
square pulse, the bridges turned to an amorphous state (Figure 2.5b) and the resistance 
increased to between 0.5 and 8 MΩ. 
https://lh3.googleusercontent.com/notebooklm/AKXwDQE5fSse4MBK35Duj4oWAHkapWMbVJ-9eCJYJi4Z2DItFX-CyEJ5dbHUW08Ult5fSZpkdBaTBi7emho9JG7jvKPyY1B-4wL8XzNvzoJAhKqaYWs-R45TdzIYTDiTju5fOOaVNlbFJQ=w587-h557-v0
ed4f1f7d-015c-43e1-b3f3-4febcab527ec
 34 
 
Figure  2.5: TEM images and SAD of switching between crystalline and amorphous phase. a, b. TEM image showing a bridge in the (a) crystalline phase and (b) amorphous phase. Typical resistance values for crystalline and amorphous phases are 10-100 kΩ and 1-8 MΩ respectively.  The red circles indicate the approximate size and location of the selected area diffraction aperture in (c) and (d) c, d. Selected area diffraction confirming the poly-crystalline (c) and amorphous (d) nature of the bridge.  
The amorphous region shows a uniform contrast in the TEM.  The edge of the PCM 
bridge looks darker, because a thin side-wall of GST remained from the lift-off 
fabrication process.  Switching back to the crystalline phase was accomplished by 
either a longer voltage pulse (2 V, 1-10 μs) or a current scan to approximately 100 μA.  
To examine the crystallinity, we obtained selected area diffraction (SAD) of both 
states (Figure 2.5c and d).  The spot pattern (Figure 2.5c) is due to a polycrystalline 
phase and the diffuse ring (Figure 2.5d) is due to an amorphous phase.  The SAD 
confirms that the phase change was successful.   
https://lh3.googleusercontent.com/notebooklm/AKXwDQHxKhFzSWgjH71WncizLie1TY0hPVd_ht-X6LtexxQN0klcvW6wffciVMJGcHH-yFCSaAYH0IztGfjQxDlKX5KCp6bRtf4z1nFtWbr224wk0KFkUaPN7tN5WBZofjtHNwz3-FBs=w621-h290-v0
0785e4cc-ff79-46fa-879d-f4498b66e867
 35 
2.3.2 Two types of amorphous phases 
After switching back and forth dozens of times, we observed that applying an 
amorphization pulse did not always result in a single-phase amorphous domain as 
depicted in Figure 2.5b100.  Instead, about half the time we obtained a two-phase 
amorphous/crystalline domain consisting of an amorphous matrix with nanocrystals 
interspersed throughout the bridge.  Interestingly, despite the significant differences in 
microstructure, in both cases the resistances were on the order of MΩ. 
 
Figure  2.6:  TEM images of two-phase amorphous/crystalline (left) and single-phase amorphous (right) domain.  The coloring is provided to give an estimate of where the material is amorphous.  
The two-phase amorphous/crystalline and single-phase amorphous domain in the same 
cell are depicted in Figure 2.6.  We will address the consequences of this variability in 
the character of the amorphous phase for the switching properties of the cell in the 
following sections.  However, first it makes sense to look at the dependence of the 
phase transition on the applied voltage pulse to understand how the crystalline to 
amorphous transition occurs and why we observe differences in the microstructure. 
https://lh3.googleusercontent.com/notebooklm/AKXwDQF6PxAqy_B4KvUijJLJ1SnwW3el-j4epBcfYwa4hcrfRrRdPmqZKQi3uBs2I7OchFeJAtlVhaSFTWxbsMpMyNiXtNYjuxhZtqznufXab5lrSwEFW8AL7uiTnCUTUc7hqRfSR5ch=w499-h382-v0
ce7b5572-67a0-4391-a273-c06102e19bdb
 36 
2.3.3 Dependence of phase transition on voltage pulse 
A typical PCM experiment often performed as a general characterization 
method is to measure the resistance as a function of the voltage pulse amplitude.  In 
such an experiment, a cell in the crystalline state is subjected to progressively higher 
pulses. After each pulse, the resistance is measured. If the resistance increased, the cell 
is re-crystallized (via a longer pulse or current scan) before the next, larger pulse is 
applied.  Figure 2.7 shows a schematic of what the data from such an experiment 
might look like. 
 
Figure  2.7:  Schematic of typical PCM resistance as a function of applied voltage pulse.  The crystal structure between crystalline and amorphous is unknown.  
At first the resistance remains constant at a low value independent of the applied 
voltage pulse, because the cell is completely crystalline and the voltage pulse is too 
small to cause sufficient heating to melt the material.  When the voltage amplitude 
reaches a certain value, the resistance starts to increase.  In this transitional region, it is 
believed that a small amorphous phase is formed that increases the resistance53, 101: the 
higher the voltage pulse, the larger the amorphous region.  Once the voltage amplitude 
 37 
becomes large enough, the resistance levels off at a high value, because essentially the 
whole region has been transformed to the amorphous state.  We indicated the 
transitional region in Figure 2.7 with a ‘?’, because it is not clear what the distribution 
and size of the amorphous region looks like.  However, our in situ TEM method 
allows us to observe the detailed microstructural changes during such an experiment. 
To observe the details of the crystalline to amorphous transition and to 
measure the dependence of resistivity on the voltage pulse, we applied 400 ns pulses 
of increasing amplitude to a crystalline device with an initial resistance of 62 kΩ.  
Whenever the resistance exceeded 200 kΩ we re-crystallized the device by scanning 
the current to 100 μA before pulsing it again.  The curve shows typical PCM behavior: 
the general trend is that a higher pulse amplitude leads to a higher resistance which 
correlates with increasing amorphization (Figure 2.8a).  However, we note that the 
resistance value depends not only on the pulse amplitude, but also on the history of the 
sample.  For example, we observed a range of resulting resistances after switching the 
same cell from the low resistance state with a 4 V pulse (see multiple data points at 4V 
in Figure 2.8a). 
 
 
 
https://lh3.googleusercontent.com/notebooklm/AKXwDQF_DBgWyGEwrsfE07OXcBUssbYVV4FO5gSUvTaMYtPAvsAXI482NAhj_n04AORxMjCQyDKsc9nJ3P6tCAXv-8-0TZi3F6aYP6CP9FnzqWIG4GRBtI0ilemzcSfUUktqG11sBuUzBg=w988-h387-v0
0efa401a-a422-4abc-af38-c05ded2fc226
 38 
 
Figure  2.8: Study of crystalline to amorphous transition. a. Resistance as a function of applied 400 ns voltage pulse. TEM images (b), (c), (d) correspond to labeled points in the graph.  The red line connects the average resistance values.  b-d. TEM images of phase-change memory bridge.  Red ellipses show examples of crystals that survived the amorphization process.  Yellow circles point out small differences in microstructure that accompany resistance change from 62 kΩ to 150 kΩ.  Green dashed lines surround areas that are predominantly amorphous.  
To capture the detailed changes in microstructure as we increased the pulse 
amplitude, we recorded TEM images of the device after consecutive 3 V, 4 V, and 5 V 
pulses (Figure 2.8 b-d).  Figure 2.8b shows that the bridge was predominantly 
crystalline with a large spread in crystal size.  After a 4 V pulse, the resistance 
increased from 62 to 150 kΩ, but the change in crystallization was only minor (Figure 
2.8b,c).  After a 5 V pulse (Figure 2.8d), the resistance increased to 3 MΩ and a 
significant amorphous domain (indicated by green dashed line) interspersed with 
crystals was observed.  To confirm the crystallinity of the bridge we also obtained 
SAD patterns at various resistances after switching (Figure 2.9). 
https://lh3.googleusercontent.com/notebooklm/AKXwDQH_0TGA_-S6oi4L_fm6Q4G9Ws1XTvBbQA7chnt09KjOEBGb4AcVGkLSTcounHZxr-kGDEol6UZUdGs4yY4ay-uiWH4sSr1NSRapYgLwPT9DBtZw5mWdjwvhMqE6b7-MRrz1FGxADg=w1101-h685-v0
369769db-a928-4b22-a285-9814352b7b74
 39 
 
Figure  2.9: TEM images and corresponding SADs of bridge in various states of crystallization. a-c. Resistance of bridge in (a), (b), and (c) is 29 kΩ, 115 kΩ and 3.5 MΩ, respectively.  The SADs (approximate size and location of SAD aperture indicated by red circles) confirm the crystallinity of the states.  In (a), the bridge is essentially completely crystalline as indicated by spot pattern and absence of diffuse ring. In (b), the bridge has some amorphous background, but the SAD still shows significant crystallinity.  In (c), the bridge is predominantly amorphous with several crystals remaining embedded in the amorphous matrix.  
From these images (Figure 2.8, 2.9) it is evident that resistance is not simply 
proportional to the size of the amorphous region, but is rather a function of the 
detailed crystalline and amorphous phase distribution that determines available 
conduction pathways.  During pulsing, the larger crystals (~100 nm) survived the 
melting (some examples indicated by red ellipses in Figure 2.8 b-d).  Smaller crystals 
(<50 nm) tended to disappear (yellow ellipses in Figure 2.8 b,c) after the 4 V pulse 
indicating that some degree of vitrification occurred.  After the 5 V pulse, significant 
melt-quenching occurred, but the pulse was still insufficient to completely melt the 
 40 
larger crystals (Figure 2.8d, area encompassed by green line is mostly amorphous).  
The device could be switched back and forth dozens of times with the same crystals 
remaining in the amorphous phase.  However, after a longer pulse (500 ns), the larger 
crystals were more likely to melt completely and in that case the amorphous domain 
showed only little crystalline residue even after repeated switching.  
Careful study of Figure 2.8 b-d suggests that besides the pulse amplitude and 
time, the microstructure of the final high resistance state is influenced by factors such 
as the initial size distribution of crystals and available current paths that can lead to 
localized heating and melting.  While the resistance of the amorphous state was 
always in the MΩ range, we expect that its microstructure can have significant impact 
on the electrical behavior.  For example, the crystals that remain in the amorphous 
phase may be a source of resistance drift, as Ostwald ripening and structural relaxation 
can further change the conductivity.  These detailed observations demonstrate the 
value of the in-situ TEM technique and reveal the complex relationship between 
voltage pulses and crystallinity as a source of the variability that is often observed in 
PCM measurements. 
2.4 Threshold field measurements 
2.4.1 Significance of threshold field 
Since our method allows for an accurate observation of the amorphous phase, 
it is ideal for measuring the electric field required to induce threshold switching and 
for studying the effect of the microstructure (i.e. presence or absence of a second 
phase in of the amorphous domain) on threshold switching.  Knowing the exact 
https://lh3.googleusercontent.com/notebooklm/AKXwDQEloX-sxeZfVg0kLHmOSTUZrNJpICzAH7w4Tz9zVtAwdo9fhhsvaAwCtRmCW9O76ivj0tbUaAnAG0FucbvwzdPB-25sQwz0xaxUiDJm2ZjURYXIIGbtMDXZIzq85-nETkllLUmH=w668-h288-v0
8227b569-2788-43e4-9049-ca585fdcefc5
 41 
threshold field is important for the design and operation of PCM cells.  Especially 
lateral cells have shown a dramatic dependence on this parameter, because large 
electric fields can result in current spikes and destructive switching46. 
 
Figure  2.10: Current spikes and destructive switching due to high threshold field. Voltage response graph indicating the point at which breakage can occur (left). TEM image of a sample broken during crystallization attempt (right).  
If the electric threshold field is too large, a large threshold voltage must be 
applied.  Figure 2.10 (left) shows a schematic of a corresponding current scan.  As 
always, to SET the cell, a voltage larger than Vth has to be applied.  If Vth is too large 
this leads to a current spike and destructive switching.  Figure 2.10 (right) shows an 
SEM image after a device broke from a too large voltage pulse. 
2.4.2 Measurements 
To measure the threshold field, we first switched the bridge to the high 
resistance state, then estimated the size of the amorphous region and performed a 
current scan while measuring the applied voltage to re-crystallize the bridge.  As 
expected, we observed two different behaviors in the voltage response to the current 
scan corresponding to the presence or absence of a crystalline phase within the 
amorphous domain. 
https://lh3.googleusercontent.com/notebooklm/AKXwDQGY3nIo7ViVLoNPthpIO-ZiyWbrAMApFkQv2ccGr2yax3tNboP8rw0ORDqwp8zuozRcDldBuQglOxBcgKVbfKZENaU1Go0NEaz-slIAn7toa1eKZK3BrpAAyLPq_5_0ZxZHSreadw=w659-h594-v0
e699cb93-19d2-468b-9763-ec3d5df5049e
 42 
 
Figure  2.11: Measurement of threshold switching in high-resistance bridges. a. IV curve showing 
120 μA current scan to crystallize the bridge in (c) and to measure the threshold voltage. This bridge exhibits complicated switching behavior. b. IV curve showing 100 μA current scan to 
crystallize the bridge in (d) and to measure the threshold voltage. This bridge exhibits clean switching behavior. c. TEM image of two-phase bridge before current scan (a).  The approximate amorphous domain has been colored blue to assist with visualization. d. TEM image of single-phase amorphous bridge before current scan (b).  The approximate amorphous domain has been colored red to assist with visualization.  
If there is very little crystalline residue inside the bridge (Figure 2.11d), then the IV 
curve shows a very clean snapback52, 96 once the threshold voltage is reached (Figure 
2.11b).  At this point the entire bridge is in a dynamic conductive state that is still 
amorphous with a current of 10 μA (corresponding to a current density of 
approximately 0.04MA·cm-2); too low to produce significant heating.  As the current is 
further increased, the bridge crystallizes.  The IV-curve in Figure 2.11b shows that the 
voltage in the up-scan is close to the voltage in the down-scan indicating that the 
 43 
resistance in the dynamic on-state immediately after threshold switching is very 
similar to the resistance after crystallization has taken place. 
In contrast to the threshold switching for a pure amorphous phase, the required 
voltage to switch a mixed phase (Figure 2.11c) is much lower (Figure 2.11a) and the 
IV curve does not show a clean snapback.  These differences in electrical behavior are 
due to the complicated crystalline-amorphous mixture that can lead to conductive 
percolation paths when the threshold field is exceeded locally.  Once such a 
conductive filament exists, it causes local heating and crystallization resulting in 
continuously decreasing resistance of the bridge (Figure 2.11a). The complexity of the 
IV behavior suggests that several processes, including threshold switching, localized 
heating and crystallization, may be occurring simultaneously.  When switching back 
and forth several times, we found that the threshold voltage is nearly constant at about 
2V regardless of the resistance for a mixed amorphous phase with crystalline residue 
(Figure 2.11a).  Figure 2.12 shows two more examples of threshold switching 
correlated with crystal structure. 
https://lh3.googleusercontent.com/notebooklm/AKXwDQFdlFPsE0TE1zjHYySeftGdLWYdWBpvgY4H86j_3QBFgaubDygH9azhP6kVqPApd4WheysPpVj3P4c92RO7pO47sd4-UpX5m9TUOiCFgb3yTt-eECs7fKkIMl4AQ4KZvDsOD37ihA=w659-h583-v0
e964d9ca-8b2b-4f35-b5c2-8976e66a2778
 44 
 
Figure  2.12: Measurement of threshold switching in high-resistance bridges. a. IV curve showing 
120 μA current scan to crystallize the bridge in (c) and to measure the threshold voltage. This 
bridge exhibits complicated switching behavior, because it is in a mixed phase consisting of nanocrystals interspersed in an amorphous matrix resulting from repeated switching. b. IV curve 
showing 100 μA current scan to crystallize the bridge in (d) and to measure the threshold voltage. 
This bridge exhibits complicated switching behavior, because it consists of nanocrystals interspersed in an amorphous matrix. c. TEM image of mixed phase bridge before current scan (a). d.  TEM image of bridge before current scan (b). The bridge consists of nanocrystals that are due to annealing the as-deposited GST225 film after sputtering at 180°C for 10 min.  Despite the high density of nanocrystals, the resistance of the bridge is still very high indicating that no connected current paths exist. The nanocrystals appear as dark dots in TEM images due to the diffraction contrast.  Amorphous regions exhibit uniform contrast.  
Direct correlation between the IV behavior and the detailed microstructure of 
the amorphous phase using in situ TEM can explain the source of variability that is 
observed in conventional current scans.  With this knowledge one may form 
conclusions about the microstructure of the amorphous domain simply by studying the 
current scan response. 
https://lh3.googleusercontent.com/notebooklm/AKXwDQFBK228B7RiWBl_41Af9V6nAOQUrHttAZIZcgx15R7jAPJ6EJ04c-4KwcLrXJvFAhFa255zVilkjWkLewUUBa0ovk9nron9feBFzahpGQZgo-C2HS5snSpeqS1c7RpakdXHMlM6=w865-h337-v0
74fa54f1-2e66-45fe-9ab8-45f83a5a42c9
 45 
2.4.3 Discussion 
If the amorphous phase is relatively pure as shown in Figure 2.11d, the 
threshold voltage scales nearly linearly with the resistance. This is expected, since the 
resistance and required threshold voltage should be dominated by the smallest 
separation distance between the two crystalline regions at the contacts (Figure 2.13b).  
By measuring the shortest distance between crystal paths in the pure amorphous 
domain, damorph, and comparing it to the threshold voltage, we estimate the required 
threshold field to be on the order of 4 V·μm-1.  This number appears to be largely 
independent of the cross-sectional area of the sample for the geometries studied here.  
The plot of the threshold voltage as a function of the estimated size of the amorphous 
domain provides a near linear relationship for the pure amorphous phase (Figure 
2.13a).  Since the mixed amorphous phase is interspersed with nanocrystals and 
depends on percolation paths rather than the electric switching of a clearly defined 
region, it is not possible to measure a corresponding damorph.   
 
Figure  2.13: Dependence of threshold voltage on amorphous region parameters. a. Threshold voltage as a function of the size of the amorphous region. b. Threshold voltage as a function of resistance in the amorphous state.  We observe two different behaviors depending on the microstructure of the amorphous phase.  
 46 
Interestingly, the threshold field we measured for the pure amorphous GST 
phase is about 1 order of magnitude below that reported by other groups who have 
investigated PCM bridges46, 102.  While the origin of this disparity is still under 
investigation, we note that the lower threshold field was necessary for reversible 
switching.  Groups who measured larger threshold fields found the resulting threshold 
voltage for Ge2Sb2Te5 prohibitively high as it prevented switching from the 
amorphous to the crystalline state for all but very short bridges46.  This observation 
further corroborates the need for careful studies that can pinpoint the variables that 
affect the threshold field. 
Factors contributing to measured threshold field variability between research 
groups include differences in materials composition, processing, cooling-rates during 
melt-quenching and the difference between melt-quenched and as-deposited 
amorphous phases. In our study, the correct Ge2Sb2Te5 composition was confirmed to 
within experimental error via energy dispersive x-ray spectroscopy and diffraction 
analysis, as detailed in Section 2.2.2. Since etching can change the material properties 
of GST, we avoided etching and used a lift-off process instead.  Similarly, we took 
precautions to limit exposure of the phase-change bridge to solvents.  Further studies 
are needed to find the root cause of the variation in threshold fields.  Our in-situ 
technique may be a useful tool in this investigation, because it allows a direct 
correlation between the electrical and structural properties. A better understanding of 
the contributing factors may allow the material to be engineered to obtain threshold 
fields that result in desirable threshold voltages for a given device geometry. 
https://lh3.googleusercontent.com/notebooklm/AKXwDQER8cFlypmQpf9-1oW65BPLqTSjjLGveI-xesncDNOou00PEU7Y3vuEReVXLRWz9bD9c3GqeDf8whjEy2P1sOqp17kp7yjpwG3N6SirIGLlxfgntZANqmG2W4cuIE0cFvyKy2Gb2g=w516-h617-v0
8814b7f8-81eb-41e2-99b1-d9d39c1c64a4
 47 
2.5 Control of quenching rate via device geometry 
The above discussion of differences in amorphous phases and threshold 
switching shows that the microstructure of the high resistance state is very important 
for device performance.  It is likely that a single-phase amorphous domain will show 
less resistance drift and longer data retention, because it offers fewer nuclei that can 
grow or be affected by Ostwald ripening.  However, the mixed phase can be switched 
with less energy, because it requires a smaller volume to be programmed.  In an effort 
to control the microstructure of the amorphous phase, we manipulated the quenching 
rate by changing the device geometry.   
 
Figure  2.14: Switching of high-aspect-ratio bridge with lower cooling rate. a. Crystalline bridge 
obtained after 60μA current scan; resistance is 18 kΩ.  The red circles show examples of large 
crystals embedded inside the bridge. b. The same bridge after applying a 2V, 300ns pulse. The red circles show that the crystals in (a) disappeared, indicating that the bridge melted completely as a result of the pulse.  However, the bridge did not turn completely amorphous but re-crystallized 
due to the lower cooling rate.  c. The same bridge after 60μA current scan; resistance is 29 kΩ. 
 
https://lh3.googleusercontent.com/notebooklm/AKXwDQGK73B-v3Dzjc4LG9JH6oeu5xmShkwFpoeCiQOToPRN2VWUGF9QpaUoo4nBp3a_lSCtNolP0lD9XsSuReADP3D2BpFF2nOmvTD7oCRiMQpgxs18nQZMGI-Ni8OxaOxd7WXZ6JRaBA=w282-h338-v0
03b89497-e59a-4528-8f2f-82bcf5bea812
https://lh3.googleusercontent.com/notebooklm/AKXwDQEQgZ1El9x286vQxp_1ka3-4sFdMuI6V0_1GqWCtwTSqvwegVstXEArxuEk9zl33LAboAa0mq_3nsQTo_-GUIpqvIm7C-cDxlgFlQiHVD91grBYsou_4O8Y6-y0fv8QKdqtmpR9Sw=w866-h444-v0
86c9a27d-3867-47a4-9407-b13e423063d1
 48 
We created a narrower (200 nm), longer (1.5 μm) and thicker (100 nm) bridge. This 
results in a slower quenching rate since the main heat dissipation is through the 
contact leads.  Figure 2.14a shows the bridge in a low resistance (18 kΩ) crystalline 
state.  After a 2 V, 300 ns voltage pulse, the resistance increased to 176kΩ.  While the 
domain is still highly crystalline (Figure 2.14b), the disappearance of the larger 
crystals indicates that the complete bridge melted and then partially re-crystallized due 
to the extended cooling time (red circles in Figures 2.14a,b show examples of the re-
crystallization).  The bridge could be returned to its low resistance state by applying a 
60 μA current scan.  As expected, the bridge could not be switched to a single-phase 
amorphous domain by increasing the voltage pulse. Figure 2.15 shows the complete 
switching sequence of the NW shown in Figure 2.14.  
 
Figure  2.15: Repeated switching of high-aspect-ratio bridge with lower cooling rate. The figure 
shows TEM micrographs of the bridge after repeated switching.  60 μA current scans were used 
for crystallization and various voltage pulses were applied to achieve a high-resistance state.  The series of TEM images with the resistance shows that the bridge could not be turned completely amorphous by a 2V, 300ns pulse.  Increasing the pulse further resulted in the bridge breaking.  
https://lh3.googleusercontent.com/notebooklm/AKXwDQFfQOfYNA9b9y-c7-o32xwx_1IPb4HsNcTm9soPAZRNr1N0j2a_GXWHkRU1GB5_kJtQsF-rOZXDswBUu6Lap8UU0YF7C8lm11fCpPTjH-TT_ckB5-HTaexCM9f9zwSoB_oyXFywog=w312-h392-v0
6046f2fe-ba2a-498c-a08e-f5393e296094
 49 
Increasing the duration of the 2V pulse did not lead to complete amorphization, and 
increasing the pulse amplitude resulted in sample breakage. This experiment 
demonstrates that by changing the bridge geometry we can decrease the cooling rate 
and thereby increase the crystal residue of the high resistance state.  
Similarly, we can achieve pure amorphous phases by using bridge geometries 
designed for higher cooling rates (Figure 2.16).   
 
Figure  2.16: TEM micrograph of a short bridge that can achieve a single-phase amorphous domain without crystalline residue due to its fast cooling-rate.  
Accurate control of the cooling-rate is necessary to achieve optimized switching 
performance. Our experiments show that changing the device geometry provides 
control over quenching rate, which in turn determines the level of amorphization 
achieved. Further studies are needed to optimize these parameters. 
2.6 Conclusions 
In situ TEM studies of PCM cells during switching enable observation of the 
phase-change with unprecedented accuracy.  In this chapter we presented the first 
 50 
observation of in situ switching of lateral phase-change cells inside the TEM.  Using 
this technique, we found significant variability in the microstructure of the high-
resistance phase, which explains the observed variability in PCM switching 
measurements.  In particular, we observed two distinct high-resistance states: a single-
phase amorphous domain and a two-phase amorphous/crystalline domain.  The 
technique we developed will allow further investigation of current topics in PCM such 
as the source of resistance drift, scaling behavior, properties of other phase-change 
materials, failure mechanisms, and multi-state switching.  The observations presented 
here as well as future studies using this technique can assist in the design of improved 
PCM cells. 
As mentioned in chapter 1, it is not clear yet which material will ultimately 
show the best properties for PCM.  Interestingly, studies on NWs have shown 
exceptional performance48.  Hence, the next chapter will discuss the synthesis of 
phase-change NWs and our in situ study of these NWs will be covered in chapter 4. 
 51 
3 Synthesis and characterization of GeTe phase-
change nanowires 
3.1  Introduction 
3.1.1 Motivation and overview 
 While PCM is gaining increasing momentum in academia and industry, the 
phase-change materials that make up the active region of the device are still 
extensively researched because materials optimization is a straightforward way to 
improve the performance of any PCM cell.  In this search for ever-better materials, 
nanowires can play an important role: synthesis via the VLS growth is relatively 
simple, they can be made into nanoscale dimensions without the need for multi-
million dollar equipment, and they offer high quality single crystalline geometries 
without etching damage or other defects.  Hence, NWs are an ideal platform for 
fundamental studies.  In this chapter, we report the synthesis and characterization of 
GeTe and Sb2Te3 nanowires via the vapor liquid solid growth.  
3.1.2 Background 
 Since the early 1990s, the vapor-liquid-solid (VLS) mechanism has been 
demonstrated to be a general method for producing one-dimensional IV, II-VI, and III-
V semiconducting NWs19, 20, 103-107.6-12 Gold nanoparticles are often used as universal 
catalysts to define the growth of these materials into wire-like structures.  As part of 
this dissertation research, we were the first group to report the VLS growth of Sb2Te3 
https://lh3.googleusercontent.com/notebooklm/AKXwDQFDTBP2VcfDpki92pa1u9Cmde45lNha5XTCQItI2EKSv8beiqOP4k3pcpgxqYEUGPpivuyOI3PvTJMDJYg_q3Ynfl80Rso2NF6VUlZWbzSivNCcw1r46XFzWfJpUXJgoXzO0hmbtw=w763-h407-v0
a19d855c-6ec5-49e4-ad39-0360a8c67a37
 52 
NWs.  The VLS synthesis of GeTe NWs was developed by us and by a group at 
Harvard that worked on the same topic independently around the same time.  Since the 
development of the growth, phase-change NWs have been investigated by several 
groups.  We will briefly discuss their progress in section 3.5. 
3.1.3 Materials 
 Here we exploit the VLS growth of GeTe (GT) and Sb2Te3 (ST) phase-change 
NWs with Au nanoparticles as catalysts. The family of Ge-Sb-Te (GST) materials is 
one of the most important systems for phase-change memory devices due to their rapid 
reversible change between crystalline and amorphous states at temperatures 
compatible with those of device applications (for Ge2Sb2Te5, melting point 610 °C, 
glass transition temperature 350 °C)44. Germanium telluride and ST are two important 
members of this family of materials and function as the basis to fabricate GST ternary 
alloys. They have melting points of 716 and 630 °C108 and amorphous phase 
crystallization temperatures of 145109 and 77 °C110, respectively.  
 
Figure  3.1: Quasi-binary phase diagram between Au and GeTe (Sb2Te3).  The shape of the drawing represents the phase diagram between Au and GeTe.  However, the general shape for Au and Sb2Te3 is very similar and the diagram can be used for showing the temperature values and general shape. 
 53 
To investigate the fundamental possibility of a VLS growth with Au as the catalyst, 
we have looked into the phase diagrams of the materials involved. As shown in Figure 
3.1, GT and ST have a relatively simple bulk quasi-binary phase diagram with Au. 
The eutectic temperatures are at 480 and 454 °C, respectively108. The phase diagram 
suggests that it is possible to use Au nanoparticles for VLS growth of GT and ST 
phase-change NWs. Due to the small size of Au nanoparticles, the eutectic 
temperature might be lower than the bulk value111. 
3.2 Synthesis 
 Nanowires were grown on silicon (100) substrates with a native oxide that 
were functionalized with 0.1% w/v aqueous poly-L-lysine solution (Ted Pella) and 
dipped into 50 nm diameter Au colloid solution (Ted Pella). The negatively charged 
Au nanoparticles stick to the positively charged poly-L-lysine. The substrates were 
positioned downstream in a 1 in. diameter horizontal tube furnace (Lindberg/Blue M) 
with the source material, finely ground GeTe (Alfa Aesar, 99.999%), placed in the hot 
center region. A 5% H2 in N2 gas mixture acted as a carrier gas to transport the vapor 
to the colder furnace region. Before each experiment, the quartz tube of the furnace 
was evacuated to <100 mTorr and flushed with the carrier gas repeatedly to decrease 
oxygen contamination. NWs were grown at ~50 Torr and ST NWs were grown at 1 
atm pressure. Typical parameters for the NW synthesis were as follows: temperature T 
= 450 °C, duration time t = 1-6 h, and carrier gas flow rate = 150 sccm.  The best 
growth was achieved in the colder region within 5-10 cm of the furnace end with a 
temperature of ~370 °C. Samples were also grown on 50 nm thick Si3N4 membranes 
https://lh3.googleusercontent.com/notebooklm/AKXwDQHzm15SWq_hCYAUr-PfJLVr_fv6z5wEg-GAWdxjFs9QPJuYQmcuk6WbE5MX0tidkCXgqwsmcvBKhhrqkCn745wQW91QVdb__TdGKdYnZqKaoRTQqrKSXn1Wh0Z3WIczB6jmbXnaBQ=w487-h65-v0
83c0d4b7-5064-4aee-a4a5-6c4e116943e6
https://lh3.googleusercontent.com/notebooklm/AKXwDQG_KsEr5DCLYJKZ9L0Y3goleDQdFQzddmdbu27-gA5JyeeDH1fcAvakzDkm0SvWCAZ5ZM1YizqfXTfl9WZfLCTduLNCMZJWe3o3yf4NkF_UC5VhoKZ6cR3CAIhBM3_CNNYjU-BO=w487-h65-v0
92f89c62-1f01-4127-aa37-cb98ec10187f
https://lh3.googleusercontent.com/notebooklm/AKXwDQFnPxcAqmdCPq4ofcuWsIbt8WQOV7CeSCQP0Q-3mV61YyBgcq_ZU4fwgg7Wbpk7vfZvVAqpx9J-zTu8ygmrpd8coYmUgfP4wYmAf_Za1HXy18TjHop6qrqkniWwq1sM0ncHCyzHFA=w487-h65-v0
fe2507d6-b7fd-4619-af79-84e0e0c2f546
https://lh3.googleusercontent.com/notebooklm/AKXwDQHkGW6Kr1kTKk0XIhjHn8io4dbnfZ4KAaDzYFiybdHnY9ot0OisLSygAXIZlEDOX39bQUML6SsN2k-ZeTEHd1RD8WU3SIuYUTuBDeeLFJF6wWw8omW5_zV9xkoJY-U-taqQrOEi_g=w487-h65-v0
49f14618-3642-42dd-978b-353ebc2917d1
https://lh3.googleusercontent.com/notebooklm/AKXwDQEIqSB9cYPrufYLxPYX0TswilGL5CJSxFC6E35HrpiF_tvWh-v32_4EXsmU2FKOKJxvOu_Z8HLjzO4dobs_KDfi1Odn67P9a_X_L02Ra4rJiafYNvbHKk-eTSQx8R4EJmfsdJVY-A=w487-h65-v0
fcf24b99-8164-4867-8ec8-f2c7376b4f94
https://lh3.googleusercontent.com/notebooklm/AKXwDQE5ze_DULY2El-o72amitkqRzCXTftinzdySblaIMEdAhmFLpGeq7yIeLrXohdQNyCJi7dKlVHjsrEYiMRqEGDMZQhEEOgZyJOsopPU1t6dV6YGr-CpOxpmv3hRI4YYDkPevyYBfQ=w487-h65-v0
4843aad5-be0f-4704-81f4-cd31f40b5079
https://lh3.googleusercontent.com/notebooklm/AKXwDQEFJ6WLHAvJHF1NUuJFAxT7-ZNhgq0ykBSHVrJk8i7xerGvwlUqTQTN8zJLfsL44bWmtPSnF88r42zKvH5woWPxkENioZzpTfxXBEyyNbOJOxYuY6ueAkvbo3F7g5PrxwncbCV2=w487-h65-v0
348708ef-789d-42b2-8424-21919917437e
https://lh3.googleusercontent.com/notebooklm/AKXwDQFZPu0E0riqWuWrEXJYPE6K3z-AotMH7rjw_OIC-ua0VVngIw3fJbtWo6WDMLlcblNDzizGNOCwqiZLo-SxWnvBgnHKbjQuzG86wNoUSU-Xu5BrQwSPl7LLfOdgqC3G4Z6CGgWU=w487-h65-v0
3f2ebedd-616d-4b20-8566-51ad3b4e792a
https://lh3.googleusercontent.com/notebooklm/AKXwDQGFsZ8ejAIABRwT6a5Fk_8V1fNj_RMsgVXjdRY6wXye6SwCOVLk7sp0dq5RJm7DqmihgMtNPa28vQlbopTvk6kSfLmkOJPdj4tEMcKlbCOvbOa2CBKy364IlsjEdE0RW3fygYyGyg=w487-h65-v0
55fae0fb-fe6b-43d0-9cfb-3a2e96b5014c
https://lh3.googleusercontent.com/notebooklm/AKXwDQFnBLpwz3gNKNC3b8DJPHuIxLy6Uld8g2etabPuvPUI0JUdPamZr2JupH66MIP8HRGmWEOEqLEGzeJ4fvshn5lBBMQfdf1OqhMiFFaNPIxiNruh-5Ml5pNtlAg5lUf2s1s6sXcH=w487-h64-v0
e9ff56ab-3cb7-472f-b52b-16668f88c992
https://lh3.googleusercontent.com/notebooklm/AKXwDQErqfN-e2qyYsIWHzJiEr4YhwZRNjwxCVGuqIqEoEnjoiSzaoP21R1C1VEdo80n05gngaPz6qBdGojmjCXUmc8tWuBkgFVO_O3mnTmfRQsBaUHrn7GiyBdV3dBQcu4v56TjxouyFg=w487-h585-v0
3bd8f23f-3cd7-4413-8570-5157d1460130
https://lh3.googleusercontent.com/notebooklm/AKXwDQHDHfUxLLFYlROG_SwXyZjJQNSIg07V_fEcep4hyf9heZiKens7gUgUu5kFnpigpRDb8yuUOQLojGf6VYU5dQ9i-Y5uQi53jQQYkr3ZbaCZrVpjzMQ26nioKJQzm-I5kcseUL2G=w487-h64-v0
2b2a5aa8-a097-4e6b-865f-7309de710203
https://lh3.googleusercontent.com/notebooklm/AKXwDQFjSV3lOSmoJzBdp0deOdi7BHU2EFmqt1TnFlt_66yxLgA-ImMbwCPMTdVK4bpy2GtaD-EF9NiWaHuk5Ry75pZ8Y8pFtE411DYEYhwfNemqBgwVZiWSKfTUnniln_6RUUpewjQq=w487-h65-v0
d1cd8394-749b-43d4-af3d-6f846e47de23
https://lh3.googleusercontent.com/notebooklm/AKXwDQEXPgDmrqPldIuQnJ0pSHoQIjEnLZLaiF_TtBl-5_oWkDlO0jZEeZluhpB7hmlcVsa00Bm6zTMlh3umeaqXNEpCZ_TEUf5o5QOyY0n58TgdeC1K7jGJizYxeNikMjUVwXgURxtN=w487-h65-v0
9514b66b-b05e-4272-b28f-d25f71df65d1
https://lh3.googleusercontent.com/notebooklm/AKXwDQGRUCxb_ZQQ0WDsyRw-_TWuGsnDelIUk-sRBMaRoXT4-6dyDClzM8mWDcmLqFscXjdGXX9PyXqrdwKvuYaqNkjIdz7DkksAl5u73kjzOUh3oMKGvrwhWxRcRL0uE9t2bHYBqsExJA=w487-h65-v0
6205788b-7330-445e-9838-96103388cc1c
https://lh3.googleusercontent.com/notebooklm/AKXwDQFbhjm6vAHys1yUqNAuAGg2VWMIj377_Yw9t7CTqsNdZY7BjhrjY5ngqPHl1Fdzqw1Mnxk3zlQYZZyueAh7_nMRG8X7UZOCqCeoSHxKvPeLAfbExtnOk8p7YMS7Wg-EmEkHpa9Ibw=w487-h65-v0
df88debd-3120-406d-ac2c-4d57a41a5a9d
https://lh3.googleusercontent.com/notebooklm/AKXwDQFha5PgGQbc2GKpNUrVe8fNLynIX7yQOo4wzXPvMDOsXjQLPsIFyRbEKzQ-of9tccNJpvVDIQUFprS6oYky-1Cp9EIcZ12m53gY1K5jj-DgfOFthd6Z_KOB3baTI6PzbEBxnWt5=w487-h65-v0
5b3086ad-a9d2-4745-9554-92b536960399
https://lh3.googleusercontent.com/notebooklm/AKXwDQHmJ6byGdvtNt1kP_Dt_waRm3m0NUTuY3kpWmGXXOFRV84LSwo44Hzkiw1kV408AQo-kJ7-ITj_LrOVY5f2wfTB3l9inVT8Q5eioTM3RHNP7q7PK2LyhHwAvknVl8-_K3gPygNB=w487-h65-v0
7067e6a3-80c5-49a7-a9c2-9aa384a08911
https://lh3.googleusercontent.com/notebooklm/AKXwDQGztdPnRojCElbjoiFIUVn5_QQGijdhSh7ggLWomLWm4GXJrecoZOyxCxJRc5HUOrXsztx8AUoHRpvO-BhiGKtzKlpHHc2dcGhuyJSU5kIMRLabWk47GA1zpS3jiwwKFfDSLaFKng=w487-h65-v0
0e9c865a-86b6-4324-bec0-cb507e66420c
https://lh3.googleusercontent.com/notebooklm/AKXwDQFKSYroomXF6K1mREeatx6vAVtNXWVvVpNA2_6iekT_rkXBlUMFrVXZGIKcNc-ei-X0GxpLmsZt4zzORvUdCjsFjE5HjZwow0nWTifPWP8h4EAfSqSWnBUynDPzFt4xM_Qvu--d3Q=w487-h65-v0
c69db417-1ac0-4a07-b686-c0d71bae279e
https://lh3.googleusercontent.com/notebooklm/AKXwDQHqeujXjY7gE_ddpNIwXyO4K7oA_Y9Vohcznkfc7l7zKHeh-cCDUZ3B_euE2rHBNxorPhquD51hAfLtYVcOKyhNeSnJ8hFO24XwqQk4a2i-6Oc6OhwZas-Ts2Ovt4n2-Q9xrfMq=w487-h65-v0
2e7101ff-0666-4327-9dd3-dad2d11dfcb4
https://lh3.googleusercontent.com/notebooklm/AKXwDQEhsUC2TRp7_-NS9vGH_aBe--4O651pFnksjwKplS9smdVAP6CLY02CAb9Y4-5qycoQqvE-9UU_SxNc8komwmJh1eI7u-7x9eEG5ceQHuXiS5OERb7OBrjqrdDfNt0W1J301l_zZQ=w487-h64-v0
15a00167-2631-41c1-8640-b5c255014d2c
https://lh3.googleusercontent.com/notebooklm/AKXwDQEazkb2GQNlYzzHs2IVj0fLfgVZtM6mZQrnXsw1VU0iiO7DkWu09XBWAFurxO6ivjypK6trOOkkDYtUgSAIVVhBVBvrV6CMm3ZNGG6xDHAXX4HCQgNZn9p4CW_zYqYKfrObQvzh3Q=w487-h65-v0
f9c13f24-bfde-4611-a7b1-786e1e0619ef
https://lh3.googleusercontent.com/notebooklm/AKXwDQEl60i1syfqschIg02saEgMUIPfOMqioWEB-nHXeqz5L47Ldu2C4rNIJccJNfh3pOqoxIM7IZITiE55k54etjQDTqNHCDmbdJCDEBTHpIe844sr8PlDT4QEN6ywdH42YBxGwPTTtw=w487-h65-v0
548d6ef9-60fb-47d9-b15c-9d6b6dcadcd5
https://lh3.googleusercontent.com/notebooklm/AKXwDQESIo6X1jO58sBogllvzsAYnc3kNXocs26eDWIziIT_YompG4SI0yFcvWBSRxj3YbZ6obLIGu66a7IOOrqVgdun3Q26HHi1n3vmFxAmpTy1AEx1gcjCkmkhZpI4Bae0NgGDdocP4A=w487-h65-v0
6e84d989-15f6-4bb1-a3ed-8bd8b393314a
https://lh3.googleusercontent.com/notebooklm/AKXwDQHh7WCx7H-_dCGHKOFusTQ8cTZlMJt7ifnIA8HJu54tgodPvm-PEL2vA82Y1WqlchYjh9u_PshTbhPft_LIvFqEe-LF5lxM-vRoyk0YM3aftFgFMLMmUVdcgkMozlbUm9Z07hMFkA=w487-h65-v0
35099249-4e90-4b3b-982a-216342571383
https://lh3.googleusercontent.com/notebooklm/AKXwDQHsemqs14c7Fw2OU_E2uMnapTinGKyELw74MLPUDiTrwy2EIp83ISiZwJrDYzuQOK8Y698Cu71GJ2cjKtnF5A90dCZ2YCb-QwVH7Ki9U0yfUhpzFEDaXRC88E9yNxzec1q1BdOL-A=w487-h65-v0
289ab4ce-cf2c-481e-b7f8-d72141f35cd3
https://lh3.googleusercontent.com/notebooklm/AKXwDQGZkvt8LQvYmIwQKOaxtOeIuTbhhSMFyP6NMyNTGOgmKhxAqKDG0oqHYEn6dShhyGgVHj7ELYytUZD3etGRSumUr1jhKVncBw8La_YrZ83PzIbgH36nNOsEjGRstToAzcShxIED=w487-h65-v0
61b784a5-f909-4e69-aed6-b86b08e02142
https://lh3.googleusercontent.com/notebooklm/AKXwDQEWkN1eAeAgqZVh5aNRsRZl3y46SlxzjQ8hkAzAL2GHZ2vVM2N_ojNWwvzUEFlx_hqNaFYqauyoB7fIQ17Nyv5eubI6LoJohhbqNm0TlMu3AInXtNnRJuhBwVZKQyyJDIgh5qLlTw=w487-h65-v0
c692c473-a9ca-4b93-9eff-81b929fb3260
https://lh3.googleusercontent.com/notebooklm/AKXwDQHY6LLtS9ZGP4LWSsA_N25wQ1F2T5_Sc38eOnM_ukhGbXQTlOkeJ67Ih9SVRx28eztQ_zbr4HIsczsjXn-GHUrD9hLEI9HItGveTJaZwHzrlXE7XjCWZlFr8mPvJkVIOwBGI17I4Q=w487-h65-v0
3061a6d7-0789-40d5-bf06-e8248352eaad
https://lh3.googleusercontent.com/notebooklm/AKXwDQG5Yjozl9iQ8XBucsTQud_gsIOsylCbx6h0xQdT3vzPybGt_US3h8f7vd1ZG3dP_pEANCVenbosHvUanajP0uJu0RW99aB7HRcXSFdfg-WnjCGQg4jFCdGfRXNKtpC3afQu7fVuWw=w487-h65-v0
a17a0207-d92f-4b05-8eef-64de4d295eb3
https://lh3.googleusercontent.com/notebooklm/AKXwDQFhBx7knPAPyVXDy236u_rCMtDz6Vouq_c1Z3MPYAjsk8vPVh0nj-F0CtET-vx9fK5AwXq4NkQHCQz-uoE4OWY_PvRcMCjlDI7HaFdGCkrvIsQnLrlZAgFNCb-GYE2Ghhp-GyQY=w487-h64-v0
2f6547da-10bf-4b0e-94d7-f6a2ddd95e3a
https://lh3.googleusercontent.com/notebooklm/AKXwDQFVrrKW2UVkWqSC9ee1qImd3G2LY33ScDJtHkplDFMAc7sOQMAln1AegvU_hlSYgGdjqukB2LvVbwB4a6rVsQCbFEalZOlkFYdmUN98ADdp38pGzJeto-c2RO7RhTqVf5zQvYLbRg=w487-h585-v0
c7a018b8-2495-4a23-9114-6dd0d73e9acf
https://lh3.googleusercontent.com/notebooklm/AKXwDQGZcE7xaMU7bB9cDtbmsmwbl0R8ThxeNWz6J6_ObBvOQBynaSbavdDRyPh3hhKBd5UGH0SK4C9SXfWbniQYN9Es4sgpn7_9ALYIYKmcuwOwI15cNRfEOssyMmyUDSytqn3O5Er8fA=w487-h64-v0
20de5148-14d6-4de0-ad31-cecc6954181e
https://lh3.googleusercontent.com/notebooklm/AKXwDQFEPvg2urhHcy8Hgj4ALXw5hPCGT0Hd401tAs-GuLojicvwhlHF688QwQqzfz0p1-LPAnAV0gxO9VqiWdPwt_5nWaR3uQUnouhv6544sO7og1jW3Ht6Bg_064UCARdvUAvxguCr=w487-h585-v0
3956b049-8c8c-48e4-9a1c-48466f6d4b5f
https://lh3.googleusercontent.com/notebooklm/AKXwDQHd76sEzSU9z9Ni9ZpbOnbcGDbwxPwivQpNRFfIIBx08RE9B_H87g6b9W7nFR0ZfU0i4MRgFhSV1vw_4VSiqO450i7Lp_8Xmcktgp5_ckWVsl29JRSlicYRlXI14M8rsWAA6W-Z=w487-h64-v0
43e0eea2-5f85-4e12-860c-ae0daa5f51b5
 54 
for further studies with a TEM. 
3.3 Characterization 
3.3.1 Scanning electron microscopy 
 The NW surface morphologies were examined in an FEI Sirion scanning 
electron microscope.  The SEM is the first step in characterizing any growth product, 
because it allows for visual inspection of the as-grown NWs. Figure 3.2 shows two 
SEM images of GeTe NWs at various magnifications to show the density and size 
distribution of the NWs.  We found that the NWs can grow 10s of micrometer long 
with a diameter distribution ranging from approximately 20-300 nm. 
20 μm 2 μm 
 
Figure  3.2: SEM image of as-grown GeTe nanowires, showing high density and a wide size distribution with diameters ranging from roughly 20-300 nm.   
The thicker NWs (~200 nm diameter) can even grow 100s of micrometer long (Figure 
3.3) if the growth time is increased sufficiently (~ 4hrs).  The fact that the diameter of 
https://lh3.googleusercontent.com/notebooklm/AKXwDQE13LhWJvBo4coEzBeqki0cLEeRNPuH2Aj79hXYS_Sg-wcl8_BQsuQvsBKFBgUOVwbt2SMAfo-m8NToQbtIonax3U9j07b3JCdl7FuuyvOJvmDWbE1cb9wc8XSE3FIRsql9avqCuA=w247-h33-v0
bdfa819e-d597-4f30-8d61-18143921bc25
https://lh3.googleusercontent.com/notebooklm/AKXwDQEt6hqtzpbqykcVJw_O7WGMbkMxNXa2fsaPq381ql5IwLAtFJCqRDuP0pjq6s_biyxVhfFEOPvQdkQon8OLr9DUo52gnGjZkm7qg2OgtO2vWm9RzmEsFe0f8beLEn-Lzvhrzt0OYw=w247-h33-v0
cf21b248-c2b8-4ad1-b5ec-3ac91e37f710
https://lh3.googleusercontent.com/notebooklm/AKXwDQF-vP6PWb4hQhzXaWpol3IWzi98xkt3MuTd_cu_fHoAqwmuOPEuCkpAMd9W5DoAZbZnRXzUfljRhU9AuEsOkzpfJuPUE51vSHT7s6Bdv9N1QT_Fz22PsnNfPwns4v8RxmhqFKlOHg=w247-h33-v0
a983ddc6-c478-489f-b444-4fce591af39d
https://lh3.googleusercontent.com/notebooklm/AKXwDQGD9w5oBq9fcrNoAH4UTGlkPGwbsWy4OFsWxdJ_TsCJmFVZvEVHD9_632sEkzbI5O39ROw2BZpWp-dZcbvrTAHYDEot7QuCiWa9Gp2ddokAodsF-0M9eKMhLKm78qfkhOQhD0pUPw=w247-h33-v0
622a259e-6e48-4de9-8a03-78cb162193ae
https://lh3.googleusercontent.com/notebooklm/AKXwDQFQw8dMw2wiHpM3WTx4MQcRHj1snfukljj1pC2OfqABAdntnC6IyHZ3tbINfzezAshx394RMRHooaBjk0n9wSwn0fsKaS6wmu1gXuc4X0Q0uVwLdCFmtZiA1u-FY0HBcV_kVZEaPg=w247-h33-v0
9ebbbb21-7d98-45fe-84c0-342d7a9d6da8
https://lh3.googleusercontent.com/notebooklm/AKXwDQFh3Z-erK0jmxCHE9HKJIUREqlGiIkKjdgUiXaFvrmSiRvjWZrN3lYrB8e-0JktqL2xV2-23rZ-AUgS-fQ2uPmekRAkl1CE0bS39HWYZvIyOHTUTAXool7_DlgjLF23uJGk0f7Uew=w247-h33-v0
43190501-a9e7-4539-ad37-d88f02f8d609
https://lh3.googleusercontent.com/notebooklm/AKXwDQFdGpp31irnvcd7TCFZXWobspneXtcGX_dneRUm3cUrgLuLQ-84qsN6Lf_Uw32ojAGEoDGm894bpEgfpUx5osjPe5Oc_uDiINnIkaECr7Z1fPAUh00HAX8ARYmr_RoGI4d8BYRgnQ=w247-h33-v0
4ea27a98-72c9-4f15-8853-40986002e06a
https://lh3.googleusercontent.com/notebooklm/AKXwDQFNDThQfSisYhrrA14iSbkYduFyYLMJctxEpl5Lrm50xKJZdvOVPzRS62BMIww2EZ9m8cDtH2KW070hhD1UPKi9-vkbabjDo_jKpFclAX5R78BuIr01-Oh0dLszl5tYMYQarS5NaA=w247-h33-v0
48f05b70-d86f-41bf-8fd6-c4909bc06428
https://lh3.googleusercontent.com/notebooklm/AKXwDQFjM-3Iw6IDROLnJw2MlhtoLeybhPndMeKKUvuZUEzgC5tGG7jCHpX6E67OvN7c7pmAB2eW-K-dAh_1TBxc5RDwkWalVZdTMy3M8gBhmPxYg6OTLaB8pJnHrnwzNUyvi3lhF8NBAg=w247-h33-v0
e7a45d13-26e4-4466-8a88-9ff54deea2f6
https://lh3.googleusercontent.com/notebooklm/AKXwDQFXLgMu776IPZDMQCSR7qm9htOMRKqsjJGuD_x4mtykmYgcGmRgLH1zeeSwYDpl8p3I1qz_YYAQ3VLQVCJsc1DIo-d5DR175p6ffl95btLHoQ3w5ZVBDfXB7Lj5qXF5xNgg2Fqn=w247-h32-v0
19056eaa-22d4-4bb0-b204-a76bcdee7d4a
https://lh3.googleusercontent.com/notebooklm/AKXwDQGUUzkPfsb2AGpm0G2-FOnTXefqe9SUK-T4-dWqt6Kebw8C8ZC_jvrni-qKItKlpK5mjNGy2yHgqVyADdclf3yMIrEXSdA-EIhIF09ep3yEjmLvKw53-und-P_l2psLGr7FlOCV=w247-h32-v0
6fe210f5-7ec4-4049-a381-50b637e3d8f6
https://lh3.googleusercontent.com/notebooklm/AKXwDQEvdH5L0f8ORCBWiEoQ531FVLJ4VdZm_NmxPxK9XgTjno_rPt6C4T61AVQOl7DLe2oXaCZxpkPJTnKy10Y4rVOhDGMFTEEo40ZNTNjovF5EwMtTdzFErqKDgoRI96nvinqgb220WQ=w712-h484-v0
9a78e5c4-b342-47a1-be7f-d80c828c04fe
 55 
the NWs is significantly larger than the starting catalyst size is believed to be due 
catalyst growth from Ostwald ripening or the absorbance of GeTe precursor112. 
 
Figure  3.3: SEM image of long GeTe nanowires.  
The large size distribution observed here is good for switching experiments, 
because it allows for the study of scaling properties49.  However, for future device 
fabrication, it is important to obtain good control.  Progress has been made by other 
groups112. 
Interestingly, using the same method we could also grow GeTe helical 
nanowires (Figure 3.4) without significantly changing the growth parameters.  Straight 
and helical structures can coexist in the same NWs as shown in the Figure 3.4 
(bottom), suggesting that they have the same chemical composition and crystal 
structure. 
https://lh3.googleusercontent.com/notebooklm/AKXwDQHTCnHZ5095rYo7NrKBJpfkstELlBxGf_h8b3UfHdKvOtNcImHghOL_uf_-nJQjHu8eRi6noxjQ63Ekan4KPxS71SnqH5YffnmfLFoIvT238ZoURkw6GivAc2NL05LhD7t5K_oIhw=w645-h516-v0
70706f4e-9fcc-4fae-bf38-4f7ef6006252
https://lh3.googleusercontent.com/notebooklm/AKXwDQFAnVvbHxQCugrk0L5QZUg_vwZgjsg2c71oe4ommLFixGWnEgtBcrWs2aLjhcf6a-CnFGOPp-_nJbq9aG_c9rR8BCA8aJe82vfv67arbvY0lpf2z8Tn6u6741SJNpreIcLDthxMEA=w645-h516-v0
a18d8785-0d2f-45ba-a90b-45f02cffa72a
 56 
 
 
Figure  3.4:  SEM image of as-grown GeTe helical and straight NWs (top).  The nanowires can randomly change from straight to helical growth (bottom).  
Both left- and right-handed helical NWs can be found with equal probability.  Similar 
helical structures have been observed in many other systems such as ZnO113, Si114, 
SiO2 115, boron carbide116, amorphous carbon117 and ZnGa2O4 
118.  Several mechanisms 
have been proposed that can form helical structures including growth influenced by 
the surface tension between the catalyst and nanowire, the presence of internal 
structural defects, electrostatic attractions between polar surfaces, and a 
https://lh3.googleusercontent.com/notebooklm/AKXwDQEA_zpsKJ32ydhZNqP5bTYjN_WTNMNzcY2nQ2IHDHUsETAvD0Y2WDjcllWrIo5lungF06WjPis9TMlz1nYISV4k-FCUIw9hIAu-9G-bTWcrnRFlZwX7pfAdtQNyZ61sLB1bTlvt=w392-h392-v0
dad4e83c-656c-492f-97c7-00bf0c493623
 57 
crystallographic superlattice structure119.  However, since the helical NWs are not 
important for our phase-change memory investigations, they are mentioned here for 
completeness only and will not be discussed further. 
3.3.2 Transmission electron microscopy 
To study the crystal structure and composition of the NWs we transferred them 
from the growth substrate onto carbon film supported by Cu grids by carefully 
touching the two substrates together.  Alternatively, we sometimes directly grew NWs 
on Si3N4 membranes.  To characterize the chemical compositions and structures, we 
carried out EDX, HRTEM and electron diffraction (ED) studies.  As expected, the 
straight and helical NWs show the same chemical composition and crystal structure. 
 
Figure  3.5:  TEM image of a straight GeTe NW. The dark spot at the tip corresponds to a gold nanoparticles.  Insets show a high resolution image of the lattice fringes and SAD pattern. 
 
Figure 3.5 shows a TEM image of a GeTe NW.  The dark spot at the tip 
corresponds to a gold nanoparticle suggesting that the growth was indeed via the VLS 
mechanism.  Most nanowires have the catalyst directly at the tip120; Figure 3.5 shows 
https://lh3.googleusercontent.com/notebooklm/AKXwDQHkg6KOQmjC4LZMp-YAHsv3ks5Dz8daSajW4cWMJEjiMkBGX-VkGMylT7B5Qn05DJ8OYI7FJo2VAzdojXlcj-4u9AXNGvyBcG35lYXKK6jszSKNLvCsa9Zl0LoelhUY2HIr5Bn1LA=w631-h434-v0
61a00677-570b-4fc0-b7ab-012843148b7a
 58 
another common configuration where the particle is at the side of the NW.  It is likely 
that during growth the catalyst is directly at the tip and thereby defining the diameter 
of the NW.  During cool-down of the furnace, the conditions inside the growth 
chamber change significantly and the catalyst may move to the side of the wire and 
stay there upon solidification.  The movement of the catalyst to the side of the 
nanowire may offer some insights into the mechanism to form helical nanowires, but 
further studies for this are necessary. 
The HRTEM and SAD (inset of Figure 3.5) can be indexed to the 
rhombohedral crystal structure of GeTe with a growth direction of [-111].  However, 
we also found [-102] as a growth direction in other GeTe NWs120.   
 
Figure  3.6:  TEM Energy Dispersive X-ray Spectroscopy of GeTe NW. 
 
The EDX analysis confirmed a composition of 50% Ge and 50% Te, each within 2% 
experimental error, for both straight and helical NWs (Figure 3.6).  The Cu and C 
signals in the EDX spectrum are from the TEM grids. 
https://lh3.googleusercontent.com/notebooklm/AKXwDQF6SJEvCDjK3C5DnvbTXcKC5VJLVEjlyn_iS8soMvVDPeHB0OpDGuabK9SK-KR6TjI13IxWWPuOshgLQYOHlbd7ze_KE-rJzpZXatB2qZbQFE3ybT2ehGJnAeEn-t_5WEdkwuy3Hg=w712-h484-v0
595872e3-8f98-4351-b1d1-07c8a19128c5
 59 
3.4 Sb2Te3 nanowires 
 We also developed the VLS growth method for Sb2Te3 NWs, because it is 
another technologically relevant material: doped Sb2Te3 has shown excellent 
switching properties in lateral PCM cells46 and it can be regarded as a building block 
of GST.  Figure 3.7 shows a typical SEM image of as-grown Sb2Te3 NWs.   
 
Figure  3.7: SEM image of as-grown Sb2Te3 NW 
 
The growth conditions were similar to the ones used for GeTe (Section 3.2), but 
Sb2Te3 grew preferentially within 10 cm of the hot center region of the furnace, where 
the temperature was ~440 °C.  The as-grown NWs have diameters ranging from 
approximately 50-100 nm and lengths of approximately 1-2 μm.  We also confirmed 
the composition of these NWs with EDX elemental mapping120. 
3.5 Recent developments and future outlook 
Since the development of the VLS technique as a simple synthesis method for 
https://lh3.googleusercontent.com/notebooklm/AKXwDQEKXtnmyLM0c16B71uRt2RW42nTUImJ5-rmwhLPeXN6khqSu5DUJDATVqRT_12t6Z3BRmxscOa8llVrFwjznrLeSluMsOP9jukiqzTJ7mZBZr8B-vXt_SfooulNIpxJgcOQTzC4Hw=w438-h231-v0
096e8b8b-f610-4682-9caa-4632f4e720c3
 60 
phase-change NWs, the field has been moving rapidly thanks to the contributions of 
several groups researching phase-change NW structures.  This includes work on the 
improvement of growth control112, study of phase-change nanowire switching 
properties48, 49, new materials such as GST48 and In2Se3 121, and studies of threshold 
switching53 and drift122.  The progress in this field makes it likely that phase-change 
NWs will remain an important platform for fundamental study in the near future.  
However, it is not yet clear whether they will ever be important for technological 
applications.  The IC industry is still looking beyond the scaling of their standard 
transistor designs, and nanowires are considered one possible option to replace current 
transistors.  If a paradigm shift towards nanowires and self-assembled electronics 
comes to pass, phase-change nanowires may also play an important role. 
 
Figure  3.8: Schematic of phase-change memory that is based on NWs.  The phase-change NW is 
grown on top of a p-n junction for selective addressing. 
  
For example, if Silicon NWs were integrated into future circuits one could easily 
incorporate phase-change nanowires to make essentially self-assembled memory 
elements.  Figure 3.8 is a schematic that outlines a simple fabrication process for 
nanowire based memory.  In this process the phase-change material (i.e. GST) is 
 61 
grown directly on top of a p-n junction to form a hetero-structure NW that acts as a 
selection device and memory element.  While potential applications like these are still 
many years away, it will be exciting to see what the future holds beyond the scaling of 
regular CMOS structures. 
3.6 Conclusion 
We have successfully developed the VLS synthesis of single crystalline GeTe 
NWs and Sb2Te3 NWs, paving the way for many future studies on scaling and other 
current issues in PCM research. 
 62 
4 Electrical characterization and in-situ TEM of 
phase-change nanowires 
4.1 Introduction 
4.1.1 Background and motivation 
Over the past several years, phase-change memory (PCM) has shown promise 
as a replacement for flash because of its excellent scalability84, 85, high-speed 
switching, long lifetime, and nonvolatility123. PCM operates by reversibly driving a 
small volume of material through a reversible crystalline-amorphous structural 
transition. The phase-change is actuated electrically by joule heating, and the two 
states can be easily distinguished due to the substantially lower resistivity of the 
crystalline phase compared to the amorphous phase.  Cells usually have a vertical 
architecture, where the PCM material is sandwiched between two electrodes44. This 
structure can be integrated into a CMOS architecture. However, vertical cells do suffer 
from one significant drawback for fundamental study:  since the active material is 
buried inside several other materials, it is difficult to directly probe the structural 
transformation inside a working device.  
 Cells have also been fabricated in a horizontal architecture, where the PCM 
material is patterned into a narrow bridge between two electrodes46, 47. This open 
structure is much more amenable to characterization. The bridge is not buried under an 
electrode, so it is accessible from above with probe microscopy. A careful choice of 
 63 
substrate124 can allow even for direct observation of the structure in a TEM. PCM 
NWs developed recently by our group120 and others48, 125, 126 are good candidates for 
use as the active material in horizontal line cell studies. NWs present several 
advantages over patterned thin films: they have smooth well-defined surfaces, they are 
initially in a high quality single crystalline state, and they can be deposited on a 
substrate in a single solvent-free room temperature step124. Single crystalline GeTe 
NWs are particularly interesting, because their diameter is smaller than grains in 
crystallized thin films that are on the order of several micrometers127. The electrical 
switching properties of single NWs have been studied and excellent scaling behaviors 
have been shown48, 49, but so far few studies have taken advantage of the horizontal 
architecture of NW devices for in-depth characterization of the details of the structural 
transformation. Of particular interest are the size and location of the amorphous 
domains of the devices in the off state, the growth morphology and kinetics of the 
crystalline domains when switching to the on state, and other behaviors that may limit 
device reliability or dictate the power required to actuate the devices. 
In this chapter, we examine phase-change GeTe single-nanowire devices using 
ex situ and in situ transmission electron microscopy techniques to directly correlate 
nanoscale structural transformations with electrical switching. The results are 
surprising: instead of a crystalline-amorphous transformation, the dominant switching 
mechanism during multiple cycling appears to be the opening and closing of voids in 
the nanowires due to material migration, which offers a new mechanism for memory. 
During switching, compositional changes and the formation of banded structural 
defects are observed in addition to the expected crystal-amorphous transformation. 
https://lh3.googleusercontent.com/notebooklm/AKXwDQGkciyQVQ8enKiiFdSeZZN22N2ZZUNrw1o-yHZtn7YRMcq4VkSMFCDhjOUqFLgE_StJC13mDp4C2Uam3D6WVseckEm32-Ifiu4ZtmWgxcV2tebMGffdKBzIimCYS2Oh08-KVsjf3g=w854-h665-v0
43dd799a-7749-4507-90ba-a60a8cbac5e4
 64 
Our method and results are important for phase-change memories specifically, but also 
for any device whose operation relies on a small scale structural transformation. 
4.1.2 Device fabrication 
 For this study we grew single crystal GeTe NWs (explained in chapter 3) and 
fabricated a large variety of devices on NWs ranging in diameter from 60 to 200 nm. 
Our as-grown NWs were single crystalline with the equilibrium rhombohedral phase 
of GeTe. 
 
Figure  4.1: Device fabrication steps outlined with SEM micrographs.   
Figure 4.1 outlines the typical fabrication steps used to make single nanowire devices. 
Silicon (100) substrates were pre-patterned with photolithographically defined lines 
https://lh3.googleusercontent.com/notebooklm/AKXwDQFSZxR1KkIb45AQv985o0ZAiE4LkhNxIA-0Yno9m5Gm2BQoqCKYuxjw5NTjtQa2cBlqyWXPVV-Y7bkdYThsb32GHnfTsB6DwAiif3uaRmQye3Ps_LpvJGFdP5_8azFii1SkycqazQ=w232-h232-v0
249f16b7-8ad7-4526-a4a0-38a82f496333
 65 
(Figure 4.1a).  These lines were connected to larger pads, allowing us to make 
electrical contact with a probe station or via wire bonding.  Next we used electron-
beam lithography to deposit small numbers in the center region of the larger contacts 
(Figure 4.1a,b).  These numbers acted as a coordinate system that allowed us to 
accurately locate each individual nanowire.  The nanowires were typically deposited 
via a dry transfer. Gently touching the growth substrate with the measurement 
substrate was then often sufficient to cause nanowires to break off and adhere.  Figure 
4.1a and 4.1b show the density distribution of nanowires after such a dry transfer.  An 
alternative method of nanowire deposition was to sonicate the growth substrates in 
solvent.  The resulting solution could be deposited on the measurement substrate by 
spin coating or drop casting.  After depositing the NWs, we determined their position 
with the SEM and use electron beam lithography to deposit contacts on the NWs.  
Figure 4.1c shows the finished devices.  For switching measurements, we also 
deposited an encapsulation layer to prevent the nanowires from evaporating.  For this 
purpose, we used 20-30nm films of Al2O3 or SiO2 deposited via sputtering or atomic 
layer deposition. 
 
Figure  4.2: SEM micrographs of GeTe NW with Pt contacts deposited by FIB 
 66 
 As an alternative to depositing contacts with EBL, we also used Pt deposition 
with a focused ion beam (FIB).  The advantages of the FIB method are that it does not 
require designing of contacts, and the ion beam can break through a potential oxide on 
the surface of the NW.  The disadvantage of the FIB is that it is limited to deposit a 
low quality Pt that has significant C content.  Further, the FIB also causes some Pt 
“overspray” that can lead to shorting of the device if the separation is too short.  To 
prevent shorting, an electrode separation of at least 2 μm was used.  An example 
device is pictured in Figure 4.2. 
In addition to making single NW devices on Si substrates, we used the 
methods described in this section to make devices on 50 nm thick Si3N4 membranes 
for our in situ observations (Figure 4.6 shows example). 
4.1.3 Instruments and measurements 
Platinum deposition was performed with an FEI Strata 235DB dual-beam 
FIB/SEM with a 10 pA Ga+ ion beam and an accelerating voltage of 30 kV. Scanning 
electron microscope (SEM) images were obtained with the same FEI strata or an FEI 
XL30 Sirion SEM with FEG source. The EFM image was obtained with an Asylum 
MFP-3D AFM. The scan was performed in a noncontact mode at 200 nm tip-sample 
separation with one electrode grounded, the other electrode held at 2 V and the tip at -
1 V. The ex situ TEM studies were carried out on an FEI CM20 operated at 200 kV, 
and the in situ TEM studies were carried out in a JEOL 3010 operated at 300 kV at the 
National Center for Electron Microscopy at Lawrence Berkeley National Laboratory. 
Resistance measurements in the lower resistive states were done at a low bias of 0.2 V, 
https://lh3.googleusercontent.com/notebooklm/AKXwDQEVs7xcgWWk9pK6Oy_ANDcxKgcM2LrtplC4AYNNFKfem7yY8f4200ZYqm8ZUBxWneq6uirC6SuqhFkpfJn4Nf6OPipTsrVDrZZ6rOhcCD0cW4h698a8aj7XB6J8Lm2eJadyHYSYgg=w712-h484-v0
9515588c-86f0-42ef-872d-a6c52c2bd722
https://lh3.googleusercontent.com/notebooklm/AKXwDQELOpvyj9HdryufIecahOa2a4kjwINQk9HUbXUPoS9TkD89ld2baUYR0bM-RAnL90b8UJ6bjxNIX1t-a4acQklpcr7W_8QrKGn1voJQ1H2QyFwuP3UHmq7SwNm2GtF81nxFI0YiZg=w334-h169-v0
d2fa730f-7aaa-4ee2-ac57-ef39429772e0
 67 
the highly resistive states (R > 1 GΩ) were measured at a bias of 2 V.  
4.2 Conventional (black-box) switching experiment 
4.2.1 Electrical characterization 
 Before trying to switch the nanowires we characterized their electrical 
properties and compared them to those of the bulk material.  Figure 4.3 shows an SEM 
image of a NW with four contacts on Si-SiO2 substrate and the corresponding 
measurement results. Two-point and four-point probe measurements show linear IV 
behavior; however, the lower resistance obtained by the four-point probe measurement 
reveals that even in the crystalline state, the majority of the resistance comes from the 
contacts.  
 
Figure  4.3: Four point probe GeTe nanowires device with corresponding measurement results.  
The two-point probe resistance of 26 kΩ is about 50 times higher than the four-point 
resistance of 530 Ω, suggesting that the contact resistance is much larger than the 
intrinsic NW resistance. The resistivity of the NWs as calculated from the 4-point 
https://lh3.googleusercontent.com/notebooklm/AKXwDQHaCNg6AFkm1V8rBur1j8xharT-36kTqRz8YCdBQQ4gptT2NMSRBlmYRexMxajmALbQkT6vyx2v8zi_0ZW71V7Msmqxn6ho9NHbP9W1OBx3ezSW0lt8MxCLga5k6vqCe3kL0FAhnQ=w254-h130-v0
13c3e793-1260-4503-b6e8-938a01c6a01f
https://lh3.googleusercontent.com/notebooklm/AKXwDQFdsGOEeZLhY14fhU-AOq3Kt8ENROMGjsdUdYmYdWb617xoNqYFG7FaaMCBRLTlguYOjc6KyvNL-9lVBwYiuESein7nCbvrLrvDDwtm_Nx3zNGUTiRIjsbJACgwH0BbQLhdRPoSZg=w254-h233-v0
3b066722-7759-4b95-9c6e-011798c281be
 68 
measurement is approximately 4 × 10-4 Ω·cm, which is consistent with the bulk value 
of GeTe128. Our measurements conducted on approximately 50 devices show that the 
contact resistance is 5-50 times that of the NW resistance. Occasionally, the contact 
resistance is similar to the NW resistance.  
 Even though our TEM examinations did not show a significant surface oxide 
on the NWs (chapter 3.3.2), we believe that the contact resistance is in part due to the 
existence of a thin amorphous oxide layer between metal leads and NWs129. To 
examine this point further, we conducted in situ TEM heating experiments. 
 
Figure  4.4: TEM image of GeTe NWs during heating experiment.  
Interestingly, when heating the NWs we observed sublimation of the GeTe only out of 
the NW ends rather than the surface.  After sublimation, a thin amorphous shell 
remained.  From EDX measurements we concluded that the shell was germanium 
oxide.  This in situ TEM heating study provides direct proof that the GeTe NWs tend 
to have a thin surface oxide that can increase contact resistance. 
https://lh3.googleusercontent.com/notebooklm/AKXwDQHXtJsHl09823hs-8AINHY4OkGLnfbvG5ELrUBOM9vlz-_A_ojZgW5lpe-H3L3u3N6wFdlwFFxrsyXW1I_vDU4bu0P1dfHOd34q-RrxUyC79r7Usm8VO5XWzHW1F2M4KU5xsrxQ0w=w461-h369-v0
18279c31-f315-410f-8e95-4a96f665b569
 69 
4.2.2 Nanowire switching 
 The NWs can be switched from a low resistance to a high resistance state by 
applying a short voltage pulse, as in previous studies49, 125. Despite the intrinsic, 
amorphous germanium oxide of 2-5 nm thickness on the NW surface, switching back 
to the low resistance state was not observed unless the NWs were coated in an extra 
encapsulation layer.  Figure 4.5 shows the resistance as a function of switching cycle 
for a NW that is 200 nm in diameter and 5 µm in length encapsulated with 20 nm of 
SiO2.  
  Figure  4.5: Cycling behavior. Nanowires were switched to a high resistance state with a 10 V, 200 ns pulse, and switched back to the low resistance state with a 100 mV/s scan up to 5 V.  
The NW with an initially low two-point resistance state of 44 kΩ switched to a high 
two-point resistance state of 8 MΩ after a short (200 ns) voltage pulse with 10 V 
amplitude was applied. Switching back to the low-resistance was accomplished by a 
voltage scan to 5 V at a rate of 100 mV/second. 
 There are several interesting observations. First, the resistance of the device in 
the on state drops slightly from the initial on state after the first cycle. This can 
probably be explained by annealing of the contacts via joule heating leading to a lower 
 70 
contact resistance. Second, since the resistivity in the crystalline state after the first 
cycle is 11 kΩ, the following 10 V pulses correspond to approximately 0.9 mA of 
current (or a current density of 2.9 × 106 A/cm2), which is 4 times lower than 
previously reported values for a 100 ns pulse49. Lastly, and most significantly, the on-
off ratio of our NW devices after the first cycle is increased with cycling to nearly 107. 
While this ratio is similar to what has been found in thin film studies130, a previous 
NW study has revealed a rather large diversity of values for the on-off ratio125, from 
103 to 107, and our values are at the top of this range.  
4.2.3 Investigation of high resistance in off state via SPM 
 A naive model for the resistivity of the off state might simply take into account 
the volume of transformed material. If a cylindrical plug of the NW is transformed to 
the amorphous state, one would expect the resistance to scale linearly with the length 
of this plug. Given that the value of the resistivity of the amorphous phase is between 
103 and 104 Ω·cm128, 130, a measured resistance of 100 GΩ in a roughly cylindrical 
wire of diameter 200 nm would require that the wire be more than 30 µm long, even 
taking the lower value for the reported resistivity. This observation is interesting, 
because our devices have an electrode separation less than 10 µm. Even though the 
resistivity of the amorphous GeTe devices in our NWs may be somewhat different 
than that reported for the thin films, one would assume that at least the entire device 
under measurement must transform to the amorphous phase to generate the measured 
resistance. In order to test this prediction, devices switched to a highly resistive state 
were examined via electric force microscopy (EFM).  
https://lh3.googleusercontent.com/notebooklm/AKXwDQH6GiJQApiW2ailopvCzKD8qiCJYqL3TbCivJqg9-1cLjhIN1I93_eWSPJPxGkkT07swzsq0fVgm1-ll0Y4N_4VfDV90TqSy_ol0sVP1lTAhDB6G1ZUMEEPCwzaWEpz-WkJN0h9=w822-h429-v0
8f916f66-9c5e-430b-a698-d453971de93c
 71 
  Figure  4.6: SEM, AFM, and EFM images of the same single nanowire device in a high resistance state. There is a 2 V difference between the light and dark color in the EFM image.  
Figure 4.6 shows three images of a device taken with SEM, atomic force 
microscopy (AFM), and EFM (from left to right). The contrast in the EFM image is 
due to the local electric potential and topographic features. If the whole NW had 
transformed to the amorphous phase as expected, the EFM should show a gradual 
change in contrast from one contact to the other as the potential slowly drops through 
the uniformly resistive region. The observation in Figure 4.6 is quite different however 
as the entire voltage appears to drop over a region tightly confined to the top contact, 
suggesting that the structural transformation is localized there, contrary to the 
expectation based on the naive model and the measured switching data. 
4.3 Direct TEM Observation of NWs during switching 
4.3.1 TEM observation of off state 
 The inconsistency between the predicted size of the amorphous domain and the 
https://lh3.googleusercontent.com/notebooklm/AKXwDQH5XVzdrWlZsTVHmIXCfa-X-cMwksN8Oy-JxFsvIOI2wLHgtw-zeclVvawX8UNJtYBroze-4Fbq2yoP-uudU7pavNf-d7wpQH9cGRvaKCqOsqxVVOWT6zRx5gmXK6GQUrQR-x4FPg=w335-h335-v0
c061e64c-447b-483d-808d-2cbc4a8a1ffc
https://lh3.googleusercontent.com/notebooklm/AKXwDQHHDA7GJkj6lRGlDX18sc15EO_A_MBdgClmRkZLG0Ppmx1VwyFVAWfxMdSulgY8ahvEwwToEUvmQn-U2mptA77-KwieV4oMhsfNY6alugSlGsOl2rHBy3u0_ygQl7ehh_BV87l1=w452-h491-v0
23a2537d-2dd7-4fe4-8c14-59001474e297
 72 
physical situation motivated us to fabricate the NW devices on electron transparent 
silicon nitride membranes (Figure 4.7), making possible direct observation of the 
NWs’ structure by TEM25 in the high and low resistance state.  
 
Figure  4.7: Low-magnification SEM image of a silicon nitride membrane (dark) with gold contact pads (light).  
Our initial work focused on discovering the structure of the off state after pulse-
induced switching in air without extra encapsulation. During TEM observation, care 
was taken to avoid e-beam induced damage. 
 
Figure  4.8: Nanowire before (lower left inset) and after pulsing (main panel); the switching mechanism is identified as void formation at the top contact (upper right inset). 
 
 73 
The bottom left inset of Figure 4.8 shows a TEM image of a NW device before 
switching. The initial two-point resistance was 8 kΩ. The NW was very stable with 
respect to 200 ns square pulses with voltage below 10 V. After a 10 V pulse in air, 
which resulted in a current of approximately 1.3 mA, the two-point resistance was 
changed to 1012 Ω. 
 Simultaneously, a dramatic structural change was observed close to one of the 
contacts (bright contrast in NW, Figure 4.8 (main panel and inset)). We observed a 
thin amorphous hollow tube of GeO2 confirmed by EDS, indicating that a void formed 
in the NW. GeO2 is highly resistive and even a small segment close to the metal 
contact can increase the measured NW resistance up to 1012 Ω, suggesting that void 
formation could be a switching mechanism for the devices we measured on regular 
silicon chips. 
Considerable effort was invested to apply pulses just large enough to raise the 
resistance of the NWs without forming voids. A 20 µs voltage pulse of 3.5 V applied 
to a device with a large electrode separation of 15 µm and resistivity of 12 kΩ, 
resulted in very little change. Only some hillock formation and small pinholes were 
observed (Figure 4.9).  
https://lh3.googleusercontent.com/notebooklm/AKXwDQHSoFbTWDCrTQRenizFcDfqBlgDn3XHdUbXKCclh0tdOo0UTdVol9hz9fwp5wDGpWRWq6bqMlFEDXx1yf7nh3L5aN7r7CuFSDltvaLLpRDz8b2UGIFmdp9iWYQR1YEBVh4yll-6cQ=w843-h358-v0
0e425f4e-57e4-4ca2-9b8d-3bedd04fa258
https://lh3.googleusercontent.com/notebooklm/AKXwDQEIIpM9LB3OHi51qX4UnyeQVU_pGaIJD6ax0qKwBJg0hdCr_fULR_KJV1CW45xfHTtfWYP7rBJt31uXR9foGYa-jUAxPUjBrjFoGJoRMp3yUye8Y3xuePnwwH5WfZ7UNmTbczra=w797-h377-v0
898e5e56-328c-4a04-a161-6f370d1ba471
 74 
 
Figure  4.9: a.  TEM image of nanowire after a 3.5V, 200ns pulse shows only minor changes including a bulge and small pinhole evaporation. b. Higher magnification image of bulge and pin hole c. Higher magnification image of pinhole close to contact.  
When the pulse was raised to 4.0 V, the resistance increased by a factor of 104 to 100 
MΩ and a surprising variety of structural transformations were observed (Figure 
4.10a). 
 
Figure  4.10: a. Low-magnification TEM image of nanowire after a long low magnitude pulse. b. Banded planar defect structure. c. Void and amorphous region formation. Area I is amorphous and Area II, like the rest of the wire, is crystalline (SAED inset).  
Bulging and small voids are formed as before, but we also observe a periodic set of 
planar defects in one section of the NW (Figure 4.10b) that extends over several 
https://lh3.googleusercontent.com/notebooklm/AKXwDQHYrFZIMvJ--sor2i0KCHmQpStHAko_PXghNIqixBjTyCJKURUBkEbsif-RwDAxjI2PSkB2oKzwf7medg2ND8M-kT0aUksJFjGwdFns6Ot7Y54xwBJL5NUqMHUB1hXksYcn8t3GFg=w717-h224-v0
b6076852-b9d7-4198-b4ae-f1411433bd6f
 75 
microns. These defects are likely twin boundaries formed by cooling GeTe from its 
higher temperature cubic phase back to the room temperature rhombohedral phase131 
and can also be epitaxial misfit upon re-growth of material with different compositions. 
Further studies are required to clarify these details. A region that was transformed to 
the amorphous state was also observed (Figure 4.10c); its structure was confirmed by 
selected area electron diffraction of the slightly brighter area (amorphous, top inset) 
and the darker area (crystalline, bottom inset). The amorphous region has also 
undergone a composition change as shown in the comparative EDS spectrum in Figure 
4.11 (right). The amorphous region has been partially depleted of tellurium, most 
likely due to the higher vapor pressure of tellurium at temperatures sufficient to melt 
the material. The tellurium may escape the GeO2 shell through small defects formed 
during the heating process, since no tellurium rich areas have been observed. It should 
be noted that in this case the transformations occurred over large parts of the NW, 
because its resistance during the pulse is similar to the contact resistance resulting in 
less localized heating. Figure 4.11 (left) shows the voltage pulse and current response 
in the NW indicating an initial resistance of only 3.7 kΩ.  
 
Figure  4.11: Pulse applied to NW shown in Figure 4.10a; blue is the applied voltage, and red is the current through the device (left). EDS spectrum of areas I and II from Figure 4.10c (right).  
https://lh3.googleusercontent.com/notebooklm/AKXwDQEhM00a4RQmKqNaPtPfo3K2KwV0KIbW6tEg0_JeBXzPvsIKYJWOneuKLXZsHaFEEdNzMqib0RclbNhHDXraxnrVupTyIo5A7AssPOTQk95cbNinLmzBj4dGzkJK9080UGGpySacmQ=w867-h298-v0
6654d100-2eba-4c05-8d01-33ae02fb7f03
 76 
These experiments dramatically illustrate the fundamental mechanisms that render 
reversible switching in these systems impossible without a high quality encapsulating 
shell, but the large number of structural transformations observed in the ex situ study 
makes it very difficult to determine which structural transformation is chiefly 
responsible for the measured resistance change during reversible switching.  
4.3.2 Real-time observation of dynamic behavior: opening and closing of voids 
In order to determine which of the observed behaviors was the primary 
contributor to the resistance change, the real-time dynamic behavior of the NWs was 
observed via in situ electron microscopy of the devices under a voltage scan. Figure 
4.12 and 4.13 summarize the surprising results of these measurements with a NW 
coated with 20 nm sputtered silicon oxide (Figure 4.12 inset). Figure 4.12 shows the 
electrical and structural behavior of the NW beginning with its as-fabricated state with 
a low initial two-point resistance of 3.7 kΩ. As in the ex situ observations, the initial 
increase in resistance between points I and II in Figure 4.12a was correlated with the 
formation of a small void.  
 
Figure  4.12: a. Voltage scan on a single nanowire device (inset). The blue square in the inset shows the location of the TEM observation in (b). b. TEM images taken in situ during the voltage scan in panel, at times I, II, III, and IV. Note the correlation of resistance with void size. 
https://lh3.googleusercontent.com/notebooklm/AKXwDQFz5GlTHRt003WLnVc9Cds1_A5HGPjq46cZUaJwrSEMd9xrvFin0VZKRWg8fhNLcWjAeF6tWdOYhV7uTJH3I8zlTJoXOT2HwPY0j3W7_l4KcPszjA3lKymnp2PsbjH5hDqNXjp-0w=w587-h202-v0
d80c98e5-6ee6-44e2-96bf-1e4f52efe6ed
https://lh3.googleusercontent.com/notebooklm/AKXwDQEg7IY8vRf77THfHKFJId8iljV31AzMxpXllHllfbzhhXRO9c8M0A_2yFxfcJ8cT7PGeE4237QJMWvrex-ZEgqm_mIqLLK1p3tzW0agGI_A9v0J7a2rfjpEeCsoevQP3cWkW6P48A=w860-h228-v0
3a55b0ce-ca1c-4530-9eb0-56e80581c4c7
 77 
As more current was applied, the resistance of the device continued to rise, correlated 
with the growth of the void. A thin shell of GeTe material on the inside of the 
encapsulating oxide tube appeared to provide a current path through the device around 
the void. A blue rectangle shows where the initial structural changes occurred due to 
the voltage scan as shown in Figure 4.12b. At the end of the scan the NW’s resistance 
had increased to 42 kΩ (~10 times the original resistance), and the void had grown to 
almost 1 µm in length. Similar opening of voids could also be achieved by pulsing the 
nanowire, but there tended to be less GeTe remaining resulting in higher final 
resistances.  
 
Figure  4.13:  TEM micrographs showing void formation via voltage pulse.  
For example, Figure 4.13 shows the same nanowire before and after applying a 4V 
square pulse.  The pulse was strong enough to move the GeTe material and leave a 
large void inside the nanowire. 
Remarkably, a new mechanism for returning the device to a low resistance 
state was observed (Figure 4.14). When a small voltage was applied, the NW remains 
in a high resistance state, and large void regions were observed by TEM. As the 
voltage was scanned past 1.5 V, movement in the remaining material was observed 
(SEM sequence in Figure 4.14). Between points ‘S’ and ‘F’, the TEM images suggest 
https://lh3.googleusercontent.com/notebooklm/AKXwDQFkSUCOQRZmCSJQryE4OLkMkLbAbwaqLqGrLDG6C-WF7hdLK5Yx82Q9faxIvT2S5_xPSeJ-1JNOGwZlbOU0FGsypiKnlbuHzW9s8oOWKlX6iIJB1bCy_s969qeaab8C_yTJo9bf=w751-h673-v0
5c95c410-fc43-417e-97fb-aa7acf26acd3
 78 
that the material became molten, and the shell was suddenly refilled with material. 
This closing of the void was correlated with a large increase in the measured current, 
carrying it over the compliance set for the measurement (Figure 4.14).  
 
Figure  4.14:  In situ TEM observation showing closing of void and corresponding voltage scan.  
The final resistance measured was similar to the resistance of the NW in its original 
state before any void formation had been observed. Though counter-intuitive, this void 
formation mechanism is the best candidate for explaining the extremely large on-off 
ratios observed in the many NW devices fabricated and tested on regular substrates.  
https://lh3.googleusercontent.com/notebooklm/AKXwDQGKwrCNoCZoHj_w0zDkvXOCD3oWxQ6S83zbxfKhnFWtkG78hyHxFo7iz0qhv86tusH98rF-_PpFZG8u5ucdbBlGy9SqSwiNsqiiBpPR0ByiEY2tAJKjsvaedxaTM06g6EGsQ-bX1w=w407-h301-v0
e18a80b3-ce28-4b25-beba-6ff32a975c01
 79 
 
Figure  4.15:  Material movement in void induced switching.  a. SEM after multiple cycles.  b. Schematic showing the movement of material inside the NW.  
 SEM images of the NW after several cycles of this behavior are shown in 
Figure 4.15a, in which the bright (dark) contrast on the NW indicates the presence 
(absence) of GeTe materials. Since part of the NW outside the contact appears to be 
empty (dark), it is evident that the material in the NW outside the contacted region can 
be a source for refilling voids. A schematic (Figure 4.15b) illustrates the observed 
flow of material that was observed: the NW region outside the contacts acted as a 
reservoir allowing more material to enter the NW and close voids.  Material could 
escape through small cracks or pinholes in the oxide shell. 
The exact mechanisms that lead to movement of material are not yet 
understood, but all our TEM studies have shown that the structural transformations are 
localized to rather small regions of the NW. These regions are usually, but not always, 
located close to the contacts.  To better understand the significance localized heating 
plays in the motion of material, my collaborator, David Schoen, made a simple model 
with commercially available software (COMSOL Multiphysics).  The model confirms 
that localized heating can play a major role in the behavior of the NW99.  The 
 80 
temperature distribution in the NW is highly influenced by contact resistances or other 
hot spots (such as voids).  The actual pattern of transformation in a NW can be very 
complicated and narrow regions can move.  Hence, one might expect the heating 
during a voltage scan to be highly dynamic. Since voids can form on either or both of 
the positive and negative electrode after a pulse or scan, and material can move in 
either direction in the same NW during the same scan, electromigration can probably 
be ruled out as a dominant mechanism. Instead, capillary forces and expansion of 
material due to melting and pressure buildup in the oxide encapsulation due to the 
evaporation of tellurium seem the most likely candidates to explain to the observed 
motion of liquid PCM material. 
4.4 Conclusion 
 Our in situ TEM study revealed the mechanism responsible for the very high 
resistance state in GeTe NWs.  Surprisingly, rather than the expected crystalline to 
amorphous transition, we found that the reversible switching mechanism was 
dominated by the opening and closing of voids inside the NW.  This new switching 
mechanism could potentially be useful in devices that require a very high resistance in 
the OFF state.  However, using this mechanism in a useful switch (i.e. one that can 
switch more often in a well controlled manner) would require a significant amount of 
engineering.  The device geometry presented here is not ideal for such a purpose, 
because switching endurance is limited to dozens of cycles.  It might be possible to 
engineer a switch using a larger reservoir of material so that switching could be 
repeated many times. 
 81 
 While our study showed interesting behavior in phase-change NWs, one 
important question remains: why did we not observe the expected crystalline to 
amorphous transition?  Since we saw melting, but never a pure amorphous phase, the 
most likely explanation is that we could not achieve cooling rates sufficient to vitrify 
GeTe.  In order to achieve the crystalline to amorphous transition, it may be necessary 
to make design changes to achieve higher cooling-rates.  However, very good 
switching performance has been observed in GST NWs48.  Hence, it would be 
interesting to use this in situ technique to observe the details of switching in GST 
NWs and compare it to our observations presented in Chapter 2. 
https://lh3.googleusercontent.com/notebooklm/AKXwDQHZX6XTMxf3FYrG6z9TjPyA-BdPjWiNYlcV7HF9NYeR-vCV9UEokgP-SmEhu2QblOLFoe6LIQaXt4TOShPvtkiicQptvCdyyFpOV1x-BVVg1p8lpKPapo_2QDepepUirhtxZc5u1A=w572-h238-v0
6931fb3c-da0a-47e2-8a06-21251b015433
 82 
5 Topological insulator nanoribbons 
5.1 Introduction and motivation 
 Topological insulators, a new class of materials which are insulating in the 
bulk but have conductive surface states, have generated great interest since their 
theoretical discovery in 200514-18, 82, 132-134. Theory predicts many fascinating 
electronic properties in topological insulators, including spin-polarized dissipationless 
current. However, few transport measurements have shown signatures of the 
topological states. 
 
Figure  5.1:  Schematic of (a) bulk sample of Bi2Se3 and corresponding (b) band diagram.  
The reason for this discrepancy is that bulk samples tend to have many intrinsic 
defects that act as electron donors, effectively lowering the resistance of the materials.  
Figure 5.1a shows a schematic of a bulk sample that serves to illustrate the difficulty 
of measuring the surface states.  A bulk crystal is typically 1mm thick, consisting of 
approximately 1 million quintuple layers.  If the bulk layers contribute to the 
conduction mechanism, it is very difficult to measure the contribution of the surface 
states because of the small signal-to-noise ratio (1 million bulk layers compared to 2 
https://lh3.googleusercontent.com/notebooklm/AKXwDQEYRE6oPh3QZY6QbIawA7KNshSltW4yLDM9NVVbEDiZH04mPYzUpHLr9XYQVHB6_4Qwbf7Yb2lQzd6hAMMwJM5qL8PJu8ZxutyRUZJf7gu2iJhQlV86t7pF_MoRUqY5eatc42xDyQ=w744-h160-v0
4359b52f-1b6e-4fdd-aa50-1aab9ba4af5e
 83 
surface layers).  The band structure of a bulk crystal looks similar to that of a 
degenerately doped semiconductor with the Fermi level in the conduction band 
(Figure 5.1b).  In order to decrease the contribution of the inner layers to conduction, 
we synthesized and measured topological insulator nanoribbons.  Figure 5.2 depicts a 
schematic of a nanoribbon (NR) that consists of only 20-100 quintuple layers, greatly 
increasing the surface-to-volume ratio.  In nanoribbons, the bulk contributes much less 
to the overall conduction, producing a more favorable signal-to-noise ratio (20-100 
bulk layers compared to 2 surface layers) for the study of the topological states. 
 
Figure  5.2:  Schematic of topological insulator nanoribbon   
 The work for this chapter was a fruitful collaboration with Hailin Peng, Keji 
Lai, Desheng Kong and Yulin Chen.  All contributed to the experiments and to the 
analysis of the results. I was heavily involved in the synthesis, characterization, device 
fabrication, measurements and analysis discussed in this chapter over the span of one 
year, but the work is a result of our close collaboration. 
5.2 Synthesis of topological insulator nanoribbons 
 From our experiments with gallium selenide135  we learned that these layered 
compounds grow into both nanowires and sheet-like structures called “nanoribbons”.  
Since Bi2Se3 has a layered structure, we expected that it could grow into nanoribbons 
https://lh3.googleusercontent.com/notebooklm/AKXwDQGcO4FRL6kJEkGyvKBYqdUKnayljPgTuHZKmBoGibuIUwG_WnLVfu5chvf36GgZoUwCpNdlnf7RoOc6RClOmbqK6_rZlVjXPzcR0V81AIE2LCYdB7B00-ubVki27aHwcUTXt-KfGw=w795-h265-v0
33450408-e37d-4f97-8839-30419bb65f8b
 84 
as well.  Wide nanoribbons have the advantage of allowing for important experimental 
techniques such as the Hall effect measurement, an important tool in the 
characterization of these materials.  We synthesized Bi2Se3 NRs in the same VLS 
growth furnace that was set up for GeTe NW growth (chapter 2). 
 The range of possible growth parameters for Bi2Se3 turned out to be relatively 
large.  For a typical synthesis136 we placed the source material, Bi2Se3 powder 
(99.999%, 0.2 g per growth from Alfa Aesar), in the hot center of the furnace and we 
put Si (100) substrates, functionalized with 0.1% w/v aqueous poly-L-lysine solution 
(Ted Pella) and coated with 20 nm Au nanoparticles (Sigma Aldrich) in the 
downstream side of the furnace at distances ranging between 6 to 12 cm from the 
center. We initially pumped down the tube to a base pressure of less than 100 mTorr 
and flushed with Ar gas several times to remove O2 residue. We then heated the 
furnace to 450-580 °C (setpoint at hot center of the tube) and maintained this high 
temperature for 1-5 h while flowing 30 standard cubic centimeters (sccm) Ar carrier 
gas.  Finally, we allowed the system to cool down over the time span of a few hours. 
After the synthesis, a gray layer covering each substrate over a 1 cm2 area could be 
observed by the unaided eye. 
 
Figure  5.3:  SEM of as-synthesized Bi2Se3 nanoribbons. 
https://lh3.googleusercontent.com/notebooklm/AKXwDQHeQg7CoAgCf7-yNEEX-eadiTNCrpHTY6WCkwX6G02_CcJzPRCbzSocc0_WHOP3kpib3Zos81LPWbBiTclKly30i1d2HzV_ttXxBoYLfcMwhS7zT3OH_w8lsf8yyaTg8TOgvWKm=w869-h532-v0
b41c5272-0cd4-4878-a19d-d9c7c86ae0c1
 85 
 Our SEM observations (Figure 5.3) confirmed that Bi2Se3 could grow in a 
nanoribbon or sheet-like form.  Indeed, we observed sheets with lateral dimensions of 
over 100 μm for the longer growth times.  However, the thickness of the sheets tended 
to range between 20-100 nm. 
 
Figure  5.4: SEM and AFM of Bi2Se3 NR device. Graph shows height measurement of AFM cross section.  
To confirm the thickness of the ribbons we conducted AFM experiments.  As an 
example, Figure 5.4 shows an SEM and AFM image of a single nanoribbon device.  
The AFM cross section measurement shows that the thickness of the ribbon is only 22 
nm. 
 To characterize the crystal structure, growth direction and chemical 
composition of the NRs, we performed TEM and EDX characterization.  Figure 5.5 
depicts a TEM image of a nanoribbon. The SAD pattern and HRTEM (Figure 5.5 
https://lh3.googleusercontent.com/notebooklm/AKXwDQFCJNsTy6SQ9MoUUuBVhA03Xc2DVPPAfmeCbSQmQzQfbCc0b4t_idxTEy4u6oaV_ZWCpvfN9fTgABHeo4Cudt91oyf6Jwomgi8uUH-FBhCgexLCMoFq9aRCMdUOan-Mj7w4g9ey-A=w336-h308-v0
b8ca79ca-d088-4b61-b5ac-ab525713e400
 86 
insets) shows a hexagonal pattern confirming that the top face is perpendicular to the 
[001] direction.  The growth direction is equivalent to a [11-20] direction, which 
agrees with our observation of other nanowires135, 137 with a layered structure. 
 
Figure  5.5: SEM and AFM of Bi2Se3 NR device.  Graph shows height measurement of AFM cross section.  
The HRTEM image shows hexagonal lattice fringes with a lattice spacing of 2.1 Å 
between (11-20) planes, in agreement with the literature value.  As a result of their 
crystal structure and growth direction, nanoribbons have a rectangular cross section 
perpendicular to the growth direction.  The EDX analysis confirmed that the 
composition was Bi2Se3 to within ~2% experimental error. Further AFM and scanning 
tunneling microscopy measurements showed that the NRs had atomically flat surfaces 
with 1 nm step edges136.  Our characterization of the Bi2Se3 NRs confirmed their 
suitability for transport measurements due to their very high surface-to-volume ratio 
and compatibility with Hall measurements.  These measurements are discussed in the 
following sections. 
https://lh3.googleusercontent.com/notebooklm/AKXwDQHBzQ3A61fSD9_qC5uOEx70mO4z6enWp927MldSA-N6b5YomqeuhXJrQYbbGTpM1BfOwFnMG27vLXPg7xSe4lU4D20spQ8KGKzl0A4BFRse4tYJD9LEu1FLeDypKQ3v57FuH5v04Q=w475-h259-v0
a9b5da47-9af2-4486-bdf6-ad088b8a50d1
 87 
5.3 Electrical characterization of nanoribbons 
 In order to characterize the electronic properties of the as-synthesized Bi2Se3 
NRs, we fabricated devices via the electron beam lithography method discussed in 
Chapter 4.1.2.  Figure 5.6 shows a schematic of a device that allows for 4-point probe 
and Hall measurements on the same NR. 
 
Figure  5.6: Schematic of NR device.  Setup allows for 4-point probe (green V-) and Hall (blue V-) measurement  on the same ribbon.  
The resistivity of an n-type doped semiconductor is given by ρ 
= 1 
e 
⋅ μ ⋅ 
n 
, where e is 
the electron charge, μ is the electron mobility and n is the electron density.  Similarly, 
the Hall resistance is RH 
= −1 
n 
⋅ 
e 
.  Hence, measuring the resistance and Hall resistance 
allows us to deduce the carrier concentration and the mobility as long as we know the 
dimensions of the ribbon.  Low-frequency (1,000 Hz) and d.c. standard four-probe 
magnetoresistance measurements were carried out in a Quantum Design PPMS-7 
instrument. The temperature range is 2-300 K and the magnetic field can be applied up 
to ±9 T. 
 Figure 5.7 shows a basic device for a narrow ribbon.  These ribbons are not 
wide enough to make Hall Probe contacts, but they are useful for measuring the 4-
https://lh3.googleusercontent.com/notebooklm/AKXwDQFNDs_wrkEacCHy4ztOAJFxHASy6EUfnWUN9l3v0LfQZ87UIdpI_fNa1r5HFw4ybTpDlw8eyc7dPKmLPEcB3m8a8fRU3dVMQcMetM4NMbpMmm5LZDgjm0kxVYxwvXkMfJHSTgZE=w712-h484-v0
1364b88e-db20-476d-8c79-12f0086ad4a3
 88 
point probe resistance.  To make Ohmic contacts we evaporated either Cr/Au or Ti/Au 
contacts with a thickness of approximately 5/195 nm.  After measuring dozens of 
devices we found that the contact resistance was typically negligible and the sheet 
resistance of the devices at room temperature was typically on the order of a few 100 
Ω, demonstrating that the nanoribbons are still quite conductive, similar to bulk 
crystals. 
 
Figure  5.7: SEM of Bi2Se3 NR device at 30° rotation.  Even though the NR appears bent it is lying flat on the substrate and the contacts are on top.   
 Figure 5.8 shows the four-terminal resistance of a device from room 
temperature down to 2K.  The resistance decreases with temperature and reaches a 
minimum value below 20 K.  This behavior agrees with that of heavily doped 
semiconductors.  The doping in Bi2Se3 NRs is believed to be due intrinsic defects such 
as Se vacancies138.   
2 μm
 89 
 
Figure  5.8:  Resistance as a function of temperature for Bi2Se3 NR.  
These measurements indicate that the conduction mechanism in NRs is still dominated 
by bulk carriers, despite the single crystalline nature and high quality of the ribbons.  
The Fermi level appears to remain inside the conduction band as depicted in Figure 
5.1. 
 To measure the mobility, we fabricated devices that allow for 4-point and Hall 
measurements (Figure 5.9) on the same NR.  For the Hall measurement, a known 
current is driven through the device (indicated by I+ and I- in Figure 5.5) and the 
voltage is measured between electrodes that are aligned perpendicular to the flow of 
current while a magnetic field is applied perpendicular to the top face of the NR. 
600 700 800 
900 1000 1100 1200 1300 1400 
1500 1600 1700 
R es 
is ta 
nc e 
(O hm 
) 
0 50 100 150 200 250 300 Temperature (K)
https://lh3.googleusercontent.com/notebooklm/AKXwDQHHEUUokiXJsAMLpGVM5qFiMwLKCajg5pMJTnvbOfj0u-zBX5wdDrEeoQrgZJGQGAQUq62F_iCa_dsJmqqnXn4DowwJmY7r6e7GtKvquYrlmwYmem7ZoZi2VsguvigWO_8ncXKFGA=w355-h283-v0
0890d5e3-d206-4288-b08f-358ad95e2915
https://lh3.googleusercontent.com/notebooklm/AKXwDQF-owlYnx_M_T3htcbrmm1dj5jDki5OmO-SnkxPVfc2dmCsIJYNyikkLkfu4clIEOgc-18s9Krd3Vo1SZTuocfsrtpCOnC9p_dLGJ8UDfAPawdqCMOSuKCtNmKDf263YIknXtFL=w712-h484-v0
f1cad95c-5849-4b49-8b44-a9807a7c9655
 90 
 
Figure  5.9: SEM Bi2Se3 NR device.  This setup allows for 4-point probe and Hall measurements on the same device.  
We measured over 10 Hall bar devices and generally observed two types of behavior 
(Figure 5.10).  Some devices showed very linear behavior with a relatively small slope 
corresponding to a high carrier area density (in this case 1.5×1014 cm-2).  Other 
devices had a larger slope corresponding to a lower density (in this case 2.6×1013 cm-
2) at low magnetic fields.  Interestingly, in the low density samples, we could observe 
a difference in slope between the low and high magnetic field measurement. 
https://lh3.googleusercontent.com/notebooklm/AKXwDQFOA_JShmsrK6z6y6v9fC5yW4P3dSATo1JwTemUrCMOnQLsd1Vl4cjhoXfJd1NsD-gBi3IopAJA755bwEPzb77U-yMrVfR5Aqrj5YdMAxG6_u3MuXynGs1mQkZS4kSyvoyuY7gnbA=w541-h429-v0
a402ed7b-4353-4ae8-8638-8d58f6f72e61
 91 
 
Figure  5.10: Hall measurements of two different devices showing different behaviors.  
This change in slope is typically due to the presence of two types of carriers with 
different mobility.  In this case, it is likely that the slope change is due to the surface 
states that were masked by excessive bulk carriers in the high density samples.  All the 
measurements showed clear n-type behavior by the sign of the Hall slope.  The 
variation in carrier density is probably due to variations in the defect concentration in 
the NRs.  To study this further, it would be interesting to perform in situ TEM studies 
of the NRs allowing a correlation between structure and electrical parameters.  
However, in our regular TEM observations we did not see a large variability in the 
morphology or composition for most ribbons.  The measured mobility was on the 
order of 2000 cm2 V-1 s-1. 
 The measurements in this section show that NRs, despite their favorable 
surface-to-volume ratio, are still dominated by bulk conduction.  In order to find more 
experimental proof of the surface states, we conducted magneto-resistance 
https://lh3.googleusercontent.com/notebooklm/AKXwDQHls4eM13f2RndZNcyvTZt162KT4T0Z9Y5boDpdi6df-7wgLOYN-F3Fwhk62GNI9anczZwVbSjFH5kCKrhdf23v7TfBFdsN0vYL5zOPZ2qwPnJd3IeDErEgfQSgVG2savP8STxohQ=w491-h313-v0
8d031c9b-fa96-4e50-baf2-df6ddecaecf2
 92 
measurements to look for Aharonov-Bohm oscillations32.  These measurements are 
discussed in the following section. 
5.4 Aharonov-Bohm interference in topological insulator 
nanoribbons 
5.4.1 Introduction to Aharonov-Bohm effect 
Since the conduction in Bi2Se3 is dominated by bulk carriers originating from 
crystal defects and thermal excitation, it is difficult to perform transport measurements 
on the surface states.  To prove the existence of surface states we set out to measure a 
transport signature of the topological states via the Aharonov-Bohm Effect. 
 The Aharonov-Bohm (AB) effect is strongly related to one of the fundamental 
mysteries of quantum mechanics: the double slit experiment (Figure 5.11).  When 
more than one path is available to an electron, the electron can interfere with itself, 
creating an interference pattern. 
 
Figure  5.11: Schematic of double slit experiment.  
https://lh3.googleusercontent.com/notebooklm/AKXwDQFC-plseStjxaFaMOWNwQlYOCAgopoDOIlIrk0oShcyQ52m8BBDzkLwLisxUp2ihPqSi5BFBf8EYqZus6JXLYdw0QoEuQlojyo8dbLyBYgRSp7Ufo9s8jJtlcMoesbX_smqqRL44w=w284-h275-v0
04decf51-9c76-462e-8022-4e2239b576c3
 93 
In the AB effect, the electrons also have multiple available paths; however, the 
electrons also pass through a magnetic field that changes their quantum phase.  Figure 
5.12 shows a schematic of a conducting ring structure that provides two pathways for 
the electrons.  A magnetic field is applied perpendicular to the electron flow.  When 
the magnetic field strength is varied, the change in quantum phase gives rise to 
constructive and destructive interference between the electrons139.  This interference 
can be measured as oscillations in the resistance of the ring structure.  The 
characteristic periodicity in the magnetic field is given by ∆B = Φ0/S, where Φ0 = h/e 
is the flux quantum, S is the area enclosed by the electron pathways, h is Planck’s 
constant and e is the electron charge. 
 
Figure  5.12: Schematic of Aharonov-Bohm experiment.  
Further, the AB effect has been measured in conducting cylinders such as carbon 
nanotubes140, In2O3/InOx core-shell NWs141 and other NWs that have special surface 
states142, 143.  In these cases, the same periodicity in resistance fluctuations is observed 
if the magnetic field is aligned along the NW and S is taken to be the cross-sectional 
area of the NW.  It is important to note that the AB effect is only observed when just 
https://lh3.googleusercontent.com/notebooklm/AKXwDQHYbDlvaHQitOq0JT8T8MhJ07DvB45VlIVl-aeNxvpeqGQAJBFEA6ghX2ilEbON6Gr-xuu9tI4gc0UlADZTHPuWr0nsbckEstfZl8VcdqPtO5gvj9ZDIuWZEMET6VSbAQPbowVN=w294-h484-v0
c408dadc-9117-4aa0-914f-dd1e82a0699a
 94 
the surface of the NW is conducting or when the surface has distinct states that do not 
significantly interfere with the bulk conduction. 
5.4.2 Aharonov-Bohm measurement 
 AB interference can only be observed in nanostructures if the conduction 
electrons remain phase coherent after completing closed trajectories.  Hence, the AB 
effect is more likely to be seen in narrow ribbons than in very wide ones.  In order to 
look for the AB effect in the Bi2Se3 NRs, we fabricated devices of narrow NRs and 
aligned the magnetic field parallel to the ribbons.  The samples were measured at 2K 
to decrease phonon contributions. 
 
Figure  5.13: Magnetoresistance and SEM of Bi2Se3 NR  
Figure 5.13 shows an SEM of a narrow NR device and the corresponding resistance 
measurement as a function of magnetic field strength. A pronounced drop in resistance 
1250 
1260 
1270 
1280 
R es 
is ta 
nc e 
(O hm 
s) 
-10 0 10 Magnetic Field (T) 
B 
https://lh3.googleusercontent.com/notebooklm/AKXwDQHzUm022JivUeKjG2J0eebqy4zqNDEV1SPESVOSN9wM7d3lPWk6YDlO0J8Nxsx6psV3_0jaAfmwM-dAKm-QB3GMpPaOvF9rJWrLn599gAdU64n8aAf3Be6ZY6L8WPxgvWjBfzzSlQ=w480-h461-v0
b625d2ec-6309-499a-aa2c-0b804d1d6306
 95 
at zero field due to the weak anti-localization effect144 is evident, consistent with the 
presence of strong spin–orbit coupling in Bi2Se3.  For magnetic fields between -9T to 
9T, clear periodic oscillations can be observed in the resistance.  To find the 
periodicity, we first take the derivative dR dB 
 to separate the oscillatory part from the 
slow-varying background145, and then take the Fourier transform. 
 
Figure  5.14: Fourier transform of dR/dB data derived from Figure 5.X  
The Fourier transform shows a sharp peak corresponding to a periodicity of 0.62T 
(Figure 5.14).  This measurement agrees well with the expected period of ∆B = Φ0/S = 
0.63T.  The cross section, S, was determined via SEM and AFM measurements. 
5.4.3 Discussion and conclusion 
 The observation of the AB effect in Bi2Se3 NRs may represent the first 
transport measurement of the topological surface states in this material system146.  
Further, we can reach several conclusions based on our observations. First, though the 
majority of the conduction still occurs through the bulk of the nanoribbons, we can 
clearly observe the AB oscillations.  These considerations strongly suggest that there 
https://lh3.googleusercontent.com/notebooklm/AKXwDQGn8Ccvw4uTZ2MriDW0ZJnOeoOX3Jfdt1rkFjJbOCPpKLk5r7HStyyuBVE6YJ6aPIIIH9iaqJ4oQ1ZOS034j7pko-bfBa-XjLEbqJlKlt-mWhiyzh82yzJIo8PSQHwvQgVLJcUV=w221-h212-v0
ea1f519b-1799-44ee-94cb-503146826ea7
 96 
is little interaction between the bulk and surface electrons.  This is to be expected, 
because if the Fermi level is close to the bottom of the conduction band, the surface 
states and bulk states have different momentum (Figure 5.1b) making interactions 
unlikely.  Second, since the AB effect requires the electrons to move around the whole 
perimeter of the NR, our results demonstrate that the surface states exist on all the 
surfaces of the NR, not just on the basal plane.  Since the side walls expose dangling 
bonds and the quintuple layers are only linked by weak van der Waals forces, this 
observation provides further evidence for the robustness of the surface states. 
Current work in this area focuses on further lowering the bulk contribution to 
conduction via doping and gating the NRs147, 148.  Achieving pure surface conduction 
will open up new experimental possibilities for probing the surface states in these 
exciting materials. 
5.5 Conclusion 
 Topological insulators are a new class of materials with exciting prospects in 
electronics, spintronics, and other applications.  In this chapter we presented the 
synthesis and characterization of topological insulator Bi2Se3 NRs.  The high surface-
to-volume ratio helped suppress bulk conduction inside the nanoribbons, which 
allowed for the observation of Aharonov-Bohm interference.  This interference 
measurement was the first transport measurement to provide evidence of the 
topological states in this material system.  Rapid progress in the young field of 
topological insulators is producing a wealth of new knowledge; we can expect to see 
more breakthroughs soon. 
 97 
6 Conclusion 
Though we could only focus on a few materials, the research for this 
dissertation gave a glimpse of the varied and fascinating properties of chalcogenide 
materials. We concentrated on chalcogenides as phase-change memory and 
topological insulator materials, two applications with great significance for electronics.  
Phase change memory is on the verge of commercialization and could eventually 
replace flash memory, while topological insulators have the potential to transform 
current electronics by offering a new paradigm for computer design.  The right 
geometry was needed to reveal the most interesting properties of our phase-change 
and topological insulator chalcogenide materials.  Nanostructures provided high 
crystal quality, TEM compatibility and a large surface-to-volume ratio.  These 
properties made possible in situ TEM observation of phase-change memory cells and 
measurement of Aharonov-Bohm interference in topological insulators.  The studies 
yielded several interesting and often unexpected results. 
We developed in-situ TEM switching of phase-change materials, enabling 
direct correlation of electrical switching behavior with structural changes. Our in situ 
study of lateral phase-change cells showed significant variability in the microstructure 
of the high-resistance phase; even in the same cell after applying the same 
amorphization pulse.  We observed a pure amorphous phase as well as a mixed 
amorphous phase containing crystalline residues, both with similar high resistances 
but different threshold switching behavior.   This finding can assist in the design of 
better PCM cells through control of the microstructure of the OFF state.  Our in situ 
 98 
study of phase-change GeTe nanowires allowed us to explain the very high resistances 
observed in the OFF state, and we discovered a new switching mechanism: reversible 
void formation.  In the future, this mechanism could be exploited to create devices 
with a highly resistive OFF state, though careful engineering would be required to 
achieve sufficient device endurance. Our in-situ studies of the phase-change cells and 
nanowires during switching provided important insights into the detailed mechanisms 
of the phase-change.  The in situ TEM technique applied to PCM studies can be an 
effective tool to elucidate important topics in phase-change memory such as the origin 
of resistance drift, scaling and differences in materials. 
In our topological insulator study, we synthesized single-crystal nanoribbons 
because they offer a large surface to bulk conduction ratio.  These nanoribbons 
enabled us to measure the AB effect, and hence to observe one of the first electrical 
signatures of the topological states.  Doping and gating may help to further suppress 
the bulk conduction and to enable future spintronics devices. 
 99 
References 
1. Schock, H.-W. & Noufi, R. CIGS-based solar cells for the next millennium. 
Progress in Photovoltaics: Research and Applications 8, 151-160 (2000). 
2. Chu, T. L. Thin film cadmium telluride solar cells by two chemical vapor 
deposition techniques. Solar Cells 23, 31-48 (1988). 
3. Pelusi, M. et al. Photonic-chip-based radio-frequency spectrum analyser with 
terahertz bandwidth. Nature Photonics (2009). 
4. Ho, N. et al. Single-mode low-loss chalcogenide glass waveguides for the mid-
infrared. Optics Letters 31, 1860-1862 (2006). 
5. Lamont, M. R., Luther-Davies, B., Choi, D., Madden, S. & Eggleton, B. J. 
Supercontinuum generation in dispersion engineered highly nonlinear (γ = 10 
/W/m) As2S3 chalcogenide planar waveguide. Opt. Express 16, 14938–14944 
(2008). 
6. Paivasaari, K., Tikhomirov, V. K. & Turunen, J. High refractive index 
chalcogenide glass for photonic crystal applications. Optics Express 15, 2336-
2340 (2007). 
7. Jha, R. & Sharma, A. K. High-performance sensor based on surface plasmon resonance with  chalcogenide  prism and aluminum for  detection  in  infrared. 
Optics Letters 34, 749-751 (2009). 
8. Zogg, H. et al. IV-VI mid-IR tunable lasers and detectors with external 
resonant cavities. Proc. of SPIE 7453, 74530R (2009). 
9. DiSalvo, F. J. Thermoelectric Cooling and Power Generation. Science 285, 
703-706 (1999). 
10. Kim, Y. et al. Structural and thermoelectric transport properties of Sb2Te3 thin films grown by molecular beam epitaxy. Journal of Applied Physics 91 (2002). 
11. Zhang, T. et al. High Speed Chalcogenide Random Access Memory Based on 
Si2Sb2Te5. Jap. Journ. App. Phy. 46, L247–L249 (2007). 
12. Wuttig, M. & Yamada, N. Phase-change materials for rewriteable data storage. Nature Materials 6, 824-832 (2007). 
13. Kane, C. L. & Mele, E. J. Quantum spin Hall effect in graphene. Phys. Rev. Lett. 95, 226801 (2005). 
14. Bernevig, B. A., Hughes, T. L. & Zhang, S.-C. Quantum Spin Hall Effect and 
Topological Phase Transition in HgTe Quantum Wells. Science 314, 1757-
1761 (2006). 
15. Fu, L., Kane, C. L. & Mele, E. J. Topological insulators in three dimensions. 
Phys. Rev. Lett. 98, 106803 (2007). 
16. Moore, J. E. & Balents, L. Topological invariants of time-reversal-invariant 
band structures. Phys. Rev. B 75, 121306 (2007). 
17. Qi, X. L., Hughes, T. L. & Zhang, S. C. Topological field theory of time-
reversal invariant insulators. Phys. Rev. B 78, 195424 (2008). 
18. Zhang, H. et al. Topological insulators in Bi2Se3, Bi2Te3 and Sb2Te3 with a 
single Dirac cone on the surface. Nature Physics 5, 438-442 (2009). 
19. Morales, A. M. & Lieber, C. M. A laser ablation method for the synthesis of 
crystalline semiconductor nanowires. Science 279, 208-211 (1998). 
 100 
20. Wagner, R. S. & Ellis, W. C. VAPOR-LIQUID-SOLID MECHANISM OF 
SINGLE CRYSTAL GROWTH. App. Phys. Lett. 4, 1753975 (1964). 
21. Duan, X., Wang, J. & Lieber, C. M. Synthesis and optical properties of gallium 
arsenide nanowires. App. Phys. Lett. 76, 1116-1118 (2000). 
22. Guichard, A. R., Barsic, D. N., Sharma, S., Kamins, T. I. & Brongersma, M. L. Tunable Light Emission from Quantum-Confined Excitons in TiSi2-Catalyzed 
Silicon Nano Lett. 6, 2140 (2006). 
23. Hochbaum, A. I. et al. Enhanced thermoelectric performance of rough silicon 
nanowires. Nature 451, 163 (2007). 
24. Boukai, A. I. et al. Silicon nanowires as efficient thermoelectric materials. 
Nature 451, 168 (2008). 
25. Y., C., Wei, Q., Park, H. & Lieber, C. M. Nanowire Nanosensors for Highly 
Sensitive and Selective Detection of Biological and Chemical Species. Science 
293, 1289 (2001). 
26. Patolsky, F. & Lieber, C. M. Nanowire nanosensors. Mater. Today 8, 20 
(2005). 
27. Chan, C. K. et al. High-performance lithium battery anodes using silicon 
nanowires. Nature Nanotech. 3, 31 (2008). 
28. Schoen, D. T. et al. Phase transformations in one-dimensional materials: 
applications in electronics and energy sciences. J. Mater. Chem. 19, 5879– 
5890 (2009). 
29. Peng, H. L., Xie, C., Schoen, D. T. & Cui, Y. Large Anisotropy of Electrical 
Properties in Layer-Structured In2Se3 Nanowires. Nano Lett. 8, 1511-1516 
(2008). 
30. Lai, K. et al. Nanoscale Electronic Inhomogeneity in In2Se3 Nanoribbons 
Revealed by Microwave Impedance Microscopy. Nano Lett. 9, 1265-1269 
(2009). 
31. Merget, F., Kim, D. H. & Haring Bolivar, P. Lateral phase change random 
access memory cell design for low power operation. Microsyst. Technol. 13, 
169-172 (2007). 
32. Aharonov, Y. & Bohm, D. Significance of electromagnetic potentials in the 
quantum theory. Phys. Rev. 115, 485-491 (1959). 
33. Raoux, S., Welnic, W. & Ielmini, D. Phase Change Materials and Their 
Application to Nonvolatile Memories. Chem. Rev. 110, 240-267 (2010). 
34. Terao, M., Morikawa, T. & Ohta, T. Electrical Phase-Change Memory: 
Fundamentals and State of the Art. Jap. Journ. Appl. Phy. 48, 080001 (2009). 
35. Jedema, F. Phase-change materials: Designing optical media of the future. 
Nature Mater. 6, 90-91 (2007). 
36. Ovshinsky, S. R. Reversible electrical switching phenomena in disordered 
structures. Phys. Rev. Lett. 21, 1450-1453 (1968). 
37. Kim, K. & Koh, G. H. in 24th International Conference on Microelectronics 377-384 (2004). 
38. Bez, R. & Cappelletti, P. in Symposium on VLSI Technology 84-87 (2005). 
39. Akerman, J. Applied Physics: Toward a Universal Memory. Science 308, 508 
(2005). 
 101 
40. Scott, J. F. & Paz de Araujo, C. A. Ferroelectric Memories. Science 246, 1400 
(1989). 
41. Segal, M. Ferroelectric memory: Slim fast. Nature Nanotech. 4, 405 (2009). 
42. Yang, Y. C., Pan, F., Liu, Q., Liu, M. & Zeng, F. Fully Room-Temperature-
Fabricated Nonvolatile Resistive Memory for Ultrafast and High-Density 
Memory Application. Nano Lett. 9, 1636-1643 (2009). 
43. Wuttig, M. Nature Mat. 4, 65 - 266 (2005). 
44. Hudgens, S. & Johnson, B. Overview of phase-change chalcogenide 
nonvolatile memory technology. Mrs Bulletin 29, 829-832 (2004). 45. Solis, J. & Afonso, C. N. Ultrashort-laser-pulse-driven rewritable phase-
change optical recording in Sb-based films. Appl. Phys. A: Mater. Sci. & Process. 76, 331-338 (2003). 
46. Lankhorst, M. H. R., Ketelaars, B. W. S. M. M. & Wolters, R. A. M. Low-cost 
and nanoscale non-volatile memory concept for future silicon chips. Nature Mater. 4, 347-352 (2005). 
47. Chen, Y. C. et al. Ultra-thin phase-change bridge memory device using GeSb. 
Int. Electron. Devices Meet. Tech. Dig., 777-780 (2006). 
48. Lee, S. H., Jung, Y. & Agarwal, R. Highly scalable non-volatile and ultra-low 
power phase-change nanowire memory. Nature Nanotech. 2, 626-630 (2007). 
49. Lee, S. H., Ko, D. K., Jung, Y. & Agarwal, R. Size-dependent phase transition 
memory switching behavior and low writing currents in GeTe nanowires. App. Phys. Lett. 89 (2006). 
50. Yoon, S.-M. et al. Electrical Characterization of Nonvolatile Phase-Change 
Memory Devices Using Sb-Rich Ge-Sb-Te Alloy Films. Jpn. J. Appl. Phys. 46, 
7225-7231 (2007). 
51. Adler, D., Henisch, H. K. & Mott, S. N. The mechanism of threshold switching 
in amorphous alloys. Rev. Mod. Phys. 50, 209 (1978). 
52. Pirovano, A., Lacaita, A. L., Benvenuti, A., Pellizzer, F. & Bez, R. Electronic 
Switching in Phase-Change Memories. IEEE Trans. Elect. Dev. 51, 452-459 
(2004). 
53. Yu, D., Brittman, S., Lee, J. S., Falk, A. L. & Park, H. Minimum Voltage for 
Threshold Switching in Nanoscale Phase-Change Memory. Nano Lett. 8, 3429-
3433 (2008). 
54. Warren, A. C. Reversible thermal breakdown as a switching mechanism in 
chalcogenide glasses. IEEE Trans. Electron Devices 20, 123-31 (1973). 
55. Adler, D., Shur, M. S., Silver, M. & Ovshinsky, S. R. Threshold switching in 
chalcogenide-glass thin films. J. Appl. Phys. 51, 3289-309 (1980). 
56. Emin, D., Seager, C. H. & Quinn, R. K. Small-polaron hopping motion in 
some chalgogenide glasses. Phys. Rev. Lett. 28, 813-16 (1972). 
57. Lai, S. Current status of the phase change memory and its future. IEDM Tech. Dig. 29.6 (2003). 
58. Lee, S. H. et al. Full Integration and Cell Characteristics for 64Mb Nonvolatile 
PRAM. Proc. Symp. VLSI Tech. Dig., 20-21 (2004). 
59. Chen, C.-F. et al. in Memory Workshop, 2009. IMW '09. IEEE International 1-2 (2009). 
 102 
60. Klein, A. et al. Changes in electronic structure and chemical bonding upon crystallization of the phase change material GeSb2Te4. Phys Rev Lett 100, 016402 (2008). 
61. Shportko, K. et al. Resonant bonding in crystalline phase-change materials. Nat. Mater. 7, 653-658 (2008). 
62. Williamson, M. J., Tromp, R. M., Vereecken, P. M., Hull, R. & Ross, F. M. Dynamic microscopy of nanoscale cluster growth at the solid-liquid interface. 
Nature Mater. 2, 532-536 (2003). 
63. Kodambaka, S., Tersoff, J., Reuter, M. C. & Ross, F. M. Germanium 
Nanowire Growth Below the Eutectic Temperature. Science 316, 729-732 
(2007). 
64. Stach, E. A. et al. Watching GaN Nanowires Grow. Nano Lett. 3, 867-869 
(2003). 
65. Wen, C. Y. et al. Formation of Compositionally Abrupt Axial Heterojunctions 
in Silicon-Germanium Nanowires. Science 326, 1247-1250 (2009). 
66. Zheng, H. et al. Observation of Single Colloidal Platinum Nanocrystal Growth 
Trajectories. Science 324, 1309-1312 (2009). 
67. Molzen, W. W., Broers, A. N., Cuomo, J. J., Harper, J. M. E. & Laibowitz, R. 
B. Materials and technique used in nanostructure fabrication. J. Vac. Sci. Technol. 16, 269-272 (1978). 
68. Enquist, F. & Spetz, A. The fabrication of amorphous SiO2 substrates suitable for transmission electron microscopy studies of ultrathin polycrystalline films. 
Thin Solid Films 145, 99-104 (1986). 
69. Morkved, T. L., Lopes, W. A., Hahm, J., Sibener, S. J. & Jaeger, H. M. Silicon nitride membrane substrates for the investigation of local structure of polymer 
thin films. Polymer 39, 3871-3875 (1998). 
70. Grant, A. W., Hu, Q.-H. & Kasemo, B. Transmission electron microscopy 
'windows' for nanofabricated structures. Nanotech. 15, 1175-1181 (2004). 
71. Gibby, A. M. A layered chalcogenide phase change memory device. Ph.D. Thesis. Stanford University (2008). 
72. Zhang, S.-C. Topological states of quantum matter. Physics 1 (2008). 73. Kane, C. L. & Mele, E. J. A New Spin on the Insulating State. Science 314, 
1692-1693 (2006). 74. Qi, X. L. & Zhang, S.-C. The quantum spin Hall effect and topological 
insulators. Physics Today, 33-38 (2010). 75. Moore, J. E. The birth of topological insulators. Nature 464, 194-198 (2010). 76. Nagaosa, N. A New State of Quantum Matter. Science 318, 758-759 (2007). 77. Kane, C. L. An insulator with a twist. Nature Phys. 4, 348-349 (2008). 78. Moore, J. An insulator's metallic side. Nature 460, 1090-1091 (2009). 
79. Manoharan, H. C. Topological insulators: A romance with many dimensions. 
Nature Nanotech. 5, 477-479 (2010). 
80. Chadov, S. et al. Tunable multifunctional topological insulators in ternary 
Heusler compounds. Nature Mater. 9, 541-545 (2010). 
 103 
81. Lin, H. et al. Half-Heusler ternary compounds as new multifunctional 
experimental platforms for topological quantum phenomena. Nature Mater. 9, 
546-549 (2010). 
82. Xia, Y. et al. Observation of a large-gap topological-insulator class with a 
single Dirac cone on the surface. Nature Phys. 5, 398-402 (2009). 
83. Wyckoff, R. W. G. Crystal Structures (Krieger, 1986). 84. Hamann, H. F., O'Boyle, M., Martin, Y. C., Rooks, M. & Wickramasinghe, K. 
Ultra-high-density phase-change storage and memory. Nature Mater. 5, 383-
387 (2006). 
85. Milliron, D. J., Raoux, S., Shelby, R. & Jordan-Sweet, J. Solution-phase 
deposition and nanopatterning of GeSbSe phase-change materials. Nature Mater. 6, 352-356 (2007). 
86. Hong, S.-H., Bae, B.-J. & Lee, H. Fast switching behavior of nanoscale 
Ag6In5Sb59Te30 based nanopillar type phase change memory. Nanotech. 21, 
025703 (2010). 
87. Lee, S. et al. Demonstration of a Reliable High Speed Phase-Change Memory 
Using Ge-Doped SbTe. Jour. Electrochem. Soc. 156, H612-H615 (2009). 
88. Lencer, D. et al. A map for phase-change materials. Nature Mater. 7, 972-977 
(2008). 
89. Hegedus, J. & Elliott, S. R. Microscopic origin of the fast crystallization ability 
of Ge-Sb-Te phase-change memory materials. Nature Mater. 7, 399-405 
(2008). 
90. Kolobov, A. V. et al. Understanding the phase-change mechanism of 
rewritable optical media. Nature Mater. 3, 703-708 (2004). 
91. Sun, Z. M., Zhou, J. & Ahuja, R. Unique melting behavior in phase-change 
materials for rewritable data storage. Phys. Rev. Lett. 98 (2007). 
92. Welnic, W. et al. Unravelling the interplay of local structure and physical properties in phase-change materials. Nature Mat. 5, 56-62 (2006). 
93. Akola, J. & Jones, R. O. Structural phase transitions on the nanoscale: The 
crucial pattern in the phase-change materials Ge2Sb2Te5 and GeTe. Phys. Rev. B 76, 235201 (2007). 
94. Sun, Z., Zhou, J. & Ahuja, R. Structure of Phase Change Materials for Data 
Storage. Phys. Rev. Lett. 96, 055507 (2006). 
95. Pirovano, A. et al. Low-Field Amorphous State Resistance and Threshold 
Voltage Drift in Chalcogenide Materials. IEEE Trans. Elect. Dev. 51, 714-719 
(2004). 
96. Ielmini, D., Lacaita, A. L. & Mantegazza, D. Recovery and Drift Dynamics of 
Resistance and Threshold Voltages in Phase-Change Memories. IEEE Trans. Elect. Dev. 54, 308-315 (2007). 
97. Song, S. A., Zhang, W., Jeong, H. S., Kim, J.-G. & Kim, Y.-J. In situ dynamic HR-TEM and EELS study on phase transitions of Ge2Sb2Te5 chalcogenides. 
Ultramicroscopy 108, 1408-1419 (2008). 
98. Yoon, S.-M. et al. Nanoscale observations of the operational failure for phase-change-type nonvolatile memory devices using Ge2Sb2Te5 chalcogenide thin 
films. App. Surf. Sci. 254, 316–320 (2007). 
 104 
99. Meister, S., Schoen, D. T., Topinka, M. A., Minor, A. M. & Cui, Y. Void 
Formation Induced Electrical Switching in Phase-Change Nanowires. Nano Lett. 8, 4562-4567 (2008). 
100. Meister, S., Kim, S., Cha, J. J., Wong, H.-S. P. & Cui, Y. In situ TEM observation of microstructural changes in phase-change memory bridges 
during electrical switching. (submitted to Nature Nanotech.) (2010). 
101. Krebs, D. et al. Characterization of phase change memory materials using 
phase change bridge devices. Jour. App. Phy. 106, 054308-7 (2009). 
102. Krebs, D. et al. Threshold field of phase change memory materials measured 
using phase change bridge devices. App. Phys. Lett. 95 (2009). 
103. Wu, Y. & Yang, P. Germanium Nanowire Growth via Simple Vapor Transport. 
Chem. of Mater. 12, 605-607 (2000). 
104. Duan, X. & Lieber, C. M. General Synthesis of Compound Semiconductor 
Nanowires. Advanced Materials 12, 298-302 (2000). 
105. Duan, X. & Lieber, C. M. Laser-Assisted Catalytic Growth of Single Crystal 
GaN Nanowires. Journ. Amer. Chem. Soc. 122, 188-189 (1999). 
106. Bjork, M. T. et al. One-dimensional heterostructures in semiconductor 
nanowhiskers. Appl. Phys. Lett. 80, 1058-1060 (2002). 
107. Kuykendall, T. et al. Crystallographic alignment of high-density gallium 
nitride nanowire arrays. Nature Mater. 3, 524-528 (2004). 
108. Prince, A., Raynor, G. V. & Evans, D. S. Phase Diagrams of Ternary Gold Alloys (ed. Metals, I. o.) (Brookfield, VT, 1990). 
109. Yamada, N., Ohno, E., Nishiuchi, K., Akahira, N. & Takao, M. Rapid-phase transitions of GeTe-Sb2Te3 pseudobinary amorphous thin films for an optical 
disk memory. Journ. Appl. Phys. 69, 2849-2856 (1991). 
110. Damodara Das, V., Soundararajan, N. & Pattabi, M. Electrical conductivity and thermoelectric power of amorphous Sb2Te3 thin films and amorphous-
crystalline transition. Journal of Materials Science 22, 3522-3528 (1987). 
111. Zhang, Z. & et al. Modelling for size-dependent and dimension-dependent 
melting of nanocrystals. J. Phys. D: Appl. Phys. 33, 2653 (2000). 
112. Jennings, A. T., Jung, Y., Engel, J. & Agarwal, R. Diameter-Controlled Synthesis of Phase-Change Germanium Telluride Nanowires via the Vapour-
Liquid-Solid Mechanism. J. Phys. Chem. C 113, 6898-6901 (2009). 
113. Gao, P. X. et al. Conversion of Zinc Oxide Nanobelts into Superlattice-
Structured Nanohelices. Science 309, 1700-1704 (2005). 
114. Tang, Y. H. et al. Morphology of Si nanowires synthesized by high-
temperature laser ablation. J. Appl. Phys. 85, 7981-7983 (1999). 
115. Zhang, H.-F., Wang, C.-M., Buck, E. C. & Wang, L.-S. Synthesis, 
Characterization, and Manipulation of Helical SiO2 Nanosprings. Nano Lett. 3, 
577-580 (2003). 
116. McIlroy, D. N., Zhang, D., Kranov, Y. & Norton, M. G. Nanosprings. Appl. Phys. Lett. 79, 1540-1542 (2001). 
117. Chen, X. et al. Mechanics of a Carbon Nanocoil. Nano Lett. 3, 1299-1304 
(2003). 
 105 
118. Bae, S. Y., Lee, J., Jung, H., Park, J. & Ahn, J.-P. Helical Structure of Single-
Crystalline ZnGa2O4 Nanowires. J. Am. Chem. Soc. 127, 10802-10803 (2005). 
119. Korgel, B. A. MATERIALS SCIENCE: Nanosprings Take Shape. Science 309, 
1683-1684 (2005). 
120. Meister, S. et al. Synthesis and Characterization of Phase-Change Nanowires. 
Nano Lett. 6, 1514-1517 (2006). 
121. Yu, B. et al. Indium selenide nanowire phase-change memory. Appl. Phys. Lett. 
91, 133119-3 (2007). 
122. Mitra, M., Jung, Y., Gianola, D. S. & Agarwal, R. Extremely low drift of resistance and threshold voltage in amorphous phase change nanowire devices. 
Appl. Phys. Lett. 96, 222111-3 (2010). 
123. Wuttig, M. & Yamada, N. Phase-change materials for rewriteable data storage. 
Nature Mater. 6, 824-832 (2007). 
124. Sedgwick, T. O., Agule, B. J. & Broers, A. N. Novel Method for Fabrication of 
Ultrafine Metal Liners by Electron-Beams. J. Electrochem. Soc. 119, 1769-& 
(1972). 
125. Yu, D., Wu, J., Gu, Q. & Park, H. Germanium telluride nanowires and 
nanohelices with memory-switching behavior. J. Amer. Chem. Soc. 128, 8148-
8149 (2006). 
126. Lee, J. S., Brittman, S., Yu, D. & Park, H. Vapor-liquid-solid. and vapor-solid growth of phase-change Sb2Te3 nanowires and Sb2Te3/GeTe nanowire 
heterostructures. J. Amer. Chem. Soc. 130, 6252-6258 (2008). 
127. Chopra, K. L. & Bahl, S. K. Amorphous versus Crystalline GeTe Films. I. 
Growth and Structural Behavior. J.  Appl. Phys. 40, 4171-4178 (1969). 
128. Mikolaichuk, A. G., Kogut, A. N. & Ignativ, M. I. Electric Properties of 
Telluride and Germanium Selenide Thin Films. Izv. Vyssh. Uchebn. Zaved., Fiz., 103-& (1970). 
129. Sun, X., Yu, B., Ng, G. & Meyyappan, M. One-Dimensional Phase-Change 
Nanostructure: Germanium Telluride Nanowire. J. Phys. Chem. C 111, 2421-
2425 (2007). 
130. Bahl, S. K. & Chopra, K. L. AMORPHOUS VERSUS CRYSTALLINE GETE 
FILMS .3. ELECTRICAL PROPERTIES AND BAND STRUCTURE. J. Appl. Phys. 41, 2196-& (1970). 
131. Stoemenos, J. & Vincent, R. Twinning Faults in Epitaxial Films of GeTe and 
GeTe-SnTe Alloys. Physica Status Solidi (a) 11, 545-558 (1972). 
132. Konig, M. Quantum spin hall insulator state in HgTe quantum wells. Science 
318, 766-770 (2007). 
133. Chen, Y. L. et al. Experimental realization of a three-dimensional topological 
insulator, Bi2Te3. Science 325, 178-181 (2009). 
134. Fu, L. & Kane, C. L. Topological insulators with inversion symmetry. Phys. Rev. B 76, 045302 (2007). 
135. Peng, H., Meister, S., Chan, C. K., Zhang, X. F. & Cui, Y. Morphology 
Control of Layer-Structured Gallium Selenide Nanowires. Nano Lett. 7, 199-
203 (2006). 
 106 
136. Kong, D. et al. Topological Insulator Nanowires and Nanoribbons. Nano Lett. 
10, 329-333 (2009). 
137. Peng, H., Schoen, D. T., Meister, S., Zhang, X. F. & Cui, Y. Synthesis and 
Phase Transformation of In2Se3 and CuInSe2 Nanowires. J. Am. Chem. Soc. 
129, 34-35 (2006). 
138. Hyde, G. R., Beale, H. A., Spain, I. L. & Woollam, J. A. Electronic properties 
of Bi2Se3 crystals. J. Phys. Chem. Solids 35, 1719-1728 (1974). 
139. Aronov, A. G. & Sharvin, Y. V. Magnetic flux effects in disordered conductors. 
Rev. Mod. Phys. 59, 755 (1987). 
140. Bachtold, A. Aharonov-Bohm oscillations in carbon nanotubes. Nature 397, 
673-675 (1999). 
141. Jung, M. et al. Quantum Interference in Radial Heterostructure Nanowires. 
Nano Lett. 8, 3189-3193 (2008). 
142. Nikolaeva, A., Gitsu, D., Konopko, L., Graf, M. J. & Huber, T. E. Quantum interference of surface states in bismuth nanowires probed by the Aharonov-
Bohm oscillatory behavior of the magnetoresistance. Phys. Rev. B 77, 075332 
(2008). 
143. Richter, T. et al. Flux Quantization Effects in InN Nanowires. Nano Lett. 8, 
2834-2838 (2008). 
144. Hikami, S., Larkin, A. I. & Nagaoka, Y. Spin-Orbit Interaction and 
Magnetoresistance in the Two Dimensional Random System. Prog. Theor. Phys. 63, 707-710 (1980). 
145. Huber, T. E., Celestine, K. & Graf, M. J. Magnetoquantum oscillations and 
confinement effects in arrays of 270-nm-diameter bismuth nanowires. Phys. Rev. B 67, 245317 (2003). 
146. Peng, H. et al. Aharonov-Bohm interference in topological insulator 
nanoribbons. Nat. Mater. 9, 225-229 (2010). 
147. Kong, D. et al. Few-Layer Nanoplates of Bi2Se3 and Bi2Te3 with Highly 
Tunable Chemical Potential. Nano Lett. 10, 2245-2250 (2010). 
148. Cha, J. J. et al. Magnetic Doping and Kondo Effect in Bi2Se3 Nanoribbons. 
Nano Lett. 10, 1076-1081.
