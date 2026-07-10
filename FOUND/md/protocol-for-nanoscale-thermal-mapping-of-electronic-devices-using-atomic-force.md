---
Title: "Protocol for nanoscale thermal mapping of electronic devices using atomic force microscopy with phase change material"
Author: "Qilong Cheng; Sukumar Rajauria; Erhard Schreck; Robert Smith; Na Wang; Jim Reiner; Qing Dai; David Bogy"
Reference: "https://pmc.ncbi.nlm.nih.gov/articles/PMC11068603/"
ContentType:
  - "markdown"
Created: 2026-06-17
Processed: true
tags:
  - "source"
---

_Recovered full text. Original (blocked): https://pmc.ncbi.nlm.nih.gov/articles/PMC11068603/_

## Summary

In this protocol, we present a facile nanoscale thermal mapping technique for electronic devices by use of atomic force microscopy and a phase change material Ge2Sb2Te5. We describe steps for Ge2Sb2Te5 thin film coating, Ge2Sb2Te5 temperature calibration, thermal mapping by varying heater power, and thermal mapping by varying heating time. The protocol can be applied for resolving surface temperatures of various operational microelectronic devices with a nanoscale precision.

For complete details on the use and execution of this protocol, please refer to Cheng et al.1

## Before you begin

Precisely mapping the temperature field is essential for fundamental understanding of thermal dissipation in electronic devices,2,3 contributing to the development of more efficient and powerful technologies. Current thermometry techniques4,5,6 usually suffer from extensive calibration, perturbation of the actual device temperature, low throughput, and the use of ultra-high vacuum. Here, we provide a detailed protocol using a phase change material Ge2Sb2Te5 for nanoscale thermal mapping in electronic devices. It can be used to characterize surface temperatures with negligible temperature interference due to the deposited measurement film. The protocol requires minimal effort in temperature calibration and the temperature contour can be precisely mapped using atomic force microscopy (AFM) at the nanoscale. We use a recording head from a commercial hard disk drive as the device for demonstration, and its temperature field can be resolved by varying either the heater power or the heating time.

This protocol consists of four steps: Ge2Sb2Te5 thin film coating, Ge2Sb2Te5 temperature calibration, thermal mapping vs. heater power, and thermal mapping vs. heating time.

## Key resources table

REAGENT or RESOURCESOURCEIDENTIFIERChemicals, peptides, and recombinant proteinsSilicon waferUniversity Wafer478PhotoresistKayaku Advanced Materials, Inc.SU-8 2000Software and algorithmsNanoScope AnalysisBrukerhttp://nanoscaleworld.bruker-axs.com/nanoscaleworld/PythonPython Software Foundationhttps://www.python.org/RRID:SCR_008394MATLAB 2018bMathWorkshttps://www.mathworks.com/products/matlab.html RRID:SCR_001622OtherMagnetic recording headWestern Digital Corporation-Ge2Sb2Te5 sputtering targetACI Alloys, Inc.Ge2Sb2Te5 99.9%Sputtering systemDenton Vacuum, LLCDesktop Pro Sputter ToolAtomic force microscopeBrukerDimension IconSource measure unitKeithley Instruments, LLC2602Hot plateVWR International12365-382ThermocouplesOMEGA Engineering, Inc.5TC-TT-K-30-72Copper chamberCustom-made-

## Step-by-step method details

### Ge2Sb2Te5 thin film coating

Timing: ∼1 h 1.Prepare a photolithography defined feature on a silicon wafer (Figure 1A).Figure 1Silicon wafer and device for Ge2Sb2Te5 coating(A) Photomask on silicon wafer.(B) Ge2Sb2Te5 thin film on silicon wafer. Scale bar is 20 μm.(C) Recording head from hard disk drive. Scale bar is 1 cm. Note: Besides SU-8, most common accessible negative photoresists satisfy this requirement. The photoresist thickness over tens of nanometers is enough as the sputtered Ge2Sb2Te5 is only ∼20 nm. Note: The feature should be around tens of micrometers. 2.Mount electronic devices and photolithography-defined silicon wafer on a flat substrate such as another large silicon wafer. Note: Ensure that the surface of interest is level horizontally. Note: We use a recording head as the device (Figure 1C). There is an embedded nano-heater, also known as embedded contact sensor. 3.Sputter ∼20 nm Ge2Sb2Te5 thin film on the electronic devices and the pretreated silicon wafer, and lift off the photoresist on the silicon wafer, leaving behind bare Ge2Sb2Te5 thin film (Figure 1B). The sputtering condition is at high vacuum (∼10−6 torr) with a deposition rate ∼5 nm/min. CRITICAL: The Ge2Sb2Te5 should show a sharp edge for accurate thickness measurement.

