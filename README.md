# Heuristics

## Motivation

La solution optimale à un problème d'optimisation ne peut que très rarement
être déterminée en un temps polynomial 1 . Il est donc souvent nécessaire de
trouver des modes de résolution qui fournissent une solution de bonne qualité
dans un laps de temps raisonnable : c'est ce que font les heuristiques. Depuis
une vingtaine d'années, les heuristiques les plus populaires, et également les
plus ecaces, sont des techniques générales, appelées méta-heuristiques, qu'il
s'agit d'adapter à chaque problème particulier. Parmi ces techniques générales,
nous nous pencherons dans ce chapitre sur deux approches ayant clairement
démontré leur utilité dans de nombreux domaines, y compris la gestion des systèmes de production. La première de ces approches, appelée Recherche Locale,
est couramment utilisée depuis plus de 20 ans et comprend, entre autres, la
technique du Recuit Simulé [Kirkpatrick et al., 1983] et la Recherche Taboue
[Glover, 1986]. La deuxième approche, appelée Méthode Évolutive, est plus récente puisqu'elle date du début des années 90. Elle s'est particulièrement faite
connaître par l'intermédiaire des algorithmes génétiques dont l'origine remonte
aux travaux de Holland [Holland, 1975].

##  Problème générale
Soit S un ensemble et soit f une fonction qui associe une valeur f(s) à chaque
élément s ∈ S. L'objectif d'un algorithme d'optimisation est de déterminer un
élément dans S qui minimise la fonction f. En d'autres termes, il s'agit de déterminer s
∗ ∈ S tel que :
f(s
∗
) = min f(s) ∀ s ∈ S
L'ensemble S contient typiquement toutes les solutions d'un problème d'optimisation, et la fonction f correspond alors à l'objectif qu'on tente d'optimiser.
On peut cependant également dénir S comme un ensemble de solutions ne satisfaisant pas nécessairement toutes les contraintes du problème considéré ; les
violations de contraintes sont alors également prises en compte par la fonction
f qui pénalise ces violations
