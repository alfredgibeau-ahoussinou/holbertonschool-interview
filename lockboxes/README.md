<img height="50px" align="right" src="https://raw.githubusercontent.com/fchavonet/fchavonet/main/resources/images/logo-holberton_school.png" alt="Logo de l'école Holberton">

# Lockboxes

## 🔖 Table des matières

<details>
    <summary>
    CLIQUEZ POUR AGRANDIR 😇
    </summary>
    📄 <a href="#description">Description</a>
    <br>
    🎓 <a href="#objectifs">Objectifs</a>
    <br>
    📋 <a href="#exigences">Exigences</a>
    <br>
    📝 <a href="#instructions">Instructions</a>
    <br>
    🔨 <a href="#technologies">Technologies</a>
    <br>
    📂 <a href="#description-des-fichiers">Description des fichiers</a>
    <br>
    💻 <a href="#installation_et_utilisation">Installation et utilisation</a>
    <br>
    ♥️ <a href="#remerciements">Remerciements</a>
    <br>
    👷 <a href="#auteurs">Auteurs</a>
</details>

## 📄 <span id="description">Description</span>

Dans ce projet, vous avez plusieurs boîtes verrouillées, chacune contenant des clés pour d'autres boîtes. La première boîte (boîte 0) est déverrouillée, et vous pouvez utiliser les clés à l'intérieur pour ouvrir plus de boîtes. Par exemple, si la boîte 1 contient la clé de la boîte 2, cela signifie que la boîte 2 peut maintenant être ouverte. Vous continuez à utiliser les clés trouvées dans chaque boîte pour déverrouiller autant de boîtes que possible. L'objectif est de déterminer si toutes les boîtes peuvent être ouvertes. Si vous pouvez ouvrir toutes les boîtes, la fonction renvoie True; sinon, elle renvoie False.

## 🎓 <span id="objectifs">Objectifs</span>

À la fin de ce projet, je devais être capable d'expliquer à n'importe qui, **sans l'aide de Google** :

- Comment comprendre et implémenter un algorithme qui résout le problème des Lockboxes.
- Comment écrire du code Python qui respecte les meilleures pratiques, y compris suivre les directives de style PEP8.
- Comment analyser les exigences du problème et les traduire en code fonctionnel.
- Comment s'assurer que la solution est efficace et capable de gérer divers cas limites.

## 📋 <span id="exigences">Exigences</span>

- Tous mes fichiers doivent se terminer par une nouvelle ligne.
- La première ligne de tous mes fichiers doit être exactement `#!/usr/bin/python3`.
- Un fichier `README.md`, à la racine du dossier du projet, est obligatoire.
- Mon code doit être documenté.
- Mon code doit utiliser le style `PEP 8` (version 1.7.x).
- Tous mes fichiers doivent être exécutables.

## 📝 <span id="instructions">Instructions</span>

<details>
    <summary>
    <b>0. Lockboxes</b>
    </summary>
    <br>

Vous avez `n` boîtes verrouillées devant vous. Chaque boîte est numérotée séquentiellement de `0` à `n - 1` et chaque boîte peut contenir des clés pour les autres boîtes.

Écrivez une méthode qui détermine si toutes les boîtes peuvent être ouvertes.

- Prototype : `def canUnlockAll(boxes)`.
- `boxes` est une liste de listes.
- Une clé avec le même numéro qu'une boîte ouvre cette boîte.
- Vous pouvez supposer que toutes les clés seront des entiers positifs :
    - Il peut y avoir des clés qui n'ont pas de boîtes.
- La première boîte `boxes[0]` est déverrouillée.
- Retourne `True` si toutes les boîtes peuvent être ouvertes, sinon retourne `False`.

```
carrie@ubuntu:~/lockboxes$ cat 0-main.py
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

carrie@ubuntu:~/lockboxes$
```

```
carrie@ubuntu:~/lockboxes$ ./0-main.py
True
True
False
carrie@ubuntu:~/lockboxes$
```

#
**Repo:**
- Répertoire GitHub : `holbertonschool-interview`.
- Dossier : `lockboxes`.
- Fichier : `0-lockboxes.py`.
<hr>
</details>

## 🔨 <span id="technologies">Technologies</span>

<p align="left">
    <img src="https://img.shields.io/badge/PYTHON-3776ab?logo=python&logoColor=white&style=for-the-badge" alt="Badge Python">
</p>

## 📂 <span id="description-des-fichiers">Description des fichiers</span>

| **FICHIER**      | **DESCRIPTION**                                                                |
| :-----------:    | ------------------------------------------------------------------------------ |
| `0-lockboxes.py` | Script Python qui résout le problème des Lockboxes.                            |
| `0-main.py`      | Programme principal d'exemple pour tester la fonction `canUnlockAll` avec différentes entrées. |
| `README.md`      | Le fichier readme que vous êtes en train de lire 😉.                           |

## 💻 <span id="installation_et_utilisation">Installation et utilisation</span>

**Installation :**

1. Clonez ce dépôt :
    - Ouvrez votre terminal préféré.
    - Naviguez jusqu'au répertoire où vous souhaitez cloner le dépôt.
    - Exécutez la commande suivante :

```
git clone https://github.com/alfredgibeau-ahoussinou/holbertonschool-interview.git
```

2. Ouvrez le dépôt que vous venez de cloner.

3. Naviguez jusqu'au répertoire `lockboxes` :

```
cd lockboxes
```

4. Assurez-vous que les fichiers sont exécutables :

```
chmod 777 0-lockboxes.py 0-main.py
```

**Comment utiliser :**

1. Pour tester la fonction, exécutez le fichier `0-main.py` avec la commande suivante :

```
./0-main.py
```

2. Vous pouvez modifier le script `0-main.py` avec vos propres cas de test si vous le souhaitez.

## ♥️ <span id="remerciements">Remerciements</span>

Un grand merci à tous mes camarades de l'école Holberton pour leur aide et leur soutien tout au long de ces projets.

## 👷 <span id="auteurs">Auteurs</span>

**Fabien CHAVONET**
- Github: [@fchavonet](https://github.com/alfredgibeau-ahoussinou)
