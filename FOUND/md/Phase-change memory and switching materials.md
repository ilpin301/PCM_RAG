---
Title: "Phase-change memory and switching materials"
Author: "Stephen Richard Elliott (University of Oxford / University of Cambridge)"
Reference: "https://www.youtube.com/watch?v=0XCHWlXfUyw"
ContentType:
  - "video"
  - "conference-talk"
Created: 2026-05-25
Processed: true
tags:
  - "source"
---

Conference talk by Prof. Stephen Elliott on machine-learned interatomic potentials (GAP/ACE) applied to GST and elemental Te. Covers atomic structure of glassy GST, device-scale crystallization simulations, and chiral crystallization of Te.

## Key Claims

- **Machine-learned potentials (GAP/ACE)**: DFT-accurate, linear-scaling; enable million-atom simulations of GST (vs. 500-atom DFT limit). Three orders of magnitude faster with ACE vs. original GAP.
- Amorphous GST contains many defective-octahedral (seesaw) units already present in the glass — minimal atomic movement needed to form crystal nuclei → fast crystallization (~nanoseconds).
- Glassy GST band structure: ~60% of models show no gap states; ~37% do. Deep gap states are localized on 5- or 6-coordinate Ge, spread over complex multi-atom wavefunctions.
- Shallow (band-edge) localized states form small chains of hyper-bonded seesaw units (3-center 4-electron bonds), distinct from normal covalent bonds.
- **Device-scale simulation**: 20×20×40 nm GST device (half-million atoms) crystallizes in ~20 ns matching experimental timescale; nucleation-dominated at 550 K (many small crystals) vs. growth-dominated at 650 K (large single crystal growth).
- Neuromorphic computing: 100×100×5 nm slice (~800,000 atoms) models continuous crystal/glass states and grain-boundary effects on conductivity.
- **Elemental Te as selector switch**: crystal Te = semiconductor (off); liquid Te = metal (on). First switching event requires ~3 V (single crystal melting); subsequent events ~1 V (grain-boundary-induced lower melting temperature).
- **Chiral Te crystallization**: amorphous Te crystallizes via cubic intermediate motifs (only ~90 meV/atom above chain crystal) that transform into left- or right-handed helical chains. Grain boundaries between chiralities move via soliton-like mechanism.

