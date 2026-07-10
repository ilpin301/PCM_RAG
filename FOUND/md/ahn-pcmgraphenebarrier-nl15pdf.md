---
Title: "Energy-Efficient Phase-Change Memory with Graphene as a Thermal Barrier"
Author: "Chiyui Ahn; Scott W. Fong; Yongsung Kim; Seunghyun Lee; Aditya Sood; Christopher M. Neumann; Mehdi Asheghi; Kenneth E. Goodson; Eric Pop; H.-S. Philip Wong"
Reference: "https://poplab.stanford.edu/pdfs/Ahn-PCMgrapheneBarrier-nl15.pdf"
ContentType:
  - "pdf"
Created: 2026-06-17
Processed: true
tags:
  - "source"
---

https://lh3.googleusercontent.com/notebooklm/AKXwDQEJ1Nk0UMxOGi-deI-I5UOfy5MN7C7DKNGQr7ftnqBB32-7n_E5dpYWjhQffDZx__3xnoz0RAi7raJwvxymVmN1AUAzVpUDsCE5pnvPwFP85wo6JP8xZCayEvVeQPegUDhg2VdGZg=w995-h422-v0
1860b131-2d3e-4822-aea1-ebf89fc64a02
Energy-Efficient Phase-Change Memory with Graphene as a Thermal Barrier 
Chiyui Ahn,*,† Scott W. Fong,† Yongsung Kim,‡ Seunghyun Lee,† Aditya 
Sood,§,∥ 
Christopher M. Neumann,† Mehdi Asheghi,§ Kenneth E. Goodson,§ Eric Pop,† and H.-S. Philip Wong*,† 
†Department of Electrical Engineering, §Department of Mechanical Engineering, and 
∥Department 
of Materials Science and Engineering, Stanford University, Stanford, California 94305, United States ‡Samsung Advanced Institute of Technology (SAIT), Suwon, 443-803, South Korea 
*S Supporting Information 
ABSTRACT: Phase-change memory (PCM) is an important class of data storage, yet lowering the programming current of individual devices is known to be a significant challenge. Here we improve the energy-efficiency of PCM by placing a graphene layer at the interface between the phase-change material, Ge2Sb2Te5 (GST), and the bottom electrode (W) heater. Graphene-PCM (G-PCM) devices have ∼40% lower RESET current compared to control devices without the graphene. This is attributed to the graphene as an added interfacial thermal resistance which helps confine the generated heat inside the active PCM volume. The G-PCM achieves programming up to 105 cycles, and the graphene could further enhance the PCM endurance by limiting atomic migration or material segregation at the bottom electrode interface. 
KEYWORDS: Graphene, Joule heating, phase-change memory, reset current, thermal boundary resistance 
Phase-change memory (PCM)1−5 has been one of the 
leading candidates of emerging nonvolatile memories, 
mainly due to its great scalability down to the single-digit nanometer regime.6−11 PCM has superior performance compared to mainstream NAND Flash, with cycling endurance up to 109 demonstrated12,13 and faster switching speed of less than 10 ns.14 The phenomenon of resistive switching in PCM is based on the reversible phase transition of chalcogenide alloys between low-resistance crystalline and high-resistance amor-phous phases,1 caused by current-induced Joule heating. Because crystallization (for SET) and melting (for RESET) of the phase-change material occurs at relatively high temperatures (around 150 °C15 for crystallization to the fcc-phase Ge2Sb2Te5 (GST) and over 600 °C16 for GST melting), relatively high programming (RESET) currents remain a challenge for PCM. Although reduction of IRESET down to the 
μA 
range has been demonstrated using individual carbon nanotube electrodes,7,8,10,11 a more scalable approach to energy-efficient PCM is needed. For a given technology node, the strategy for reducing the 
programming current of PCM falls into two complementary categories: materials engineering and thermal engineering. Examples of materials engineering include the use of GeTe/ Sb2Te3 superlattices for interfacial17 and charge-injection18 
PCMs, as well as the use of nanocrystalline doped GST.19 
Thermal engineering aims to achieve PCM heating with minimal current by increasing the thermal resistance and thermal confinement of PCM. The early invention of the confined PCM cell structure20 was a prototypical approach of 
thermal engineering, and the use of thermally confined TaN/ TiN bottom electrode (BE) in the conventional mushroom structure21,22 has also been effective. For the PCM to be more energy-efficient, the Joule heating should be restricted inside a small volume of the phase-change material and heat loss by thermal conduction to the surroundings needs to be minimized. One approach to achieve this has been to engineer the interface between the phase-change material and the metal heater.23−25 
For example, PCM with a semiconducting fullerene film (∼30 nm C60) inserted at the interface between GST and metal bottom electrode24 has shown up to ∼70% reduction of IRESET. However, such interfacial films with a relatively large thickness (∼10 nm for TiO2, 
23 about 30 nm for C60, 24 and over 100 nm 
for WO3 25) may not be an ideal solution because they 
introduce series resistance24 and may degrade the PCM reliability.23 
In this work, we demonstrate the use of graphene as an atomically thin interfacial thermal barrier between the PCM and the heater electrode. Although graphene has a large in-plane thermal conductivity,26 the out-of-plane heat flow across'mo-nolayer and few-layer graphenes is strongly limited by its weak van der Waals interfaces.27−29 In fact, the cross-plane thermal resistance of graphene is estimated to be equivalent to that of ∼25 nm of SiO2 but with subnanometer thickness, 
26 depending 
Received: July 5, 2015 Revised: August 19, 2015 Published: August 26, 2015 
Letter 
pubs.acs.org/NanoLett 
© 2015 American Chemical Society 6809 DOI: 10.1021/acs.nanolett.5b02661 
https://lh3.googleusercontent.com/notebooklm/AKXwDQFM2mjAx7k1A9ffH7OyM775GrEIZ7bl9kLW9V8-zLqmVj1wXVAjmUDEZB1WRibFRih1RUcZ0TcbE2HJZHtiq0iCj6BnlvWWuLjkHlbr5lSGOXdU9IFgily45wCKP-GBDL7QVRB9wQ=w856-h1129-v0
37510a3e-6e70-4118-b3af-b8b9c9b14245
https://lh3.googleusercontent.com/notebooklm/AKXwDQFkoEHpKFSDs3DAY_aDWinJLndP14IS-5lJEwA8wq_CiM4IaxeJC2qc413Ivf5YrZQJTCuNgKs1pI7eglM_6PRKrZ7DDtPIHWkFh2n1tC2AoYu7J4NwiV69h5diUwgnrvkvnTJTYA=w1250-h532-v0
2298ae99-4aad-43eb-ad7b-9f23f6ed5f98
https://lh3.googleusercontent.com/notebooklm/AKXwDQE92Dma6EweunpyjOxStTS3-wYs1wbawNU--gL9yeOY_d4dnt5OUoRjuH08ybxBOW78eXATu3k6GrmQ3RdHpPyLLS79FwQNh8Dvqp-xwjqebSLzdqA9xTUOfuXa7e4soQn4wTNC=w1280-h459-v0
8bd89677-aab2-4855-8a7d-91e07da9169b
on the adjacent materials.30 Consequently, we insert a graphene layer at the interface between GST and metal (W) bottom electrode to confine heating of the PCM and form a novel graphene-PCM (G-PCM) device structure. The interfacial graphene layer is patterned by electron-beam lithography (EBL) to be as small as the effective contact area of the PCM. About 40% reduction in RESET current of the fabricated G-PCM structure is achieved with minimal increase in electrical contact resistance of the graphene, and high programming endurance is also maintained. This study demonstrates a practical electronic application of graphene as a thermal barrier for heat-sensitive devices and systems such as PCM. In order to understand the thermal effect of the graphene 
layer, we first investigated the out-of-plane thermal resistance of Al (80 nm)/GST (10 nm)/graphene/SiO2 (285 nm)/Si stacks by employing the time-domain thermoreflectance (TDTR) technique (see Figure 1a). TDTR is a well-established pump− probe technique, capable of measuring the cross-plane thermal conductivity of nanometer-thin films and thermal conductance per unit area across interfaces of particular interest27 (see Supporting Information, Section 1 and Figure S1). Compared to control test structures without the graphene in the stack, the TDTR measurement with the graphene exhibited a slower 
thermal response (Figure 1a), corresponding to an increased thermal boundary resistance (TBR). The inserted graphene layer and its interfaces added a TBR of 32 ± 10 and 44 ± 3 m2K/GW for graphene interfaces with as-deposited (amor-phous) and annealed (fcc-crystalline phase) GST films, respectively, at room temperature. These values are remarkable, demonstrating how a subnanometer thin graphene can serve as an effective thermal barrier. This cross-plane TBR of the graphene is equivalent to the thermal resistance of a much thicker layer of 10−15 nm GST, while occupying negligible volume within an overall PCM bit. Using the measured TBR values for the graphene and its 
interfaces, we also performed an electro-thermal COMSOL31 
analysis (see Figure 1b and Supporting Information Section 2) to assess how effective the graphene is as a thermal barrier in the practical PCM device structure. Temperature profiles were simulated for typical mushroom-type PCM structures, except that graphene of different sizes (of area DG 
2, where DG is the dimension of the graphene) were inserted at the interface between the GST and the metal (W) heater. We compared the impact of different dimensions of the graphene interfacial layer in Figure 1b, in terms of the normalized RESET-programming current. Because the graphene has >100× higher in-plane 
Figure 1. (a) TDTR (time-domain thermoreflectance) measurements of the ratio of the in-phase (Vin) and out-of-phase (Vout) components of the reflected probe intensity, comparing the film stacks (see Figure S1) with and without the graphene. The inserted graphene layer leads to a slower thermal decay, thus indicating that it adds a significant amount of thermal resistance in the out-of-plane direction. (b) Simulated RESET programming current of the G-PCM as a function of ratio between the graphene width and the bottom electrode width (DG/DBE). IRESET is normalized to that of the conventional PCM. Also see Figure S2. 
Figure 2. (a) Schematic representation of the G-PCM device fabricated in this work. The top electrode voltage (Vtop) is applied to the Pt/Ti top electrode, and the larger area W via, which connects the smaller e-beam patterned heat plug through the bottom electrode underneath, is electrically grounded. Two different types of PCM devices are fabricated with different graphene sizes (DG) as a comparison (inset). DG is set at 1 
μm, 
equal to DGST for the control sample, while DG varies with the effective contact diameter (DG = DBE) for the G-PCM. (b) Cross-sectional HR-TEM image of the G-PCM device in the high-resistance state (HRS) with typical resistances of a few 
MΩ’s 
and the effective contact size (the diameter of the columnar W heater plug) ∼ 100 nm. The TEM cannot resolve the subnanometer thick graphene; thus, its location is shown by an arrow at the a-GST (amorphous GST) interface with the W-plug. See Figure S5; some physical damage to the graphene is observed after the 10 nm GST film is sputtered on top. 
Nano Letters Letter 
 
