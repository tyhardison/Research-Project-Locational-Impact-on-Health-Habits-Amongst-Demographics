{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red15\green112\blue1;\red255\green255\blue255;\red0\green0\blue0;
\red144\green1\blue18;\red0\green0\blue255;\red131\green0\blue165;\red86\green65\blue25;\red19\green85\blue52;
\red31\green99\blue128;}
{\*\expandedcolortbl;;\cssrgb\c0\c50196\c0;\cssrgb\c100000\c100000\c100000;\cssrgb\c0\c0\c0;
\cssrgb\c63922\c8235\c8235;\cssrgb\c0\c0\c100000;\cssrgb\c59216\c13725\c70588;\cssrgb\c41569\c32157\c12941;\cssrgb\c6667\c40000\c26667;
\cssrgb\c14510\c46275\c57647;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # \uc0\u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # CELL 10 \'97 K-MEANS CLUSTERING\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 #\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Clusters on reliable rows only (all metric sample sizes >= 100).\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # StandardScaler required before k-means \'97 Euclidean distance is scale-sensitive.\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # K selected via elbow + silhouette. random_state=42 for reproducibility.\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Clusters describe co-occurring population health profiles. Not causal.\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # \uc0\u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \cf0 \cb1 \strokec4 \
\
\cf2 \cb3 \strokec2 # Reliable rows only \'97 prevents sampling noise from influencing cluster boundaries\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 cluster_df = (profile[profile[\cf5 \strokec5 'Reliable'\cf0 \strokec4 ]]\cb1 \
\cb3               .dropna(subset=METRICS)\cb1 \
\cb3               .reset_index(drop=\cf6 \strokec6 True\cf0 \strokec4 )\cb1 \
\cb3               .copy())\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # Standardize all 7 metrics to mean=0, std=1 before clustering\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 scaler   = StandardScaler()\cb1 \
\cb3 X_scaled = scaler.fit_transform(cluster_df[METRICS])\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # \uc0\u9472 \u9472  K selection: elbow + silhouette \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 inertias, silhouettes = [], []\cb1 \
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 for\cf0 \strokec4  k \cf6 \strokec6 in\cf0 \strokec4  \cf8 \strokec8 range\cf0 \strokec4 (\cf9 \strokec9 2\cf0 \strokec4 , \cf9 \strokec9 9\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     km = KMeans(n_clusters=k, random_state=\cf9 \strokec9 42\cf0 \strokec4 , n_init=\cf9 \strokec9 10\cf0 \strokec4 )\cb1 \
\cb3     lbl = km.fit_predict(X_scaled)\cb1 \
\cb3     inertias.append(km.inertia_)\cb1 \
\cb3     silhouettes.append(silhouette_score(X_scaled, lbl))\cb1 \
\
\cb3 fig, axes = plt.subplots(\cf9 \strokec9 1\cf0 \strokec4 , \cf9 \strokec9 2\cf0 \strokec4 , figsize=(\cf9 \strokec9 13\cf0 \strokec4 , \cf9 \strokec9 4\cf0 \strokec4 ))\cb1 \
\cb3 axes[\cf9 \strokec9 0\cf0 \strokec4 ].plot(\cf8 \strokec8 range\cf0 \strokec4 (\cf9 \strokec9 2\cf0 \strokec4 ,\cf9 \strokec9 9\cf0 \strokec4 ), inertias,   marker=\cf5 \strokec5 'o'\cf0 \strokec4 , color=sns.color_palette(PALETTE)[\cf9 \strokec9 0\cf0 \strokec4 ])\cb1 \
\cb3 axes[\cf9 \strokec9 1\cf0 \strokec4 ].plot(\cf8 \strokec8 range\cf0 \strokec4 (\cf9 \strokec9 2\cf0 \strokec4 ,\cf9 \strokec9 9\cf0 \strokec4 ), silhouettes, marker=\cf5 \strokec5 'o'\cf0 \strokec4 , color=sns.color_palette(PALETTE)[\cf9 \strokec9 1\cf0 \strokec4 ])\cb1 \
\cb3 axes[\cf9 \strokec9 0\cf0 \strokec4 ].\cf10 \strokec10 set\cf0 \strokec4 (title=\cf5 \strokec5 'Elbow \'97 Inertia by K'\cf0 \strokec4 ,          xlabel=\cf5 \strokec5 'K'\cf0 \strokec4 , ylabel=\cf5 \strokec5 'Inertia'\cf0 \strokec4 )\cb1 \
\cb3 axes[\cf9 \strokec9 1\cf0 \strokec4 ].\cf10 \strokec10 set\cf0 \strokec4 (title=\cf5 \strokec5 'Silhouette Score by K'\cf0 \strokec4 ,          xlabel=\cf5 \strokec5 'K'\cf0 \strokec4 , ylabel=\cf5 \strokec5 'Silhouette'\cf0 \strokec4 )\cb1 \
\cb3 plt.suptitle(\cf5 \strokec5 'K Selection'\cf0 \strokec4 , fontsize=\cf9 \strokec9 12\cf0 \strokec4 )\cb1 \
\cb3 plt.tight_layout()\cb1 \
\cb3 plt.show()\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # \uc0\u9472 \u9472  Fit final model (adjust K if elbow/silhouette suggest otherwise) \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 K = \cf9 \strokec9 4\cf0 \cb1 \strokec4 \
\cb3 km_final              = KMeans(n_clusters=K, random_state=\cf9 \strokec9 42\cf0 \strokec4 , n_init=\cf9 \strokec9 10\cf0 \strokec4 )\cb1 \
\cb3 cluster_df[\cf5 \strokec5 'Cluster'\cf0 \strokec4 ] = km_final.fit_predict(X_scaled)\cb1 \
\
\cb3 cluster_summary = cluster_df.groupby(\cf5 \strokec5 'Cluster'\cf0 \strokec4 )[METRICS].mean().\cf8 \strokec8 round\cf0 \strokec4 (\cf9 \strokec9 1\cf0 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf8 \cb3 \strokec8 print\cf0 \strokec4 (\cf5 \strokec5 "\\nCluster mean profiles:"\cf0 \strokec4 )\cb1 \
\cf8 \cb3 \strokec8 print\cf0 \strokec4 (cluster_summary.to_string())\cb1 \
}