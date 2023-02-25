TODAY'S OUTFIT vous permet de savoir pour quelle tenue du jour opté selon la température journalière. 

TODAY'S OUTFIT : anaconda 

NB : peut-etre aurez-vous besoin de taper la commande " source activate" avant d'installer l'environnement virtuel anaconda"

1. Install command : bash install.sh 
vous permet d'installer l'environnement virtuel anaconda 

2. Activate the virtual environment : conda activate myenv 
vous permet d'activer l'environnement virtuel anaconda necessaire à l'éxécution du projet

3. Launch command : bash launch.sh vous permet de charger les données et d'avoir accès à notre recommandation de look du jour selon la température actuelle à Paris. 
En lançant cette commande, une interface sera deployée sur votre machine en local ainsi, 

Vous aurez le choix entre : 
- Une recommandation automatique (Y) qui selon votre sexe (F ou M) vous donnera une recommandation de look du jour.
- Une recommandation manuelle (N) qui selon la température entrée par l'utilisateur et son sexe(F ou M), vous recommandera un look adapté.

NB : entrez la température en float, exemple : 10.0.

#### Dans le cas échéant où l'interface ne se déploie pas, vous pourrez avoir accès aux mêmes fonctionnalités en écrivant en ligne de commande : python -m filter_data_meteo.py ! 

MERCI D'AVANCE !! : - ) 
