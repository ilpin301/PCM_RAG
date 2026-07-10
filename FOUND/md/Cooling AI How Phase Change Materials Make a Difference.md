---
Title: "Cooling AI: How Phase Change Materials Make a Difference"
Author: "SINTEF Energy Research (Juan M. Corberán, Arash Nemati)"
Reference: "https://www.sintef.no/en/latest-news/2024/cooling-ai-how-phase-change-materials-make-a-difference/"
ContentType:
  - "article"
Created: 2026-05-25
Processed: true
tags:
  - "source"
---

SINTEF blog post about PCM-based thermal energy storage (TES) for data centre cooling. Part of the EU La-Flex project. **Not about electronic/photonic PCMs.**

## Key Claims

- LLMs use ~700,000 kWh/day worldwide; data centre cooling consumes up to 50% of total power.
- Generating 10–50 AI responses requires ~500 mL water to cool the data centre.
- Norway: 18 data centres; 6 in Oslo; new regulations require cost-benefit analysis for waste heat utilization for centres > 2 MW.
- PCM-TES: stores 4× more energy per volume than water (latent heat vs. sensible heat); offers precise temperature control at phase-change point.
- La-Flex project: SINTEF leads EU consortium to develop PCM-based cold storage unit (Cartesian AS) for data centre cooling; DTU, AI-nergy, THWS, KLP Eiendom as partners.
- **Peak shaving**: PCM-TES reduces electrical grid load during demand peaks.
- **Ancillary services / frequency regulation**: PCM-TES can respond to grid frequency changes to absorb/release energy, creating revenue opportunities.
- Immersion cooling and waste-heat-to-district-heating also under investigation.

## Why cooling is critical for the future of data centres

