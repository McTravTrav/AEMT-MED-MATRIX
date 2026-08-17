import random
import streamlit as st

# Configure Streamlit Page
st.set_page_config(
    page_title="KS AEMT Pharmacology Suite", page_icon="🚑", layout="centered"
)

# -----------------------------------------------------------------------------
# MASTER MEDICATION DATASET (37 ENTRIES)
# -----------------------------------------------------------------------------
MEDICATIONS = [
    {
        "name": "Acetaminophen (Tylenol)",
        "class": "Analgesic; Antipyretic",
        "action": (
            "Elevates the pain threshold and fights fever by regulating the"
            " hypothalamic heat-regulating center of the brain."
        ),
        "indications": "Relief of mild pain or fever, headache, muscle aches.",
        "contraindications": "Hypersensitivity.",
        "precautions": (
            "Caution to avoid potential overdosing. Many OTC medications"
            " contain acetaminophen."
        ),
        "side_effects": (
            "Nausea & vomiting, GI upset, renal & liver complications."
        ),
        "adult_dose": "500-1000 mg PO every 4 hrs PRN",
        "peds_dose": "15 mg/kg PO every 4 hours PRN",
    },
    {
        "name": "Activated Charcoal (Actidose, Liquid Char)",
        "class": "Adsorbent",
        "action": (
            "Absorbs toxins in the GI tract through chemical binding which"
            " prevents absorption by the GI tract."
        ),
        "indications": "Non-caustic ingested poisonings/overdoses.",
        "contraindications": "Must have gag reflex present.",
        "precautions": (
            "Do not administer to patients without an intact gag reflex."
        ),
        "side_effects": "Nausea, vomiting, constipation, dark stools.",
        "adult_dose": (
            "1 g/kg PO (Normal range 50-75g). Mix with water to form slurry if"
            " not premixed."
        ),
        "peds_dose": "1 g/kg PO. Mix with water to form slurry.",
    },
    {
        "name": "Albuterol Sulfate (Ventolin, Proventil, Pro-Air)",
        "class": (
            "Sympathetic Agonist / Selective Beta-2 Agonist Bronchodilator"
        ),
        "action": (
            "Selective Beta-2 agonist causing rapid bronchodilation (onset 5-15"
            " mins)."
        ),
        "indications": (
            "Acute bronchial asthma attack, bronchospasm associated with COPD"
            " and emphysema."
        ),
        "contraindications": "Known hypersensitivity (allergy) to drug.",
        "precautions": (
            "Use caution in patients with known heart disease; monitor ECG"
            " rhythm."
        ),
        "side_effects": (
            "Palpitations, anxiety, dizziness, headache, nervousness, tremors,"
            " HTN, dysrhythmias, chest pain, N/V."
        ),
        "adult_dose": "2.5 mg in 3 mL NS via small volume nebulizer over 5-15 mins",
        "peds_dose": "2.5 mg in 3 mL NS via small volume nebulizer over 5-15 mins",
    },
    {
        "name": "Albuterol / Ipratropium (DuoNeb, Combivent)",
        "class": "Beta Agonist with Anti-cholinergic Bronchodilator",
        "action": (
            "Ipratropium blocks acetylcholine receptors inhibiting"
            " parasympathetic response, drying secretions. Albuterol selectively"
            " stimulates Beta-2 receptors causing rapid bronchodilation."
        ),
        "indications": (
            "Bronchospasm associated with COPD in patients requiring multiple"
            " bronchodilators; acute asthma attacks."
        ),
        "contraindications": (
            "Known hypersensitivity to Albuterol, Ipratropium, Atrovent, or"
            " Atropine derivatives."
        ),
        "precautions": (
            "May exacerbate cardiac-related disease; watch for severe"
            " hypersensitivity reactions."
        ),
        "side_effects": (
            "Palpitations, anxiety, dizziness, headache, tremors, HTN, chest"
            " pain, N/V, hives, angioedema."
        ),
        "adult_dose": (
            "0.5 mg Ipratropium / 3.0 mg Albuterol in 3 mL via in-line"
            " nebulizer. Switch to Albuterol-only if further doses needed."
        ),
        "peds_dose": (
            "1 vial via in-line nebulizer (6-10 LPM O2). Switch to"
            " Albuterol-only if further doses needed."
        ),
    },
    {
        "name": "Amiodarone (Cordarone)",
        "class": "Antiarrhythmic Agent (Class III)",
        "action": (
            "Prolongs action potential & refractory period, blocks myocardial"
            " potassium channels, causes vasodilation to decrease myocardial"
            " O2 demand."
        ),
        "indications": (
            "Refractory ventricular fibrillation/pulseless VT; interfacility"
            " transport maintenance."
        ),
        "contraindications": (
            "2nd or 3rd degree AV blocks, cardiogenic shock, severe bradycardia."
        ),
        "precautions": (
            "QT prolongation (risk of Torsades); precipitates with Sodium"
            " Bicarb; interactions with Beta/Calcium Channel blockers."
        ),
        "side_effects": "Hypotension, bradycardia, CHF, nausea, cardiac arrest.",
        "adult_dose": (
            "Initial 300 mg rapid IV/IO push. May repeat in 3-5 mins at 150 mg"
            " rapid IV/IO push."
        ),
        "peds_dose": "5 mg/kg rapid IV/IO push (Max 15 mg/kg).",
    },
    {
        "name": "Aspirin (Acetylsalicylic Acid / ASA / Bayer)",
        "class": "Platelet Inhibitor / Anti-Inflammatory (NSAID)",
        "action": "Blocks platelet aggregation ('de-stickies' platelets).",
        "indications": (
            "New chest pain suggestive of acute myocardial infarction/ischemic"
            " event."
        ),
        "contraindications": (
            "Hypersensitivity, exceeded maximum dose, active peptic ulcer,"
            " active GI bleed."
        ),
        "precautions": (
            "Do not administer to children due to high risk of Reye's syndrome."
        ),
        "side_effects": (
            "Heartburn, nausea, vomiting, wheezing, GI bleeding, prolonged"
            " bleeding."
        ),
        "adult_dose": "160 to 325 mg PO chewed (2-4 baby ASA tablets)",
        "peds_dose": "Not recommended",
    },
    {
        "name": "Atropine (Atropen)",
        "class": "Parasympatholytic / Anticholinergic",
        "action": (
            "Blocks acetylcholine receptors, reducing parasympathetic"
            " stimulation. Increases HR, dilates bronchioles, and dries"
            " secretions."
        ),
        "indications": (
            "Organophosphate poisoning, nerve agent exposure/poisoning. Self or"
            " peer care."
        ),
        "contraindications": (
            "None in organophosphate or nerve agent poisoning settings."
        ),
        "precautions": (
            "None in emergency setting when given by an AEMT. Large doses"
            " indicated in severe poisoning."
        ),
        "side_effects": (
            "Blurred vision, dilated pupils, dry mouth, drowsiness, confusion,"
            " tachycardia."
        ),
        "adult_dose": (
            "2 mg Atropine per Mark 1 or DuoDote kit IM. Repeat if no"
            " improvement per local protocol."
        ),
        "peds_dose": "None at this time for AEMT level.",
    },
    {
        "name": "Dextrose (D50, D25, D10)",
        "class": "Hyperglycemic Agent / Carbohydrate",
        "action": (
            "Restores blood sugar to normal levels and provides immediate"
            " cellular energy."
        ),
        "indications": "Hypoglycemia ONLY.",
        "contraindications": (
            "Diabetic coma with hyperglycemia, intracranial or intraspinal"
            " hemorrhage."
        ),
        "precautions": (
            "Draw blood sample prior to administration; highly hypertonic (can"
            " cause vein irritation/necrosis)."
        ),
        "side_effects": (
            "Venous thrombosis, phlebitis, tissue necrosis upon extravasation,"
            " polydipsia, tachypnea."
        ),
        "adult_dose": "25 g IV of D50 (50 mL). Repeat PRN if ineffective.",
        "peds_dose": (
            "30 days to 25kg: 0.5-1.0 g/kg IV of D25 solution; Neonates (<30"
            " days): 0.2 g/kg IV of D10 solution."
        ),
    },
    {
        "name": "Diazepam (Valium)",
        "class": "Benzodiazepine / Sedative / Anticonvulsant",
        "action": (
            "Suppresses spread of seizure activity through motor cortex,"
            " relaxes skeletal muscle."
        ),
        "indications": "Status Epilepticus ONLY.",
        "contraindications": (
            "Hypersensitivity, severe CNS depression, respiratory depression,"
            " narrow-angle glaucoma."
        ),
        "precautions": (
            "Rapid IV push causes respiratory depression, apnea, or"
            " hypotension. Potentiated by CNS depressants."
        ),
        "side_effects": (
            "Apnea, bradycardia, hypotension, drowsiness, confusion, pain with"
            " injection."
        ),
        "adult_dose": (
            "2-10 mg slow IV/IO/IM/IN/PR (titrated to stop seizure). Max total:"
            " 30 mg."
        ),
        "peds_dose": (
            "Up to 5 yrs: 0.2-0.5 mg/kg IV/IO/PR (Max 5mg); >5 yrs: 1.0 mg every"
            " 2-5 min (Max 10mg)."
        ),
    },
    {
        "name": "Diphenhydramine (Benadryl)",
        "class": "Antihistamine / Sedative",
        "action": (
            "Competes with histamine for H1 receptor sites on effector cells in"
            " GI, blood vessels, and respiratory tract."
        ),
        "indications": (
            "Acute Allergic Reaction (AEMT IV route), dyspnea/mild allergic"
            " symptoms, anaphylaxis after shock is managed."
        ),
        "contraindications": (
            "Hypersensitivity, acute asthma attack (unless wheezing concurrent"
            " with anaphylaxis)."
        ),
        "precautions": (
            "Potentiates sedatives & anticholinergics. Use caution in glaucoma,"
            " peptic ulcer, hyperthyroidism."
        ),
        "side_effects": (
            "Sedation, dizziness, hypotension, palpitations, dry mucous"
            " membranes, thickened bronchial secretions."
        ),
        "adult_dose": "25 - 50 mg IV, IM, or PO",
        "peds_dose": "1.0 - 2.0 mg/kg IV, IM, or PO (Do not exceed adult dose)",
    },
    {
        "name": "DuoDote Kit (Atropine & Pralidoxime Chloride)",
        "class": "Antidote / Anticholinergic & Cholinesterase Reactivator",
        "action": (
            "Atropine blocks acetylcholine receptors to reduce parasympathetic"
            " stimulation. Pralidoxime removes phosphate groups from"
            " cholinesterase, reactivating the enzyme to breakdown excess"
            " acetylcholine."
        ),
        "indications": (
            "Organophosphate poisoning, nerve agent exposure/poisoning (Self"
            " or peer care)."
        ),
        "contraindications": (
            "None in organophosphate or nerve agent poisoning setting."
        ),
        "precautions": (
            "Self or peer care priority. Large doses indicated in severe"
            " poisoning."
        ),
        "side_effects": (
            "Blurred vision, dilated pupils, dry mouth, dizziness, headache,"
            " tachycardia, HTN, N/V."
        ),
        "adult_dose": (
            "1 auto-injector IM (delivers 2.1 mg Atropine / 600 mg Pralidoxime"
            " Cl). Repeat per local protocol if no improvement."
        ),
        "peds_dose": "Protocol driven / None at this time for AEMT level.",
    },
    {
        "name": "Epinephrine 1:1,000 (Adrenaline)",
        "class": "Catecholamine / Sympathomimetic",
        "action": (
            "Stimulates Alpha, Beta-1, and Beta-2 adrenergic receptors."
            " Relaxes bronchial smooth muscle, causes cardiac stimulation and"
            " skeletal muscle vasodilation."
        ),
        "indications": "Anaphylactic reaction.",
        "contraindications": "None in severe anaphylaxis.",
        "precautions": (
            "Use caution in patients > 50 years old in non-arrest state."
        ),
        "side_effects": (
            "Tachycardia, HTN, palpitations, anxiety, headache, dyspnea,"
            " cardiac dysrhythmias."
        ),
        "adult_dose": (
            "0.1 - 0.3 - 0.5 mg IM (1:1,000 solution via manual draw or"
            " auto-injector)"
        ),
        "peds_dose": (
            "0.15 mg IM (1:1,000 solution via manual draw or auto-injector)"
        ),
    },
    {
        "name": "Epinephrine 1:10,000 (Adrenaline)",
        "class": "Catecholamine / Sympathomimetic",
        "action": (
            "Increases HR, cardiac contractile force, myocardial electrical"
            " activity, SVR ('makes the tank smaller'), BP, and automaticity."
            " Lowers V-Fib threshold."
        ),
        "indications": "Cardiac Arrest.",
        "contraindications": "None in cardiac arrest.",
        "precautions": (
            "Deactivated by alkaline solutions like Sodium Bicarb; flush line"
            " between uses."
        ),
        "side_effects": (
            "Tachycardia, HTN, increased myocardial O2 demand,"
            " dysrhythmias, anxiety, headache."
        ),
        "adult_dose": "1 mg IV/IO every 3-5 minutes (No max dose)",
        "peds_dose": (
            "0.01 mg/kg (0.1 mL/kg of 1:10,000) IV/IO every 3-5 minutes (No max"
            " dose)"
        ),
    },
    {
        "name": "Fentanyl Citrate (Sublimaze)",
        "class": "Opiate Analgesic (Schedule II)",
        "action": (
            "Potent synthetic narcotic agonist. Increases pain threshold,"
            " alters pain reception, depresses CNS. 50-100x more potent than"
            " morphine with minimal histamine release."
        ),
        "indications": "Pain relief (including ischemic chest pain).",
        "contraindications": (
            "Hypersensitivity to opiates, current use of MAOIs."
        ),
        "precautions": (
            "Rapid IV push causes chest wall rigidity (inability to ventilate"
            " via BVM). Use caution in head injury/ICP."
        ),
        "side_effects": "Bradycardia, hypotension, flushing, dizziness, N/V.",
        "adult_dose": (
            "1 mcg/kg slow IV/IO/IN (titrate to effect, typical range 25-100"
            " mcg). May repeat x1 in 5 min (Max 2 mcg/kg)."
        ),
        "peds_dose": (
            "1 mcg/kg slow IV/IO/IN (Age 1-12 yrs). Do not exceed adult dose."
            " May repeat x1 in 30 min with physician order."
        ),
    },
    {
        "name": "Glucagon (GlucaGen)",
        "class": "Pancreatic Hormone / Hyperglycemic Agent",
        "action": (
            "Stimulates hepatic glycogenolysis to convert stored glycogen to"
            " glucose. Has positive inotropic and chronotropic effects on heart"
            " independent of beta blockade."
        ),
        "indications": (
            "Acute Hypoglycemia when oral glucose or IV/IO access is"
            " unobtainable."
        ),
        "contraindications": (
            "Hypersensitivity, 2nd and 3rd-degree heart block."
        ),
        "precautions": (
            "Requires intact liver glycogen stores; give supplemental oral carbs"
            " as soon as patient wakes. Caution in pheochromocytoma."
        ),
        "side_effects": "Nausea, vomiting, transient hypotension.",
        "adult_dose": (
            "1.0 mg IM (via traditional kit or auto-injector/GlucaPen)"
        ),
        "peds_dose": "30 days to 25kg: 0.5 mg IM; > 25kg: 1.0 mg IM",
    },
    {
        "name": "Glutose (Oral Glucose / Gel)",
        "class": "Carbohydrate",
        "action": (
            "Raises blood glucose levels via direct absorption through oral"
            " mucous membranes and GI tract."
        ),
        "indications": "Acute Hypoglycemia.",
        "contraindications": (
            "Inability to swallow, inability to maintain airway, total"
            " unresponsiveness."
        ),
        "precautions": (
            "Continuously monitor LOC during administration to avoid"
            " aspiration."
        ),
        "side_effects": "Nausea, vomiting, hyperglycemia.",
        "adult_dose": "1 tube PO (15g, 31g, or 45g squeeze tube/pack)",
        "peds_dose": "1 tube PO titrated to effect",
    },
    {
        "name": "Hydrocortisone (Solu-Cortef)",
        "class": "Corticosteroid / Anti-inflammatory",
        "action": (
            "Short-acting synthetic steroid that inhibits formation, storage,"
            " and release of histamine from mast cells."
        ),
        "indications": "Severe Asthma.",
        "contraindications": "Hypersensitivity.",
        "precautions": (
            "Single dose in prehospital setting. Long-term use causes GI"
            " bleeding and delayed wound healing."
        ),
        "side_effects": (
            "Fluid retention, HTN, abdominal distention, vertigo, headache,"
            " hiccups."
        ),
        "adult_dose": (
            "40 - 250 mg IV (Usually 250 mg; 'Core is More'). IM is permitted"
            " per KSBEMS."
        ),
        "peds_dose": "4 - 8 mg/kg IV/IM (IV preferred)",
    },
    {
        "name": "Hydromorphone (Dilaudid)",
        "class": "Opiate Analgesic (Schedule II)",
        "action": (
            "Potent opiate receptor agonist (7x more potent than Morphine)."
            " Alters pain reception and causes peripheral vasodilation"
            " decreasing venous return."
        ),
        "indications": "Moderate to severe pain (including chest pain).",
        "contraindications": (
            "Hypersensitivity to opiates, hypotension, hypovolemia, head injury"
            " with AMS, active status asthmaticus."
        ),
        "precautions": (
            "Requires continuous pulse oximetry, cardiac monitoring, and airway"
            " readiness. May need 9mL NS dilution for accurate dosing."
        ),
        "side_effects": (
            "Respiratory depression, bradycardia, hypotension, lightheadedness,"
            " hallucinations, N/V."
        ),
        "adult_dose": (
            "0.5 mg slow IVP over 2-3 minutes every 10 min PRN (Max 2.0 mg"
            " total)"
        ),
        "peds_dose": "Not recommended for pediatric pain control.",
    },
    {
        "name": "Ipratropium Bromide (Atrovent)",
        "class": "Anticholinergic Bronchodilator",
        "action": (
            "Inhibits acetylcholine at bronchial smooth muscle receptors,"
            " suppressing cholinergic response to allow Beta-2 bronchodilation."
            " Abolishes vagally mediated reflex bronchospasm."
        ),
        "indications": (
            "Acute asthma and bronchospasm (alone or co-administered with"
            " Albuterol)."
        ),
        "contraindications": (
            "Hypersensitivity to Ipratropium, Atrovent components, or Atropine"
            " derivatives."
        ),
        "precautions": (
            "Watch for acute hypersensitivity reactions (angioedema,"
            " laryngospasm)."
        ),
        "side_effects": (
            "Hives, angioedema, rash, paradoxical bronchospasm, anaphylaxis,"
            " oropharyngeal edema."
        ),
        "adult_dose": "500 mcg (0.5 mg) via nebulizer at 6-10 LPM O2",
        "peds_dose": "500 mcg (0.5 mg) via nebulizer at 6-10 LPM O2",
    },
    {
        "name": "Ketorolac (Toradol)",
        "class": "Nonsteroidal Anti-Inflammatory Drug (NSAID)",
        "action": (
            "Inhibits prostaglandin synthesis via COX enzyme inhibition."
            " Provides potent analgesia with moderate anti-inflammatory"
            " action. Effective for renal colic."
        ),
        "indications": "Mild to moderate pain.",
        "contraindications": (
            "Hypersensitivity/NSAID allergy, asthma, renal insufficiency, PUD/GI"
            " bleed, pregnancy, hypovolemia, non-isolated trauma, upcoming major"
            " surgery."
        ),
        "precautions": (
            "NOT for abdominal or chest pain. Reduce dose by 50% in patients >"
            " 65 yrs old."
        ),
        "side_effects": (
            "GI bleeding, N/V, headache, drowsiness, abdominal pain, dyspepsia."
        ),
        "adult_dose": (
            "15 - 30 mg IM or slow IVP (over at least 15 sec). Max daily: 60 mg"
            " IM / 120 mg IV."
        ),
        "peds_dose": (
            "0.5 - 1.0 mg/kg IM/IV single dose (Max 15 mg total daily)."
        ),
    },
    {
        "name": "Lactated Ringers (LR)",
        "class": "Isotonic Crystalloid Salt Solution",
        "action": (
            "Expands circulating volume by approximating blood sodium content"
            " (273 mOsmol/L). Contains Na 130, Cl 109, K 4, Ca 3, Lactate 28"
            " mEq/L."
        ),
        "indications": (
            "Volume replacement fluid, TKO line for medication administration,"
            " wound irrigation."
        ),
        "contraindications": (
            "None (avoid during blood transfusion due to risk of coagulation)."
        ),
        "precautions": (
            "Avoid blood co-infusion; perform frequent lung sound assessments"
            " to prevent fluid overload."
        ),
        "side_effects": "Fluid overload, edema, electrolyte imbalance, HTN, CHF.",
        "adult_dose": "TKO or 20 mL/kg boluses per protocol",
        "peds_dose": "TKO or 20 mL/kg boluses per protocol",
    },
    {
        "name": "Levalbuterol (Xopenex / Zopanex)",
        "class": "Beta Adrenergic Agonist (Beta-2 Selective)",
        "action": (
            "Stimulates Beta-2 receptors, increasing cyclic AMP to relax"
            " bronchial smooth muscle. Inhibits mast cell mediator release."
            " R-isomer provides bronchodilation with potentially less cardiac"
            " stimulation/tachycardia than racemic Albuterol."
        ),
        "indications": (
            "Acute bronchial asthma attack, reversible bronchospasm associated"
            " with COPD and emphysema."
        ),
        "contraindications": (
            "History of hypersensitivity to Levalbuterol HCl or racemic"
            " Albuterol."
        ),
        "precautions": (
            "Use caution in patients with known heart disease; monitor cardiac"
            " rhythm (ECG)."
        ),
        "side_effects": (
            "Palpitations, anxiety, dizziness, headache, nervousness, tremors,"
            " HTN, dysrhythmias, chest pain, N/V."
        ),
        "adult_dose": (
            "1.25 – 2.5 mg in 3 mL via small volume, in-line nebulizer every 20"
            " mins (Max 3 doses)."
        ),
        "peds_dose": (
            "0.075 mg/kg/dose (Min dose 1.25 mg) via small volume, in-line"
            " nebulizer every 20 mins (Max 3 doses)."
        ),
    },
    {
        "name": "Lidocaine (Xylocaine)",
        "class": "Antiarrhythmic (Class IB) / Local Anesthetic",
        "action": (
            "Suppresses ventricular ectopic activity, increases V-Fib"
            " threshold, reduces conduction velocity, decreases pain threshold"
            " prior to IO infusion."
        ),
        "indications": (
            "VF, Pulseless VT, anesthesia prior to or after IO insertion."
        ),
        "contraindications": (
            "High-degree heart blocks, PVCs associated with bradycardia,"
            " bradycardic rhythms."
        ),
        "precautions": (
            "Max cumulative dose 3 mg/kg. Reduce dose by 50% in patients > 70"
            " yrs or with liver disease. Watch for metallic taste/tinnitus (CNS"
            " toxicity)."
        ),
        "side_effects": (
            "Anxiety, drowsiness, confusion, N/V, seizures, metallic taste,"
            " tinnitus."
        ),
        "adult_dose": (
            "Cardiac Arrest: 1-1.5 mg/kg IV/IO (Repeat 0.5-0.75 mg/kg to max"
            " 3mg/kg). IO Anesthetic: 40 mg slowly over 120s, 60s dwell, flush"
            " NS, then 20 mg over 60s."
        ),
        "peds_dose": (
            "Cardiac Arrest: 1 mg/kg IV/IO. IO Anesthetic: 0.5 mg/kg (Max 40"
            " mg) over 120s, 60s dwell, flush NS, then half initial dose over"
            " 60s."
        ),
    },
    {
        "name": "Lorazepam (Ativan)",
        "class": "Benzodiazepine / Anticonvulsant",
        "action": (
            "Potent benzodiazepine acting via inhibitory neurotransmitter GABA"
            " at thalamic, hypothalamic, and limbic CNS levels. Suppresses"
            " seizure activity in motor cortex."
        ),
        "indications": "Status Epilepticus ONLY.",
        "contraindications": (
            "Hypersensitivity, comatose state, pre-existing CNS depression,"
            " narrow-angle glaucoma, severe uncontrolled pain, severe"
            " hypotension."
        ),
        "precautions": (
            "Preferred drug for pediatric seizures due to shorter half-life."
            " Caution in renal/hepatic/pulmonary impairment."
        ),
        "side_effects": (
            "Respiratory depression, apnea, bradycardia, hypotension, CNS"
            " depression, sedation, confusion."
        ),
        "adult_dose": "1 - 4 mg slow IV/IO, IM, IN, or PR",
        "peds_dose": (
            "12-17 yrs: 0.07 mg/kg; 1 mo - 11 yrs: 0.1 mg/kg (Max 2 mg); < 1"
            " mo: 0.05 mg/kg IV/IO/IM/IN/PR"
        ),
    },
    {
        "name": "Methylprednisolone (Solu-Medrol)",
        "class": "Corticosteroid / Anti-inflammatory",
        "action": (
            "Anti-inflammatory steroid that reduces tissue-destructive enzyme"
            " release, inhibits capillary permeability, and blocks allergic"
            " substance storage."
        ),
        "indications": "Respiratory Emergencies (Severe Asthma).",
        "contraindications": (
            "Premature infants (fatal gasping syndrome risk), hypersensitivity."
        ),
        "precautions": (
            "Single dose for prehospital use; long-term use causes GI bleeding,"
            " delayed wound healing, adrenocortical suppression."
        ),
        "side_effects": (
            "Hiccups, fluid retention, nausea, abdominal distention."
        ),
        "adult_dose": (
            "125 - 250 mg IV (Usually 125 mg; IV preferred). Up to 30 mg/kg via"
            " medical order."
        ),
        "peds_dose": "1 - 2 mg/kg IV/IM (IV preferred)",
    },
    {
        "name": "Midazolam (Versed)",
        "class": "Benzodiazepine / Tranquilizer",
        "action": (
            "Short-acting parenteral benzodiazepine with CNS depressant,"
            " muscle relaxant, anticonvulsant, and anterograde amnestic"
            " effects. Intensifies GABA activity. No analgesic effect."
        ),
        "indications": "Status Epilepticus ONLY.",
        "contraindications": (
            "Hypersensitivity, narrow-angle glaucoma, shock."
        ),
        "precautions": (
            "Have resuscitative equipment ready. Dilute with NS or D5W prior to"
            " IV administration. High risk of respiratory depression."
        ),
        "side_effects": (
            "Respiratory depression, apnea, hypotension, drowsiness,"
            " confusion, amnesia."
        ),
        "adult_dose": (
            "2.5 mg initial slow IV/IO/IM/IN/PR (Repeat to avg range 5 mg; Max"
            " 8 mg total)"
        ),
        "peds_dose": (
            "0.1 mg/kg IV/IO/IM/IN/PR (Typical single max 2.5 mg; max total 5"
            " mg)"
        ),
    },
    {
        "name": "Morphine Sulfate (MSO4)",
        "class": "Narcotic Analgesic (Schedule II)",
        "action": (
            "Natural opium derivative acting on brain opiate receptors."
            " Depresses CNS, causes peripheral vasodilation ('makes tank"
            " bigger'), reducing preload and myocardial O2 demand."
        ),
        "indications": "Pain relief (including ischemic chest pain).",
        "contraindications": (
            "Head injury, severe volume depletion, hypersensitivity to"
            " morphine."
        ),
        "precautions": (
            "Respiratory depression risk (have Narcan available),"
            " hypotension, N/V."
        ),
        "side_effects": (
            "Altered LOC, dizziness, hives, respiratory depression,"
            " hypotension, N/V."
        ),
        "adult_dose": "2.0 - 10 mg IV/IO/IM (Titrate to effect per protocol)",
        "peds_dose": (
            "0.1 - 0.2 mg/kg IV/IO bolus (Titrate to effect; direct physician"
            " order encouraged)"
        ),
    },
    {
        "name": "Naloxone (Narcan)",
        "class": "Narcotic Antagonist",
        "action": (
            "Pure opioid antagonist that competes for and displaces narcotic"
            " molecules from brain opiate receptors to reverse respiratory"
            " depression."
        ),
        "indications": (
            "Narcotic toxicity / overdose reversal with respiratory depression."
        ),
        "contraindications": "Hypersensitivity.",
        "precautions": (
            "Do NOT insert supraglottic airway prior to administration. May"
            " trigger acute withdrawal (HTN, agitation, combativeness, vomiting)."
        ),
        "side_effects": (
            "HTN, hypotension, tachycardia, ventricular dysrhythmias, cardiac"
            " arrest, N/V."
        ),
        "adult_dose": (
            "0.4 - 2.0 mg increments IV/IO/IM/SQ/IN (Max SINGLE dose 2.0 mg;"
            " Max total 6.0 mg)"
        ),
        "peds_dose": "0.1 mg/kg IV/IO/IM/SQ/IN (Max SINGLE dose 2.0 mg)",
    },
    {
        "name": "Nitroglycerin (NitroStat, NitroBid)",
        "class": "Antianginal / Vasodilator",
        "action": (
            "Potent organic nitrate vasodilator that relaxes smooth muscle,"
            " dilates veins > arteries, reduces preload/afterload, and improves"
            " collateral coronary flow."
        ),
        "indications": "Acute angina or chest pain of cardiac origin.",
        "contraindications": (
            "Hypersensitivity, increased ICP, Systolic BP < 100 mmHg, PDE-5"
            " inhibitor use within 36 hrs (e.g., Viagra, Cialis, Levitra,"
            " Revatio)."
        ),
        "precautions": (
            "Obtain 12-lead EKG prior to administration to rule out Right"
            " Ventricular Infarction."
        ),
        "side_effects": (
            "Headache, severe hypotension, syncope, reflex tachycardia,"
            " flushing, N/V."
        ),
        "adult_dose": (
            "0.4 - 0.8 mg SL every 5 min PRN (up to 3 doses); Dermal: 1/2 to 1"
            " inch Nitro-Bid paste."
        ),
        "peds_dose": "Not recommended",
    },
    {
        "name": "Normal Saline (0.9% NaCl, NS)",
        "class": "Isotonic Crystalloid Salt Solution",
        "action": (
            "Expands intravascular volume approximating blood sodium levels"
            " (308 mOsmol/L). Contains 154 mEq Na+ and 154 mEq Cl- per liter."
        ),
        "indications": (
            "Volume replacement fluid, TKO line for medication administration,"
            " wound irrigation."
        ),
        "contraindications": "None.",
        "precautions": (
            "Frequent breath sound assessments to avoid fluid overload; maintain"
            " aseptic IV technique to avoid sepsis."
        ),
        "side_effects": "Fluid overload, edema, electrolyte imbalance, HTN, CHF.",
        "adult_dose": "TKO or 20 mL/kg boluses per protocol",
        "peds_dose": "TKO or 20 mL/kg boluses per protocol",
    },
    {
        "name": "Ondansetron (Zofran)",
        "class": "Antiemetic / Serotonin (5-HT3) Antagonist",
        "action": (
            "Selectively blocks serotonin 5-HT3 receptors in the CNS at the"
            " chemoreceptor trigger zone and in the PNS on vagal nerve"
            " terminals."
        ),
        "indications": "Nausea and vomiting.",
        "contraindications": (
            "Hypersensitivity. Use caution in patients with hepatic impairment."
        ),
        "precautions": (
            "Pushing too fast can increase side effects (headache, dizziness,"
            " dysrhythmias)."
        ),
        "side_effects": (
            "Headache, malaise, fatigue, dizziness, sedation, EPS, chest pain,"
            " dysrhythmias, diarrhea, constipation, ABD pain, rash."
        ),
        "adult_dose": (
            "4 - 8 mg slow IV push over 2-5 minutes (or PO, IV, IO, IM per"
            " KSBEMS)"
        ),
        "peds_dose": (
            "1 mo to 12 yrs: >40kg = 4 mg slow IV push over 2-5 min; <40kg = 0.1"
            " mg/kg slow IV push over 2-5 min (or PO, IV, IO, IM)"
        ),
    },
    {
        "name": "Oral Analgesics & OTC Medications",
        "class": "Analgesics / Antipyretics / Antihistamines / Antacids",
        "action": (
            "Varies by specific OTC medication class (e.g., Acetaminophen,"
            " Ibuprofen, Diphenhydramine, Bismuth Subsalicylate, Ranitidine,"
            " Omeprazole)."
        ),
        "indications": (
            "Mild to moderate pain, fever, mild allergic symptoms, GI distress."
        ),
        "contraindications": (
            "Standing orders (NOT permitted in standing orders for AEMTs)."
        ),
        "precautions": (
            "Requires DIRECT PHYSICIAN ORDER ONLY. AEMTs must report patient's"
            " existing medications to physician to avoid adverse drug"
            " interactions. Most common in clinical or industrial settings."
        ),
        "side_effects": "Varies by agent administered.",
        "adult_dose": "Per Direct Physician Order ONLY",
        "peds_dose": "Per Direct Physician Order ONLY",
    },
    {
        "name": "Oxygen (O2)",
        "class": "Medical Gas",
        "action": (
            "Essential for cellular metabolism. Increases arterial oxygen"
            " saturation and tissue oxygenation."
        ),
        "indications": (
            "Hypoxia (SpO2 < 94%), hypoperfusion, conditions requiring"
            " increased oxygen supply."
        ),
        "contraindications": "None in life-threatening situations.",
        "precautions": (
            "Use caution in COPD/emphysema patients reliant on hypoxic drive;"
            " do NOT withhold O2 if patient is hypoxic, but be prepared to"
            " ventilate via BVM if apnea occurs."
        ),
        "side_effects": (
            "Apnea in COPD patients, drying of mucous membranes."
        ),
        "adult_dose": (
            "Cardiac Arrest / Critical: 100% (15-25 LPM via BVM, NRB, or ETT);"
            " COPD: 35% titrate to effect"
        ),
        "peds_dose": "24% - 100% titrated to target oxygenation",
    },
    {
        "name": "Pralidoxime (2-PAM / Protopam Chloride)",
        "class": "Cholinesterase Reactivator",
        "action": (
            "Removes phosphate groups from cholinesterase, allowing it to"
            " deactivate acetylcholine (ACh). Returns body toward normal"
            " function following nerve agent exposure."
        ),
        "indications": "Severe organophosphate poisoning, nerve agent poisoning.",
        "contraindications": (
            "Inorganic compounds or carbamate insecticides (e.g., 1-naphthol,"
            " carbofuran)."
        ),
        "precautions": (
            "Administer alongside Atropine for optimal efficacy in severe"
            " poisonings."
        ),
        "side_effects": (
            "Dizziness, headache, tachycardia, HTN, nausea, vomiting, increased"
            " salivation."
        ),
        "adult_dose": (
            "600 mg IM via Mark 1 or DuoDote kit. Repeat per local protocol for"
            " self or peer care."
        ),
        "peds_dose": "Protocol driven",
    },
    {
        "name": "Promethazine (Phenergan)",
        "class": "Phenothiazine Antiemetic",
        "action": (
            "Blocks central dopaminergic D1 and D2 receptors in the"
            " chemoreceptor trigger zone (CTZ) of the brain."
        ),
        "indications": "Nausea and vomiting.",
        "contraindications": (
            "Known hypersensitivity, Parkinson's disease, narrow-angle"
            " glaucoma."
        ),
        "precautions": (
            "Severe tissue irritant (risk of severe vascular injury/gangrene if"
            " extravasated or given intra-arterially). Lowers seizure threshold."
            " Contains metabisulfites (asthma risk)."
        ),
        "side_effects": (
            "Sedation, extrapyramidal/dystonic reactions, hypotension,"
            " tachycardia, blurred vision, dry mouth, neuroleptic malignant"
            " syndrome, paradoxical excitation."
        ),
        "adult_dose": "12.5 to 25 mg IV or IM every 4 hours PRN",
        "peds_dose": "6.25 to 12.5 mg IV or IM (1 mo - 12 yrs) every 4 hours PRN",
    },
    {
        "name": "Terbutaline (Brethine)",
        "class": "Selective Beta-2 Adrenergic Agonist / Sympathomimetic",
        "action": (
            "Stimulates Beta-2 receptors causing rapid bronchodilation with"
            " minimal cardiac effects. Relaxes uterine smooth muscle"
            " (suppresses pre-term labor)."
        ),
        "indications": "Acute asthma attack, bronchospasm.",
        "contraindications": "Known hypersensitivity.",
        "precautions": (
            "Monitor vital signs; use caution in elderly or patients with"
            " cardiovascular disease/HTN. Beta-blockers may blunt response."
        ),
        "side_effects": (
            "Palpitations, anxiety, dizziness, headache, tremors, HTN,"
            " dysrhythmias, chest pain, N/V."
        ),
        "adult_dose": (
            "0.25 mg SC; or 2 mg in 3 mL NS via nebulizer at 6-8 LPM O2 (repeat"
            " in 15-30 min PRN)"
        ),
        "peds_dose": (
            "0.25 mg SC; or 2 mg in 3 mL NS via nebulizer at 6-8 LPM O2 (repeat"
            " in 15-30 min PRN)"
        ),
    },
    {
        "name": "Tranexamic Acid (TXA)",
        "class": "Antifibrinolytic Agent",
        "action": (
            "Reversibly binds lysine receptor sites on plasminogen, preventing"
            " its conversion to plasmin. Preserves fibrin matrix to stabilize"
            " clot formation and stop hyper-fibrinolysis."
        ),
        "indications": (
            "Adult trauma patients with significant hemorrhage (SBP < 90 mmHg,"
            " HR > 110 bpm) requiring MTP within 3 hours of injury (max 8 hrs)."
        ),
        "contraindications": (
            "Hypersensitivity, time elapsed > 3 hours, age < 16 years, isolated"
            " closed head injury, pregnancy >= 24 weeks, concurrent use of PCCs"
            " or Factor VIIa."
        ),
        "precautions": (
            "Infuse slowly over 10 mins to prevent severe hypotension. Caution"
            " in urinary tract bleeding. Inform receiving facility of field"
            " loading dose."
        ),
        "side_effects": (
            "Visual disturbances, N/V, headache, abdominal pain, diarrhea,"
            " seizures, DVT, PE, anaphylaxis."
        ),
        "adult_dose": (
            "1 gram IV infusion over 10 minutes (placed in 50 mL NS bag or slow"
            " push)"
        ),
        "peds_dose": (
            "0.5 - 1.0 mg/kg IM or IV single dose (Max 15 mg total daily dose)"
        ),
    },
]