https://lh3.googleusercontent.com/notebooklm/AKXwDQGIYuXDYGJ7Wc1WO2azTS-BQzoaiiYiqTJY5e6JVk4w5kvlB8KmzH7rFU9oVnYPEr4O7CfPdS17PtdcI_ovsXz179a_qleHYhrdgVjcwyTcWC4vNkD7S3XDI4l_y4mHSIrOV36NbQ=w856-h1129-v0
1f1e20c2-c48e-4fff-ab96-aa7bcc07e421
https://lh3.googleusercontent.com/notebooklm/AKXwDQFzKKGS7voNPDwlRnCVE3SmhegmpqCEp8elkCwLu_Seva5SbUeSrctdgpAFNiiGzeDd8DDbXV1Q_THVDF-b7hTSNbJR4wzrI01OFXXnvjfNMQAZG7F-G6b3FyGcDk7dpxYK0RqQtg=w733-h592-v0
c6afbdb6-2e08-4891-a8d9-86fbc2ddde29
https://lh3.googleusercontent.com/notebooklm/AKXwDQFNbnSZ2wHn-vmQvOThWRMiNQD7o1sKyyZkZwyryXNbN_gu6OkGeYNpEVr3EQ5Oy1yBrulVjagztaU9UXpkY6T-MHlyGzXzsyFZTNIIS0Xp9eXfYfdBLbZQlNy3QmmRQzpMxOJW=w634-h510-v0
fa985c95-df0d-4ec9-913e-e8d705fcff7e
thermal conductivity than out-of-plane,26 its width affects the heating efficiency of the PCM cell. When the graphene covers a larger area, the efficiency in heating up the thin GST film (10 nm) becomes lower due to heat flow along the graphene lateral direction. It is therefore necessary to limit the inserted graphene layer in the PCM into a much smaller region than that of the GST layer on top. By doing so, one can more fully utilize the benefits of the graphene as a thermal barrier in the out-of-plane direction while minimizing the heat lost along the in-plane direction. The temperature profile in Figure S2 suggests that when the graphene is patterned as small as the W heater underneath (DG 
≈ 
215 nm), the hottest region inside the active GST volume can reach as high as its melting temperature (Tmelt = 900 K in the simulation) with the lowest RESET current applied. Based on the observations made in Figure 1a and b, we 
fabricated the novel G-PCM device structure (see Figure 2a and b), where the interfacial graphene thermal barrier enables an energy-efficient PCM design, as follows (see Figure S3 for the details of device fabrication). The 30 nm W layer is first electron-beam (e-beam) evaporated to serve as the bottom electrode, followed by 30 nm of SiO2 by plasma-enhanced chemical vapor deposition (PECVD). The 100 kV EBL is then applied to pattern the nanoscale via, and the subsequent processes of dry-etching the dielectric layer and filling via holes with e-beam evaporated W are precisely calibrated such that the surface of the W plug is nearly flush with the oxide surface (<10 nm) after lift-off (see Figure S4 for the top view SEM image of the e-beam patterned vias). A graphene layer purchased from Graphene Supermarket32 is then transferred using a typical poly (methyl methacrylate) (PMMA) scaffold33 and patterned by EBL to be as small as the bottom W heater electrode, i.e., DG = DBE. The 10 nm GST is sputtered directly on top of the graphene layer (see Figure S5 for Raman data for graphene), followed by a TiN adhesion layer (10 nm), a Ti layer (10 nm), and Pt (30 nm) top electrode. As shown in the inset of Figure 2a, a control sample is separately prepared with the graphene patterned into a much larger area of DG = DGST and compared with the optimal design of the G-PCM with DG = DBE. The typical threshold switching behavior of the fabricated G-
PCM devices is presented in Figure 3 for a DC current sweep. Here G-PCM devices with DG = DBE = 100 nm are compared with control PCM devices without graphene that have various bottom electrode contact sizes (DBE). For both G-PCM and PCM, the large conductivity increase occurs at the voltage above the threshold point (VT ∼ 5.5 V), accompanied by a well-known voltage snap-back. The threshold switching is the key electrical process which enables current-induced phase change to occur in PCM devices. The fabricated G-PCM device shows similar DC threshold switching as the control PCM device of the same size (100 nm) without the graphene. One difference is that device-to-device variation of the low-resistance state (LRS) resistance (RLRS) after SET seems larger for the G-PCM device. RLRS of the G-PCM device varies from about 50 to 200 
kΩ 
for the effective contact size of 100 nm, while that of the control PCM device of the same size ranges from 40 to 50 
kΩ. 
Since the LRS resistance of the PCM is the sum of the resistances of the heater element (columnar W-plug), the phase-change material (GST), and various interfaces, the difference in the distribution of RLRS between the G-PCM and the PCM is attributed to the imperfect graphene interfaces. It is noteworthy that we successfully minimized the electrical contact resistance of graphene by (1) keeping the PMMA 
support layer fresh before graphene transfer and (2) optimizing the conditions for PMMA removal after graphene transfer, and for e-beam resist removal after graphene patterning. Addition-ally, other approaches may be implemented to further reduce contamination of the graphene surface.34−37 
Next, in order to explore the potential advantage of the G-PCM in achieving lower RESET current (IRESET), we compared the R-I (resistance vs current) switching characteristics of three different PCM devices fabricated in Figure 4: G-PCM with DG = DBE, PCM without the graphene, and control sample with DG = 1 
μm. 
We first consider the typical R-I behavior of the conventional PCM device without the graphene. Programming currents with small pulse amplitudes (<0.5 mA) lead to the 
Figure 3. SET threshold switching characteristics of fabricated PCM devices with different BE sizes of 200, 100, and 50 nm, and G-PCM devices with DG = DBE = 100 nm. Device-to-device variation in the low-resistance state (LRS) of G-PCM indicates that imperfect graphene interfaces (ostensibly arising from PMMA residues after graphene transfer and from the GST sputtering process) should be carefully treated to minimize the electrical contact resistance of graphene. 
Figure 4. RESET current reduction in the G-PCM device (with patterned graphene), compared with control samples without the graphene and with a wider graphene layer (DG = 1 
μm). 
The switching curves were obtained by applying a 10 ns/100 ns/10 ns (rise time/ duration/fall time) voltage pulse with increasing voltage amplitude to the PCM top electrode, and monitoring the waveform through the 50 
Ω 
internal resistance of the oscilloscope. All three types of PCM devices considered had the same bottom electrode size (DBE = 200 nm). About 40% decrease of IRESET in the G-PCM compared to the PCM without graphene, points to the enhanced confinement of heat by the inserted graphene layer at the interface. The G-PCM device with the smallest contact resistances (i.e., the smallest RLRS, comparable to that of the traditional PCM) was used in the pulsed switching experiment. The cycle-to-cycle distribution of IRESET for the 200 nm G-PCM is shown in Figure S7. 
Nano Letters Letter 
 
