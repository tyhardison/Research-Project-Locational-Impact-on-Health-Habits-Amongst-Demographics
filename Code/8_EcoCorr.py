{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red15\green112\blue1;\red255\green255\blue255;\red0\green0\blue0;
\red0\green0\blue255;\red86\green65\blue25;\red0\green0\blue109;\red144\green1\blue18;\red131\green0\blue165;
\red19\green85\blue52;\red31\green99\blue128;}
{\*\expandedcolortbl;;\cssrgb\c0\c50196\c0;\cssrgb\c100000\c100000\c100000;\cssrgb\c0\c0\c0;
\cssrgb\c0\c0\c100000;\cssrgb\c41569\c32157\c12941;\cssrgb\c0\c6275\c50196;\cssrgb\c63922\c8235\c8235;\cssrgb\c59216\c13725\c70588;
\cssrgb\c6667\c40000\c26667;\cssrgb\c14510\c46275\c57647;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # \uc0\u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # CELL 8 \'97 WEIGHTED ECOLOGICAL CORRELATIONS\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 #\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # All correlations are at the population-group level (ecological).\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Individual-level inference is not supported \'97 this is not causal.\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Sensitivity check: full dataset vs reliable-only (n>=100 all metrics).\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # \uc0\u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 def\cf0 \strokec4  \cf6 \strokec6 corr_matrix\cf0 \strokec4 (\cf7 \strokec7 df\cf0 \strokec4 , \cf7 \strokec7 metrics\cf0 \strokec4 , \cf7 \strokec7 w_col\cf0 \strokec4 =\cf8 \strokec8 'Harmonic Weight'\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf8 \strokec8 """Pairwise weighted Pearson correlation matrix."""\cf0 \cb1 \strokec4 \
\cb3     df  = df.reset_index(drop=\cf5 \strokec5 True\cf0 \strokec4 ).copy()\cb1 \
\cb3     mat = np.full((\cf6 \strokec6 len\cf0 \strokec4 (metrics), \cf6 \strokec6 len\cf0 \strokec4 (metrics)), np.nan)\cb1 \
\cb3     \cf9 \strokec9 for\cf0 \strokec4  i, m1 \cf5 \strokec5 in\cf0 \strokec4  \cf6 \strokec6 enumerate\cf0 \strokec4 (metrics):\cb1 \
\cb3         \cf9 \strokec9 for\cf0 \strokec4  j, m2 \cf5 \strokec5 in\cf0 \strokec4  \cf6 \strokec6 enumerate\cf0 \strokec4 (metrics):\cb1 \
\cb3             mask = df[m1].notna() & df[m2].notna() & df[w_col].notna()\cb1 \
\cb3             \cf9 \strokec9 if\cf0 \strokec4  mask.\cf6 \strokec6 sum\cf0 \strokec4 () < \cf10 \strokec10 5\cf0 \strokec4 :\cb1 \
\cb3                 \cf9 \strokec9 continue\cf0 \cb1 \strokec4 \
\cb3             mat[i, j] = w_pearson(\cb1 \
\cb3                 df.loc[mask, m1].to_numpy(dtype=\cf11 \strokec11 float\cf0 \strokec4 ),\cb1 \
\cb3                 df.loc[mask, m2].to_numpy(dtype=\cf11 \strokec11 float\cf0 \strokec4 ),\cb1 \
\cb3                 df.loc[mask, w_col].to_numpy(dtype=\cf11 \strokec11 float\cf0 \strokec4 )\cb1 \
\cb3             )\cb1 \
\cb3     \cf9 \strokec9 return\cf0 \strokec4  pd.DataFrame(mat, index=metrics, columns=metrics)\cb1 \
\
\
\cb3 corr_all  = corr_matrix(profile, METRICS)\cb1 \
\cb3 corr_rel  = corr_matrix(profile[profile[\cf8 \strokec8 'Reliable'\cf0 \strokec4 ]].reset_index(drop=\cf5 \strokec5 True\cf0 \strokec4 ), METRICS)\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # Side-by-side: full vs reliable-only\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 fig, axes = plt.subplots(\cf10 \strokec10 1\cf0 \strokec4 , \cf10 \strokec10 2\cf0 \strokec4 , figsize=(\cf10 \strokec10 18\cf0 \strokec4 , \cf10 \strokec10 7\cf0 \strokec4 ))\cb1 \
\pard\pardeftab720\partightenfactor0
\cf9 \cb3 \strokec9 for\cf0 \strokec4  ax, corr, title \cf5 \strokec5 in\cf0 \strokec4  \cf6 \strokec6 zip\cf0 \strokec4 (axes, [corr_all, corr_rel],\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3                             [\cf8 \strokec8 'All Observations'\cf0 \strokec4 , \cf8 \strokec8 'Reliable Only (n \uc0\u8805  100)'\cf0 \strokec4 ]):\cb1 \
\cb3     sns.heatmap(corr, annot=\cf5 \strokec5 True\cf0 \strokec4 , fmt=\cf8 \strokec8 '.2f'\cf0 \strokec4 , cmap=\cf8 \strokec8 'coolwarm'\cf0 \strokec4 ,\cb1 \
\cb3                 center=\cf10 \strokec10 0\cf0 \strokec4 , linewidths=\cf10 \strokec10 0.5\cf0 \strokec4 , ax=ax, vmin=\cf10 \strokec10 -1\cf0 \strokec4 , vmax=\cf10 \strokec10 1\cf0 \strokec4 )\cb1 \
\cb3     ax.set_title(\cf5 \strokec5 f\cf8 \strokec8 'Weighted Ecological Correlations\\n\cf0 \strokec4 \{title\}\cf8 \strokec8 '\cf0 \strokec4 )\cb1 \
\
\cb3 plt.suptitle(\cf8 \strokec8 'Sensitivity Analysis \'97 Full vs Reliable\\n'\cf0 \cb1 \strokec4 \
\cb3              \cf8 \strokec8 'Population-group level only. Not individual-level inference.'\cf0 \strokec4 ,\cb1 \
\cb3              fontsize=\cf10 \strokec10 10\cf0 \strokec4 , style=\cf8 \strokec8 'italic'\cf0 \strokec4 , y=\cf10 \strokec10 1.02\cf0 \strokec4 )\cb1 \
\cb3 plt.tight_layout()\cb1 \
\cb3 plt.show()\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # Flag any notable shifts between full and reliable-only\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 print\cf0 \strokec4 (\cf8 \strokec8 "\\nCorrelation shifts > 0.05 (full vs reliable):"\cf0 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 notable = [(m1, m2, \cf6 \strokec6 abs\cf0 \strokec4 (corr_rel.loc[m1,m2] - corr_all.loc[m1,m2]))\cb1 \
\cb3            \cf9 \strokec9 for\cf0 \strokec4  m1 \cf5 \strokec5 in\cf0 \strokec4  METRICS \cf9 \strokec9 for\cf0 \strokec4  m2 \cf5 \strokec5 in\cf0 \strokec4  METRICS \cf9 \strokec9 if\cf0 \strokec4  m1 < m2\cb1 \
\cb3            \cf9 \strokec9 if\cf0 \strokec4  \cf6 \strokec6 abs\cf0 \strokec4 (corr_rel.loc[m1,m2] - corr_all.loc[m1,m2]) > \cf10 \strokec10 0.05\cf0 \strokec4 ]\cb1 \
\pard\pardeftab720\partightenfactor0
\cf9 \cb3 \strokec9 if\cf0 \strokec4  notable:\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf9 \strokec9 for\cf0 \strokec4  m1, m2, d \cf5 \strokec5 in\cf0 \strokec4  notable:\cb1 \
\cb3         \cf6 \strokec6 print\cf0 \strokec4 (\cf5 \strokec5 f\cf8 \strokec8 "  \cf0 \strokec4 \{m1\}\cf8 \strokec8  vs \cf0 \strokec4 \{m2\}\cf8 \strokec8 : \uc0\u916 =\cf0 \strokec4 \{d\cf10 \strokec10 :.2f\cf0 \strokec4 \}\cf8 \strokec8 "\cf0 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf9 \cb3 \strokec9 else\cf0 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf6 \strokec6 print\cf0 \strokec4 (\cf8 \strokec8 "  None \'97 findings are robust across full and reliable subsets."\cf0 \strokec4 )\cb1 \
}