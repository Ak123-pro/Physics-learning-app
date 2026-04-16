import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Physics Lab — National",
                   page_icon="⚛️", layout="wide",
                   initial_sidebar_state="collapsed")

# ─── Global CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap');
html,body,[class*="css"]{font-family:'Nunito',sans-serif!important}
#MainMenu,footer,header{visibility:hidden}
.block-container{padding:.4rem .8rem 2rem!important;max-width:780px!important;margin:auto}

/* Header */
.hdr{background:linear-gradient(135deg,#0a0a1a 0%,#12122a 40%,#1a1040 100%);
  color:white;padding:1rem 1.4rem;border-radius:22px;margin-bottom:.8rem;
  text-align:center;border:1px solid rgba(255,255,255,.08);
  box-shadow:0 8px 32px rgba(0,0,0,.4)}
.hdr h1{font-size:1.25rem;margin:0;font-weight:900;
  background:linear-gradient(90deg,#a78bfa,#60a5fa,#34d399);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent}
.hdr p{font-size:.73rem;margin:.25rem 0 0;opacity:.7;color:#ccc}

/* Cards */
.topic-card{border-radius:18px;padding:1rem 1.1rem;margin-bottom:.6rem;
  border:2px solid rgba(255,255,255,.06);cursor:pointer;
  box-shadow:0 4px 20px rgba(0,0,0,.12);transition:transform .2s}
.topic-card:hover{transform:translateY(-2px)}
.glass-card{background:rgba(255,255,255,.03);backdrop-filter:blur(10px);
  border:1px solid rgba(255,255,255,.08);border-radius:20px;padding:1.2rem}

/* Nav pills */
.nav-pill{display:inline-flex;gap:6px;background:rgba(0,0,0,.2);
  padding:5px;border-radius:30px;margin-bottom:.8rem}

/* Note sections */
.note-card{background:white;border-radius:16px;padding:1.1rem;
  margin-bottom:.7rem;border:1px solid #eef0f8;
  box-shadow:0 2px 12px rgba(0,0,0,.06)}
.note-card h4{margin:0 0 .5rem;font-size:.96rem;color:#1e1b4b}
.note-body{font-size:.87rem;line-height:1.85;color:#374151;white-space:pre-line}
.fact-box{background:linear-gradient(135deg,#fef3c7,#fde68a);border-radius:12px;
  padding:.7rem 1rem;margin-top:.6rem;font-size:.82rem;color:#78350f;font-weight:600}
.mem-card{background:linear-gradient(135deg,#7c3aed,#db2777);
  color:white;border-radius:16px;padding:.9rem 1.1rem;margin:.7rem 0;font-size:.86rem}
.tip-card{background:#fffbeb;border:2px solid #fbbf24;border-radius:14px;
  padding:.9rem 1rem;margin-top:.6rem}

/* Score */
.score-hero{background:linear-gradient(135deg,#0a0a1a,#1e1b4b,#312e81);
  color:white;text-align:center;padding:2rem;border-radius:22px;
  box-shadow:0 12px 40px rgba(0,0,0,.4)}

/* XP bar */
.xp-wrap{background:#1e1b4b;border-radius:20px;height:8px;margin:3px 0;overflow:hidden}
.xp-fill{height:8px;border-radius:20px;
  background:linear-gradient(90deg,#7c3aed,#2563eb,#059669)}

/* Steps */
.steps{display:flex;align-items:center;gap:4px;margin-bottom:.8rem;
  background:rgba(0,0,0,.15);padding:8px 12px;border-radius:30px}

@media(max-width:480px){
  .hdr h1{font-size:1rem}
  .block-container{padding:.3rem .4rem 2rem!important}
}
</style>
""", unsafe_allow_html=True)

# ─── Session State ────────────────────────────────────────────────────────────
def init():
    d = dict(screen="home", grade="Grade 9", name="", onboarded=False,
             tid=None, stage="story",
             quiz_i=0, quiz_ans=False, quiz_sel=None, quiz_sc=0,
             done=set(), scores={}, xp=0, stars=0, streak=1,
             dark=True)
    for k,v in d.items():
        if k not in st.session_state: st.session_state[k]=v
init()
S = st.session_state

def go(s): S.screen=s; st.rerun()
def begin(tid):
    S.tid=tid; S.stage="story"
    S.quiz_i=0; S.quiz_ans=False; S.quiz_sel=None; S.quiz_sc=0
    S.screen="topic"; st.rerun()

# ─── ALL PHYSICS CONTENT ──────────────────────────────────────────────────────
# Each topic: id, title, emoji, color, grade, tagline, story, games[], note{}, quiz[]
# Game types: "projectile","pendulum","circuit","wave","collision","gravity_well",
#             "optics","gas_law","freefall","ohm_builder","lens_builder","force_balance"

TOPICS = {
"Grade 8":[
 {
  "id":"g8_motion","title":"Motion & Kinematics","emoji":"🚀","color":"#3b82f6",
  "grade":"Grade 8","chapter":"Chapter 1",
  "tagline":"Launch rockets and discover the laws of motion!",
  "story":{"title":"🚀 Launch Day!",
   "text":"Mission Control: T-minus 10 seconds! Riya's team is about to launch a model rocket. The rocket goes UP, slows down, stops, and falls back. In those few seconds, EVERY concept of kinematics plays out — velocity, acceleration, displacement, free fall. Let's become rocket scientists!"},
  "games":[
   {"type":"projectile","title":"🚀 Projectile Rocket Launcher",
    "desc":"Set angle & speed — watch the rocket fly! Land on the target!"},
   {"type":"freefall","title":"🌍 Free Fall Simulator",
    "desc":"Drop objects from different heights — measure fall time!"},
   {"type":"velocity_graph","title":"📈 Velocity-Time Graph Builder",
    "desc":"Drive a car — see its v-t graph draw in real time!"},
  ],
  "note":{
   "sections":[
    {"h":"🚗 Distance vs Displacement","body":"DISTANCE: total path length (scalar — no direction)\nDISPLACEMENT: shortest straight line, start→end (vector — has direction)\n\nExample: Run 400m around a track and return:\n• Distance = 400 m\n• Displacement = 0 m (same start and end point!)\n\nSpeed = Distance/Time (scalar)\nVelocity = Displacement/Time (vector)","fact":"🌟 A homing pigeon flies 500 km but its displacement might be only 50 km — straight line home!"},
    {"h":"⚡ Equations of Motion","body":"For UNIFORM ACCELERATION (memorise all three!):\n\n1️⃣  v = u + at\n2️⃣  s = ut + ½at²\n3️⃣  v² = u² + 2as\n\nu = initial velocity, v = final velocity\na = acceleration, t = time, s = displacement\n\nFor FREE FALL: u=0, a=g=9.8 m/s² (downward)","fact":"🌟 Galileo proved in 1589 that all objects fall at the SAME rate — mass doesn't matter!"},
    {"h":"📈 Motion Graphs","body":"Distance-Time Graph:\n• Slope = Speed\n• Horizontal line = at rest\n• Curve upward = accelerating\n\nVelocity-Time Graph:\n• Slope = Acceleration\n• Area under line = Displacement\n• Horizontal line = constant velocity\n• Line going up = positive acceleration","fact":None},
    {"h":"🎯 Projectile Motion","body":"When an object is thrown at an angle, it has:\n• Horizontal: constant velocity (no force)\n• Vertical: constant acceleration (gravity = 9.8 m/s²)\n\nRange = u²sin(2θ)/g  (maximum at θ = 45°!)\nMax height = u²sin²θ/2g\nTime of flight = 2u sinθ/g","fact":"🌟 A ball thrown at 45° travels the FURTHEST! That's why javelin throwers aim at ~45°."},
   ],
   "memory":"🧠 'SuVaT' — the 5 variables: s, u, v, a, t. Know 3, find the other 2!",
   "tips":["Speed=scalar (no direction), Velocity=vector (has direction)","Free fall: a=g=9.8 m/s², initial velocity=0","Max range of projectile at θ=45°","Area under v-t graph = displacement; slope of v-t = acceleration"]
  },
  "quiz":[
   {"q":"A ball is thrown upward at 20 m/s. Using v=u+at, time to reach max height (g=10)?","opts":["1 s","2 s","4 s","10 s"],"ans":1,"exp":"At max height, v=0. 0=20+(-10)t → t=2 s"},
   {"q":"In a v-t graph, what does the AREA under the line represent?","opts":["Speed","Acceleration","Displacement","Force"],"ans":2,"exp":"Area under v-t graph = Displacement. Slope of v-t graph = acceleration!"},
   {"q":"Projectile launched at 45°. The range is MAXIMUM because:","opts":["sin(90°)=1, so sin(2×45°)=sin(90°)=1 — maximum","45° looks good","gravity is less at 45°","speed is highest"],"ans":0,"exp":"Range = u²sin(2θ)/g. sin(2θ) is maximum when 2θ=90° → θ=45°!"},
   {"q":"Free fall from rest. After 3 seconds, velocity = (g=10)?","opts":["3 m/s","10 m/s","30 m/s","90 m/s"],"ans":2,"exp":"v=u+at=0+(10×3)=30 m/s. Objects gain 10 m/s every second in free fall!"},
   {"q":"A car travels 100m in 5s then 200m in 5s. Average speed = ?","opts":["30 m/s","60 m/s","20 m/s","40 m/s"],"ans":0,"exp":"Total distance=300m, total time=10s. Avg speed=300/10=30 m/s"},
  ]
 },
 {
  "id":"g8_forces","title":"Force, Pressure & Friction","emoji":"💥","color":"#ef4444",
  "grade":"Grade 8","chapter":"Chapter 2",
  "tagline":"Balance forces, crush pressure, beat friction!",
  "story":{"title":"💥 The Tug of War!",
   "text":"Two teams pull a rope. When forces are EQUAL, nobody moves (balanced forces). When one team pulls harder, the rope — and everyone — accelerates toward them. This is Newton's world! Forces create acceleration, pressure hurts if concentrated, and friction is why we can walk without sliding everywhere."},
  "games":[
   {"type":"force_balance","title":"⚖️ Force Balance Challenge",
    "desc":"Add/remove forces on both sides — keep the block balanced then accelerate it!"},
   {"type":"pressure_sim","title":"🔩 Pressure Crusher",
    "desc":"Same force, different areas — see which nail goes deeper!"},
   {"type":"friction_racer","title":"🏎️ Friction Surface Racer",
    "desc":"Race your car on different surfaces — discover friction coefficients!"},
  ],
  "note":{
   "sections":[
    {"h":"💪 Newton's Laws","body":"1st Law: Object stays at rest OR moves at constant velocity unless a NET force acts.\n(This is INERTIA — resistance to change)\n\n2nd Law: F = m × a\n(Net force = mass × acceleration)\n\n3rd Law: Every action has equal & opposite reaction\n(Act on DIFFERENT objects — they never cancel!)","fact":"🌟 A rocket works by Newton's 3rd Law — exhaust gas pushed DOWN → rocket pushed UP!"},
    {"h":"⚖️ Pressure","body":"P = F ÷ A\nUnit: Pascal (Pa) = N/m²\n\nSmaller area → MORE pressure (same force)\nLarger area → LESS pressure\n\nExamples:\n• Knife: thin edge = tiny area = huge pressure\n• Snowshoes: wide = large area = less pressure\n• Camel feet: wide = spread weight on sand\n• Dam: walls thicker at bottom (more water pressure below)","fact":"🌟 A stiletto heel concentrates more pressure than an elephant's foot — it can damage hardwood floors!"},
    {"h":"🛞 Friction","body":"Types (strongest → weakest):\n• Static friction (prevents motion)\n• Kinetic/Sliding friction (during sliding)\n• Rolling friction (wheels)\n• Fluid friction (in liquids/gases)\n\nf = μN  (μ = coefficient of friction, N = normal force)\n\nAdvantages: walking, braking, writing\nDisadvantages: wear, heat, energy loss\n\nReduce friction: lubricants, ball bearings, streamlining","fact":"🌟 Ice has μ≈0.03 (very slippery!). Rubber on dry road: μ≈0.7. That's why cars brake well on dry roads!"},
   ],
   "memory":"🧠 'F=ma' and 'P=F/A' — the two most important formulas in this chapter. Learn them cold!",
   "tips":["Net force = sum of ALL forces (with direction)","More area = LESS pressure (same force)","Static friction > kinetic friction","Weight W=mg (in Newtons, not kg!)","μ (mu) = friction coefficient: 0=frictionless, 1=very rough"]
  },
  "quiz":[
   {"q":"F=ma. A 4 kg block accelerates at 5 m/s². Net force = ?","opts":["0.8 N","9 N","20 N","1.25 N"],"ans":2,"exp":"F=ma=4×5=20 N"},
   {"q":"Same force on a nail tip (0.001m²) vs flat board (0.1m²). Which has more pressure?","opts":["Flat board","Nail tip","Same pressure","Depends on material"],"ans":1,"exp":"P=F/A. Nail: F/0.001 = 1000F. Board: F/0.1=10F. Nail has 100× more pressure!"},
   {"q":"A car stops faster on dry road than wet road. This is because:","opts":["More gravity on dry road","Higher friction coefficient on dry road","Less weight on wet road","Car engine helps on dry road"],"ans":1,"exp":"Dry road has higher μ → more friction force → faster deceleration → shorter stopping distance!"},
   {"q":"Action and reaction forces act on:","opts":["Same object and cancel","Different objects","Same object but don't cancel","Always the same surface"],"ans":1,"exp":"Newton's 3rd: action-reaction always on DIFFERENT objects — they CANNOT cancel because they're not on the same body!"},
   {"q":"Atmospheric pressure at sea level ≈","opts":["100 Pa","10,000 Pa","101,325 Pa","1,000,000 Pa"],"ans":2,"exp":"Atmospheric pressure ≈ 101,325 Pa = 1 atm = 760 mmHg"},
  ]
 },
 {
  "id":"g8_sound","title":"Sound, Waves & Music","emoji":"🎵","color":"#8b5cf6",
  "grade":"Grade 8","chapter":"Chapter 3",
  "tagline":"Make music, send echoes, ride the waves of sound!",
  "story":{"title":"🎵 The Concert Hall Mystery!",
   "text":"Why do concert halls sound SO much better than a classroom? Architects carefully control how sound BOUNCES and ABSORBS. Dolphins 'see' with sound underwater. Bats navigate dark caves perfectly using ultrasound. Sound is invisible but shapes our entire world of hearing!"},
  "games":[
   {"type":"wave","title":"〰️ Sound Wave Lab",
    "desc":"Draw sound waves — change frequency (pitch) and amplitude (volume)!"},
   {"type":"echo_sonar","title":"🦇 SONAR Echo Challenge",
    "desc":"Send pulses and calculate distance from echo time — like a bat or submarine!"},
   {"type":"string_wave","title":"🎸 Guitar String Simulator",
    "desc":"Pluck virtual strings — see standing waves and harmonics form!"},
  ],
  "note":{
   "sections":[
    {"h":"🔊 What is Sound?","body":"Sound = mechanical longitudinal wave (particles vibrate parallel to wave direction)\n\nNeeds a MEDIUM — cannot travel in vacuum!\nSpeed in air: 343 m/s at 20°C\nSpeed in water: ~1480 m/s  \nSpeed in steel: ~5960 m/s\n→ Solid > Liquid > Gas\n\nWave equation: v = f × λ\n(speed = frequency × wavelength)","fact":"🌟 You see lightning before hearing thunder because light (3×10⁸ m/s) is nearly a million times faster than sound!"},
    {"h":"🎵 Sound Properties","body":"FREQUENCY (f): vibrations/second → Unit: Hz → determines PITCH\n• Low freq (20-500 Hz): bass, rumbling\n• High freq (5000-20000 Hz): treble, high-pitched\n• Human range: 20–20,000 Hz\n\nAMPLITUDE: max displacement → determines LOUDNESS (dB)\nWAVELENGTH (λ): distance between compressions\n\nInfrasound: <20 Hz (elephants, earthquakes)\nUltrasound: >20,000 Hz (bats, SONAR, medical scans)","fact":"🌟 Blue whales produce sounds at 188 dB — louder than a jet engine — heard 1,600 km away!"},
    {"h":"📣 Reflection & Resonance","body":"ECHO: reflected sound heard ≥0.1s after original\nMinimum distance = 343×0.1÷2 = 17.15 m\n\nREVERBERATION: multiple rapid reflections merging\n→ Used in concert hall design\n\nRESONANCE: vibration at natural frequency → max amplitude\nExamples: tuning fork, opera singer breaking glass!\n\nSTANDING WAVES on string:\nfundamental f₁ = v/2L\nHarmonics: f₂=2f₁, f₃=3f₁...","fact":"🌟 Tacoma Narrows Bridge (1940) collapsed due to resonance with wind — an engineering disaster caused by physics!"},
   ],
   "memory":"🧠 'v=fλ' — velocity equals frequency times wavelength. True for ALL waves!",
   "tips":["Sound needs medium — NO travel in vacuum","Speed of sound: Solid>Liquid>Gas","Frequency=pitch, Amplitude=loudness","Echo needs min 17m distance","v=fλ — memorise this wave equation!"]
  },
  "quiz":[
   {"q":"f=500 Hz, λ=0.686 m. Wave speed = ?","opts":["343 m/s","500 m/s","1000 m/s","0.686 m/s"],"ans":0,"exp":"v=fλ=500×0.686=343 m/s — speed of sound in air!"},
   {"q":"Sound from a bat returns as echo after 0.02 s. Distance to object = (v=340m/s)?","opts":["6.8 m","3.4 m","0.34 m","34 m"],"ans":1,"exp":"Distance=v×t÷2=340×0.02÷2=3.4 m (divide by 2 because sound travels THERE and BACK!)"},
   {"q":"Which property of sound determines its PITCH?","opts":["Amplitude","Speed","Frequency","Wavelength×amplitude"],"ans":2,"exp":"PITCH is determined by FREQUENCY. High frequency = high pitch. Loudness is determined by amplitude!"},
   {"q":"A concert hall is designed to use reverberation for better sound. Reverberation means:","opts":["Sound speeding up","Multiple rapid reflections merging","Echo after 0.1 seconds","Sound slowing down"],"ans":1,"exp":"Reverberation: multiple sound reflections reach the listener in rapid succession, creating a fuller sound!"},
   {"q":"Ultrasound is used in medical imaging because:","opts":["It's cheaper","It's visible to eyes","High frequency gives better image resolution","It travels in vacuum"],"ans":2,"exp":"High frequency=short wavelength=can detect smaller details. Ultrasound scans show baby development, organ structures!"},
  ]
 },
],
"Grade 9":[
 {
  "id":"g9_newton","title":"Newton's Laws & Momentum","emoji":"🍎","color":"#10b981",
  "grade":"Grade 9","chapter":"Chapter 1",
  "tagline":"Collide, conserve, and conquer momentum!",
  "story":{"title":"🍎 The Billiard Ball Revelation!",
   "text":"A billiard ball hits another and transfers ALL its momentum — stops dead while the other flies off. This isn't magic — it's Newton's laws and conservation of momentum working perfectly. The same physics governs car crashes, rocket launches, and even how the Sun burns. Master momentum, master the universe!"},
  "games":[
   {"type":"collision","title":"💥 Elastic Collision Lab",
    "desc":"Launch balls at each other — watch momentum and energy transfer in real time!"},
   {"type":"force_balance","title":"⚖️ Newton's 2nd Law Sandbox",
    "desc":"Apply forces to objects of different masses — discover F=ma live!"},
   {"type":"projectile","title":"🎯 Cannon Ball Challenge",
    "desc":"Hit moving targets using projectile physics — adjust angle and power!"},
  ],
  "note":{
   "sections":[
    {"h":"🍎 Three Laws Summarised","body":"1st (Inertia): No net force → no change in motion\nMore mass = more inertia = harder to start/stop\n\n2nd: F = ma  (Net Force = Mass × Acceleration)\nDouble force → double acceleration\nDouble mass → half acceleration\n\n3rd: Action = −Reaction (on DIFFERENT objects!)\n\nMomentum: p = mv (kg·m/s)\nImpulse: J = FΔt = Δp","fact":"🌟 Car airbags increase the time of impact, reducing the FORCE on passengers (J=FΔt — same impulse, more time = less force)!"},
    {"h":"💥 Conservation of Momentum","body":"When no external force acts:\nTotal momentum before = Total momentum after\n\nm₁u₁ + m₂u₂ = m₁v₁ + m₂v₂\n\nTypes of collision:\nELASTIC: KE conserved (billiard balls)\nINELASTIC: KE lost (clay hitting clay)\nPERFECTLY INELASTIC: objects stick together\n\nExplosion (reverse collision):\n0 = m₁v₁ + m₂v₂ (total momentum still zero!)","fact":"🌟 When a gun fires, bullet + gun initially have ZERO momentum. After firing: bullet goes one way, gun recoils the other — total still zero!"},
    {"h":"🚀 Applications","body":"• Rockets: eject gas backward → move forward\n• Recoil of gun\n• Jet engines: push air back → plane moves forward\n• Catching a ball: hands move back (increase time → reduce force)\n• Car crumple zones: absorb impact (increase time)\n• Seatbelts: spread force over time","fact":None},
   ],
   "memory":"🧠 'Momentum is ALWAYS conserved when no external force acts' — this is LAW, not suggestion!",
   "tips":["p=mv (momentum), J=FΔt (impulse)","Elastic: KE+momentum conserved. Inelastic: only momentum conserved","Newton's 3rd: forces on DIFFERENT objects","F=ma uses NET force (all forces combined)","For explosions: total momentum = 0 if starts from rest"]
  },
  "quiz":[
   {"q":"2 kg ball at 6 m/s hits stationary 2 kg ball. After elastic collision, first ball:","opts":["Stops, second moves at 6 m/s","Both move at 3 m/s","First moves at 3 m/s","Both stop"],"ans":0,"exp":"In elastic collision between equal masses, first ball STOPS and second moves at the first ball's original speed — momentum and KE both conserved!"},
   {"q":"Momentum of 5 kg object at 10 m/s = ?","opts":["0.5 kg·m/s","2 kg·m/s","50 kg·m/s","15 kg·m/s"],"ans":2,"exp":"p=mv=5×10=50 kg·m/s"},
   {"q":"Why do car airbags save lives?","opts":["They're soft","They increase impact time → reduce force (J=FΔt)","They absorb all momentum","They reduce car speed"],"ans":1,"exp":"J=FΔt. Airbags increase Δt → smaller F for same impulse J. Less force on head = less injury!"},
   {"q":"A 60 kg astronaut pushes a 20 kg toolbox away at 3 m/s. Astronaut moves at:","opts":["1 m/s opposite","3 m/s same","9 m/s opposite","1 m/s same"],"ans":0,"exp":"Conservation: 0=60v+20×3. 60v=-60. v=-1 m/s (opposite direction to toolbox)"},
   {"q":"Impulse = ?","opts":["mv","F×t","½mv²","ma"],"ans":1,"exp":"Impulse J = Force × time = FΔt = change in momentum Δp"},
  ]
 },
 {
  "id":"g9_gravity","title":"Gravitation & Orbits","emoji":"🌍","color":"#06b6d4",
  "grade":"Grade 9","chapter":"Chapter 2",
  "tagline":"Orbit planets and feel the pull of the cosmos!",
  "story":{"title":"🌍 Orbiting on the Edge!",
   "text":"The ISS travels at 7.7 km/s. If it slows down, it falls to Earth. If it speeds up, it escapes to space. At exactly the right speed, it keeps 'falling around' Earth — an orbit! This is ALL gravity does. Newton unified earthly falling and planetary orbiting into ONE equation. Mind-blowing!"},
  "games":[
   {"type":"gravity_well","title":"🌌 Gravity Well Orbit Simulator",
    "desc":"Launch satellites — find the perfect speed to achieve stable orbit!"},
   {"type":"freefall","title":"🌕 Moon vs Earth Drop",
    "desc":"Drop objects on Earth AND Moon — compare accelerations!"},
   {"type":"projectile","title":"🛸 Orbital Slingshot",
    "desc":"Use gravity assists to slingshot your probe to different planets!"},
  ],
  "note":{
   "sections":[
    {"h":"🌍 Newton's Law of Gravitation","body":"F = G × m₁ × m₂ / r²\n\nG = 6.67×10⁻¹¹ N·m²/kg² (Universal constant)\nF is always ATTRACTIVE\nInverse Square Law: double distance → ¼ force\n\ng on Earth surface:\ng = GM/R² = 9.8 m/s² ≈ 10 m/s²\n\ng changes with:\n• Altitude (decreases going up)\n• Location (slightly more at poles)\n• Planet (Moon: 1.6 m/s², Mars: 3.7 m/s²)","fact":"🌟 You and your phone attract each other with ~10⁻⁷ N of gravitational force — far too small to feel!"},
    {"h":"⚖️ Weight vs Mass","body":"MASS: amount of matter (scalar, constant everywhere)\nUnit: kg — never changes\n\nWEIGHT: gravitational force on mass\nW = mg\nUnit: Newton (N) — changes with location!\n\n60 kg person:\n• Earth: 60×10 = 600 N\n• Moon: 60×1.6 = 96 N\n• Space (no gravity): 0 N (mass still 60 kg!)","fact":"🌟 You weigh slightly LESS at the equator than poles — equator is farther from Earth's centre AND spins faster!"},
    {"h":"🛸 Orbital Motion","body":"Orbital velocity: v = √(GM/r)\n\nISS orbital speed: ~7.7 km/s\nEscape velocity from Earth: 11.2 km/s\n\nKepler's Laws:\n1. Elliptical orbits (Sun at one focus)\n2. Equal areas in equal times (faster near Sun)\n3. T² ∝ r³ (period² ∝ radius³)\n\nGeostationary orbit: 35,786 km altitude\nOrbital period = 24 hours (appears fixed in sky)\n→ GPS satellites, weather satellites, TV satellites!","fact":"🌟 GPS satellites run slightly slower due to lower gravity, causing time dilation — engineers must correct for relativity to keep GPS accurate!"},
   ],
   "memory":"🧠 'F=Gm₁m₂/r²' — gravity law. r doubles → force becomes ¼ (INVERSE SQUARE)!",
   "tips":["F∝1/r² (inverse square law)","Mass constant; weight changes with g","W=mg in Newtons","g on Moon ≈ g_Earth/6","Escape velocity from Earth = 11.2 km/s"]
  },
  "quiz":[
   {"q":"If distance between Earth and Moon doubles, gravity between them becomes:","opts":["Half","Quarter","Double","Same"],"ans":1,"exp":"F∝1/r². Double r → F becomes 1/4. Inverse square law!"},
   {"q":"60 kg person on Moon (g=1.6 m/s²). Weight = ?","opts":["60 N","600 N","96 N","37.5 N"],"ans":2,"exp":"W=mg=60×1.6=96 N. Mass is still 60 kg (unchanged), only weight changes!"},
   {"q":"Geostationary satellite orbital period is:","opts":["1 hour","12 hours","24 hours","1 year"],"ans":2,"exp":"Geostationary = 24 hours orbital period, so it appears FIXED in sky. Used for TV, GPS, weather!"},
   {"q":"Escape velocity from Earth ≈","opts":["7.7 km/s","11.2 km/s","3 km/s","340 m/s"],"ans":1,"exp":"Escape velocity = 11.2 km/s (to escape Earth's gravity completely). ISS orbital velocity = 7.7 km/s (lower — stays in orbit)"},
   {"q":"Kepler's 3rd law: T² ∝ r³ means:","opts":["Farther planet = longer year","Closer planet = longer year","All planets have same period","Period doesn't depend on distance"],"ans":0,"exp":"T²∝r³ → farther planets have longer orbital periods. Earth: 1 year, Mars: 1.88 years, Jupiter: 11.86 years!"},
  ]
 },
],
"Grade 10":[
 {
  "id":"g10_elec","title":"Electricity & Circuits","emoji":"⚡","color":"#f59e0b",
  "grade":"Grade 10","chapter":"Chapter 1",
  "tagline":"Wire your own circuits and light up the world!",
  "story":{"title":"⚡ Build Your Own Circuit!",
   "text":"Thomas Edison tested over 6,000 materials to find the right filament for his light bulb. Every failure taught him something. Today, you can build a circuit with a click. Understanding electricity isn't just about light bulbs — it's about every electronic device you've ever used!"},
  "games":[
   {"type":"circuit","title":"🔌 Circuit Builder Lab",
    "desc":"Drag wires, batteries, bulbs, resistors — build real working circuits!"},
   {"type":"ohm_builder","title":"📊 Ohm's Law Explorer",
    "desc":"See V, I, R relationship live — the triangle that powers everything!"},
   {"type":"wave","title":"🔄 AC vs DC Visualiser",
    "desc":"See how alternating and direct current actually look as waves!"},
  ],
  "note":{
   "sections":[
    {"h":"⚡ Current, Voltage, Resistance","body":"CURRENT (I): rate of charge flow\nI = Q/t   Unit: Ampere (A)\nConventional: + to −   Electron flow: − to +\n\nVOLTAGE (V): electrical 'pressure', drives current\nV = W/Q   Unit: Volt (V)\n\nRESISTANCE (R): opposition to current\nR = V/I   Unit: Ohm (Ω)\n\nOHM'S LAW: V = IR\n(valid for ohmic conductors at constant temperature)","fact":"🌟 Your brain runs on electrical signals — neurons fire at ~100 m/s using ~20 W of power. Your brain is more efficient than any computer!"},
    {"h":"🔌 Circuits","body":"SERIES circuit:\n• Same current everywhere: I = I₁ = I₂\n• Voltages add: V = V₁ + V₂\n• Resistances add: R = R₁ + R₂\n• One bulb fails → all fail\n\nPARALLEL circuit:\n• Same voltage: V = V₁ = V₂\n• Currents add: I = I₁ + I₂\n• 1/R = 1/R₁ + 1/R₂\n• One bulb fails → others stay on\n(House wiring is always PARALLEL!)","fact":"🌟 Thomas Edison's Pearl Street Station (1882) powered 400 light bulbs in Lower Manhattan — the world's first commercial power station!"},
    {"h":"💡 Power & Energy","body":"Power: P = VI = I²R = V²/R   Unit: Watt (W)\nEnergy: E = Pt = VIt   Unit: Joule (J)\n\nCommercial unit: kWh (kilowatt-hour)\n1 kWh = 3.6×10⁶ J\n\nYour electricity bill = kWh used × price/kWh\n\nFuse: melts when current too high → safety\nCircuit breaker: trips and resets (modern fuse)\nEarth wire: prevents electric shock","fact":None},
   ],
   "memory":"🧠 VIR Triangle: cover what you want → V=IR, I=V/R, R=V/I. Same idea for P=VI!",
   "tips":["V=IR — Ohm's Law (most important)","Series: same current; Parallel: same voltage","P=VI=I²R=V²/R","Fuse always in SERIES","1 kWh=3.6×10⁶ J — your electricity bill unit"]
  },
  "quiz":[
   {"q":"V=12V, R=4Ω. Current I = ?","opts":["3 A","48 A","0.33 A","8 A"],"ans":0,"exp":"I=V/R=12/4=3 A (Ohm's Law)"},
   {"q":"Why is household wiring done in PARALLEL?","opts":["Cheaper","Each appliance gets full voltage and works independently","Series is dangerous always","Parallel uses less current"],"ans":1,"exp":"Parallel: each appliance gets full 240V and switching one off doesn't affect others. Series: all share voltage and one failure kills all!"},
   {"q":"60W bulb on for 10 hours uses how many kWh?","opts":["600 kWh","0.6 kWh","6 kWh","60 kWh"],"ans":1,"exp":"Energy=Pt=60W×10h=600Wh=0.6 kWh"},
   {"q":"Two 10Ω resistors in parallel. Total resistance = ?","opts":["20 Ω","10 Ω","5 Ω","0.2 Ω"],"ans":2,"exp":"1/R=1/10+1/10=2/10=1/5 → R=5 Ω. Parallel always gives LESS than smallest resistor!"},
   {"q":"P=I²R. I=2A, R=5Ω. Power = ?","opts":["10 W","40 W","20 W","2.5 W"],"ans":2,"exp":"P=I²R=2²×5=4×5=20 W"},
  ]
 },
 {
  "id":"g10_light","title":"Light: Optics & Colour","emoji":"🌈","color":"#ec4899",
  "grade":"Grade 10","chapter":"Chapter 2",
  "tagline":"Bend light, make rainbows, build a telescope!",
  "story":{"title":"🌈 The Glass That Bends Light!",
   "text":"Newton split sunlight into all the colours of the rainbow using just a glass prism in 1666. He discovered that white light is actually ALL colours mixed! Today, the same principle gives us rainbows, fibre optic internet, camera lenses, and even laser surgery. Light is the fastest, most mysterious thing in physics."},
  "games":[
   {"type":"optics","title":"🔍 Ray Tracer — Lens & Mirror Lab",
    "desc":"Shoot light rays through lenses and mirrors — watch them bend and focus!"},
   {"type":"refraction_game","title":"🌊 Snell's Law Refraction Game",
    "desc":"Guide light rays through different media — hit the target by predicting bending!"},
   {"type":"wave","title":"🌈 Colour Mixing Simulator",
    "desc":"Mix light (RGB) and pigments (CMY) — discover why they're different!"},
  ],
  "note":{
   "sections":[
    {"h":"🪞 Reflection","body":"Laws of Reflection:\n1. ∠incidence = ∠reflection (both from NORMAL)\n2. Incident ray, normal, reflected ray all in same plane\n\nPlane mirror: virtual, erect, same size, laterally inverted\nImage distance = object distance\n\nConcave mirror (converging):\nUsed in: torch, car headlights, satellite dishes\n\nConvex mirror (diverging):\nUsed in: rear-view mirrors (wider field of view)\n\nMirror formula: 1/v + 1/u = 1/f","fact":"🌟 The mirrors in Hubble Space Telescope are polished to accuracy of 10 nanometres — 1/10,000th the width of a human hair!"},
    {"h":"〰️ Refraction & Snell's Law","body":"Bending of light as it passes between media:\nn₁sin θ₁ = n₂sin θ₂  (Snell's Law)\n\nRefractive index n = c/v = sin(i)/sin(r)\n\nDenser medium: light slows down and bends TOWARD normal\nRarer medium: light speeds up and bends AWAY from normal\n\nTotal Internal Reflection (TIR):\n• Light goes denser→rarer at angle > critical angle\n• ALL light reflects back inside\n• sin(critical angle) = 1/n\n\nApplications of TIR:\n• Optical fibres (internet!)\n• Diamonds sparkle\n• Endoscopes (medical)","fact":"🌟 Optical fibres use TIR to carry data as light pulses — a single fibre thinner than hair can carry millions of phone calls simultaneously!"},
    {"h":"🔍 Lenses & Power","body":"Convex (converging): thicker middle\n• Corrects long-sight (hypermetropia)\n• Camera, projector, magnifying glass, eye\n\nConcave (diverging): thinner middle\n• Corrects short-sight (myopia)\n• Peepholes in doors\n\nLens formula: 1/v − 1/u = 1/f\nMagnification: m = v/u = h'/h\nPower: P = 1/f(m)   Unit: Dioptre (D)\n\nRainbow: refraction + TIR + dispersion in raindrops!","fact":None},
   ],
   "memory":"🧠 'VIBGYOR' in rainbow — Violet bends most, Red bends least. V for Very sharp bend!",
   "tips":["Both reflection angles from NORMAL (not surface)","n=c/v — higher n = slower light = more bending","TIR: denser to rarer + angle > critical angle","Convex lens: converges (corrects long-sight)","Concave lens: diverges (corrects short-sight)"]
  },
  "quiz":[
   {"q":"Critical angle for glass (n=1.5). sin(c)=1/n=1/1.5=0.667. Critical angle ≈ ?","opts":["42°","60°","30°","90°"],"ans":0,"exp":"sin(c)=1/1.5=0.667 → c=arcsin(0.667)≈42°. Above this angle, TIR occurs!"},
   {"q":"Convex lens f=25cm. Power = ?","opts":["25 D","4 D","0.25 D","2.5 D"],"ans":1,"exp":"P=1/f(m)=1/0.25=4 D. Always convert cm to m first!"},
   {"q":"A fish in water looks closer than it is. This is because of:","opts":["Reflection","Refraction (light bends at water surface)","Dispersion","Total internal reflection"],"ans":1,"exp":"Light from fish bends AWAY from normal at water-air boundary → fish appears closer (apparent depth < real depth)!"},
   {"q":"Optical fibres work using:","opts":["Reflection","Refraction","Total internal reflection","Dispersion"],"ans":2,"exp":"TIR keeps light inside the fibre — light bounces along the fibre without escaping. This carries internet data at light speed!"},
   {"q":"Short-sightedness (myopia) is corrected by:","opts":["Convex lens","Concave lens","Plane mirror","Concave mirror"],"ans":1,"exp":"Myopia: image forms in FRONT of retina. Concave (diverging) lens pushes image back onto retina. Hypermetropia: convex lens."},
  ]
 },
],
"Grade 11":[
 {
  "id":"g11_thermo","title":"Thermodynamics","emoji":"🌡️","color":"#f97316",
  "grade":"Grade 11","chapter":"Chapter 1",
  "tagline":"Heat engines, entropy, and the limits of energy!",
  "story":{"title":"🌡️ The Engine That Changed the World!",
   "text":"James Watt's steam engine powered the Industrial Revolution. But engineers kept trying to make it 100% efficient — convert ALL heat to work. Then a young French engineer named Sadi Carnot proved it's MATHEMATICALLY IMPOSSIBLE. The universe itself has limits. This is thermodynamics — the science of heat, work, and why disorder always wins."},
  "games":[
   {"type":"gas_law","title":"💨 Ideal Gas Law Simulator",
    "desc":"Change P, V, T of a gas container — watch the molecules move!"},
   {"type":"carnot_engine","title":"🔄 Carnot Engine Builder",
    "desc":"Set hot and cold temperatures — calculate maximum possible efficiency!"},
   {"type":"heat_transfer","title":"🌡️ Heat Transfer Race",
    "desc":"Cool or heat objects — identify conduction, convection, radiation!"},
  ],
  "note":{
   "sections":[
    {"h":"🌡️ Temperature & Zeroth Law","body":"Zeroth Law: If A in equilibrium with C, and B in equilibrium with C → A in equilibrium with B.\n(This defines TEMPERATURE as a real measurable quantity!)\n\nTemperature scales:\n• Celsius: °C (ice=0, steam=100)\n• Kelvin: K = °C + 273 (absolute zero = 0 K)\n• Fahrenheit: °F = 9/5 × °C + 32\n\nAbsolute zero (0 K = −273°C): all molecular motion stops","fact":"🌟 Absolute zero has never been achieved — scientists have reached within a billionth of a degree but never quite there!"},
    {"h":"📐 Gas Laws","body":"Boyle's Law (constant T): PV = constant → P₁V₁ = P₂V₂\nCharles's Law (constant P): V/T = constant → V₁/T₁ = V₂/T₂\nGay-Lussac's Law (constant V): P/T = constant\nAvogadro's Law: Equal volumes of gases (same T,P) contain equal molecules\n\nIdeal Gas Law: PV = nRT\n• n = moles, R = 8.314 J/(mol·K)\n• T MUST be in Kelvin!\n\nKinetic Theory: temperature = average KE of molecules","fact":"🌟 At 0°C, oxygen molecules move at ~461 m/s on average — faster than sound! At higher temperature, they move faster still."},
    {"h":"⚡ Laws of Thermodynamics","body":"0th: Thermal equilibrium (defines temperature)\n\n1st: ΔU = Q − W\n(Energy conserved: internal energy = heat added − work done by system)\n\n2nd: Entropy of isolated system always increases\n(Heat flows hot→cold spontaneously, not cold→hot)\n\nCarnot Efficiency: η = 1 − Tc/Th\n(Maximum possible efficiency — no engine beats Carnot!)\n\n3rd: Entropy→0 as T→0 K (absolute zero unachievable)","fact":"🌟 The best real engines (hydrogen fuel cells) reach ~60% efficiency. Car petrol engines: ~25-30%. Carnot sets the maximum ceiling!"},
   ],
   "memory":"🧠 'ΔU=Q-W' — change in internal energy = heat IN minus work done BY the system. Think: 'you earn Q, spend W'",
   "tips":["T MUST be in Kelvin for gas law calculations (T=°C+273)","PV=nRT — Ideal Gas Law","Carnot η=1-Tc/Th (temperatures in Kelvin)","1st Law: energy conserved. 2nd Law: entropy increases","Carnot efficiency is the MAXIMUM — real engines always less"]
  },
  "quiz":[
   {"q":"Gas at 27°C, V=2L, P=1 atm. T raised to 127°C at constant V. New pressure = ?","opts":["4/3 atm","2 atm","1 atm","0.75 atm"],"ans":0,"exp":"Gay-Lussac: P/T=constant. P₁/T₁=P₂/T₂. 1/300=P₂/400. P₂=4/3 atm. Always use KELVIN!"},
   {"q":"Carnot engine: Th=500K, Tc=300K. Maximum efficiency = ?","opts":["60%","40%","20%","80%"],"ans":1,"exp":"η=1-Tc/Th=1-300/500=1-0.6=0.4=40%"},
   {"q":"First Law ΔU=Q-W. System absorbs 800J heat, does 300J work. ΔU = ?","opts":["500 J","1100 J","-500 J","300 J"],"ans":0,"exp":"ΔU=Q-W=800-300=500 J. Internal energy increases by 500 J."},
   {"q":"Heat transfer in vacuum (like from Sun to Earth) occurs by:","opts":["Conduction","Convection","Radiation","All three"],"ans":2,"exp":"Radiation requires NO medium — travels as electromagnetic waves. Sun heats Earth across 150 million km of vacuum!"},
   {"q":"Second Law means:","opts":["Energy cannot be created","All heat converts to work","Entropy always increases, heat flows hot→cold","Temperature always rises"],"ans":2,"exp":"2nd Law: entropy always increases in isolated system. Heat ONLY flows spontaneously from HOT to COLD — never the reverse!"},
  ]
 },
],
"Grade 12":[
 {
  "id":"g12_quantum","title":"Quantum Physics","emoji":"⚛️","color":"#6366f1",
  "grade":"Grade 12","chapter":"Chapter 1",
  "tagline":"Enter the quantum world where reality is truly strange!",
  "story":{"title":"⚛️ The Experiment That Broke Physics!",
   "text":"Shoot electrons one at a time through two slits. Each electron should make ONE dot. But after millions of electrons... you get an INTERFERENCE PATTERN — as if each electron went through BOTH slits simultaneously and interfered with itself. This isn't broken equipment. This is quantum mechanics — where particles are waves, reality is probabilistic, and observation itself changes outcomes."},
  "games":[
   {"type":"wave","title":"〰️ Double Slit Interference",
    "desc":"Watch electrons build up an interference pattern one by one — truly mind-bending!"},
   {"type":"photoelectric","title":"⚡ Photoelectric Effect Lab",
    "desc":"Shine light on metals — discover that ONLY frequency (not brightness) ejects electrons!"},
   {"type":"atom_builder","title":"🔵 Bohr Atom Simulator",
    "desc":"Add energy to electrons — watch them jump shells and emit photons!"},
  ],
  "note":{
   "sections":[
    {"h":"💫 Photons & Wave-Particle Duality","body":"Light behaves as WAVE (interference, diffraction)\nLight behaves as PARTICLE (photoelectric effect, Compton scattering)\n\nPlanck (1900): Energy is quantised!\nE = hf  (h = 6.63×10⁻³⁴ J·s, Planck's constant)\n\nEinstein (1905): Light = photons (particles of energy hf)\nde Broglie (1924): ALL particles have wavelength!\nλ = h/p = h/mv\n\nWave-particle duality is UNIVERSAL — not just light!","fact":"🌟 Electrons show interference (double-slit), proving they're waves. But they also hit detectors as single particles. This paradox is unresolved!"},
    {"h":"⚡ Photoelectric Effect","body":"Light hits metal → electrons ejected IF f > f₀ (threshold freq)\n\nKE_max = hf − φ  (φ = work function of metal)\nf₀ = φ/h  (threshold frequency)\n\nCRITICAL observations:\n✅ Below f₀: NO electrons, even with bright light!\n✅ Above f₀: electrons instantly ejected\n✅ More intensity → more electrons (not faster)\n✅ More frequency → more energetic electrons\n\nThis DISPROVES wave theory of light!","fact":"🌟 Einstein won the 1921 Nobel Prize specifically for explaining the photoelectric effect — NOT for relativity!"},
    {"h":"🔵 Bohr's Atom & de Broglie","body":"Bohr's model (hydrogen):\nElectrons in fixed circular orbits with quantised energy:\nEₙ = −13.6/n² eV  (n = 1, 2, 3...)\n\nElectron absorbs photon → jumps to higher shell\nElectron emits photon → falls to lower shell\nhf = E_upper − E_lower\n\nHeisenberg Uncertainty Principle:\nΔx · Δp ≥ ℏ/2\n(Cannot know BOTH position AND momentum precisely — fundamental limit!)\n\nSchrödinger's equation → electron 'cloud' (probability density)","fact":"🌟 Quantum tunnelling allows electrons to 'teleport' through barriers — without this, nuclear fusion in the Sun would be impossible!"},
   ],
   "memory":"🧠 'E=hf for photons, λ=h/mv for particles' — Planck's h connects both worlds. h=6.63×10⁻³⁴ J·s",
   "tips":["E=hf — photon energy","Photoelectric: FREQUENCY determines emission, NOT intensity","KE_max=hf-φ","Bohr: En=-13.6/n² eV for hydrogen","ΔxΔp≥ℏ/2 — Heisenberg is FUNDAMENTAL, not measurement error"]
  },
  "quiz":[
   {"q":"Photoelectric effect: light below threshold frequency hits metal. Effect:","opts":["Electrons slowly emitted","Electrons emitted after delay","NO electrons emitted regardless of brightness","Metal heats and emits"],"ans":2,"exp":"Below threshold frequency f₀: ZERO electrons emitted, no matter how bright. Only frequency above f₀ can eject electrons!"},
   {"q":"E=hf. f=5×10¹⁴ Hz, h=6.63×10⁻³⁴. Photon energy = ?","opts":["3.3×10⁻¹⁹ J","3.3×10⁻²⁰ J","6.63×10⁻¹⁹ J","1×10⁻¹⁹ J"],"ans":0,"exp":"E=hf=6.63×10⁻³⁴×5×10¹⁴=33.15×10⁻²⁰=3.3×10⁻¹⁹ J"},
   {"q":"de Broglie wavelength of an electron (m=9.1×10⁻³¹kg) at v=10⁶m/s ≈ (h=6.63×10⁻³⁴)?","opts":["7.3×10⁻¹⁰ m","7.3×10⁻⁷ m","6.6×10⁻³⁴ m","9.1×10⁻³¹ m"],"ans":0,"exp":"λ=h/mv=6.63×10⁻³⁴/(9.1×10⁻³¹×10⁶)=6.63/9.1×10⁻⁹≈0.73×10⁻⁹=7.3×10⁻¹⁰ m"},
   {"q":"Bohr model: energy of electron in n=2 shell of hydrogen:","opts":["-13.6 eV","-3.4 eV","-1.51 eV","0 eV"],"ans":1,"exp":"En=-13.6/n²=-13.6/4=-3.4 eV. n=1: -13.6 eV (ground state). n=∞: 0 eV (free electron)"},
   {"q":"Heisenberg Uncertainty Principle implies:","opts":["Instruments are imperfect","We cannot FUNDAMENTALLY know both position and momentum precisely","Quantum particles don't exist","Only applies to large objects"],"ans":1,"exp":"The uncertainty is FUNDAMENTAL — not a measurement limitation. Nature itself forbids simultaneous precise knowledge of x and p!"},
  ]
 },
 {
  "id":"g12_nuclear","title":"Nuclear Physics","emoji":"☢️","color":"#84cc16",
  "grade":"Grade 12","chapter":"Chapter 2",
  "tagline":"Split atoms, fuse suns, unlock E=mc²!",
  "story":{"title":"☢️ The Energy Inside an Atom!",
   "text":"1 kg of uranium contains the same energy as 3,000 tonnes of coal. Einstein's E=mc² told us mass IS energy. In 1938, Hahn and Strassmann split uranium for the first time. The energy released was enormous. The same physics that powers nuclear reactors also powers the Sun — and every star in the universe has been running on nuclear fusion for billions of years."},
  "games":[
   {"type":"decay_chain","title":"☢️ Radioactive Decay Simulator",
    "desc":"Watch atoms decay in real time — plot the half-life curve!"},
   {"type":"fission_chain","title":"💥 Chain Reaction Controller",
    "desc":"Control a nuclear chain reaction — too slow=fizzle, too fast=meltdown!"},
   {"type":"wave","title":"☀️ Fusion Reactor Designer",
    "desc":"Set temperature and pressure to achieve fusion — power the grid!"},
  ],
  "note":{
   "sections":[
    {"h":"⚛️ Nuclear Structure","body":"Nucleus: protons (Z) + neutrons (N)\nMass number A = Z + N\nIsotopes: same Z, different N\n\nNuclear forces:\n• Strong nuclear force: holds nucleus together (strongest!)\n• Overcomes electrostatic repulsion between protons\n• Very short range (~10⁻¹⁵ m)\n\nBinding energy: energy needed to split nucleus\nMass defect: Δm = mass of parts − mass of nucleus\nE = Δmc²   (Einstein's equation!)","fact":"🌟 Nuclear density is ~10¹⁷ kg/m³. A teaspoon of nuclear matter would weigh 100 MILLION TONNES!"},
    {"h":"☢️ Radioactive Decay","body":"ALPHA (α): emits ²₄He nucleus\n• Charge: +2, Mass: 4 u\n• Least penetrating (stopped by paper)\n• Most ionising\n\nBETA (β⁻): emits electron + antineutrino\n• Stopped by thin aluminium\n\nGAMMA (γ): emits high-energy photon\n• Most penetrating (needs lead/concrete)\n• No change in Z or A\n\nDecay Law: N = N₀e^(−λt)\nHalf-life: T½ = 0.693/λ\n(After each T½, half the atoms have decayed)","fact":"🌟 Carbon-14 has T½=5,730 years — used to date ancient fossils, mummies, wooden artefacts up to ~50,000 years old!"},
    {"h":"💥 Fission & Fusion","body":"FISSION: heavy nucleus splits into lighter ones\n²³⁵₉₂U + n → Kr + Ba + 3n + energy (~200 MeV)\nChain reaction → nuclear reactor / bomb\nCritical mass: minimum for self-sustaining chain reaction\n\nFUSION: light nuclei join → heavier + energy\n²₁H + ³₁H → ⁴₂He + n + 17.6 MeV\nPowers the SUN and all stars!\nNeeds: T > 10⁷ K and huge pressure\n\nFusion releases MORE energy per unit mass than fission!\nE=mc²: tiny mass → enormous energy","fact":"🌟 The Sun converts 600 MILLION tonnes of hydrogen to helium every second by fusion, releasing 3.8×10²⁶ Watts. It's been doing this for 4.6 billion years!"},
   ],
   "memory":"🧠 'FuSion=Sun (joins light nuclei). FiSSion=Splits (heavy nuclei)'. F-U → fusion. F-I → fission!",
   "tips":["A=Z+N (mass number = protons + neutrons)","Half-life: N=N₀(1/2)^(t/T½)","α least penetrating; γ most penetrating","Fission for reactors (U-235); Fusion for stars","E=Δmc² — mass defect → energy released"]
  },
  "quiz":[
   {"q":"²³⁵₉₂U: number of neutrons = ?","opts":["92","235","143","327"],"ans":2,"exp":"N=A-Z=235-92=143 neutrons"},
   {"q":"T½=10 years. After 30 years, fraction remaining = ?","opts":["1/2","1/4","1/8","1/16"],"ans":2,"exp":"30 years = 3 half-lives. After each: 1→½→¼→⅛. So 1/8 remains!"},
   {"q":"Which radiation is most penetrating?","opts":["Alpha (α)","Beta (β)","Gamma (γ)","All equal"],"ans":2,"exp":"Gamma rays are EM radiation — need thick lead or concrete to stop. Alpha stopped by paper. Beta by thin aluminium!"},
   {"q":"Fusion releases more energy than fission per unit mass. Fusion powers:","opts":["Nuclear reactors on Earth","The Sun and stars","Both equally","Car engines"],"ans":1,"exp":"Fusion powers ALL stars including the Sun! On Earth, controlled fusion is still being developed (ITER project). Reactors currently use fission."},
   {"q":"E=mc². Mass defect=0.001 kg. Energy = ? (c=3×10⁸ m/s)","opts":["3×10⁵ J","9×10¹³ J","3×10¹¹ J","0.001 J"],"ans":1,"exp":"E=mc²=0.001×(3×10⁸)²=0.001×9×10¹⁶=9×10¹³ J — enormous energy from tiny mass!"},
  ]
 },
],
}

# flatten
ALL_TOPICS = [t for gl in TOPICS.values() for t in gl]
GRADES = list(TOPICS.keys())
def get_topics(grade): return TOPICS.get(grade,[])
def get_topic(tid): return next((t for t in ALL_TOPICS if t["id"]==tid),None)

# ─── Dynamic Game HTML (real physics simulations) ─────────────────────────────

def projectile_game(cfg):
    return """
<style>
*{box-sizing:border-box;font-family:'Nunito',system-ui,sans-serif}
body{margin:0;background:#0a0a1a;color:white}
#wrap{max-width:520px;margin:auto;padding:10px}
.title-bar{background:linear-gradient(135deg,#7c3aed,#2563eb);border-radius:14px;
  padding:.7rem 1rem;text-align:center;margin-bottom:10px}
.title-bar h2{margin:0;font-size:1rem;font-weight:800}
canvas{border-radius:14px;border:1px solid rgba(255,255,255,.1);display:block;margin:auto;width:100%;max-width:500px}
.controls{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:10px}
.ctrl{background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1);
  border-radius:12px;padding:.7rem}
.ctrl label{font-size:.7rem;color:#a78bfa;font-weight:700;display:block;margin-bottom:4px;text-transform:uppercase}
input[type=range]{width:100%;accent-color:#7c3aed;cursor:pointer}
.val{font-size:1.1rem;font-weight:900;color:#60a5fa;float:right}
.btn-row{display:flex;gap:8px;margin-top:10px}
button{flex:1;padding:10px;border-radius:12px;border:none;font-size:.88rem;
  font-weight:800;cursor:pointer;font-family:inherit;transition:all .15s}
.btn-fire{background:linear-gradient(135deg,#ef4444,#f97316);color:white}
.btn-reset{background:rgba(255,255,255,.1);color:white}
button:active{transform:scale(.97)}
.stats{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);
  border-radius:12px;padding:.7rem;margin-top:8px;font-size:.78rem;
  display:grid;grid-template-columns:repeat(3,1fr);gap:6px;text-align:center}
.stat-item{} .stat-val{color:#34d399;font-weight:800;font-size:.95rem}
.stat-lbl{color:#888;font-size:.68rem;margin-top:1px}
#msg{background:rgba(99,102,241,.2);border:1px solid #6366f1;border-radius:10px;
  padding:.5rem 1rem;text-align:center;font-size:.82rem;font-weight:700;
  margin-top:8px;display:none}
</style>
<div id="wrap">
<div class="title-bar"><h2>🚀 Projectile Launcher — Hit the Target!</h2></div>
<canvas id="c" width="500" height="280"></canvas>
<div class="controls">
  <div class="ctrl">
    <label>Launch Angle <span class="val" id="ang-v">45°</span></label>
    <input type="range" id="ang" min="10" max="80" value="45"
      oninput="document.getElementById('ang-v').textContent=this.value+'°'">
  </div>
  <div class="ctrl">
    <label>Speed (m/s) <span class="val" id="spd-v">30</span></label>
    <input type="range" id="spd" min="10" max="60" value="30"
      oninput="document.getElementById('spd-v').textContent=this.value">
  </div>
</div>
<div class="btn-row">
  <button class="btn-fire" onclick="fire()">🚀 FIRE!</button>
  <button class="btn-reset" onclick="reset()">🎯 New Target</button>
</div>
<div class="stats">
  <div class="stat-item"><div class="stat-val" id="s-range">—</div><div class="stat-lbl">Range (m)</div></div>
  <div class="stat-item"><div class="stat-val" id="s-height">—</div><div class="stat-lbl">Max Height (m)</div></div>
  <div class="stat-item"><div class="stat-val" id="s-time">—</div><div class="stat-lbl">Flight Time (s)</div></div>
</div>
<div id="msg"></div>
</div>
<script>
const cvs=document.getElementById('c'),ctx=cvs.getContext('2d');
const W=500,H=280,g=9.8,scale=4;
let anim=null,px,py,vx,vy,trail=[],targetX,scored=0,attempts=0;

function randTarget(){targetX=180+Math.random()*240;}
randTarget();

function drawScene(bx,by){
  ctx.clearRect(0,0,W,H);
  // Sky gradient
  const sky=ctx.createLinearGradient(0,0,0,H);
  sky.addColorStop(0,'#0a0a2e');sky.addColorStop(1,'#1a1040');
  ctx.fillStyle=sky;ctx.fillRect(0,0,W,H);
  // Stars
  ctx.fillStyle='rgba(255,255,255,.5)';
  for(let i=0;i<40;i++){const sx=(i*73)%W,sy=(i*47)%H*0.6;ctx.fillRect(sx,sy,1,1);}
  // Ground
  const grd=ctx.createLinearGradient(0,H-30,0,H);
  grd.addColorStop(0,'#2d5a27');grd.addColorStop(1,'#1a3a15');
  ctx.fillStyle=grd;ctx.fillRect(0,H-30,W,30);
  // Grid lines
  ctx.strokeStyle='rgba(255,255,255,.04)';ctx.lineWidth=1;
  for(let x=0;x<W;x+=50){ctx.beginPath();ctx.moveTo(x,0);ctx.lineTo(x,H-30);ctx.stroke();}
  for(let y=0;y<H-30;y+=40){ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(W,y);ctx.stroke();}
  // Trail
  if(trail.length>1){
    ctx.beginPath();ctx.moveTo(trail[0][0],trail[0][1]);
    for(let i=1;i<trail.length;i++){
      const a=i/trail.length;
      ctx.strokeStyle=`rgba(167,139,250,${a*0.7})`;
      ctx.lineWidth=2;
      ctx.lineTo(trail[i][0],trail[i][1]);ctx.stroke();
      ctx.beginPath();ctx.moveTo(trail[i][0],trail[i][1]);
    }
  }
  // Target (flag)
  const tx=targetX,ty=H-30;
  ctx.fillStyle='#ef4444';
  ctx.beginPath();ctx.arc(tx,ty,10,0,Math.PI*2);ctx.fill();
  ctx.strokeStyle='#fbbf24';ctx.lineWidth=2;
  ctx.beginPath();ctx.moveTo(tx,ty-10);ctx.lineTo(tx,ty-40);ctx.stroke();
  ctx.fillStyle='#fbbf24';
  ctx.beginPath();ctx.moveTo(tx,ty-40);ctx.lineTo(tx+20,ty-32);ctx.lineTo(tx,ty-24);ctx.fill();
  ctx.fillStyle='white';ctx.font='bold 9px Nunito,system-ui';ctx.textAlign='center';
  ctx.fillText('TARGET',tx,ty+5);
  // Launcher
  ctx.fillStyle='#4b5563';ctx.fillRect(8,H-50,24,22);
  ctx.fillStyle='#6b7280';ctx.fillRect(6,H-28,30,8);
  // Angle indicator
  const ang=parseFloat(document.getElementById('ang').value);
  ctx.strokeStyle='rgba(167,139,250,.5)';ctx.lineWidth=1.5;
  ctx.setLineDash([3,3]);
  ctx.beginPath();ctx.moveTo(20,H-40);
  ctx.lineTo(20+Math.cos(ang*Math.PI/180)*40,H-40-Math.sin(ang*Math.PI/180)*40);
  ctx.stroke();ctx.setLineDash([]);
  // Projectile
  if(bx!==undefined){
    const grad=ctx.createRadialGradient(bx,by,0,bx,by,8);
    grad.addColorStop(0,'#fbbf24');grad.addColorStop(1,'#f97316');
    ctx.fillStyle=grad;
    ctx.beginPath();ctx.arc(bx,by,7,0,Math.PI*2);ctx.fill();
    ctx.strokeStyle='rgba(255,255,255,.4)';ctx.lineWidth=1.5;
    ctx.stroke();
  }
  // Score
  ctx.fillStyle='rgba(255,255,255,.7)';ctx.font='bold 11px Nunito,system-ui';
  ctx.textAlign='left';
  ctx.fillText(`Hits: ${scored}/${attempts}`,8,16);
}

function worldToCanvas(wx,wy){return[20+wx*scale, H-30-wy*scale];}

function fire(){
  if(anim)cancelAnimationFrame(anim);
  const ang=parseFloat(document.getElementById('ang').value)*Math.PI/180;
  const spd=parseFloat(document.getElementById('spd').value);
  px=0;py=0;vx=spd*Math.cos(ang);vy=spd*Math.sin(ang);
  trail=[];attempts++;
  const range=spd*spd*Math.sin(2*ang)/g;
  const maxH=spd*spd*Math.sin(ang)*Math.sin(ang)/(2*g);
  const tFlight=2*spd*Math.sin(ang)/g;
  document.getElementById('s-range').textContent=range.toFixed(1);
  document.getElementById('s-height').textContent=maxH.toFixed(1);
  document.getElementById('s-time').textContent=tFlight.toFixed(2);
  const msg=document.getElementById('msg');msg.style.display='none';

  let dt=0.05;
  function step(){
    px+=vx*dt;py+=vy*dt;vy-=g*dt;
    const[cx,cy]=worldToCanvas(px,py);
    trail.push([cx,cy]);if(trail.length>80)trail.shift();
    drawScene(cx,cy);
    const tCanvasX=targetX;
    const inAir=py>=0&&px*scale+20<W;
    if(!inAir){
      const finalCanvasX=20+px*scale;
      const dist=Math.abs(finalCanvasX-tCanvasX);
      if(dist<20){
        scored++;
        msg.textContent='🎉 HIT! Amazing shot! Score: '+scored+'/'+attempts;
        msg.style.background='rgba(16,185,129,.3)';msg.style.borderColor='#10b981';
      }else{
        const err=(dist/scale).toFixed(1);
        msg.textContent=`❌ Missed by ${err} m! Try adjusting angle/speed.`;
        msg.style.background='rgba(239,68,68,.2)';msg.style.borderColor='#ef4444';
      }
      msg.style.display='block';
      drawScene();return;
    }
    anim=requestAnimationFrame(step);
  }
  step();
}

function reset(){
  if(anim)cancelAnimationFrame(anim);
  trail=[];randTarget();
  document.getElementById('msg').style.display='none';
  document.getElementById('s-range').textContent='—';
  document.getElementById('s-height').textContent='—';
  document.getElementById('s-time').textContent='—';
  drawScene();
}
drawScene();
</script>
""", 620


def collision_game(cfg):
    return """
<style>
*{box-sizing:border-box;font-family:'Nunito',system-ui,sans-serif}
body{margin:0;background:#0a0a1a;color:white}
#wrap{max-width:520px;margin:auto;padding:10px}
.title-bar{background:linear-gradient(135deg,#059669,#0284c7);border-radius:14px;
  padding:.7rem 1rem;text-align:center;margin-bottom:10px}
.title-bar h2{margin:0;font-size:.98rem;font-weight:800}
canvas{border-radius:14px;border:1px solid rgba(255,255,255,.1);display:block;
  margin:auto;width:100%;max-width:500px}
.ctrl-row{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:10px}
.ctrl{background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1);
  border-radius:12px;padding:.65rem}
.ctrl label{font-size:.68rem;color:#34d399;font-weight:700;display:block;margin-bottom:3px;text-transform:uppercase}
input[type=range]{width:100%;accent-color:#059669}
.val{color:#60a5fa;font-weight:800;float:right}
.btn-row{display:flex;gap:8px;margin-top:8px}
button{flex:1;padding:10px;border-radius:12px;border:none;font-size:.86rem;
  font-weight:800;cursor:pointer;font-family:inherit;transition:transform .1s}
.btn-launch{background:linear-gradient(135deg,#059669,#0284c7);color:white}
.btn-r{background:rgba(255,255,255,.08);color:white}
button:active{transform:scale(.97)}
.stats-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:8px}
.stat-box{background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.08);
  border-radius:12px;padding:.65rem;text-align:center}
.stat-title{font-size:.65rem;color:#888;text-transform:uppercase;font-weight:700}
.stat-vals{display:flex;justify-content:space-around;margin-top:4px}
.sv{text-align:center}
.sv-n{font-size:.9rem;font-weight:900}
.sv-l{font-size:.6rem;color:#888}
#law-box{background:rgba(99,102,241,.15);border:1px solid rgba(99,102,241,.4);
  border-radius:12px;padding:.6rem;text-align:center;font-size:.78rem;
  margin-top:8px;font-weight:700}
</style>
<div id="wrap">
<div class="title-bar"><h2>💥 Elastic Collision Lab — Conservation of Momentum!</h2></div>
<canvas id="c" width="500" height="220"></canvas>
<div class="ctrl-row">
  <div class="ctrl">
    <label>Ball 1 Mass (kg) <span class="val" id="m1v">3</span></label>
    <input type="range" id="m1" min="1" max="10" value="3"
      oninput="document.getElementById('m1v').textContent=this.value;reset()">
    <label style="margin-top:6px">Ball 1 Speed (m/s) <span class="val" id="v1v">8</span></label>
    <input type="range" id="v1" min="1" max="15" value="8"
      oninput="document.getElementById('v1v').textContent=this.value;reset()">
  </div>
  <div class="ctrl">
    <label>Ball 2 Mass (kg) <span class="val" id="m2v">3</span></label>
    <input type="range" id="m2" min="1" max="10" value="3"
      oninput="document.getElementById('m2v').textContent=this.value;reset()">
    <label style="margin-top:6px">Collision Type</label>
    <select id="ctype" style="width:100%;background:#1e1b4b;color:white;
        border:1px solid rgba(255,255,255,.2);border-radius:8px;padding:5px;font-family:inherit">
      <option value="elastic">Elastic (KE conserved)</option>
      <option value="inelastic">Inelastic (KE lost)</option>
      <option value="perfect">Perfectly Inelastic (stick)</option>
    </select>
  </div>
</div>
<div class="btn-row">
  <button class="btn-launch" onclick="launch()">▶ LAUNCH COLLISION</button>
  <button class="btn-r" onclick="reset()">↺ Reset</button>
</div>
<div class="stats-grid">
  <div class="stat-box">
    <div class="stat-title">Momentum (kg·m/s)</div>
    <div class="stat-vals">
      <div class="sv"><div class="sv-n" id="pb" style="color:#f97316">—</div><div class="sv-l">Before</div></div>
      <div class="sv"><div class="sv-n" id="pa" style="color:#10b981">—</div><div class="sv-l">After</div></div>
    </div>
  </div>
  <div class="stat-box">
    <div class="stat-title">Kinetic Energy (J)</div>
    <div class="stat-vals">
      <div class="sv"><div class="sv-n" id="kb" style="color:#f97316">—</div><div class="sv-l">Before</div></div>
      <div class="sv"><div class="sv-n" id="ka" style="color:#10b981">—</div><div class="sv-l">After</div></div>
    </div>
  </div>
</div>
<div id="law-box">📐 Law of Conservation of Momentum: p_before = p_after</div>
</div>
<script>
const c=document.getElementById('c'),ctx=c.getContext('2d');
const W=500,H=220;
let b1,b2,animId=null,done=false;

function getVals(){
  return{
    m1:parseFloat(document.getElementById('m1').value),
    m2:parseFloat(document.getElementById('m2').value),
    v1:parseFloat(document.getElementById('v1').value),
    ctype:document.getElementById('ctype').value
  };
}

function reset(){
  if(animId)cancelAnimationFrame(animId);
  const v=getVals();
  const r1=12+v.m1*3, r2=12+v.m2*3;
  b1={x:60,y:H/2,vx:v.v1*20,vy:0,m:v.m1,r:r1,col:'#f97316'};
  b2={x:W-60,y:H/2,vx:0,vy:0,m:v.m2,r:r2,col:'#60a5fa'};
  done=false;
  document.getElementById('pb').textContent='—';
  document.getElementById('pa').textContent='—';
  document.getElementById('kb').textContent='—';
  document.getElementById('ka').textContent='—';
  document.getElementById('law-box').style.borderColor='rgba(99,102,241,.4)';
  document.getElementById('law-box').style.background='rgba(99,102,241,.15)';
  document.getElementById('law-box').textContent='📐 Law of Conservation of Momentum: p_before = p_after';
  draw();
}

function draw(){
  ctx.clearRect(0,0,W,H);
  // BG
  ctx.fillStyle='#0d0d1f';ctx.fillRect(0,0,W,H);
  // Floor
  ctx.fillStyle='rgba(255,255,255,.04)';ctx.fillRect(0,H-20,W,20);
  // Grid
  ctx.strokeStyle='rgba(255,255,255,.03)';ctx.lineWidth=1;
  for(let x=0;x<W;x+=50){ctx.beginPath();ctx.moveTo(x,0);ctx.lineTo(x,H-20);ctx.stroke();}
  // Balls
  [b1,b2].forEach(b=>{
    const grd=ctx.createRadialGradient(b.x-b.r*.3,b.y-b.r*.3,b.r*.1,b.x,b.y,b.r);
    grd.addColorStop(0,'white');grd.addColorStop(.3,b.col);grd.addColorStop(1,'rgba(0,0,0,.5)');
    ctx.fillStyle=grd;
    ctx.beginPath();ctx.arc(b.x,b.y,b.r,0,Math.PI*2);ctx.fill();
    // Velocity arrow
    if(Math.abs(b.vx)>2){
      const dir=b.vx>0?1:-1,len=Math.min(Math.abs(b.vx)*1.5,60);
      ctx.strokeStyle=b.col;ctx.lineWidth=3;
      ctx.beginPath();ctx.moveTo(b.x,b.y);ctx.lineTo(b.x+dir*len,b.y);ctx.stroke();
      ctx.fillStyle=b.col;ctx.beginPath();
      ctx.moveTo(b.x+dir*len,b.y-6);ctx.lineTo(b.x+dir*len+dir*10,b.y);ctx.lineTo(b.x+dir*len,b.y+6);
      ctx.fill();
    }
    // Mass label
    ctx.fillStyle='white';ctx.font='bold 11px Nunito,system-ui';ctx.textAlign='center';
    ctx.fillText(b.m+'kg',b.x,b.y+4);
  });
}

function calcAfterVelocities(m1,m2,u1,u2,ctype){
  if(ctype==='elastic'){
    const v1=((m1-m2)*u1+2*m2*u2)/(m1+m2);
    const v2=((m2-m1)*u2+2*m1*u1)/(m1+m2);
    return[v1,v2];
  }else if(ctype==='inelastic'){
    const v1=((m1-m2*.5)*u1+1.5*m2*u2)/(m1+m2);
    const v2=((m2-m1*.5)*u2+1.5*m1*u1)/(m1+m2);
    return[v1,v2];
  }else{
    const vf=(m1*u1+m2*u2)/(m1+m2);
    return[vf,vf];
  }
}

function launch(){
  if(animId)cancelAnimationFrame(animId);
  reset();
  const v=getVals();
  const pBefore=b1.m*b1.vx/20+b2.m*b2.vx/20;
  const kBefore=0.5*b1.m*(b1.vx/20)**2+0.5*b2.m*(b2.vx/20)**2;
  document.getElementById('pb').textContent=pBefore.toFixed(1);
  document.getElementById('kb').textContent=kBefore.toFixed(1);
  let collided=false;

  function step(){
    b1.x+=b1.vx*.016; b2.x+=b2.vx*.016;
    // Bounce off walls
    if(b1.x-b1.r<0){b1.x=b1.r;b1.vx*=-1;}
    if(b2.x+b2.r>W){b2.x=W-b2.r;b2.vx*=-1;}
    // Collision
    if(!collided&&Math.abs(b1.x-b2.x)<b1.r+b2.r){
      collided=true;
      const [nv1,nv2]=calcAfterVelocities(b1.m,b2.m,b1.vx/20,b2.vx/20,v.ctype);
      b1.vx=nv1*20; b2.vx=nv2*20;
      if(v.ctype==='perfect'){b2.vx=b1.vx;}
      const pAfter=b1.m*b1.vx/20+b2.m*b2.vx/20;
      const kAfter=0.5*b1.m*(b1.vx/20)**2+0.5*b2.m*(b2.vx/20)**2;
      document.getElementById('pa').textContent=pAfter.toFixed(1);
      document.getElementById('ka').textContent=kAfter.toFixed(1);
      const pOk=Math.abs(pAfter-pBefore)<0.5;
      document.getElementById('law-box').textContent=
        pOk?'✅ Momentum conserved! p_before≈p_after ('+pBefore.toFixed(1)+'≈'+pAfter.toFixed(1)+')':
            '⚠️ External forces affected momentum';
      document.getElementById('law-box').style.borderColor=pOk?'#10b981':'#f97316';
      document.getElementById('law-box').style.background=pOk?'rgba(16,185,129,.15)':'rgba(249,115,22,.15)';
    }
    draw();
    animId=requestAnimationFrame(step);
  }
  step();
}
reset();
</script>
""", 680


def wave_lab(cfg):
    return """
<style>
*{box-sizing:border-box;font-family:'Nunito',system-ui,sans-serif}
body{margin:0;background:#0a0a1a;color:white}
#wrap{max-width:520px;margin:auto;padding:10px}
.title-bar{background:linear-gradient(135deg,#7c3aed,#db2777);border-radius:14px;
  padding:.7rem 1rem;text-align:center;margin-bottom:10px}
.title-bar h2{margin:0;font-size:.98rem;font-weight:800}
canvas{border-radius:14px;border:1px solid rgba(255,255,255,.1);display:block;
  margin:auto;width:100%;max-width:500px;cursor:crosshair}
.ctrl-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:10px}
.ctrl{background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1);
  border-radius:12px;padding:.65rem}
.ctrl label{font-size:.68rem;font-weight:700;display:block;margin-bottom:3px;text-transform:uppercase}
input[type=range]{width:100%;cursor:pointer}
.val{font-weight:800;float:right}
.wave-tabs{display:flex;gap:6px;margin-top:8px}
.wtab{flex:1;padding:8px;border-radius:10px;border:none;font-size:.78rem;
  font-weight:700;cursor:pointer;font-family:inherit;transition:all .15s}
.wtab.active{background:linear-gradient(135deg,#7c3aed,#db2777);color:white}
.wtab:not(.active){background:rgba(255,255,255,.06);color:#aaa}
.formula-bar{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);
  border-radius:12px;padding:.65rem;text-align:center;margin-top:8px;font-size:.82rem}
.fval{color:#a78bfa;font-weight:800}
</style>
<div id="wrap">
<div class="title-bar"><h2>〰️ Sound Wave Lab — Visualise Frequency & Amplitude!</h2></div>
<canvas id="c" width="500" height="200"></canvas>
<div class="wave-tabs">
  <button class="wtab active" onclick="setMode('single')" id="tab-single">Single Wave</button>
  <button class="wtab" onclick="setMode('interference')" id="tab-int">Interference</button>
  <button class="wtab" onclick="setMode('standing')" id="tab-stand">Standing Wave</button>
</div>
<div class="ctrl-grid">
  <div class="ctrl">
    <label style="color:#a78bfa">Frequency <span class="val" id="f1v" style="color:#a78bfa">3</span> Hz</label>
    <input type="range" id="f1" min="1" max="10" value="3" step=".5" style="accent-color:#7c3aed"
      oninput="document.getElementById('f1v').textContent=this.value">
    <label style="color:#f472b6;margin-top:6px">Amplitude <span class="val" id="a1v" style="color:#f472b6">5</span></label>
    <input type="range" id="a1" min="1" max="10" value="5" style="accent-color:#db2777"
      oninput="document.getElementById('a1v').textContent=this.value">
  </div>
  <div class="ctrl" id="wave2ctrl">
    <label style="color:#34d399">Wave 2 Freq <span class="val" id="f2v" style="color:#34d399">3</span> Hz</label>
    <input type="range" id="f2" min="1" max="10" value="3" step=".5" style="accent-color:#059669"
      oninput="document.getElementById('f2v').textContent=this.value">
    <label style="color:#60a5fa;margin-top:6px">Phase Shift <span class="val" id="phv" style="color:#60a5fa">0</span>°</label>
    <input type="range" id="ph" min="0" max="360" value="0" style="accent-color:#2563eb"
      oninput="document.getElementById('phv').textContent=this.value">
  </div>
</div>
<div class="formula-bar">
  v = f × λ &nbsp;|&nbsp; f = <span id="fdisp" class="fval">—</span> Hz &nbsp;|&nbsp;
  λ = <span id="ldisp" class="fval">—</span> m &nbsp;|&nbsp;
  Type: <span id="tdisp" class="fval">Audible</span>
</div>
</div>
<script>
const c=document.getElementById('c'),ctx=c.getContext('2d');
const W=500,H=200;let t=0,mode='single';

function setMode(m){
  mode=m;
  ['single','int','stand'].forEach(id=>{
    const el=document.getElementById('tab-'+id);
    if(el)el.className='wtab'+(id===m.split('er')[0].split('ing')[0]?'':id===m?'':'')+
    (id==='single'&&m==='single'?' active':'')+(id==='int'&&m==='interference'?' active':'')+(id==='stand'&&m==='standing'?' active':'');
  });
  document.getElementById('tab-single').className='wtab'+(mode==='single'?' active':'');
  document.getElementById('tab-int').className='wtab'+(mode==='interference'?' active':'');
  document.getElementById('tab-stand').className='wtab'+(mode==='standing'?' active':'');
}

function draw(){
  ctx.clearRect(0,0,W,H);
  ctx.fillStyle='#0d0d1f';ctx.fillRect(0,0,W,H);
  // Grid
  ctx.strokeStyle='rgba(255,255,255,.04)';ctx.lineWidth=1;
  for(let x=0;x<W;x+=50){ctx.beginPath();ctx.moveTo(x,0);ctx.lineTo(x,H);ctx.stroke();}
  ctx.strokeStyle='rgba(255,255,255,.08)';
  ctx.beginPath();ctx.moveTo(0,H/2);ctx.lineTo(W,H/2);ctx.stroke();

  const f1=parseFloat(document.getElementById('f1').value);
  const a1=parseFloat(document.getElementById('a1').value);
  const f2=parseFloat(document.getElementById('f2').value);
  const ph=parseFloat(document.getElementById('ph').value)*Math.PI/180;
  const A=a1*12;

  // Update formula
  const v=343;
  document.getElementById('fdisp').textContent=(f1*50).toFixed(0);
  document.getElementById('ldisp').textContent=(v/(f1*50)).toFixed(2);
  const freq=f1*50;
  document.getElementById('tdisp').textContent=freq<20?'Infrasound':freq>20000?'Ultrasound':'Audible';

  function y1(x){return A*Math.sin(2*Math.PI*f1*x/W+t*2);}
  function y2(x){return A*Math.sin(2*Math.PI*f2*x/W+t*2+ph);}

  if(mode==='single'){
    // Wave 1
    ctx.beginPath();ctx.strokeStyle='#a78bfa';ctx.lineWidth=2.5;
    for(let x=0;x<W;x++){
      const y=H/2-y1(x);
      x===0?ctx.moveTo(x,y):ctx.lineTo(x,y);
    }
    ctx.stroke();
    // Shade
    ctx.beginPath();
    for(let x=0;x<W;x++){const y=H/2-y1(x);x===0?ctx.moveTo(x,y):ctx.lineTo(x,y);}
    ctx.lineTo(W,H/2);ctx.lineTo(0,H/2);ctx.closePath();
    ctx.fillStyle='rgba(167,139,250,.08)';ctx.fill();
  }else if(mode==='interference'){
    // Wave 1
    ctx.beginPath();ctx.strokeStyle='#a78bfa';ctx.lineWidth=2;
    for(let x=0;x<W;x++){const y=H/2-y1(x);x===0?ctx.moveTo(x,y):ctx.lineTo(x,y);}
    ctx.stroke();
    // Wave 2
    ctx.beginPath();ctx.strokeStyle='#34d399';ctx.lineWidth=2;
    for(let x=0;x<W;x++){const y=H/2-y2(x);x===0?ctx.moveTo(x,y):ctx.lineTo(x,y);}
    ctx.stroke();
    // Resultant
    ctx.beginPath();ctx.strokeStyle='#fbbf24';ctx.lineWidth=3;
    for(let x=0;x<W;x++){const y=H/2-(y1(x)+y2(x));x===0?ctx.moveTo(x,y):ctx.lineTo(x,y);}
    ctx.stroke();
    ctx.fillStyle='rgba(255,255,255,.6)';ctx.font='bold 9px Nunito,system-ui';ctx.textAlign='left';
    ctx.fillText('Wave 1',5,15);
    ctx.fillStyle='#a78bfa';ctx.fillRect(50,8,20,3);
    ctx.fillStyle='rgba(255,255,255,.6)';ctx.fillText('Wave 2',75,15);
    ctx.fillStyle='#34d399';ctx.fillRect(120,8,20,3);
    ctx.fillStyle='rgba(255,255,255,.6)';ctx.fillText('Resultant',145,15);
    ctx.fillStyle='#fbbf24';ctx.fillRect(205,8,20,3);
  }else{
    // Standing wave — nodes and antinodes
    const nodes=Math.round(f1);
    ctx.beginPath();ctx.strokeStyle='#60a5fa';ctx.lineWidth=2.5;
    for(let x=0;x<W;x++){
      const standing=A*Math.sin(nodes*Math.PI*x/W)*Math.cos(t*3);
      const y=H/2-standing;
      x===0?ctx.moveTo(x,y):ctx.lineTo(x,y);
    }
    ctx.stroke();
    // Envelope
    ctx.beginPath();ctx.strokeStyle='rgba(96,165,250,.3)';ctx.lineWidth=1;ctx.setLineDash([3,3]);
    for(let x=0;x<W;x++){const y=H/2-A*Math.sin(nodes*Math.PI*x/W);x===0?ctx.moveTo(x,y):ctx.lineTo(x,y);}
    ctx.stroke();
    ctx.beginPath();
    for(let x=0;x<W;x++){const y=H/2+A*Math.sin(nodes*Math.PI*x/W);x===0?ctx.moveTo(x,y):ctx.lineTo(x,y);}
    ctx.stroke();ctx.setLineDash([]);
    // Mark nodes
    for(let i=0;i<=nodes;i++){
      const nx=i*W/nodes;
      ctx.fillStyle='#ef4444';ctx.beginPath();ctx.arc(nx,H/2,5,0,Math.PI*2);ctx.fill();
    }
    ctx.fillStyle='rgba(255,255,255,.6)';ctx.font='bold 9px Nunito,system-ui';ctx.textAlign='center';
    ctx.fillText('N=node (zero amplitude)',W/2,H-8);
  }
  t+=0.04;
  requestAnimationFrame(draw);
}
draw();
</script>
""", 620


def gravity_well(cfg):
    return """
<style>
*{box-sizing:border-box;font-family:'Nunito',system-ui,sans-serif}
body{margin:0;background:#0a0a1a;color:white}
#wrap{max-width:520px;margin:auto;padding:10px}
.title-bar{background:linear-gradient(135deg,#0ea5e9,#6366f1);border-radius:14px;
  padding:.7rem 1rem;text-align:center;margin-bottom:10px}
.title-bar h2{margin:0;font-size:.98rem;font-weight:800}
canvas{border-radius:14px;border:1px solid rgba(255,255,255,.15);display:block;
  margin:auto;width:100%;max-width:500px;cursor:crosshair}
.info{font-size:.72rem;color:#94a3b8;text-align:center;margin:4px 0 8px}
.ctrl-row{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:8px}
.ctrl{background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1);
  border-radius:12px;padding:.65rem}
.ctrl label{font-size:.68rem;color:#60a5fa;font-weight:700;display:block;margin-bottom:3px;text-transform:uppercase}
input[type=range]{width:100%;accent-color:#0ea5e9}
.vl{color:#a78bfa;font-weight:800;float:right}
.btn-row{display:flex;gap:8px;margin-top:8px}
button{flex:1;padding:9px;border-radius:11px;border:none;font-size:.84rem;
  font-weight:800;cursor:pointer;font-family:inherit;transition:transform .1s}
.btn-l{background:linear-gradient(135deg,#0ea5e9,#6366f1);color:white}
.btn-c{background:rgba(239,68,68,.2);color:#fca5a5;border:1px solid rgba(239,68,68,.3)}
button:active{transform:scale(.97)}
.orbit-info{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);
  border-radius:12px;padding:.65rem;display:grid;grid-template-columns:repeat(3,1fr);
  gap:6px;text-align:center;margin-top:8px;font-size:.72rem}
.oi-val{color:#34d399;font-weight:900;font-size:.9rem}
</style>
<div id="wrap">
<div class="title-bar"><h2>🌌 Gravity Well — Orbital Mechanics Simulator!</h2></div>
<canvas id="c" width="500" height="300"></canvas>
<div class="info">Click on canvas to launch a satellite from that position!</div>
<div class="ctrl-row">
  <div class="ctrl">
    <label>Planet Mass <span class="vl" id="pmv">5</span></label>
    <input type="range" id="pm" min="1" max="15" value="5"
      oninput="document.getElementById('pmv').textContent=this.value">
  </div>
  <div class="ctrl">
    <label>Launch Speed <span class="vl" id="lsv">4</span></label>
    <input type="range" id="ls" min="1" max="10" value="4"
      oninput="document.getElementById('lsv').textContent=this.value">
  </div>
</div>
<div class="btn-row">
  <button class="btn-l" onclick="launchRandom()">🛸 Launch Satellite</button>
  <button class="btn-c" onclick="clearSats()">✕ Clear All</button>
</div>
<div class="orbit-info">
  <div><div class="oi-val" id="nsats">0</div><div>Satellites</div></div>
  <div><div class="oi-val" id="bestorbit">—</div><div>Best Orbit</div></div>
  <div><div class="oi-val" id="escaped">0</div><div>Escaped</div></div>
</div>
</div>
<script>
const c=document.getElementById('c'),ctx=c.getContext('2d');
const W=500,H=300,CX=W/2,CY=H/2;
let sats=[],escaped=0,frame=0;
const G=500,PM_BASE=5;

function getPlanetMass(){return parseFloat(document.getElementById('pm').value)*PM_BASE;}
function getSpeed(){return parseFloat(document.getElementById('ls').value)*1.5;}

function launchRandom(){
  const angle=Math.random()*Math.PI*2;
  const dist=80+Math.random()*100;
  const x=CX+Math.cos(angle)*dist;
  const y=CY+Math.sin(angle)*dist;
  launch(x,y);
}

c.addEventListener('click',e=>{
  const rect=c.getBoundingClientRect();
  const sx=e.clientX-rect.left,sy=e.clientY-rect.top;
  const cx=sx*(W/rect.width),cy=sy*(H/rect.height);
  launch(cx,cy);
});

function launch(x,y){
  const dx=x-CX,dy=y-CY;
  const dist=Math.sqrt(dx*dx+dy*dy);
  const spd=getSpeed();
  // Launch perpendicular to radius for orbit attempt
  const vx=-dy/dist*spd*(1+Math.random()*.3-.15);
  const vy=dx/dist*spd*(1+Math.random()*.3-.15);
  const hue=Math.random()*360;
  sats.push({x,y,vx,vy,trail:[],col:`hsl(${hue},80%,60%)`,alive:true,age:0});
}

function step(){
  const PM=getPlanetMass()*PM_BASE;
  sats.forEach(s=>{
    if(!s.alive)return;
    s.trail.push([s.x,s.y]);if(s.trail.length>80)s.trail.shift();
    const dx=CX-s.x,dy=CY-s.y,dist=Math.sqrt(dx*dx+dy*dy);
    if(dist<22){s.alive=false;return;}
    if(s.x<-50||s.x>W+50||s.y<-50||s.y>H+50){
      if(s.alive){s.alive=false;escaped++;}return;
    }
    const force=G*PM/(dist*dist);
    s.vx+=dx/dist*force*.016;
    s.vy+=dy/dist*force*.016;
    s.x+=s.vx*.016*60;s.y+=s.vy*.016*60;
    s.age++;
  });
  sats=sats.filter(s=>s.alive||s.age<10);
}

function draw(){
  ctx.clearRect(0,0,W,H);
  // Space background
  ctx.fillStyle='#050510';ctx.fillRect(0,0,W,H);
  // Stars
  for(let i=0;i<80;i++){
    const sx=(i*137)%W,sy=(i*83)%H;
    const br=0.2+((i*31)%10)/20;
    ctx.fillStyle=`rgba(255,255,255,${br})`;
    ctx.fillRect(sx,sy,1,1);
  }
  // Gravity well rings
  const PM=getPlanetMass()*PM_BASE;
  for(let r=40;r<200;r+=40){
    const alpha=0.06-r/4000;
    if(alpha>0){
      ctx.strokeStyle=`rgba(96,165,250,${alpha})`;
      ctx.lineWidth=1;ctx.setLineDash([4,6]);
      ctx.beginPath();ctx.arc(CX,CY,r,0,Math.PI*2);ctx.stroke();
    }
  }
  ctx.setLineDash([]);
  // Planet
  const psize=18+PM/4;
  const pgrd=ctx.createRadialGradient(CX-psize*.3,CY-psize*.3,psize*.1,CX,CY,psize);
  pgrd.addColorStop(0,'#60a5fa');pgrd.addColorStop(.6,'#2563eb');pgrd.addColorStop(1,'#1e1b4b');
  ctx.fillStyle=pgrd;ctx.beginPath();ctx.arc(CX,CY,psize,0,Math.PI*2);ctx.fill();
  // Atmosphere glow
  const atmo=ctx.createRadialGradient(CX,CY,psize,CX,CY,psize+15);
  atmo.addColorStop(0,'rgba(96,165,250,.3)');atmo.addColorStop(1,'transparent');
  ctx.fillStyle=atmo;ctx.beginPath();ctx.arc(CX,CY,psize+15,0,Math.PI*2);ctx.fill();

  // Satellites
  sats.forEach(s=>{
    if(s.trail.length>1){
      ctx.beginPath();ctx.moveTo(s.trail[0][0],s.trail[0][1]);
      for(let i=1;i<s.trail.length;i++){
        const alpha=i/s.trail.length*0.6;
        ctx.strokeStyle=s.col.replace('hsl','hsla').replace(')',`,${alpha})`);
        ctx.lineWidth=1.5;
        ctx.lineTo(s.trail[i][0],s.trail[i][1]);ctx.stroke();
        ctx.beginPath();ctx.moveTo(s.trail[i][0],s.trail[i][1]);
      }
    }
    ctx.fillStyle=s.col;
    ctx.beginPath();ctx.arc(s.x,s.y,4,0,Math.PI*2);ctx.fill();
  });
  // HUD
  document.getElementById('nsats').textContent=sats.filter(s=>s.alive).length;
  document.getElementById('escaped').textContent=escaped;
}

function clearSats(){sats=[];escaped=0;}

function loop(){step();draw();frame++;requestAnimationFrame(loop);}
loop();
</script>
""", 680


def circuit_builder(cfg):
    return """
<style>
*{box-sizing:border-box;font-family:'Nunito',system-ui,sans-serif}
body{margin:0;background:#0a0a1a;color:white}
#wrap{max-width:520px;margin:auto;padding:10px}
.title-bar{background:linear-gradient(135deg,#d97706,#dc2626);border-radius:14px;
  padding:.7rem 1rem;text-align:center;margin-bottom:10px}
.title-bar h2{margin:0;font-size:.98rem;font-weight:800}
.circuit-display{background:#0d1117;border:1px solid rgba(255,255,255,.1);
  border-radius:14px;padding:1.2rem;margin-bottom:10px;min-height:200px}
.ctrl-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:10px}
.ctrl{background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1);
  border-radius:12px;padding:.65rem}
.ctrl label{font-size:.68rem;font-weight:700;display:block;margin-bottom:3px;text-transform:uppercase}
input[type=range]{width:100%;cursor:pointer}
.vl{font-weight:800;float:right}
.mode-row{display:flex;gap:6px;margin-bottom:8px}
.mbutton{flex:1;padding:8px;border-radius:10px;border:none;font-size:.78rem;
  font-weight:700;cursor:pointer;font-family:inherit;transition:all .15s}
.mbutton.active{color:white}
.mbutton:not(.active){background:rgba(255,255,255,.06);color:#888}
canvas{border-radius:12px;width:100%;max-width:480px;display:block;margin:auto}
.ohm-display{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;margin-top:8px}
.od{background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.08);
  border-radius:12px;padding:.6rem;text-align:center}
.od-val{font-size:1rem;font-weight:900;margin-bottom:2px}
.od-lbl{font-size:.62rem;color:#888;text-transform:uppercase}
</style>
<div id="wrap">
<div class="title-bar"><h2>🔌 Ohm's Law Live Lab — Build & Measure Circuits!</h2></div>
<div class="mode-row">
  <button class="mbutton active" id="m-series" onclick="setCircuit('series')"
    style="background:linear-gradient(135deg,#d97706,#dc2626)">Series Circuit</button>
  <button class="mbutton" id="m-parallel" onclick="setCircuit('parallel')">Parallel Circuit</button>
</div>
<canvas id="c" width="480" height="220"></canvas>
<div class="ctrl-grid">
  <div class="ctrl">
    <label style="color:#fbbf24">Battery Voltage <span class="vl" id="vv" style="color:#fbbf24">9</span> V</label>
    <input type="range" id="volt" min="1" max="24" value="9" style="accent-color:#d97706"
      oninput="document.getElementById('vv').textContent=this.value;update()">
    <label style="color:#f87171;margin-top:6px">Resistor 1 <span class="vl" id="r1v" style="color:#f87171">4</span> Ω</label>
    <input type="range" id="r1" min="1" max="20" value="4" style="accent-color:#dc2626"
      oninput="document.getElementById('r1v').textContent=this.value;update()">
  </div>
  <div class="ctrl">
    <label style="color:#a78bfa">Resistor 2 <span class="vl" id="r2v" style="color:#a78bfa">8</span> Ω</label>
    <input type="range" id="r2" min="1" max="20" value="8" style="accent-color:#7c3aed"
      oninput="document.getElementById('r2v').textContent=this.value;update()">
    <label style="color:#34d399;margin-top:6px">Resistor 3 <span class="vl" id="r3v" style="color:#34d399">12</span> Ω</label>
    <input type="range" id="r3" min="1" max="20" value="12" style="accent-color:#059669"
      oninput="document.getElementById('r3v').textContent=this.value;update()">
  </div>
</div>
<div class="ohm-display">
  <div class="od"><div class="od-val" id="d-rt" style="color:#fbbf24">—</div><div class="od-lbl">R_total (Ω)</div></div>
  <div class="od"><div class="od-val" id="d-i" style="color:#60a5fa">—</div><div class="od-lbl">Current (A)</div></div>
  <div class="od"><div class="od-val" id="d-p" style="color:#f472b6">—</div><div class="od-lbl">Power (W)</div></div>
  <div class="od"><div class="od-val" id="d-e" style="color:#34d399">—</div><div class="od-lbl">Energy/hr (J)</div></div>
</div>
</div>
<script>
const c=document.getElementById('c'),ctx=c.getContext('2d');
const W=480,H=220;
let circuitMode='series',animT=0;

function setCircuit(m){
  circuitMode=m;
  document.getElementById('m-series').className='mbutton'+(m==='series'?' active':'');
  document.getElementById('m-parallel').className='mbutton'+(m==='parallel'?' active':'');
  document.getElementById('m-series').style.background=m==='series'?'linear-gradient(135deg,#d97706,#dc2626)':'';
  document.getElementById('m-parallel').style.background=m==='parallel'?'linear-gradient(135deg,#7c3aed,#2563eb)':'';
  update();
}

function getVals(){
  return{
    V:parseFloat(document.getElementById('volt').value),
    R1:parseFloat(document.getElementById('r1').value),
    R2:parseFloat(document.getElementById('r2').value),
    R3:parseFloat(document.getElementById('r3').value),
  };
}

function update(){
  const{V,R1,R2,R3}=getVals();
  let Rt,I,I1,I2,I3;
  if(circuitMode==='series'){
    Rt=R1+R2+R3; I=V/Rt;
    I1=I;I2=I;I3=I;
  }else{
    Rt=1/(1/R1+1/R2+1/R3);
    I=V/Rt;
    I1=V/R1;I2=V/R2;I3=V/R3;
  }
  const P=V*I;
  document.getElementById('d-rt').textContent=Rt.toFixed(2);
  document.getElementById('d-i').textContent=I.toFixed(3);
  document.getElementById('d-p').textContent=P.toFixed(2);
  document.getElementById('d-e').textContent=(P*3600).toFixed(0);
}

function drawCircuit(){
  ctx.clearRect(0,0,W,H);
  ctx.fillStyle='#0d1117';ctx.fillRect(0,0,W,H);
  const{V,R1,R2,R3}=getVals();
  let Rt,I;
  if(circuitMode==='series'){Rt=R1+R2+R3;I=V/Rt;}
  else{Rt=1/(1/R1+1/R2+1/R3);I=V/Rt;}

  // Animated current flow
  const flowSpeed=Math.min(I*30,8);
  animT+=0.05;

  if(circuitMode==='series'){
    // Series: top wire → R1 → R2 → R3 → bottom wire → battery
    drawWire(40,40,440,40);drawWire(440,40,440,180);
    drawWire(440,180,40,180);drawWire(40,180,40,40);
    // Resistors on top wire
    drawResistor(80,40,'R1',R1,'#f87171');
    drawResistor(210,40,'R2',R2,'#a78bfa');
    drawResistor(340,40,'R3',R3,'#34d399');
    // Battery on left
    drawBattery(40,110,V);
    // Current particles
    drawCurrentParticles([[40,40,440,40],[440,40,440,180],[440,180,40,180]],flowSpeed);
  }else{
    // Parallel: battery on left, three branches
    drawWire(40,30,440,30);drawWire(440,30,440,190);
    drawWire(440,190,40,190);drawWire(40,190,40,30);
    // Junction lines
    drawWire(150,30,150,190);drawWire(280,30,280,190);
    // Resistors in each branch
    drawResistor(70,100,'R1',R1,'#f87171');
    drawResistor(200,100,'R2',R2,'#a78bfa');
    drawResistor(340,100,'R3',R3,'#34d399');
    // Battery
    drawBattery(40,110,V);
    drawCurrentParticles([[40,30,440,30]],flowSpeed*0.8);
  }
  // Labels
  ctx.fillStyle='rgba(255,255,255,.6)';ctx.font='bold 10px Nunito,system-ui';
  ctx.textAlign='left';
  ctx.fillText(circuitMode==='series'?`Series: Rt=${Rt.toFixed(1)}Ω, I=${I.toFixed(2)}A`:
    `Parallel: Rt=${Rt.toFixed(1)}Ω, I_total=${I.toFixed(2)}A`,8,H-6);
}

function drawWire(x1,y1,x2,y2){
  ctx.strokeStyle='rgba(250,204,21,.4)';ctx.lineWidth=2.5;
  ctx.beginPath();ctx.moveTo(x1,y1);ctx.lineTo(x2,y2);ctx.stroke();
}

function drawResistor(cx,cy,label,val,col){
  const w=60,h=22;
  ctx.fillStyle='rgba(0,0,0,.6)';ctx.strokeStyle=col;ctx.lineWidth=2;
  ctx.beginPath();ctx.roundRect(cx-w/2,cy-h/2,w,h,6);ctx.fill();ctx.stroke();
  // Zigzag inside
  ctx.strokeStyle=col;ctx.lineWidth=1.5;ctx.beginPath();
  const steps=6,sx=cx-w/2+8,ex=cx+w/2-8;
  ctx.moveTo(sx,cy);
  for(let i=0;i<steps;i++){
    const x=sx+i*(ex-sx)/steps,x2=sx+(i+1)*(ex-sx)/steps;
    ctx.lineTo(x+(ex-sx)/(steps*2),(i%2===0)?cy-8:cy+8);
    ctx.lineTo(x2,cy);
  }
  ctx.stroke();
  ctx.fillStyle='white';ctx.font='bold 9px Nunito,system-ui';ctx.textAlign='center';
  ctx.fillText(`${label}:${val}Ω`,cx,cy+h/2+12);
}

function drawBattery(cx,cy,V){
  ctx.fillStyle='rgba(251,191,36,.15)';ctx.strokeStyle='#fbbf24';ctx.lineWidth=2;
  ctx.beginPath();ctx.roundRect(cx-14,cy-30,28,60,6);ctx.fill();ctx.stroke();
  // Terminals
  for(let i=0;i<3;i++){
    const y=cy-20+i*20;
    ctx.strokeStyle=i%2===0?'#fbbf24':'rgba(251,191,36,.4)';
    ctx.lineWidth=i%2===0?3:1.5;
    ctx.beginPath();ctx.moveTo(cx-8,y);ctx.lineTo(cx+8,y);ctx.stroke();
  }
  ctx.fillStyle='#fbbf24';ctx.font='bold 10px Nunito,system-ui';ctx.textAlign='center';
  ctx.fillText(V+'V',cx,cy+45);
  ctx.fillText('+',cx+20,cy-22);ctx.fillText('−',cx+20,cy+26);
}

function drawCurrentParticles(paths,speed){
  paths.forEach(([x1,y1,x2,y2])=>{
    const len=Math.sqrt((x2-x1)**2+(y2-y1)**2);
    const nx=(x2-x1)/len,ny=(y2-y1)/len;
    const numP=Math.floor(len/30);
    for(let i=0;i<numP;i++){
      const t=((animT*speed*0.1+i/numP)%1);
      const px=x1+nx*len*t,py=y1+ny*len*t;
      const grd=ctx.createRadialGradient(px,py,0,px,py,5);
      grd.addColorStop(0,'rgba(250,204,21,.9)');
      grd.addColorStop(1,'rgba(250,204,21,0)');
      ctx.fillStyle=grd;
      ctx.beginPath();ctx.arc(px,py,5,0,Math.PI*2);ctx.fill();
    }
  });
}

function loop(){drawCircuit();animT+=0.05;requestAnimationFrame(loop);}
update();loop();
</script>
""", 700


def optics_game(cfg):
    return """
<style>
*{box-sizing:border-box;font-family:'Nunito',system-ui,sans-serif}
body{margin:0;background:#0a0a1a;color:white}
#wrap{max-width:520px;margin:auto;padding:10px}
.title-bar{background:linear-gradient(135deg,#db2777,#7c3aed);border-radius:14px;
  padding:.7rem 1rem;text-align:center;margin-bottom:8px}
.title-bar h2{margin:0;font-size:.95rem;font-weight:800}
canvas{border-radius:14px;border:1px solid rgba(255,255,255,.12);
  display:block;margin:auto;width:100%;max-width:500px;cursor:col-resize}
.ctrl-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:8px}
.ctrl{background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1);
  border-radius:12px;padding:.65rem}
.ctrl label{font-size:.68rem;font-weight:700;display:block;margin-bottom:3px;text-transform:uppercase}
input[type=range]{width:100%;cursor:pointer}
.vl{font-weight:800;float:right}
.lens-tabs{display:flex;gap:6px;margin-top:8px}
.lt{flex:1;padding:8px;border-radius:10px;border:none;font-size:.78rem;
  font-weight:700;cursor:pointer;font-family:inherit}
.lt.active{color:white}
.lt:not(.active){background:rgba(255,255,255,.06);color:#888}
.results{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;margin-top:8px}
.res{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);
  border-radius:10px;padding:.55rem;text-align:center}
.res-v{font-size:.9rem;font-weight:900}
.res-l{font-size:.6rem;color:#888;text-transform:uppercase}
</style>
<div id="wrap">
<div class="title-bar"><h2>🔍 Ray Tracer — Lenses & Mirrors Live!</h2></div>
<div class="lens-tabs">
  <button class="lt active" id="lt-cvx" onclick="setLens('convex')"
    style="background:linear-gradient(135deg,#db2777,#7c3aed)">Convex Lens</button>
  <button class="lt" id="lt-ccv" onclick="setLens('concave')">Concave Lens</button>
  <button class="lt" id="lt-cm" onclick="setLens('cmirror')">Concave Mirror</button>
  <button class="lt" id="lt-vm" onclick="setLens('vmirror')">Convex Mirror</button>
</div>
<canvas id="c" width="500" height="260"></canvas>
<div class="ctrl-grid">
  <div class="ctrl">
    <label style="color:#f472b6">Object Distance <span class="vl" id="udv" style="color:#f472b6">15</span> cm</label>
    <input type="range" id="ud" min="5" max="50" value="15" style="accent-color:#db2777"
      oninput="document.getElementById('udv').textContent=this.value">
    <label style="color:#a78bfa;margin-top:6px">Focal Length <span class="vl" id="fdv" style="color:#a78bfa">10</span> cm</label>
    <input type="range" id="fd" min="5" max="30" value="10" style="accent-color:#7c3aed"
      oninput="document.getElementById('fdv').textContent=this.value">
  </div>
  <div class="ctrl">
    <label style="color:#34d399">Object Height <span class="vl" id="hov" style="color:#34d399">4</span> cm</label>
    <input type="range" id="ho" min="1" max="8" value="4" style="accent-color:#059669"
      oninput="document.getElementById('hov').textContent=this.value">
    <label style="color:#60a5fa;margin-top:6px">n (refractive idx) <span class="vl" id="nv" style="color:#60a5fa">1.5</span></label>
    <input type="range" id="nval" min="1.0" max="2.5" value="1.5" step=".1" style="accent-color:#2563eb"
      oninput="document.getElementById('nv').textContent=parseFloat(this.value).toFixed(1)">
  </div>
</div>
<div class="results">
  <div class="res"><div class="res-v" id="r-v" style="color:#60a5fa">—</div><div class="res-l">Image dist (cm)</div></div>
  <div class="res"><div class="res-v" id="r-m" style="color:#f472b6">—</div><div class="res-l">Magnification</div></div>
  <div class="res"><div class="res-v" id="r-hi" style="color:#34d399">—</div><div class="res-l">Image height</div></div>
  <div class="res"><div class="res-v" id="r-type" style="color:#fbbf24">—</div><div class="res-l">Image type</div></div>
</div>
</div>
<script>
const c=document.getElementById('c'),ctx=c.getContext('2d');
const W=500,H=260,CX=W/2,CY=H/2;
let lensType='convex';

function setLens(t){
  lensType=t;
  ['cvx','ccv','cm','vm'].forEach((id,i)=>{
    const types=['convex','concave','cmirror','vmirror'];
    const el=document.getElementById('lt-'+id);
    el.className='lt'+(types[i]===t?' active':'');
    el.style.background=types[i]===t?'linear-gradient(135deg,#db2777,#7c3aed)':'';
  });
}

function drawScene(){
  ctx.clearRect(0,0,W,H);
  ctx.fillStyle='#080818';ctx.fillRect(0,0,W,H);
  const u=parseFloat(document.getElementById('ud').value);
  const f=parseFloat(document.getElementById('fd').value);
  const ho=parseFloat(document.getElementById('ho').value);
  const n=parseFloat(document.getElementById('nval').value);
  const scale=5;

  // Principal axis
  ctx.strokeStyle='rgba(255,255,255,.15)';ctx.lineWidth=1;ctx.setLineDash([6,4]);
  ctx.beginPath();ctx.moveTo(0,CY);ctx.lineTo(W,CY);ctx.stroke();
  ctx.setLineDash([]);

  let v,m,imgType;
  const isMirror=lensType==='cmirror'||lensType==='vmirror';
  const isConverging=lensType==='convex'||lensType==='cmirror';

  if(lensType==='convex'||lensType==='concave'){
    // Lens formula: 1/v - 1/u = 1/f (u negative on same side as object)
    const uSigned=-u;
    const fSigned=lensType==='convex'?f:-f;
    v=1/(1/fSigned-1/uSigned);
    m=v/uSigned;
  }else{
    // Mirror: 1/v + 1/u = 1/f
    const fSigned=lensType==='cmirror'?f:-f;
    v=1/(1/fSigned-1/u);
    m=-v/u;
  }

  const hi=ho*Math.abs(m);
  if(!isFinite(v)){imgType='At ∞';}
  else if(v>0&&!isMirror){imgType='Real, inv';}
  else if(v<0&&!isMirror){imgType='Virtual, erect';}
  else if(v>0&&isMirror){imgType='Real, inv';}
  else{imgType='Virtual, erect';}

  document.getElementById('r-v').textContent=isFinite(v)?v.toFixed(1)+'':'∞';
  document.getElementById('r-m').textContent=isFinite(m)?m.toFixed(2):'∞';
  document.getElementById('r-hi').textContent=isFinite(hi)?hi.toFixed(1):'∞';
  document.getElementById('r-type').textContent=imgType;

  // Draw lens/mirror
  if(!isMirror){
    ctx.strokeStyle='rgba(167,139,250,.8)';ctx.lineWidth=3;
    const lensH=80;
    if(lensType==='convex'){
      ctx.beginPath();ctx.moveTo(CX,CY-lensH);
      ctx.bezierCurveTo(CX+20,CY-lensH/2,CX+20,CY+lensH/2,CX,CY+lensH);ctx.stroke();
      ctx.beginPath();ctx.moveTo(CX,CY-lensH);
      ctx.bezierCurveTo(CX-20,CY-lensH/2,CX-20,CY+lensH/2,CX,CY+lensH);ctx.stroke();
    }else{
      ctx.beginPath();ctx.moveTo(CX,CY-lensH);
      ctx.bezierCurveTo(CX-15,CY-lensH/2,CX-15,CY+lensH/2,CX,CY+lensH);ctx.stroke();
      ctx.beginPath();ctx.moveTo(CX,CY-lensH);
      ctx.bezierCurveTo(CX+15,CY-lensH/2,CX+15,CY+lensH/2,CX,CY+lensH);ctx.stroke();
    }
    // Focus points
    ctx.fillStyle='#fbbf24';
    ctx.beginPath();ctx.arc(CX+f*scale,CY,5,0,Math.PI*2);ctx.fill();
    ctx.beginPath();ctx.arc(CX-f*scale,CY,5,0,Math.PI*2);ctx.fill();
    ctx.fillStyle='rgba(251,191,36,.6)';ctx.font='bold 9px Nunito,system-ui';ctx.textAlign='center';
    ctx.fillText('F',CX+f*scale,CY+16);ctx.fillText('F',CX-f*scale,CY+16);
  }else{
    // Mirror arc
    ctx.strokeStyle='rgba(167,139,250,.8)';ctx.lineWidth=3;
    const r=f*scale*2;
    const startA=lensType==='cmirror'?-Math.PI/3:Math.PI*2/3;
    const endA=lensType==='cmirror'?Math.PI/3:-Math.PI*2/3;
    ctx.beginPath();
    if(lensType==='cmirror'){
      ctx.arc(CX+r,CY,r,Math.PI-Math.PI/3,Math.PI+Math.PI/3);
    }else{
      ctx.arc(CX-r,CY,r,-Math.PI/3,Math.PI/3);
    }
    ctx.stroke();
    ctx.fillStyle='#fbbf24';
    ctx.beginPath();ctx.arc(CX+(lensType==='cmirror'?-1:1)*f*scale,CY,5,0,Math.PI*2);ctx.fill();
  }

  // Object arrow
  const objX=CX-u*scale;
  ctx.strokeStyle='#34d399';ctx.lineWidth=2.5;
  ctx.beginPath();ctx.moveTo(objX,CY);ctx.lineTo(objX,CY-ho*scale);ctx.stroke();
  ctx.fillStyle='#34d399';
  ctx.beginPath();ctx.moveTo(objX,CY-ho*scale);
  ctx.lineTo(objX-6,CY-ho*scale+10);ctx.lineTo(objX+6,CY-ho*scale+10);ctx.fill();
  ctx.fillStyle='rgba(52,211,153,.7)';ctx.font='bold 9px Nunito,system-ui';ctx.textAlign='center';
  ctx.fillText('Object',objX,CY+16);

  // Rays from object tip
  if(isFinite(v)&&Math.abs(v)<200){
    const imgX=CX+(isMirror?-v:v)*scale;
    const imgY=CY-ho*m*scale;
    // Ray 1: parallel to axis → through F
    ctx.strokeStyle='rgba(248,113,113,.7)';ctx.lineWidth=1.5;
    ctx.beginPath();ctx.moveTo(objX,CY-ho*scale);ctx.lineTo(CX,CY-ho*scale);
    ctx.lineTo(imgX,imgY);ctx.stroke();
    // Ray 2: through centre
    ctx.strokeStyle='rgba(96,165,250,.7)';ctx.lineWidth=1.5;
    ctx.beginPath();ctx.moveTo(objX,CY-ho*scale);
    ctx.lineTo(CX,CY);ctx.lineTo(imgX,imgY);ctx.stroke();
    // Image arrow
    if(imgX>10&&imgX<W-10){
      const imgCol=v>0?'#f87171':'rgba(248,113,113,.5)';
      ctx.strokeStyle=imgCol;ctx.lineWidth=2;ctx.setLineDash(v<0?[4,3]:[]);
      ctx.beginPath();ctx.moveTo(imgX,CY);ctx.lineTo(imgX,imgY);ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle=imgCol;
      ctx.beginPath();ctx.moveTo(imgX,imgY);
      ctx.lineTo(imgX-5,imgY+(m>0?-1:1)*10);ctx.lineTo(imgX+5,imgY+(m>0?-1:1)*10);ctx.fill();
      ctx.fillStyle='rgba(248,113,113,.8)';ctx.font='bold 9px Nunito,system-ui';ctx.textAlign='center';
      ctx.fillText('Image',imgX,CY+16);
    }
  }
  // n label
  ctx.fillStyle='rgba(96,165,250,.6)';ctx.font='bold 9px Nunito,system-ui';ctx.textAlign='left';
  ctx.fillText(`n=${n} | λ = 589nm (yellow)`,8,H-6);
}

function loop(){drawScene();requestAnimationFrame(loop);}
loop();
</script>
""", 720


def gas_law_sim(cfg):
    return """
<style>
*{box-sizing:border-box;font-family:'Nunito',system-ui,sans-serif}
body{margin:0;background:#0a0a1a;color:white}
#wrap{max-width:520px;margin:auto;padding:10px}
.title-bar{background:linear-gradient(135deg,#f97316,#dc2626);border-radius:14px;
  padding:.7rem 1rem;text-align:center;margin-bottom:8px}
.title-bar h2{margin:0;font-size:.98rem;font-weight:800}
canvas{border-radius:14px;border:1px solid rgba(255,255,255,.12);display:block;
  margin:auto;width:100%;max-width:500px}
.ctrl-grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:7px;margin-top:8px}
.ctrl{background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1);
  border-radius:12px;padding:.6rem}
.ctrl label{font-size:.65rem;font-weight:700;display:block;margin-bottom:3px;text-transform:uppercase}
input[type=range]{width:100%;cursor:pointer}
.vl{font-weight:800;float:right;font-size:.82rem}
.law-tabs{display:flex;gap:5px;margin-bottom:8px}
.lawtab{flex:1;padding:7px;border-radius:10px;border:none;font-size:.72rem;
  font-weight:700;cursor:pointer;font-family:inherit}
.lawtab.active{color:white}
.lawtab:not(.active){background:rgba(255,255,255,.06);color:#888}
.result-row{display:grid;grid-template-columns:repeat(3,1fr);gap:6px;margin-top:8px}
.res{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);
  border-radius:10px;padding:.55rem;text-align:center}
.res-v{font-size:.95rem;font-weight:900}
.res-l{font-size:.6rem;color:#888}
</style>
<div id="wrap">
<div class="title-bar"><h2>💨 Ideal Gas Law Lab — PV=nRT Live!</h2></div>
<div class="law-tabs">
  <button class="lawtab active" id="lt-boyle" onclick="setLaw('boyle')"
    style="background:linear-gradient(135deg,#f97316,#dc2626)">Boyle's Law</button>
  <button class="lawtab" id="lt-charles" onclick="setLaw('charles')">Charles's Law</button>
  <button class="lawtab" id="lt-ideal" onclick="setLaw('ideal')">PV=nRT</button>
</div>
<canvas id="c" width="500" height="230"></canvas>
<div class="ctrl-grid">
  <div class="ctrl">
    <label style="color:#fbbf24">Pressure <span class="vl" id="pv" style="color:#fbbf24">2</span> atm</label>
    <input type="range" id="pres" min=".5" max="10" value="2" step=".5" style="accent-color:#f97316"
      oninput="document.getElementById('pv').textContent=this.value;calc()">
  </div>
  <div class="ctrl">
    <label style="color:#60a5fa">Volume <span class="vl" id="vv" style="color:#60a5fa">5</span> L</label>
    <input type="range" id="vol" min="1" max="20" value="5" style="accent-color:#2563eb"
      oninput="document.getElementById('vv').textContent=this.value;calc()">
  </div>
  <div class="ctrl">
    <label style="color:#f87171">Temp <span class="vl" id="tv" style="color:#f87171">300</span> K</label>
    <input type="range" id="temp" min="100" max="1000" value="300" step="10" style="accent-color:#dc2626"
      oninput="document.getElementById('tv').textContent=this.value;calc()">
  </div>
</div>
<div class="result-row">
  <div class="res"><div class="res-v" id="r-pv" style="color:#fbbf24">—</div><div class="res-l">PV (atm·L)</div></div>
  <div class="res"><div class="res-v" id="r-n" style="color:#34d399">—</div><div class="res-l">Moles (n)</div></div>
  <div class="res"><div class="res-v" id="r-law" style="color:#a78bfa">—</div><div class="res-l">Law Applied</div></div>
</div>
</div>
<script>
const c=document.getElementById('c'),ctx=c.getContext('2d');
const W=500,H=230;let lawMode='boyle',particles=[],animId;
const R=0.0821;

function setLaw(l){
  lawMode=l;
  ['boyle','charles','ideal'].forEach(id=>{
    const el=document.getElementById('lt-'+id);
    el.className='lawtab'+(id===l?' active':'');
    el.style.background=id===l?'linear-gradient(135deg,#f97316,#dc2626)':'';
  });
  calc();
}

function calc(){
  const P=parseFloat(document.getElementById('pres').value);
  const V=parseFloat(document.getElementById('vol').value);
  const T=parseFloat(document.getElementById('temp').value);
  const n=P*V/(R*T);
  document.getElementById('r-pv').textContent=(P*V).toFixed(1);
  document.getElementById('r-n').textContent=n.toFixed(3);
  document.getElementById('r-law').textContent=lawMode==='boyle'?'PV=const':lawMode==='charles'?'V/T=const':'PV=nRT';
  updateParticles(P,V,T);
}

function updateParticles(P,V,T){
  const boxW=Math.min(V*20,300);const boxH=150;
  const boxX=(W-boxW)/2,boxY=30;
  const nP=Math.min(Math.floor(P*V*3),60);
  const speed=Math.sqrt(T/100)*2;
  while(particles.length<nP)particles.push({
    x:boxX+Math.random()*boxW,y:boxY+Math.random()*boxH,
    vx:(Math.random()-.5)*speed*2,vy:(Math.random()-.5)*speed*2,
    col:`hsl(${Math.random()*60+10},80%,60%)`
  });
  particles=particles.slice(0,nP);
  particles.forEach(p=>{
    p.vx=(Math.random()-.5)*speed+(p.vx*.7);
    p.vy=(Math.random()-.5)*speed+(p.vy*.7);
    const sp=Math.sqrt(p.vx**2+p.vy**2);
    if(sp>speed*3){p.vx*=.5;p.vy*=.5;}
  });
}

function drawScene(){
  ctx.clearRect(0,0,W,H);
  ctx.fillStyle='#050510';ctx.fillRect(0,0,W,H);
  const P=parseFloat(document.getElementById('pres').value);
  const V=parseFloat(document.getElementById('vol').value);
  const T=parseFloat(document.getElementById('temp').value);
  const boxW=Math.min(V*20,300);const boxH=150;
  const boxX=(W-boxW)/2,boxY=30;

  // Thermal glow
  const hue=Math.max(0,Math.min(60,60-(T-100)/900*60));
  const grd=ctx.createRadialGradient(W/2,H/2,0,W/2,H/2,Math.max(boxW,boxH));
  grd.addColorStop(0,`hsla(${hue},70%,50%,0.08)`);
  grd.addColorStop(1,'transparent');
  ctx.fillStyle=grd;ctx.fillRect(boxX,boxY,boxW,boxH);

  // Container
  ctx.strokeStyle=`rgba(251,191,36,${0.3+P/20})`;ctx.lineWidth=2+P/5;
  ctx.strokeRect(boxX,boxY,boxW,boxH);
  ctx.fillStyle='rgba(255,255,255,.02)';ctx.fillRect(boxX,boxY,boxW,boxH);

  // Pressure indicator on sides
  const pw=Math.min(P*3,20);
  ctx.fillStyle=`rgba(251,191,36,${P/12})`;
  ctx.fillRect(boxX-pw,boxY,pw,boxH);
  ctx.fillRect(boxX+boxW,boxY,pw,boxH);

  // Particles
  particles.forEach(p=>{
    p.x+=p.vx;p.y+=p.vy;
    if(p.x<boxX+4){p.x=boxX+4;p.vx=Math.abs(p.vx);}
    if(p.x>boxX+boxW-4){p.x=boxX+boxW-4;p.vx=-Math.abs(p.vx);}
    if(p.y<boxY+4){p.y=boxY+4;p.vy=Math.abs(p.vy);}
    if(p.y>boxY+boxH-4){p.y=boxY+boxH-4;p.vy=-Math.abs(p.vy);}
    const speed=Math.sqrt(p.vx**2+p.vy**2);
    const grd2=ctx.createRadialGradient(p.x,p.y,0,p.x,p.y,4+speed*.3);
    grd2.addColorStop(0,p.col);grd2.addColorStop(1,'transparent');
    ctx.fillStyle=grd2;
    ctx.beginPath();ctx.arc(p.x,p.y,4+speed*.2,0,Math.PI*2);ctx.fill();
  });

  // Labels
  ctx.fillStyle='rgba(255,255,255,.7)';ctx.font='bold 10px Nunito,system-ui';ctx.textAlign='center';
  ctx.fillText(`P=${P} atm`,boxX+boxW/2,boxY-8);
  ctx.fillText(`V=${boxW.toFixed(0)} px (${V} L)`,boxX+boxW/2,boxY+boxH+16);
  ctx.textAlign='left';
  ctx.fillStyle='rgba(248,113,113,.8)';
  ctx.fillText(`T=${T}K = ${T-273}°C`,8,H-6);
  ctx.fillStyle='rgba(96,165,250,.8)';ctx.textAlign='right';
  ctx.fillText('PV = nRT  (R = 0.0821 atm·L/mol·K)',W-8,H-6);

  requestAnimationFrame(drawScene);
}
calc();drawScene();
</script>
""", 680


# map game type → generator function
GAME_GEN = {
    "projectile": projectile_game,
    "collision":  collision_game,
    "wave":       wave_lab,
    "gravity_well": gravity_well,
    "circuit":    circuit_builder,
    "ohm_builder": circuit_builder,
    "optics":     optics_game,
    "gas_law":    gas_law_sim,
    "freefall":   projectile_game,
    "force_balance": collision_game,
    "pressure_sim": gas_law_sim,
    "friction_racer": collision_game,
    "echo_sonar": wave_lab,
    "string_wave": wave_lab,
    "refraction_game": optics_game,
    "carnot_engine": gas_law_sim,
    "heat_transfer": gas_law_sim,
    "photoelectric": wave_lab,
    "atom_builder": wave_lab,
    "decay_chain": wave_lab,
    "fission_chain": collision_game,
    "velocity_graph": wave_lab,
}

def render_game(game):
    gen = GAME_GEN.get(game["type"])
    if not gen: return
    html, h = gen(game)
    components.html(html, height=h, scrolling=False)


# ─── UI helpers ───────────────────────────────────────────────────────────────
def hdr():
    lvl = S.xp//100+1; pct = S.xp%100
    nm = f"Hi {S.name}! " if S.name else ""
    st.markdown(f"""
    <div class="hdr">
      <h1>⚛️ Let's Learn Physics with National</h1>
      <p>{nm}Grade: {S.grade} &nbsp;·&nbsp; ⭐ {S.stars} &nbsp;·&nbsp;
         ✨ {S.xp} XP &nbsp;·&nbsp; 🔥 {S.streak}d &nbsp;·&nbsp; Lv {lvl}</p>
      <div class="xp-wrap" style="margin-top:6px">
        <div class="xp-fill" style="width:{pct}%"></div>
      </div>
    </div>""", unsafe_allow_html=True)

def nav():
    c1,c2,c3 = st.columns(3)
    with c1:
        if st.button("🏠 Topics", use_container_width=True,
                     type="primary" if S.screen=="home" else "secondary"): go("home")
    with c2:
        if st.button("🏆 Progress", use_container_width=True,
                     type="primary" if S.screen=="progress" else "secondary"): go("progress")
    with c3:
        if st.button("🎮 Free Play", use_container_width=True,
                     type="primary" if S.screen=="arcade" else "secondary"): go("arcade")

def steps_bar(cur):
    stages=["story","games","note","quiz"]
    icons=["🎬","🎮","📖","📝"]; labels=["Intro","Games","Notes","Quiz"]
    html='<div class="steps">'
    for i,(ic,lb) in enumerate(zip(icons,labels)):
        s=stages[i]
        done_s=stages.index(cur)>i
        active_s=cur==s
        if active_s: col,bg="#fff","rgba(124,58,237,.6)"
        elif done_s: col,bg="#34d399","transparent"
        else: col,bg="#555","transparent"
        html+=f'<div style="display:flex;align-items:center;gap:4px;padding:4px 8px;border-radius:20px;background:{bg}">'
        html+=f'<span style="font-size:.8rem">{ic}</span>'
        html+=f'<span style="font-size:.68rem;font-weight:700;color:{col}">{lb}</span>'
        html+='</div>'
        if i<3: html+=f'<div style="flex:1;height:2px;background:{"#34d399" if done_s else "rgba(255,255,255,.1)"};border-radius:2px"></div>'
    html+='</div>'
    st.markdown(html, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SCREENS
# ══════════════════════════════════════════════════════════════════════════════
def screen_onboard():
    st.markdown("""
    <div style="background:linear-gradient(135deg,#0f0c29,#302b63,#24243e);
        color:white;border-radius:24px;padding:2.2rem;text-align:center;
        margin-bottom:1.2rem;border:1px solid rgba(255,255,255,.08)">
      <div style="font-size:3.5rem;margin-bottom:.5rem">⚛️</div>
      <h1 style="font-size:1.7rem;margin:.3rem 0;font-weight:900;
          background:linear-gradient(90deg,#a78bfa,#60a5fa,#34d399);
          -webkit-background-clip:text;-webkit-text-fill-color:transparent">
        Let's Learn Physics!</h1>
      <p style="color:rgba(255,255,255,.75);font-size:.92rem;margin:.5rem 0">
        🚀 Real simulations &nbsp;·&nbsp; 🎮 Dynamic games &nbsp;·&nbsp; 📖 Complete notes<br>
        Built for Grade 8–12 students 🎓
      </p>
    </div>""", unsafe_allow_html=True)

    c1,c2,c3 = st.columns(3)
    c1.markdown("### 🚀\n**Rocket Launch**\nProjectile simulator")
    c2.markdown("### 💥\n**Collisions**\nMomentum lab")
    c3.markdown("### 🌌\n**Gravity Well**\nOrbit simulator")
    c4,c5,c6 = st.columns(3)
    c4.markdown("### 🔌\n**Circuit Lab**\nOhm's Law live")
    c5.markdown("### 〰️\n**Wave Lab**\nInterference & more")
    c6.markdown("### 🔍\n**Ray Tracer**\nLens & mirror optics")

    st.markdown("---")
    name = st.text_input("Your name (optional)", placeholder="e.g. Arjun, Priya…")
    grade = st.selectbox("Your class", GRADES, index=1)
    if st.button("🚀 Start Physics Journey!", type="primary", use_container_width=True):
        S.name=name.strip(); S.grade=grade; S.onboarded=True; st.rerun()


def screen_home():
    hdr(); nav()
    ng = st.selectbox("📚 Grade", GRADES, index=GRADES.index(S.grade), key="grade_sel")
    if ng!=S.grade: S.grade=ng; st.rerun()

    topics = get_topics(S.grade)
    done = len([t for t in topics if t["id"] in S.done])
    pct = int(done/max(len(topics),1)*100)
    st.markdown(f"**{S.grade} — {done}/{len(topics)} topics · {pct}% complete**")
    st.markdown(f'<div class="xp-wrap"><div class="xp-fill" style="width:{pct}%"></div></div>', unsafe_allow_html=True)
    st.markdown(" ")

    for t in topics:
        is_done = t["id"] in S.done
        sc = S.scores.get(t["id"])
        sc_str = f" · Quiz: {sc}/5" if sc is not None else ""
        game_icons = " ".join(["🚀" if g["type"]=="projectile" else
                                "💥" if g["type"]=="collision" else
                                "🌌" if g["type"]=="gravity_well" else
                                "〰️" if g["type"]=="wave" else
                                "🔌" if g["type"] in ("circuit","ohm_builder") else
                                "🔍" if g["type"]=="optics" else
                                "💨" if g["type"]=="gas_law" else "🎮"
                                for g in t["games"]])
        c1,c2 = st.columns([5,1])
        with c1:
            st.markdown(f"""
            <div class="topic-card" style="background:linear-gradient(135deg,{t['color']}22,{t['color']}08);
                border-color:{t['color']}44">
              <div style="display:flex;align-items:center;gap:12px">
                <div style="width:46px;height:46px;border-radius:14px;
                    background:linear-gradient(135deg,{t['color']},rgba(0,0,0,.3));
                    display:flex;align-items:center;justify-content:center;
                    font-size:1.4rem;flex-shrink:0;box-shadow:0 4px 12px {t['color']}44">
                  {t['emoji']}</div>
                <div style="flex:1">
                  <div style="font-weight:800;font-size:.95rem;color:white">{t['title']}</div>
                  <div style="font-size:.7rem;color:rgba(255,255,255,.5);margin-top:2px">
                    {'✅' if is_done else '🔓'} {t['chapter']}{sc_str}</div>
                  <div style="font-size:.72rem;color:rgba(255,255,255,.4);margin-top:2px">
                    Games: {game_icons}</div>
                </div>
              </div>
              <div style="font-size:.75rem;color:{t['color']};margin-top:.5rem;
                  padding:.4rem .7rem;background:{t['color']}11;border-radius:8px">
                {t['tagline']}</div>
            </div>""", unsafe_allow_html=True)
        with c2:
            st.markdown("<div style='padding-top:.35rem'></div>", unsafe_allow_html=True)
            if st.button("Redo 🔄" if is_done else "Play ▶️",
                         key=f"p_{t['id']}", use_container_width=True,
                         type="secondary" if is_done else "primary"):
                begin(t["id"])

    st.markdown("---")
    c1,c2,c3 = st.columns(3)
    c1.metric("⭐ Stars", S.stars)
    c2.metric("✨ XP", S.xp)
    c3.metric("✅ Done", len(S.done))


def screen_topic():
    t = get_topic(S.tid)
    if not t: go("home"); return
    hdr()
    if st.button("← Back to Topics", key="back"): go("home")

    if S.stage == "story":
        s = t["story"]
        st.markdown(f"""
        <div style="background:linear-gradient(135deg,{t['color']}33,{t['color']}11);
            border:1px solid {t['color']}55;border-radius:20px;padding:1.3rem;margin-bottom:1rem">
          <div style="font-size:1.1rem;font-weight:800;color:white;margin-bottom:.6rem">{s['title']}</div>
          <div style="font-size:.9rem;color:rgba(255,255,255,.85);line-height:1.75">{s['text']}</div>
        </div>""", unsafe_allow_html=True)
        st.markdown(f"### This topic has **{len(t['games'])} interactive simulations**!")
        for g in t["games"]:
            icon = {"projectile":"🚀","collision":"💥","wave":"〰️","gravity_well":"🌌",
                    "circuit":"🔌","ohm_builder":"📊","optics":"🔍","gas_law":"💨",
                    "freefall":"🌍","force_balance":"⚖️"}.get(g["type"],"🎮")
            st.markdown(f"**{icon} {g['title']}** — {g['desc']}")
        st.markdown(" ")
        if st.button("🎮 Play the Simulations!", type="primary", use_container_width=True):
            S.stage="games"; st.rerun()

    elif S.stage == "games":
        games = t["games"]
        steps_bar("games")
        tabs = st.tabs([f"🎮 {g['title'][:25]}" for g in games])
        for tab, game in zip(tabs, games):
            with tab:
                st.markdown(f"**{game['desc']}**")
                render_game(game)
        st.markdown("---")
        if st.button("📖 Read Study Notes →", type="primary", use_container_width=True):
            S.stage="note"; st.rerun()

    elif S.stage == "note":
        steps_bar("note")
        note = t["note"]
        st.markdown(f"""
        <div style="background:linear-gradient(135deg,#059669,#10b981);color:white;
            padding:1rem;border-radius:17px;text-align:center;margin-bottom:.9rem">
          <div style="font-size:1.8rem">📖</div>
          <div style="font-size:1rem;font-weight:800">Complete Study Notes — {t['title']}</div>
          <div style="opacity:.8;font-size:.75rem;margin-top:3px">Read carefully — quiz is next!</div>
        </div>""", unsafe_allow_html=True)

        for sec in note["sections"]:
            fact = f'<div class="fact-box">{sec["fact"]}</div>' if sec.get("fact") else ""
            st.markdown(f"""
            <div class="note-card">
              <h4>{sec['h']}</h4>
              <div class="note-body">{sec['body']}</div>
              {fact}
            </div>""", unsafe_allow_html=True)

        if note.get("memory"):
            st.markdown(f'<div class="mem-card">🧠 {note["memory"]}</div>', unsafe_allow_html=True)
        if note.get("tips"):
            tips = "".join([f'<div style="font-size:.83rem;color:#5a3800;margin:.22rem 0">📌 {tip}</div>' for tip in note["tips"]])
            st.markdown(f'<div class="tip-card"><b style="color:#5a3800;font-size:.88rem">🎯 Exam Tips — Know These!</b>{tips}</div>', unsafe_allow_html=True)

        st.markdown(" ")
        if st.button("📝 I'm Ready — Take the Quiz! →", type="primary", use_container_width=True):
            S.stage="quiz"; S.quiz_i=0; S.quiz_ans=False; S.quiz_sel=None; S.quiz_sc=0; st.rerun()

    elif S.stage == "quiz":
        quiz = t["quiz"]
        if S.quiz_i >= len(quiz):
            S.stage="done"; st.rerun(); return
        steps_bar("quiz")
        st.markdown(f"**📝 Q{S.quiz_i+1}/{len(quiz)}** · Score so far: {S.quiz_sc}/{S.quiz_i}")
        st.progress(S.quiz_i/len(quiz))
        q = quiz[S.quiz_i]
        st.markdown(f"""
        <div style="background:linear-gradient(135deg,rgba(99,102,241,.15),rgba(139,92,246,.1));
            border:1px solid rgba(99,102,241,.4);border-radius:15px;
            padding:1rem;margin-bottom:.9rem;font-size:.93rem;font-weight:700;
            color:white;line-height:1.55">
          ❓ {q['q']}
        </div>""", unsafe_allow_html=True)
        if not S.quiz_ans:
            for i,opt in enumerate(q["opts"]):
                if st.button(f"  {opt}", key=f"qo_{S.quiz_i}_{i}", use_container_width=True):
                    S.quiz_ans=True; S.quiz_sel=i
                    if i==q["ans"]: S.quiz_sc+=1; S.xp+=20; S.stars+=1
                    st.rerun()
        else:
            for i,opt in enumerate(q["opts"]):
                if i==q["ans"]: st.success(f"✅ {opt}")
                elif i==S.quiz_sel: st.error(f"❌ {opt}")
                else: st.button(opt, key=f"qd_{S.quiz_i}_{i}", disabled=True, use_container_width=True)
            if S.quiz_sel==q["ans"]: st.success("🎉 Correct!")
            else: st.error(f"Correct answer: **{q['opts'][q['ans']]}**")
            st.info(f"📖 {q['exp']}")
            lbl = "Finish Quiz 🏁" if S.quiz_i==len(quiz)-1 else f"Next ({S.quiz_i+2}/{len(quiz)}) →"
            if st.button(lbl, type="primary", use_container_width=True):
                S.quiz_i+=1; S.quiz_ans=False; S.quiz_sel=None; st.rerun()

    elif S.stage == "done":
        sc=S.quiz_sc; tot=len(t["quiz"]); pct=int(sc/max(tot,1)*100)
        S.scores[t["id"]]=sc; S.done.add(t["id"]); S.xp+=50; S.stars+=sc
        em = "🏆" if pct==100 else "🌟" if pct>=80 else "😊" if pct>=60 else "💪"
        msg = ("PERFECT! You're a Physics Genius! 🎓" if pct==100 else
               "Excellent! Great understanding! 🌟" if pct>=80 else
               "Good job! A little more practice! 💪" if pct>=60 else
               "Keep going — re-read the notes! 📖")
        st.markdown(f"""
        <div class="score-hero">
          <div style="font-size:3rem;margin-bottom:.4rem">{em}</div>
          <div style="font-size:3.5rem;font-weight:900;background:linear-gradient(90deg,#a78bfa,#60a5fa);
              -webkit-background-clip:text;-webkit-text-fill-color:transparent">{sc}/{tot}</div>
          <div style="color:rgba(255,255,255,.9);font-size:1rem;margin:.5rem 0">{msg}</div>
          <div style="color:rgba(255,255,255,.5);font-size:.8rem">+50 XP bonus for completing! ✨</div>
        </div>""", unsafe_allow_html=True)
        c1,c2 = st.columns(2)
        with c1:
            if st.button("🎮 Replay Games", use_container_width=True):
                S.stage="games"; st.rerun()
        with c2:
            if st.button("🏠 Back to Topics →", type="primary", use_container_width=True): go("home")
        # next topic
        all_t = get_topics(S.grade)
        ci = next((i for i,x in enumerate(all_t) if x["id"]==S.tid), -1)
        if ci>=0 and ci+1<len(all_t):
            nt=all_t[ci+1]; st.markdown("---")
            if st.button(f"▶️ Next: {nt['emoji']} {nt['title']}", type="primary", use_container_width=True):
                begin(nt["id"])


def screen_progress():
    hdr(); nav()
    st.markdown("### 🏆 Your Physics Journey")
    lvl=S.xp//100+1; xp_in=S.xp%100
    st.markdown(f"**Level {lvl} Physics Explorer · {S.xp} XP**")
    st.markdown(f'<div class="xp-wrap"><div class="xp-fill" style="width:{xp_in}%"></div></div>', unsafe_allow_html=True)
    st.markdown(" ")
    c1,c2,c3,c4 = st.columns(4)
    c1.metric("⭐",S.stars); c2.metric("✨ XP",S.xp)
    c3.metric("✅",len(S.done)); c4.metric("🔥",S.streak)
    st.markdown("---")
    for grade in GRADES:
        ts = get_topics(grade)
        dn = len([t for t in ts if t["id"] in S.done])
        with st.expander(f"{grade} — {dn}/{len(ts)} complete"):
            for t in ts:
                c=t["id"] in S.done; sc=S.scores.get(t["id"])
                st.markdown(f"""
                <div style="display:flex;align-items:center;gap:10px;padding:8px 11px;
                    border-radius:12px;background:rgba(255,255,255,.03);
                    border:1px solid rgba(255,255,255,.07);margin-bottom:5px">
                  <div style="width:36px;height:36px;border-radius:10px;
                      background:linear-gradient(135deg,{t['color']},rgba(0,0,0,.3));
                      display:flex;align-items:center;justify-content:center;font-size:1.1rem">
                    {t['emoji']}</div>
                  <div style="flex:1">
                    <div style="font-weight:700;font-size:.88rem;color:white">{t['title']}</div>
                    <div style="font-size:.7rem;color:#666">{'✅ Done' if c else '🔓 Not started'}{f" · {sc}/5" if sc else ''}</div>
                  </div>
                </div>""", unsafe_allow_html=True)
    st.markdown("---")
    achs = []
    if len(S.done)>=1: achs.append(("🥉","First Topic!","You started your physics journey"))
    if len(S.done)>=3: achs.append(("🥈","Curious Scientist","Completed 3 topics"))
    if len(S.done)>=6: achs.append(("🥇","Physics Champion","Completed 6 topics"))
    if S.stars>=15: achs.append(("⭐","Star Collector","Earned 15+ stars"))
    if S.xp>=500: achs.append(("⚡","XP Guru","Earned 500+ XP"))
    if any(S.scores.get(t,0)==5 for t in S.done): achs.append(("🏆","Perfect Score!","Got 5/5 on a quiz"))
    if achs:
        for icon,title,desc in achs:
            st.markdown(f"""
            <div style="display:flex;align-items:center;gap:12px;padding:10px 14px;
                border-radius:14px;background:rgba(255,255,255,.04);
                border:1px solid rgba(255,255,255,.08);margin-bottom:6px">
              <div style="font-size:2rem">{icon}</div>
              <div><div style="font-weight:800;color:white">{title}</div>
              <div style="font-size:.75rem;color:#666">{desc}</div></div>
            </div>""", unsafe_allow_html=True)
    else: st.info("🎯 Complete topics to unlock achievements!")
    st.markdown("---")
    if st.button("🔄 Reset All Progress", use_container_width=True):
        S.done=set(); S.scores={}; S.stars=0; S.xp=0; S.streak=1
        st.success("Reset!"); st.rerun()


def screen_arcade():
    hdr(); nav()
    st.markdown("### 🎮 Free Play Arcade")
    st.markdown("Play any simulation — no pressure, just explore physics!")

    sim_map = {
        "🚀 Projectile Launcher": {"type":"projectile","title":"Projectile Launcher","desc":"Launch at any angle and speed"},
        "💥 Elastic Collision Lab": {"type":"collision","title":"Collision Lab","desc":"Explore momentum conservation"},
        "🌌 Gravity Well Orbits": {"type":"gravity_well","title":"Gravity Well","desc":"Launch satellites into orbit"},
        "〰️ Sound Wave Lab": {"type":"wave","title":"Wave Lab","desc":"Visualise frequency and amplitude"},
        "🔌 Circuit & Ohm's Law": {"type":"circuit","title":"Circuit Lab","desc":"Build circuits, measure V I R"},
        "🔍 Ray Tracer — Optics": {"type":"optics","title":"Optics Lab","desc":"Lenses and mirrors simulator"},
        "💨 Ideal Gas Law Lab": {"type":"gas_law","title":"Gas Law Lab","desc":"PV=nRT with moving molecules"},
    }
    choice = st.selectbox("Choose a simulation:", list(sim_map.keys()), key="arcade_sel")
    st.markdown(f"*{sim_map[choice]['desc']}*")
    st.markdown("---")
    render_game(sim_map[choice])


# ─── ROUTER ───────────────────────────────────────────────────────────────────
if not S.onboarded:
    screen_onboard()
elif S.screen=="home":
    screen_home()
elif S.screen=="topic":
    screen_topic()
elif S.screen=="progress":
    screen_progress()
elif S.screen=="arcade":
    screen_arcade()
else:
    screen_home()
