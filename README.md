# Django Project

Rendu de la semaine de découverte de Django

Projet développéà l'aide de Django et PostgreSQL

Groupe: Léo Gourvès et Nicolas Boudier


# Le projet

Nous sommes partis d'un template simple de site vitrine auquel nous avons ajouté plusieurs fonctionnalités.

Nous avons dans un premiers temps changé le contenu du site pour en faire un site factice d'une entreprise vendant différents composants de 
serveurs physiques. Ce site avait aussi besoin de déployer du contenu en rapport avec son activité afin d'augmenter
son engagement (partie blog). 


Les fonctionnalités principales ajoutées sont donc:
1. Une partie blog
1. Un formulaire de contact
1. Un dépot de fichier pour l'upload des CV


### Le blog
On peut ajouter des nouveaux articles depuis l'admin

Les utilisateurs peuvent commenter ces articles

Une gestion des articles et des commentaires est possible depuis l'administration (ajout de nouveaux articles, suppression, 
validation des commentaires pour l'affichage en front, publication des articles etc)

### Le formulaire de contact

Accessible depuis la page contact

Le formulaire permet d'enregistrer l'email de l'utilisateur. Ces emails sont ensuite visible et accessible dans l'admin

### Le dépôt de fichier

Accessible depuis la page about. L'utilisateur peut déposer un fichier pdf qui sera ensuite accessible depuis l'admin de Django

