{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red15\green112\blue1;\red255\green255\blue255;\red0\green0\blue0;
\red144\green1\blue18;\red0\green0\blue255;\red86\green65\blue25;\red0\green0\blue109;\red131\green0\blue165;
\red31\green99\blue128;\red19\green85\blue52;}
{\*\expandedcolortbl;;\cssrgb\c0\c50196\c0;\cssrgb\c100000\c100000\c100000;\cssrgb\c0\c0\c0;
\cssrgb\c63922\c8235\c8235;\cssrgb\c0\c0\c100000;\cssrgb\c41569\c32157\c12941;\cssrgb\c0\c6275\c50196;\cssrgb\c59216\c13725\c70588;
\cssrgb\c14510\c46275\c57647;\cssrgb\c6667\c40000\c26667;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # \uc0\u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # CELL 7 \'97 PROFILE TABLE\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 #\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # One row per [Year, State, Region, Group, Group Value] with all 7 metrics.\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 #\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Overweight/Obese combination:\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 #   Obese and Overweight are mutually exclusive BMI categories from the same\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 #   survey sample. Combined % = Obese% + Overweight% (mathematically exact sum).\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 #   Confirmed: sums never exceed 100% (mean ~66%), so ~34% of each sample is\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 #   normal/underweight \'97 not captured in this dataset.\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 #   Combined sample size = harmonic mean of the two effective sample sizes\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 #   (conservative \'97 avoids double counting the same respondents).\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 #\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # All 7 metrics joined via inner join on shared key columns.\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Harmonic Weight = minimum pairwise harmonic mean across all 7 sample sizes.\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Reliable flag   = True when every metric's sample size >= 100.\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # \uc0\u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 KEY = [\cf5 \strokec5 'Year'\cf0 \strokec4 ,\cf5 \strokec5 'State'\cf0 \strokec4 ,\cf5 \strokec5 'Region'\cf0 \strokec4 ,\cf5 \strokec5 'Group'\cf0 \strokec4 ,\cf5 \strokec5 'Group Value'\cf0 \strokec4 ]\cb1 \
\
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 def\cf0 \strokec4  \cf7 \strokec7 build_metric\cf0 \strokec4 (\cf8 \strokec8 df\cf0 \strokec4 , \cf8 \strokec8 filter_col\cf0 \strokec4 , \cf8 \strokec8 filter_val\cf0 \strokec4 , \cf8 \strokec8 name\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf5 \strokec5 """Aggregate one metric to KEY level with weighted mean % and total n."""\cf0 \cb1 \strokec4 \
\cb3     sub     = df[df[filter_col] == filter_val].copy()\cb1 \
\cb3     records = []\cb1 \
\cb3     \cf9 \strokec9 for\cf0 \strokec4  keys, grp \cf6 \strokec6 in\cf0 \strokec4  sub.groupby(KEY):\cb1 \
\cb3         kt = keys \cf9 \strokec9 if\cf0 \strokec4  \cf7 \strokec7 isinstance\cf0 \strokec4 (keys, \cf10 \strokec10 tuple\cf0 \strokec4 ) \cf9 \strokec9 else\cf0 \strokec4  (keys,)\cb1 \
\cb3         records.append(\cf10 \strokec10 dict\cf0 \strokec4 (\cf7 \strokec7 zip\cf0 \strokec4 (KEY, kt)) | \{\cb1 \
\cb3             name        : np.average(grp[\cf5 \strokec5 'Percentage'\cf0 \strokec4 ], weights=grp[\cf5 \strokec5 'Sample Size'\cf0 \strokec4 ]),\cb1 \
\cb3             \cf6 \strokec6 f\cf5 \strokec5 '\cf0 \strokec4 \{name\}\cf5 \strokec5 _N'\cf0 \strokec4  : grp[\cf5 \strokec5 'Sample Size'\cf0 \strokec4 ].\cf7 \strokec7 sum\cf0 \strokec4 (),\cb1 \
\cb3         \})\cb1 \
\cb3     \cf9 \strokec9 return\cf0 \strokec4  pd.DataFrame(records)\cb1 \
\
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 def\cf0 \strokec4  \cf7 \strokec7 build_ow_ob\cf0 \strokec4 (\cf8 \strokec8 df\cf0 \strokec4 , \cf8 \strokec8 name\cf0 \strokec4 =\cf5 \strokec5 'Overweight/Obese %'\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf5 \strokec5 """\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5     Combine Obese% + Overweight% via sum (mutually exclusive categories).\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5     Sample size = harmonic mean of the two effective sample sizes.\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5     """\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     records = []\cb1 \
\cb3     \cf9 \strokec9 for\cf0 \strokec4  keys, grp \cf6 \strokec6 in\cf0 \strokec4  df[df[\cf5 \strokec5 'Weight Status'\cf0 \strokec4 ].isin([\cf5 \strokec5 'Obese'\cf0 \strokec4 ,\cf5 \strokec5 'Overweight'\cf0 \strokec4 ])].groupby(KEY):\cb1 \
\cb3         kt        = keys \cf9 \strokec9 if\cf0 \strokec4  \cf7 \strokec7 isinstance\cf0 \strokec4 (keys, \cf10 \strokec10 tuple\cf0 \strokec4 ) \cf9 \strokec9 else\cf0 \strokec4  (keys,)\cb1 \
\cb3         ob_rows   = grp[grp[\cf5 \strokec5 'Weight Status'\cf0 \strokec4 ] == \cf5 \strokec5 'Obese'\cf0 \strokec4 ]\cb1 \
\cb3         ow_rows   = grp[grp[\cf5 \strokec5 'Weight Status'\cf0 \strokec4 ] == \cf5 \strokec5 'Overweight'\cf0 \strokec4 ]\cb1 \
\cb3         \cf9 \strokec9 if\cf0 \strokec4  ob_rows.empty \cf6 \strokec6 or\cf0 \strokec4  ow_rows.empty:\cb1 \
\cb3             \cf9 \strokec9 continue\cf0 \cb1 \strokec4 \
\cb3         ob_pct = np.average(ob_rows[\cf5 \strokec5 'Percentage'\cf0 \strokec4 ], weights=ob_rows[\cf5 \strokec5 'Sample Size'\cf0 \strokec4 ])\cb1 \
\cb3         ob_n   = ob_rows[\cf5 \strokec5 'Sample Size'\cf0 \strokec4 ].\cf7 \strokec7 sum\cf0 \strokec4 ()\cb1 \
\cb3         ow_pct = np.average(ow_rows[\cf5 \strokec5 'Percentage'\cf0 \strokec4 ], weights=ow_rows[\cf5 \strokec5 'Sample Size'\cf0 \strokec4 ])\cb1 \
\cb3         ow_n   = ow_rows[\cf5 \strokec5 'Sample Size'\cf0 \strokec4 ].\cf7 \strokec7 sum\cf0 \strokec4 ()\cb1 \
\cb3         records.append(\cf10 \strokec10 dict\cf0 \strokec4 (\cf7 \strokec7 zip\cf0 \strokec4 (KEY, kt)) | \{\cb1 \
\cb3             name        : ob_pct + ow_pct,       \cf2 \strokec2 # exact sum for mutually exclusive categories\cf0 \cb1 \strokec4 \
\cb3             \cf6 \strokec6 f\cf5 \strokec5 '\cf0 \strokec4 \{name\}\cf5 \strokec5 _N'\cf0 \strokec4  : harmonic(ob_n, ow_n),  \cf2 \strokec2 # conservative combined sample size\cf0 \cb1 \strokec4 \
\cb3         \})\cb1 \
\cb3     \cf9 \strokec9 return\cf0 \strokec4  pd.DataFrame(records)\cb1 \
\
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # Build each metric profile\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 ow_ob    = build_ow_ob(HealthStatus)\cb1 \
\cb3 no_act   = build_metric(HealthHabits, \cf5 \strokec5 'Activity Profile'\cf0 \strokec4 , \cf5 \strokec5 'No Activity'\cf0 \strokec4 ,        \cf5 \strokec5 'No Activity %'\cf0 \strokec4 )\cb1 \
\cb3 m150     = build_metric(HealthHabits, \cf5 \strokec5 'Activity Profile'\cf0 \strokec4 , \cf5 \strokec5 '150 Min Aerobic'\cf0 \strokec4 ,    \cf5 \strokec5 'Meets 150 Min %'\cf0 \strokec4 )\cb1 \
\cb3 str_only = build_metric(HealthHabits, \cf5 \strokec5 'Activity Profile'\cf0 \strokec4 , \cf5 \strokec5 'Strength Only'\cf0 \strokec4 ,      \cf5 \strokec5 'Strength Only %'\cf0 \strokec4 )\cb1 \
\cb3 str_aer  = build_metric(HealthHabits, \cf5 \strokec5 'Activity Profile'\cf0 \strokec4 , \cf5 \strokec5 '150 Min + Strength'\cf0 \strokec4 , \cf5 \strokec5 'Strength + Aerobic %'\cf0 \strokec4 )\cb1 \
\cb3 no_fruit = build_metric(HealthDiet,   \cf5 \strokec5 'No Fruits and Vegetables'\cf0 \strokec4 , \cf5 \strokec5 'No Fruit'\cf0 \strokec4 ,      \cf5 \strokec5 'No Fruit %'\cf0 \strokec4 )\cb1 \
\cb3 no_veg   = build_metric(HealthDiet,   \cf5 \strokec5 'No Fruits and Vegetables'\cf0 \strokec4 , \cf5 \strokec5 'No Vegetables'\cf0 \strokec4 , \cf5 \strokec5 'No Vegetables %'\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # Inner join all metrics \'97 only keep rows with complete data across all 7\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 profile = ow_ob\cb1 \
\pard\pardeftab720\partightenfactor0
\cf9 \cb3 \strokec9 for\cf0 \strokec4  df_m \cf6 \strokec6 in\cf0 \strokec4  [no_act, m150, str_only, str_aer, no_fruit, no_veg]:\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     profile = profile.merge(df_m, on=KEY, how=\cf5 \strokec5 'inner'\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # Sample size columns \'97 _N suffix prevents substring matching issues\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 N_COLS = [\cf5 \strokec5 'Overweight/Obese %_N'\cf0 \strokec4 ,\cf5 \strokec5 'No Activity %_N'\cf0 \strokec4 ,\cf5 \strokec5 'Meets 150 Min %_N'\cf0 \strokec4 ,\cb1 \
\cb3           \cf5 \strokec5 'Strength Only %_N'\cf0 \strokec4 ,\cf5 \strokec5 'Strength + Aerobic %_N'\cf0 \strokec4 ,\cf5 \strokec5 'No Fruit %_N'\cf0 \strokec4 ,\cf5 \strokec5 'No Vegetables %_N'\cf0 \strokec4 ]\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # Conservative harmonic weight \'97 minimum pairwise harmonic mean across all 7 metrics\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 profile[\cf5 \strokec5 'Harmonic Weight'\cf0 \strokec4 ] = profile.apply(\cb1 \
\cb3     \cf6 \strokec6 lambda\cf0 \strokec4  r: \cf7 \strokec7 min\cf0 \strokec4 (harmonic(r[a], r[b])\cb1 \
\cb3                   \cf9 \strokec9 for\cf0 \strokec4  i, a \cf6 \strokec6 in\cf0 \strokec4  \cf7 \strokec7 enumerate\cf0 \strokec4 (N_COLS)\cb1 \
\cb3                   \cf9 \strokec9 for\cf0 \strokec4  b \cf6 \strokec6 in\cf0 \strokec4  N_COLS[i+\cf11 \strokec11 1\cf0 \strokec4 :]), axis=\cf11 \strokec11 1\cf0 \cb1 \strokec4 \
\cb3 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # Reliable = all metric sample sizes >= 100\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 profile[\cf5 \strokec5 'Reliable'\cf0 \strokec4 ] = profile[N_COLS].\cf7 \strokec7 min\cf0 \strokec4 (axis=\cf11 \strokec11 1\cf0 \strokec4 ) >= \cf11 \strokec11 100\cf0 \cb1 \strokec4 \
\
\cb3 METRICS = [\cf5 \strokec5 'Overweight/Obese %'\cf0 \strokec4 ,\cf5 \strokec5 'No Activity %'\cf0 \strokec4 ,\cf5 \strokec5 'Meets 150 Min %'\cf0 \strokec4 ,\cb1 \
\cb3            \cf5 \strokec5 'Strength Only %'\cf0 \strokec4 ,\cf5 \strokec5 'Strength + Aerobic %'\cf0 \strokec4 ,\cf5 \strokec5 'No Fruit %'\cf0 \strokec4 ,\cf5 \strokec5 'No Vegetables %'\cf0 \strokec4 ]\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 print\cf0 \strokec4 (\cf6 \strokec6 f\cf5 \strokec5 "Profile table   : \cf0 \strokec4 \{profile.shape[\cf11 \strokec11 0\cf0 \strokec4 ]\cf11 \strokec11 :,\cf0 \strokec4 \}\cf5 \strokec5  rows \'d7 \cf0 \strokec4 \{profile.shape[\cf11 \strokec11 1\cf0 \strokec4 ]\}\cf5 \strokec5  cols"\cf0 \strokec4 )\cb1 \
\cf7 \cb3 \strokec7 print\cf0 \strokec4 (\cf6 \strokec6 f\cf5 \strokec5 "Reliable rows   : \cf0 \strokec4 \{profile[\cf5 \strokec5 'Reliable'\cf0 \strokec4 ].\cf7 \strokec7 sum\cf0 \strokec4 ()\cf11 \strokec11 :,\cf0 \strokec4 \}\cf5 \strokec5  (\cf0 \strokec4 \{profile[\cf5 \strokec5 'Reliable'\cf0 \strokec4 ].mean()*\cf11 \strokec11 100:.1f\cf0 \strokec4 \}\cf5 \strokec5 %)"\cf0 \strokec4 )\cb1 \
\cf7 \cb3 \strokec7 print\cf0 \strokec4 (\cf6 \strokec6 f\cf5 \strokec5 "\\nOverweight/Obese % (should average ~66%):"\cf0 \strokec4 )\cb1 \
\cf7 \cb3 \strokec7 print\cf0 \strokec4 (profile[\cf5 \strokec5 'Overweight/Obese %'\cf0 \strokec4 ].describe().\cf7 \strokec7 round\cf0 \strokec4 (\cf11 \strokec11 1\cf0 \strokec4 ).to_string())\cb1 \
}