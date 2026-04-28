{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red15\green112\blue1;\red255\green255\blue255;\red0\green0\blue0;
\red131\green0\blue165;\red144\green1\blue18;\red0\green0\blue255;\red31\green99\blue128;\red86\green65\blue25;
\red19\green85\blue52;}
{\*\expandedcolortbl;;\cssrgb\c0\c50196\c0;\cssrgb\c100000\c100000\c100000;\cssrgb\c0\c0\c0;
\cssrgb\c59216\c13725\c70588;\cssrgb\c63922\c8235\c8235;\cssrgb\c0\c0\c100000;\cssrgb\c14510\c46275\c57647;\cssrgb\c41569\c32157\c12941;
\cssrgb\c6667\c40000\c26667;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # \uc0\u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # CELL 10b \'97 CLUSTER PROFILE DIAGNOSTIC\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 #\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Systematically interprets clusters before assigning labels.\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Rankings, risk scores, and demographic composition all shown clearly.\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Includes distribution boxplots so profiles are fully characterized here.\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # \uc0\u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 from\cf0 \strokec4  sklearn.metrics \cf5 \strokec5 import\cf0 \strokec4  pairwise_distances\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # \uc0\u9472 \u9472  Ranked profiles \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Rank 1 = worst outcome on that metric\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 RISK_METRICS  = [\cf6 \strokec6 'Overweight/Obese %'\cf0 \strokec4 ,\cf6 \strokec6 'No Activity %'\cf0 \strokec4 ,\cf6 \strokec6 'No Fruit %'\cf0 \strokec4 ,\cf6 \strokec6 'No Vegetables %'\cf0 \strokec4 ]\cb1 \
\cb3 PROT_METRICS  = [\cf6 \strokec6 'Meets 150 Min %'\cf0 \strokec4 ,\cf6 \strokec6 'Strength Only %'\cf0 \strokec4 ,\cf6 \strokec6 'Strength + Aerobic %'\cf0 \strokec4 ]\cb1 \
\
\cb3 ranks = pd.DataFrame(index=cluster_summary.index)\cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 for\cf0 \strokec4  col \cf7 \strokec7 in\cf0 \strokec4  RISK_METRICS:\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     ranks[col] = cluster_summary[col].rank(ascending=\cf7 \strokec7 False\cf0 \strokec4 ).astype(\cf8 \strokec8 int\cf0 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 for\cf0 \strokec4  col \cf7 \strokec7 in\cf0 \strokec4  PROT_METRICS:\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     ranks[col] = cluster_summary[col].rank(ascending=\cf7 \strokec7 True\cf0 \strokec4 ).astype(\cf8 \strokec8 int\cf0 \strokec4 )\cb1 \
\cb3 ranks[\cf6 \strokec6 'Total Risk Score'\cf0 \strokec4 ] = ranks.\cf9 \strokec9 sum\cf0 \strokec4 (axis=\cf10 \strokec10 1\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf9 \cb3 \strokec9 print\cf0 \strokec4 (\cf6 \strokec6 "="\cf0 \strokec4  * \cf10 \strokec10 60\cf0 \strokec4 )\cb1 \
\cf9 \cb3 \strokec9 print\cf0 \strokec4 (\cf6 \strokec6 "CLUSTER RANKINGS  (1 = worst outcome on each metric)"\cf0 \strokec4 )\cb1 \
\cf9 \cb3 \strokec9 print\cf0 \strokec4 (\cf6 \strokec6 "="\cf0 \strokec4  * \cf10 \strokec10 60\cf0 \strokec4 )\cb1 \
\cf9 \cb3 \strokec9 print\cf0 \strokec4 (ranks.to_string())\cb1 \
\
\cf9 \cb3 \strokec9 print\cf0 \strokec4 (\cf6 \strokec6 "\\nTotal Risk Score (lower = worse overall health profile):"\cf0 \strokec4 )\cb1 \
\cf9 \cb3 \strokec9 print\cf0 \strokec4 (ranks[\cf6 \strokec6 'Total Risk Score'\cf0 \strokec4 ].sort_values().to_string())\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # \uc0\u9472 \u9472  Cluster means \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf9 \cb3 \strokec9 print\cf0 \strokec4 (\cf6 \strokec6 "\\n"\cf0 \strokec4  + \cf6 \strokec6 "="\cf0 \strokec4  * \cf10 \strokec10 60\cf0 \strokec4 )\cb1 \
\cf9 \cb3 \strokec9 print\cf0 \strokec4 (\cf6 \strokec6 "CLUSTER MEAN PROFILES"\cf0 \strokec4 )\cb1 \
\cf9 \cb3 \strokec9 print\cf0 \strokec4 (\cf6 \strokec6 "="\cf0 \strokec4  * \cf10 \strokec10 60\cf0 \strokec4 )\cb1 \
\cf9 \cb3 \strokec9 print\cf0 \strokec4 (cluster_summary.to_string())\cb1 \
\
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # \uc0\u9472 \u9472  Most common demographic values per cluster \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf9 \cb3 \strokec9 print\cf0 \strokec4 (\cf6 \strokec6 "\\n"\cf0 \strokec4  + \cf6 \strokec6 "="\cf0 \strokec4  * \cf10 \strokec10 60\cf0 \strokec4 )\cb1 \
\cf9 \cb3 \strokec9 print\cf0 \strokec4 (\cf6 \strokec6 "DOMINANT GROUP VALUES PER CLUSTER"\cf0 \strokec4 )\cb1 \
\cf9 \cb3 \strokec9 print\cf0 \strokec4 (\cf6 \strokec6 "="\cf0 \strokec4  * \cf10 \strokec10 60\cf0 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 for\cf0 \strokec4  c \cf7 \strokec7 in\cf0 \strokec4  \cf9 \strokec9 sorted\cf0 \strokec4 (cluster_df[\cf6 \strokec6 'Cluster'\cf0 \strokec4 ].unique()):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     sub = cluster_df[cluster_df[\cf6 \strokec6 'Cluster'\cf0 \strokec4 ] == c]\cb1 \
\cb3     top = (sub.groupby([\cf6 \strokec6 'Group'\cf0 \strokec4 ,\cf6 \strokec6 'Group Value'\cf0 \strokec4 ]).size()\cb1 \
\cb3              .reset_index(name=\cf6 \strokec6 'n'\cf0 \strokec4 )\cb1 \
\cb3              .sort_values(\cf6 \strokec6 'n'\cf0 \strokec4 , ascending=\cf7 \strokec7 False\cf0 \strokec4 )\cb1 \
\cb3              .head(\cf10 \strokec10 8\cf0 \strokec4 ))\cb1 \
\cb3     \cf9 \strokec9 print\cf0 \strokec4 (\cf7 \strokec7 f\cf6 \strokec6 "\\n  Cluster \cf0 \strokec4 \{c\}\cf6 \strokec6   "\cf0 \cb1 \strokec4 \
\cb3           \cf7 \strokec7 f\cf6 \strokec6 "(n=\cf0 \strokec4 \{\cf9 \strokec9 len\cf0 \strokec4 (sub)\cf10 \strokec10 :,\cf0 \strokec4 \}\cf6 \strokec6   "\cf0 \cb1 \strokec4 \
\cb3           \cf7 \strokec7 f\cf6 \strokec6 "OW/OB=\cf0 \strokec4 \{cluster_summary.loc[c,\cf6 \strokec6 'Overweight/Obese %'\cf0 \strokec4 ]\cf10 \strokec10 :.1f\cf0 \strokec4 \}\cf6 \strokec6 %  "\cf0 \cb1 \strokec4 \
\cb3           \cf7 \strokec7 f\cf6 \strokec6 "NoAct=\cf0 \strokec4 \{cluster_summary.loc[c,\cf6 \strokec6 'No Activity %'\cf0 \strokec4 ]\cf10 \strokec10 :.1f\cf0 \strokec4 \}\cf6 \strokec6 %  "\cf0 \cb1 \strokec4 \
\cb3           \cf7 \strokec7 f\cf6 \strokec6 "Meets150=\cf0 \strokec4 \{cluster_summary.loc[c,\cf6 \strokec6 'Meets 150 Min %'\cf0 \strokec4 ]\cf10 \strokec10 :.1f\cf0 \strokec4 \}\cf6 \strokec6 %)"\cf0 \strokec4 )\cb1 \
\cb3     \cf5 \strokec5 for\cf0 \strokec4  _, r \cf7 \strokec7 in\cf0 \strokec4  top.iterrows():\cb1 \
\cb3         \cf9 \strokec9 print\cf0 \strokec4 (\cf7 \strokec7 f\cf6 \strokec6 "    \cf0 \strokec4 \{r[\cf6 \strokec6 'Group'\cf0 \strokec4 ]\cf10 \strokec10 :18s\cf0 \strokec4 \}\cf6 \strokec6 : \cf0 \strokec4 \{r[\cf6 \strokec6 'Group Value'\cf0 \strokec4 ]\}\cf6 \strokec6  (\cf0 \strokec4 \{r[\cf6 \strokec6 'n'\cf0 \strokec4 ]\}\cf6 \strokec6  rows)"\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # \uc0\u9472 \u9472  Distribution boxplots \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Shown here so cluster profiles are fully characterized before labeling\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 fig, axes = plt.subplots(\cf10 \strokec10 2\cf0 \strokec4 , \cf10 \strokec10 4\cf0 \strokec4 , figsize=(\cf10 \strokec10 20\cf0 \strokec4 , \cf10 \strokec10 10\cf0 \strokec4 ))\cb1 \
\cb3 axes = axes.flatten()\cb1 \
\cb3 pal  = sns.color_palette(PALETTE, K)\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 for\cf0 \strokec4  ax, metric \cf7 \strokec7 in\cf0 \strokec4  \cf9 \strokec9 zip\cf0 \strokec4 (axes, METRICS):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     data = [cluster_df[cluster_df[\cf6 \strokec6 'Cluster'\cf0 \strokec4 ] == c][metric].dropna().values\cb1 \
\cb3             \cf5 \strokec5 for\cf0 \strokec4  c \cf7 \strokec7 in\cf0 \strokec4  \cf9 \strokec9 range\cf0 \strokec4 (K)]\cb1 \
\cb3     bp = ax.boxplot(data, patch_artist=\cf7 \strokec7 True\cf0 \strokec4 )\cb1 \
\cb3     \cf5 \strokec5 for\cf0 \strokec4  patch, color \cf7 \strokec7 in\cf0 \strokec4  \cf9 \strokec9 zip\cf0 \strokec4 (bp[\cf6 \strokec6 'boxes'\cf0 \strokec4 ], pal):\cb1 \
\cb3         patch.set_facecolor(color)\cb1 \
\cb3         patch.set_alpha(\cf10 \strokec10 0.7\cf0 \strokec4 )\cb1 \
\cb3     ax.set_xticklabels([\cf7 \strokec7 f\cf6 \strokec6 'C\cf0 \strokec4 \{i\}\cf6 \strokec6 '\cf0 \strokec4  \cf5 \strokec5 for\cf0 \strokec4  i \cf7 \strokec7 in\cf0 \strokec4  \cf9 \strokec9 range\cf0 \strokec4 (K)])\cb1 \
\cb3     ax.yaxis.set_major_formatter(mtick.PercentFormatter())\cb1 \
\cb3     ax.\cf8 \strokec8 set\cf0 \strokec4 (title=metric, xlabel=\cf6 \strokec6 'Cluster'\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 for\cf0 \strokec4  ax \cf7 \strokec7 in\cf0 \strokec4  axes[\cf9 \strokec9 len\cf0 \strokec4 (METRICS):]:\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     ax.set_visible(\cf7 \strokec7 False\cf0 \strokec4 )\cb1 \
\
\cb3 fig.suptitle(\cf6 \strokec6 'Metric Distributions by Cluster\\n'\cf0 \cb1 \strokec4 \
\cb3              \cf6 \strokec6 'Spread within each cluster \'97 use alongside means above.'\cf0 \strokec4 ,\cb1 \
\cb3              fontsize=\cf10 \strokec10 11\cf0 \strokec4 , y=\cf10 \strokec10 1.02\cf0 \strokec4 )\cb1 \
\cb3 plt.tight_layout()\cb1 \
\cb3 plt.show()\cb1 \
}