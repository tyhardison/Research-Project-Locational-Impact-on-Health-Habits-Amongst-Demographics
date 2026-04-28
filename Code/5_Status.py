{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red15\green112\blue1;\red255\green255\blue255;\red0\green0\blue0;
\red86\green65\blue25;\red144\green1\blue18;\red131\green0\blue165;\red0\green0\blue255;\red19\green85\blue52;
\red31\green99\blue128;}
{\*\expandedcolortbl;;\cssrgb\c0\c50196\c0;\cssrgb\c100000\c100000\c100000;\cssrgb\c0\c0\c0;
\cssrgb\c41569\c32157\c12941;\cssrgb\c63922\c8235\c8235;\cssrgb\c59216\c13725\c70588;\cssrgb\c0\c0\c100000;\cssrgb\c6667\c40000\c26667;
\cssrgb\c14510\c46275\c57647;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # \uc0\u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # CELL 5 \'97 HEALTHSTATUS EDA\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Weight status patterns across groups, states, and time\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # \uc0\u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 print\cf0 \strokec4 (\cf6 \strokec6 "HEALTHSTATUS EDA"\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # \uc0\u9472 \u9472  Obese vs Overweight side by side \'97 one chart per demographic group \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Kept separate before combining downstream so each classification is visible\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 for\cf0 \strokec4  grp \cf8 \strokec8 in\cf0 \strokec4  HealthStatus[\cf6 \strokec6 'Group'\cf0 \strokec4 ].unique():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     sub   = HealthStatus[HealthStatus[\cf6 \strokec6 'Group'\cf0 \strokec4 ] == grp]\cb1 \
\cb3     agg   = w_agg(sub, [\cf6 \strokec6 'Group Value'\cf0 \strokec4 , \cf6 \strokec6 'Weight Status'\cf0 \strokec4 ])\cb1 \
\cb3     pivot = agg.pivot(index=\cf6 \strokec6 'Group Value'\cf0 \strokec4 , columns=\cf6 \strokec6 'Weight Status'\cf0 \strokec4 , values=\cf6 \strokec6 'Weighted %'\cf0 \strokec4 )\cb1 \
\cb3     fig, ax = plt.subplots(figsize=(\cf9 \strokec9 10\cf0 \strokec4 , \cf9 \strokec9 5\cf0 \strokec4 ))\cb1 \
\cb3     pivot.plot(kind=\cf6 \strokec6 'barh'\cf0 \strokec4 , ax=ax, colormap=PALETTE)\cb1 \
\cb3     ax.xaxis.set_major_formatter(mtick.PercentFormatter())\cb1 \
\cb3     ax.\cf10 \strokec10 set\cf0 \strokec4 (title=\cf8 \strokec8 f\cf6 \strokec6 'Obese vs Overweight \'97 by \cf0 \strokec4 \{grp\}\cf6 \strokec6 '\cf0 \strokec4 , xlabel=\cf6 \strokec6 'Weighted %'\cf0 \strokec4 , ylabel=grp)\cb1 \
\cb3     plt.tight_layout()\cb1 \
\cb3     plt.show()\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # \uc0\u9472 \u9472  State-level combined rate colored by urbanicity \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Obese + Overweight averaged here \'97 exact sum combination is in Cell 7\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 state_rate = (w_agg(\cb1 \
\cb3     HealthStatus[HealthStatus[\cf6 \strokec6 'Weight Status'\cf0 \strokec4 ].isin([\cf6 \strokec6 'Obese'\cf0 \strokec4 ,\cf6 \strokec6 'Overweight'\cf0 \strokec4 ])],\cb1 \
\cb3     [\cf6 \strokec6 'State'\cf0 \strokec4 ,\cf6 \strokec6 'Region'\cf0 \strokec4 ])\cb1 \
\cb3     .sort_values(\cf6 \strokec6 'Weighted %'\cf0 \strokec4 , ascending=\cf8 \strokec8 True\cf0 \strokec4 ))\cb1 \
\
\cb3 region_colors = \cf10 \strokec10 dict\cf0 \strokec4 (\cf5 \strokec5 zip\cf0 \strokec4 (state_rate[\cf6 \strokec6 'Region'\cf0 \strokec4 ].unique(),\cb1 \
\cb3                          sns.color_palette(PALETTE, state_rate[\cf6 \strokec6 'Region'\cf0 \strokec4 ].nunique())))\cb1 \
\
\cb3 fig, ax = plt.subplots(figsize=(\cf9 \strokec9 12\cf0 \strokec4 , \cf9 \strokec9 14\cf0 \strokec4 ))\cb1 \
\cb3 ax.barh(state_rate[\cf6 \strokec6 'State'\cf0 \strokec4 ], state_rate[\cf6 \strokec6 'Weighted %'\cf0 \strokec4 ],\cb1 \
\cb3         color=state_rate[\cf6 \strokec6 'Region'\cf0 \strokec4 ].\cf5 \strokec5 map\cf0 \strokec4 (region_colors))\cb1 \
\cb3 ax.xaxis.set_major_formatter(mtick.PercentFormatter())\cb1 \
\cb3 ax.\cf10 \strokec10 set\cf0 \strokec4 (title=\cf6 \strokec6 'Combined Overweight/Obese Rate by State'\cf0 \strokec4 , xlabel=\cf6 \strokec6 'Weighted %'\cf0 \strokec4 )\cb1 \
\cb3 ax.legend(handles=[plt.Rectangle((\cf9 \strokec9 0\cf0 \strokec4 ,\cf9 \strokec9 0\cf0 \strokec4 ),\cf9 \strokec9 1\cf0 \strokec4 ,\cf9 \strokec9 1\cf0 \strokec4 , color=v, label=k)\cb1 \
\cb3                    \cf7 \strokec7 for\cf0 \strokec4  k, v \cf8 \strokec8 in\cf0 \strokec4  region_colors.items()], title=\cf6 \strokec6 'Region'\cf0 \strokec4 , loc=\cf6 \strokec6 'lower right'\cf0 \strokec4 )\cb1 \
\cb3 plt.tight_layout()\cb1 \
\cb3 plt.show()\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # \uc0\u9472 \u9472  Year-over-year trend \'97 combined Overweight/Obese \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 for\cf0 \strokec4  grp \cf8 \strokec8 in\cf0 \strokec4  HealthStatus[\cf6 \strokec6 'Group'\cf0 \strokec4 ].unique():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     sub = HealthStatus[\cb1 \
\cb3         (HealthStatus[\cf6 \strokec6 'Group'\cf0 \strokec4 ] == grp) &\cb1 \
\cb3         (HealthStatus[\cf6 \strokec6 'Weight Status'\cf0 \strokec4 ].isin([\cf6 \strokec6 'Obese'\cf0 \strokec4 ,\cf6 \strokec6 'Overweight'\cf0 \strokec4 ]))\cb1 \
\cb3     ]\cb1 \
\cb3     trend_chart(w_agg(sub, [\cf6 \strokec6 'Year'\cf0 \strokec4 ,\cf6 \strokec6 'Group Value'\cf0 \strokec4 ]), \cf6 \strokec6 'Group Value'\cf0 \strokec4 ,\cb1 \
\cb3                 title=\cf8 \strokec8 f\cf6 \strokec6 'Overweight/Obese Rate Over Time \'97 by \cf0 \strokec4 \{grp\}\cf6 \strokec6 '\cf0 \strokec4 )\cb1 \
}