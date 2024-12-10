from flask import Flask, request, jsonify
import chromadb

app = Flask(__name__)

# Initialize the ChromaDB client and collection
client = chromadb.Client()
collection = client.create_collection("database")

# Adding documents to the collection with corresponding metadata and ids
collection.add(
        documents = [
        "Ce film explore les conflits familiaux et sociaux au sein d'une communauté à travers un récit riche en émotions. Chaque scène dépeint des valeurs culturelles profondes avec une authenticité touchante. Une œuvre incontournable pour comprendre les réalités de la société Ewe.",
        "Une histoire poignante qui explore les luttes quotidiennes des familles africaines. Ce film traduit les subtilités des récits nigérians dans un français accessible, tout en préservant leur essence culturelle. Idéal pour découvrir les drames humains sous un nouveau jour.",
        "Ce récit puissant évoque la quête d’indépendance et de justice dans une société en transformation. Avec des personnages charismatiques et un scénario bien ficelé, le film explore les notions de liberté et de responsabilité. Une œuvre inspirante qui soulève des questions profondes.",
        "Une comédie béninoise hilarante qui met en scène des situations improbables et des personnages hauts en couleur. À travers son humour, le film aborde des thèmes sociaux importants avec légèreté. Une expérience cinématographique mémorable pour tous les amateurs de rires.",
        "Découvrez l'incroyable duo Pipi et Semako dans une série de mésaventures comiques. Leur maladresse les entraîne dans des situations absurdes, mais toujours pleines de bon sens. Un film qui allie humour et réflexion sociale.",
        "Plongez dans la vie quotidienne de Tanti, un personnage dont la maison devient le théâtre de scènes aussi drôles qu’imprévisibles. Entre disputes, rires et solidarité, ce film capture l'essence de la vie béninoise. Une comédie qui promet un bon moment en famille.",
        "Cette première partie suit les aventures d’un apprenti aux mille caprices. Ses maladresses entraînent des péripéties hilarantes tout en mettant en lumière la relation maître-apprenti. Un mélange parfait d’humour et de leçons de vie.",
        "Le célèbre 'Cerveau Man' revient avec des idées toujours plus folles et des gags à n’en plus finir. Ce film explore les dynamiques entre intelligence et absurdité avec une touche béninoise unique. Préparez-vous à une avalanche de rires.",
        "Dans cette suite, l’histoire prend une tournure encore plus drôle et surprenante. Les personnages, déjà attachants, évoluent dans des situations encore plus rocambolesques. Une comédie rafraîchissante qui reste fidèle à son esprit original.",
        "Ce film explore les mésaventures culinaires d’un personnage maladroit mais attachant. Entre le rire et la réflexion, il montre comment de simples situations peuvent révéler des leçons de vie. Une ode humoristique à la résilience quotidienne.",
        "Une comédie dramatique burkinabè sur les complexités de la recherche d’un partenaire idéal. Le film explore les attentes culturelles et personnelles avec humour et sincérité. Une œuvre qui divertit tout en portant un regard critique sur les relations modernes.",
        "Ce drame épique plonge dans les récits historiques et mythiques du Bénin. Avec des scènes grandioses et des costumes traditionnels, il célèbre le patrimoine culturel. Un film qui captive à travers ses récits riches et visuellement saisissants.",
        "Dans ce deuxième opus, le protagoniste est confronté aux conséquences de ses choix passés. Une intrigue intense mêlée de drames humains et de rédemption. Ce film laisse une impression durable grâce à son message puissant.",
        "Une comédie sociale explorant les défis relationnels avec un ton humoristique et décalé. Les situations absurdes et les dialogues amusants captivent du début à la fin. Un film qui met en lumière les hauts et les bas de la vie quotidienne.",
        "Ce drame captivant débute par une série de mystères qui tiennent en haleine. Les personnages sont confrontés à des dilemmes moraux et des situations imprévues. Une première partie prometteuse qui donne envie de découvrir la suite.",
        "Une satire sociale qui imagine un procès contre le virus qui a bouleversé le monde. Avec humour et intelligence, le film critique les réponses humaines face à la crise. Un mélange unique de comédie et de réflexion.",
        "Ce film aborde des thématiques contemporaines avec une touche béninoise authentique. Les personnages offrent une fenêtre sur les réalités sociales tout en captivant par leurs histoires personnelles. Un drame sincère et engageant.",
        "Une exploration humoristique et critique du comportement des élèves modernes. Ce film met en lumière des situations comiques et parfois absurdes dans le monde scolaire. Idéal pour rire tout en réfléchissant aux enjeux éducatifs actuels.",
        "Un drame mystique qui mélange quête personnelle et croyances traditionnelles. L’histoire de la fille du féticheur est à la fois intrigante et pleine de rebondissements. Un film qui allie spiritualité et divertissement avec brio.",
        "Dans ce deuxième volet, l’humour et les mésaventures atteignent un niveau supérieur. Les personnages affrontent des défis encore plus absurdes, tout en restant attachants et authentiques. Une suite qui promet des éclats de rire sans fin.",
        "Une histoire drôle et touchante où la cuisine devient le théâtre de malentendus hilarants. Ce film célèbre l'art de surmonter les petites catastrophes quotidiennes avec un soupçon de philosophie. Idéal pour ceux qui aiment l'humour simple et sincère.",
        "Ce drame bouleversant explore la rédemption et la justice divine à travers des situations poignantes. Le protagoniste, toujours hanté par ses actes passés, doit faire face à de nouvelles épreuves. Un film fort en émotions, avec une intrigue captivante et un message puissant.",
        "Ce film mystique plonge dans une histoire fascinante de quête et de découverte spirituelle. La fille d’un féticheur se retrouve confrontée à des choix difficiles entre traditions et modernité. Une œuvre captivante qui mêle culture et intrigue avec brio."
    ],


    metadatas = [
              {"name": "Qui cherche, trouve - La Fille du Féticheur"},
              {"name": "La gloire de Dieu"},
              {"name": "La puissance de Toffa"},
              {"name": "Le secret du village"},
              {"name": "L'héritage maudit"},
              {"name": "Le retour du roi"},
              {"name": "La vengeance des dieux"},
              {"name": "Le mystère de la forêt"},
              {"name": "La prophétie oubliée"},
              {"name": "Le combat des titans"},
              {"name": "L'amour interdit"},
              {"name": "La trahison du cœur"},
              {"name": "Le destin des étoiles"},
              {"name": "Le songe d'or"},
              {"name": "La danse des ombres"},
              {"name": "Le chant des sirènes"},
              {"name": "Le souffle du vent"},
              {"name": "La marche des éléphants"},
              {"name": "Le cri de l'aigle"},
              {"name": "La course des lions"},
              {"name": "Le sourire du serpent"},
              {"name": "Le regard du jaguar"},
              {"name": "La griffe du tigre"}
          ],



        ids = ["cL2u000001IfwBEEYaJ6",
                "cL2u000001IfwBEEYaJ7",
                "cL2u000001IfwBEEYaJ8",
                "cL2u000001IfwBEEYaJ9",
                "cL2u000001IfwBEEYaJA",
                "cL2u000001IfwBEEYaJB",
                "cL2u000001IfwBEEYaJC",
                "cL2u000001IfwBEEYaJD",
                "cL2u000001IfwBEEYaJE",
                "cL2u000001IfwBEEYaJF",
                "cL2u000001IfwBEEYaJG",
                "cL2u000001IfwBEEYaJH",
                "cL2u000001IfwBEEYaJI",
                "cL2u000001IfwBEEYaJJ",
                "cL2u000001IfwBEEYaJK",
                "cL2u000001IfwBEEYaJL",
                "cL2u000001IfwBEEYaJM",
                "cL2u000001IfwBEEYaJN",
                "cL2u000001IfwBEEYaJO",
                "cL2u000001IfwBEEYaJP",
                "cL2u000001IfwBEEYaJQ",
                "cL2u000001IfwBEEYaJR",
                "cL2u000001IfwBEEYaJS"]

)



@app.route('/query', methods=['POST'])
def query_collection():
    # Vérifiez l'en-tête Content-Type
    if request.headers.get('Content-Type') != 'application/json':
        return jsonify({'error': 'Content-Type must be application/json'}), 415

    try:
        # Récupération des données de la requête
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid JSON'}), 400

        # Extraction des paramètres
        query_texts = data.get('query_texts', [])
        n_results = data.get('n_results', 3)

        # Requête à la collection
        results = collection.query(query_texts=query_texts, n_results=n_results)

        # Extraire les IDs
        video_ids = results.get('ids', [[]])[0]  # Accéder à la première liste imbriquée
        if not isinstance(video_ids, list):
            video_ids = []  # Gérer le cas où les IDs ne sont pas une liste

        # Retourner les IDs
        return jsonify({'video_ids': video_ids})

    except Exception as e:
        # Gérer les erreurs inattendues
        return jsonify({'error': 'An error occurred', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)