### Ge2Sb2Te5 temperature calibration

Timing: ∼2 h

The amorphous Ge2Sb2Te5 is a chalcogenide phase change material that crystallizes at 140°C–170°C, accompanied by an increase in density and volume reduction.7 The specific glass transition temperature Tg depends on the material composition and the heating rate.8,9 In this step, the Tg of the sputtered Ge2Sb2Te5 is determined. Multiple measurements should be performed to guarantee the accuracy and stability.4.Heat the Ge2Sb2Te5 thin film on the silicon wafer at a fixed temperature using a hot plate.a.Dwell time is 300 s in this protocol.b.A custom-made copper chamber is used to enclose the sample and ensure a stable isothermal environment.CRITICAL: The Tg calibration result heavily depends on the dwell time because the phase change process is driven by an activation energy around 2.6 eV.8,10 A longer dwell time leads to a lower Tg.5.Cool down the sample to room temperature (∼23°C) and measure the Ge2Sb2Te5 thickness using AFM. Typical temperature history is shown in Figure 2A.Figure 2Ge2Sb2Te5 temperature calibration(A) Temperature history of Ge2Sb2Te5.(B) Ge2Sb2Te5 thickness versus temperature. Figure reprinted and adapted with permission from Cheng et al. (2020).16.Repeat steps 4–5 at increasing temperatures, and then plot the Ge2Sb2Te5 thickness as a function of the temperature as Figure 2B. The Tg of the sputtered Ge2Sb2Te5 is determined as 149°C.Note: This phase change material does not have a large abrupt jump at a single temperature, as in a first order phase transition. As a result, the full temperature history of the sample, not just the final temperature, can influence its phase change. In this protocol, the heating history induces a slight under-prediction of ∼2 K at the 149°C crystallization condition.Note: It is suggested that each sample is used only once for heating at a single temperature. Thus, the issue of the heating history is avoided.

### Thermal mapping vs. heater power

Timing: ∼3 h

When heated up to over Tg by the heater in the device, the amorphous Ge2Sb2Te5 on the device surface undergoes a density increase, so its film thickness reduces in the area with local temperature > Tg. Based on the thickness reduction that is characterized by AFM, we can perform thermal mapping at the nanoscale. Such thickness reduction or phase change depends not only on the heater power but also on the heating time. Therefore, varying either the heater power or the heating time works effectively in constructing a thermal map. This step focuses on varying the heater power to generate different phase change contours.7.Turn on the heater at a fixed power Pi for a dwell time of 300 s.8.Scan the Ge2Sb2Te5 topography after heating. If no thickness reduction is observed, which indicates that the device temperature is lower than Tg, increase the power Pi in step 7 until thickness reduction occurs as Figure 3B.Figure 3AFM images of Ge2Sb2Te5 phase change areas at multiple heater powers(A) Original device surface coated with Ge2Sb2Te5 thin film. All scale bars are 1 μm.(B‒E) Phase change areas at the nano-heater powers of 0.75 mW, 0.92 mW, 1.13 mW, and 1.37 mW.Figure reprinted and adapted with permission from Cheng et al. (2020).1Note: The heater power should be properly estimated to yield a temperature near Tg or higher than Tg.9.Repeat steps 7–8 with increasing heater powers to generate growing phase change contours as Figures 3B–3E.10.Construct the thermal map.a.Detect the edge of the phase change area using the Image Processing Toolbox in MATLAB or other edge detection algorithms, as Figure 4A.Figure 4Thermal mapping result by varying the heater power(A) The edges of phase change areas at multiple heater powers.(B) The constructed temperature field at the heater power of 1.37 mW. Figure reprinted and adapted with permission from Cheng et al. (2020).1b.The last edge corresponds to the calibration temperature Tg at the largest heater power Po. Assuming that the temperature is linear with the applied power, the temperature isotherm Ti at each previous edge is given by (RT is room temperature ∼23°C).(Equation 1)Ti=(Tg−RT)PoPi+RTc.Based on the temperature data at multiple edges, the temperature map To(x,y) at the largest heater power Po can be constructed as Figure 4B. At other heater powers, the temperature map Ti(x,y) can be correspondingly obtained by.(Equation 2)Ti(x,y)=[To(x,y)−RT]PiPo+RTNote: The AFM images should be pre-treated to eliminate the degree of inclination. The images should also have high resolution (at least 256 × 256 pixels) such that the edge can be extracted smoothly and precisely.CRITICAL: The multiple times of heating in the history affects the phase change. In this protocol, the estimated temperature step is kept at 10 K, which leads to a slight under-prediction of the temperature by around 2 K at the 149°C crystallization condition. It is suggested that the temperature step be kept over 10 K to avoid this effect of heating history. This effect can be estimated by assuming an Arrhenius phase change process.1