https://lh3.googleusercontent.com/notebooklm/AKXwDQElwK0p5CvPIKRTQvT0pW-b4rjzW7SqJmiMBloUljR3E66h5dl-8Go-_rUnK6mTu572_z4DEp2GhN32cFRfGtcf7UhgwZ_2dc_ybz-3GgegbInQChmdz9J5kWiA7KcpV7QaSCGxPw=w856-h1129-v0
298e4b02-3777-4da9-a026-9d0272e5cb7e
https://lh3.googleusercontent.com/notebooklm/AKXwDQFE0P1Z44djloecQiIYJUHzfMj850p1oFu4wReuOoRtxFZ_7Sj5ucdNsBA_RzWAGH9Uq5SAHZE6qfSLWrzsL-4in8ZMbLz5aU-EWRQZ6iyI1DPqFxreoAktJ2UCXR9e_Li7yQL4MA=w1280-h1074-v0
970b5a5f-b21d-429c-8521-14f991c86a58
initial annealing of the active amorphous volume of the GST and the consequent decrease in the cell resistance. As the current increases and approaches the value of IRESET, the melt-and-quench of the critical volume results in an increase of the cell resistance, and the RESET transition occurs. The measured IRESET of about 2 mA for the 200 nm control PCM without graphene is in agreement with a trend line1 of the linear relationship between the RESET current and the effective contact area of the PCM (see Supporting Information Figure S6 for the measured IRESET values as a function of the PCM bottom electrode size, for both PCM and G-PCM). It is significant that the PCM devices fabricated in this study require relatively low programming current densities (JRESET) of <7 MA/cm2 (see the inset of Figure S6). Carefully designed PCM cell structures have been programmed typically at JRESET ∼ 10 MA/cm2.1 
Compared with the control PCM without graphene, the G-PCM exhibits 40% smaller RESET programming current, IRESET ∼ 1.2 mA, although it has the same effective contact diameter, DBE 
≈ 
200 nm (see Figure S7 for the cycle-to-cycle distribution of measured IRESET). As shown by our earlier measurements and simulations (Figure 1), this occurs because the interfacial graphene layer (patterned by EBL as small as the W heater plug) limits the generated heat from being dissipated through the plug into the bottom electrode of the PCM. The critical role of the inserted graphene layer as an effective thermal barrier is also supported by the fact that IRESET of the control sample (with DG = 1 
μm, 
see Figure 2a) is similar to or a bit larger than that of the conventional PCM. If the observed IRESET reduction in the G-PCM resulted in part from added 
series resistance of the graphene and its interfaces, the control sample would also have led to a smaller IRESET than the traditional PCM, as it also had the interfacial layer of graphene. Since the larger graphene in this control sample conducts more heat in the in-plane direction than the EBL patterned graphene in the G-PCM, it heats a larger GST volume on top, canceling out the advantage in IRESET reduction. It should be noted that the G-PCM device used for the 
pulsed switching experiments in Figure 4 (and the one in Figure 5) had RLRS comparable to that of the PCM device without graphene. This is important, as the minimal electrical contact resistance due to graphene can rule out the possibility of increased Joule heating, and confirms our reasoning of graphene-assisted heat confinement as the physical source of the reduced IRESET in the G-PCM. Another key challenge in utilizing low thermal conductivity 
thin films (thermal conductivity in the range of 0.4−1.7 W m−1 
K−1 for TiO2, C60, and WO3 23−25) to engineer the interface 
between the phase-change material and the metal heater is the need to maintain the endurance of the integrated PCM device. Endurance characteristics have not been tested in many previous studies using interfacial thin films24,25 or only a limited and degraded number of switching cycles have been reported.23 The difficulty arises from the fact that the thin film inserted at the phase-change material interface with the metal heater could participate in physical interactions (atom intermixing or alloying) with the adjacent phase-change atoms, as the interface is very hot during programming. In this regard, Figure 5, which displays the endurance character-istics and the resistance distributions for both PCM (Figure 5a 
Figure 5. (a) Pulsed write/erase endurance characteristics and (b) cycle-to-cycle resistance distributions of the PCM control devices (without graphene) fabricated with varying BE sizes, DBE = 200, 100, and 50 nm. (c and d) Similar plots for the G-PCM devices with patterned graphene, DG = DBE. For electrical switching, voltage pulses of 1 
μs/100 μs/1 μs 
and 10 ns/50 ns/10 ns were applied for SET (write) and RESET (erase), respectively. Both types of devices can be switched up to 105 cycles, with an on/off resistance ratio between 30 and 100. 
Nano Letters Letter 
 
https://lh3.googleusercontent.com/notebooklm/AKXwDQEA_xAI_rsNV4VigpkSfJQhGQLG2j2FEkC0S77npYZ5eKZEwT8mc2QTpWEu8v_9f6q8POjJv4rmENzqxSgGpXJGEDIWnthVIVo-yKtS6Aj0cCf6lEJn6Bw2-nNpC81tuqHZ0y5p=w856-h1129-v0
5d72a501-c9a7-4b24-a3cc-044ca30b282e
and b) and G-PCM (Figure 5c and d) devices, is of great importance in verifying a functional G-PCM device. First, the G-PCM device shows excellent electrical performance, as compared with earlier studies using other thin films.23−25 We achieved good programming endurance of up to 105 cycles in the G-PCM, along with tight cycle-to-cycle resistance distributions and on/off resistance ratios of ∼30, ∼60, ∼100 for devices with DBE 
≈ 
50, 100, and 200 nm, respectively. Second, it is interesting to note that the G-PCM did not exhibit any degradation in the memory window. The LRS resistance did not change even after the graphene insertion, owing to the minimal electrical contact resistance of graphene. In general, the main cause to the endurance failure of PCM is 
the physical movement and segregation of phase-change atoms.38,39 Graphene-inserted PCM may lead to higher endurance as compared to conventional structures because the graphene serves as a physical barrier40,41 between the phase-change material and the metal heater, preventing atomic migration or material segregation that could occur at this interface during repeated programming cycles. However, in this work we did not observe improved endurance in devices with graphene at the interface; the endurance was limited to 105 
cycles for both PCM and G-PCM devices for unidentified reasons which will be the focus of future work. Nevertheless, our study suggests that graphene is a good candidate for an interfacial material to improve the thermal efficiency of the PCM and possibly increases the endurance of the PCM as well. As an added advantage, the inserted graphene layer gives no degradation in electrical performance of the PCM while improving the thermal efficiency. In summary, we have found that graphene is a uniquely 
suited material for interfacial thermal engineering of the PCM, as it is atomically thin and chemically inert due to strong sp2 
carbon bonds. We experimentally demonstrated that graphene-inserted PCM devices consume less programming current (using lower power), with the best results obtained when the graphene was patterned to the same width as the bottom electrode. These devices showed 40% lower RESET current compared with traditional PCM devices of the same effective contact size, while still maintaining fast switching speed of sub-50 ns (for RESET), high programming endurance of up to 105 
cycles, and good on/off resistance ratio between 30 and 100. The reduced IRESET is attributed to the thermal boundary resistance of graphene and its interfaces, leading to improved thermal efficiency of the device by restricting heating within the active programming region of the PCM. 
■ ASSOCIATED CONTENT 
*S Supporting Information The Supporting Information is available free of charge on the ACS Publications website at DOI: 10.1021/acs.nano-lett.5b02661. 
Details of the TDTR (time−domain thermoreflectance) measurements, 3D finite-element (COMSOL) simula-tion, process flow for fabricating the G-PCM (graphene-inserted PCM) device, SEM image of the electron-beam patterned W plug and via, Raman spectroscopy for graphene, measured RESET current (IRESET) as a function of the effective contact diameter of the PCM/ G-PCM, and cycle-to-cycle distributions of measured IRESET for PCM and G-PCM devices (PDF) 
■ AUTHOR INFORMATION 
Corresponding Authors *C.A. E-mail: cyahn@stanford.edu. *H.-S.P.W. E-mail: hspwong@stanford.edu. Notes The authors declare no competing financial interest. 
■ ACKNOWLEDGMENTS 
This work is supported in part by the Office of the Director of National Intelligence (ODNI), Intelligence Advanced Research Projects Activity (IARPA) Trusted Integrated Circuits (TIC) Program (Program Directors: Dennis Polla and Carl McCants), Samsung Electronics, the Samsung GRO program, the member companies of Stanford Non-Volatile Memory Technology Research Initiative (NMTRI) affiliate program, Systems on Nanoscale Information Fabrics (SONIC) Center, one of six centers of Semiconductor Technology Advanced Research Network (STARnet), a Semiconductor Research Corporation (SRC) program sponsored by Microelectronics Advanced Research Corporation (MARCO) and Defense Advanced Research Projects Agency (DARPA), and the Air Force Office of Scientific Research (AFOSR). 
■ REFERENCES 
(1) Wong, H.-S. P.; Raoux, S.; Kim, S.; Liang, J.; Reifenberg, J. P.; Rajendran, B.; Asheghi, M.; Goodson, K. E. Phase Change Memory. Proc. IEEE 2010, 98, 2201−2227. (2) Burr, G. W.; Breitwisch, M. J.; Franceschini, M.; Garetto, D.; Gopalakrishnan, K.; Jackson, B.; Kurdi, B.; Lam, C.; Lastras, L. A.; Padilla, A.; Rajendran, B.; Raoux, S.; Shenoy, R. S. Phase change memory technology. J. Vac. Sci. Technol. B 2010, 28, 223−262. (3) Jeyasingh, R.; Fong, S. W.; Lee, J.; Li, Z.; Chang, K.-W.; Mantegazza, D.; Asheghi, M.; Goodson, K. E.; Wong, H.-S. P. Ultrafast Characterization of Phase-Change Material Crystallization Properties in the Melt-Quenched Amorphous Phase. Nano Lett. 2014, 14, 3419− 3426. (4) Kang, M. J.; Park, T. J.; Kwon, Y. W.; Ahn, D. H.; Kang, Y. S.; Jeong, H.; Ahn, S. J.; Song, Y. J.; Kim, B. C.; Nam, S. W.; Kang, H. K.; Jeong, G. T.; Chung, C. H. PRAM cell technology and characterization in 20nm node size. IEEE Int. Electron Devices Meet. 2011, 3.1.1−3.1.4. (5) Choi, Y.; Song, I.; Park, M.-H.; Chung, H.; Chang, S.; Cho, B.; Kim, J.; Oh, Y.; Kwon, D.; Jung, S.; Shin, J.; Rho, Y.; Lee, C.; Kang, M. G.; Lee, J.; Kwon, Y.; Kim, S.; Kim, J.; Lee, Y.-J.; Wang, Q.; Cha, S.; Ahn, S.; Horii, H.; Lee, J.; Kim, K.; Joo, H.; Lee, K.; Lee, Y.-T.; Yoo, J.; Jeong, G. A 20nm 1.8V 8Gb PRRAM with 40 MB/s Program Bandwidth. IEEE Int. Solid-State Circuits Conference 2012, 46−48. (6) Behnam, A.; Xiong, F.; Grosse, K. L.; Cappelli, A.; Hong, S.; Wang, N.; Bae, M.-H.; Dai, Y.; Liao, A. D.; Carrion, E. A.; Ielmini, D.; Piccinini, E.; Jacoboni, C.; King, W. P.; Pop, E. Sub-10 nm Scaling of Phase-Change Memory: Thermoelectric Physics, Carbon Nanotube and Graphene Electrodes. Eur. Phase Change Ovonics Symp. 2013, S6− 05. (7) Liang, J.; Jeyasingh, R. G. D.; Chen, H.-Y.; Wong, H.-S. P. A 1.4 
μA 
Reset Current Phase Change Memory Cell with Integrated Carbon Nanotube Electrodes for Cross-Point Memory Application. VLSI Technology Symp. 2011, 100−101. (8) Liang, J.; Jeyasingh, R. G. D.; Chen, H.-Y.; Wong, H.-S. P. An Ultra-Low Reset Current Cross-Point Phase Change Memory with Carbon Nanotube Electrodes. IEEE Trans. Electron Devices 2012, 59, 1155−1163. (9) Raoux, S.; Jordan-Sweet, J. L.; Kellock, A. J. Crystallization properties of ultrathin phase change films. J. Appl. Phys. 2008, 103, 114310. (10) Xiong, F.; Bae, M.-H.; Dai, Y.; Liao, A. D.; Behnam, A.; Carrion, E. A.; Hong, S.; Ielmini, D.; Pop, E. Self-Aligned Nanotube-Nanowire Phase Change Memory. Nano Lett. 2013, 13, 464−469. 
Nano Letters Letter 
 
