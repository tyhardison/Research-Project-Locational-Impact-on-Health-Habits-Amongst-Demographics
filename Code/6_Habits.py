{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red15\green112\blue1;\red255\green255\blue255;\red0\green0\blue0;
\red86\green65\blue25;\red144\green1\blue18;\red0\green0\blue255;\red0\green0\blue109;\red19\green85\blue52;
\red131\green0\blue165;\red31\green99\blue128;}
{\*\expandedcolortbl;;\cssrgb\c0\c50196\c0;\cssrgb\c100000\c100000\c100000;\cssrgb\c0\c0\c0;
\cssrgb\c41569\c32157\c12941;\cssrgb\c63922\c8235\c8235;\cssrgb\c0\c0\c100000;\cssrgb\c0\c6275\c50196;\cssrgb\c6667\c40000\c26667;
\cssrgb\c59216\c13725\c70588;\cssrgb\c14510\c46275\c57647;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # \uc0\u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # CELL 6 \'97 HEALTHHABITS & HEALTHDIET EDA\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Activity profiles and diet patterns across groups and regions\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # \uc0\u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 print\cf0 \strokec4 (\cf6 \strokec6 "HEALTHHABITS EDA"\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # Activity profiles ordered sedentary \uc0\u8594  most active for consistency across charts\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 PROFILE_ORDER = [\cf6 \strokec6 'No Activity'\cf0 \strokec4 ,\cf6 \strokec6 '150 Min Aerobic'\cf0 \strokec4 ,\cf6 \strokec6 '150 Min + Strength'\cf0 \strokec4 ,\cb1 \
\cb3                  \cf6 \strokec6 '300+ Min Aerobic'\cf0 \strokec4 ,\cf6 \strokec6 'Strength Only'\cf0 \strokec4 ]\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 def\cf0 \strokec4  \cf5 \strokec5 activity_cluster_chart\cf0 \strokec4 (\cf8 \strokec8 data\cf0 \strokec4 , \cf8 \strokec8 group_col\cf0 \strokec4 , \cf8 \strokec8 title\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf6 \strokec6 """Clustered bar chart showing all 5 activity profiles for each group value."""\cf0 \cb1 \strokec4 \
\cb3     agg   = w_agg(data, [group_col, \cf6 \strokec6 'Activity Profile'\cf0 \strokec4 ])\cb1 \
\cb3     pivot = (agg.pivot(index=group_col, columns=\cf6 \strokec6 'Activity Profile'\cf0 \strokec4 , values=\cf6 \strokec6 'Weighted %'\cf0 \strokec4 )\cb1 \
\cb3                .reindex(columns=PROFILE_ORDER).fillna(\cf9 \strokec9 0\cf0 \strokec4 ))\cb1 \
\cb3     n     = \cf5 \strokec5 len\cf0 \strokec4 (pivot)\cb1 \
\cb3     x     = np.arange(n)\cb1 \
\cb3     w     = \cf9 \strokec9 0.15\cf0 \cb1 \strokec4 \
\cb3     pal   = sns.color_palette(PALETTE, \cf5 \strokec5 len\cf0 \strokec4 (PROFILE_ORDER))\cb1 \
\cb3     fig, ax = plt.subplots(figsize=(\cf5 \strokec5 max\cf0 \strokec4 (\cf9 \strokec9 10\cf0 \strokec4 , n * \cf9 \strokec9 1.8\cf0 \strokec4 ), \cf9 \strokec9 6\cf0 \strokec4 ))\cb1 \
\cb3     \cf10 \strokec10 for\cf0 \strokec4  i, (prof, color) \cf7 \strokec7 in\cf0 \strokec4  \cf5 \strokec5 enumerate\cf0 \strokec4 (\cf5 \strokec5 zip\cf0 \strokec4 (PROFILE_ORDER, pal)):\cb1 \
\cb3         ax.bar(x + (i - \cf5 \strokec5 len\cf0 \strokec4 (PROFILE_ORDER)/\cf9 \strokec9 2\cf0 \strokec4 ) * w + w/\cf9 \strokec9 2\cf0 \strokec4 ,\cb1 \
\cb3                pivot[prof], width=w, label=prof, color=color)\cb1 \
\cb3     ax.set_xticks(x)\cb1 \
\cb3     ax.set_xticklabels(pivot.index, rotation=\cf9 \strokec9 20\cf0 \strokec4 , ha=\cf6 \strokec6 'right'\cf0 \strokec4 )\cb1 \
\cb3     ax.yaxis.set_major_formatter(mtick.PercentFormatter())\cb1 \
\cb3     ax.\cf11 \strokec11 set\cf0 \strokec4 (title=title, ylabel=\cf6 \strokec6 'Weighted %'\cf0 \strokec4 , xlabel=group_col)\cb1 \
\cb3     ax.legend(title=\cf6 \strokec6 'Activity Profile'\cf0 \strokec4 , bbox_to_anchor=(\cf9 \strokec9 1.01\cf0 \strokec4 ,\cf9 \strokec9 1\cf0 \strokec4 ), loc=\cf6 \strokec6 'upper left'\cf0 \strokec4 , fontsize=\cf9 \strokec9 9\cf0 \strokec4 )\cb1 \
\cb3     plt.tight_layout()\cb1 \
\cb3     plt.show()\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # One chart per demographic group\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf10 \cb3 \strokec10 for\cf0 \strokec4  grp \cf7 \strokec7 in\cf0 \strokec4  HealthHabits[\cf6 \strokec6 'Group'\cf0 \strokec4 ].unique():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     activity_cluster_chart(\cb1 \
\cb3         HealthHabits[HealthHabits[\cf6 \strokec6 'Group'\cf0 \strokec4 ] == grp],\cb1 \
\cb3         \cf6 \strokec6 'Group Value'\cf0 \strokec4 , \cf7 \strokec7 f\cf6 \strokec6 'Activity Profile Distribution \'97 by \cf0 \strokec4 \{grp\}\cf6 \strokec6 '\cf0 \cb1 \strokec4 \
\cb3     )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # One chart for Region\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 activity_cluster_chart(HealthHabits, \cf6 \strokec6 'Region'\cf0 \strokec4 , \cf6 \strokec6 'Activity Profile Distribution \'97 by Region'\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 print\cf0 \strokec4 (\cf6 \strokec6 "\\nHEALTHDIET EDA"\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 def\cf0 \strokec4  \cf5 \strokec5 diet_chart\cf0 \strokec4 (\cf8 \strokec8 data\cf0 \strokec4 , \cf8 \strokec8 group_col\cf0 \strokec4 , \cf8 \strokec8 title\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf6 \strokec6 """Horizontal bar chart \'97 No Fruit vs No Vegetables for each group value."""\cf0 \cb1 \strokec4 \
\cb3     agg   = w_agg(data, [group_col, \cf6 \strokec6 'No Fruits and Vegetables'\cf0 \strokec4 ])\cb1 \
\cb3     pivot = agg.pivot(index=group_col, columns=\cf6 \strokec6 'No Fruits and Vegetables'\cf0 \strokec4 ,\cb1 \
\cb3                       values=\cf6 \strokec6 'Weighted %'\cf0 \strokec4 ).fillna(\cf9 \strokec9 0\cf0 \strokec4 )\cb1 \
\cb3     fig, ax = plt.subplots(figsize=(\cf9 \strokec9 10\cf0 \strokec4 , \cf9 \strokec9 5\cf0 \strokec4 ))\cb1 \
\cb3     pivot.plot(kind=\cf6 \strokec6 'barh'\cf0 \strokec4 , ax=ax, colormap=PALETTE)\cb1 \
\cb3     ax.xaxis.set_major_formatter(mtick.PercentFormatter())\cb1 \
\cb3     ax.\cf11 \strokec11 set\cf0 \strokec4 (title=title, xlabel=\cf6 \strokec6 'Weighted %'\cf0 \strokec4 )\cb1 \
\cb3     plt.tight_layout()\cb1 \
\cb3     plt.show()\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf10 \cb3 \strokec10 for\cf0 \strokec4  grp \cf7 \strokec7 in\cf0 \strokec4  HealthDiet[\cf6 \strokec6 'Group'\cf0 \strokec4 ].unique():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     diet_chart(HealthDiet[HealthDiet[\cf6 \strokec6 'Group'\cf0 \strokec4 ] == grp],\cb1 \
\cb3                \cf6 \strokec6 'Group Value'\cf0 \strokec4 , \cf7 \strokec7 f\cf6 \strokec6 'No Fruit vs No Vegetables \'97 by \cf0 \strokec4 \{grp\}\cf6 \strokec6 '\cf0 \strokec4 )\cb1 \
\
\cb3 diet_chart(HealthDiet, \cf6 \strokec6 'Region'\cf0 \strokec4 , \cf6 \strokec6 'Poor Diet Rate by Region'\cf0 \strokec4 )\cb1 \
}