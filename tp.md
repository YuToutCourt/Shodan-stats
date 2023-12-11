# Partie 1

- Explication de la pertinence du mot clé, pourquoi il a été choisi et pourquoi c’est sensible
- Capture d’écran du résultat
- Commentaire sur la capture
- Explication de pourquoi cette IoT ne devrait pas être là
- Conclusion

## Requête 1 

## Explication de la pertinence du mot clé, pourquoi il a été choisi et pourquoi c’est sensible

- Recherche : title:"VNC viewer for Java" open

La recherche avec le mot clé "title:"VNC viewer for Java" open" a été choisie pour identifier les instances ouvertes et accessibles publiquement de visionneurs VNC écrits en Java. Cette requête est sensible car elle pourrait révéler des installations non sécurisées de visionneurs VNC, ce qui pourrait potentiellement exposer des systèmes à des risques de sécurité si des mesures appropriées n'ont pas été prises pour restreindre l'accès.


| <img src="./image/vnc.png"> |
|:--:|
| *Résultat de la recherche "title:"VNC viewer for Java" open".* |

Lien du truc le plus casser : https://www.shodan.io/host/45.79.44.30


## Commentaire sur la capture

La capture révèle la présence de plusieurs `VNC Viewer for Java`. Étrangement Shodan détecte beaucoup de technologies différentes qui reviennent souvent:
- Java
- Ruby
- Php
- SonarQube
- AngualrJS
- Jquery
- Ruby on Rails
- RoundCube Webmail

Surement autre chose de caché derrière tout ça. Ce qui rend la recherche assez floue mais la chose un peu plus critique.

## Explication de pourquoi cette IoT ne devrait pas être là

Il est impératif de restreindre l'accès aux installations de VNC viewer, surtout s'ils sont accessibles publiquement. Des mesures de sécurité appropriées, telles que l'utilisation de mots de passe forts, la limitation des adresses IP autorisées, et l'application de mises à jour régulières, sont nécessaires pour éviter tout accès non autorisé. La présence d'instances ouvertes sans protection adéquate peut potentiellement compromettre la confidentialité et l'intégrité des systèmes.


## Conclusion

La recherche a souligné la nécessité d'une gestion sécurisée des installations de VNC viewer en Java. Il est crucial pour les administrateurs de systèmes de mettre en œuvre des pratiques de sécurité robustes, de restreindre l'accès non autorisé, et de surveiller régulièrement ces installations pour garantir un environnement informatique sûr et protégé.


## Requête 2

## Explication de la pertinence du mot clé, pourquoi il a été choisi et pourquoi c’est sensible

- Recherche : Server: IP Webcam Server 200 OK country:kr

Le mot clé «Server: IP Webcam Server 200 OK country:kr» est pertinent, car il permet de repérer des caméras de surveillance connectées, dont la réponse du serveur est «200 OK». Cela signifie qu'il est possible de se connecter en temps réel à la caméra.

C'est assez sensible car une caméra de surveillance est censée être sécurisée et ne pas être accessible à tout le monde. Le but des caméras de surveillance est d'être utilisé par des personnes de confiance et non par n'importe qui.

| <img src="https://gyazo.com/68634ea88520a9c6dc9a2914058dbd5e.gif"> |
|:--:|
| *Résultat de la recherche "Server: IP Webcam Server 200 OK country:kr". Plusieurs caméras de surveillance sont visibles en KR* |

## Commentaire sur la capture

La capture révèle la présence de caméras de surveillance en Corée du Sud. Il est possible d'accéder au direct des caméras en suivant le lien. Bien entendu, on ne va pas le faire 🙂 On peut voir aussi que ce sont les mêmes marques de caméra qui sont utilisées (On retrouve les mêmes technologies détectées par Shodan).

## Explication de pourquoi cette IoT ne devrait pas être là

Comme mentionné précédemment, une caméra de surveillance est censée être sécurisée et ne pas être accessible à tout le monde. Le but des caméras de surveillance est d'être utilisé par des personnes de confiance et non par n'importe qui. De plus, certaines caméras sont directement installées chez des particuliers. Être filmé à son insu est vraiment creepy.

## Conclusion

Cette exploration des caméras de surveillance souligne le risque que représente leur accessibilité à tout un chacun. Il est impératif de prendre conscience de la nécessité de sécuriser ces dispositifs. L'achat et l'installation de caméras de surveillance doivent être effectués avec précaution, en veillant à protéger la vie privée des individus.


## Requête 3

## Explication de la pertinence du mot clé, pourquoi il a été choisi et pourquoi c’est sensible

- Recherche : http.title:"router" server: nginx 200 OK

Le mot clé «http.title:"router" server: nginx» est pertinent, car il permet de repérer des routeurs dont le serveur est nginx. Ce qui veut dire que le routeur est accessible via un navigateur web (page de connexion ou directement une page de configuration).

C'est assez tragique de voir des routeurs accessible comme ça. On pourrait modifier la configuration du routeur et donc modifier la configuration du réseau.