https://lh3.googleusercontent.com/notebooklm/AKXwDQHJHrXb-2XvaFJ55-IPp2gH52JddqYmzTYebW84BlWT475PyTHi5A3bV6UGsSR-7FFvue9m9Yruk8yxc5MN0Bq9SWptP3rU3_4twP73dp2n69SEh88IoHmSJkMadOfXwe35JqZCnQ=w856-h1129-v0
d33df015-cd1f-4c5a-9d93-7b889d9b3c81
(11) Xiong, F.; Liao, A. D.; Estrada, D.; Pop, E. Low-Power Switching of Phase-Change Materials with Carbon Nanotube Electrodes. Science 2011, 332, 568−570. (12) Chen, C.-F.; Schrott, A.; Lee, M. H.; Raoux, S.; Shih, Y. H.; Breitwisch, M.; Baumann, F. H.; Lai, E. K.; Shaw, T. M.; Flaitz, P.; Cheek, R.; Joseph, E. A.; Chen, S. H.; Rajendran, B.; Lung, H. L.; Lam, C. Endurance Improvement of Ge2Sb2Te5-Based Phase Change Memory. IEEE Int. Memory Workshop 2009, 1−2. (13) Lee, J.; Cho, S.; Ahn, D.; Kang, M.; Nam, S.; Kang, H.-K.; Chung, C. Scalable High-Performance Phase-Change Memory Employing CVD GeBiTe. IEEE Electron Device Lett. 2011, 32, 1113−1115. (14) Zhu, M.; Xia, M.; Rao, F.; Li, X.; Wu, L.; Ji, X.; Lv, S.; Song, Z.; Feng, S.; Sun, H.; Zhang, S. One order of magnitude faster phase change at reduced power in Ti-Sb-Te. Nat. Commun. 2014, 5, 4086. (15) Friedrich, I.; Weidenhof, V.; Njoroge, W.; Franz, P.; Wuttig, M. Structural transformations of Ge2Sb2Te5 films studied by electrical resistance measurements. J. Appl. Phys. 2000, 87, 4130−4134. (16) Jeong, T. H.; Kim, M. R.; Seo, H.; Kim, S. J.; Kim, S. Y. Crystallization behavior of sputter-deposited amorphous Ge2Sb2Te5 thin films. J. Appl. Phys. 1999, 86, 774−778. (17) Simpson, R. E.; Fons, P.; Kolobov, A. V.; Fukaya, T.; Krbal, M.; Yagi, T.; Tominaga, J. Interfacial phase-change memory. Nat. Nanotechnol. 2011, 6, 501−505. (18) Takaura, N.; Ohyanagi, T.; Kitamura, M.; Tai, M.; Kinoshita, M.; Akita, K.; Morikawa, T.; Kato, S.; Araidai, M.; Kamiya, K.; Yamamoto, T.; Shiraishi, K. Charge Injection Super-Lattice Phase Change Memory for Low Power and High Density Storage Device Applications. VLSI Technology Symp. 2013, T130−T131. (19) Morikawa, T.; Akita, K.; Ohyanagi, T.; Kitamura, M.; Kinoshita, M.; Tai, M.; Takaura, N. A Low Power Phase Change Memory Using Low Thermal Conductive Doped-Ge2Sb2Te5 with Nano-Crystalline Structure. IEEE Int. Electron Devices Meet. 2012, 31.4.1−31.4.4. (20) Hwang, Y. N.; Lee, S. H.; Ahn, S. J.; Lee, S. Y.; Ryoo, K. C.; Hong, H. S.; Koo, H. C.; Yeung, F.; Oh, J. H.; Kim, H. J.; Jeong, W. C.; Park, J. H.; Horii, H.; Ha, Y. H.; Yi, J. H.; Koh, G. H.; Jeong, G. T.; Jeong, H. S.; Kim, K. Writing current reduction for high-density phase-change RAM. IEEE Int. Electron Devices Meet. 2003, 37.1.1−37.1.4. (21) Wu, J. Y.; Breitwisch, M.; Kim, S.; Hsu, T. H.; Cheek, R.; Du, P. Y.; Li, J.; Lai, E. K.; Zhu, Y.; Wang, T. Y.; Cheng, H. Y.; Schrott, A.; Joseph, E. A.; Dasaka, R.; Raoux, S.; Lee, M. H.; Lung, H. L.; Lam, C. A Low Power Phase Change Memory Using Thermally Confined TaN/TiN Bottom Electrode. IEEE Int. Electron Devices Meet. 2011, 3.2.1−3.2.4. (22) Sood, A.; Eryilmaz, S. B.; Jeyasingh, R.; Cho, J.; Asheghi, M.; Wong, H.-S. P.; Goodson, K. E. Thermal characterization of nanostructured superlattices of TiN/TaN: Applications as electrodes in Phase Change Memory. IEEE Intersociety Conference on Thermal and Thermomechanical Phenomena in Electronic Systems 2014, 765−770. (23) Song, S.; Song, Z.; Peng, C.; Gao, L.; Gu, Y.; Zhang, Z.; Lv, Y.; Yao, D.; Wu, L.; Liu, B. Performance improvement of phase-change memory cell using AlSb3Te and atomic layer deposition TiO2 buffer layer. Nanoscale Res. Lett. 2013, 8, 77. (24) Kim, C.; Suh, D.-S.; Kim, K. H. P.; Kang, Y.-S.; Lee, T.-Y.; Khang, Y.; Cahill, D. G. Fullerene thermal insulation for phase change memory. Appl. Phys. Lett. 2008, 92, 013109. (25) Rao, F.; Song, Z.; Gong, Y.; Wu, L.; Feng, S.; Chen, B. Programming voltage reduction in phase change memory cells with tungsten trioxide bottom heating layer/electrode. Nanotechnology 2008, 19, 445706. (26) Pop, E.; Varshney, V.; Roy, A. K. Thermal properties of graphene: Fundamentals and applications. MRS Bull. 2012, 37, 1273− 1281. (27) Guzman, P. A. V.; Sood, A.; Mleczko, M. J.; Wang, B.; Wong, H.-S. P.; Nishi, Y.; Asheghi, M.; Goodson, K. E. Cross Plane Thermal Conductance of Graphene-Metal Interfaces. IEEE Intersociety Confer-ence on Thermal and Thermomechanical Phenomena in Electronic Systems 2014, 1385−1389. 
(28) Koh, Y. K.; Bae, M.-H.; Cahill, D. G.; Pop, E. Heat Conduction across Monolayer and Few-Layer Graphenes. Nano Lett. 2010, 10, 4363−4368. (29) Mak, K. F.; Lui, C. H.; Heinz, T. F. Measurement of the thermal conductance of the graphene/SiO2 interface. Appl. Phys. Lett. 2010, 97, 221904. (30) Ong, Z.-Y.; Fischetti, M. V.; Serov, A. Y.; Pop, E. Signatures of dynamic screening in interfacial thermal transport of graphene. Phys. Rev. B: Condens. Matter Mater. Phys. 2013, 87, 195404. (31) COMSOL Multiphysics, http://www.comsol.com/comsol-multiphysics/. (32) Graphene Supermarket, https://graphene-supermarket.com/. (33) Lee, S.; Lee, K.; Liu, C. H.; Zhong, Z. Homogeneous bilayer graphene film based flexible transparent conductor. Nanoscale 2012, 4, 639−644. (34) Goossens, A. M.; Calado, V. E.; Barreiro, A.; Watanabe, K.; Taniguchi, T.; Vandersypen, L. M. K. Mechanical cleaning of graphene. Appl. Phys. Lett. 2012, 100, 073110. (35) Cheng, Z.; Zhou, Q.; Wang, C.; Li, Q.; Wang, C.; Fang, Y. Toward Intrinsic Graphene Surfaces: A Systematic Study on Thermal Annealing and Wet-Chemical Treatment of SiO2-Supported Graphene Devices. Nano Lett. 2011, 11, 767−771. (36) Lim, Y.-D.; Lee, D.-Y.; Shen, T.-Z.; Ra, C.-H.; Choi, J.-Y.; Yoo, W. J. Si-Compatible Cleaning Process for Graphene Using Low-Density Inductively Coupled Plasma. ACS Nano 2012, 6, 4410−4417. (37) Wood, J. D.; Doidge, G. P.; Carrion, E. A.; Koepke, J. C.; Kaitz, J. A.; Datye, I.; Behnam, A.; Hewaparakrama, J.; Aruin, B.; Chen, Y.; Dong, H.; Haasch, R. T.; Lyding, J. W.; Pop, E. Annealing free, clean graphene transfer using alternative polymer scaffolds. Nanotechnology 2015, 26, 055302. (38) Park, J.-B.; Park, G.-S.; Baik, H.-S.; Lee, J.-H.; Jeong, H.; Kim, K. Phase-Change Behavior of Stoichiometric Ge2Sb2Te5 in Phase-Change Random Access Memory. J. Electrochem. Soc. 2007, 154, H139−H141. (39) Nam, S.-W.; Lee, D.; Kwon, M.-H.; Kang, D.; Kim, C.; Lee, T.-Y.; Heo, S.; Park, Y.-W.; Lim, K.; Lee, H.-S.; Wi, J.-S.; Yi, K.-W.; Khang, Y.; Kim, K.-B. Electric-field-induced mass movement of Ge2Sb2Te5 in bottleneck geometry line structures. Electrochem. Solid-State Lett. 2009, 12, H155−H159. (40) Chen, S.; Brown, L.; Levendorf, M.; Cai, W.; Ju, S.-Y.; Edgeworth, J.; Li, X.; Magnuson, C. W.; Velamakanni, A.; Piner, R. D.; Kang, J.; Park, J.; Ruoff, R. S. Oxidation Resistance of Graphene-Coated Cu and Cu/Ni Alloy. ACS Nano 2011, 5, 1321−1327. (41) Bunch, J. S.; Verbridge, S. S.; Alden, J. S.; van der Zande, A. M.; Parpia, J. M.; Craighead, H. G.; McEuen, P. L. Impermeable Atomic Membranes from Graphene Sheets. Nano Lett. 2008, 8, 2458−2462. 
Nano Letters Letter 
 
