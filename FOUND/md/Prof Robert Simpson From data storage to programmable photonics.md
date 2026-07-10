---
Title: "From data storage to programmable photonics"
Author: "Prof. Robert Simpson (University of Birmingham, formerly SUTD Singapore)"
Reference: "https://www.youtube.com/watch?v=g-l_OJzupp8"
ContentType:
  - "video"
  - "conference-talk"
Created: 2026-05-25
Processed: true
tags:
  - "source"
---

UK Metamaterials Network Colloquia talk (17 Feb 2023). Covers PCM history, metals compatibility with GST, wide-bandgap PCMs (Sb₂S₃), hyperbolic metamaterials, and visible photonics applications.

## Key Claims

- PCM history oscillation: Ovshinsky (1968, electrical) → optical discs (Matsushita/Panasonic) → Intel Optane (electrical) → photonics research (now back to optical).
- **Metals compatibility with GST** (XRR measurements): Al reacts immediately; Ag also reacts; W is better; Au is good but shows minor interface reaction with thin GST; **TiN is best** — no reaction, melting point 3000°C, plasmonic in visible (like gold), used as standard PCRAM electrode.
- GST designed for optical data storage (high absorption to absorb laser for heating) → poor fit for transmissive metamaterials (need to control phase, not absorb).
- **Wide-bandgap PCMs needed for visible photonics**: data storage PCMs have bandgap < 0.7 eV; visible requires > 1.5 eV. Selenides and sulfides have larger bandgaps than tellurides.
- **Sb₂S₃** (antimony trisulfide): widest bandgap of PCM candidates (~1.5 eV); transparent only above ~600 nm in visible; refractive index ~3→~4 in near-IR; cheaper (~20× vs. Sb₂Se₃) and more Earth-abundant; challenges include birefringence and growth-dominated crystallization.
- Sb₂S₃ demonstrations: color-change films (pink amorphous → blue crystalline), multi-state writing (Mona Lisa over Girl with Pearl Earring), on-chip Mach-Zehnder interferometer (π phase shift, with TU Eindhoven).
- **Hyperbolic metamaterials**: Sb₂S₃ as dielectric + Ag as conductor → Type 2 hyperbolic metamaterial at visible wavelengths.
- Nanohole arrays in Sb₂S₃-loaded structures enable beam steering at ~700 nm.
- Intel Optane PCRAM uses near-same material (GST) but was discontinued (announced ~2022–2023 by Intel).

