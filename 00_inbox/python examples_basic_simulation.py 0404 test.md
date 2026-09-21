
@shimojok ➜ /workspaces/M3-BioSynergy (main) $ python examples/basic_simulation.py

======================================================================
M³-BioSynergy: Extended MBT55 Simulation
Ecological Hypercycle Theory Implementation
======================================================================
======================================================================
M³-BioSynergy: MBT55 Ecosystem Simulation
======================================================================

--------------------------------------------------
1. Microbial Diversity Simulation (120 species)
--------------------------------------------------
/workspaces/M3-BioSynergy/src/core/microbial_diversity.py:154: ODEintWarning: Excess work done on this call (perhaps wrong Dfun type). Run with full_output = 1 to get quantitative information.
  solution = odeint(system, initial_population, t)
   Final Diversity Index: 4.403
   Total Microbial Biomass: 8 units
   MEI (Microbial Emergence Index): 94.865
   Hypercycle Formed: True

--------------------------------------------------
2. Hypercycle Dynamics Simulation
--------------------------------------------------
/workspaces/M3-BioSynergy/src/core/hypercycle_engine.py:84: RuntimeWarning: overflow encountered in scalar multiply
  next_state[i] = current[i] + (growth * (1 + coupling) - loss + external) * dt
/workspaces/M3-BioSynergy/src/core/hypercycle_engine.py:84: RuntimeWarning: invalid value encountered in scalar subtract
  next_state[i] = current[i] + (growth * (1 + coupling) - loss + external) * dt
   Amplification Factor: nanx
   Self-Sustaining: False
   Hypercycle Efficiency: 0.000

--------------------------------------------------
3. Nutrient Cascade Simulation
--------------------------------------------------
   Total Humus Formed: 593.0 kg
   Carbon Use Efficiency: 0.000

--------------------------------------------------
4. Carbon Flow & Sequestration
--------------------------------------------------
Traceback (most recent call last):
  File "/workspaces/M3-BioSynergy/examples/basic_simulation.py", line 534, in <module>
    main()
  File "/workspaces/M3-BioSynergy/examples/basic_simulation.py", line 483, in main
    results = simulator.run_full_simulation(
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/workspaces/M3-BioSynergy/examples/basic_simulation.py", line 193, in run_full_simulation
    results['carbon']['cce'] = cce_results
    ~~~~~~~^^^^^^^^^^
KeyError: 'carbon'
@shimojok ➜ /workspaces/M3-BioSynergy (main) $ 