https://lh3.googleusercontent.com/notebooklm/AKXwDQEsvbbCa8_15oR9ZjruOEcEpFbmFeXJo2FTgRywRHKaFI0g9O3-VCJhKRAzg6CtHZfNhZvv6jRi3278oFVwgYYaNcBOAFug_lK-BK8ayOr-UvTCTPoodmiB6qzQsAPW6F852ugN=w856-h1129-v0
adc0c1a0-71a1-4c49-aea2-49a01058bd8a
1  
SUPPORTING INFORMATION FOR 
Energy-Efficient Phase-Change Memory with Graphene as a Thermal 
Barrier 
 
Chiyui Ahn 1 , Scott W. Fong 
1 , Yongsung Kim 
2 , Seunghyun Lee 
1 , Aditya Sood 
3,4 , Christopher M. 
Neumann, 1  Mehdi Asheghi 
3 , Kenneth E. Goodson 
3 , Eric Pop 
1 , and H.-S. Philip Wong 
1  
1 Department of Electrical Engineering, Stanford University, Stanford, CA 94305, U.S.A. 
2 Samsung Advanced Institute of Technology (SAIT), Samsung Electronics, Suwon, 443-803, South 
Korea  
3 Department of Mechanical Engineering, Stanford University, Stanford, CA 94305, U.S.A. 
4 Department of Materials Science and Engineering, Stanford University, Stanford, CA 94305, U.S.A. 
 