# -----------------------------------------------------------------------------
# SESSION STATE INITIALIZATION
# -----------------------------------------------------------------------------
if "card_idx" not in st.session_state:
    st.session_state.card_idx = 0
if "show_back" not in st.session_state:
    st.session_state.show_back = False

if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0
if "quiz_total" not in st.session_state:
    st.session_state.quiz_total = 0
if "current_question" not in st.session_state:
    st.session_state.current_question = None

# -----------------------------------------------------------------------------
# HELPER FUNCTIONS
# -----------------------------------------------------------------------------


def generate_quiz_question():
    """Generates a dynamic multiple choice question based on the dataset."""
    target = random.choice(MEDICATIONS)
    q_type = random.choice([
        "indications",
        "contraindications",
        "adult_dose",
        "class",
    ])

    correct_ans = target[q_type]

    # Pull distractor options from other medications
    other_meds = [m for m in MEDICATIONS if m["name"] != target["name"]]
    wrong_choices = random.sample(
        [m[q_type] for m in other_meds], min(3, len(other_meds))
    )

    choices = wrong_choices + [correct_ans]
    random.shuffle(choices)

    st.session_state.current_question = {
        "drug_name": target["name"],
        "q_type": q_type,
        "correct": correct_ans,
        "choices": choices,
        "user_answered": False,
    }