### Thermal mapping vs. heating time

Timing: ∼3 h

As aforementioned in the last step, varying the heating time can also alter the phase change area. In this step, we construct a thermal map based on time-dependent phase change.11.Turn on the heater at a fixed power P0 for a dwell time ti.Note: The fixed power P0 should be chosen such that the heater yields a temperature higher than Tg. Otherwise, no phase change occurs.12.Scan the Ge2Sb2Te5 topography after heating. If no thickness reduction is observed, which indicates that the heating time is not long enough to induce phase change, increase the dwell time ti in step 11 until thickness reduction occurs as Figure 5B.Figure 5AFM images of Ge2Sb2Te5 phase change areas at multiple heating times(A‒F) Phase change areas at the nano-heater powers of 0.68 mW. The heating times are 5 s, 30 s, 60 s, 90 s, 150 s, 300 s from (A) to (F), respectively. All scale bars are 500 nm. Figure reprinted and adapted with permission from Cheng et al. (2020).113.Repeat steps 11–12 with increasing dwell times to generate growing phase change contours as Figures 5B–5F.14.Construct the thermal map.a.Detect the edge of the phase change area using the Image Processing Toolbox in MATLAB or other edge detection algorithms, as Figure 6A.Figure 6Thermal mapping result by varying the heating time(A) The edges of phase change areas at multiple heating times. The heater power is 0.68 mW.(B) The constructed temperature field at the heater power of 0.68 mW. Figure reprinted and adapted with permission from Cheng et al. (2020).1b.The edge at the reference dwell time (tref = 300 s) corresponds to the calibration temperature Tg. Assuming that the phase change conversion follows an Arrhenius model and the conversion is linear with time, the temperature for each edge Ti at dwell time ti is given by.(Equation 3)Ti=[−kBEA(ln1ti−ln1tref)+1Tg]−1where kB is the Boltzmann constant and EA ∼ 2.6 eV is the activation energy of Ge2Sb2Te5 transition. Simply put, the edge at a shorter dwell time corresponds to a higher temperature.c.Based on the temperature data at multiple edges, the temperature map can be constructed as Figure 6B. The temperature maps at other heater powers can be obtained similarly as step 10c.

## Expected outcomes

This protocol provides a versatile method of measuring temperatures in microelectronic devices that relies on density change of a phase change material Ge2Sb2Te5. It can precisely characterize temperatures at nanoscale with minimal interference and minimal need for calibration. Temperature mappings can be constructed by varying either the heater power (Figure 4B) or the heating time (Figure 6B). The technique can achieve a spatial resolution as fine as 20 nm, which comes from the grain size of the Ge2Sb2Te5 material. The application of this technology can enhance the understanding of temperature field and heat transfer process in electronics such as magnetic recording heads and the embedded nano-heaters, which can lead to development of more reliable and efficient devices.

## Limitations

There are two main limitations to this protocol. Firstly, the contours, i.e., the edges of the phase change areas, correspond to Tg isotherm. To construct a thermal mapping from the edges, at least several heater powers or heating times need to be applied to induce temperature variations. Secondly, the current technique only works for temperature field that is higher than Tg. Otherwise, no phase change will occur. In this protocol, our Tg calibration result of Ge2Sb2Te5 is 149°C at the used dwell time of 300 s. The embedded nano-heater we used can easily exceed this Tg requirement. For other electronic devices with working temperatures lower than this Tg, then Ge2Sb2Te5 will not work to map the temperature field. This issue could be addressed by use of a different composition phase change material in the GeSbTe family, or other phase change materials.11,12 Pre-heating of devices may also work. In addition, the effect of heating history on Ge2Sb2Te5 phase change introduces uncertainty. This issue can be overcome by applying a large temperature step (e.g., >10 K) or using multiple identical samples.