Corresponding authors: Chiyui Ahn, email: cyahn@stanford.edu; H.-S. Philip Wong, email: 
hspwong@stanford.edu  
 
1. Details of the TDTR (time-domain thermoreflectance) measurements 
We performed TDTR measurements [1]-[2] on the stack of Al (80 nm)/GST (10 nm)/graphene/SiO2 (285 
nm)/Si structures (Figure S1) to assess the impact of the graphene inserted at the interface between GST 
and SiO2. Our TDTR setup is built around a 9 ps mode-locked Nd:YVO4 laser source which emits pulses 
at 1064 nm wavelength with a repetition rate of 82 MHz. The pump beam is amplitude modulated at a 
frequency fmod = 4 MHz, and converted to 532 nm with a periodically poled lithium niobate crystal. The 
Al capping layer of the test structure acts as an optothermal transducer, converting pump optical pulses 
into heat that travels through the film of interest. The thermal decay profile due to this downward 
diffusion of heat is measured by monitoring the reflectivity of the top Al layer using time-delayed probe 
pulses (0 to 3.5 ns).  
We measure the in-phase (Vin) and out-of-phase (Vout) components of the reflected probe intensity 
demodulated at fmod using a lock-in amplifier. In these experiments, the pump and probe beams are 
focused onto the sample with 1/e 2 
 spot diameters of 10 μm and 6 μm, respectively. We fit the time-series 
of -Vin/Vout data (Figure 1a) to a three-dimensional (3D) thermal model that numerically solves the heat 
conduction equation taking into account effects due to pulse accumulation and radial spreading [3]-[4].  
We perform measurements on samples with and without the graphene inserted at the GST/SiO2 interface. 
Using data from control samples without the graphene, we extract the thermal conductivities of the GST 
film in the as-deposited amorphous and fcc annealed (at 160 ºC for 1 hour) crystalline states. These values 
are ka = 0.21 ± 0.02 and kc = 0.33 ± 0.03 (Wm -1 
K -1 
) for the amorphous and fcc crystalline GST, 
respectively, in reasonable agreement with reported values from literature [5]-[6].  
The known thermal parameters at room temperature are assumed in the fitting as follows. 
2  
 Thermal conductivity of Al: 110 (Wm -1 
K -1 
) 
 Thermal conductivity of SiO2: 1.38 (Wm -1 
K -1 
) 
 Specific heat of GST: 1.2 × 10 6  (Jm 
-3 K 
-1 ) [7] 
Having measured the thermal conductivities of the GST films, we then extract the thermal boundary 
resistance (TBR) at the GST/graphene/SiO2 interface by measuring the samples with the inserted 
graphene; the TBR is found to be 32 ± 10 and 44 ± 3 (m 2 K/GW) for graphene interfaces with as-deposited 
(amorphous) and annealed (fcc crystalline) GST films, respectively, at room temperature. These values 
indicate the increase in overall TBR introduced by the graphene (i.e., the two different interfaces of 
GST/graphene and graphene/SiO2 are not distinguishable). TBR for the initial GST/SiO2 interface 
measured for fcc-phase GST in our previous work [8] is 24 ± 10 (m 2 K/GW), and thus inserting the 
graphene (doubling the number of interfaces) increases the effective TBR to be more than doubled.   
 
Figure S1. Films stacks for TDTR measurements. GST and aluminum (Al) were DC-sputtered and 
evaporated using a shadow mask, respectively. 
 
2. 3D finite-element (COMSOL) simulation 
The thermal and electrical physics of the phase-change memory (PCM) devices are modeled with three-
dimensional (3D) finite-element simulations, to generate temperature profiles inside the mushroom-type 
PCM structure. The out-of-plane electrical resistivities of graphene interfaces are set such that the 
graphene-inserted PCM (G-PCM) is calibrated to the experimental value of RLRS (resistance in low-
resistance state). A constant current is driven as a simulation input to the top electrode, and the Joule-
heating is used to determine the heat generation throughout the structure. The heat flow is modeled using 
Fourier's law, with thermal conductivities of relevant materials as listed in the following (in Wm -1 
K -1 
). 
 SiO2: 1.38, W: 50, TiN: 10, Pt: 30, GST (amorphous): 0.2, GST (crystalline): 0.4 
 Graphene: 1000 (in-plane) 
It should be noted that for a 30 nm e-beam evaporated Pt film, the thermal conductivity of 30 Wm -1 
K -1 
 is 