# -----------------------------------------------------------------------------
# INTERFACE LAYOUT
# -----------------------------------------------------------------------------
st.title("🚑 Kansas AEMT Pharmacology Suite")

# Sidebar navigation
mode = st.sidebar.radio("Study Mode", ["Flashcards", "Multiple Choice Quiz"])

# =============================================================================
# MODE 1: TRADITIONAL TWO-SIDED FLASHCARDS
# =============================================================================
if mode == "Flashcards":
    st.header("Interactive Two-Sided Flashcards")

    total_cards = len(MEDICATIONS)
    current_card = MEDICATIONS[st.session_state.card_idx]

    # Card Progress
    st.progress((st.session_state.card_idx + 1) / total_cards)
    st.caption(f"Medication {st.session_state.card_idx + 1} of {total_cards}")

    # Card Container
    with st.container(border=True):
        st.subheader(f"💊 {current_card['name']}")

        if not st.session_state.show_back:
            st.info("👆 Click **Flip Card** to view detailed pharmacology.")
        else:
            st.markdown(f"**Class:** {current_card['class']}")
            st.markdown(f"**Action:** {current_card['action']}")
            st.markdown(f"**Indications:** {current_card['indications']}")
            st.markdown(
                f"**Contraindications:** {current_card['contraindications']}"
            )
            st.markdown(f"**Precautions:** {current_card['precautions']}")
            st.markdown(f"**Side Effects:** {current_card['side_effects']}")
            st.markdown(f"**Adult Dose:** {current_card['adult_dose']}")
            st.markdown(f"**Peds Dose:** {current_card['peds_dose']}")

    # Controls
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        if st.button("⬅️ Previous"):
            st.session_state.card_idx = (
                st.session_state.card_idx - 1
            ) % total_cards
            st.session_state.show_back = False
            st.rerun()

    with col2:
        if st.button("🔄 Flip Card"):
            st.session_state.show_back = not st.session_state.show_back
            st.rerun()

    with col3:
        if st.button("Next ➡️"):
            st.session_state.card_idx = (
                st.session_state.card_idx + 1
            ) % total_cards
            st.session_state.show_back = False
            st.rerun()