| <img src="./image/cisco.png"> |
|:--:|
| *Résultat de la recherche "http.title:"router" server: nginx 200 OK". Plusieurs routeurs sont visibles dans divers pays.*

## Commentaire sur la capture

Comme prévu la plus part des routeurs trouver sont des routeurs Cisco. On peut voir que les routeurs sont accessible via un navigateur web. Et sont tous sur nginx. 


## Explication de pourquoi cette IoT ne devrait pas être là

Un routeur est un élément essentiel dans un réseau. Déjà cela augement les risques de se faire attaquer. Les fabriquants de routeurs font des mises à jour pour corriger les failles de sécurité. Mais si les utilisateurs ne font pas les mises à jour, les routeurs sont vulnérables.

## Conclusion

Cette investigation sur les routeurs met en lumière la vulnérabilité potentielle des réseaux domestiques ou pro. Il est crucial que les utilisateurs comprennent l'importance des mises à jour de sécurité pour les routeurs, renforçant ainsi la protection de leurs réseaux contre les attaques. Acheter et installer des routeurs doit s'accompagner d'une vigilance constante en matière de sécurité.

## Requête 4 


## Explication de la pertinence du mot clé, pourquoi il a été choisi et pourquoi c’est sensible

- Recherche : Server: gSOAP/2.8 200 OK

Comme la recherche de base gSOAP/2.8 donnée beaucoup de résultat avec des réponse 401 Unauthorized, j'ai décidé de rajouter 200 OK pour avoir des résultats plus pertinents. Car cela veut dire que la plus sont accessible sans mot de passe. De plus la version gSOAP.2.8 à un directory traversal vulnérability. 

Lien : https://www.exploit-db.com/exploits/47653

Ce qui est sensible est que l'on peut trouver des versions de gSOAP qui sont encore vulnérable. 


| <img src="./image/gsoap.png"> |
|:--:|
| *Résultat de la recherche "Server: gSOAP/2.8 200 OK".*

## Commentaire sur la capture

