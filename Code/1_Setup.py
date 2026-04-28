{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red15\green112\blue1;\red255\green255\blue255;\red0\green0\blue0;
\red0\green0\blue255;\red131\green0\blue165;\red144\green1\blue18;\red19\green85\blue52;\red86\green65\blue25;
}
{\*\expandedcolortbl;;\cssrgb\c0\c50196\c0;\cssrgb\c100000\c100000\c100000;\cssrgb\c0\c0\c0;
\cssrgb\c0\c0\c100000;\cssrgb\c59216\c13725\c70588;\cssrgb\c63922\c8235\c8235;\cssrgb\c6667\c40000\c26667;\cssrgb\c41569\c32157\c12941;
}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # \uc0\u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # CELL 1 \'97 SETUP\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # \uc0\u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 !\cf0 \strokec4 pip install adjustText -q\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 import\cf0 \strokec4  warnings\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 warnings.filterwarnings(\cf7 \strokec7 "ignore"\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 import\cf0 \strokec4  random\cb1 \
\cf6 \cb3 \strokec6 import\cf0 \strokec4  numpy \cf6 \strokec6 as\cf0 \strokec4  np\cb1 \
\cf6 \cb3 \strokec6 import\cf0 \strokec4  pandas \cf6 \strokec6 as\cf0 \strokec4  pd\cb1 \
\cf6 \cb3 \strokec6 import\cf0 \strokec4  matplotlib.pyplot \cf6 \strokec6 as\cf0 \strokec4  plt\cb1 \
\cf6 \cb3 \strokec6 import\cf0 \strokec4  matplotlib.ticker \cf6 \strokec6 as\cf0 \strokec4  mtick\cb1 \
\cf6 \cb3 \strokec6 import\cf0 \strokec4  matplotlib.patches \cf6 \strokec6 as\cf0 \strokec4  mpatches\cb1 \
\cf6 \cb3 \strokec6 import\cf0 \strokec4  matplotlib.patheffects \cf6 \strokec6 as\cf0 \strokec4  pe\cb1 \
\cf6 \cb3 \strokec6 import\cf0 \strokec4  seaborn \cf6 \strokec6 as\cf0 \strokec4  sns\cb1 \
\cf6 \cb3 \strokec6 from\cf0 \strokec4  sklearn.preprocessing \cf6 \strokec6 import\cf0 \strokec4  StandardScaler\cb1 \
\cf6 \cb3 \strokec6 from\cf0 \strokec4  sklearn.cluster \cf6 \strokec6 import\cf0 \strokec4  KMeans\cb1 \
\cf6 \cb3 \strokec6 from\cf0 \strokec4  sklearn.metrics \cf6 \strokec6 import\cf0 \strokec4  silhouette_score\cb1 \
\cf6 \cb3 \strokec6 import\cf0 \strokec4  plotly.graph_objects \cf6 \strokec6 as\cf0 \strokec4  go\cb1 \
\cf6 \cb3 \strokec6 from\cf0 \strokec4  adjustText \cf6 \strokec6 import\cf0 \strokec4  adjust_text\cb1 \
\cf6 \cb3 \strokec6 from\cf0 \strokec4  google.colab \cf6 \strokec6 import\cf0 \strokec4  drive\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # Reproducibility\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 random.seed(\cf8 \strokec8 42\cf0 \strokec4 )\cb1 \
\cb3 np.random.seed(\cf8 \strokec8 42\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # Global plot style\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 sns.set_theme(style=\cf7 \strokec7 'whitegrid'\cf0 \strokec4 , palette=\cf7 \strokec7 'Set2'\cf0 \strokec4 )\cb1 \
\cb3 plt.rcParams[\cf7 \strokec7 'figure.dpi'\cf0 \strokec4 ]     = \cf8 \strokec8 120\cf0 \cb1 \strokec4 \
\cb3 plt.rcParams[\cf7 \strokec7 'axes.titlesize'\cf0 \strokec4 ] = \cf8 \strokec8 13\cf0 \cb1 \strokec4 \
\cb3 plt.rcParams[\cf7 \strokec7 'axes.labelsize'\cf0 \strokec4 ] = \cf8 \strokec8 11\cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # tab10 chosen for 10 distinct colors \'97 needed for Race/Ethnicity (8 values)\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 PALETTE = \cf7 \strokec7 'tab10'\cf0 \cb1 \strokec4 \
\
\cb3 drive.mount(\cf7 \strokec7 '/content/drive'\cf0 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf9 \cb3 \strokec9 print\cf0 \strokec4 (\cf7 \strokec7 "Setup complete."\cf0 \strokec4 )\cb1 \
}