![](https://www.youtube.com/watch?v=0XCHWlXfUyw)

Stephen Richard Elliott presents Phase-change memory and switching materials  
‘Phase-change’ (PC) materials can be defined as those that exhibit (ideally marked) changes in physical properties between their structural phases. There are very many examples of such materials, and of the properties involved. One such example is the material AgI: the low-temperature β-crystalline phase is a moderate silver-ion conductor; the high-temperature α-crystalline phase, on the other hand, is a superionic (fast-ion) Ag+ conductor. However, in this talk, I will concentrate on those PC materials which also exhibit extremely rapid phase-transformation rates, of the order of nanoseconds. In addition, one of the phases involved is crystalline but the other is non-crystalline (glass or liquid).  
  
The PC materials of interest here are tellurides. One such is Ge2Sb2Te5 (GST-225), or related compositions along or near the GeTe-Sb2Te3 compositional tie-line. The metastable rocksalt crystalline phase is electrically conductive (degenerate semiconductor); the glassy phase is an electrically resistive semiconductor. The glassy phase is extremely thermally unstable; voltage-pulse-induced Joule heating can cause crystallization to take place in a few ns or less. This PC behaviour forms the basis of new non-volatile, electronic random-access memory (RAM) devices, in-memory and neuromorphic computing applications. Elemental Te has recently been shown \[1\] to function as a selector switch, e.g. for individual memory cells in 3D cross-point PCRAM arrays; crystalline Te is a poorly-conducting semiconductor, whereas liquid Te (produced transiently by Joule-heating voltage pulses) is metallic and conducting.  
  
In this talk, I will describe the results of molecular-dynamics simulations using density-functional theory (DFT) and linear-scaling machine-learned interatomic potentials of both GST-225 and Te, exploring the phase-transformation behaviour of these PC materials, as well as chiral crystal growth in Te.  
  
\[1\] “Elemental electrical switch enabling phase segregation-free operation”, J Shen, S Jia, N Shi, Q Ge, T Gotoh, S Lv, Q Liu, R Dronskowski, SR Elliott, Z Song and M Zhu, Science 374, 1390 (2021)  
\[2\] “The pathway to chirality in elemental tellurium”, Y Zhou, SR Elliott, DF Thomas du Toit, W Zhang, VL Deringer, arXiv:2409.03860 (2024)

## Transcript

**0:04** · all right welcome to the last session of the morning uh our first speaker is Stephen Elliot who's professor of chemistry and both the University of Oxford and the University of Cambridge and without more Ado please stepen please start thank you very much Mike and um thank you for the organizers for uh this invitation to um talk here uh present

**0:37** · some of our uh very latest um results so it's a great pleasure to be at this really interesting conference um and um I'm first time I've been to UAE actually so that that's also good uh and the weather's rather good I looked just before I came out here the weather in London at it's three degrees so this is very satisfactory really so um so I'm going to talk um today about um well the

**1:06** · the methodology of machine learned potentials machine learned simulations which actually Mike mentioned in his talk so there's a brief introduction there and the applications I'm going to talk about are in um phase change memory uh and switching materials and uh bilga Iles gave a quite a good introduction

**1:28** · actually to to that um before she talked about her materials so that's also good um and um but the materials I'm going to be talking about are not crystalline mostly they're are glassier morphis and we haven't um heard too much about that there's a lot of Crystal work here but um Rajesh ganapathi talked

**1:48** · about glassy colloids which is also an introduction to this um so that's the sort of formal title but perhaps an alternative title might be what use is a really bad glass um and if you accept this is

**2:06** · actually what I'm going to be talking about you might then say well why am I here right talking to Advanced Materials conference really so I tried to persuade you during my talk that actually this these materials are quite Advanced and um and quite interesting um so before I carry on I'd just like to acknowledge the people who did the work um the group in Oxford v daringer

**2:31** · machine learn potentials and the molecular Dynamics associated with that colleague tyun Lee in Dau in South Korea uh hyper bonding model DFT calculations weang inian on molecular Dynamics um using machine learn Potentials mju in his group experimental group actually looking at selector devices I'll talk about those and uh Costas Constantino in Finland uh who did the work on defects

**3:00** · so my interests mainly um are to do with uh the effect of disorder on material properties uh and that leads you naturally to think about glasses and a more for solids and uh in order to understand their properties that particularly their functional material properties it is not just useful essential really to do computer simulations um because unlike a crystal

**3:25** · where you know absolutely what the uh Atomic uh position are of course and then you can s calculate in often really quite simplistic way what the properties should be from a crystal for a glass you know nothing about that um uh so you

**3:42** · have to do a lot of simulations and um I'm in the last five six years I've got very uh involved and interested in machine learned uh interatomic potentials for simulations and these are interesting because they're linear scaling um unlike DFT which is cubic

**4:00** · scaling so double the number of atoms you only double the time to do the simulations and the applications I'm going to be I very briefly mention silicon struction defects but most of the time on phase change materials and the materials I'm talking about torium and uh this geranium anoran

**4:18** · material okay so uh atomic structure of a glass what do we know if anything well probably there might be some short range order first coordination shell second coordination shell Bond lengths Bond angles pretty well mostly pretty well defined like a crystal possibly some

**4:37** · medium range intermediate range order going up to say 10 angstroms maybe preferred Ang ring sizes dihedral angles angular twist and so on definitely no long range order of periodicity because they're glassy so we

**4:52** · can only describe the structure in statistical terms using correlation functions there's no unique structure unlike a crystal and as I said before you need models really structural models in order to understand what the atomic structure is and then calculate what the properties are and understand them so you want to

**5:11** · do this modeling and you want to do computer modeling and you want the probably the best way to do it is using molecular Dynamics where you put the atoms in a box and they interact by some potential and you can give them energy you can do it to certain temperatures reduce the temperature whatever you want to do you can look at the Dynamics and you can look at the static properties um so you need a potential and the simplest way is

**5:34** · just using empirical potential Bond stretching Bond bending something like that it is simple it is quick and it's not accurate um you can go to The Other Extreme you could use as much quantum mechanics as you can get in using density functional Theory complex slow

**5:52** · cubic scaling uh but it's accurate within approximations on what the exchange correlation functional is and so on or you can have a compromise you can basically have what's one of these machine learn potentials which basically feeds off density functional Theory potential energy surface as I mentioned in a minute uh so you keep the DFT accuracy uh it's complex but it's quick it's linear scaling so how do you do this you have a

**6:21** · whole series of models thousands tens of thousands of small models with very very different configurations those configurations you think you might find in a molecular Dynamic simulation when you're going from a liquid to a glass or glass to a crystal whatever um and you um take all these models and you U do electronic calculations using DFT level um and you fit the potential uh the electron potential uh

**6:50** · your potential to the potential energy surfaces using some structural descriptor the one we used earlier was a thing called soap know about that so you describe the structure locally going out to maybe s 10 angstrum or so in terms of a general descriptor and then you map

**7:08** · your energy onto that descriptor and there are two ways of doing this you can use Neal Nets or Gan regression progression which what we used these potentials are linear scaling mostly because they have a spatial cut off for the structural descriptors right um and so that's one

**7:27** · advantage another advantage of the energy is actually the sum of the individual machine learned Atomic energies so you can calculate these things you can't observe them actually experimentally but you can calculate them and use them um so that's all good thing the bad thing is you don't get any direct electronic information out at all wave functions um so this gives you a timeline on where we've been doing in Silicon say um and before about

**7:55** · 2018 we could do TF DFT calculations on about 500 atoms Max 500 atoms could take several months on a supercomputer to do these calculations um 2 nanometer size first Gap model we had was in about 2018 allowed us to look at 4,000 atoms roughly order magnitude more um so this is DFT accurate but 10 times the size and then three L three years later we could make a model of 100,000 atoms DFT

**8:26** · accurate uh and then using this model which is now this one uh 13 nanometers on size is basically a teaching the next generation of potential which is this one um and we can go up to a million atoms a million atoms models all DFT accurate as accurate as this one 500 atoms so um that sounds quite good um

**8:53** · but you might say why big models apart from just bragging right well my model is bigger than your model right so um um what are the advantages uh well the advantage is that of course if you got a large number of atoms you can look at rare events in a statistically significant way I'll mention that in the next slide to mention here I'm going to talk about silicon in the next slide and um there are silicon is normally fourfold coordinated tetral sp3 bonding you have

**9:20** · some defect you have some three coordinate undercoordinated dangling bonds or you have five coordinate extra atom interstitial atom comes in so people knew about this not many of them fractions of a percent um but they didn't know what the geometry was everybody thought it's this floating Bond a tetrahedron with an interstitial uh silicon coming in actually we found in this million atom model that there are three types of geometrically different types of five coordinate um uh

**9:53** · defects which you can only find out if you got the statistics what what else might be interesting well if you're looking at um uh in this case this is pressure pressurized crystallization of a morphos silicon at 20 GPA you go to simple hexagonal silicon and look at this is this is 12 13 nanometers size and look at the size the crystals you generate of course you can't understand this crystallization here if you've only got a very small model basically and also there others too of

**10:23** · course you the bigger the model goes the the the um fewer um boundary effect there are size effects and so on um so uh hello at the back this doesn't seem to be working anymore all right it does good um so

**10:44** · this uh just one slide to show an advantage of these really large models a million atom silicon model uh I've mentioned these five coordinate uh defects and U there're only about 1% of them in 1 million at in the model there only 10,000 of these um overcoordinated

**11:04** · five units which are uh uh independent which are separate um so if you only got 1% and you've got a a DFT model of 500 atoms you've only got possibly four or five of these defects there you can't in the very small model you can't get any statistics here we've got 10,000 to look at but actually we found that most of them most of them are uh separate but

**11:28** · actually quite a lot of them cluster uh and you have clusters of two and you have clusters of three and you have clusters of four and in this million atom model we just found 2 only of these four coordinate ones right so we can look at these very rare events in these very large models um and this also slide

**11:46** · also shows the advantage of this this thing which you don't get in DFT you can't do this in DFT simulations actually ascribing energies particular type of atoms so here is the energy scale going from very low to very high and in this um um dier of these two five

**12:05** · coordinate uh defects uh this is the highest um Energy site which actually is the bridging uh silicon between the two 5f coordinate so we've got all this local information that we can get um this this clicker isn't working actually hello at the back could you just change the slide for me do you think yeah that's good um so I'm going

**12:36** · to talk from now on about these phase change materials which uh biller mentioned um and I should say if you do a Google search you might have done before this talk what's a pH phase change material um you find actually there are two meanings in the literature so caveat mtor here right uh I'm talking about phase change memory switching materials if you go down another Rabbit Hole you find that phase change materials refer to energy storage materials those like salt hydrates soan

**13:05** · fire sulfate or something where the latent heat stored or released phase transitions you just use as a heat Source basically these are nothing to do with these right so I'm only talking about these phase change materials here um sorry could you change again this is very boring actually thank you

**13:25** · um so what are the characteristics of the materials I'm talking about there are materials with very different physical opto electronic properties of the two structural phases uh these materials can be switched reversibly between phases U so we could go from a crystal to a glass to a crystal we could go from a crystal to a liquid to a crystal again in a sort of cyclic way um

**13:47** · I should say to going from Crystal to Glass which I'm going to be talking about you don't go directly you go from the crystal to a melt and quench the Melt to the glass and then you go directly from the glass to the crystal and obviously this you just go Crystal Liquid Crystal and there's no glass uh intermediate here um how do you do this two ways you could switch them by uh applying a voltage dual heating uh voltage or an short Optical pulse um and the point is that you can always melt a

**14:21** · crystal uh unbelievably rapidly right if you put a huge amount of power in a very short time you can melt in PE or seconds basically so the rate limiting time is not the crystal liquid or crystal glass and you can quench that liquid very quickly too um is that is not the rate limiting step in this process the rate limiting step is from the glass to the crystal the crystallization process um and mostly As

**14:49** · you probably know that's really quite a slow process right it could take seconds it could take minutes could be hours right in our case it crystallized in nanc crystallized in a nanc so this is what I mean a really bad glass it is very thermally unstable um and so we got two options we could have a meta metastable phases which is what we have here crystal glass Crystal or meta metastable and this will then form the Bas of a non-volatile

**15:19** · uh memory phase change Random Access Memory where you store uh Bits n and one in the structure so you're thought might be the uh Crystal which has got a high connectivity and your one might be the glass which has got a low conductivity um and this information is stored oh thank you very much indeed let's just try this yay look at that brilliant thank you very much indeed

**15:51** · um yeah so you store the uh information here not as electrons as in cosos devices um in Flash or something like that but as the atomic structure the atomic structure encodes the information um so that oops um I'm not used to it working now um the um so that's the meta stable

**16:13** · or you've got the transient phase actually this one here uh and this is volatile so you the the material only changes when you apply voltage to it so this is nonvolatile it remains off you switch the voltage off this is volatile it's only on when it when you you apply the voltage so the sort of materials we're looking at are in this Turner uh composition diagram between torium typically geranium antimony along this tie line between GT and SP2

**16:44** · T3 canonical composition is this 225 composition here right um all these are congruent melting actually the composition doesn't change when it melts because we're going through the Melt from going from the crystal to the Melt to the glass and back again so we don't want the stuff to face separate which it does not um the stable Crystal form of

**17:05** · these materials is actually hexagonal but we don't crystallize on time scale of hours or minutes we crystallize in nanoseconds and so you got a metastable crystal which is rock salt actually this cubic phase which is stabilized by having vacances in it so the motifs for rock salt remember are for Rings cubes 90° angles edal sixf coordination right so you'll see those come up in a minute and these meta stable phases glass is um

**17:37** · semiconductor resistive let's call that reset State this cubic structure crystalline is conductive because it's actually um degenerate semiconductor pretty metallic actually uh so this is the on state if you like um conducting State and this is the off State um and these are very simple

**17:58** · device they're two terminal devices you have a top electrode a bottom electrode your magic material in between and you apply these short voltage pulses to switch the material between Crystal to glass or back again uh and here they are in a uh 3D Cross Point array so these

**18:16** · blue lines are electrical conductor lines uh these are um the um word lines and these are the bit lines so you apply voltages the blue conductors here um and then if you've got a selector here switch which I'm going to talk about a bit later on uh you can switch on or off individual pixel here individual memories um and these memory units are what I've just been talking about so these were commercialized a few years ago by um Intel Micron um using this um

**18:49** · uh geometry here and it's faster higher density than nand memory um so let's just talk in one or two slides about at the atomistic level write down at atomistic level what this stuff looks like here's this composition geranium anomy torium 225 um and here's

**19:11** · a DFT model as it happens uh we Analyze This to finding out what the coordinations were normally in this business what you do is to say what's the first coordination number you sit on an atom geranium and you have a cut off and say what how many atoms of what type are within this spatial cut off

**19:29** · and in some case like silica that works really well because there's a really big uh minimum between the first and second peaks in the correlation function here there's no minimum it's rather arbitrary what you take as a cut off so we didn't use cut offs we used to say actually since we know everything about the electrons in this system um is there actually a bond between a given origin

**19:50** · atom and its neighbors based on thing called the electron localization function basically what the electron density is is there a bond or is there not a bond no um and if there is a bond where is it or a loone pair and what you find is the following so for geranium you find as you might expect tetrahedr geranium no lone pair so this is four means number of uh lians and zero is the number of Lone pairs so tetrahedral normally expect but there's another type of four coordinate geranium 2o which is this one

**20:22** · which is defective octahedral with 180 90° Bond angles so it's an octahedron missing two neighbors uh and you also see this dangling Bond basically is three coordinate janian you antimony you see similar defective octahedral sites four and five uh no tetrahedral ones but this trigonal one too and torum what you might expect twofold coordinated but also three coordinate um so actually quite a zoo of

**20:52** · um of uh local coordinations and importantly remember this stuff crystallizes in a nanc or so you don't have time in a nanc for atoms to move a long way to find the local Crystal minimum they've got to find it very very quickly and they do it because many of the my God sorry many of the uh atoms in

**21:13** · the glass are already pretty crystalline like remember rock salt crystal is octahedral and here these units are all in the glass are already fairly octahedral so just to blow up this is what you see we see these units here um defective octahedral sites they look a bit like a seesaw here's a seaw remember like Charles seesaw uh here's the plank and here's the fulcrum these bonds here are long weak

**21:44** · and strongly polarizable and we believe they are basically uh three Center four electron so these are not normal calent bonds these are three Center one two three four electrons distribute over those and these are nor coent bonds here because why do I say that if you look at say four here um these are baby electron

**22:08** · oet rule so I've got uh four bonds each with two electrons four twos are eight right uh here I've got three bonds three TW are six plus a lone pair of two 6 plus two is eight all these arey electron octet rule but these things like 41 or 51 don't because I've got four bonds four to four twos eight plus another two pair 10 electrons in this unit right that is not not obeying octet

**22:34** · rule it looks as if you have hypervalency actually the bonding is RA is this rather special hyper bonding which I'm not going to talk more about here but talk later if you want um so just to then say that this glass in the glassy state it contains many crystallite like units here they are right in the glass already so youd only need one or two atoms to move a very small distance to then make this you know a crystal nucleus basically so this was our first um the

**23:07** · first our first uh Gap uh machine learned potential ging approximation potential for GST 58,000 configurations it was trained on uh it's linear scaling it's DFT

**23:23** · accurate you can build as we did there about a couple of years after it was um made made in 2018 2020 we've made this 25,000 atom model uh which we're quite pleased within but of course this is rapidly looking rather small now so uh and this potential is transferable it was trained basically on lots of different compositions this is 225 but you can make G you can make SP2 T3 with it it's a sort of generic potential another advantage of this um

**23:55** · very fast potential is that you can make either quite a really big model in a reasonable length of time or you can make lots of smaller models in a very short time so you might say why do I want to make an ensemble of 30 atoms 30 models each of sort DFT size 315 atom

**24:16** · when you can make something as big as this point is you cannot do a proper DFT calculation electronic calculation on something this big you can only do it on very small models so to get around this let's make lots and lots of them an ensemble and look at the statistics of this and that's what we did so we took 30 models of this 225 um and we found uh this rather

**24:43** · interesting Pat surprising Behavior so in the old days it might take you six months just to make one model 3155 atom model 6 months for 300 let's say you get this you write a PRL there red letter paper saying there are no Gap States in GST in my DFT models right somebody else does another

**25:05** · model and they say yeah there are Gap States right um so what you believe well actually what we found was you know 60% of the models actually have no Gap States 37% do so it gives us some idea about the statistics of these things um so that

**25:20** · was quite interesting uh and then we started to analyze so what is this Shing this is the density of States this is the veilance band here's the gap here's the conduction band and you know these two models got basically the same band Gap but they differ by having this state deep in the Gap here um so let's look now at a particular

**25:42** · model uh here's the veilance band again here's the conduction band density of States here's a state deep in the Gap and I'm also this is the density of states in Black I'm also showing the calculated what's called inverse participation ratio which basically tells you what the localization of electrons is at a particular site so when this red when this number is very big it's very localized and when it's small it's delocalized so small values deep into

**26:14** · the band delocalized States just as you have in a crystal except these are not block states of course this is glassy of course but at the band edges and particularly in the middle you have very strongly localized States um so due to Disorder so what does this

**26:33** · Deep Gap State look like it looks like this actually it's rather complicated it's not as simple defect at all as you have in Silicon say where you just have an undercoordinated or overcoordinated atom this is very complicated the wave function which is in green here basically you can see spreads all over here and it's centered on a germanium which is five coordinate and there's another one here actually which is even six coordinate um this crystall likee

**27:02** · little bit of glass seems to be the host for this deep State here um so that's the Deep Gap State uh which are localized what about these uh shallow that is banded states which are also quite localized what they look like they look completely different they are

**27:23** · small chains of these hyper bonded seesaw units okay so here's a seesaw unit here's another seesaw unit right here's the fum here's the here's the plank um these are the geranium atoms here these are conduction band State these are all conduction band States uh these are uh from The Gap model uh and this is from a DFT model so you can see the same in DFT or in gap and the same

**27:51** · at the veins band edge2 um so why is this interesting well because um when you do the um uh transformation from a crystal to a glass or vice versa you apply very high voltage only one volt but it's over

**28:11** · maybe 10 10 20 nanometers so exceedingly High field for a very short time and you pump loads of electrons and holes into the system and it heats up of course but the electrons and holes can be themselves trapped and this is what how they can be trapped so oh my God sorry um this is a conduction band State bottom the conduction band um and this this is what you find in the glass right you then add one electron to the model and this electron is trapped by this uh this

**28:42** · is the uh highest occupied uh sorry uh yeah the highest unoccupied State uh so lumo basically lowest yeah the lowest unoccupied State um and this

**28:58** · is trapped in this region here and you can see this Bond here has got a bit longer and you send another electron in so it's two electron trap uh and each should break this Bond right so two electrons break a bond here here is a veence band State top of the veilance band uh states are localized in this uh

**29:19** · and you trap one hole and again bonds get a bit bigger two holes it also breaks so actually this is eventally a self tra bio uh um scenario basically so these states can trap electrons and holes quite easily and that has a impact on what the conduction process is

**29:44** · um seem to be jinxed here actually just try and go back can you do go right okay um so um that was then now is now so we've got a latest uh machine learn potential GST

**30:07** · based on a different structural descriptor an atomic cluster expansion and it's three orders of magnitude faster than what we had before so we can now simulate million atom models for 50 NS and we actually tested uh a billion atom at DFT accuracy and we can find that actually you know we can have a reasonable number number of time steps just actually on just eight nodes basically um so uh timing doing the

**30:35** · calculations is not a problem actually storing the data from an MD simulation of a billion atoms um is actually what we the limiting Step at the moment basically we just don't have enough memory to do this but we can we've done million and we can do a billion um just

**30:52** · let me skip that so this is the application so here is a blur up of that Cross Point uh memory array I showed you earlier on here are the word and bit lines here's the memories here with a n and a wand stored in it here it is again here's the switch here's the uh GST uh memory element and typically this is 20 by 20 by 40 nanometers in a real device

**31:17** · so we want to actually do a device level simulation here it is here actually is a model of 20x 20 by 40 and this is what we start with single crystal in here logic State one uh and we apply heat to it uh and we just melt it and depending on how fast we do it this melts in about 50 p a seconds so this is the initial reset process going from Crystal to melt and then if you quench that down equally in the S similar time it can go to the glass here we are in the glassy State um and we are

**31:49** · heating it up um and this is how long it takes to crystallize 20 NCS which is what the experimental time scale is um in this device size box basically and you can see that it starts with a glass and you end up with a poly Crystal and then so this is logic 81 and then we can heat this up again and melt it and so on go around around the loop so we can do simulations at the device scale uh and this is uh half a million atoms doing this 500k all at DFT

**32:22** · accuracy um I have another slide please thank you um so how do these things crystallize there are two ways of crystallizing one is that um the blue is uh the glass here

**32:41** · yellow are the crystals um you could have a sort of spontaneous homogeneous nucleation here that the you have to have a certain number of atoms forming little Crystal nuclei before they start to grow this is nucleation driven um and you get lots and lots of very small CST crystals or or it could be growth driven

**33:01** · that basically uh often is templated out from some interface uh and growth is the uh limiting step not nucleation and this is interesting and important because these the rate of these rate of nucleation or rate of growth occur at different temperatures uh so if you are at a temperature here you just uh will nucleate more than you grow and here you

**33:24** · uh will grow more than you nucleate and so we did the same sim in this device size thing uh crystallizing at 550k here uh and you can see this this this is starting at 3 nanc it start on a morphos right 3 nond you're starting to see uh the nuclei form and you form basically a polycrystalline array with very very small crystals because this is nucleation driven if we then anal at not

**33:52** · at 550 but 650k we're here now and we're in the growth limit there are very few new well basically no nuclei here forming and eventually as soon as you form one the thing just grows so you get a completely different morphology depending on what the temperature is and people knew this I

**34:10** · mean people know that crystallization behaves like this but nobody's actually seen it in simulations before and you can only see it at this sort of size because look at the size of the crystalites here they're comparable basically to the size of our box um uh the next slide please thank you um so the last one I want to talk about this uh is uh bilgo mentioned uh

**34:34** · neuromorphic uh brain light Computing basically where you don't just have binary bits not one you have a Continuum States going in our case going from 100% glass to 100% Crystal continuously and you can have a cell like this where basically uh this is all crystal and you're just making a dome or mushroom of glass uh and it gets bigger and bigger and bigger and of course these have different um different um conductivities

**35:03** · so you have a continuous range of um conductivities but depending on how much you program this region here so this is typically what they look like 100 by 100 by 40 nanometers in a real device uh we can't do that at the moment uh so we took a slice the area is Right

**35:22** · 100 by 100 but then we took a 5 nanometer slice through the middle uh that's all already nearly a million atoms actually 800,000 atoms uh and this is what it looks like and we can program different regions so uh we can here's a single Crystal and we can melt it uh and then recrystallize and we have a more uh a bigger amorphous region and we can crystallize that as well so we're now looking at this this um way of of of

**35:51** · trying to store more data basically in a continuous way here and I should say while you're looking at this people thought up to now that this device was only determined by the proportion of Crystal conducting Crystal to resistive

**36:09** · glass that you had just that ratio actually that can't be true it is parly true of course but it can't be only true because you got these poly crystals here with all these grain boundaries and you can control the grain boundary size by what the temperature is your crystallization so these grain boundaries also have their own uh resistivity uh behavior and that's an extra level of control that you can

**36:33** · have I've talked about memory I now want to talk about the switch because without the switch you can't just write individual memory cells here and in the devices that are be used uh um at the moment they use these rather complicated uh chalcogenides um and the on state here is just an electronic effect it's just electron trap fills um we discovered two or three years ago

**37:03** · that actually you could do it with an element single element torium uh and that switches so here you have a top electrode tium nitride a bottom electrode tum nitride here's torium about you know 10 nanometers thick um and this is what happens when you apply voltage first time uh is you're in the uh crystalline state it is semiconducting uh and about initially about two three Vols then suddenly you melt the torium and molten torium is a

**37:32** · liquid torium is a metal uh you suddenly switch on this very highly conducting State here so it looks here a negative differential resistance you don't you're just switching from One path to another so this is off semiconducting Crystal this is on the metal and of course when you switch the voltage off again the liquid crystallizes and you go back to the on state again so you can see the very first time you do it you need a Thresh control voltage a fire voltage about 3 volts subsequently second third

**38:01** · fourth you only need about one volt right why which is good but why this difference um and this so this this just shows you you won't be able to see can't even see it here right at the back but this intermediate State the on state here we've done Institute TM and actually you do see that the stuff melts and then crystallizes again to a poly Crystal having started as a single Crystal

**38:29** · um sorry um so we did a simulation of this um so this is the original on state single Crystal here and you need a threshold voltage to uh melt it so this is what we found in the simulation this is a 100,000 atom uh simulation here uh

**38:49** · using this Ace potential uh and the stuff melts at about 723 Kelvin uh look at the mean Square placement nothing happens it's in the crystal solid and then it suddenly melts here this happens to be amazingly the experimental melting temperature right so we can reproduce the experimental melting temperature starting with a single Crystal so we have the Melt and then we quench the Melt uh and what you end up is a poly Crystal now and this let's do the cycle again let's heat the poly Crystal up um

**39:20** · and what happens is that actually lots of grain boundaries the stuff melts at a much lower temperature like 200° lower than the single Crystal um and uh at 500k rather than 700k so a lower melting

**39:35** · temperature it means you need a lower power you need a lower Vol threshold voltage in order to melt so we believe that this transition from this high voltage to this low voltage uh is simply due to the fact that you have this grain boundary induced melting uh subsequently for all these states here um

**39:58** · I would tell you something else if I could change the slide again right here we go um how much time are we got do you want me to stop it says 1 minute 30 I've got let me just very very briefly talk about again tum crystaline torium is a chain structure helical chain structure and it could have a helix this way right hand or have a helix this way left hand these are chyal they're not trans superimposed

**40:27** · posable um so the question is how does chyal torium crystallize um and it's been proposed in a long long time ago that maybe there's a cubic intermediary you have a cube which is symmetric and you squeeze it in one way then you actually get three short and three long bonds uh or squeeze another way you get three short long bonds another way and actually you can generate these helices through this cubic intermediary um and and we did a simulation just to

**40:58** · see this so here we have 100,000 atom model of the uh glass um and basically nothing happens really for about a nanc and then we start to see something happening and we see some nuclei we look at them lo and behold these are cubic motifs coming up cubic motifs right so

**41:18** · between one and three NCS basically these cubes appear more and more and then suddenly for nanc you go from cubes to chains switches um and these then chains just grow more and more um and uh so these are chain structures uh showing where the the the

**41:39** · where the crystals are so crystals here and grain boundaries here this is colorcoded to show you what the type of cality is are they left or right and you can see that actually you're getting both right and left forming in equal proportions here so this is all crystallizing at 300K um and then if we uh just carry on from that state if I can show you uh next slide

**42:04** · please thank you uh if we then increase the temperature to accelerate things uh and look at what happening these grain bound grains get bigger and bigger grain bars get smaller and smaller and we end up with just two grains in our humog model one right one left reic mixture um and it's quite interesting

**42:25** · what's happening you get in chyal transfer grain boundaries here's a grain boundary between right and left stuff in the middle and you get a statistical fluctuation you get these cubes formed uh and then basically this blue then just grows through the red region or

**42:40** · alternatively you could have happening within a grain you could have these chains here moving this way you got a fluctuation you get some cubes formed again and then actually you get um a completely orthogonal growth of the other type of chanity right so I should stop I've got 35 seconds so I'll let you read thank you very much indeed for your time thank you thank you um any

**43:11** · questions anybody Stephen I think that's absolutely fascinating talking it it um we do very similar things and we're always pushing up against the boundaries of how many atoms you have in your models yeah so with your DFT you talked

**43:29** · about having 3155 atoms and doing 30 variations of that yeah if if you if you go to more atoms or less atoms do you see a difference like can you have you tried it going because you it sounds like you can get up to 50,000 or 500,000 atoms so if you went to like 100,000 rather than 315 is that possible with theft now or not yeah yeah yeah yeah well we can we made um to answer your point that was then I give you s timeline that was then that's all we could do then right yeah yeah so uh so um but we know we we do

**44:02** · need to uh look at small model I'll just come back the bottom bit talks about that but we've done um multiple models of this million atom silicon model for instance right yeah not 30 but three or four and you know and they behave exactly the same so um you know you already got economy of scale basically

**44:20** · okay a million atoms but actually you have to worry well am I getting trapped at a particular local minimum here but not really no so um but but the problem is we have these humongous models and if if you look at Atomic properties that's okay if you look at electronic property is not okay because all we can cope with are 300 out of Model right directly so what we've done is that uh in this paper uh that's referred to here we've done machine learning not of only of the potential but of any other property particularly the electron density States okay so we

**44:53** · machine learn and we can then so let me ask one more question then so I think you had slide where you compared the DFT with the machine learning yeah and you had a graph with a number of atoms and I can't remember what was on the vertical axis but it looked like there was a difference for the same number of atoms you had a difference in energy or I can't remember that would be it's kind of like right in the middle of your talk

**45:16** · right um quite far back far back sorry the crystallization um I can't think what that was uh that's it there that one that one there okay you had the blue curves so it's oh yeah yeah okay well this is just telling you how fast sorry that's all speed okay speed of the thing right there's your thousand atom speed up right so uh for a million atoms Gap

**45:42** · oh my God uh million atoms for Gap uh that takes this time up here uh and um for the other thing you can just do it in red right basically so but the actual magnitude of the energies or whatever you get out of the same the same yeah yeah yeah it's DFT accurate whole thing is DFT accurate fascinating thank usually the fitting is to what one me or something yeah it's about two M

**46:09** · okay um the business you showed about the nucleation of the left and right-handed and the grain boundary that is effectively a Solon so it doesn't require a lot of energy to move and that's why you eventually see yeah yeah yeah yeah if you use a onedimensional model or a few dimensional models it maps onto a silic Solon Solon that's cool yeah we found that actually you're only 90 uh me per

**46:41** · atom higher in the cube than you are in the chain actually so it's a great it's a great you know you do go through this but it's a very low barrier actually so yeah any other question thanks stepen lovely to when you were referring to the temperature and the correlation with the switching time yeah is that current driven what the voltage you said a

**47:08** · certain voltage is needed yeah yeah that that's thermal thermal oh yeah absolutely everything's thermal yeah yeah yeah yeah actually both for the um for the memory it's thermal um so we're going from the crystal we melt it switch the pulse off get to the glass got the glass go to the crystal you you heat it all voltage dual heating same with the tarium switch just the same yeah yeah thank you last

**47:45** · question yeah very nice talk I have just one question uh what is the switching time when you talk about the neuromorphic uh Computing application for this kind of material what's the switching time switching time and what what what what what things limit the switching time for this neuromorphic complications yeah sorry the last B your question what limits the switching time and for the neuromorphic comp yeah yeah

**48:10** · well neuromorphic is just like the other thing actually it's except you have this continuous range of glass to Crystal right it's not 100% 100% continuous range so you still worrying about how long it takes to switch between a crystal and a glass right that's the limiting stage and it's material limited as I've shown you here like 10 NC 5 NCS doesn't matter it's neuromorphic or or or um flash type we found that actually about 10

**48:38** · years ago I suppose um if you can prime the material you send in a small voltage which is not enough to switch it but it actually nucleates material and then we showed that what was it about 50 Peak a seconds we can switch it actually um so it's a more complicated pulse sequence but um but that gets around the intrinsic material limitation so this material is quite fast actually 5 NCS to crystallize is pretty fast but

**49:06** · um and it's certainly fast enough for Dam replacement actually so we've got a nonvolatile answer for for Dam so you know we talking about sustainability means you don't have to boot up your computer right you know it's always on basically and so okay okay uh let's thank Stephen and we'll move on to the next speaker