On peut voir que le premier et troisième résultat sont des caméras de surveillance.
Le deuxième résultat est assez flou. Par contre le 4ème résultat et le 5ème (qu'on voit pas trop) ne font pas du tout partie de ce qui est recherché. A cause de la recherche 200 OK cela inclus aussi des résultat qui utilise pas gSOAP.2.8.

## Explication de pourquoi cette IoT ne devrait pas être là

Comme dit au dessus, la version gSOAP.2.8 à un directory traversal vulnérability. Ce qui veut dire que l'on peut accéder à des fichiers qui ne sont pas censé être accessible. On peut donc accéder à des fichiers sensibles.

## Conclusion

Cette exploration des caméras et autres dispositifs utilisant gSOAP/2.8 souligne la persistance des vulnérabilités, même avec des versions plus anciennes. Il est crucial de rester informé sur les mises à jour de sécurité et d'éviter l'utilisation de versions obsolètes. La sécurité des dispositifs connectés dépend directement de la vigilance des utilisateurs dans le choix et la maintenance de leurs équipements.


## Requête 5

## Explication de la pertinence du mot clé, pourquoi il a été choisi et pourquoi c’est sensible

- Recherche : title:"Epson" "port:80" country:fr

Le but de cette recherche est de trouver des imprimantes Epson en France qui sont accessible via un navigateur web. C'est assez sensible car on peut modifier la configuration de l'imprimante. On peut aussi voir les documents qui ont été imprimé.

|<img src="./image/printer.png">|
|:--:|
| *Résultat de la recherche "title:"Epson" "port:80" country:fr". Plusieurs imprimantes sont visibles en France.* |


## Commentaire sur la capture

On peut voir seulement 4 imprimantes de la marque EPSON en France. Les 2 dernières ont CONNECTION : close, ce qui réduit bien le nombre d'imprimente EPSON accessible en France à 2.


## Explication de pourquoi cette IoT ne devrait pas être là

Une imprimante est souvent connecter au réseau d'une maison ou d'une boite et donc accessible par plusieurs personnes. Si une personne malveillante arrive à accéder à l'imprimante, elle peut modifier la configuration de l'imprimante ou même devenir domain admin.

## Conclusion

L'accès non sécurisé à une imprimante pourrait permettre des intrusions malveillantes, compromettant ainsi la confidentialité et la sécurité des informations. Les utilisateurs d'imprimantes doivent prendre des mesures pour renforcer la sécurité de ces dispositifs, en modifiant les mots de passe par défaut et en restreignant l'accès aux seules personnes autorisées. La vigilance dans la gestion de la sécurité des périphériques connectés est essentielle pour éviter les compromissions indésirables.


## Requête 6 

## Explication de la pertinence du mot clé, pourquoi il a été choisi et pourquoi c’est sensible

- Recherche : «bulb last-modified»

Le mot clé «bulb» est pertinent car il désigne une ampoule connectée. Sa sensibilité réside dans la possibilité de repérer des ampoules connectées vulnérables aux attaques, surtout lorsque les utilisateurs négligent de modifier les mots de passe par défaut.

Le mot clé «last-modified» est pertinent car il permet d'identifier des objets connectés ayant récemment subi des modifications.


| <img src="./image/bulb.png"> |
|:--:|
| *Résultat de la recherche "bulb last-modified". Plusieurs ampoules connectées sont visibles dans divers pays.* |

## Commentaire sur la capture

La capture révèle la présence d'ampoules connectées dans plusieurs pays. Il est possible d'accéder à la page de connexion en suivant le lien. Bien entendu, cela nécessite un mot de passe et un identifiant, mais de nombreux utilisateurs ne changent pas le mot de passe par défaut. Ainsi, il serait envisageable de prendre le contrôle de l'ampoule.

## Explication de pourquoi cette IoT ne devrait pas être là

La possibilité de contrôler l'éclairage d'une maison à l'insu de ses occupants est une menace sérieuse. Elle pourrait entraîner la surchauffe de l'ampoule, voire sa destruction, et augmenter de manière significative la facture d'électricité. Payer une somme importante pour une simple ampoule serait regrettable.

## Conclusion

En résumé, cette recherche met en évidence la vulnérabilité des ampoules connectées, exposant le risque potentiel de manipulation à distance. Il est crucial que les utilisateurs prennent conscience de cette menace, modifient les mots de passe par défaut et n'exposent pas en ligne des objets connectés sans protection, garantissant ainsi la sécurité de leur domicile.


## Requête 7

## Explication de la pertinence du mot clé, pourquoi il a été choisi et pourquoi c’est sensible

- Recherche : "title:voice assistant"

Le mot clé «voice assistant» est pertinent car il permet de repérer des assistants vocaux connectés, tels que Google Home ou Alexa. Et voulant ajouter plus de filtre la recherche devenait pas pertinente. On avait plus de résultat correspondant à ce que l'on voulait.
La sensibilité réside dans la possibilité de repérer des assistants vocaux connectés vulnérables aux attaques, surtout lorsque les utilisateurs négligent de modifier les mots de passe par défaut.

| <img src="./image/voice.png"> |
|:--:|
| *Résultat de la recherche "title:voice assistant". Plusieurs assistants vocaux connectés sont visibles dans divers pays.* |

## Commentaire sur la capture

On peut voir des choses plutôt sympa ici 👀
Premier résultat : `Say It Now - Award Winning Voice Assistant Advertising with Alexa`
Et une entreprise qui à compris le principe de Shodan et qui a mis en place une campagne de pub. C'est assez drôle. On est redirigé vers un site web de leur assistant vocal. **https://sayitnow.ai/**

| <img src="./image/pub.png"> |
|:--:|
| *Preuve de la redirection* |

Le 3ème résultat est aussi une redirection vers le site de l'assistant vocal. Mais il y a d'autre port HTTP qui sont ouvert et qui ne font pas de redirection. C'est difficile de savoir si c'est vraiment une campagne de pub ou si c'est un assistant vocal qui est mal configuré. 

Par contre le deuxième résultat pas de doute possible. C'est un assistant vocal qui est mal configuré.


## Explication de pourquoi cette IoT ne devrait pas être là

La présence d'assistants vocaux accessibles publiquement peut présenter des risques pour la vie privée des utilisateurs. Ces dispositifs sont souvent conçus pour interagir avec des données personnelles, et leur exposition pourrait potentiellement permettre des accès non autorisés à des informations sensibles. En conséquence, il est crucial de restreindre l'accès à ces dispositifs pour garantir la confidentialité des utilisateurs.



## Conclusion

Cette recherche souligne la sensibilité de la présence d'assistants vocaux accessibles en ligne. Il est impératif de mettre en œuvre des mesures de sécurité robustes pour ces dispositifs, en restreignant l'accès et en appliquant des pratiques de sécurité adéquates. Les utilisateurs et les administrateurs doivent être conscients des risques potentiels liés à l'exposition des assistants vocaux et prendre les mesures nécessaires pour protéger la vie privée et la sécurité des données.


## Requête 8

## Explication de la pertinence du mot clé, pourquoi il a été choisi et pourquoi c’est sensible





# Partie 2 : Automatisation de la Recherche avec un Script Python

TODO : Développez un Script Python pour automatiser la Recherche :

- Utilisez la librairie Shodan pour créer un script qui automatise les recherches de mots-clés.

- Le script doit pouvoir saisir des mots-clés, exécuter la recherche et enregistrer les résultats dans un fichier.

- Utilisez une lib python de visualisation statistique, comme matplotlib ou seaborn, pour créer des graphiques représentant les données recueillies. (les marques, les ports ouverts, et toues les infro(s) importtantes)
Bonne chance ! Merci !!


Lien du git: https://github.com/YuToutCourt/Shodan-stats/blob/main/tp.md