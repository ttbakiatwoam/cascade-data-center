# Data Center Workload Types

> This file is technical background, not a statement that the proposed Cascade facility will perform every workload described here.
>
> Last reviewed: 2026-09-10

## Why workload labels matter

“Data center” is an umbrella term. Cryptocurrency mining, AI/HPC, cloud hosting, colocation, enterprise storage, and conventional server workloads can use substantially different hardware and facility designs. A valid local-impact comparison should therefore focus on the physical design and operating envelope, not the label alone.

## Cryptocurrency mining

Typical proof-of-work Bitcoin mining uses purpose-built ASIC hardware. Important facility characteristics include:

- large, relatively steady electrical load;
- substantial heat generation;
- air-cooled, hydro/liquid-cooled, or immersion-cooled miner designs;
- potentially large fan arrays where air cooling is used;
- workload that can often be curtailed more readily than latency-sensitive cloud services;
- comparatively modest networking requirements per MW compared with large AI training clusters.

Simple Mining's public business is specifically Bitcoin-mining hosting and support.

## AI and high-performance computing

Large AI training/inference and HPC environments increasingly use dense GPU/accelerator clusters. Relative to conventional hosting, these can require:

- very high rack power density;
- direct-to-chip or other liquid cooling at high density;
- high-bandwidth, low-latency interconnect fabrics;
- substantial storage and data movement;
- power-delivery designs optimized for large synchronized compute clusters.

Meta's infrastructure publications are useful examples of how hyperscale AI clusters differ from a containerized Bitcoin-mining proposal, but Meta facilities should not be treated as direct Cascade comparables without matching scale and design.

## Cloud, colocation, and enterprise hosting

These facilities often emphasize:

- redundancy and uptime;
- diverse fiber/network paths;
- UPS and generator systems;
- security/compliance;
- mixed server/storage/network equipment;
- varied customer utilization rather than one uniform compute workload.

## The variables that matter locally

For zoning and community-impact analysis, the most useful variables are:

1. maximum and average MW;
2. heat rejected to the environment;
3. fan and mechanical-equipment noise;
4. water consumption and discharge;
5. cooling and heat-rejection design;
6. backup generation and fuel;
7. UPS/BESS configuration;
8. site footprint, setbacks, screening, and lighting;
9. road and construction traffic;
10. permanent staffing;
11. expansion rights and maximum buildout.

A change in customer or workload is primarily a local concern when it changes one or more of those physical impacts.

## Sources

- Simple Mining — Documentation: https://docs.simplemining.io/
- Simple Mining — Hosting: https://www.simplemining.io/hosting
- Meta Engineering — Meta's Infrastructure Evolution and the Advent of AI: https://engineering.fb.com/2025/09/29/data-infrastructure/metas-infrastructure-evolution-and-the-advent-of-ai/
- Meta Engineering — Building Prometheus: How Backend Aggregation Enables Gigawatt-Scale AI Clusters: https://engineering.fb.com/2026/02/09/data-center-engineering/building-prometheus-how-backend-aggregation-enables-gigawatt-scale-ai-clusters/
- Meta Engineering — Maintaining Large-Scale AI Capacity at Meta: https://engineering.fb.com/2024/06/12/production-engineering/maintaining-large-scale-ai-capacity-meta/
- Meta Engineering — MetaRoCE: A New RDMA Transport Built for AI-Scale Ethernet: https://engineering.fb.com/2026/08/24/networking-traffic/metaroce-rdma-transport-ai-ethernet/
