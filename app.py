import random
import streamlit as st

# Configure Streamlit Page
st.set_page_config(
    page_title="KS AEMT Pharmacology Suite", page_icon="🚑", layout="centered"
)

# -----------------------------------------------------------------------------
# MASTER MEDICATION DATASET (29 ENTRIES — sourced from Med Matrix reference card)
# -----------------------------------------------------------------------------
MEDICATIONS = [
    {
        "name": "Activated Charcoal",
        "category": "Toxicology / Overdose",
        "class": "Adsorbent",
        "route": "Oral",
        "indications": "Most oral poisonings or overdoses.",
        "contraindications": (
            "Decreased LOC, inability to maintain airway, overdose of"
            " corrosives, caustics, or petroleum substances."
        ),
        "adult_dose": "1 - 2 g/kg",
        "peds_dose": "1 - 2 g/kg",
    },
    {
        "name": "Oral Glucose",
        "category": "Endocrine / Glucose",
        "class": "Carbohydrate",
        "route": "Buccal/Oral",
        "indications": "Hypoglycemia.",
        "contraindications": (
            "Decreased LOC, inability to maintain airway, nausea and vomiting."
        ),
        "adult_dose": "15 g",
        "peds_dose": "15 g",
    },
    {
        "name": "Albuterol",
        "category": "Respiratory",
        "class": "Bronchodilator",
        "route": "Inhaled",
        "indications": "Asthma; difficulty breathing associated with wheezing.",
        "contraindications": (
            "None in true emergency. Consider tachycardia, cardiac chest pain."
        ),
        "adult_dose": "2.5 mg/3 cc",
        "peds_dose": "2.5 mg/3 cc",
    },
    {
        "name": "Epinephrine 1:1,000",
        "category": "Allergy / Anaphylaxis",
        "class": "Sympathomimetic",
        "route": "IM, Autoinjector",
        "indications": "Anaphylactic reaction.",
        "contraindications": (
            "None in true emergency. Consider cardiac chest pain, hypothermia,"
            " HTN."
        ),
        "adult_dose": "0.3 mg",
        "peds_dose": "0.01 mg/kg",
    },
    {
        "name": "Nitroglycerin (NTG)",
        "category": "Cardiac",
        "class": "Nitrate",
        "route": "Dermal, Sublingual",
        "indications": "Cardiac chest pain.",
        "contraindications": (
            "BP under 90 systolic, ED medications within the last 24 hours,"
            " head injuries."
        ),
        "adult_dose": "0.4 mg",
        "peds_dose": "Not indicated.",
    },
    {
        "name": "Aspirin (ASA)",
        "category": "Cardiac",
        "class": "Anti-platelet",
        "route": "Oral",
        "indications": (
            "Cardiac chest pain; OTC for headaches, minor aches and pains."
        ),
        "contraindications": "Active or recent bleeding.",
        "adult_dose": "324 mg chewable tablets (baby ASA is 81 mg)",
        "peds_dose": "Not indicated.",
    },
    {
        "name": "Zofran (Ondansetron)",
        "category": "GI / Antiemetic",
        "class": "Anti-emetic",
        "route": "Oral (ODT), IM/IV",
        "indications": "Nausea.",
        "contraindications": "Abnormal heart beat, allergic, pregnant.",
        "adult_dose": "4 mg - 8 mg",
        "peds_dose": "(<40 kg) 0.1 mg/kg",
    },
    {
        "name": "Narcan (Naloxone)",
        "category": "Toxicology / Overdose",
        "class": "Opiate Antagonist",
        "route": "IM, IV, IN, IO",
        "indications": "Opiate overdose.",
        "contraindications": "Hypersensitivity.",
        "adult_dose": "0.4 mg - 2 mg",
        "peds_dose": "0.1 mg/kg",
    },
    {
        "name": "Diphenhydramine HCL (Benadryl)",
        "category": "Allergy / Anaphylaxis",
        "class": "Anti-histamine",
        "route": "IM, IV, Oral",
        "indications": "Allergic reaction.",
        "contraindications": "Allergic, hypertension, constipation.",
        "adult_dose": "25 - 50 mg",
        "peds_dose": "1.0 - 2.0 mg/kg",
    },
    {
        "name": "Duo-Neb (Albuterol + Ipratropium Bromide)",
        "category": "Respiratory",
        "class": "Beta Agonist + Anticholinergic Bronchodilator",
        "route": "Inhaled",
        "indications": (
            "Bronchospasm in COPD; 2nd line for asthma attacks."
        ),
        "contraindications": "None in true emergency setting.",
        "adult_dose": "3.5 mg/3 ml (Ipratropium 0.50 mg / Albuterol 3 mg)",
        "peds_dose": "0.5 mg",
    },
    {
        "name": "Glucagon",
        "category": "Endocrine / Glucose",
        "class": "Hormone",
        "route": "IM, Auto-injector",
        "indications": (
            "Low BGL less than 50 and unable to swallow; altered mental"
            " status."
        ),
        "contraindications": "None in true emergency setting.",
        "adult_dose": "1 mg/ml",
        "peds_dose": "(<25 kg) 0.5 mg",
    },
    {
        "name": "Duo-Dote",
        "category": "Toxicology / Overdose",
        "class": "Parasympatholytic",
        "route": "Auto-injector",
        "indications": "Organophosphate poisoning.",
        "contraindications": "None in true emergency setting.",
        "adult_dose": "2 mg",
        "peds_dose": "Not specified on reference card.",
    },
    {
        "name": "Dextrose (D50)",
        "category": "Endocrine / Glucose",
        "class": "Carbohydrate",
        "route": "IV, IO",
        "indications": "Hypoglycemia.",
        "contraindications": "Hyperglycemia, intracranial hemorrhage.",
        "adult_dose": "25 gm/50 ml",
        "peds_dose": "1 gm/kg of D25",
    },
    {
        "name": "Midazolam",
        "category": "Neuro / Seizure",
        "class": "Sedative, Benzodiazepine, Anticonvulsant, Amnesic",
        "route": "IV, IO, IN",
        "indications": (
            "Seizures, status epilepticus, anxiety (depending on protocols)."
        ),
        "contraindications": (
            "Respiratory depression, hypersensitivity, CNS depression."
        ),
        "adult_dose": "1.0 - 2.5 mg",
        "peds_dose": "0.1 mg/kg (MAX 2 mg)",
    },
    {
        "name": "Diazepam (Valium)",
        "category": "Neuro / Seizure",
        "class": "Sedative, Benzodiazepine, Anticonvulsant",
        "route": "IV, IO, Rectal",
        "indications": (
            "Seizures, status epilepticus, anxiety (depending on protocols)."
        ),
        "contraindications": (
            "Respiratory depression, hypersensitivity, CNS depression."
        ),
        "adult_dose": "2 - 10 mg",
        "peds_dose": "0.5 - 1.0 mg/kg (MAX 2 mg)",
    },
    {
        "name": "Lorazepam (Ativan)",
        "category": "Neuro / Seizure",
        "class": "Sedative, Benzodiazepine, Anticonvulsant",
        "route": "IV, IO, IN, Rectal",
        "indications": (
            "Seizures, status epilepticus, anxiety (depending on protocols)."
        ),
        "contraindications": "Hypotension, hypersensitivity, CNS depression.",
        "adult_dose": "1 - 4 mg",
        "peds_dose": "0.1 mg/kg",
    },
    {
        "name": "Amiodarone (Cordarone)",
        "category": "Cardiac",
        "class": "Sedative, Antiarrhythmic Agent (Class III)",
        "route": "IV, IO",
        "indications": (
            "Cardiac arrest: ventricular fibrillation, pulseless ventricular"
            " tachycardia."
        ),
        "contraindications": (
            "2nd and 3rd degree blocks, cardiogenic shock, bradycardia."
        ),
        "adult_dose": "1st dose: 300 mg; 2nd dose: 150 mg",
        "peds_dose": "5 mg/kg (MAX 300 mg)",
    },
    {
        "name": "Epinephrine 1:10,000",
        "category": "Cardiac",
        "class": "Sympathomimetic",
        "route": "IV, IO",
        "indications": "Cardiac arrest.",
        "contraindications": "None in cardiac arrest.",
        "adult_dose": "1 mg/10 ml",
        "peds_dose": "0.01 mg/kg",
    },
    {
        "name": "Fentanyl (Sublimaze)",
        "category": "Pain Management",
        "class": "Analgesic Opioid",
        "route": "IV, IO, IN, IM",
        "indications": '"Pain relief."',
        "contraindications": (
            "Hypertensives to opiates, patients using MAOI's. Caution: ICP,"
            " bradycardia."
        ),
        "adult_dose": "1 mcg/kg (range 25 - 100 mcg)",
        "peds_dose": "1 mcg/kg",
    },
    {
        "name": "Morphine",
        "category": "Pain Management",
        "class": "Analgesic Opioid",
        "route": "IV, IO, IM",
        "indications": '"Pain relief."',
        "contraindications": (
            "Hypotension, hypersensitivity to morphine, head injury."
        ),
        "adult_dose": "2.0 - 10 mg",
        "peds_dose": "0.1 - 0.2 mg/kg",
    },
    {
        "name": "Lidocaine",
        "category": "Cardiac",
        "class": "Antiarrhythmic, Anesthetic",
        "route": "IV, IO",
        "indications": (
            "Ventricular fibrillation, pulseless V-Tach; anesthesia after IO"
            " insertion and before fluid or medication administration."
        ),
        "contraindications": "None in true emergency.",
        "adult_dose": (
            "Cardiac arrest: 1 mg/kg; IO anesthetic: 20 - 40 mg, flush 20 -"
            " 40 mg"
        ),
        "peds_dose": "IO anesthetic: 0.5 mg/kg",
    },
    {
        "name": "Tranexamic Acid (TXA)",
        "category": "IV Fluids / Hemorrhage",
        "class": "Antifibrinolytic Agent",
        "route": "IV, IO",
        "indications": (
            "Hemorrhagic shock within 3 hours, marked blood loss, initial"
            " systolic BP < 90."
        ),
        "contraindications": "Hemorrhagic shock from non-traumatic causes.",
        "adult_dose": "1 g/10 ml placed in 100 ml, given over 10 min",
        "peds_dose": "Adults only.",
    },
    {
        "name": "Methylprednisolone (Solu-Medrol)",
        "category": "Respiratory",
        "class": "Corticosteroid",
        "route": "IV, IM, IO",
        "indications": "Respiratory distress.",
        "contraindications": "Premature infants, hypersensitivity.",
        "adult_dose": "125 - 250 mg",
        "peds_dose": "1.0 - 2.0 mg/kg",
    },
    {
        "name": "Ketorolac (Toradol)",
        "category": "Pain Management",
        "class": "Non-Steroidal Anti-inflammatory Drug (NSAID)",
        "route": "IV, IO",
        "indications": '"Pain relief."',
        "contraindications": (
            "Hypersensitivity to ASA or NSAIDs, ulcers, GI bleeds, taking"
            " blood thinners."
        ),
        "adult_dose": "30 - 60 mg IV",
        "peds_dose": "0.5 mg/kg IV",
    },
    {
        "name": "Ipratropium",
        "category": "Respiratory",
        "class": "Anticholinergic Bronchodilator",
        "route": "Inhaled",
        "indications": "Acute bronchospasm.",
        "contraindications": "Hypersensitivity to ipratropium or atropine.",
        "adult_dose": "0.5 mg",
        "peds_dose": "0.5 mg",
    },
    {
        "name": "Promethazine (Phenergan)",
        "category": "GI / Antiemetic",
        "class": "Antiemetic, Phenothiazine",
        "route": "IM (preferred) or IV",
        "indications": "Nausea and vomiting.",
        "contraindications": (
            "Known hypersensitivity, narrow angle glaucoma, Parkinson's"
            " disease."
        ),
        "adult_dose": "12.5 - 25 mg",
        "peds_dose": "(>2 yr) 0.25 - 0.5 mg/kg",
    },
    {
        "name": "D5W (5% Dextrose in 100 ml)",
        "category": "IV Fluids / Hemorrhage",
        "class": "Crystalloid, Isotonic (becomes hypotonic)",
        "route": "IV, IO",
        "indications": "Dehydration, hypoglycemia, hyponatremia.",
        "contraindications": (
            "Hyperglycemia, DKA, head bleeds, intracranial pressure."
        ),
        "adult_dose": "5 - 10 ml/kg (renal/cardiac/edema issues)",
        "peds_dose": "20 ml/kg",
    },
    {
        "name": "Lactated Ringers",
        "category": "IV Fluids / Hemorrhage",
        "class": "Crystalloid",
        "route": "IV, IO",
        "indications": (
            "Burns; med administration (TKO) or volume replacement with"
            " electrolytes (sodium, chloride, calcium, and lactate)."
        ),
        "contraindications": "Blood transfusions.",
        "adult_dose": "5 - 10 ml/kg (renal/cardiac/edema issues)",
        "peds_dose": "20 ml/kg",
    },
    {
        "name": "Normal Saline",
        "category": "IV Fluids / Hemorrhage",
        "class": "Crystalloid",
        "route": "IV, IO",
        "indications": (
            "Med administration (TKO) or volume replacement with"
            " electrolytes (sodium, chloride)."
        ),
        "contraindications": "None.",
        "adult_dose": "5 - 10 ml/kg (renal/cardiac/edema issues)",
        "peds_dose": "20 ml/kg",
    },
]

