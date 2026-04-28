{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red15\green112\blue1;\red255\green255\blue255;\red0\green0\blue0;
\red131\green0\blue165;\red0\green0\blue255;\red144\green1\blue18;\red19\green85\blue52;\red86\green65\blue25;
\red0\green0\blue109;\red31\green99\blue128;}
{\*\expandedcolortbl;;\cssrgb\c0\c50196\c0;\cssrgb\c100000\c100000\c100000;\cssrgb\c0\c0\c0;
\cssrgb\c59216\c13725\c70588;\cssrgb\c0\c0\c100000;\cssrgb\c63922\c8235\c8235;\cssrgb\c6667\c40000\c26667;\cssrgb\c41569\c32157\c12941;
\cssrgb\c0\c6275\c50196;\cssrgb\c14510\c46275\c57647;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # \uc0\u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # CELL 9 \'97 STRATIFIED ASSOCIATION ANALYSIS\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 #\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Focus groups: Income, Age, Region\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Tests whether the demographic-weight relationship varies by urbanicity.\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # All associations are ecological \'97 conditional on group context.\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # \uc0\u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \cf0 \cb1 \strokec4 \
\
\cf2 \cb3 \strokec2 # Urbanicity levels for stratification (exclude national aggregates)\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 URB = [u \cf5 \strokec5 for\cf0 \strokec4  u \cf6 \strokec6 in\cf0 \strokec4  profile[\cf7 \strokec7 'Region'\cf0 \strokec4 ].unique() \cf5 \strokec5 if\cf0 \strokec4  u \cf6 \strokec6 not\cf0 \strokec4  \cf6 \strokec6 in\cf0 \strokec4  [\cf7 \strokec7 'National'\cf0 \strokec4 ,\cf7 \strokec7 'Territory'\cf0 \strokec4 ]]\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # Income ordered low \uc0\u8594  high for correlation calculation\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 INCOME_RANK = \{\cb1 \
\cb3     \cf7 \strokec7 'Less than $15,000'\cf0 \strokec4 :\cf8 \strokec8 0\cf0 \strokec4 , \cf7 \strokec7 '$15,000 - $24,999'\cf0 \strokec4 :\cf8 \strokec8 1\cf0 \strokec4 , \cf7 \strokec7 '$25,000 - $34,999'\cf0 \strokec4 :\cf8 \strokec8 2\cf0 \strokec4 ,\cb1 \
\cb3     \cf7 \strokec7 '$35,000 - $49,999'\cf0 \strokec4 :\cf8 \strokec8 3\cf0 \strokec4 , \cf7 \strokec7 '$50,000 - $74,999'\cf0 \strokec4 :\cf8 \strokec8 4\cf0 \strokec4 , \cf7 \strokec7 '$75,000 or greater'\cf0 \strokec4 :\cf8 \strokec8 5\cf0 \strokec4 ,\cb1 \
\cb3 \}\cb1 \
\
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 def\cf0 \strokec4  \cf9 \strokec9 stratified_bars\cf0 \strokec4 (\cf10 \strokec10 df\cf0 \strokec4 , \cf10 \strokec10 group_col\cf0 \strokec4 , \cf10 \strokec10 metric\cf0 \strokec4 , \cf10 \strokec10 urb_levels\cf0 \strokec4 , \cf10 \strokec10 title\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf7 \strokec7 """Horizontal bar charts of metric by group value, one panel per urbanicity."""\cf0 \cb1 \strokec4 \
\cb3     fig, axes = plt.subplots(\cf8 \strokec8 1\cf0 \strokec4 , \cf9 \strokec9 len\cf0 \strokec4 (urb_levels),\cb1 \
\cb3                              figsize=(\cf8 \strokec8 5\cf0 \strokec4  * \cf9 \strokec9 len\cf0 \strokec4 (urb_levels), \cf8 \strokec8 5\cf0 \strokec4 ), sharey=\cf6 \strokec6 True\cf0 \strokec4 )\cb1 \
\cb3     \cf5 \strokec5 for\cf0 \strokec4  ax, urb \cf6 \strokec6 in\cf0 \strokec4  \cf9 \strokec9 zip\cf0 \strokec4 (axes, urb_levels):\cb1 \
\cb3         sub = df[df[\cf7 \strokec7 'Region'\cf0 \strokec4 ] == urb]\cb1 \
\cb3         \cf5 \strokec5 if\cf0 \strokec4  sub.empty:\cb1 \
\cb3             ax.set_visible(\cf6 \strokec6 False\cf0 \strokec4 )\cb1 \
\cb3             \cf5 \strokec5 continue\cf0 \cb1 \strokec4 \
\cb3         agg = w_agg(sub, [\cf7 \strokec7 'Group Value'\cf0 \strokec4 ], value_col=metric,\cb1 \
\cb3                     weight_col=\cf7 \strokec7 'Harmonic Weight'\cf0 \strokec4 ).sort_values(\cf7 \strokec7 'Weighted %'\cf0 \strokec4 , ascending=\cf6 \strokec6 True\cf0 \strokec4 )\cb1 \
\cb3         ax.barh(agg[\cf7 \strokec7 'Group Value'\cf0 \strokec4 ], agg[\cf7 \strokec7 'Weighted %'\cf0 \strokec4 ],\cb1 \
\cb3                 color=sns.color_palette(PALETTE, \cf9 \strokec9 len\cf0 \strokec4 (agg)))\cb1 \
\cb3         ax.xaxis.set_major_formatter(mtick.PercentFormatter())\cb1 \
\cb3         ax.\cf11 \strokec11 set\cf0 \strokec4 (title=urb, xlabel=metric)\cb1 \
\cb3     fig.suptitle(\cf6 \strokec6 f\cf7 \strokec7 '\cf0 \strokec4 \{title\}\cf7 \strokec7 \\nEcological association only.'\cf0 \strokec4 ,\cb1 \
\cb3                  fontsize=\cf8 \strokec8 10\cf0 \strokec4 , style=\cf7 \strokec7 'italic'\cf0 \strokec4 )\cb1 \
\cb3     plt.tight_layout()\cb1 \
\cb3     plt.show()\cb1 \
\
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # \uc0\u9472 \u9472  Income \'d7 Overweight/Obese \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 income_df = profile[profile[\cf7 \strokec7 'Group'\cf0 \strokec4 ] == \cf7 \strokec7 'Income'\cf0 \strokec4 ].reset_index(drop=\cf6 \strokec6 True\cf0 \strokec4 )\cb1 \
\cb3 stratified_bars(income_df, \cf7 \strokec7 'Group Value'\cf0 \strokec4 , \cf7 \strokec7 'Overweight/Obese %'\cf0 \strokec4 , URB,\cb1 \
\cb3                 \cf7 \strokec7 'Overweight/Obese Rate by Income \'97 Stratified by Urbanicity'\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf9 \cb3 \strokec9 print\cf0 \strokec4 (\cf7 \strokec7 "\\nWeighted r (Income rank vs Overweight/Obese %) by Urbanicity:"\cf0 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 for\cf0 \strokec4  urb \cf6 \strokec6 in\cf0 \strokec4  URB:\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     sub = (income_df[(income_df[\cf7 \strokec7 'Region'\cf0 \strokec4 ] == urb) &\cb1 \
\cb3                      (income_df[\cf7 \strokec7 'Group Value'\cf0 \strokec4 ].isin(INCOME_RANK))]\cb1 \
\cb3            .dropna(subset=[\cf7 \strokec7 'Overweight/Obese %'\cf0 \strokec4 ,\cf7 \strokec7 'Harmonic Weight'\cf0 \strokec4 ])\cb1 \
\cb3            .reset_index(drop=\cf6 \strokec6 True\cf0 \strokec4 ))\cb1 \
\cb3     \cf5 \strokec5 if\cf0 \strokec4  \cf9 \strokec9 len\cf0 \strokec4 (sub) < \cf8 \strokec8 5\cf0 \strokec4 :\cb1 \
\cb3         \cf5 \strokec5 continue\cf0 \cb1 \strokec4 \
\cb3     r = w_pearson(sub[\cf7 \strokec7 'Group Value'\cf0 \strokec4 ].\cf9 \strokec9 map\cf0 \strokec4 (INCOME_RANK).to_numpy(dtype=\cf11 \strokec11 float\cf0 \strokec4 ),\cb1 \
\cb3                   sub[\cf7 \strokec7 'Overweight/Obese %'\cf0 \strokec4 ].to_numpy(dtype=\cf11 \strokec11 float\cf0 \strokec4 ),\cb1 \
\cb3                   sub[\cf7 \strokec7 'Harmonic Weight'\cf0 \strokec4 ].to_numpy(dtype=\cf11 \strokec11 float\cf0 \strokec4 ))\cb1 \
\cb3     \cf9 \strokec9 print\cf0 \strokec4 (\cf6 \strokec6 f\cf7 \strokec7 "  \cf0 \strokec4 \{urb\cf8 \strokec8 :12s\cf0 \strokec4 \}\cf7 \strokec7  : r = \cf0 \strokec4 \{r\cf8 \strokec8 :.3f\cf0 \strokec4 \}\cf7 \strokec7 "\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # \uc0\u9472 \u9472  Age \'d7 Overweight/Obese \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 age_df = profile[profile[\cf7 \strokec7 'Group'\cf0 \strokec4 ] == \cf7 \strokec7 'Age(years)'\cf0 \strokec4 ].reset_index(drop=\cf6 \strokec6 True\cf0 \strokec4 )\cb1 \
\cb3 stratified_bars(age_df, \cf7 \strokec7 'Group Value'\cf0 \strokec4 , \cf7 \strokec7 'Overweight/Obese %'\cf0 \strokec4 , URB,\cb1 \
\cb3                 \cf7 \strokec7 'Overweight/Obese Rate by Age \'97 Stratified by Urbanicity'\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # \uc0\u9472 \u9472  Region summary \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 region_agg = (w_agg(profile[profile[\cf7 \strokec7 'Region'\cf0 \strokec4 ].isin(URB)],\cb1 \
\cb3                     [\cf7 \strokec7 'Region'\cf0 \strokec4 ], value_col=\cf7 \strokec7 'Overweight/Obese %'\cf0 \strokec4 ,\cb1 \
\cb3                     weight_col=\cf7 \strokec7 'Harmonic Weight'\cf0 \strokec4 )\cb1 \
\cb3               .sort_values(\cf7 \strokec7 'Weighted %'\cf0 \strokec4 , ascending=\cf6 \strokec6 True\cf0 \strokec4 ))\cb1 \
\
\cb3 fig, ax = plt.subplots(figsize=(\cf8 \strokec8 8\cf0 \strokec4 , \cf8 \strokec8 4\cf0 \strokec4 ))\cb1 \
\cb3 ax.barh(region_agg[\cf7 \strokec7 'Region'\cf0 \strokec4 ], region_agg[\cf7 \strokec7 'Weighted %'\cf0 \strokec4 ],\cb1 \
\cb3         color=sns.color_palette(PALETTE, \cf9 \strokec9 len\cf0 \strokec4 (region_agg)))\cb1 \
\cb3 ax.xaxis.set_major_formatter(mtick.PercentFormatter())\cb1 \
\cb3 ax.\cf11 \strokec11 set\cf0 \strokec4 (title=\cf7 \strokec7 'Overall Overweight/Obese Rate by Urbanicity\\nEcological only.'\cf0 \strokec4 ,\cb1 \
\cb3        xlabel=\cf7 \strokec7 'Overweight/Obese %'\cf0 \strokec4 )\cb1 \
\cb3 plt.tight_layout()\cb1 \
\cb3 plt.show()\cb1 \
}