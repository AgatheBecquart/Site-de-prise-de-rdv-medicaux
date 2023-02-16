# Site-de-prise-de-rdv-medicaux

Coach&moi 

* Description :

Coach&moi est un site dédié à la prise de rendez-vous pour les patients du coach en développement personnel EdouardBaert. Il permet également au coach de gérer les rendez-vous en ayant accès à tous les rendez-vous pris par les patients.

* Installation : 

Ne pas oublier d'installer les packages présents dans requirements.txt pour le bon fonctionnement du site. 

* Utilisation

La base de données contient déjà le coach, 3 patients et moi-même en tant que Superuser. 

En créant le site j'ai attribué le rôle de médecin(le coach) directement dans l'administration Django et dans la projection de fournir directement ses codes d'accès au coach avec son interface différente des patients.

Pour la démonstration du site, tous les utilisateurs ont le même mot de passe que je vous ai communiqué. 

Vous pouvez aussi choisir d'effacer la base de données présente et vous mettre dans la peau du superuser en créant un premier user dont on affectera manuellement dans l'administration le rôle de médecin(coach) et par la suite des patients directement sur le site. 