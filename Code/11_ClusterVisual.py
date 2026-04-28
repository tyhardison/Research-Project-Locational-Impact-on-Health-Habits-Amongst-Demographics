{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red15\green112\blue1;\red255\green255\blue255;\red0\green0\blue0;
\red19\green85\blue52;\red144\green1\blue18;\red86\green65\blue25;\red131\green0\blue165;\red0\green0\blue255;
\red31\green99\blue128;}
{\*\expandedcolortbl;;\cssrgb\c0\c50196\c0;\cssrgb\c100000\c100000\c100000;\cssrgb\c0\c0\c0;
\cssrgb\c6667\c40000\c26667;\cssrgb\c63922\c8235\c8235;\cssrgb\c41569\c32157\c12941;\cssrgb\c59216\c13725\c70588;\cssrgb\c0\c0\c100000;
\cssrgb\c14510\c46275\c57647;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # \uc0\u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # CELL 11 \'97 CLUSTER VISUALIZATIONS\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 #\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Labels assigned from Cell 10b diagnostic.\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Update CLUSTER_LABELS if K or cluster order changes.\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # \uc0\u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 CLUSTER_LABELS = \{\cb1 \
\cb3     \cf5 \strokec5 0\cf0 \strokec4 : \cf6 \strokec6 'Cluster 0 \'97 Sedentary & Overweight'\cf0 \strokec4 ,\cb1 \
\cb3     \cf5 \strokec5 1\cf0 \strokec4 : \cf6 \strokec6 'Cluster 1 \'97 Active & Overweight'\cf0 \strokec4 ,\cb1 \
\cb3     \cf5 \strokec5 2\cf0 \strokec4 : \cf6 \strokec6 'Cluster 2 \'97 Healthy Weight'\cf0 \strokec4 ,\cb1 \
\cb3     \cf5 \strokec5 3\cf0 \strokec4 : \cf6 \strokec6 'Cluster 3 \'97 Inactive, Poor Diet & Overweight'\cf0 \strokec4 ,\cb1 \
\cb3 \}\cb1 \
\cb3 cluster_df[\cf6 \strokec6 'Label'\cf0 \strokec4 ] = cluster_df[\cf6 \strokec6 'Cluster'\cf0 \strokec4 ].\cf7 \strokec7 map\cf0 \strokec4 (CLUSTER_LABELS)\cb1 \
\
\cb3 C_PAL    = sns.color_palette(PALETTE, K)\cb1 \
\cb3 C_COLORS = \{CLUSTER_LABELS[i]: C_PAL[i] \cf8 \strokec8 for\cf0 \strokec4  i \cf9 \strokec9 in\cf0 \strokec4  \cf7 \strokec7 range\cf0 \strokec4 (K)\}\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # \uc0\u9472 \u9472  Parallel coordinates \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 par_df = cluster_summary.reset_index()\cb1 \
\cb3 par_df[\cf6 \strokec6 'Label'\cf0 \strokec4 ] = par_df[\cf6 \strokec6 'Cluster'\cf0 \strokec4 ].\cf7 \strokec7 map\cf0 \strokec4 (CLUSTER_LABELS)\cb1 \
\
\cb3 fig, ax = plt.subplots(figsize=(\cf5 \strokec5 15\cf0 \strokec4 , \cf5 \strokec5 6\cf0 \strokec4 ))\cb1 \
\pard\pardeftab720\partightenfactor0
\cf8 \cb3 \strokec8 for\cf0 \strokec4  _, row \cf9 \strokec9 in\cf0 \strokec4  par_df.iterrows():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     label = row[\cf6 \strokec6 'Label'\cf0 \strokec4 ]\cb1 \
\cb3     ax.plot(METRICS, row[METRICS].values.astype(\cf10 \strokec10 float\cf0 \strokec4 ),\cb1 \
\cb3             marker=\cf6 \strokec6 'o'\cf0 \strokec4 , label=label, color=C_COLORS[label], lw=\cf5 \strokec5 2.5\cf0 \strokec4 )\cb1 \
\cb3     ax.annotate(\cf9 \strokec9 f\cf6 \strokec6 "\cf0 \strokec4 \{row[METRICS[\cf5 \strokec5 -1\cf0 \strokec4 ]]\cf5 \strokec5 :.1f\cf0 \strokec4 \}\cf6 \strokec6 %"\cf0 \strokec4 ,\cb1 \
\cb3                 xy=(\cf7 \strokec7 len\cf0 \strokec4 (METRICS)\cf5 \strokec5 -1\cf0 \strokec4 , row[METRICS[\cf5 \strokec5 -1\cf0 \strokec4 ]]),\cb1 \
\cb3                 xytext=(\cf5 \strokec5 5\cf0 \strokec4 ,\cf5 \strokec5 0\cf0 \strokec4 ), textcoords=\cf6 \strokec6 'offset points'\cf0 \strokec4 ,\cb1 \
\cb3                 color=C_COLORS[label], fontsize=\cf5 \strokec5 8\cf0 \strokec4 )\cb1 \
\
\cb3 ax.set_xticks(\cf7 \strokec7 range\cf0 \strokec4 (\cf7 \strokec7 len\cf0 \strokec4 (METRICS)))\cb1 \
\cb3 ax.set_xticklabels(METRICS, rotation=\cf5 \strokec5 20\cf0 \strokec4 , ha=\cf6 \strokec6 'right'\cf0 \strokec4 )\cb1 \
\cb3 ax.yaxis.set_major_formatter(mtick.PercentFormatter())\cb1 \
\cb3 ax.\cf10 \strokec10 set\cf0 \strokec4 (title=\cf9 \strokec9 f\cf6 \strokec6 'Parallel Coordinates \'97 Cluster Health Profiles (K=\cf0 \strokec4 \{K\}\cf6 \strokec6 )\\n'\cf0 \cb1 \strokec4 \
\cb3              \cf6 \strokec6 'Population-level co-occurrence patterns. Not causal.'\cf0 \strokec4 ,\cb1 \
\cb3        ylabel=\cf6 \strokec6 'Mean %'\cf0 \strokec4 )\cb1 \
\cb3 ax.legend(bbox_to_anchor=(\cf5 \strokec5 1.01\cf0 \strokec4 ,\cf5 \strokec5 1\cf0 \strokec4 ), loc=\cf6 \strokec6 'upper left'\cf0 \strokec4 , fontsize=\cf5 \strokec5 9\cf0 \strokec4 )\cb1 \
\cb3 plt.tight_layout()\cb1 \
\cb3 plt.show()\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # \uc0\u9472 \u9472  Pairwise scatter plots colored by cluster \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 SCATTER_PAIRS = [\cb1 \
\cb3     (\cf6 \strokec6 'Overweight/Obese %'\cf0 \strokec4 , \cf6 \strokec6 'No Activity %'\cf0 \strokec4 ),\cb1 \
\cb3     (\cf6 \strokec6 'Overweight/Obese %'\cf0 \strokec4 , \cf6 \strokec6 'Meets 150 Min %'\cf0 \strokec4 ),\cb1 \
\cb3     (\cf6 \strokec6 'Overweight/Obese %'\cf0 \strokec4 , \cf6 \strokec6 'Strength Only %'\cf0 \strokec4 ),\cb1 \
\cb3     (\cf6 \strokec6 'Overweight/Obese %'\cf0 \strokec4 , \cf6 \strokec6 'Strength + Aerobic %'\cf0 \strokec4 ),\cb1 \
\cb3     (\cf6 \strokec6 'Overweight/Obese %'\cf0 \strokec4 , \cf6 \strokec6 'No Fruit %'\cf0 \strokec4 ),\cb1 \
\cb3     (\cf6 \strokec6 'Overweight/Obese %'\cf0 \strokec4 , \cf6 \strokec6 'No Vegetables %'\cf0 \strokec4 ),\cb1 \
\cb3 ]\cb1 \
\
\cb3 fig, axes = plt.subplots(\cf5 \strokec5 2\cf0 \strokec4 , \cf5 \strokec5 3\cf0 \strokec4 , figsize=(\cf5 \strokec5 16\cf0 \strokec4 , \cf5 \strokec5 14\cf0 \strokec4 ))\cb1 \
\cb3 axes = axes.flatten()\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf8 \cb3 \strokec8 for\cf0 \strokec4  ax, (xc, yc) \cf9 \strokec9 in\cf0 \strokec4  \cf7 \strokec7 zip\cf0 \strokec4 (axes, SCATTER_PAIRS):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf8 \strokec8 for\cf0 \strokec4  label, color \cf9 \strokec9 in\cf0 \strokec4  C_COLORS.items():\cb1 \
\cb3         sub = cluster_df[cluster_df[\cf6 \strokec6 'Label'\cf0 \strokec4 ] == label]\cb1 \
\cb3         ax.scatter(sub[xc], sub[yc], color=color, alpha=\cf5 \strokec5 0.4\cf0 \strokec4 , s=\cf5 \strokec5 15\cf0 \strokec4 , label=label)\cb1 \
\cb3     \cf2 \strokec2 # Cluster centroids as stars\cf0 \cb1 \strokec4 \
\cb3     \cf8 \strokec8 for\cf0 \strokec4  _, row \cf9 \strokec9 in\cf0 \strokec4  par_df.iterrows():\cb1 \
\cb3         ax.scatter(row[xc], row[yc], color=C_COLORS[row[\cf6 \strokec6 'Label'\cf0 \strokec4 ]],\cb1 \
\cb3                    s=\cf5 \strokec5 200\cf0 \strokec4 , marker=\cf6 \strokec6 '*'\cf0 \strokec4 , edgecolors=\cf6 \strokec6 'black'\cf0 \strokec4 , lw=\cf5 \strokec5 0.5\cf0 \strokec4 , zorder=\cf5 \strokec5 5\cf0 \strokec4 )\cb1 \
\cb3     ax.xaxis.set_major_formatter(mtick.PercentFormatter())\cb1 \
\cb3     ax.yaxis.set_major_formatter(mtick.PercentFormatter())\cb1 \
\cb3     ax.\cf10 \strokec10 set\cf0 \strokec4 (xlabel=xc, ylabel=yc, title=\cf9 \strokec9 f\cf6 \strokec6 '\cf0 \strokec4 \{xc\}\cf6 \strokec6  vs \cf0 \strokec4 \{yc\}\cf6 \strokec6 '\cf0 \strokec4 )\cb1 \
\
\cb3 fig.legend(handles=[mpatches.Patch(color=C_COLORS[l], label=l) \cf8 \strokec8 for\cf0 \strokec4  l \cf9 \strokec9 in\cf0 \strokec4  C_COLORS],\cb1 \
\cb3            bbox_to_anchor=(\cf5 \strokec5 0.5\cf0 \strokec4 ,\cf5 \strokec5 -0.02\cf0 \strokec4 ), loc=\cf6 \strokec6 'upper center'\cf0 \strokec4 , ncol=\cf5 \strokec5 2\cf0 \strokec4 , fontsize=\cf5 \strokec5 9\cf0 \strokec4 )\cb1 \
\cb3 fig.suptitle(\cf6 \strokec6 'Pairwise Scatter \'97 Colored by Cluster\\n'\cf0 \cb1 \strokec4 \
\cb3              \cf6 \strokec6 'Stars = centroids. Ecological level only.'\cf0 \strokec4 , fontsize=\cf5 \strokec5 11\cf0 \strokec4 , y=\cf5 \strokec5 1.02\cf0 \strokec4 )\cb1 \
\cb3 plt.tight_layout()\cb1 \
\cb3 plt.show()\cb1 \
}