## Troubleshooting

### Problem 1

How to choose the film thickness when sputtering Ge2Sb2Te5 in step 3?

### Potential solution

In this protocol, we use ∼20 nm Ge2Sb2Te5 as it is thin enough to have negligible effect on the heat transfer. The thickness reduction due to the phase change is around 1 nm, which is enough for AFM to detect. A thicker Ge2Sb2Te5 can induce a larger thickness reduction and thus increase the precision in the Z direction, but the Ge2Sb2Te5 film should not be thick enough to have a large thermal resistance, which will alter the temperature field.

### Problem 2

When operating the electronic devices in steps 2, 7–9, 11–13, the fragile nanoscale component (e.g., nano-heater in this protocol) sometimes breaks down.

### Potential solution

Proper anti-static operations should be taken to avoid electrical breakdown, such as wearing an electrostatic discharge (ESD) wrist strap.

### Problem 3

When calibrating the glass transition temperature of Ge2Sb2Te5, its film thickness is difficult to measure (step 6 in Ge2Sb2Te5 temperature calibration).

### Potential solution

First of all, the sputtered Ge2Sb2Te5 film should have a good and uniform surface quality with sharp edges on the silicon wafer, which depend on proper choices of sputtering parameters and photomask. In the step of measuring the Ge2Sb2Te5 thickness, the AFM images should be correctly post-processed (flattening) to eliminate the “bow” or “tilt” in the background. In addition, the heating condition affects the Ge2Sb2Te5 crystallization. The dwell time should be long enough to have a uniform crystallized surface as shown in Figure 7.Figure 7AFM images of Ge2Sb2Te5 after heating(A) Uniform crystallization.(B) Non-uniform crystallization.

### Problem 4

No thickness reduction is observed in step 8 or step 12.

### Potential solution

The Ge2Sb2Te5 transition temperature is near 150°C. The heater inside the device should at least yield a surface temperature higher than 150°C somewhere. The heater power should be estimated beforehand. This requires prerequisite knowledge on the heater design and the device design such as how deep the heater is embedded and how high the thermal conductivity of the device material is. Choice of the dwell time is also of the same importance.

### Problem 5

The edge of the phase change area is difficult to extract in step 10a or step 14a.

### Potential solution

How to effectively extract the edge relies on the quality of the AFM images. In some cases, the edge detection algorithm in the Image Processing Toolbox of MATLAB does not work well. It is suggested to develop customized algorithms for edge extraction. In this protocol, we start with the height data of AFM images, and then find the elliptical contour line with the maximal contrast.

### Problem 6

Besides AFM, are there other equipment suitable for this thermal mapping protocol?

### Potential solution

The Ge2Sb2Te5 undergoes the phase transition with abrupt changes in multiple properties (density, resistance, reflectivity). This protocol is based on the density change, so AFM is used to measure the film thickness. Regarding the resistance change, scanning electron microscopy (SEM) can be used to map the phase change area. As for the reflectivity, an inexpensive optical microscope can be used at the microscale. An optical demonstration of the Ge2Sb2Te5 response to micro-heating can be found in Cheng et al. (2020).1

### Problem 7

The temperature range of interest does not match the transition temperature of Ge2Sb2Te5.

### Potential solution

The GeSbTe family with another composition or an alternative phase change material with a similar property change can be used. For example, the GeSbTe family9 works for temperatures over 120°C, and a polymer13 works for temperatures below 200°C. Also, pre-heating or pre-cooling can be applied to change the environmental temperature.

## Resource availability

### Lead contact

Further information and requests for resources should be directed to and will be fulfilled by the lead contact, Dr. Qilong Cheng (qlcheng@berkeley.edu).

### Technical contact

Technical questions on executing this protocol should be directed to and will be answered by the technical contact, Dr. Sukumar Rajauria (Sukumar.Rajauria@wdc.com).

### Materials availability

This study did not generate new unique reagents.

### Data and code availability

This study did not generate new unique datasets or codes.
