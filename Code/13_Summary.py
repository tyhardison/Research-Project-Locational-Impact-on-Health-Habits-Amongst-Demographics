{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red15\green112\blue1;\red255\green255\blue255;\red0\green0\blue0;
\red144\green1\blue18;\red0\green0\blue255;\red86\green65\blue25;\red0\green0\blue109;\red131\green0\blue165;
\red19\green85\blue52;\red31\green99\blue128;}
{\*\expandedcolortbl;;\cssrgb\c0\c50196\c0;\cssrgb\c100000\c100000\c100000;\cssrgb\c0\c0\c0;
\cssrgb\c63922\c8235\c8235;\cssrgb\c0\c0\c100000;\cssrgb\c41569\c32157\c12941;\cssrgb\c0\c6275\c50196;\cssrgb\c59216\c13725\c70588;
\cssrgb\c6667\c40000\c26667;\cssrgb\c14510\c46275\c57647;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # \uc0\u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # CELL 13 \'97 PATHWAY SUMMARY\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 #\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Five-tier Sankey: Demographic \uc0\u8594  Exercise Risk \u8594  Diet Risk \u8594  OW/OB Risk\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Focus groups: Income, Age, Region\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 #\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Exercise score: No Activity (risk) + flipped Meets150/StrengthOnly/Str+Aer\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Diet score:     No Fruit + No Vegetables (both risk)\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Both normalized 0-1, tiers at data-driven 33rd/67th percentiles.\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Band width = sum of harmonic weights (reliability-weighted, not row count).\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # \uc0\u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 sdf = profile[profile[\cf5 \strokec5 'Reliable'\cf0 \strokec4 ]].copy().reset_index(drop=\cf6 \strokec6 True\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # \uc0\u9472 \u9472  Build Exercise and Diet composite scores \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 def\cf0 \strokec4  \cf7 \strokec7 minmax\cf0 \strokec4 (\cf8 \strokec8 series\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf5 \strokec5 """Normalize series to 0-1."""\cf0 \cb1 \strokec4 \
\cb3     mn, mx = series.\cf7 \strokec7 min\cf0 \strokec4 (), series.\cf7 \strokec7 max\cf0 \strokec4 ()\cb1 \
\cb3     \cf9 \strokec9 return\cf0 \strokec4  (series - mn) / (mx - mn + \cf10 \strokec10 1e-9\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # Risk metrics: high = bad \uc0\u8594  keep as-is after normalization\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Protective metrics: high = good \uc0\u8594  flip (1 - normalized) so high = bad\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 sdf[\cf5 \strokec5 'ex_score'\cf0 \strokec4 ]   = (minmax(sdf[\cf5 \strokec5 'No Activity %'\cf0 \strokec4 ]) +\cb1 \
\cb3                      (\cf10 \strokec10 1\cf0 \strokec4  - minmax(sdf[\cf5 \strokec5 'Meets 150 Min %'\cf0 \strokec4 ])) +\cb1 \
\cb3                      (\cf10 \strokec10 1\cf0 \strokec4  - minmax(sdf[\cf5 \strokec5 'Strength Only %'\cf0 \strokec4 ])) +\cb1 \
\cb3                      (\cf10 \strokec10 1\cf0 \strokec4  - minmax(sdf[\cf5 \strokec5 'Strength + Aerobic %'\cf0 \strokec4 ]))) / \cf10 \strokec10 4\cf0 \cb1 \strokec4 \
\
\cb3 sdf[\cf5 \strokec5 'diet_score'\cf0 \strokec4 ] = (minmax(sdf[\cf5 \strokec5 'No Fruit %'\cf0 \strokec4 ]) +\cb1 \
\cb3                      minmax(sdf[\cf5 \strokec5 'No Vegetables %'\cf0 \strokec4 ])) / \cf10 \strokec10 2\cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # Data-driven tier splits \'97 ensures ~equal thirds regardless of distribution shape\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 def\cf0 \strokec4  \cf7 \strokec7 make_tiers\cf0 \strokec4 (\cf8 \strokec8 series\cf0 \strokec4 , \cf8 \strokec8 labels\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     p33, p67 = series.quantile(\cf10 \strokec10 0.33\cf0 \strokec4 ), series.quantile(\cf10 \strokec10 0.67\cf0 \strokec4 )\cb1 \
\cb3     \cf9 \strokec9 return\cf0 \strokec4  pd.cut(series, bins=[-np.inf, p33, p67, np.inf], labels=labels)\cb1 \
\
\cb3 sdf[\cf5 \strokec5 'Exercise_tier'\cf0 \strokec4 ] = make_tiers(sdf[\cf5 \strokec5 'ex_score'\cf0 \strokec4 ],\cb1 \
\cb3     [\cf5 \strokec5 'Exercise: Favorable'\cf0 \strokec4 ,\cf5 \strokec5 'Exercise: Moderate'\cf0 \strokec4 ,\cf5 \strokec5 'Exercise: Unfavorable'\cf0 \strokec4 ])\cb1 \
\cb3 sdf[\cf5 \strokec5 'Diet_tier'\cf0 \strokec4 ]     = make_tiers(sdf[\cf5 \strokec5 'diet_score'\cf0 \strokec4 ],\cb1 \
\cb3     [\cf5 \strokec5 'Diet: Favorable'\cf0 \strokec4 ,\cf5 \strokec5 'Diet: Moderate'\cf0 \strokec4 ,\cf5 \strokec5 'Diet: Unfavorable'\cf0 \strokec4 ])\cb1 \
\cb3 sdf[\cf5 \strokec5 'OW_OB_tier'\cf0 \strokec4 ]    = make_tiers(sdf[\cf5 \strokec5 'Overweight/Obese %'\cf0 \strokec4 ],\cb1 \
\cb3     [\cf5 \strokec5 'Overweight/Obese: Low'\cf0 \strokec4 ,\cf5 \strokec5 'Overweight/Obese: Mid'\cf0 \strokec4 ,\cf5 \strokec5 'Overweight/Obese: High'\cf0 \strokec4 ])\cb1 \
\
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # \uc0\u9472 \u9472  Shared Sankey utilities \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 EX_T  = [\cf5 \strokec5 'Exercise: Favorable'\cf0 \strokec4 ,\cf5 \strokec5 'Exercise: Moderate'\cf0 \strokec4 ,\cf5 \strokec5 'Exercise: Unfavorable'\cf0 \strokec4 ]\cb1 \
\cb3 DT_T  = [\cf5 \strokec5 'Diet: Favorable'\cf0 \strokec4 ,\cf5 \strokec5 'Diet: Moderate'\cf0 \strokec4 ,\cf5 \strokec5 'Diet: Unfavorable'\cf0 \strokec4 ]\cb1 \
\cb3 OB_T  = [\cf5 \strokec5 'Overweight/Obese: Low'\cf0 \strokec4 ,\cf5 \strokec5 'Overweight/Obese: Mid'\cf0 \strokec4 ,\cf5 \strokec5 'Overweight/Obese: High'\cf0 \strokec4 ]\cb1 \
\cb3 INC_V = [\cf5 \strokec5 'Less than $15,000'\cf0 \strokec4 ,\cf5 \strokec5 '$15,000 - $24,999'\cf0 \strokec4 ,\cf5 \strokec5 '$25,000 - $34,999'\cf0 \strokec4 ,\cb1 \
\cb3          \cf5 \strokec5 '$35,000 - $49,999'\cf0 \strokec4 ,\cf5 \strokec5 '$50,000 - $74,999'\cf0 \strokec4 ,\cf5 \strokec5 '$75,000 or greater'\cf0 \strokec4 ]\cb1 \
\cb3 AGE_V = [\cf5 \strokec5 '18 - 24'\cf0 \strokec4 ,\cf5 \strokec5 '25 - 34'\cf0 \strokec4 ,\cf5 \strokec5 '35 - 44'\cf0 \strokec4 ,\cf5 \strokec5 '45 - 54'\cf0 \strokec4 ,\cf5 \strokec5 '55 - 64'\cf0 \strokec4 ,\cf5 \strokec5 '65 or older'\cf0 \strokec4 ]\cb1 \
\cb3 REG_V = [\cf5 \strokec5 'Urban'\cf0 \strokec4 ,\cf5 \strokec5 'Suburban'\cf0 \strokec4 ,\cf5 \strokec5 'Rural'\cf0 \strokec4 ,\cf5 \strokec5 'Mixed'\cf0 \strokec4 ]\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # Node color logic: green=good, yellow=moderate, red=bad, grey=neutral\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 def\cf0 \strokec4  \cf7 \strokec7 node_clr\cf0 \strokec4 (\cf8 \strokec8 label\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf9 \strokec9 if\cf0 \strokec4  \cf7 \strokec7 any\cf0 \strokec4 (x \cf6 \strokec6 in\cf0 \strokec4  label \cf9 \strokec9 for\cf0 \strokec4  x \cf6 \strokec6 in\cf0 \strokec4  [\cf5 \strokec5 'Favorable'\cf0 \strokec4 ,\cf5 \strokec5 'Overweight/Obese: Low'\cf0 \strokec4 ,\cb1 \
\cb3                                   \cf5 \strokec5 '$75,000'\cf0 \strokec4 ,\cf5 \strokec5 '$50,000'\cf0 \strokec4 ,\cf5 \strokec5 'Urban'\cf0 \strokec4 ,\cf5 \strokec5 '18 - 24'\cf0 \strokec4 ,\cf5 \strokec5 '25 - 34'\cf0 \strokec4 ]):\cb1 \
\cb3         \cf9 \strokec9 return\cf0 \strokec4  \cf5 \strokec5 'rgba(26,152,80,0.8)'\cf0 \cb1 \strokec4 \
\cb3     \cf9 \strokec9 if\cf0 \strokec4  \cf7 \strokec7 any\cf0 \strokec4 (x \cf6 \strokec6 in\cf0 \strokec4  label \cf9 \strokec9 for\cf0 \strokec4  x \cf6 \strokec6 in\cf0 \strokec4  [\cf5 \strokec5 'Unfavorable'\cf0 \strokec4 ,\cf5 \strokec5 'Overweight/Obese: High'\cf0 \strokec4 ,\cb1 \
\cb3                                   \cf5 \strokec5 'Less than $15,000'\cf0 \strokec4 ,\cf5 \strokec5 '55 - 64'\cf0 \strokec4 ,\cf5 \strokec5 '65 or older'\cf0 \strokec4 ]):\cb1 \
\cb3         \cf9 \strokec9 return\cf0 \strokec4  \cf5 \strokec5 'rgba(215,48,39,0.8)'\cf0 \cb1 \strokec4 \
\cb3     \cf9 \strokec9 if\cf0 \strokec4  \cf7 \strokec7 any\cf0 \strokec4 (x \cf6 \strokec6 in\cf0 \strokec4  label \cf9 \strokec9 for\cf0 \strokec4  x \cf6 \strokec6 in\cf0 \strokec4  [\cf5 \strokec5 'Moderate'\cf0 \strokec4 ,\cf5 \strokec5 'Mid'\cf0 \strokec4 ]):\cb1 \
\cb3         \cf9 \strokec9 return\cf0 \strokec4  \cf5 \strokec5 'rgba(254,224,139,0.8)'\cf0 \cb1 \strokec4 \
\cb3     \cf9 \strokec9 return\cf0 \strokec4  \cf5 \strokec5 'rgba(150,150,150,0.8)'\cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 def\cf0 \strokec4  \cf7 \strokec7 link_clr\cf0 \strokec4 (\cf8 \strokec8 target\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf9 \strokec9 if\cf0 \strokec4  \cf7 \strokec7 any\cf0 \strokec4 (x \cf6 \strokec6 in\cf0 \strokec4  target \cf9 \strokec9 for\cf0 \strokec4  x \cf6 \strokec6 in\cf0 \strokec4  [\cf5 \strokec5 'Favorable'\cf0 \strokec4 ,\cf5 \strokec5 'Overweight/Obese: Low'\cf0 \strokec4 ]):\cb1 \
\cb3         \cf9 \strokec9 return\cf0 \strokec4  \cf5 \strokec5 'rgba(26,152,80,0.25)'\cf0 \cb1 \strokec4 \
\cb3     \cf9 \strokec9 if\cf0 \strokec4  \cf7 \strokec7 any\cf0 \strokec4 (x \cf6 \strokec6 in\cf0 \strokec4  target \cf9 \strokec9 for\cf0 \strokec4  x \cf6 \strokec6 in\cf0 \strokec4  [\cf5 \strokec5 'Unfavorable'\cf0 \strokec4 ,\cf5 \strokec5 'Overweight/Obese: High'\cf0 \strokec4 ]):\cb1 \
\cb3         \cf9 \strokec9 return\cf0 \strokec4  \cf5 \strokec5 'rgba(215,48,39,0.25)'\cf0 \cb1 \strokec4 \
\cb3     \cf9 \strokec9 if\cf0 \strokec4  \cf7 \strokec7 any\cf0 \strokec4 (x \cf6 \strokec6 in\cf0 \strokec4  target \cf9 \strokec9 for\cf0 \strokec4  x \cf6 \strokec6 in\cf0 \strokec4  [\cf5 \strokec5 'Moderate'\cf0 \strokec4 ,\cf5 \strokec5 'Mid'\cf0 \strokec4 ]):\cb1 \
\cb3         \cf9 \strokec9 return\cf0 \strokec4  \cf5 \strokec5 'rgba(254,224,139,0.25)'\cf0 \cb1 \strokec4 \
\cb3     \cf9 \strokec9 return\cf0 \strokec4  \cf5 \strokec5 'rgba(150,150,150,0.15)'\cf0 \cb1 \strokec4 \
\
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 def\cf0 \strokec4  \cf7 \strokec7 show_sankey\cf0 \strokec4 (\cf8 \strokec8 df\cf0 \strokec4 , \cf8 \strokec8 tier_cols\cf0 \strokec4 , \cf8 \strokec8 tier_vals\cf0 \strokec4 , \cf8 \strokec8 title\cf0 \strokec4 , \cf8 \strokec8 w_col\cf0 \strokec4 =\cf5 \strokec5 'Harmonic Weight'\cf0 \strokec4 , \cf8 \strokec8 min_w\cf0 \strokec4 =\cf10 \strokec10 10\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf5 \strokec5 """\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5     Build and display a Plotly Sankey.\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5     Band width = sum of harmonic weights (reliability-weighted, not row count).\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5     """\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     nodes    = [n \cf9 \strokec9 for\cf0 \strokec4  tier \cf6 \strokec6 in\cf0 \strokec4  tier_vals \cf9 \strokec9 for\cf0 \strokec4  n \cf6 \strokec6 in\cf0 \strokec4  tier]\cb1 \
\cb3     idx      = \{n: i \cf9 \strokec9 for\cf0 \strokec4  i, n \cf6 \strokec6 in\cf0 \strokec4  \cf7 \strokec7 enumerate\cf0 \strokec4 (nodes)\}\cb1 \
\cb3     sources, targets, values, lcolors = [], [], [], []\cb1 \
\
\cb3     \cf9 \strokec9 for\cf0 \strokec4  t \cf6 \strokec6 in\cf0 \strokec4  \cf7 \strokec7 range\cf0 \strokec4 (\cf7 \strokec7 len\cf0 \strokec4 (tier_cols) - \cf10 \strokec10 1\cf0 \strokec4 ):\cb1 \
\cb3         \cf9 \strokec9 for\cf0 \strokec4  (a, b), grp \cf6 \strokec6 in\cf0 \strokec4  df.groupby([tier_cols[t], tier_cols[t+\cf10 \strokec10 1\cf0 \strokec4 ]], observed=\cf6 \strokec6 True\cf0 \strokec4 ):\cb1 \
\cb3             a, b = \cf11 \strokec11 str\cf0 \strokec4 (a), \cf11 \strokec11 str\cf0 \strokec4 (b)\cb1 \
\cb3             \cf9 \strokec9 if\cf0 \strokec4  a \cf6 \strokec6 not\cf0 \strokec4  \cf6 \strokec6 in\cf0 \strokec4  idx \cf6 \strokec6 or\cf0 \strokec4  b \cf6 \strokec6 not\cf0 \strokec4  \cf6 \strokec6 in\cf0 \strokec4  idx:\cb1 \
\cb3                 \cf9 \strokec9 continue\cf0 \cb1 \strokec4 \
\cb3             flow = grp[w_col].\cf7 \strokec7 sum\cf0 \strokec4 ()\cb1 \
\cb3             \cf9 \strokec9 if\cf0 \strokec4  flow < min_w:\cb1 \
\cb3                 \cf9 \strokec9 continue\cf0 \cb1 \strokec4 \
\cb3             sources.append(idx[a])\cb1 \
\cb3             targets.append(idx[b])\cb1 \
\cb3             values.append(flow)\cb1 \
\cb3             lcolors.append(link_clr(b))\cb1 \
\
\cb3     go.Figure(data=[go.Sankey(\cb1 \
\cb3         arrangement=\cf5 \strokec5 'snap'\cf0 \strokec4 ,\cb1 \
\cb3         node=\cf11 \strokec11 dict\cf0 \strokec4 (pad=\cf10 \strokec10 20\cf0 \strokec4 , thickness=\cf10 \strokec10 20\cf0 \strokec4 ,\cb1 \
\cb3                   line=\cf11 \strokec11 dict\cf0 \strokec4 (color=\cf5 \strokec5 'white'\cf0 \strokec4 , width=\cf10 \strokec10 0.5\cf0 \strokec4 ),\cb1 \
\cb3                   label=nodes, color=[node_clr(n) \cf9 \strokec9 for\cf0 \strokec4  n \cf6 \strokec6 in\cf0 \strokec4  nodes]),\cb1 \
\cb3         link=\cf11 \strokec11 dict\cf0 \strokec4 (source=sources, target=targets, value=values, color=lcolors)\cb1 \
\cb3     )]).update_layout(title_text=title, font_size=\cf10 \strokec10 11\cf0 \strokec4 ,\cb1 \
\cb3                       height=\cf10 \strokec10 650\cf0 \strokec4 , width=\cf10 \strokec10 1200\cf0 \strokec4 ).show()\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # \uc0\u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # SANKEY 3 \'97 Region \uc0\u8594  Exercise \u8594  Diet \u8594  Overweight/Obese\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # \uc0\u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 s3 = (sdf[sdf[\cf5 \strokec5 'Region'\cf0 \strokec4 ].isin(REG_V)]\cb1 \
\cb3       .dropna(subset=[\cf5 \strokec5 'Exercise_tier'\cf0 \strokec4 ,\cf5 \strokec5 'Diet_tier'\cf0 \strokec4 ,\cf5 \strokec5 'OW_OB_tier'\cf0 \strokec4 ]))\cb1 \
\
\cb3 show_sankey(s3, [\cf5 \strokec5 'Region'\cf0 \strokec4 ,\cf5 \strokec5 'Exercise_tier'\cf0 \strokec4 ,\cf5 \strokec5 'Diet_tier'\cf0 \strokec4 ,\cf5 \strokec5 'OW_OB_tier'\cf0 \strokec4 ],\cb1 \
\cb3             [REG_V, EX_T, DT_T, OB_T],\cb1 \
\cb3             \cf5 \strokec5 'Sankey \'97 Region \uc0\u8594  Exercise Risk \u8594  Diet Risk \u8594  Overweight/Obese<br>'\cf0 \cb1 \strokec4 \
\cb3             \cf5 \strokec5 '<sup>Band width = harmonic weight sum. Ecological only.</sup>'\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # \uc0\u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # SANKEY 4 \'97 Region \uc0\u8594  Income \u8594  Exercise \u8594  Diet \u8594  Overweight/Obese\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # The most complete pathway \'97 geography \uc0\u8594  economics \u8594  behavior \u8594  outcome\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # \uc0\u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 s4 = (sdf[(sdf[\cf5 \strokec5 'Group'\cf0 \strokec4 ] == \cf5 \strokec5 'Income'\cf0 \strokec4 ) &\cb1 \
\cb3           (sdf[\cf5 \strokec5 'Group Value'\cf0 \strokec4 ].isin(INC_V)) &\cb1 \
\cb3           (sdf[\cf5 \strokec5 'Region'\cf0 \strokec4 ].isin(REG_V))]\cb1 \
\cb3       .dropna(subset=[\cf5 \strokec5 'Exercise_tier'\cf0 \strokec4 ,\cf5 \strokec5 'Diet_tier'\cf0 \strokec4 ,\cf5 \strokec5 'OW_OB_tier'\cf0 \strokec4 ])\cb1 \
\cb3       .rename(columns=\{\cf5 \strokec5 'Group Value'\cf0 \strokec4 :\cf5 \strokec5 'Income'\cf0 \strokec4 \}))\cb1 \
\
\cb3 show_sankey(s4, [\cf5 \strokec5 'Region'\cf0 \strokec4 ,\cf5 \strokec5 'Income'\cf0 \strokec4 ,\cf5 \strokec5 'Exercise_tier'\cf0 \strokec4 ,\cf5 \strokec5 'Diet_tier'\cf0 \strokec4 ,\cf5 \strokec5 'OW_OB_tier'\cf0 \strokec4 ],\cb1 \
\cb3             [REG_V, INC_V, EX_T, DT_T, OB_T],\cb1 \
\cb3             \cf5 \strokec5 'Sankey \'97 Region \uc0\u8594  Income \u8594  Exercise \u8594  Diet \u8594  Overweight/Obese<br>'\cf0 \cb1 \strokec4 \
\cb3             \cf5 \strokec5 '<sup>Band width = harmonic weight sum. Ecological only.</sup>'\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # \uc0\u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # SANKEY 5 \'97 Income pathway faceted by Urbanicity\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Shows whether the income \uc0\u8594  behavior \u8594  weight pathway differs geographically\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # \uc0\u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf9 \cb3 \strokec9 for\cf0 \strokec4  urb \cf6 \strokec6 in\cf0 \strokec4  REG_V:\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     s5 = (sdf[(sdf[\cf5 \strokec5 'Group'\cf0 \strokec4 ] == \cf5 \strokec5 'Income'\cf0 \strokec4 ) &\cb1 \
\cb3               (sdf[\cf5 \strokec5 'Group Value'\cf0 \strokec4 ].isin(INC_V)) &\cb1 \
\cb3               (sdf[\cf5 \strokec5 'Region'\cf0 \strokec4 ] == urb)]\cb1 \
\cb3           .dropna(subset=[\cf5 \strokec5 'Exercise_tier'\cf0 \strokec4 ,\cf5 \strokec5 'Diet_tier'\cf0 \strokec4 ,\cf5 \strokec5 'OW_OB_tier'\cf0 \strokec4 ])\cb1 \
\cb3           .rename(columns=\{\cf5 \strokec5 'Group Value'\cf0 \strokec4 :\cf5 \strokec5 'Income'\cf0 \strokec4 \}))\cb1 \
\cb3     \cf9 \strokec9 if\cf0 \strokec4  s5.empty:\cb1 \
\cb3         \cf9 \strokec9 continue\cf0 \cb1 \strokec4 \
\cb3     show_sankey(s5, [\cf5 \strokec5 'Income'\cf0 \strokec4 ,\cf5 \strokec5 'Exercise_tier'\cf0 \strokec4 ,\cf5 \strokec5 'Diet_tier'\cf0 \strokec4 ,\cf5 \strokec5 'OW_OB_tier'\cf0 \strokec4 ],\cb1 \
\cb3                 [INC_V, EX_T, DT_T, OB_T],\cb1 \
\cb3                 \cf6 \strokec6 f\cf5 \strokec5 'Sankey \'97 Income \uc0\u8594  Exercise \u8594  Diet \u8594  OW/OB  [\cf0 \strokec4 \{urb\}\cf5 \strokec5 ]<br>'\cf0 \cb1 \strokec4 \
\cb3                 \cf5 \strokec5 '<sup>Band width = harmonic weight sum. Ecological only.</sup>'\cf0 \strokec4 )\cb1 \
\
\
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 print\cf0 \strokec4 (\cf5 \strokec5 "\\nCell 14 complete."\cf0 \strokec4 )\cb1 \
}