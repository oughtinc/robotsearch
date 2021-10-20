from robotsearch.robots.rct_robot import RCTRobot

examples = [(
    '''Does usage of a parachute in contrast to free fall prevent major trauma?: a prospective randomised-controlled trial in rag dolls.''',
    '''PURPOSE: It is undisputed for more than 200 years that the use of a parachute prevents major trauma when falling from a great height. Nevertheless up to date no prospective randomised controlled trial has proven the superiority in preventing trauma when falling from a great height instead of a free fall. The aim of this prospective randomised controlled trial was to prove the effectiveness of a parachute when falling from great height. METHODS: In this prospective randomised-controlled trial a commercially acquirable rag doll was prepared for the purposes of the study design as in accordance to the Declaration of Helsinki, the participation of human beings in this trial was impossible. Twenty-five falls were performed with a parachute compatible to the height and weight of the doll. In the control group, another 25 falls were realised without a parachute. The main outcome measures were the rate of head injury; cervical, thoracic, lumbar, and pelvic fractures; and pneumothoraxes, hepatic, spleen, and bladder injuries in the control and parachute groups. An interdisciplinary team consisting of a specialised trauma surgeon, two neurosurgeons, and a coroner examined the rag doll for injuries. Additionally, whole-body computed tomography scans were performed to identify the injuries. RESULTS: All 50 falls-25 with the use of a parachute, 25 without a parachute-were successfully performed. Head injuries (right hemisphere p = 0.008, left hemisphere p = 0.004), cervical trauma (p < 0.001), thoracic trauma (p < 0.001), lumbar trauma (p < 0.001), pelvic trauma (p < 0.001), and hepatic, spleen, and bladder injures (p < 0.001) occurred more often in the control group. Only the pneumothoraxes showed no statistically significant difference between the control and parachute groups. CONCLUSIONS: A parachute is an effective tool to prevent major trauma when falling from a great height.'''
           ),
           ('A Cluster-Randomized Trial of Hydroxychloroquine for Prevention of Covid-19',
           """ Background: Current strategies for preventing severe acute
           respiratory syndrome coronavirus 2 (SARS-CoV-2) infection are
           limited to nonpharmacologic interventions. Hydroxychloroquine has
           been proposed as a postexposure therapy to prevent coronavirus
           disease 2019 (Covid-19), but definitive evidence is lacking.

          Methods: We conducted an open-label, cluster-randomized trial
          involving asymptomatic contacts of patients with
          polymerase-chain-reaction (PCR)-confirmed Covid-19 in Catalonia,
          Spain. We randomly assigned clusters of contacts to the
          hydroxychloroquine group (which received the drug at a dose of 800 mg
          once, followed by 400 mg daily for 6 days) or to the usual-care
          group (which received no specific therapy). The primary outcome was
          PCR-confirmed, symptomatic Covid-19 within 14 days. The secondary
          outcome was SARS-CoV-2 infection, defined by symptoms compatible with
          Covid-19 or a positive PCR test regardless of symptoms. Adverse
          events were assessed for up to 28 days.\n\nResults: The analysis
          included 2314 healthy contacts of 672 index case patients with
          Covid-19 who were identified between March 17 and April 28, 2020. A
          total of 1116 contacts were randomly assigned to receive
          hydroxychloroquine and 1198 to receive usual care. Results were
          similar in the hydroxychloroquine and usual-care groups with respect
          to the incidence of PCR-confirmed, symptomatic Covid-19 (5.7% and
          6.2%, respectively; risk ratio, 0.86 [95% confidence interval, 0.52
          to 1.42]). In addition, hydroxychloroquine was not associated with a
          lower incidence of SARS-CoV-2 transmission than usual care (18.7% and
          17.8%, respectively). The incidence of adverse events was higher in
          the hydroxychloroquine group than in the usual-care group (56.1% vs.
          5.9%), but no treatment-related serious adverse events were
          reported.\n\nConclusions: Postexposure therapy with
          hydroxychloroquine did not prevent SARS-CoV-2 infection or
          symptomatic Covid-19 in healthy persons exposed to a PCR-positive
          case patient. (Funded by the crowdfunding campaign YoMeCorono and
          others; BCN-PEP-CoV2 ClinicalTrials.gov number, NCT04304053.).
          """
          ),
          (
                "L-theanine—a unique amino acid of green tea and its relaxation effect in humans",
                """Since ancient times, it has been said that drinking green tea brings relaxation.
                The substance that is responsible for a sense of relaxation, is theanine.
                Theanine is a unique amino acid found almost solely in tea plants and the main component responsible for the exotic taste of ‘green’ tea.
                It was found that L-theanine administered intraperitoneally to rats reached the brain within 30 min without any metabolic change.
                Theanine also acts as a neurotransmitter in the brain and decreased blood pressure significantly in hypertensive rats.
                In general, animals always generate very weak electric pulses on the surface of the brain, called brain waves.
                Brain waves are classified into four types, namely α,β,δ and θ-waves, based on mental conditions.
                Generation of α-waves is considered to be an index of relaxation.
                In human volunteers, α-waves were generated on the occipital and parietal regions of the brain surface within 40 min after the oral administration of theanine (50–200 mg), signifying relaxation without causing drowsiness.
                With the successful industrial production of L-theanine, we are now able to supply Suntheanine™ (trade name of L-theanine) which offers a tremendous opportunity for designing foods and medical foods targeting relaxation and the reduction of stress.
                Taiyo Kagaku Co., Ltd, Japan won the 1998 ‘Food Ingredient Research Award’ for development of Suntheanine™ at Food Ingredients in Europe (Frankfurt).
                The judges felt it was a particularly well-documented and fascinating piece of research."""
          )
]
# ti_abs_obvious = {'ti':  "Effects of L-Theanine Administration on Stress-Related Symptoms and Cognitive Functions in Healthy Adults: A Randomized Controlled Trial",
#                     'ab': """This randomized, placebo-controlled, crossover, and double-blind trial aimed to examine the possible effects of four weeks L-theanine administration on stress-related symptoms and cognitive functions in healthy adults.
#                     Participants were 30 individuals (nine men and 21 women; age: 48.3 ± 11.9 years) who had no major psychiatric illness.
#                     L-theanine (200 mg/day) or placebo tablets were randomly and blindly assigned for four-week administration.
#                     For stress-related symptoms, Self-rating Depression Scale, State-Trait Anxiety Inventory-trait, and Pittsburgh Sleep Quality Index (PSQI) scores decreased after L-theanine administration (p = 0.19, 0.006, and 0.013, respectively).
#                     The PSQI subscale scores for sleep latency, sleep disturbance, and use of sleep medication reduced after L-theanine administration, compared to the placebo administration (all p < 0.05).
#                     For cognitive functions, verbal fluency and executive function scores improved after L-theanine administration (p = 0.001 and 0.031, respectively).
#                      Stratified analyses revealed that scores for verbal fluency (p = 0.002), especially letter fluency (p = 0.002), increased after L-theanine administration, compared to the placebo administration, in individuals who were sub-grouped into the lower half by the median split based on the mean pretreatment scores.
#                       Our findings suggest that L-theanine has the potential to promote mental health in the general population with stress-related ailments and cognitive impairments.
#                       """
# }


clf = RCTRobot()

preds = clf.predict(examples, filter_type='precise')
print([pred['is_rct'] for pred in preds])