# =============================================================================
# MODE 2: MULTIPLE CHOICE QUIZ
# =============================================================================
elif mode == "Multiple Choice Quiz":
    st.header("Pharmacology Knowledge Check")

    # Metrics on sidebar
    st.sidebar.metric(
        "Current Score",
        f"{st.session_state.quiz_score} / {st.session_state.quiz_total}",
    )

    if st.session_state.current_question is None:
        generate_quiz_question()

    q = st.session_state.current_question

    field_labels = {
        "indications": "indication(s)",
        "contraindications": "contraindication(s)",
        "adult_dose": "adult dose & route",
        "class": "pharmacological class",
    }

    st.write(
        f"**Question:** What is the correct **{field_labels[q['q_type']]}** for"
        f" **{q['drug_name']}**?"
    )

    # Choice Selection
    user_choice = st.radio(
        "Select your answer:", q["choices"], key="quiz_choice"
    )

    col1, col2 = st.columns([1, 1])

    with col1:
        if st.button("Submit Answer") and not q.get("user_answered"):
            st.session_state.quiz_total += 1
            if user_choice == q["correct"]:
                st.success("🎯 Correct!")
                st.session_state.quiz_score += 1
            else:
                st.error(
                    f"❌ Incorrect. The right answer is:\n\n{q['correct']}"
                )
            q["user_answered"] = True

    with col2:
        if st.button("Next Question ➡️"):
            generate_quiz_question()
            st.rerun()