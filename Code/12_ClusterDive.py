{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red15\green112\blue1;\red255\green255\blue255;\red0\green0\blue0;
\red131\green0\blue165;\red0\green0\blue255;\red144\green1\blue18;\red86\green65\blue25;\red19\green85\blue52;
\red31\green99\blue128;}
{\*\expandedcolortbl;;\cssrgb\c0\c50196\c0;\cssrgb\c100000\c100000\c100000;\cssrgb\c0\c0\c0;
\cssrgb\c59216\c13725\c70588;\cssrgb\c0\c0\c100000;\cssrgb\c63922\c8235\c8235;\cssrgb\c41569\c32157\c12941;\cssrgb\c6667\c40000\c26667;
\cssrgb\c14510\c46275\c57647;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # \uc0\u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # CELL 12 \'97 EXPANDED CLUSTER DEEP DIVE\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 #\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Y = Overweight/Obese % (fixed outcome)\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # X = each of 6 predictor metrics\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Focus groups: Income, Age, Region (3 rows)\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Clusters ordered worst \uc0\u8594  best health profile (4 columns)\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # \uc0\u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 PREDICTORS    = [m \cf5 \strokec5 for\cf0 \strokec4  m \cf6 \strokec6 in\cf0 \strokec4  METRICS \cf5 \strokec5 if\cf0 \strokec4  m != \cf7 \strokec7 'Overweight/Obese %'\cf0 \strokec4 ]\cb1 \
\cb3 CLUSTER_ORDER = [\cb1 \
\cb3     \cf7 \strokec7 'Cluster 3 \'97 Inactive, Poor Diet & Overweight'\cf0 \strokec4 ,\cb1 \
\cb3     \cf7 \strokec7 'Cluster 0 \'97 Sedentary & Overweight'\cf0 \strokec4 ,\cb1 \
\cb3     \cf7 \strokec7 'Cluster 1 \'97 Active & Overweight'\cf0 \strokec4 ,\cb1 \
\cb3     \cf7 \strokec7 'Cluster 2 \'97 Healthy Weight'\cf0 \strokec4 ,\cb1 \
\cb3 ]\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 for\cf0 \strokec4  xm \cf6 \strokec6 in\cf0 \strokec4  PREDICTORS:\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     fig, axes = plt.subplots(\cb1 \
\cb3         \cf8 \strokec8 len\cf0 \strokec4 (FOCUS_GROUPS), \cf8 \strokec8 len\cf0 \strokec4 (CLUSTER_ORDER),\cb1 \
\cb3         figsize=(\cf9 \strokec9 7\cf0 \strokec4  * \cf8 \strokec8 len\cf0 \strokec4 (CLUSTER_ORDER), \cf9 \strokec9 6\cf0 \strokec4  * \cf8 \strokec8 len\cf0 \strokec4 (FOCUS_GROUPS)),\cb1 \
\cb3         sharex=\cf6 \strokec6 False\cf0 \strokec4 , sharey=\cf6 \strokec6 False\cf0 \cb1 \strokec4 \
\cb3     )\cb1 \
\
\cb3     \cf5 \strokec5 for\cf0 \strokec4  ri, grp \cf6 \strokec6 in\cf0 \strokec4  \cf8 \strokec8 enumerate\cf0 \strokec4 (FOCUS_GROUPS):\cb1 \
\cb3         demo    = color_col(cluster_df, grp)\cb1 \
\cb3         vals    = \cf8 \strokec8 sorted\cf0 \strokec4 (demo[\cf7 \strokec7 '_color_val'\cf0 \strokec4 ].dropna().unique())\cb1 \
\cb3         cmap    = \cf10 \strokec10 dict\cf0 \strokec4 (\cf8 \strokec8 zip\cf0 \strokec4 (vals, sns.color_palette(PALETTE, \cf8 \strokec8 len\cf0 \strokec4 (vals))))\cb1 \
\
\cb3         \cf5 \strokec5 for\cf0 \strokec4  ci, clabel \cf6 \strokec6 in\cf0 \strokec4  \cf8 \strokec8 enumerate\cf0 \strokec4 (CLUSTER_ORDER):\cb1 \
\cb3             ax  = axes[ri, ci]\cb1 \
\cb3             sub = demo[demo[\cf7 \strokec7 'Label'\cf0 \strokec4 ] == clabel].dropna(\cb1 \
\cb3                 subset=[xm,\cf7 \strokec7 'Overweight/Obese %'\cf0 \strokec4 ,\cf7 \strokec7 'Harmonic Weight'\cf0 \strokec4 ])\cb1 \
\cb3             \cf5 \strokec5 if\cf0 \strokec4  sub.empty:\cb1 \
\cb3                 ax.set_visible(\cf6 \strokec6 False\cf0 \strokec4 )\cb1 \
\cb3                 \cf5 \strokec5 continue\cf0 \cb1 \strokec4 \
\
\cb3             \cf5 \strokec5 for\cf0 \strokec4  val \cf6 \strokec6 in\cf0 \strokec4  vals:\cb1 \
\cb3                 grp_sub = sub[sub[\cf7 \strokec7 '_color_val'\cf0 \strokec4 ] == val]\cb1 \
\cb3                 valid   = grp_sub.dropna(subset=[xm,\cf7 \strokec7 'Overweight/Obese %'\cf0 \strokec4 ,\cf7 \strokec7 'Harmonic Weight'\cf0 \strokec4 ])\cb1 \
\cb3                 \cf5 \strokec5 if\cf0 \strokec4  grp_sub.empty:\cb1 \
\cb3                     \cf5 \strokec5 continue\cf0 \cb1 \strokec4 \
\cb3                 ax.scatter(grp_sub[xm], grp_sub[\cf7 \strokec7 'Overweight/Obese %'\cf0 \strokec4 ],\cb1 \
\cb3                            color=cmap[val], s=scale_pt_sizes(grp_sub[\cf7 \strokec7 'Harmonic Weight'\cf0 \strokec4 ]),\cb1 \
\cb3                            alpha=\cf9 \strokec9 0.65\cf0 \strokec4 , edgecolors=\cf7 \strokec7 'white'\cf0 \strokec4 , lw=\cf9 \strokec9 0.3\cf0 \strokec4 , label=val)\cb1 \
\cb3                 \cf5 \strokec5 if\cf0 \strokec4  \cf8 \strokec8 len\cf0 \strokec4 (valid) >= \cf9 \strokec9 5\cf0 \strokec4 :\cb1 \
\cb3                     plot_wls_line(ax,\cb1 \
\cb3                                   valid[xm].to_numpy(dtype=\cf10 \strokec10 float\cf0 \strokec4 ),\cb1 \
\cb3                                   valid[\cf7 \strokec7 'Overweight/Obese %'\cf0 \strokec4 ].to_numpy(dtype=\cf10 \strokec10 float\cf0 \strokec4 ),\cb1 \
\cb3                                   valid[\cf7 \strokec7 'Harmonic Weight'\cf0 \strokec4 ].to_numpy(dtype=\cf10 \strokec10 float\cf0 \strokec4 ),\cb1 \
\cb3                                   cmap[val])\cb1 \
\
\cb3             label_extremes(ax, sub, xm, \cf7 \strokec7 'Overweight/Obese %'\cf0 \strokec4 , z=\cf9 \strokec9 1.0\cf0 \strokec4 )\cb1 \
\cb3             ax.xaxis.set_major_formatter(mtick.PercentFormatter())\cb1 \
\cb3             ax.yaxis.set_major_formatter(mtick.PercentFormatter())\cb1 \
\
\cb3             \cf5 \strokec5 if\cf0 \strokec4  ri == \cf9 \strokec9 0\cf0 \strokec4 :\cb1 \
\cb3                 ax.set_title(clabel, fontsize=\cf9 \strokec9 10\cf0 \strokec4 , fontweight=\cf7 \strokec7 'bold'\cf0 \strokec4 , pad=\cf9 \strokec9 10\cf0 \strokec4 )\cb1 \
\cb3             ax.set_ylabel(\cf6 \strokec6 f\cf7 \strokec7 '\cf0 \strokec4 \{grp\}\cf7 \strokec7 \\n\\nOverweight/Obese %'\cf0 \strokec4  \cf5 \strokec5 if\cf0 \strokec4  ci == \cf9 \strokec9 0\cf0 \cb1 \strokec4 \
\cb3                           \cf5 \strokec5 else\cf0 \strokec4  \cf7 \strokec7 'Overweight/Obese %'\cf0 \strokec4 ,\cb1 \
\cb3                           fontsize=\cf9 \strokec9 9\cf0 \strokec4  \cf5 \strokec5 if\cf0 \strokec4  ci == \cf9 \strokec9 0\cf0 \strokec4  \cf5 \strokec5 else\cf0 \strokec4  \cf9 \strokec9 8\cf0 \strokec4 )\cb1 \
\cb3             \cf5 \strokec5 if\cf0 \strokec4  ri == \cf8 \strokec8 len\cf0 \strokec4 (FOCUS_GROUPS) - \cf9 \strokec9 1\cf0 \strokec4 :\cb1 \
\cb3                 ax.set_xlabel(xm, fontsize=\cf9 \strokec9 9\cf0 \strokec4 )\cb1 \
\
\cb3         axes[ri, \cf9 \strokec9 -1\cf0 \strokec4 ].legend(\cb1 \
\cb3             handles=[mpatches.Patch(color=cmap[v], label=v) \cf5 \strokec5 for\cf0 \strokec4  v \cf6 \strokec6 in\cf0 \strokec4  vals],\cb1 \
\cb3             title=grp, bbox_to_anchor=(\cf9 \strokec9 1.02\cf0 \strokec4 ,\cf9 \strokec9 1\cf0 \strokec4 ), loc=\cf7 \strokec7 'upper left'\cf0 \strokec4 ,\cb1 \
\cb3             fontsize=\cf9 \strokec9 7\cf0 \strokec4 , title_fontsize=\cf9 \strokec9 8\cf0 \strokec4 , framealpha=\cf9 \strokec9 0.8\cf0 \strokec4 )\cb1 \
\
\cb3     fig.suptitle(\cb1 \
\cb3         \cf6 \strokec6 f\cf7 \strokec7 '\cf0 \strokec4 \{xm\}\cf7 \strokec7  vs Overweight/Obese % \'97 All Clusters \'d7 Focus Groups\\n'\cf0 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 'Columns: worst \uc0\u8594  best risk. Rows: Income, Age, Region.\\n'\cf0 \cb1 \strokec4 \
\cb3         \cf7 \strokec7 'Point size = harmonic weight. Dashed = weighted regression. Ecological only.'\cf0 \strokec4 ,\cb1 \
\cb3         fontsize=\cf9 \strokec9 11\cf0 \strokec4 , y=\cf9 \strokec9 1.01\cf0 \strokec4 )\cb1 \
\cb3     plt.tight_layout()\cb1 \
\cb3     plt.show()\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf8 \cb3 \strokec8 print\cf0 \strokec4 (\cf7 \strokec7 "Expanded deep dive complete."\cf0 \strokec4 )\cb1 \
}