{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red15\green112\blue1;\red255\green255\blue255;\red0\green0\blue0;
\red0\green0\blue255;\red86\green65\blue25;\red0\green0\blue109;\red144\green1\blue18;\red131\green0\blue165;
\red31\green99\blue128;\red19\green85\blue52;}
{\*\expandedcolortbl;;\cssrgb\c0\c50196\c0;\cssrgb\c100000\c100000\c100000;\cssrgb\c0\c0\c0;
\cssrgb\c0\c0\c100000;\cssrgb\c41569\c32157\c12941;\cssrgb\c0\c6275\c50196;\cssrgb\c63922\c8235\c8235;\cssrgb\c59216\c13725\c70588;
\cssrgb\c14510\c46275\c57647;\cssrgb\c6667\c40000\c26667;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # \uc0\u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # CELL 2 \'97 HELPER FUNCTIONS\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # All shared utilities defined once here and reused throughout the project\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # \uc0\u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 def\cf0 \strokec4  \cf6 \strokec6 w_mean\cf0 \strokec4 (\cf7 \strokec7 df\cf0 \strokec4 , \cf7 \strokec7 value_col\cf0 \strokec4 , \cf7 \strokec7 weight_col\cf0 \strokec4 =\cf8 \strokec8 'Sample Size'\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf8 \strokec8 """Sample-size-weighted mean."""\cf0 \cb1 \strokec4 \
\cb3     \cf9 \strokec9 return\cf0 \strokec4  np.average(df[value_col], weights=df[weight_col])\cb1 \
\
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 def\cf0 \strokec4  \cf6 \strokec6 w_agg\cf0 \strokec4 (\cf7 \strokec7 df\cf0 \strokec4 , \cf7 \strokec7 group_by\cf0 \strokec4 , \cf7 \strokec7 value_col\cf0 \strokec4 =\cf8 \strokec8 'Percentage'\cf0 \strokec4 , \cf7 \strokec7 weight_col\cf0 \strokec4 =\cf8 \strokec8 'Sample Size'\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf8 \strokec8 """\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf8 \cb3 \strokec8     Group df and return weighted mean for each group.\cf0 \cb1 \strokec4 \
\cf8 \cb3 \strokec8     Manual loop used instead of groupby/apply to avoid pandas version issues.\cf0 \cb1 \strokec4 \
\cf8 \cb3 \strokec8     """\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     records = []\cb1 \
\cb3     \cf9 \strokec9 for\cf0 \strokec4  keys, grp \cf5 \strokec5 in\cf0 \strokec4  df.groupby(group_by):\cb1 \
\cb3         \cf9 \strokec9 if\cf0 \strokec4  \cf5 \strokec5 not\cf0 \strokec4  \cf6 \strokec6 isinstance\cf0 \strokec4 (keys, \cf10 \strokec10 tuple\cf0 \strokec4 ):\cb1 \
\cb3             keys = (keys,)\cb1 \
\cb3         records.append(\cb1 \
\cb3             \cf10 \strokec10 dict\cf0 \strokec4 (\cf6 \strokec6 zip\cf0 \strokec4 (group_by, keys)) |\cb1 \
\cb3             \{\cf8 \strokec8 'Weighted %'\cf0 \strokec4 : np.average(grp[value_col], weights=grp[weight_col])\}\cb1 \
\cb3         )\cb1 \
\cb3     \cf9 \strokec9 return\cf0 \strokec4  pd.DataFrame(records)\cb1 \
\
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 def\cf0 \strokec4  \cf6 \strokec6 harmonic\cf0 \strokec4 (\cf7 \strokec7 n1\cf0 \strokec4 , \cf7 \strokec7 n2\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf8 \strokec8 """\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf8 \cb3 \strokec8     Harmonic mean of two sample sizes.\cf0 \cb1 \strokec4 \
\cf8 \cb3 \strokec8     Conservative reliability weight \'97 penalizes imbalanced sample pairings.\cf0 \cb1 \strokec4 \
\cf8 \cb3 \strokec8     Always <= arithmetic mean, so never overstates reliability.\cf0 \cb1 \strokec4 \
\cf8 \cb3 \strokec8     """\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf9 \strokec9 return\cf0 \strokec4  (\cf11 \strokec11 2\cf0 \strokec4  * n1 * n2) / (n1 + n2)\cb1 \
\
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 def\cf0 \strokec4  \cf6 \strokec6 w_pearson\cf0 \strokec4 (\cf7 \strokec7 x\cf0 \strokec4 , \cf7 \strokec7 y\cf0 \strokec4 , \cf7 \strokec7 w\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf8 \strokec8 """\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf8 \cb3 \strokec8     Weighted Pearson correlation.\cf0 \cb1 \strokec4 \
\cf8 \cb3 \strokec8     Built from scratch \'97 scipy pearson r does not support weights.\cf0 \cb1 \strokec4 \
\cf8 \cb3 \strokec8     Inputs forced to 1D float arrays to prevent pandas shape issues.\cf0 \cb1 \strokec4 \
\cf8 \cb3 \strokec8     """\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     x, y, w = (np.asarray(v, dtype=\cf10 \strokec10 float\cf0 \strokec4 ).flatten() \cf9 \strokec9 for\cf0 \strokec4  v \cf5 \strokec5 in\cf0 \strokec4  (x, y, w))\cb1 \
\cb3     w = w / w.\cf6 \strokec6 sum\cf0 \strokec4 ()\cb1 \
\cb3     xm, ym = (w * x).\cf6 \strokec6 sum\cf0 \strokec4 (), (w * y).\cf6 \strokec6 sum\cf0 \strokec4 ()\cb1 \
\cb3     cov    = (w * (x - xm) * (y - ym)).\cf6 \strokec6 sum\cf0 \strokec4 ()\cb1 \
\cb3     sx     = np.sqrt((w * (x - xm) ** \cf11 \strokec11 2\cf0 \strokec4 ).\cf6 \strokec6 sum\cf0 \strokec4 ())\cb1 \
\cb3     sy     = np.sqrt((w * (y - ym) ** \cf11 \strokec11 2\cf0 \strokec4 ).\cf6 \strokec6 sum\cf0 \strokec4 ())\cb1 \
\cb3     \cf9 \strokec9 return\cf0 \strokec4  np.nan \cf9 \strokec9 if\cf0 \strokec4  (sx == \cf11 \strokec11 0\cf0 \strokec4  \cf5 \strokec5 or\cf0 \strokec4  sy == \cf11 \strokec11 0\cf0 \strokec4 ) \cf9 \strokec9 else\cf0 \strokec4  cov / (sx * sy)\cb1 \
\
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 def\cf0 \strokec4  \cf6 \strokec6 scale_pt_sizes\cf0 \strokec4 (\cf7 \strokec7 series\cf0 \strokec4 , \cf7 \strokec7 lo\cf0 \strokec4 =\cf11 \strokec11 30\cf0 \strokec4 , \cf7 \strokec7 hi\cf0 \strokec4 =\cf11 \strokec11 350\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf8 \strokec8 """Map a series to point sizes for scatter plots via min-max scaling."""\cf0 \cb1 \strokec4 \
\cb3     s = series.copy().astype(\cf10 \strokec10 float\cf0 \strokec4 )\cb1 \
\cb3     \cf9 \strokec9 return\cf0 \strokec4  lo + (hi - lo) * (s - s.\cf6 \strokec6 min\cf0 \strokec4 ()) / (s.\cf6 \strokec6 max\cf0 \strokec4 () - s.\cf6 \strokec6 min\cf0 \strokec4 () + \cf11 \strokec11 1e-9\cf0 \strokec4 )\cb1 \
\
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 def\cf0 \strokec4  \cf6 \strokec6 plot_wls_line\cf0 \strokec4 (\cf7 \strokec7 ax\cf0 \strokec4 , \cf7 \strokec7 x\cf0 \strokec4 , \cf7 \strokec7 y\cf0 \strokec4 , \cf7 \strokec7 w\cf0 \strokec4 , \cf7 \strokec7 color\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf8 \strokec8 """Fit and draw a weighted least-squares regression line."""\cf0 \cb1 \strokec4 \
\cb3     \cf9 \strokec9 if\cf0 \strokec4  \cf6 \strokec6 len\cf0 \strokec4 (x) < \cf11 \strokec11 5\cf0 \strokec4 :\cb1 \
\cb3         \cf9 \strokec9 return\cf0 \cb1 \strokec4 \
\cb3     coeffs = np.polyfit(x, y, deg=\cf11 \strokec11 1\cf0 \strokec4 , w=w)\cb1 \
\cb3     xl     = np.linspace(x.\cf6 \strokec6 min\cf0 \strokec4 (), x.\cf6 \strokec6 max\cf0 \strokec4 (), \cf11 \strokec11 50\cf0 \strokec4 )\cb1 \
\cb3     ax.plot(xl, np.polyval(coeffs, xl),\cb1 \
\cb3             color=color, lw=\cf11 \strokec11 1.5\cf0 \strokec4 , ls=\cf8 \strokec8 '--'\cf0 \strokec4 , alpha=\cf11 \strokec11 0.8\cf0 \strokec4 )\cb1 \
\
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 def\cf0 \strokec4  \cf6 \strokec6 extreme_points\cf0 \strokec4 (\cf7 \strokec7 df\cf0 \strokec4 , \cf7 \strokec7 xcol\cf0 \strokec4 , \cf7 \strokec7 ycol\cf0 \strokec4 , \cf7 \strokec7 z\cf0 \strokec4 =\cf11 \strokec11 1.0\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf8 \strokec8 """Return rows simultaneously above z std devs on both axes."""\cf0 \cb1 \strokec4 \
\cb3     xz = (df[xcol] - df[xcol].mean()) / (df[xcol].std() + \cf11 \strokec11 1e-9\cf0 \strokec4 )\cb1 \
\cb3     yz = (df[ycol] - df[ycol].mean()) / (df[ycol].std() + \cf11 \strokec11 1e-9\cf0 \strokec4 )\cb1 \
\cb3     \cf9 \strokec9 return\cf0 \strokec4  df[(xz > z) & (yz > z)]\cb1 \
\
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 def\cf0 \strokec4  \cf6 \strokec6 label_extremes\cf0 \strokec4 (\cf7 \strokec7 ax\cf0 \strokec4 , \cf7 \strokec7 df\cf0 \strokec4 , \cf7 \strokec7 xcol\cf0 \strokec4 , \cf7 \strokec7 ycol\cf0 \strokec4 , \cf7 \strokec7 z\cf0 \strokec4 =\cf11 \strokec11 1.0\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf8 \strokec8 """Annotate extreme points with state name, auto-adjusting for overlap."""\cf0 \cb1 \strokec4 \
\cb3     pts   = extreme_points(df, xcol, ycol, z)\cb1 \
\cb3     texts = [\cb1 \
\cb3         ax.text(r[xcol], r[ycol], r[\cf8 \strokec8 'State'\cf0 \strokec4 ], fontsize=\cf11 \strokec11 6\cf0 \strokec4 , alpha=\cf11 \strokec11 0.8\cf0 \strokec4 ,\cb1 \
\cb3                 path_effects=[pe.withStroke(linewidth=\cf11 \strokec11 1.5\cf0 \strokec4 , foreground=\cf8 \strokec8 'white'\cf0 \strokec4 )])\cb1 \
\cb3         \cf9 \strokec9 for\cf0 \strokec4  _, r \cf5 \strokec5 in\cf0 \strokec4  pts.iterrows()\cb1 \
\cb3     ]\cb1 \
\cb3     \cf9 \strokec9 if\cf0 \strokec4  texts:\cb1 \
\cb3         \cf9 \strokec9 try\cf0 \strokec4 :\cb1 \
\cb3             adjust_text(texts, ax=ax,\cb1 \
\cb3                         arrowprops=\cf10 \strokec10 dict\cf0 \strokec4 (arrowstyle=\cf8 \strokec8 '-'\cf0 \strokec4 , color=\cf8 \strokec8 'gray'\cf0 \strokec4 , lw=\cf11 \strokec11 0.5\cf0 \strokec4 ))\cb1 \
\cb3         \cf9 \strokec9 except\cf0 \strokec4  Exception:\cb1 \
\cb3             \cf9 \strokec9 pass\cf0 \cb1 \strokec4 \
\
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 def\cf0 \strokec4  \cf6 \strokec6 color_col\cf0 \strokec4 (\cf7 \strokec7 df\cf0 \strokec4 , \cf7 \strokec7 group_col\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf8 \strokec8 """\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf8 \cb3 \strokec8     Return df with '_color_val' column for a demographic lens.\cf0 \cb1 \strokec4 \
\cf8 \cb3 \strokec8     Region is a direct column; all others are in the Group/Group Value pair.\cf0 \cb1 \strokec4 \
\cf8 \cb3 \strokec8     """\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf9 \strokec9 if\cf0 \strokec4  group_col == \cf8 \strokec8 'Region'\cf0 \strokec4 :\cb1 \
\cb3         out = df.copy()\cb1 \
\cb3         out[\cf8 \strokec8 '_color_val'\cf0 \strokec4 ] = out[\cf8 \strokec8 'Region'\cf0 \strokec4 ]\cb1 \
\cb3     \cf9 \strokec9 else\cf0 \strokec4 :\cb1 \
\cb3         out = df[df[\cf8 \strokec8 'Group'\cf0 \strokec4 ] == group_col].copy()\cb1 \
\cb3         out[\cf8 \strokec8 '_color_val'\cf0 \strokec4 ] = out[\cf8 \strokec8 'Group Value'\cf0 \strokec4 ]\cb1 \
\cb3     \cf9 \strokec9 return\cf0 \strokec4  out.dropna(subset=[\cf8 \strokec8 '_color_val'\cf0 \strokec4 ])\cb1 \
\
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 def\cf0 \strokec4  \cf6 \strokec6 trend_chart\cf0 \strokec4 (\cf7 \strokec7 df\cf0 \strokec4 , \cf7 \strokec7 group_col\cf0 \strokec4 , \cf7 \strokec7 val_col\cf0 \strokec4 =\cf8 \strokec8 'Weighted %'\cf0 \strokec4 , \cf7 \strokec7 title\cf0 \strokec4 =\cf8 \strokec8 ''\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf8 \strokec8 """Line chart \'97 one line per group value over time."""\cf0 \cb1 \strokec4 \
\cb3     fig, ax = plt.subplots(figsize=(\cf11 \strokec11 12\cf0 \strokec4 , \cf11 \strokec11 6\cf0 \strokec4 ))\cb1 \
\cb3     groups  = df[group_col].unique()\cb1 \
\cb3     pal     = sns.color_palette(PALETTE, \cf6 \strokec6 len\cf0 \strokec4 (groups))\cb1 \
\cb3     \cf9 \strokec9 for\cf0 \strokec4  color, grp \cf5 \strokec5 in\cf0 \strokec4  \cf6 \strokec6 zip\cf0 \strokec4 (pal, groups):\cb1 \
\cb3         sub = df[df[group_col] == grp].sort_values(\cf8 \strokec8 'Year'\cf0 \strokec4 )\cb1 \
\cb3         ax.plot(sub[\cf8 \strokec8 'Year'\cf0 \strokec4 ], sub[val_col], marker=\cf8 \strokec8 'o'\cf0 \strokec4 , label=grp, color=color)\cb1 \
\cb3     ax.yaxis.set_major_formatter(mtick.PercentFormatter())\cb1 \
\cb3     ax.\cf10 \strokec10 set\cf0 \strokec4 (title=title, xlabel=\cf8 \strokec8 'Year'\cf0 \strokec4 , ylabel=\cf8 \strokec8 'Weighted %'\cf0 \strokec4 )\cb1 \
\cb3     ax.legend(bbox_to_anchor=(\cf11 \strokec11 1.01\cf0 \strokec4 , \cf11 \strokec11 1\cf0 \strokec4 ), loc=\cf8 \strokec8 'upper left'\cf0 \strokec4 , fontsize=\cf11 \strokec11 9\cf0 \strokec4 )\cb1 \
\cb3     plt.tight_layout()\cb1 \
\cb3     plt.show()\cb1 \
\
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 print\cf0 \strokec4 (\cf8 \strokec8 "Helpers loaded."\cf0 \strokec4 )\cb1 \
}