used in the simulation, instead of the value for a bulk Pt [9].  
Additionally, the TBRs are added for graphene interfaces, using the data obtained from the TDTR 
measurements described above. The simulation taking the effect of increased TBRs by graphene 
interfaces into account (Figure 1b) predicts almost exactly what we have measured (~40% reduction in 
IRESET).  
Al (80 nm) GST (10 nm) SiO2 (285 nm) 
Si Substrate 
Probe Laser Detector 
graphene 
Pump Laser
https://lh3.googleusercontent.com/notebooklm/AKXwDQE-57IeWK8JV1lWFOy8eYK5RM68VuqRo2RAXELbLGFByuum10bpicP3ckTkc87bLBok03q-PWy6m1o3V1f09cIsxzaJzB6ZxM5udXEtnMxy4zkkOAr18EJ-qExqeMT6pze_YuO2TA=w641-h471-v0
86dd2fa3-f925-4613-b2d8-b23165230dce
https://lh3.googleusercontent.com/notebooklm/AKXwDQFVzs3CQhNzO34CX0pAUZ4z7buCuj8nFCc6WDt7SrTD-wB62O0Lx1mfKntocH2Bka4CKiX5DT9a_xBWIYTMxCFUAoMJnzH3R4XFWLkWzcx_BnBWuGqqBr6lE4_vAh_KsZW5NXZtpA=w227-h86-v0
cc44bae0-3de9-4075-9929-751de0d73cbe
https://lh3.googleusercontent.com/notebooklm/AKXwDQH5SeOaZ7ujBc4l_AAjkSKDxPlfvmFsZbNPEcvm67rMD33DVWMdXFNAWbwg4Hy7ToaJxzR5FB47ViMuNFDLbRocFpISXLPlgNa6f4m2IvToqeQSs7kvhOceGWTWa0QxD_yyP294UA=w47-h65-v0
6e913c98-6019-4f43-a77c-eecc6f47e01c
https://lh3.googleusercontent.com/notebooklm/AKXwDQE42lynsAvnxPJ4KtbjeLuCjZnkxCxGe7FiRWRRmDWqO0jELYh1A0ZvUfbD1ZhW4RmfSKU1G-1ou9-_-fGdVOiUpVd_tp1snVhtAkmVzB-SNwOc0DyDTTX43JBu2CfwzWyctHlAVg=w80-h77-v0
d502c447-be0f-4b02-ac5b-a60b7985ed33
https://lh3.googleusercontent.com/notebooklm/AKXwDQHy8HpK2BodzrRX93TOaw_uGpKdIowqovHdJidl7QFdeTYLqboXfgTcDRduz5WgxOeDVjcxfJOOp8vfWQZVdPQut5o04YLRU6sW13gFQ2TpQbkZrnB5k3rc-zN2k4OYKPSVnFJJxA=w80-h77-v0
49c860f8-e73d-41e2-94dc-d5f4a909509d
https://lh3.googleusercontent.com/notebooklm/AKXwDQHMbv_U2VTbeOx-hiPtlm727G3n2pUVWZkQ4I6_gwmasA4ImYFpwQ3PeSCwzHbF45jD9rE03rjVMi6vAzmkpiN1t7Jp7M5MzB0IwN6iwD_YNcmC20hsEDVA3y2D4eletKUTevdNvA=w80-h77-v0
dfb23b03-ce14-491e-9b36-64528001bfbb
https://lh3.googleusercontent.com/notebooklm/AKXwDQF3JMcbKg4fHnKjQa7DOKkkuo_n4PHGd4BW1U0FdH2sIWS-ETv6T-3gXCuLWN7rX5YfmHWAFQk3jqv1newjRYatbGusH6WSLfA8NJZ8kChinfptGaTUzNU2ETWCxbEwpllWhsXOOw=w77-h80-v0
31a1a3d9-1711-409f-892d-ac396d1e6bc0
https://lh3.googleusercontent.com/notebooklm/AKXwDQHjxcRwpJmUCLz1RDYuh1iwYp1JpWhoyL4eDXFG60kmS5bB6P9-mg5Tijq7g12JT6vfBd46zj-ymBdufortsO1z_201KNRfFglQ0JVNjqz79c_CI6HSWCIMUPgPS8A_Ww13kqRqXg=w77-h80-v0
d5d68052-5eb2-47cb-b9c4-b8ba11dd91be
https://lh3.googleusercontent.com/notebooklm/AKXwDQEMz8RxVAYV9ZL046U3W2YY2YRFGDTw7JSoPUTRiMTGQsfV2sBrRfhuwyUBwE8NL8XhpJRZwQSNDW_niqyzn_LyFA9ZzxEOD9ZIqrhRaw2qQO-ffXg51_7HG4EkZkxTCnR3xCV-zA=w77-h80-v0
fa9113da-6031-47a4-b848-a3a63ea32976
https://lh3.googleusercontent.com/notebooklm/AKXwDQHhz2gn6C_GwJig7iaAEwTviyuev4wZfgGnFI2kdadmDhk8Lc6lE2fcRDABgx4HmrSuO7K9YCtTTSeVCgrDhNRwdDaC7HqauZLUm_XSCW7BYYvyULmJmNmypD1RzGj04uoqPS4NnQ=w221-h104-v0
f29a7af6-74e3-483b-9da1-e55bc4237c08
https://lh3.googleusercontent.com/notebooklm/AKXwDQHcwawBDWE3vcE9p-KNTiUik7E4xbmP3pb5EvPrMhExc6S0q-MORyACqI4xWFWkGecU2D3WQZaJq-ueSkj4OYbmB1XpE09IIGb2zNIRgtFIp6FlxuobyqBlFQe-5fzfAlwy3f0v=w221-h104-v0
46c12de9-78fd-4581-a575-b0f2f016f921
https://lh3.googleusercontent.com/notebooklm/AKXwDQGtGWZMvARYsnJhrLOLASx7ZwuCBED_W3PvRQUnkd-wr4yhsdLqDsDRdU8MbtxbJWbxYDqF-9b0wC4kPpp-wGlrYfAYsvb7Ous4qbdNRIeYn7ls8QGWmn1u0_1gprJO5VH3YqySFg=w77-h80-v0
763aebf0-79bb-4d25-91d5-b71e199c9291
https://lh3.googleusercontent.com/notebooklm/AKXwDQEFuDZtLh83bqOhwtVnLSXiUlAyhBhzEiXO47nbNghkr-GEjIAwoPcN8rkAyIWnm3qfJziTO2xlITlR7T71ZMjiCwRRLTH7UFdx2niOgkocyRG8Bw94cvjWTmKhVSdEKZaDyv1ZeA=w221-h104-v0
9a61488e-c96e-4306-a540-4ff3125bc076
https://lh3.googleusercontent.com/notebooklm/AKXwDQEi8FfKdHanfCNeeBVxYXMmx-GdSW8tYdKtruOSN9FTiq7jb8zsMM_ACWQJBPKgI2oENorabgUEg2mYQMBCEVW2UIDEwa2R_ltJ85k8ZaYERBy7JxKaSFsKEKw_Ao9-kcIXPGtoIA=w221-h104-v0
3fdf06f4-f608-4968-8aaf-770e35691a2e
https://lh3.googleusercontent.com/notebooklm/AKXwDQG7JR_xk3kku3hjW9lE3NPUku3uyWhQczyRZklycbEyRDJP8DMcnB_8XuaVXgT8ZGAOcm6qpLYgMmXDJPPda64qwPFGZ2zoMfnLnwYE8cDendIMvh8F6KJ6u79xv84opLfow3ei=w80-h77-v0
fff6a7f6-6a5a-45e3-90f5-24ac1dd25d34
3  
 
Figure S2. Temperature profile of the G-PCM where the graphene (DG ~ DB.E.) is placed at the interface 
between the GST and the W heater plug. As heat is confined and isolated by the thermally resistive 
graphene layer at the interface, the maximum temperature of GST as high as its melting temperature (Tmelt, 
~ 900 K) is achieved with minimal RESET current applied.  
 
3. Process flow for fabricating the G-PCM device 
 
Figure S3. (a) First, a 30 nm-thick SiO2 layer is grown by the PE-CVD technique at 300 ºC on top of the 
e-beam evaporated W substrate. The 30 nm W underneath serves as a bottom electrode (B.E.) that 
connects the W heater plug in the active device region to the larger-area W via. (b) The 100 kV e-beam 
lithography (EBL, JEOL 6300 FS) patterns the sub-200 nm via holes, by using the ZEP 520A positive e-
beam resist. The subsequent dry-etching of the SiO2 is made by an ICP (inductively coupled plasma) etch 
system in CHF3 and Ar atmosphere. The ZEP e-beam resist is removed by lift-off, after the e-beam 
(K)900 
300 
600 
750 
450 
Temperature profile of G-PCM 
Pt/TiTiN GST graphene 
SiO2 SiO2W plug 
SiO2/Si 
W 
*graphene is as small as W plug (DG = 215 nm, Dplug (B.E.) = 200 nm) 
30 nm 
Control sample 
G-PCM 
SiO2/Si W (30 nm) 
PE-CVD SiO2 (30 nm)(a) 
Pt/Ti 
SiO2 (30 nm)/W (30 nm) 
SiO2/Si 
(e) 
Pt/Ti 
TiN/GST 
SiO2 (30 nm)/W (30 nm) 
SiO2/Si 
(e) 
graphene (by EBL) 
SiO2 (30 nm)/W (30 nm) 
SiO2/Si 
(d) 
SiO2 (30 nm)/W (30 nm) 
graphene 
SiO2/Si 
(c) 
W via 
SiO2 (30 nm)/W (30 nm) 
SiO2/Si 
(b) 
SiO2 (30 nm)/W (30 nm) 
TiN/GST 
SiO2/Si 
(d)
https://lh3.googleusercontent.com/notebooklm/AKXwDQE-u29CtyOuXz7Gdp9sI14-KxUXVQ5RI2-2NEurZlYyNTViK_uS_0m8UE2XodI0piVdCKQnaZHssZOQZlUnKSXRn73HpGAllYS64rdNhZrCUc-uY2aV69ZeeLmnFKQNDVC2NmC8=w798-h686-v0
23875591-32eb-4acb-a1f4-d2c59d543185
4  
evaporated W fills up the nano-sized via hole. The process of filling the via with e-beam evaporated W 
metal is precisely calibrated such that the surface of the metal plug is nearly flush with the oxide surface 
(< 10 nm gap) after lift-off. (c) 1 × 1 inch pieces of single-layer (3 Å) graphene film (purchased from 
Graphene Supermarket [10]) are then transferred onto the substrate. (d) For the control sample, a stack of 
TiN (10 nm) / GST (10 nm) films is in-situ deposited in an ultra-high vacuum (UHV, base pressure of < 
10 -8 
 Torr) sputtering chamber, and it is patterned to be about 1 µm 2  by either dry-etching or lift-off 