![](https://www.youtube.com/watch?v=g-l_OJzupp8)

Prof Robert Simpson, Associate Professor at the University of Birmingham (formerly at the Singapore University of Technology and Design), highlights how new materials need to be developed specifically for programmable metamaterials.  
  
First, Prof Simpson discusses the history of phase change materials and their application to photonics. He then discusses the suitability of the materials that have been used to enable visible, near-infrared, and mid-infrared programmable metamaterials. Finally, he shares his plans for his new position at the University of Birmingham.  
  
This talk is part of the UK Metamaterials Network Colloquia series. The recording is from a talk given on Friday 17th February 2023.

## Transcript

**0:00** · uh so in 2019 I moved to Singapore um and I also spent a year in MIT sutd this University was funding collaboration with MIT and it was a new University so to give the new faculty experience we had the opportunity to spend some time in MIT I'm also the uh omax associate editor I've been doing that since 2018 and as of this year I've started working

**0:28** · in Birmingham so I've been back and forth between Asia and Europe or the west and the East quite a few times over the last decade or so yeah so a lot of what I'm going to talk to you today is about the phase change materials and how they can be applied to photonics um so for those that aren't familiar I

**0:51** · know a lot of people in Exeter are very familiar with uh phase change materials but some might not be online um the idea is quite simple you have a crystalline material um and you can heat it up with a nanosecond heat pulse and it melts it disorders and the optical properties change considerably and you can quench it into this uh amorphous structure if you remove the heat fast enough and this has a low reflectivity this has

**1:16** · a high reflectivity this is a low conductivity this is a highly conductive material and you can switch back and forth between these materials by heating to different temperatures for different amounts of time and this can be done Millions if not billions of times so it's a highly recyclable and in the 90s these materials were

**1:37** · used commercially for optical data storage in rewritable DVDs and then more recently Intel have been using the same almost the same material for electrical phase change memory in their optane products because there's a large change in resistance this is a logarithmic scale here when this material switches between amorphous and crystals and states and people are generally happy with these materials although I think Intel are not I think they've just announced that they're not they're discontinuing this product but

**2:09** · generally on Amazon at least it has very good reviews so it's kind of useful um so the history of phase change materials shows that it kind of goes backwards and forwards between Optics and and electronics so in 68 1968

### Phase Change Material History

**2:29** · ovginski shows an electrical device that changed phase based on a Telluride material and then slightly later they showed uh the same materials could be used for rewritable optical storage um and then in Panasonic or at the time machista developed Optical rewritable disks based on very similar materials and then it switched to electrical so it's gone from

**2:57** · electrical to Optical and then back to electrical again and now generally it seems that the research is going back to Optical and photonic structures again um so there's this kind of oscillation in the in the application space interestingly not many people have shown kind of Electro Optical phase change devices so the reason this material is is interesting is this huge change in

### Absorption vs Phase Control

**3:26** · refractive index so this is a real part of refractive index so this controls the phase of the light and this is the imaginary components of the fracture of index which can controls the the absorption or the amplitude of the light um you can see that in the infrared at least this famous data storage germanium anti-metillaride has an enormous change in effective index and the refractive index is very large generally in both States and if you go into the infrared

**3:53** · above one and a half two microns and the material that the the photons have energy below the band Gap so they're not absorbed strongly so the the material is also transparent but has a large change in Optical refractive index real part of a fractive index so they have the opportunity at least in the infrared to control resonances and path links and things without changing the the face I'm not sure why that happened so in 2011 uh I moved to Spain and

### Data Storage PCM Photonics

**4:26** · um we did something relatively in principle conceptually very simple but it's actually quite difficult technically we patterned a small amount of phase change material on the uh on a a silicon ring resonator and showed that we could crystallize this material and switch the

**4:46** · resonant frequency of this ring resonator by crystallizing this phase change data storage material so this again this is a material that was originally developed for data storage um and the reason there's a shift in this frequency is this has a higher refractive index and it redshifts when it crystallizes because of the higher effective index so we see this longer path length and a redshift in its resonance and we can also switch this back so we can go from the crystal to the uh amorphous phase and switch this resonance backwards and forwards

**5:17** · similarly in in Spain we made these plasmonic waveguides so these are surface plasma and ploweton waveguides we launched the light into a surface plasma mode through these gratings and it's transmitted along this uh gold waveguide and we've covered the gold wave guide in places with GST and this

### Plasmonic Waveguides Switches Probe laser

**5:40** · attenuates the transmission of the surface plasma waveguide so we're using the absorption property the extinction coefficient of this material to change the transmission so this point here is where we launch the light there's a reference scattering particle in this line defect at this point here so we can normalize the transmitted light and then we measure the intensity at different positions from the launch site and then

**6:07** · we can make these graphs and show that we can attenuate the the this is just a transmission line experiment but we can attenuate the surface plasma pluton transmission so these these were I mean the the idea of this was to make some kind of plasmonic ram some sort of Electrical uh memory that you could read

**6:25** · plasmonically um so this is the reason this GST is shaped in this way you could pass a current for a heater to crystallize it and measure the surface Plasma on plavatone waves through it so that was the whole idea behind this this this paper um so but so I was showing these two papers on the on the transmission of the surface plasma polaritones and these ring resonators at a conference in Spain in 2012 beginning of 2012 and then this

**6:55** · guy from Bristol came over to me and said well this material looks fantastic uh can we make some meta materials from it so that's how this that's how I became interested and uh started doing research into phase change metamaterials so Martin from Bristol was the one that introduced me to this this potential application for these phase changing deals and he had a student that a postdoc there finished working in

**7:25** · Bristol and took a faculty position in in Dalian university called Turn um and in 2012 we rolled out a whole bunch of papers just showing the potential of phase change materials data storage phase changing materials mostly in the infrared where the where we were controlling the phase of the light rather than the absorption based on uh the GST controlling resin resonances and

**7:53** · meta atoms so we were mainly trying to operate above two microns where the absorption is minimal and where we're just having this change in refractor index um so these are some of the the devices that we one of the first devices that we we tried to fabric tried to simulate um and uh test whether the first generator would be useful and the basic idea here is that we apply an electric field to one of these uh squares and

### Resonance in Metal-Dielectric-Metal Metama

**8:23** · this causes um uh the electrons to move obviously in this in this metallic square and this will create a magnetic field around it so essentially we have an inductor around this metallic Square

**8:38** · um and then when the electrons are at the end of the their path uh they're going to behave like a capacitor we'll have an image charged through this dielectric so we have some strong electric field going through the dielectric at this point and then the electrons move in the opposite direction because of this electric field and it turns into a conductor so this whole system can be modeled as a LC circuit um

**9:05** · so the the frequency of uh an LC circuit is one over two Pi root LC um so the wavelength is roughly proportional to one over square root of LC um and the capacitance for when the materials behaving like a capacitor is proportional to the these geometric parameters and the permittivity of the material and when it's behaving like an inductor it's proportional the inductance proportional to length and inverse is proportional to thickness so you can see that if we substitute these

**9:38** · into this frequency equation you can see that the wavelength is proportional to the geometric parameters but also dependent on the square root of the dielectric function so let's go to dielectric function is the refractive index so if we can control the refractive index of the material we can control the resonant wavelength for resonant frequency of these these meta atoms essentially so that was the whole idea behind this uh uh structure where

**10:09** · we have some kind of thin layer of tunable material um so that we can control the resonant frequency of these these structures um so these are some of the early simulation results I should mention sutd the university I joined in 2012 when we started working on these materials it was a completely new new University in

### Infrared Programmable Absorber

**10:36** · fact we didn't even have a proper campus we had a temporary campus in an old school um and then whilst we were waiting for our campus to be built our campus wasn't built into until 2015. so we didn't have any facilities we didn't have clean rooms there was nothing right um so we were relying on simulations at the beginning um so you can see here from these simulations the neomorphous state this this structure has a resonant frequency at around uh two two and a half 2.25

**11:09** · microns and then when we crystallized the material the resonant frequency uh uh switches to slightly longer wavelength because of fractal index of the material is larger so potentially you can make some kind of metamaterial filters that are programmable in the infrared using these uh phase change devices

**11:31** · so as I mentioned we didn't have a clean room um but the Harold giesen's group in Germany in Arkan did and they created very similar structures um that basically proved this this concept worked uh experimentally um so they they created aluminum square arrays with a very thin layer of GST and an aluminum back mirror underneath and it excited these plasmonic resonances in the in these aluminum layers and uh so

**12:04** · very strong tunability of the resonances when they switched the material between your morphs and crystalline States so this was an experimental proof that these data storage materials could be used for programming these mid-infrared metamaterials um I should mention that you know this is a very important paper and I don't mean to be so negative about what and what I'm about to say but this is an aluminum aluminum resonator aluminum melts at around 660 degrees C which

**12:37** · happens to be the same temperature that GST melts so it's actually um highly likely that this structure wouldn't survive many cycles and quite likely as you'll see in a minute that the aluminum will diffuse into the GST and create some sort of alloy that is non-switchable

**12:59** · so gold is a better choice but still gold is not not great gold has a melted temperature about a thousand degrees C um so we in 2012 2013 um we published a whole bunch of papers showing different metamaterial structures they're all based on the same kind of concept that we could control resonances with this metal phase change metal structure and using

**13:27** · the phase change material to change the resonant frequency of these of these devices so these were all simulation papers as I mentioned in 2015 we got a camper sent with a clean room and we could start making things so in 2016 we made our first paper which is based on plasmonic structures on top of GST and we could

**13:51** · show different colors and things that we could create with these with these devices um as I mentioned uh we were using many goals uh Metals for the plasmonic elements on the in these metamaterial structures um this you don't really need to understand this too much but this is a x-ray reflectivity measurement so if you

### Metals and Chalcogenides

**14:16** · put a very thin layer of metal on a substrate you can measure the interference of the x-rays as it bounces around off the surface um and you you see these very nice interference patterns and from this you can work out the thickness of the material you can also work out the the density and how nice the interfaces are if you see very nice oscillations it means the interfaces are great the the pristine interfaces if you see no

**14:46** · um oscillations means the interface is very rough or inter diffuse um so we did something very simple we just put different materials on top of GST because we wanted to make these tunable plasmonic resonators to see which ones um liked being on top of GST in which ones kind of into the views or became very rough um because this is fundamentally important if you're going to make plasmonic GST controlled resonators

**15:16** · um but for example aluminum this is the red curve is a measured curve here as soon as we deposit it it's reacting somehow with the uh GST and creating a horrible interface in all of these oscillations disappear same is true for silver tungsten is a lot better gold is

**15:35** · really really nice um and also titanium nitride is really nice it it turns out that even with gold we notice that there's a little bit of a reaction happening in the interface so if you have very thin layers of GST gold is not great either but titanium nitride is probably the preferred material and it also happens that titanium nitride

**15:58** · behaves like a plasmonic material it has a negative real part to the dielectric function in the in the visible spectrum and that's why for example titanium nitride tipped screws look like gold um their Optical properties are very similar to gold in the visible spectrum so I think titanium nitride is a good choice uh also the is this going to work

**16:21** · the melting temperature of titanium nitride is 3000 degrees C whereas gold is like a thousand degrees C so it's when you heat these materials up to switch them it's highly likely that titanium nitride Will Survive uh and if you need any more convincing titanium nitride is a common electrode used in phase change memory electrical phase change memory so it seems like a wide Choice uh for if you're creating plasmonic metamaterials without tuned with GST

**16:50** · um in this case we didn't use titanium nitride we used gold and that we had to put a diffusion barrier silicon nitride between the gold and the GST to stop strange things happening but our aim here was to create a transparent meta material the plasmonic metamaterial in

**17:08** · the infrared um but it didn't work great so as you can see here these are the simulations of where the resonances should be depending on the size of these plasmonic resonators silicon's transparent in intrinsic silicons um transparent in the infrared so this should be quite a transparent material with nice sharp resonances but when we did the experiment although we did see some dips the resonances have a very low

**17:38** · Q factor um but transparent meta materials are actually much nicer if we want to make tunable they had no beam steering devices or some kind of filters that we can put in front of detectors but it looked like these plasmonic approaches were not were not really that

**17:57** · suitable so there was a clue of how we might be able to do these kind of transparent beam steering devices um in 2006 at epcos which is a phase

**18:13** · change conference that is held in Europe um and this was a an abstract published by energy conservation devices which is the company that Stan of shinsky who started the face change field um start started his company and back in 2006 it basically described a way of making a beam steering device from from GST where they have an array

**18:39** · of um oscillators uh I think there are eight of them here with a separation of um quarter pie I guess between each of these oscillators and these are written into GST with a laser and they said that when they shined light through this this structure the material that it was able to bend the beam by around two degrees and theoretically it should be able to bend the beam by 10 degrees so this this

**19:10** · beam bending device was described in 2006.

**19:15** · however they said they were they they wanted to do this at telecoms wavelengths and the reason was that they wanted to make some sort of multiplexer system for uh Telecom Optical communication and they said that their material was not really GST 225 the common facial into it was not really suitable so they made a completely new alloy for this application that was more transparent at 1550

**19:43** · um and they although in the I didn't attend this conference but I downloaded the abstract they didn't describe the experiment they just described they sorry they didn't show the results from an experiment in the abstract they just described the experiment but it seems that these kind of meta surface ideas uh

**19:59** · again stanoshinsky was the head of everybody kind of proposing these things 10 years before everyone else started working on them which I think is kind of neat um yeah so then exactly 10 years later there was uh this uh paper by Nikolai

### Dielectric Metamaterials

**20:18** · zelodev's group where they used a film of GST and they laser wrote these kind of fresnel surfaces um we've entered into GST and showed that they could create different types of focusing depending on the the structures they created so there again they're using actually die dielectric effects level and plasmonic effects to control the phase of the light for each of these rings to create this focusing this focusing point and then

**20:48** · um Exeter David's group I believe um just a few years later showed that you could create dielectric resonators from Silicon and then by putting a thin layer of GST phase change material in the Silicon um you can turn on and off certain

**21:09** · resonances in the in the in the structure um for example this electric dipole resonance is removed when you crystallize the material but it doesn't look like it's it doesn't I don't know maybe you can correct me David but it doesn't look like the the the there's much of a shift in the in

**21:30** · the resonance it's mainly using the absorption effect and increased absorption rather than the change in the refractive index the real part of a fractal index to control these resonant effects um so what we would really like to do is control the resonance resonant wavelength from resonant frequency of these uh resonances because then we can

**21:56** · create uh phase arrays and do beam stirring just as uh this this paper from 2006 showed um but it seems like the the materials that are available that most people are using the data storage materials are not they're too absorbing it most of the wavelengths that we're interested in in their infrared invisible so for example if you take these uh data

### Application Parameter Importance

**22:23** · storage materials um and they were designed for a very specific purpose which was to store data for 10 years and be able to switch very easily with a visible laser light to to switch a material with visible laser light you need to heat up the material and so it needs to absorb the laser light so in

**22:44** · metamaterial transmissive metamaterial research we don't want to absorb we just want to control the uh the resonant frequencies so maybe the for different applications like holography or beam steering there are different requirement sets that we should be focusing on and trying to find new materials to meet those requirement sets so for example this this table shows the importance of of different properties for different applications so in data storage

**23:15** · stability of the material is very important we don't want to lose our data if we just leave the disk on our table for you know a few hours we want the data still to be left there data but that's not so important maybe for displays maybe we refresh the display at quite High rates so the the the the of a

**23:36** · beam steering maybe for lidar we we don't need this kind of archival stability um whereas we might quite like multi-state our analog transitions in refractive index rather than just on and off transitions which are more typically required for digital data storage um so there would I think there were horses for courses right like we need to develop new materials for specific applications

**24:07** · so yeah so I'm saying here new PCMS are need that should be needed for programming visible photonics and net infrared resonances so that I I don't know I guess you guys you guys know Back to the Future too right okay uh this was an advertisement

**24:26** · in Back to the Future too I think it was for like 2015 and by 2015 they were predicting and they got a lot of things writing their predictions and Back to the Future too but they predicted we'll be watching Jaws 19. and we would see these build

**24:43** · holographic billboards that'd be great I think if we could do this right we're a bit behind only like 10 years uh well eight years behind but I think we can still aim for having these things but to do this we need wide band Gap phase change materials so typically the data storage phase change materials have a band gap of less than 0.7 EV but the uh

**25:06** · wide band gap for Visible visible visible light we need more than one and a half EV uh in order to be able to to to create Holograms and things that our eyes can see so that requires a whole new set of phase change materials so most of the data storage materials are based on tellurium if we go up the periodic table from telone to selenium the materials become more dielectric less metallic so around the same sort of time

**25:37** · um I and also uh a few of us like JJ and MIT and also Southampton I think we're thinking along the same lines um so maybe we should be looking at selenides and sulfide level intellerides for for Visible phase change elements in in these meta atoms

**26:01** · um this this shows the point so if we look at Anton mini Telluride which is a phase change material the band Gap is around 0.5 EV but if we go to sulfur and to me sulfide the band Gap opens up to one and a half EV so we can open up the band Gap by going up the periodic table and that's what we did we took we took endomet sulfide and see try and see if

**26:22** · we could use it to make phase change devices but a few other good reasons I think this is my I'm just going to cell Anthony sulfide now because I think the few other contenders like this gsst and Anthony salivide out of all of the contending White Band Gap phase change materials and timisulfide has the widest band Gap in fact it's the only phase change material that's transparent and visible um also it's cheap especially if you exploit poor people in

**26:54** · Indonesia to carry sulfur down from volcanoes I think they only get paid five pounds a day or something it is it's crazy um how much these guys get paid but this is someone in Indonesia climbing up a volcano and taking down huge rocks of sulfur out of the volcano um I'm not saying this is a good thing by the way I'm just saying that that's that's how it's done at the moment um and if you look at Anthony sulfide on

**27:24** · Sigma Aldrich uh you can see here what am i showing okay I think I'm just showing the price yeah basically it's 106 Singapore dollars which is about 50 pounds for 100 grams of Anthony sulfide um and uh uh price per gram

**27:47** · if I compare Anthony sulfide and to myself it's about 20 times cheaper than antimeteroid and you know UH 60 times cheaper than uh Anthony so far I should mention that on the day when I looked up these prices which was just before the Mrs conference it was Black Friday so they had a signal just had a deal it's not usually that cheap

**28:11** · um and also the Earth abundance if I compare these material antimony and sulfur out of all the contending phase changing materials are the most abundant materials on Earth so it's sustainable in some way so I like Anthony sulfide um optically antimony sulfide has a

**28:31** · smaller refractive index change in the other contenders but it's still still considerable it goes from about three to nearly four in the uh near infrared um obviously GST is a lot larger it goes from four to six but the absorption is enormous in GST and same for gsst is

**28:49** · these two materials have the largest absorption if both of compare say 800 nanometers and to me sulfide and Anthony selenide the antimony sulfide is transparent whereas Anthony solenoid isn't and that way then so you do have

**29:05** · to sacrifice a little bit of the real part refractive index change is smaller than the rest but I think it's still big enough to do interesting things uh okay this is another refractive and next part of Anthony sulfide in the visible so you can see that I say it's

**29:20** · transparent and visible but it's really only the far end of the visible above 600 nanometers this material becomes transparent um so we did a whole bunch of tricks in Singapore the first paper we made was very simple we just made a thin film reflector with a a mirror essentially

**29:40** · with Anthony sulfide on the surface and uh we crystallize that it turned blue and then we re-morphize it with the laser and it turns back to Pink So this was the first kind of simple demonstration that you can get nice effects in the visible with this and the reason we see this large change it's actually we're not exploiting the we're exploiting absorption again we're not exploiting a real part of refractive index change so much it starts absorbing at around 600 nanometers so we

**30:08** · essentially built a resonator that resonates on either side of the 600 nanometer line depending on the phase of the material so we can selectively absorb or not and that's why we get this huge color contrast my friend Joelle Joelle Yang is really into making art which you can only see if you've got an expensive microscope um so he his group wrote The Girl With a

**30:33** · Pearl layering into antim sulfide with a A you know a nano scribe do you know what no scrub is it's a two Photon absorption uh direct lithography system so using the second laser and but he just used his Nano scribe to write this picture then we crystallized it and then we in the same area we wrote the Mona

**30:55** · Lisa into the into the into the material but this was just to show that cyclable and we also did some simple cyclability tests we've made electrical heaters with this material on top and then we uh again it's pink in the amorphous State we crystallize it it turns blue and you just put this material on top of a nickel chromium heater and pass a current through it and use dual heat to crystallize it um the cool thing about this material as well is that it's very easy but to

**31:27** · amorphize different refresh scenes like different refractive indices into the material so it's not just on and off we can have multiple States and I think I can explain that I'm not going to do it today but there's a there's uh it seems that the antimony coordination in the material changes with temperature and we can lock in certain coordinations and that strongly affects the optical properties other groups have started studying this material now and it showed that it can be cycled more than seven thousand times if you don't fully switch it if you just

**31:59** · go to maybe one of these intermediate States um so I think it's still a useful material we've put these things on Max Endo interferometers um on on-chip photonic structures this is with uh uh Tu Eindhoven

**32:15** · um and we showed that experimentally that we can control the interference pattern and get uh kind of the Pie Face shift essentially in the in the transmission um so this is useful for example for setting weights in neural networks Optical neural networks and we've also applied antimiculfide to metamaterials and meta surfaces so the first demonstration which we haven't published yet uh but we will probably hopefully publish it this year because just kind of still polishing it

### Hyperbolic Metamaterials

**32:48** · um but we made antimisulfide hyperbolic meta materials so these are materials that have very large um uh uh birefringence so if a material is just a normal dielectric and it has no directionality to the refractive index and you plot the the K value uh you see that we we have a

**33:16** · circle if we have a biofringent material this would become elliptical if it was a dielectric in hyperbolic metamaterials we combine conductors and dielectrics together to create highly birefringent materials and there are certain effects that you get where for example you can have Solutions which are no longer on a sphere on ellipsoid but solutions to the wave equation where you can have extremely large K vectors so large K

**33:46** · vectors means that the material the wavelength is going to be very small and we you're going to be able to set sense things uh more easily because we're more likely to interact with anything that you put close to the metal surface so two types of these metamaterials type 1 and type 2 and they've been used for a range of different applications from sub web of Imaging nanoscale wave biosensing

**34:09** · um oh and the other thing I wanted to mention another area that I've worked on in the past is antimatter souplasters these happen to be they happen to have hyperbolic dispersion in terahertz regime so I think there's some opportunities there to do create

**34:27** · hyperbolic terahertz metamaterials of these kind of super lattices um but I mean I'm talking about the visible now so that's something else so this is one of the attempts we made to make a hyperbolic metamaterial essentially we use anti-sulfide as a dielectric and silver as a conductor and

**34:46** · we put a diffusion barrier in between this is a tem image so in plane in plane in this direction the electric field feels the silver because it's conducting in the plane out of plane the material is an insulator because you have antimate sulfide so that is if we go back that is I think this condition we have a negative permittivity out of plane but in plane we have a positive permittivity so it's a type 2 metamaterial

**35:20** · so in the crystalline phase when antonymsulfide's crystal in in the crystallized phase if we look at 6 30 nanometers just here where this blue line is we see that the real part is positive and the uh the the in-plane and the outer plane is also positive so it's basically behaving like a birefringent um uh dielectric so I'll have a an ellipsic elliptical

**35:47** · um uh sphere in k-space however when we crystallize the material at the same wavelength the material now has a negative uh in-plane real part and a positive uh out of plane real part so now it's a type 2 metamaterial so we can switch between Type 2 and normal uh

**36:11** · type 2 hyperbolic meta material in a normal dispersion relation for dielectric by crystallizing the Anthony Telluride layers in this in this stack and that's kind of interesting because you can start to do some interesting things uh for example we put Quantum dots that fluoresce at 630 nanometers on top of this structure and it just concentrate on the blue and red lines here so in the crystalline phase where we have a kind of elliptical dispersion

**36:43** · relation um the material is not the fluorescent lifetime is very long for these uh Quantum dots but when we crystallize the material it has a hyperbolic dispersion relation so we can have very large K vectors and a range of K vectors which means there are more roots for the fluorescent particle to fluoresce the more options so it can fluoresce more easily and it can Decay faster so we get these uh uh much faster Decay rates

**37:13** · and this is kind of interesting for single Photon sources in single Photon sources if you have a single quantum dot you don't know when it's going to fluoresce it confess at any point um within a certain distribution of time but if you can kind of charge up the material put it into an excited state in uh in in in this with a hype within in a

**37:40** · normal elliptical material and then switch it very quickly into a hyperbolic material the emission should happen just after you switch it it'll become much more deterministic um because it the the Decay is much faster in the in the amorphous state so and you can amorphize this material much faster than you can crystallize it so this is kind of the idea behind this hyperbolic metamaterial research

**38:06** · another thing we've done is created these dielectric meta surfaces so um David's group made GST thin layers on Silicon dielectric but we created the whole structure more or less from antimosulfide so the resonance is actually in the antimony sulfide itself the resonators antimosulfide we controlled the size and uh gap for these

### Dielectric Metasurfaces

**38:30** · and we demonstrated we could create a whole bunch of different resonances and this is seen as different colors in the reflect in the reflection Spectrum and that's nicely shown by the these color gamuts here so this is the gap between the resonators and this is the distance um yeah and under certain conditions if

**38:51** · you get the magnetic uh dipole in the electric dipole in the completely out of phase in these resonators you can get uh perfect or much stronger reflection then when you crystallize the material uh the 600 nanometer starts to be absorbed so you suppress this this condition but again we're using absorption rather than the the refractive index change

### Crystallisation Problem

**39:17** · um I just want to show you a video of Anthony sulfide crystallizing and then you'll realize there's a problem so this is a film of Anthony sulfide and you can see the crystal area growing from a single point and this is under an optical microscope this is probably now about 100 microns across um and then you see another crystal growing from The Edge where it's nucleated over here um so you can see how the material crystallizes this is uh known as growth dominated crystallization not many nucleides form

**39:47** · nuclei is a very sparse and then the material grow from a from a single point the problem is the problem with Anthony sulfide is that these individual resonators are isolated in this case so if nucleation happens say here

**40:05** · it cannot grow and crystallize this one because they're isolated so this makes crystallizing these materials these structured materials these isolated structures very difficult um so we needed to come up with another solution another problem of Anthony sulfide is when it crystallizes its biofringent so you get some orientations

**40:28** · polarization orientations which have a very large Optical contrast between the amorphous state but there are other orientations which are not so uh large the contrast is much smaller so these are I'm telling you the dirty secrets of antim sulfide at the moment so we have to overcome these problems one way an engineering nanostructural engineering Solutions less for the for the uh growth problem and nucleation problem

**40:57** · um is not to create isolated structures but to create nanohol arrays which also show dielectric resonances now if the material nucleates from this point here the crystal can still grow across this net across the whole structure because the material is no longer the is everything's connected and um my my collaborators and friends in MV

**41:20** · a-star actually had this idea to solve this problem um and they showed a modeled that this could also be used to create dielectric resonances and antimiculphide um so they actually created I think this is around 100 microns by 100 microns nanohol array which should have um uh be a hugens meta surface but they

**41:47** · noticed that there are two distinct regions in here and this is due to that that birefringence problem so this Crystal orientation here has a different orientation to hair and the optical properties are slightly different within this hundred Micron Square so that's one of the issues that we're trying to solve at the moment and as I said uh in 2016 uh sorry 2006

**42:11** · not 2016. uh 2006 strand at our suggested that we could make beam steering devices by creating arrays of different size resonators and that's exactly what we tried to do here so we created these Nano hole arrays where the holes are slightly different sizes and the resonance is separated by quarter Pi um and in the amorphous state if we scan the like these little designed to operate around 700 nanometers a free

**42:39** · scanner transmitted light through it we see \[Music\] beam bending around 15 degrees or so and then when we crystallize the material this is suppressed and the light tends to go straight through and then if we reimorphize it with a laser we get beam blending again so we can achieve these sorts of effects with this nanohall array um and what our ultimate aim is not not to use different sized resonators is to

**43:07** · use the same size resonator but to gradually amorphize different levels of refractive index so that we can achieve um different resonate resonances not by size not by the geometry but by the optical state of the material

### What's next?

**43:26** · okay so that's pretty much what I wanted to show you so this is what I think we have to do next we have there's a number of new compositions uh emerging in the last few years it might be useful for dielectric phase change resonators so it's worth looking at lows we're also working on I haven't showed it here but materials which have a very phase change materials which have a very low thermal conductivity which are much easier to heat up when they're on say conducting substrates plasmonic substrates or on

**43:56** · Silicon which is also very thermally conducting and we need we need these low thermal conductivities to make very efficient phase transitions um we're also working on new types of antimiculified anti-sulfide alloy develop elements that seem to have smaller grains which will help solve this birefringence problem we're working on we found something that

**44:20** · we can put into Anthony sulfide that will open up the band Gap even more and just push it a little bit more into the visible and it still has a large effective index contrast and we've also been looking at and thinking about uh millimeter wave wave guides uh so that's

**44:38** · the other thing and I've joined a group in or joined the Department in Birmingham that has some background in uh terahertz and millimeter waves so I hope I'm hoping to be able to collaborate with those guys and others on this on this subject for me I'm also um I my plan is to try and support other groups doing phase change research but I also want to do slightly different things in the future in particular I'm interested in sensing and I have a bunch

**45:07** · of ideas relating to biosensing and magnetic field sensing using chalcogenites predominantly um which I'm going to start working on in the in the coming years in in Birmingham but I'll still do phase change 30 of my time

### Summary

**45:25** · so that's pretty much summarized what I wanted to say uh Anthony sulfide that's the widest band gap of all the PCMS um it's programmable in the info made programmable structures and invisible in the infrared we've had some success of applying antim sulfide to program displays on chip photonic structures couplers and things hyperbolic metamaterials electric metal surfaces and we've also shown that the property is a continuously tunable and my plan is

**45:54** · to continue working on PCMS but also develop new sensing Technologies based on childhood nights I think that's it lots of people to thank um so I thank all these guys um and uh if you want to link to me in in LinkedIn uh that's a QR code yeah thank you \[Applause\]