How many times have you written a prompt to ChatGPT or any another AI? While our human brain can answer many questions [by using an average of 2 kWh/day](https://doi.org/10.1109/MSP.2022.3182938), large language models (LLMs), like ChatGPT, [use about 700,000 kWh/day worldwide](https://doi.org/10.48550/arXiv.2305.03123), a consumption that is expected to grow exponentially in the coming years. This huge amount of energy is consumed, mainly, by data centres, whose use and prominence in society has been growing considerably after artificial intelligence (AI) became a daily-use tool worldwide.

Data centres are in practice low-efficiency electric heaters, generating large amounts of heat. This heat must be removed in order to maintain fire safety and ensure optimal performance. This heat generation results in an [electrical cooling demand that can range from 350 to 2,500 kWh/day](https://doi.org/10.1016/j.energy.2022.125495) depending on the geographical location and the cooling system. When it comes to the electrical demand of a single centre, on average, the cooling system requires up to 50% of the power consumption, as illustrated in the figure below.

![[5d2331d7a9ccd59b3df301f495a407da_MD5.jpg]]

Power consumption by different components of a data centre. Source: Data Center Energy Consumption Modeling: A Survey.

Just as our brain needs water to function, so does ChatGPT: [generating 10-50 responses requires 500mL of water](https://doi.org/10.48550/arXiv.2304.03271) (a typical bottle) to cool the corresponding data centre. This leads to huge volumes of water, among other resources used in refrigeration, to address all the waste heat in data centres worldwide. AI, and LLMs, are great tools, however it is also our responsibility to make them sustainable, and thermal management and excess heat utilisation are key in this process. Excess heat from data centres should be utilised, for example in district heating or nearby industrial processes with low-temperature heat demand.

Since global warming is making the thermal management even more challenging (especially on the cooling side), regions like Scandinavia are experiencing rising requirements for refrigeration systems in data centres. There are more than 11,000 data centres in the world, of which 18 are located in Norway (see the map below). Many more are expected to be built in the coming years. Given this trend, the Norwegian Ministry of Energy is working on regulatory changes that will require all data centres over 2 MW to conduct [cost-benefit analyses for utilising excess heat](https://www.regjeringen.no/no/dokumenter/etablering-av-datasentre/id2971352/?ch=1). In this context, innovative thermal solutions are essential for achieving sustainable and cost-efficient waste heat management in data centres, where **efficient and sustainable cooling is no longer optional but a necessity.**

![[56c89971fa5bf14a332c6718d01d53b7_MD5.png]]

Data centre distribution in Norway. Source: Kommunal- og moderniseringsdepartementet. Datasentre i Norge: Ringvirkningsanalyse av gjennomførte og potensielle etableringer.

## The limitations of conventional cooling in data centres

Currently, most data centres in Europe rely on airside and waterside free cooling systems to manage waste heat. These technologies depend on several factors to ensure cost and energy efficiency, such as outdoor temperatures, the quality and availability of air and water, the integration of electrical cooling backup systems, and available space. However, the challenges in maintaining precise temperature control, along with the reliance on electrical sources, limit the flexibility of both airside and waterside cooling systems, reducing their adaptability to the energy grid.

Thermal energy storage (TES) is a well-established technology that can enhance system adaptability and improve flexibility. TES works by storing heat or cold when it is available or generated at low cost (through power-to-heat solutions, for example) and releasing it during periods of higher demand or when generation costs are elevated.

One of the most widely used TES technologies is hot water tanks, also known as buffer tanks. However, these systems have two main limitations: the difficulty of maintaining precise temperature control, and the challenge of meeting their large volume requirements. In thermal management, it is particularly important to have precise temperature control to ensure that heat and cold are stored and provided at the desired input and output temperatures. For data centres, minimising the footprint of all involved technologies is crucial for efficient space utilisation, especially since data centres, while well-distributed globally, tend to cluster within small, densely populated areas within each region.

![[8d094c29c35d8969ea0b20769d90983d_MD5.png]]

Spatial concentration of selected industrial facilities compared to data centres in the United States. Source: World Energy Outlook 2024, IEA.

This concentration brings additional challenges. For example, in Norway, 6 of the country’s 18 data centres are in Oslo, where 20% of the national population resides. This high-density setup, noted by the International Energy Agency (IEA) as characteristic of the data centre industry (as shown in the figure above), intensifies the strain on both resources and space. In densely populated areas, the limited availability and quality of resources—such as air and water for cooling systems—can complicate effective cooling, underscoring the need for more compact and resource-efficient technologies. In these settings, alternative solutions with smaller physical footprints and greater adaptability, such as (PCM), become especially valuable.

## The PCM revolution: Compact and efficient data centre cooling

PCMs are materials that absorb and release large amounts of energy (latent heat) as they transition between solid and liquid states, making them highly effective for energy storage. PCMs can store thermal energy at a much higher density and within a narrower temperature range than sensible heat storage mediums (like water), providing solutions that are up to four times more compact. This compact nature makes PCMs an ideal solution for data centres. PCMs offer precise temperature control since they store and deliver heat/cold at a constant temperature (which corresponds to the solidification or melting point of the material used).

With their ability to provide fast thermal response, PCMs can quickly adjust to changes in temperature, ensuring that data centres operate within optimal temperature ranges while minimising energy consumption and reliance on electrical cooling systems. This makes PCM-based thermal storage an effective solution not only for reducing operational costs but also for making data centres more sustainable and flexible in their energy usage.

SINTEF Energy Research leads an EU-partnership project, [La-Flex](https://www.sintef.no/prosjekter/2024/la-flex/), focused on exploring how PCMs can revolutionise cooling in data centres. By integrating PCM-based TES systems, data centres can harness the advantages of both flexibility and efficiency, significantly reducing their environmental footprint. These systems allow data centres to engage in *peak shaving*, which helps balance electricity demand. We saw that data centres have an exceptionally high spatial concentration, having significant implications for local power grids. Therefore, this strategy not only reduces operational costs for data centres but also alleviates pressure on the electrical grid, contributing to a greener energy system overall.

**Peak shaving** is the practice of reducing electricity consumption during periods of high demand to lower energy costs and alleviate strain on the power grid, often achieved through energy storage, load management, or on-site power generation.

PCM-TES systems offer another interesting possibility: to participate in ancillary services\* markets, helping to stabilise the grid while creating new economic opportunities. By providing flexible cooling capacity on-demand, data centres can respond to grid imbalances caused by renewable energy variability, such as wind or solar fluctuations. Through the La-Flex project, we are testing how this integration can support the grid by delivering fast response services like frequency regulation\*\*, following the strategy described in the graph below.

By participating in ancillary services, data centres can earn additional revenue while supporting grid resilience and enabling a cleaner, more efficient energy ecosystem. As this technology matures, it has the potential to not only optimise the operation of data centres but also to contribute significantly to the broader transition toward sustainable, flexible energy systems that integrate thermal storage. This sets the stage for a future where data centres play a key role in energy flexibility, offering both environmental and economic sustainability, which will become a requirement for large-scale centres, as Norway’s newly adopted regulations demonstrate.

![[9ac05866b4ef78d7e9a5b4955adc115e_MD5.png]]

Frequency regulation strategy. The cold TES unit is charged or discharged in response to an increase or decrease (respectively) of grid frequency taking advantage of the rapid response time of PCM-based TES technologies. Source: Battery Energy Storage Applications: Two Case Studies.

**\*Ancillary services** refer to the support services provided to help maintain the reliability and stability of the power grid. These services ensure that electricity supply and demand remain balanced, voltage levels are controlled, and the grid can recover from disturbances.

**\*\*Fast response services** like **frequency regulation** are a specific type of ancillary service that helps stabilise the grid by quickly adjusting the balance between electricity supply and demand. When there is a sudden change in frequency (caused by supply-demand imbalances), systems with fast response capabilities, like those used in PCM-TES, can rapidly adjust their energy output or absorb excess energy to restore the frequency to its optimal level. These services are critical for integrating variable renewable energy sources like wind and solar into the grid.

## The future of data centre sustainability: PCMs and beyond

The [La-Flex project](https://www.sintef.no/prosjekter/2024/la-flex/) represents a significant step forward in enhancing the sustainability of data centres cooling systems. Through this initiative, SINTEF Energy Research will lead and coordinate the development of a PCM-based cold storage unit, which will be delivered by Cartesian AS, a SINTEF spin-off. This cutting-edge unit will undergo detailed analysis at DTU (Denmark) to evaluate its applicability in data centres. Furthermore, AI-nergy in Denmark will explore how the technology can participate in ancillary services, while THWS in Germany will conduct a comprehensive techno-economic assessment to understand the feasibility and potential impact of the technology. Other partners from the building sector, such as KLP Eiendom (Trondheim) will follow up the project.

La-Flex showcases an innovative solution, but it is just one of SINTEF’s many approaches to making data centres more sustainable. In addition to PCM-TES, SINTEF is advancing technologies such as [immersion cooling](https://www.sintef.no/en/latest-news/2024/revolutionizing-data-center-efficiency-with-next-gen-cooling/), which submerges electronic components in a thermally conductive liquid to improve cooling efficiency dramatically. Moreover, SINTEF is investigating other sustainable refrigeration methods, such as [reusing waste heat to support district heating networks](https://blog.sintef.com/sintefenergy/this-is-how-we-reduce-data-centers-carbon-footprint/).

As data centres continue increase in number and energy demand, the need for innovative and efficient thermal management solutions will only grow stronger. With La-Flex and other initiatives, SINTEF is at the forefront of creating technologies that not only optimise energy use but also contribute to a more sustainable and interconnected energy future.

![[3acbcbc4bd88ae16b55b8574963a8e69_MD5.png]]