techniques. (e) The O2 plasma etches out the graphene outside the active region. The top electrode is 10 
nm Ti (above the TiN), followed by 30 nm Pt on top. For the G-PCM sample, as shown in (d) and (e) 
highlighted in red, the transferred graphene layer is directly patterned by the EBL using the ma-N 2403 
negative tone e-beam resist. To keep the graphene surface relatively clean after the e-beam resist removal, 
we deposit GST followed by TiN capping by in-situ sputtering, then the Ti and finally Pt layers for the 
top electrode by e-beam evaporation. 
Graphene transfer process 
One side of the graphene sample (on a copper substrate) is first spin-coated with a PMMA solution 
(molecular weight of 950k g/mol and 2% by volume dissolved in Anisole) and carefully cured at 120 ºC 
for 60 secs. The coated PMMA layer serves as a physical support. The graphene on the back side is 
removed by O2 plasma for 30 secs at 50 W (otherwise, the backside graphene will hinder the Cu etch 
process). The copper substrate under the graphene film is then etched out in an Iron (III) Nitrate (Sigma 
Aldrich) solution (0.05 g/ml). The sample is left in the solution for at least 12 hours to completely 
dissolve away the copper layer. The transfer process onto the device is finally done in deionized water, 
and the PMMA layer on top of the graphene is removed with heated Acetone (soaking for about 2 hours). 
It is important to keep the PMMA layer fresh for complete removal of PMMA residue and consequently 
minimizing the electrical contact resistance of graphene.     
 
4. SEM image of the e-beam patterned W plug and via 
 
Figure S4. Scanning electron microscope (SEM) top-view image of the e-beam patterned W plug and via. 
The two small features at the top indicate the nano-sized via holes (ranging from 200 nm down to 50 nm), 
which are filled up with the e-beam evaporated W to act as a heater plug in the PCM cell. The larger W 
via at the bottom is directly connected to the bottom electrode underneath, which is grounded for 
electrical measurements. Image is taken at 5 kV acceleration voltage in the FEI Nova NanoSEM 450. 
https://lh3.googleusercontent.com/notebooklm/AKXwDQE0CaAFom0M6GyvM9r6OGuUgsIYX_0Xtgo3gcRWKNnsUlZgguWNHdgavAV0rHacu87VqF82xIJvRtb0ZKEAm-FzijIk29yXMKroH-f0UiLctcP0BydeQyDgJC1bJQ23tJiwff4e1w=w944-h796-v0
d19e2365-cf13-4518-8532-3bd25681cc24
https://lh3.googleusercontent.com/notebooklm/AKXwDQH1CdPjSxQ7LHXkt4oIYoQJXrXcg9T6L82LHJVMCh1EXCp173-qjjvpwzCN6Agf4lvveCHARJ-mhzextWQGWgRMymFyPOhoga8LsUrAmGpeZxOIVCaGnRQa69Rf12Oy7Xqc9FgGxw=w565-h432-v0
952e84ba-dc23-4d40-91eb-aa4f18097b3c
5  
5. Raman spectroscopy data 
 
 
Figure S5. Raman spectroscopy of graphene for (a) before and (b) after the 10 nm GST is sputtered on 
top. The technique of Raman spectroscopy is a well-established characterization tool used to analyze a 
variety of carbon materials including graphene [11]. The graphene samples (both without and with the 
GST) were measured using a WiTec 500 AFM/micro-Raman Scanning Microscope (with wavelength of 
532 nm). In (a), the ratio of 2D to G peak intensities is about 1.2, suggesting a good coverage of the 
graphene and possibility that our sample is a mix of monolayer and bilayer, and the low D to G ratio 
further indicates that the graphene film used in this study had a low defect level. In (b), the increased D to 
G peak ratio suggests some physical damage to the graphene after the 10 nm GST film is sputtered on top. 
However, the stack of GST/graphene/SiO2 maintains the G and 2D band character of graphene. 
 
6. Reset current trend 
 
Figure S6. Measured RESET current (IRESET) as a function of the effective contact diameter of the PCM, 
shown together with the (dashed) trend line from ITRS 2009 [12] and literature [13]. Our measured data 
points (symbols) follow the general trend line with reasonable agreement, for both traditional PCM (solid 
https://lh3.googleusercontent.com/notebooklm/AKXwDQE-3nc6extM55QIvs0W00crdOraxSVraLWrlORlF2gzCM2-ONWUUn2CKU9Vj5TWKXON3nV51JDwsHoZj1GTgmL0ornMB-AGtj7DcPLrh_pVi5MA3pB1DEjbKlqUgaC5A435-PsQ=w561-h436-v0
0c5aa1fa-77c2-41d9-9bec-38b12f059cca
6  
black square) and G-PCM (hollow red star) devices. The G-PCM gives a benefit of about 40% reduction 
in RESET programming current and energy. The inset shows that G-PCM devices in this study can be 
programmed at relatively low current densities of < 5 MA/cm 2 .   
 
7. Cycle-to-cycle distributions of measured RESET current 
 
Figure S7. Cycle-to-cycle distributions of measured IRESET for PCM devices of varying sizes and the G-
PCM with 200 nm contact width. The fabricated G-PCM device shows a clear reduction in RESET 
current, compared with the PCM of the same size; IRESET for the 200 nm G-PCM is 1.45 ± 0.18 mA, with 
a distribution that does not overlap much with that for the conventional 200 nm PCM device. 
 
References 
[1] Guzman, P. A. V.; Sood, A.; Mleczko, M. J.; Wang, B.; Wong, H.-S. P.; Nishi, Y.; Asheghi, M.; 
Goodson, K. E. Cross Plane Thermal Conductance of Graphene-Metal Interfaces. IEEE Intersociety 
Conference on Thermal and Thermomechanical Phenomena in Electronic Systems 2014, 1385-1389. 
[2] Sood, A.; Rowlette, J. A.; Caneau, C. G.; Bozorg-Grayeli, E.; Asheghi, M.; Goodson, K. E. Thermal 
conduction in lattice-matched superlattices of InGaAs/InAlAs. Appl. Phys. Lett. 2014, 105, 051909. 
[3] Feldman, A. Algorithm for solutions of the thermal diffusion equation in a stratified medium with a 
modulated heating source. High Temp. Press. 1999, 31, 293-298. 
[4] Cahill, D. G. Analysis of heat flow in layered structures for time-domain thermoreflectance. Rev. Sci. 
Instrum. 2004, 75, 5119-5122. 
[5] Lyeo, H.-K.; Cahill, D. G.; Lee, B.-S.; Abelson, J. R.; Kwon, M.-H.; Kim, K.-B.; Bishop, S. G.; 
Cheong, B.-K. Thermal conductivity of phase-change material Ge2Sb2Te5. Appl. Phys. Lett. 2006, 89, 
151904. 
[6] Giraud, V.; Cluzel, J.; Sousa, V.; Jacquot, A.; Dauscher, A.; Lenoir, B.; Scherrer, H.; Romer, S. 
Thermal characterization and analysis of phase change random access memory. J. Appl. Phys. 2005, 98, 
013520. 
[7] Bozorg-Grayeli, E.; Reifenberg, J. P.; Asheghi, M.; Wong, H.-S. P.; Goodson, K. E. Thermal 
Transport in Phase Change Memory Materials. Annual Review of Heat Transfer 2013, 16, 397-428.  
7  
[8] Lee, J.; Bozorg-Grayeli, E.; Kim, S.; Asheghi, M.; Wong, H.-S. P.; Goodson, K. E. Phonon and 
electron transport through Ge2Sb2Te5 films and interfaces bounded by metals. Appl. Phys. Lett. 2013, 102, 
191911. 
[9] Zhang, X.; Xie, H.; Fujii, M.; Ago, H.; Takahashi, K.; Ikuta, T.; Abe, H.; Shimizu, T. Thermal and 
electrical conductivity of a suspended platinum nanofilm. Appl. Phys. Lett. 2005, 86, 171912. 
[10] Graphene Supermarket, https://graphene-supermarket.com/. 
[11] Ferrari, A. C.; Meyer, J. C.; Scardaci, V.; Casiraghi, C.; Lazzeri, M.; Mauri, F.; Piscanec, S.; Jiang, 
D.; Novoselov, K. S.; Roth, S.; Geim, A. K. Raman Spectrum of Graphene and Graphene Layers. Phys. 
Rev. Lett. 2006, 97, 187401. 
[12] International Technology Roadmap for Semiconductors (ITRS), 2009. [Online]. Available: 
http://public.itrs/net/. 
[13] Wong, H.-S. P.; Raoux S.; Kim, S.; Liang, J.; Reifenberg, J. P.; Rajendran, B.; Asheghi, M.; 
Goodson, K. E. Phase Change Memory. Proc. IEEE 2010, 98, 2201-2227.