# -----------------------------------------------------------------------------
# CATEGORIES
# -----------------------------------------------------------------------------
ALL_CATEGORIES = sorted({m["category"] for m in MEDICATIONS})

# Fields the quiz can ask about, and how each is labeled in a question.
QUIZ_FIELDS = {
    "class": "pharmacological class",
    "route": "route of administration",
    "indications": "indication(s)",
    "contraindications": "contraindication(s)",
    "adult_dose": "adult dose",
}


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

if "selected_categories" not in st.session_state:
    st.session_state.selected_categories = list(ALL_CATEGORIES)
if "selected_qtypes" not in st.session_state:
    st.session_state.selected_qtypes = list(QUIZ_FIELDS.keys())

# -----------------------------------------------------------------------------
# HELPER FUNCTIONS
# -----------------------------------------------------------------------------


def generate_quiz_question(pool, q_types):
    """Generates a dynamic multiple choice question from the given pool,
    asking only about fields in q_types."""
    target = random.choice(pool)
    q_type = random.choice(q_types)

    correct_ans = target[q_type]

    # Prefer distractors from the same filtered pool; fall back to the full
    # dataset if the pool is too small to supply enough wrong answers.
    other_in_pool = [m for m in pool if m["name"] != target["name"]]
    if len(other_in_pool) >= 1:
        distractor_source = other_in_pool
    else:
        distractor_source = [
            m for m in MEDICATIONS if m["name"] != target["name"]
        ]

    wrong_choices = random.sample(
        [m[q_type] for m in distractor_source],
        min(3, len(distractor_source)),
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

# Category filter — applies to both Flashcards and the Quiz
st.sidebar.divider()
st.sidebar.subheader("📂 Categories")

sel_col1, sel_col2 = st.sidebar.columns(2)
with sel_col1:
    if st.button("Select All", use_container_width=True):
        st.session_state.selected_categories = list(ALL_CATEGORIES)
        st.rerun()
with sel_col2:
    if st.button("Clear All", use_container_width=True):
        st.session_state.selected_categories = []
        st.rerun()

selected_categories = st.sidebar.multiselect(
    "Study only these categories:",
    options=ALL_CATEGORIES,
    default=st.session_state.selected_categories,
    key="selected_categories",
)

filtered_meds = [
    m for m in MEDICATIONS if m["category"] in selected_categories
]

if not filtered_meds:
    st.warning(
        "⚠️ No categories selected. Choose at least one category in the"
        " sidebar to continue."
    )
    st.stop()

# Reset navigation/quiz state whenever the category selection changes
filtered_names = tuple(m["name"] for m in filtered_meds)
if st.session_state.get("_filtered_names") != filtered_names:
    st.session_state._filtered_names = filtered_names
    st.session_state.card_idx = 0
    st.session_state.show_back = False
    st.session_state.current_question = None

# Quiz field filter — only relevant in Quiz mode
if mode == "Multiple Choice Quiz":
    st.sidebar.divider()
    st.sidebar.subheader("❓ Quiz Me On")

    qsel_col1, qsel_col2 = st.sidebar.columns(2)
    with qsel_col1:
        if st.button("Select All", use_container_width=True, key="qtypes_all"):
            st.session_state.selected_qtypes = list(QUIZ_FIELDS.keys())
            st.rerun()
    with qsel_col2:
        if st.button("Clear All", use_container_width=True, key="qtypes_none"):
            st.session_state.selected_qtypes = []
            st.rerun()

    selected_qtypes = st.sidebar.multiselect(
        "Which fields should questions come from?",
        options=list(QUIZ_FIELDS.keys()),
        format_func=lambda k: QUIZ_FIELDS[k],
        default=st.session_state.selected_qtypes,
        key="selected_qtypes",
    )

    if not selected_qtypes:
        st.warning(
            "⚠️ No question fields selected. Choose at least one field"
            " (e.g. route, dose, class) in the sidebar to continue."
        )
        st.stop()

    # Reset the current question whenever the field selection changes
    qtypes_tuple = tuple(sorted(selected_qtypes))
    if st.session_state.get("_selected_qtypes_snapshot") != qtypes_tuple:
        st.session_state._selected_qtypes_snapshot = qtypes_tuple
        st.session_state.current_question = None

# =============================================================================
# MODE 1: TRADITIONAL TWO-SIDED FLASHCARDS
# =============================================================================
if mode == "Flashcards":
    st.header("Interactive Two-Sided Flashcards")
    st.caption(f"Showing {len(filtered_meds)} of {len(MEDICATIONS)} medications")

    total_cards = len(filtered_meds)
    st.session_state.card_idx = st.session_state.card_idx % total_cards
    current_card = filtered_meds[st.session_state.card_idx]

    # Card Progress
    st.progress((st.session_state.card_idx + 1) / total_cards)
    st.caption(f"Medication {st.session_state.card_idx + 1} of {total_cards}")

    # Card Container
    with st.container(border=True):
        st.subheader(f"💊 {current_card['name']}")
        st.caption(f"🏷️ {current_card['category']}")

        if not st.session_state.show_back:
            st.info("👆 Click **Flip Card** to view detailed pharmacology.")
        else:
            st.markdown(f"**Class:** {current_card['class']}")
            st.markdown(f"**Route:** {current_card['route']}")
            st.markdown(f"**Indications:** {current_card['indications']}")
            st.markdown(
                f"**Contraindications:** {current_card['contraindications']}"
            )
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
    st.caption(
        f"Quizzing on {len(filtered_meds)} of {len(MEDICATIONS)} medications"
    )

    # Metrics on sidebar
    st.sidebar.metric(
        "Current Score",
        f"{st.session_state.quiz_score} / {st.session_state.quiz_total}",
    )

    if st.session_state.current_question is None:
        generate_quiz_question(filtered_meds, selected_qtypes)

    q = st.session_state.current_question

    st.write(
        f"**Question:** What is the correct **{QUIZ_FIELDS[q['q_type']]}** for"
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
            generate_quiz_question(filtered_meds, selected_qtypes)
            st.rerun()