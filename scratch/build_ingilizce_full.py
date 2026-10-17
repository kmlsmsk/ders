# -*- coding: utf-8 -*-
"""
Comprehensive 36-week generator for İngilizce (Grades 5 Maarif, 6, 7, 8 LGS).
Generates lib/data/subjects/ingilizce_data.dart with full details.
"""
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from curriculum_builder import generate_dart_file

def _make_weeks(raw_units, prefix):
    weeks = []
    for i, u in enumerate(raw_units):
        code = f"{prefix}.{i+1}"
        theme, sub, title, desc, conc, ped, q, a = u
        weeks.append({
            'theme': theme,
            'subTheme': sub,
            'code': code,
            'title': title,
            'description': desc,
            'process': [
                f"a) Students understand and practice: {desc[:45]}.",
                f"b) Communicates using key structures and vocabulary of {sub}.",
                "c) Practices listening, speaking, reading, and writing skills interactively."
            ],
            'concepts': conc,
            'skills': ['Communication', 'Critical Thinking', 'Language Fluency', 'Global Citizenship'],
            'pedagogical': ped,
            'context': 'İngilizce (English Language)',
            'question': q,
            'solution': a,
            'weeklyGoal': f"Mastering {title} vocabulary and language functions",
            'evaluation': 'Haftalık İngilizce kelime ve beceri değerlendirme föyü'
        })
    return weeks

def get_eng_5():
    # 5. Sınıf - Türkiye Yüzyılı Maarif Modeli / MEB İngilizce (10 Ünite - Tam 36 Hafta)
    u = [
        # Unit 1: Hello! (1-4)
        ("Hello!", "Greetings and Introductions", "Meeting People and Introducing Yourself",
         "Students greet each other, introduce themselves and state their names, ages, and countries.",
         ["Greetings", "Countries", "Nationalities", "Introductions"],
         "Pair-work role play dialogues are conducted in the classroom.",
         "How do you introduce yourself and state where you are from in English?",
         "'Hello, my name is Kemal. I am 11 years old and I am from Türkiye.'"),
        
        ("Hello!", "Nationalities and Languages", "Countries, Nationalities and Languages",
         "Students express nationalities and the languages they can speak using appropriate grammar.",
         ["Turkish", "English", "Flags", "Languages"],
         "Country flag flashcards and map matching activities are performed.",
         "Which sentence correctly shows nationality and language spoken?",
         "'I am from Germany; I am German and I speak German and English.'"),
        
        ("Hello!", "School Subjects and Timetable", "Favorite Classes and School Timetable",
         "Students talk about school subjects (Maths, Science, Art, PE, Music) and their weekly schedule.",
         ["Maths", "Science", "Timetable", "Favorites"],
         "Students draw and describe their dream weekly school schedule in English.",
         "How do you express your favorite school subject?",
         "'My favorite school subject is Science because I love doing experiments.'"),
        
        ("Hello!", "Likes and Dislikes in School", "Expressing Likes and Dislikes with School Subjects",
         "Students express what classes they like, love, or dislike using simple present structures.",
         ["Like", "Dislike", "Love", "Hate"],
         "Survey activity: finding out classmates' favorite subjects.",
         "Complete: 'I _____ Art, but I _____ History.'",
         "'I like/love Art, but I dislike/hate History.'"),

        # Unit 2: My Town (5-7)
        ("My Town", "Places in Town", "City Locations: Library, Bakery, Hospital, Park",
         "Students identify and name public places and buildings located in their neighbourhood.",
         ["Bakery", "Pharmacy", "Library", "Supermarket"],
         "Interactive 3D town map design and labeling activity.",
         "Where do you go when you need to buy medicine in town?",
         "You go to the pharmacy (chemist's)."),
        
        ("My Town", "Prepositions of Place", "Next to, Between, Opposite, Behind, In front of",
         "Students describe the relative position of buildings using location prepositions accurately.",
         ["Prepositions", "Next to", "Between", "Opposite"],
         "Location guessing game based on grid maps.",
         "If the bank is between the hospital and the cafe, where is the bank located?",
         "'The bank is right in the middle, between the hospital and the cafe.'"),
        
        ("My Town", "Giving Directions", "Asking for and Giving Directions: Turn Left, Go Straight",
         "Students ask for directions and guide visitors to destinations using imperative phrases.",
         ["Turn Left", "Turn Right", "Go Straight Ahead", "Directions"],
         "Role-play: Tourist asking a local for directions to the museum.",
         "How do you ask for directions to the nearest library politely?",
         "'Excuse me, could you tell me how to get to the public library, please?'"),

        # Unit 3: Games and Hobbies (8-10)
        ("Games and Hobbies", "Indoor and Outdoor Games", "Board Games, Tag, Hopscotch, Blind Man's Buff",
         "Students name traditional and modern games played with friends and peers.",
         ["Hopscotch", "Dodgeball", "Chess", "Origami"],
         "Cultural comparison of Turkish and British children's playground games.",
         "Which game is played with a folded paper art technique?",
         "Origami is the Japanese art of paper folding."),
        
        ("Ara Tatil", "1. Dönem Ara Tatil Kampı", "English Autumn Camp: Vocabulary & Dialogue",
         "Students consolidate vocabulary from Units 1-3 through vocabulary bingo and reading puzzles.",
         ["Revision", "Camp", "Vocabulary", "Fluency"],
         "Interactive digital flashcards and crosswords are reviewed.",
         "What is the antonym of 'turn right' in giving directions?",
         "The antonym is 'turn left'."),
        
        ("Games and Hobbies", "Expressing Abilities: Can / Can't", "Talking About Abilities and Talents",
         "Students express physical and creative abilities using modal verb 'can' and 'can't'.",
         ["Can", "Can't", "Abilities", "Talents"],
         "Talent show interview in pairs: finding out what partners can do.",
         "Complete the question and short answer: '_____ you play chess?' - 'Yes, I _____.'",
         "'Can you play chess?' - 'Yes, I can.'"),

        # Unit 4: My Daily Routine (11-14)
        ("My Daily Routine", "Daily Activities and Habits", "Morning, Afternoon and Evening Routines",
         "Students describe daily recurring actions (wake up, brush teeth, have breakfast, catch bus).",
         ["Daily Routine", "Wake up", "Brush teeth", "Get dressed"],
         "Creating a daily routine comic strip storyboard.",
         "Which activity happens first in the morning routine?",
         "'First, I wake up and wash my face, then I get dressed.'"),
        
        ("My Daily Routine", "Telling the Time", "O'clock, Half past, Quarter past, Quarter to",
         "Students read digital and analog clocks and tell the time accurately in English.",
         ["Time", "Quarter past", "Half past", "Quarter to"],
         "Clock face manipulative practice and schedule synchronization.",
         "What is the British English way to say 07:45?",
         "'It is quarter to eight in the morning.'"),
        
        ("My Daily Routine", "Simple Present Tense with Routines", "He/She/It -s / -es Rules and Daily Life",
         "Students formulate affirmative, negative and interrogative sentences for third-person routines.",
         ["Simple Present", "Third person -s", "Does/Doesn't", "Habits"],
         "Spot-the-mistake grammar challenges on sentence strips.",
         "Correct the sentence: 'My brother go to school at 8 o'clock.'",
         "'My brother goes to school at 8 o'clock.'"),
        
        ("My Daily Routine", "Sequencing Words: First, Then, After that", "Organizing Daily Narrative Paragraphs",
         "Students write a short coherent paragraph about their Sunday routine using linkers.",
         ["First", "Then", "After that", "Finally"],
         "Writing peer-review workshop with descriptive rubric.",
         "Which linking word is used to conclude a sequence of steps?",
         "'Finally' or 'Lastly' is used to conclude."),

        # Unit 5: Health (15-18)
        ("Health", "Illnesses and Symptoms", "Headache, Toothache, Sore Throat, Fever, Cough",
         "Students identify and express common physical ailments and symptoms.",
         ["Health", "Fever", "Headache", "Cough", "Cold"],
         "Doctor and patient simulation clinic in the classroom.",
         "How do you tell a doctor that you have pain in your ear?",
         "'I have an earache and I feel dizzy.'"),
        
        ("Health", "Giving Advice: Should / Shouldn't", "Health Recommendations and Remedies",
         "Students give practical health advice using modal verbs 'should' and 'shouldn't'.",
         ["Should", "Shouldn't", "Rest", "Remedies"],
         "Matching illnesses with proper remedies and doctor prescriptions.",
         "What advice do you give to someone who has a high fever?",
         "'You should see a doctor and take medicine; you shouldn't go outside.'"),
        
        ("Health", "1. Dönem Sonu Sentezi", "Mid-Year English Proficiency Assessment",
         "Students synthesize Units 1-5 with an integrated reading and listening task.",
         ["Synthesis", "Assessment", "Skills", "Fluency"],
         "Mini-CEFR A1 reading comprehension and vocabulary test.",
         "What does a pharmacist do when you give them a prescription?",
         "The pharmacist gives you the appropriate medicine."),
        
        ("Health", "1. Dönem Sonu Karne ve Tatil", "Winter Reading & Movie Watchlist",
         "Students prepare a personalized English winter reading log and movie review plan.",
         ["Portfolio", "Self-Assessment", "Reading Log", "Holiday"],
         "English subtitle animation viewing guidelines are explained.",
         "Why is reading English stories beneficial during winter break?",
         "It expands vocabulary and strengthens grammar in real context."),

        # Unit 6: Movies (19-21)
        ("Movies", "Movie Types and Genres", "Animation, Comedy, Sci-Fi, Adventure, Horror",
         "Students describe genres of films and name popular movies representing each category.",
         ["Movies", "Animation", "Sci-Fi", "Comedy", "Genre"],
         "Film trailer analysis and movie poster creation.",
         "What genre is a movie about space travel and futuristic robots?",
         "It is a Science Fiction (Sci-Fi) movie."),
        
        ("Movies", "Expressing Opinions on Films", "Adjectives: Exciting, Boring, Funny, Scary",
         "Students critique movies and express personal impressions with descriptive adjectives.",
         ["Exciting", "Boring", "Frightening", "Pleasant"],
         "Movie review star-rating cards and short spoken presentations.",
         "How do you say that an animated film made you laugh a lot?",
         "'It was hilarious and very funny; I loved every scene.'"),
        
        ("Movies", "Movie Characters and Plot", "Bravery, Villains and Superheroes",
         "Students describe qualities of movie characters using adjectives (brave, strong, clever).",
         ["Characters", "Superhero", "Villain", "Plot"],
         "Character trait Venn diagrams and comparison charts.",
         "Which adjective describes a character who is not afraid of danger?",
         "The character is 'brave' or 'courageous'."),

        # Unit 7: Party Time (22-25)
        ("Party Time", "Months, Days and Ordinal Numbers", "Calendar, Birthdays and Dates",
         "Students name the 12 months, ordinal numbers (1st to 31st) and state their birthdates.",
         ["Months", "Ordinal Numbers", "Birthdays", "Calendar"],
         "Birthday timeline classroom wall chart construction.",
         "How do you write and say the date: 15 October?",
         "'The fifteenth of October' (15th of October)."),
        
        ("Party Time", "Party Preparations and Needs", "Invitations, Candles, Balloons, Cake, Confetti",
         "Students prepare shopping lists and party supplies for a birthday celebration.",
         ["Party Supplies", "Candles", "Invitation Card", "Decorations"],
         "Designing and writing an authentic birthday party invitation card.",
         "What essential details must an invitation card contain?",
         "The date, time, venue (location) and RSVP contact information."),
        
        ("Party Time", "Asking for Permission: Can / May I?", "Polite Requests and Offers",
         "Students use polite language to ask for permission and offer assistance at gatherings.",
         ["May I", "Can I", "Permission", "Politeness"],
         "Polite interaction scenarios at social events.",
         "How do you politely ask for permission to open the window?",
         "'May I open the window, please?'"),
        
        ("Ara Tatil", "2. Dönem Ara Tatil Kampı", "Spring English Language Camp",
         "Students reinforce grammar and vocabulary from Units 6-7 with communicative tasks.",
         ["Camp", "Spring Break", "Consolidation", "Games"],
         "Gamified vocabulary tournaments and dialogue challenges.",
         "What is the correct response to 'May I borrow your ruler?'",
         "'Sure, here you are!' or 'I'm sorry, I am using it right now.'"),

        # Unit 8: Fitness (26-28)
        ("Fitness", "Sports and Outdoor Activities", "Cycling, Swimming, Hiking, Jogging, Gymnastics",
         "Students name various fitness activities and sports using play, go, or do appropriately.",
         ["Cycling", "Gymnastics", "Play/Go/Do", "Fitness"],
         "Collocation rules: 'play football', 'go swimming', 'do gymnastics'.",
         "Which verb is used with gerund (-ing) sports like skiing and cycling?",
         "The verb 'go' is used (e.g., 'go cycling', 'go swimming')."),
        
        ("Fitness", "Making Suggestions: Let's / How about", "Proposing Sports and Fitness Activities",
         "Students make, accept, and decline suggestions for weekend sporting events.",
         ["Let's", "How about", "Why don't we", "Suggestions"],
         "Interactive planning of a class sports day weekend tournament.",
         "How do you invite a friend to play basketball using 'Let's'?",
         "'Let's go to the court and play basketball together!'"),
        
        ("Fitness", "Healthy Habits and Lifestyle", "Nutritious Food and Staying Active",
         "Students explain the benefits of regular physical activity and balanced diet.",
         ["Hydration", "Balanced Diet", "Active Life", "Energy"],
         "Creating a bilingual healthy lifestyle infographic poster.",
         "Why is drinking plenty of water important for young athletes?",
         "It keeps the body hydrated, prevents cramps and maintains high energy levels."),

        # Unit 9: The Animal Shelter (29-32)
        ("The Animal Shelter", "Shelter Animals and Wildlife", "Puppies, Kittens, Birds, Shelter Rules",
         "Students name domestic and rescued animals and understand responsible animal care.",
         ["Animal Shelter", "Puppy", "Adoption", "Veterinarian"],
         "Virtual tour of a modern humane animal adoption center.",
         "What should people do instead of buying pets from shops?",
         "They should adopt rescued pets from animal shelters."),
        
        ("The Animal Shelter", "Describing Current Actions: Present Continuous", "Actions Happening Right Now (Am/Is/Are + -ing)",
         "Students formulate sentences describing ongoing actions observed in pictures.",
         ["Present Continuous", "Verb + -ing", "Now", "At the moment"],
         "Action mime game: students guess what their classmate is doing.",
         "Complete: 'The vet _____ (examine) the injured puppy right now.'",
         "'The vet is examining the injured puppy right now.'"),
        
        ("The Animal Shelter", "Rules and Responsibilities at the Shelter", "Don't feed, Walk the dog, Clean cages",
         "Students express imperative commands and guidelines for visiting animal sanctuaries.",
         ["Imperatives", "Rules", "Feed the birds", "Care"],
         "Writing safety guidelines for visitors at the local zoo and shelter.",
         "What does a 'Do not feed the animals' sign mean?",
         "It means visitors must not give any snacks to the animals for their health."),
        
        ("The Animal Shelter", "Animal Protection and Welfare", "Protecting Street Animals and Kindness",
         "Students discuss putting out bowls of water and food during hot and cold seasons.",
         ["Kindness", "Street Animals", "Water bowl", "Empathy"],
         "Project: Building birdhouses and cat shelters from recycled materials.",
         "How can students help stray animals during winter months?",
         "By leaving dry food and warm sheltered boxes in safe spots."),

        # Unit 10: Festivals (33-36)
        ("Festivals", "National and Religious Festivals", "Children's Day, Republic Day, Ramadan Feast",
         "Students talk about Turkish national and religious celebrations and their cultural value.",
         ["Festivals", "Republic Day", "Children's Day", "Celebration"],
         "International student exchange simulation sharing national holidays.",
         "When do Turkish children celebrate National Sovereignty and Children's Day?",
         "On the 23rd of April every year."),
        
        ("Festivals", "Numbers up to 1000", "Hundred, Thousand and Counting Large Quantities",
         "Students pronounce, write and read cardinal numbers between 100 and 1000 in English.",
         ["Numbers", "Hundred", "Thousand", "Counting"],
         "Large numbers bingo tournament and mathematical word problems.",
         "How do you write the number 785 in English words?",
         "'Seven hundred and eighty-five.'"),
        
        ("Festivals", "Festival Activities and Traditions", "Parades, Costumes, Fireworks and Poems",
         "Students describe cultural rituals: marching in parades, reciting poems, visiting relatives.",
         ["Parades", "Costumes", "Poems", "Traditions"],
         "Reciting a short celebratory poem in English.",
         "What do students do in schools on Turkish Republic Day?",
         "They decorate classes with flags, sing national anthems and recite patriotic poems."),
        
        ("Festivals", "Maarif Modeli English Portfolio Sentezi", "Year-End English Exhibition & Showcase",
         "Students present their comprehensive CEFR A1 portfolio with speaking and writing tasks.",
         ["Portfolio", "Maarif Modeli", "CEFR A1", "Graduation"],
         "Interactive speaking showcase and language certificate ceremony.",
         "What is the ultimate goal of learning English in middle school?",
         "To communicate fluently, bridge cultures, and access global scientific knowledge.")
    ]
    assert len(u) == 36, f"Eng 5 count: {len(u)}"
    return {
        'title': '5. Sınıf',
        'subtitle': 'Türkiye Yüzyılı Maarif Modeli (10 Ünite)',
        'badge': 'Maarif Modeli ✨',
        'weeks': _make_weeks(u, 'İNG.5')
    }

def get_eng_6():
    # 6. Sınıf MEB İngilizce (10 Ünite - Tam 36 Hafta)
    u = [
        # Unit 1: Life (1-4)
        ("Life", "After-School Activities", "Daily Routines, Clubs and Hobbies",
         "Students talk about daily routines, after-school activities, and hobbies.",
         ["After-School", "Drama Club", "Folk Dance", "Routine"],
         "Creating a personalized after-school weekly diary.",
         "Which after-school activity helps improve stage acting skills?",
         "Joining the drama club."),
        
        ("Life", "Telling Dates and Time", "Ordinal Numbers and Calendar Expressions",
         "Students ask for and state dates, birthdays and special calendar events accurately.",
         ["Dates", "First of May", "Clock", "Calendar"],
         "Calendar role-play arranging weekend study sessions.",
         "How do you read '19 May 1919' in English?",
         "'The nineteenth of May, nineteen nineteen.'"),
        
        ("Life", "Simple Present Tense Review", "Habitual Actions and Adverbs of Frequency",
         "Students use always, usually, often, sometimes, never to express frequency of actions.",
         ["Frequency Adverbs", "Always", "Usually", "Never"],
         "Frequency questionnaire: analyzing daily habits with bar graphs.",
         "Where is the adverb of frequency placed in a sentence with an ordinary verb?",
         "Before the main verb (e.g., 'I always do my homework before dinner')."),
        
        ("Life", "Traditional Games vs Digital Games", "Outdoor Play and Leisure Habits",
         "Students compare past and modern playground activities in spoken paragraphs.",
         ["Outdoor Games", "Tag", "Video Games", "Comparison"],
         "Debate: Are outdoor sports healthier than digital gaming?",
         "What is a healthy balance between computer games and sports?",
         "Limiting screen time and engaging in outdoor physical activity daily."),

        # Unit 2: Yummy Breakfast (5-7)
        ("Yummy Breakfast", "Breakfast Food and Drinks", "Cheese, Olives, Honey, Bagel (Simit), Eggs, Tea",
         "Students name traditional Turkish and international breakfast items accurately.",
         ["Breakfast", "Simit", "Cheese", "Olives", "Pancakes"],
         "Designing an authentic Turkish village breakfast menu in English.",
         "Which breakfast pastry with sesame seeds is famous in Türkiye?",
         "Turkish bagel, known as 'simit'."),
        
        ("Yummy Breakfast", "Expressing Likes, Dislikes and Preferences", "I prefer croissants to bagels",
         "Students express food preferences using like, love, hate, enjoy, and prefer.",
         ["Preferences", "Prefer", "Like/Dislike", "Delicious"],
         "Class breakfast preference tally chart and dialogue role-play.",
         "Complete: 'I prefer drinking orange juice _____ drinking fizzy soda.'",
         "'I prefer drinking orange juice to drinking fizzy soda.'"),
        
        ("Yummy Breakfast", "Nutritious vs Junk Food", "Healthy Breakfast for High Energy",
         "Students distinguish healthy nutritious breakfast foods from processed junk snacks.",
         ["Nutritious", "Junk Food", "Cereals", "Healthy Diet"],
         "Nutritionist consultation simulation giving diet recommendations.",
         "Why is skipping breakfast bad for school students?",
         "It lowers energy levels, causes poor concentration and leads to unhealthy snacking."),

        # Unit 3: Downtown (8-10)
        ("Downtown", "City Life vs Country Life", "Skyscrapers, Traffic Jam, Green Fields, Fresh Air",
         "Students compare living in a busy downtown city with living in a quiet village.",
         ["Downtown", "Country", "Traffic Jam", "Skyscraper"],
         "T-chart comparing noise, pollution, transport, and fresh food.",
         "What is the main advantage of living in the countryside?",
         "Clean fresh air, quiet nature, and peaceful surroundings."),
        
        ("Ara Tatil", "1. Dönem Ara Tatil Kampı", "Vocabulary Mastery & Reading Fluency",
         "Students review vocabulary from Units 1-3 through reading puzzles and grammar games.",
         ["Consolidation", "Vocabulary", "Reading", "Camp"],
         "Interactive reading comprehension race.",
         "What is the comparative form of the adjective 'crowded'?",
         "'More crowded than'."),
        
        ("Downtown", "Comparative Adjectives", "Bigger, Busier, More expensive, Quieter",
         "Students apply rules of comparative adjectives (-er than, more ... than, irregulars).",
         ["Comparatives", "Bigger than", "More modern", "Better"],
         "Comparing Istanbul and Ankara using comparative sentences.",
         "Form comparative sentences: 'A city is _____ (crowded) than a small village.'",
         "'A city is more crowded than a small village.'"),

        # Unit 4: Weather and Emotions (11-14)
        ("Weather and Emotions", "Weather Conditions and Temperature", "Freezing, Stormy, Rainy, Hail, Celsius",
         "Students describe weather conditions, seasons, and read Celsius thermometers.",
         ["Weather", "Freezing", "Lightning", "Thermometer"],
         "National weather forecast presentation with satellite maps.",
         "How do you describe weather when the temperature is -5 degrees Celsius?",
         "'It is freezing cold and snowy outside.'"),
        
        ("Weather and Emotions", "Feelings and Moods", "Happy, Depressed, Energetic, Scared, Anxious",
         "Students describe how different weather conditions influence human mood and feelings.",
         ["Emotions", "Moody", "Energetic", "Anxious", "Feelings"],
         "Psychological weather-mood correlation matching game.",
         "How do people usually feel on warm, sunny spring mornings?",
         "They usually feel cheerful, happy, and energetic."),
        
        ("Weather and Emotions", "Expressing Emotions: Feel / Sound", "I feel sleepy on rainy days",
         "Students formulate sentences expressing emotions using feel + adjective structures.",
         ["Feelings", "Feel sleepy", "Thunder", "Scared"],
         "Diary entry describing feelings during a massive thunderstorm.",
         "Complete: 'When I hear loud thunder, I feel _____.'",
         "'When I hear loud thunder, I feel frightened/scared.'"),
        
        ("Weather and Emotions", "Weather Safety and Precautions", "Storm Warnings and Dressing Appropriately",
         "Students discuss taking precautions during extreme weather phenomena.",
         ["Precautions", "Umbrella", "Coat", "Safety"],
         "Safety checklist for blizzards and heatwaves.",
         "What should you take with you when the forecast predicts heavy rain?",
         "You should take an umbrella and wear a waterproof raincoat."),

        # Unit 5: At the Fair (15-18)
        ("At the Fair", "Carnival and Fair Rides", "Ferris Wheel, Roller Coaster, Bumper Cars, Ghost Train",
         "Students name amusement park attractions and fairground rides accurately.",
         ["Amusement Park", "Ferris Wheel", "Roller Coaster", "Bumper Cars"],
         "Designing a dream theme park with map legends and ride descriptions.",
         "Which fairground ride spins slowly and gives a panoramic view of the whole city?",
         "The Ferris Wheel (Big Wheel)."),
        
        ("At the Fair", "Expressing Opinions on Rides", "Thrilling, Terrifying, Amazing, Boring",
         "Students express their personal impressions about various rides using strong adjectives.",
         ["Thrilling", "Terrifying", "Exciting", "Adjectives"],
         "Fair survey: which ride is the most popular in class?",
         "Which ride is suitable for people who love speed and loop-the-loops?",
         "The Roller Coaster."),
        
        ("At the Fair", "1. Dönem Sonu Sentezi", "Mid-Year Comprehensive English Review",
         "Students integrate grammar and vocabulary from Units 1-5 through mock tests.",
         ["Synthesis", "Assessment", "Skills", "Grammar"],
         "Reading comprehension and error correction workshop.",
         "What is the comparative form of 'dangerous'?",
         "'More dangerous than'."),
        
        ("At the Fair", "1. Dönem Sonu Karne", "Winter Reading & Vocabulary Challenge",
         "Students receive semester performance feedback and set holiday reading goals.",
         ["Report", "Winter Goal", "Reading", "Vocabulary"],
         "Providing graded readers recommendations.",
         "How does reading graded English readers help improve vocabulary?",
         "It exposes the brain to target words multiple times in natural sentences."),

        # Unit 6: Occupations (19-21)
        ("Occupations", "Professions and Workplaces", "Architect, Engineer, Lawyer, Vet, Tailor, Chef",
         "Students identify jobs, professions and associate them with their primary duties.",
         ["Professions", "Architect", "Mechanic", "Tailor", "Dentist"],
         "Job matching riddles: guessing occupations from duty descriptions.",
         "Who designs buildings, houses, and skyscrapers?",
         "An architect designs buildings."),
        
        ("Occupations", "What Do They Do?", "Present Simple with Job Descriptions",
         "Students formulate sentences describing workplace responsibilities.",
         ["Duties", "Examine patients", "Repair cars", "Sew clothes"],
         "Career day presentation: students describe their future dream job.",
         "What does a mechanical engineer or mechanic do?",
         "A mechanic fixes and services damaged vehicle engines and machines."),
        
        ("Occupations", "Past Dates and Milestones: Was / Were", "Talking About Birth Years and Past States",
         "Students use was/were to talk about past dates, historical inventors and origins.",
         ["Was", "Were", "Past Dates", "History"],
         "Biographical timeline strips of famous Turkish scientists like Aziz Sancar.",
         "Complete: 'Aziz Sancar _____ born in Mardin in 1946.'",
         "'Aziz Sancar was born in Mardin in 1946.'"),

        # Unit 7: Holidays (22-25)
        ("Holidays", "Vacation Types and Activities", "Sightseeing, Seaside, Skiing, Camping, Sailing",
         "Students describe holiday destinations and recreational travel experiences.",
         ["Holidays", "Sightseeing", "Camping", "Seaside", "Hiking"],
         "Travel brochure analysis and dream holiday pitch in small teams.",
         "Which holiday type involves sleeping in tents and cooking on campfires?",
         "A camping holiday."),
        
        ("Holidays", "Simple Past Tense: Regular Verbs (-ed)", "Visited, Climbed, Stayed, Walked, Played",
         "Students learn spelling rules and pronunciation of regular past tense verbs (/t/, /d/, /id/).",
         ["Regular Verbs", "-ed Ending", "Past Tense", "Pronunciation"],
         "Audio-recorded sentence reading focusing on past verb endings.",
         "What is the past simple form of 'visit' and 'stay'?",
         "'Visited' and 'stayed'."),
        
        ("Holidays", "Simple Past Tense: Irregular Verbs", "Went, Saw, Bought, Ate, Swam, Had",
         "Students memorize and apply common irregular past verbs in holiday narratives.",
         ["Irregular Verbs", "Went", "Saw", "Bought", "Narrative"],
         "Holiday postcard writing to an international pen pal.",
         "Write the past form of: buy, go, see, eat.",
         "Bought, went, saw, ate."),
        
        ("Ara Tatil", "2. Dönem Ara Tatil Kampı", "Past Tense & Reading Comprehension Camp",
         "Students reinforce past tense structures through mystery stories and timeline puzzles.",
         ["Camp", "Past Tense", "Puzzles", "Reading"],
         "Detective story analysis finding clues written in past tense.",
         "What did you do yesterday? (Sample past response)",
         "'Yesterday, I visited my grandparents and we had lunch together.'"),

        # Unit 8: Bookworms (26-28)
        ("Bookworms", "Reading Habits and Book Types", "Novel, Poetry, Fairy Tale, Biography, Dictionary",
         "Students categorize literary genres and discuss reading habits and favorite authors.",
         ["Bookworm", "Novel", "Poetry", "Author", "Library"],
         "Book club speed-chat: pitching favorite books in 2 minutes.",
         "What type of book tells the life story of a real famous person?",
         "A biography."),
        
        ("Bookworms", "Library Rules and Prepositions of Place", "On, Under, In front of, Next to, Between",
         "Students locate books on library shelves using precise spatial prepositions.",
         ["Library Rules", "Silence", "Bookshelf", "Prepositions"],
         "Library scavenger hunt map simulation.",
         "Where is the science dictionary located? 'It is on the third shelf, next to the encyclopedia.'",
         "'It is on the third shelf, next to the encyclopedia.'"),
        
        ("Bookworms", "Asking and Answering in the Past", "Did you read...? Yes, I did / No, I didn't",
         "Students formulate interrogative questions in Simple Past using auxiliary 'did'.",
         ["Did", "Didn't", "Past Questions", "Short Answers"],
         "Author investigation: interviewing a classmate about books they read last month.",
         "Form the question: '_____ you borrow this book from the school library yesterday?'",
         "'Did you borrow this book from the school library yesterday?'"),

        # Unit 9: Saving the Planet (29-32)
        ("Saving the Planet", "Environmental Problems", "Pollution, Global Warming, Deforestation, Littering",
         "Students identify threats facing the ecosystem and our planet Earth.",
         ["Pollution", "Deforestation", "Global Warming", "Litter"],
         "Eco-audit: assessing electricity and paper waste in the school building.",
         "What is the harmful effect of throwing plastic bottles into the sea?",
         "It causes marine pollution and kills sea animals and fish."),
        
        ("Saving the Planet", "Eco-Friendly Actions: The 3 Rs", "Reduce, Reuse, Recycle and Conserve Energy",
         "Students describe practical methods to preserve natural resources and prevent waste.",
         ["Reduce", "Reuse", "Recycle", "Energy Saving"],
         "Recycling bin sorting challenge and zero-waste pledge.",
         "What does the term 'Reduce, Reuse, Recycle' promote?",
         "It promotes sustainable living by cutting down garbage and reusing resources."),
        
        ("Saving the Planet", "Expressing Obligation: Must / Mustn't", "Environmental Rules and Imperatives",
         "Students formulate eco-rules using must, mustn't, and direct imperative orders.",
         ["Must", "Mustn't", "Eco Rules", "Imperatives"],
         "Creating school environmental protection posters with catchy slogans.",
         "Complete: 'We _____ turn off the tap while brushing our teeth.'",
         "'We must turn off the tap while brushing our teeth.'"),
        
        ("Saving the Planet", "Green Energy and Renewable Resources", "Solar Power, Wind Turbines, Clean Future",
         "Students understand the benefits of renewable solar and wind energy over fossil fuels.",
         ["Solar Energy", "Wind Turbine", "Renewable", "Clean Energy"],
         "Model wind turbine project presentation.",
         "Why are solar panels better for the environment than coal power plants?",
         "They produce clean renewable electricity without emitting toxic greenhouse gases."),

        # Unit 10: Democracy (33-36)
        ("Democracy", "Democracy and Voting Process", "Candidates, Ballot Box, Election, Vote, Speech",
         "Students learn vocabulary related to civic elections and school student council voting.",
         ["Democracy", "Election", "Ballot Box", "Vote", "Candidate"],
         "Mock student council election: campaign speeches and secret balloting.",
         "Where do voters place their marked voting paper during an election?",
         "Into the ballot box."),
        
        ("Democracy", "Qualities of a Good Leader", "Fair, Respectful, Hardworking, Honest, Kind",
         "Students evaluate characteristics required in presidential candidates and representatives.",
         ["Leadership", "Fairness", "Honesty", "Representation"],
         "Candidate debate panel on improving school facilities.",
         "Which quality ensures a leader treats all students equally without favoritism?",
         "Fairness and justice."),
        
        ("Democracy", "Rights and Responsibilities", "Freedom of Speech, Right to Education, Civic Duty",
         "Students discuss fundamental democratic rights and responsibilities in society.",
         ["Rights", "Responsibilities", "Freedom", "Equality"],
         "Classroom bill of rights constitution drafting workshop.",
         "What is an essential civic responsibility in a democratic society?",
         "Respecting others' rights and participating in elections by voting."),
        
        ("Democracy", "6. Sınıf İngilizce Yıl Sonu Sentezi", "Year-End English Language Showcase",
         "Students integrate all 10 units in an interactive communicative festival.",
         ["Synthesis", "Showcase", "CEFR A1+", "Graduation"],
         "English language portfolio celebration and award ceremony.",
         "What key skill did you develop most in 6th Grade English?",
         "Expressing opinions, narrating past events and discussing global environmental issues.")
    ]
    assert len(u) == 36, f"Eng 6 count: {len(u)}"
    return {
        'title': '6. Sınıf',
        'subtitle': 'Ortaokul İngilizce Programı (10 Ünite)',
        'badge': 'Ortaokul İngilizce',
        'weeks': _make_weeks(u, 'İNG.6')
    }

def get_eng_7():
    # 7. Sınıf MEB İngilizce (10 Ünite - Tam 36 Hafta)
    u = [
        # Unit 1: Appearance and Personality (1-4)
        ("Appearance and Personality", "Describing Physical Appearance", "Height, Build, Hair, Eyes and Facial Features",
         "Students describe physical characteristics (tall, slim, curly hair, hazel eyes).",
         ["Appearance", "Slim", "Curly Hair", "Hazel Eyes"],
         "Police sketch artist simulation: describing suspects based on witness clues.",
         "How do you describe someone who has dark, wavy hair and glasses?",
         "'He is of medium height with dark wavy hair and wears glasses.'"),
        
        ("Appearance and Personality", "Personality and Character Traits", "Generous, Punctual, Honest, Stubborn, Outgoing",
         "Students evaluate character traits and adjectives describing personalities.",
         ["Personality", "Generous", "Punctual", "Stubborn", "Honest"],
         "Personality quiz matching students with compatible study partners.",
         "Which adjective describes a person who is always on time for appointments?",
         "Punctual."),
        
        ("Appearance and Personality", "Comparative Adjectives with Personality", "More outgoing, More generous, Friendlier",
         "Students compare people's appearances and personalities using comparative forms.",
         ["Comparatives", "More outgoing", "Clumsier", "Friendlier"],
         "Sibling character comparison essay in 6 sentences.",
         "Complete: 'Emre is _____ (generous) than his brother; he always shares his books.'",
         "'Emre is more generous than his brother.'"),
        
        ("Appearance and Personality", "First Impressions vs Real Character", "Judging People and Empathy",
         "Students discuss that inner qualities and kindness are more valuable than outward beauty.",
         ["Empathy", "Inner Beauty", "Kindness", "Values"],
         "Short story analysis: 'Don't judge a book by its cover'.",
         "What does the proverb 'Don't judge a book by its cover' teach us?",
         "It teaches us not to evaluate a person solely based on their external appearance."),

        # Unit 2: Sports (5-7)
        ("Sports", "Individual and Team Sports", "Archery, Wrestling, Volleyball, Tennis, Fencing",
         "Students classify sports into indoor, outdoor, team, and individual disciplines.",
         ["Sports", "Archery", "Wrestling", "Equipment", "Court"],
         "Olympic sports research: discovering national Turkish medal sports.",
         "Which traditional Turkish sport features bow and arrows?",
         "Archery (Okçuluk)."),
        
        ("Sports", "Frequency Adverbs with Sports Habits", "How often do you train? Once a week, Twice a month",
         "Students ask and answer about training schedules using 'How often' and frequency expressions.",
         ["How often", "Twice a week", "Training", "Habits"],
         "Athlete interview role-play discussing workout routines.",
         "How do you answer: 'How often do you train at the swimming pool?'",
         "'I train at the swimming pool three times a week.'"),
        
        ("Sports", "Sports Equipment and Safety Gear", "Helmet, Racket, Goggles, Pads, Shuttlecock",
         "Students identify sports gear and emphasize safety precautions in extreme activities.",
         ["Equipment", "Helmet", "Goggles", "Protection"],
         "Equipment-to-sport matching speed drill.",
         "Which protective equipment protects the head from severe injuries?",
         "A protective safety helmet."),

        # Unit 3: Biographies (8-10)
        ("Biographies", "Talking About Past Milestones", "Birth, Education, Graduation, Marriage, Career",
         "Students narrate chronological life milestones using past tense markers and time clauses.",
         ["Biography", "Milestones", "Graduated", "Career"],
         "Timeline creation: charting the life of Mustafa Kemal Atatürk.",
         "Which verb expresses completing university and obtaining a degree?",
         "Graduated (from university)."),
        
        ("Ara Tatil", "1. Dönem Ara Tatil Kampı", "English Autumn Camp: Biography & Past Tense",
         "Students consolidate past tense with famous inventors' biographical narratives.",
         ["Camp", "Past Tense", "Biography", "Consolidation"],
         "Biographical trivia quiz show in teams.",
         "What did Alexander Graham Bell invent?",
         "He invented the first practical telephone."),
        
        ("Biographies", "Famous Scientists and Historic Figures", "Aziz Sancar, Marie Curie, Nikola Tesla, Atatürk",
         "Students read biographical sketches and summarize achievements of great scientists.",
         ["Aziz Sancar", "Nobel Prize", "Discovery", "Achievement"],
         "Nobel laureate biography presentation in 5 key dates.",
         "In which scientific field did Aziz Sancar win the Nobel Prize in 2015?",
         "In Chemistry, for his mechanistic studies of DNA repair."),

        # Unit 4: Wild Animals (11-14)
        ("Wild Animals", "Habitat, Prey and Predators", "Jungle, Savannah, Herbivore, Carnivore, Reptiles",
         "Students classify wildlife according to diet, body features, and natural ecosystem habitats.",
         ["Wild Animals", "Carnivore", "Habitat", "Predator", "Savannah"],
         "Animal kingdom classification food chain diagram.",
         "What do you call an animal that eats only plants and grass?",
         "A herbivore."),
        
        ("Wild Animals", "Endangered Species", "Threats: Poaching, Habitat Loss, Climate Change",
         "Students identify factors that drive species (panda, snow leopard, sea turtle) to extinction.",
         ["Endangered", "Extinction", "Poaching", "Deforestation"],
         "WWF endangered species case study report.",
         "Why are polar bears becoming endangered in the Arctic?",
         "Because global warming is melting their sea ice hunting grounds."),
        
        ("Wild Animals", "Giving Advice for Wildlife Conservation", "Should / Shouldn't: Protecting Endangered Species",
         "Students formulate practical measures using should and shouldn't to preserve biodiversity.",
         ["Conservation", "Protection", "Should", "Shouldn't"],
         "Creating conservation placards: 'We shouldn't hunt wild animals!'",
         "Complete: 'Governments _____ ban illegal poaching and create nature reserves.'",
         "'Governments should ban illegal poaching and create nature reserves.'"),
        
        ("Wild Animals", "Nature Reserves and National Parks", "Protected Wildlife Corridors",
         "Students describe the role of national safari parks and breeding programs.",
         ["National Park", "Reserve", "Sanctuary", "Breeding"],
         "Virtual exploration of Yellowstone and Serengeti national parks.",
         "What is the purpose of establishing national wildlife sanctuaries?",
         "To protect endangered animals and plants from human hunting and urban encroachment."),

        # Unit 5: Television (15-18)
        ("Television", "TV Programme Types", "Documentary, News, Sitcom, Soap Opera, Reality Show, Quiz Show",
         "Students identify and describe different formats of broadcast television.",
         ["Television", "Documentary", "Sitcom", "Quiz Show", "News"],
         "Designing a 24-hour educational TV channel schedule.",
         "Which television program provides real scientific facts about animals and nature?",
         "A nature documentary."),
        
        ("Television", "Expressing Preferences with 'Prefer'", "I prefer watching documentaries to reality shows",
         "Students apply the grammar structure: prefer + noun/verb-ing + to + noun/verb-ing.",
         ["Prefer", "Preferences", "To", "Opinions"],
         "Classroom TV viewing habits survey and pie chart generation.",
         "Complete: 'My father prefers _____ (watch) the evening news to watching series.'",
         "'My father prefers watching the evening news to watching series.'"),
        
        ("Television", "1. Dönem Sonu Sentezi", "Mid-Year English Synthesis Assessment",
         "Students test proficiency on Units 1-5 through multi-skill communicative tasks.",
         ["Synthesis", "Assessment", "Listening", "Reading"],
         "Mock exam analyzing reading texts and dialogue completions.",
         "What is the negative impact of watching too much television?",
         "It promotes sedentary habits, wastes study time, and strains eye health."),
        
        ("Television", "1. Dönem Sonu Karne", "Winter Reading & Series Watchlist",
         "Students draft an educational documentary viewing log for the winter break.",
         ["Karne", "Winter Break", "Watchlist", "Self-Assessment"],
         "Guidelines on watching English documentaries with English subtitles.",
         "How does watching English subtitles improve comprehension?",
         "It associates spoken phonetics with written orthography directly."),

        # Unit 6: Celebrations (19-21)
        ("Celebrations", "Party Types and Occasions", "Graduation, Housewarming, Birthday, Wedding, Anniversary",
         "Students categorize celebrations and describe customs related to life events.",
         ["Celebrations", "Housewarming", "Graduation", "Wedding"],
         "Party checklist: budgeting, catering, music and invitations.",
         "What kind of party do people throw when they move into a new house?",
         "A housewarming party."),
        
        ("Celebrations", "Quantifiers in Party Planning", "A few, A little, Some, Any, A lot of",
         "Students use countable and uncountable quantifiers correctly when ordering supplies.",
         ["Quantifiers", "A few", "A little", "A lot of", "Countable"],
         "Party catering budget worksheet calculation.",
         "Complete with 'a few' or 'a little': 'We need _____ sugar and _____ balloons.'",
         "'We need a little sugar and a few balloons.'"),
        
        ("Celebrations", "Making Offers and Polite Requests", "Would you like some punch? Can I help you?",
         "Students practice social hospitality expressions used by hosts and guests.",
         ["Hospitality", "Would you like", "Offers", "Courtesy"],
         "Role-playing guest reception at a graduation party buffet.",
         "How do you politely accept an offer of a slice of cake?",
         "'Yes, please! I'd love some.'"),

        # Unit 7: Dreams (22-25)
        ("Dreams", "Future Predictions with 'Will / Won't'", "Technology, Career, Planet Earth in 2050",
         "Students make optimistic and pessimistic predictions about future life.",
         ["Future Predictions", "Will", "Won't", "Technology", "2050"],
         "Writing a futuristic news headline from the year 2060.",
         "What is your prediction about future transportation in 2050?",
         "'I believe we will travel in flying solar-powered electric cars.'"),
        
        ("Dreams", "Personal Aspirations and Ambitions", "I hope, I believe, I imagine, I think",
         "Students express their personal dreams (career, university, travels) using opinion openers.",
         ["Aspirations", "Ambition", "I hope", "I believe"],
         "Creating a personal 10-year life vision board.",
         "Complete: 'I hope I _____ (graduate) from medical school and cure diseases.'",
         "'I hope I will graduate from medical school and cure diseases.'"),
        
        ("Dreams", "Future of Education and AI", "Robot Teachers, Virtual Classrooms, Smart Cities",
         "Students debate how artificial intelligence will reshape school learning and occupations.",
         ["AI in Education", "Virtual Reality", "Smart Cities", "Robotics"],
         "Debate: Will AI robots replace human doctors and teachers in the future?",
         "What human skill can artificial intelligence never replace?",
         "True human empathy, emotional compassion, and moral consciousness."),
        
        ("Ara Tatil", "2. Dönem Ara Tatil Kampı", "Future Predictions & Vocabulary Camp",
         "Students reinforce will/won't and quantifiers through reading comprehension challenges.",
         ["Camp", "Spring Break", "Future", "Consolidation"],
         "Futuristic creative writing sprint: 'A Day in 2075'.",
         "What auxiliary verb is used for negative future predictions?",
         "'Won't' (will not)."),

        # Unit 8: Public Buildings (26-28)
        ("Public Buildings", "City Facilities and Services", "Municipality, Governor's Office, Art Gallery, Fire Station",
         "Students identify municipal buildings and civic administrative centers.",
         ["Public Buildings", "Municipality", "Police Station", "Art Gallery"],
         "Town planning simulation: placing civic amenities in optimal zones.",
         "Where do citizens go to report an emergency fire incident?",
         "To the fire station."),
        
        ("Public Buildings", "Expressing Purpose: To-Infinitive", "I went to the post office to send a letter",
         "Students explain the purpose of visits using 'to + verb' (infinitive of purpose).",
         ["Infinitive of Purpose", "To buy", "To send", "Services"],
         "City errand chain: matching errands with destinations using 'to'.",
         "Why do people visit the municipal office?",
         "They visit the municipal office to pay city taxes and handle legal permits."),
        
        ("Public Buildings", "Smart Cities and Digital Municipal Services", "E-Government, Online Permits, Green Parks",
         "Students explore how technology simplifies administrative municipal errands.",
         ["Smart Cities", "E-Government", "Digital Services", "Efficiency"],
         "Designing a mobile civic app concept for local city residents.",
         "How do digital municipal apps help reduce traffic and paper waste?",
         "By allowing citizens to complete bureaucratic paperwork from home online."),

        # Unit 9: Environment (29-32)
        ("Environment", "Types of Environmental Pollution", "Air, Water, Soil, Noise and Light Pollution",
         "Students analyze environmental threats and their impact on global human health.",
         ["Environment", "Pollution", "Pesticides", "Exhaust Fumes"],
         "Water and soil contamination diagram analysis.",
         "Which source contributes most to air pollution in mega-cities?",
         "Exhaust fumes from motor vehicles and industrial factory chimneys."),
        
        ("Environment", "Renewable Energy vs Fossil Fuels", "Solar, Hydroelectric, Geothermal and Wind Energy",
         "Students evaluate clean green energy options versus polluting fossil hydrocarbons.",
         ["Renewable Energy", "Geothermal", "Solar Power", "Fossil Fuels"],
         "Energy grid transition case study for Türkiye.",
         "Why is wind energy called 'renewable'?",
         "Because wind naturally regenerates without depleting Earth's resources."),
        
        ("Environment", "Global Warming and Climate Crisis", "Melting Glaciers, Rising Sea Levels, Extreme Drought",
         "Students examine the greenhouse effect and evaluate measures to reduce carbon footprints.",
         ["Climate Crisis", "Carbon Footprint", "Greenhouse Effect", "Drought"],
         "Carbon footprint calculator activity measuring individual electricity and transport.",
         "What simple habit helps reduce individual carbon footprints?",
         "Using public transport, cycling, and turning off unused electrical appliances."),
        
        ("Environment", "Eco-Friendly Lifestyle Action Plan", "Planting Trees, Reusable Bags, Composting",
         "Students produce a collaborative manifesto for sustainable school communities.",
         ["Action Plan", "Composting", "Reforestation", "Sustainability"],
         "Organizing a school tree-planting campaign day.",
         "How do trees help mitigate global air pollution?",
         "They absorb carbon dioxide and release fresh oxygen through photosynthesis."),

        # Unit 10: Planets (33-36)
        ("Planets", "The Solar System and Celestial Bodies", "Sun, Moon, Mercury, Mars, Jupiter, Orbit, Asteroid",
         "Students name the planets in order of distance from the Sun and describe their physical traits.",
         ["Solar System", "Planets", "Orbit", "Jupiter", "Mars"],
         "Scale model solar system hallway exhibition.",
         "Which planet in our solar system is known as the 'Red Planet'?",
         "Mars is known as the Red Planet due to iron oxide on its surface."),
        
        ("Planets", "Superlative Adjectives", "The biggest, The closest, The hottest, The farthest",
         "Students apply superlative grammatical forms (the -est, the most) when comparing cosmic bodies.",
         ["Superlatives", "The biggest", "The hottest", "The farthest"],
         "Solar system fact file comparison cards using superlatives.",
         "Which planet is the largest planet in our entire solar system?",
         "Jupiter is the largest planet in our solar system."),
        
        ("Planets", "Space Exploration and Satellites", "Astronauts, Space Station, Moon Landing, Telescopes",
         "Students discuss space missions, James Webb telescope imagery, and Turkish astronaut Alper Gezeravcı.",
         ["Space Exploration", "Astronaut", "ISS", "James Webb"],
         "Presenting Turkish astronaut Alper Gezeravcı's scientific mission to the ISS.",
         "Who became the first Turkish astronaut to conduct science experiments on the International Space Station?",
         "Alper Gezeravcı."),
        
        ("Planets", "7. Sınıf İngilizce Yıl Sonu Sentezi", "Year-End CEFR A2 Portfolio Showcase",
         "Students consolidate appearance, biography, animals, television, dreams, and science topics.",
         ["Synthesis", "Portfolio", "CEFR A2", "Graduation"],
         "Spoken English symposium and awards ceremony.",
         "What is the ultimate benefit of mastering 7th Grade English skills?",
         "It empowers students to read global scientific literature and communicate ideas persuasively.")
    ]
    assert len(u) == 36, f"Eng 7 count: {len(u)}"
    return {
        'title': '7. Sınıf',
        'subtitle': 'Ortaokul İngilizce Programı (10 Ünite)',
        'badge': 'Ortaokul İngilizce',
        'weeks': _make_weeks(u, 'İNG.7')
    }

def get_eng_8():
    # 8. Sınıf LGS Sınav Odaklı MEB İngilizce (10 Ünite - Tam 36 Hafta)
    u = [
        # Unit 1: Friendship (1-4)
        ("Friendship", "Qualities of a Good Friend", "Honest, Generous, Back up, Count on, Reliable, Loyal",
         "Students evaluate essential traits of true companions using key vocabulary (count on, back up).",
         ["Friendship", "Count on", "Back up", "Trustworthy", "Reliable"],
         "LGS reading comprehension questions analyzing character dialogue bubbles.",
         "What phrasal verb means 'to support and help someone when they are in difficulty'?",
         "'Back up' (to back someone up)."),
        
        ("Friendship", "Making, Accepting and Refusing Invitations", "Would you like to come over? I'd love to, but...",
         "Students practice inviting friends and replying politely with genuine excuses.",
         ["Invitations", "Accepting", "Refusing", "Excuse", "Politeness"],
         "Analyzing formal and informal invitation cards for LGS exam questions.",
         "Which sentence politely refuses an invitation while giving a valid reason?",
         "'I'd love to, but I have to finish my Science project tonight.'"),
        
        ("Friendship", "Making Excuses and Giving Reasons", "Because, Since, As, Have an exam tomorrow",
         "Students identify the difference between refusing with an excuse and refusing without an excuse.",
         ["Excuses", "Because", "Reasons", "LGS Trap"],
         "Tackling LGS trick questions: 'Who refuses the invitation with an excuse?'",
         "Why is giving an excuse important when declining a friend's party invitation?",
         "It shows politeness and proves that you value the friend's feeling."),
        
        ("Friendship", "LGS Friendship Reading Passage Analysis", "Friendship Survey and Text Interpretation",
         "Students solve 20 LGS-style multiple choice questions based on dialogues and charts.",
         ["LGS Practice", "Dialogue Analysis", "Survey Chart", "Critical Reading"],
         "Speed reading and keyword scanning drills.",
         "Which question helps find the receiver of an invitation email?",
         "'To whom is the invitation written?' or 'Who is the recipient?'"),

        # Unit 2: Teen Life (5-7)
        ("Teen Life", "Teen Preferences and Free Time", "Music Genres, Camping, Snob, Trendy, Unbearable, Fond of",
         "Students express daily lifestyle preferences using phrases like keen on, fond of, into, can't stand.",
         ["Teen Life", "Fond of", "Keen on", "Can't stand", "Unbearable"],
         "Preference collocation charts: fond of rock music, keen on cycling.",
         "What does the phrase 'I can't stand heavy metal music' mean?",
         "It means 'I hate heavy metal music; I find it completely unbearable.'"),
        
        ("Teen Life", "Music Genres and Preferences", "Classical, Pop, Rap, Techno, Heavy Metal, Jazz",
         "Students compare diverse music styles with descriptive adjectives (trendy, energetic, ridiculous).",
         ["Music Genres", "Energetic", "Harmonic", "Rhythm"],
         "LGS survey chart questions: analyzing musical preferences among 100 teenagers.",
         "According to a chart where 60% listen to pop and 5% to jazz, which genre is least popular?",
         "Jazz is the least popular genre among the surveyed teens."),
        
        ("Teen Life", "Daily Routine and Habits of Teens", "Disciplined Habits, Snobbery and Realistic Goals",
         "Students describe a healthy teenage schedule balancing academics, sports, and reading.",
         ["Habits", "Reading books", "Balance", "Teen Routine"],
         "Paraphrasing sentences: matching synonymous statements in LGS options.",
         "What is the synonym of 'I am crazy about swimming'?",
         "'I really love swimming' or 'I am very fond of swimming.'"),

        # Unit 3: In the Kitchen (8-10)
        ("In the Kitchen", "Cooking Methods and Processes", "Bake, Boil, Fry, Roast, Steam, Grill, Chop, Slice, Dice",
         "Students master kitchen vocabulary, cooking verbs, utensils, and food preparation actions.",
         ["Cooking Methods", "Boil", "Bake", "Chop", "Peel", "Whisk"],
         "Recipe flowchart matching verbs with target ingredients.",
         "Which kitchen verb means 'to cut something into very thin, flat pieces'?",
         "To slice."),
        
        ("Ara Tatil", "1. Dönem Ara Tatil Kampı", "LGS Autumn Camp: Units 1-3 Mastery",
         "Students solve 100 LGS questions covering Friendship, Teen Life, and Kitchen vocabulary.",
         ["LGS Camp", "Question Analysis", "Speed", "Consolidation"],
         "Solving graphic organizer and recipe order questions under time pressure.",
         "What is the first step in preparing a vegetable soup?",
         "Peeling and washing the fresh vegetables thoroughly."),
        
        ("In the Kitchen", "Sequencing Words in Recipes", "First, Second, Then, Next, After that, Finally",
         "Students organize steps of authentic recipes (Pancake, Menemen, Cake) using transition sequencers.",
         ["Sequencers", "First", "Next", "Finally", "Recipe Steps"],
         "Reordering mixed recipe steps into correct chronological order.",
         "Which question format asks for the step immediately following the peeling of potatoes?",
         "'What is the next step after peeling the potatoes?'"),

        # Unit 4: On the Phone (11-14)
        ("On the Phone", "Telephone Expressions and Etiquette", "Hold on, Put through, Connect, Engaged, Available, Leave a message",
         "Students learn standard communication phrases used in formal and informal phone calls.",
         ["Phone Etiquette", "Hold on", "Put through", "Leave a message"],
         "Role-playing customer service and receptionist phone calls.",
         "What does a secretary say when asking a caller to wait a moment on the line?",
         "'Hold on a moment, please. I will put you through to Mr. Demir.'"),
        
        ("On the Phone", "Purposes of Phone Calls", "Make an Appointment, Book a Ticket, Complain, Ask for Info",
         "Students classify telephone conversations according to caller intentions in LGS tables.",
         ["Purposes", "Reservation", "Complaint", "Appointment"],
         "Analyzing call center log tables for LGS exam questions.",
         "Why does Ayşe call the dental clinic?",
         "She calls to book an appointment to have her tooth checked."),
        
        ("On the Phone", "Future Intentions: Will vs Be Going To", "Spontaneous Decisions and Planned Phone Actions",
         "Students distinguish instant decisions on the phone ('I'll tell him') from prior arrangements.",
         ["Will", "Be going to", "Decisions", "Promises"],
         "Phone message memo writing practice based on audio recordings.",
         "What memo note do you leave when someone calls for your absent sister?",
         "'Ali called at 14:00. He wants you to call him back regarding the Maths project.'"),
        
        ("On the Phone", "Evolution of Communication", "Smoke Signals, Pigeon, Telegraph, Smartphone, Video Call",
         "Students trace the historical progression of long-distance communication technologies.",
         ["History of Comm", "Telegraph", "Morse Code", "Smartphone"],
         "Timeline poster comparing ancient and modern communication speeds.",
         "How did ancient civilizations send emergency messages over long distances?",
         "By using smoke signals, carrier pigeons, and beacon fires."),

        # Unit 5: The Internet (15-18)
        ("The Internet", "Internet Terminology and Icons", "Browser, Search Engine, Attachment, Log in, Log out, Download, Upload",
         "Students identify internet icons, navigation buttons, and operational digital terms.",
         ["Internet Icons", "Upload", "Download", "Attachment", "Log in"],
         "Website layout identification: matching icons with corresponding actions.",
         "Which button do you click to send a file or document with your email?",
         "The 'Attachment' (paperclip) icon."),
        
        ("The Internet", "Internet Safety and Netiquette", "Strong Password, Personal Info, Cyberbullying, Virus, Scams",
         "Students formulate internet safety rules to protect digital privacy and avoid malware.",
         ["Internet Safety", "Password", "Cyberbullying", "Privacy"],
         "Analyzing internet safety posters and identifying unsafe online behaviors.",
         "What is an essential online safety rule regarding personal information?",
         "Never share your address, passwords, or credit card details with strangers."),
        
        ("The Internet", "1. Dönem Sonu Sentezi", "LGS 1. Dönem Tam Kapsamlı Deneme Sınavı",
         "Students sit for a full 10-question LGS English mock exam covering Units 1 to 5.",
         ["LGS Deneme", "Tam Puan", "Synthesis", "Exam Tactic"],
         "Detailed error analysis and question type categorization.",
         "How many questions are asked in the LGS English exam?",
         "Exactly 10 multiple-choice questions requiring critical reading and analysis."),
        
        ("The Internet", "1. Dönem Sonu Karne", "LGS Yarıyıl Tatil Çalışma Programı",
         "Students establish a rigorous vocabulary revision schedule for the 15-day winter break.",
         ["Karne", "LGS Strategy", "Vocabulary Bank", "Revision"],
         "Distributing LGS high-frequency vocabulary flashcard decks.",
         "What is the single most effective way to improve LGS English scores?",
         "Mastering high-frequency unit vocabulary and regularly solving visual chart questions."),

        # Unit 6: Adventures (19-21)
        ("Adventures", "Extreme Sports and Dangerous Activities", "Bungee Jumping, Skydiving, White-Water Rafting, Caving, Paragliding",
         "Students identify extreme adrenaline sports and evaluate risk levels.",
         ["Extreme Sports", "Paragliding", "Rafting", "Adrenaline", "Risk"],
         "Adrenaline meter ranking: ordering extreme sports from least to most dangerous.",
         "Which extreme sport involves jumping off a high bridge with an elastic cord tied to your ankles?",
         "Bungee jumping."),
        
        ("Adventures", "Expressing Preferences: Would Rather vs Prefer", "I would rather go rafting than paragliding",
         "Students apply grammar rules: 'prefer doing to doing' vs 'would rather do than do'.",
         ["Would Rather", "Prefer", "Adventures", "Grammar Rules"],
         "Sentence transformation drills converting 'prefer' sentences to 'would rather'.",
         "Complete: 'I would rather _____ (try) scuba diving than go bungee jumping.'",
         "'I would rather try scuba diving than go bungee jumping.'"),
        
        ("Adventures", "Adrenaline Seekers vs Nature Lovers", "Why do people take extreme risks?",
         "Students debate motivations behind extreme sports using adjectives (challenging, eye-catching, risky).",
         ["Adrenaline Seeker", "Daring", "Challenging", "Motivations"],
         "LGS reading passage analysis on world-record extreme athletes.",
         "Why do extreme sports athletes love dangerous activities?",
         "Because they seek excitement, love pushing their physical limits, and enjoy high adrenaline rushes."),

        # Unit 7: Tourism (22-25)
        ("Tourism", "Tourist Destinations and Attractions", "Historic Sites, Architecture, Ancient Ruins, All-Inclusive, Scenery",
         "Students describe cultural and natural attractions of worldwide tourist capitals.",
         ["Tourism", "Historic Sites", "Ancient Ruins", "All-Inclusive"],
         "Travel brochure analysis: comparing Cappadocia, Antalya, and Trabzon.",
         "What makes Cappadocia one of the most famous tourist destinations in the world?",
         "Its unique fairy chimneys, underground cities, and hot air balloon tours."),
        
        ("Tourism", "Accommodation and Travel Types", "Bed & Breakfast, Resort, Hostel, Cruise, Sightseeing Tour",
         "Students compare accommodation preferences based on budget and amenities.",
         ["Accommodation", "Resort", "Sightseeing", "Hostel"],
         "Holiday budget planning challenge: selecting accommodation for a family of four.",
         "What type of hotel includes meals, drinks, and all leisure activities in the room price?",
         "An all-inclusive resort."),
        
        ("Tourism", "Present Perfect vs Simple Past in Tourism", "Have you ever been to Rome? I went there in 2021",
         "Students understand experiences (have ever been) versus specific past trips (went in 2021).",
         ["Present Perfect", "Ever / Never", "Past Experience", "Tourism"],
         "LGS travel interview questions: analyzing tourist experience surveys.",
         "Complete: 'Have you ever _____ (visit) the ancient city of Ephesus?'",
         "'Have you ever visited the ancient city of Ephesus?'"),
        
        ("Ara Tatil", "2. Dönem Ara Tatil Kampı", "LGS Spring Break Intensive Mock Marathon",
         "Students solve 5 full LGS English mock tests focusing on Units 1-7.",
         ["LGS Marathon", "Spring Break", "Full Mock", "Time Management"],
         "Analyzing difficult question types: negative root questions ('Which is NOT correct?').",
         "What must a student highlight first when reading an LGS question stem?",
         "Negative words like 'NOT', 'CANNOT', and 'INCORRECT'."),

        # Unit 8: Chores (26-28)
        ("Chores", "Household Chores and Tasks", "Do the laundry, Mop the floor, Dust shelves, Empty dishwasher, Take out rubbish",
         "Students name household responsibilities and chore assignments in families.",
         ["Chores", "Do laundry", "Mop the floor", "Dishwasher", "Dust"],
         "Family chore chart analysis for LGS exam questions.",
         "Which household task involves removing dust from furniture using a soft cloth?",
         "Dusting the shelves/furniture."),
        
        ("Chores", "Expressing Obligation: Must, Have to, Responsible for", "I have to clean my room, It's my duty",
         "Students express household duties using must, have to, and 'be responsible for + -ing'.",
         ["Obligation", "Have to", "Responsible for", "Duty"],
         "Sentence completion matching chore roles: 'My father is responsible for repairing things.'",
         "Complete: 'Ali is responsible for _____ (take out) the trash every evening.'",
         "'Ali is responsible for taking out the trash every evening.'"),
        
        ("Chores", "Sharing Responsibilities in Family and School", "Cooperation, Equality and Clean Environment",
         "Students discuss why dividing chores equally creates a peaceful and tidy home environment.",
         ["Cooperation", "Family Harmony", "Fairness", "Teamwork"],
         "Designing a fair family chore wheel where tasks rotate weekly.",
         "Why should family members share household chores equally?",
         "Because it reduces stress on parents, fosters responsibility, and keeps the home clean faster."),

        # Unit 9: Science (29-32)
        ("Science", "Scientific Inventions and Discoveries", "Invent, Discover, Experiment, Laboratory, Vaccination, Test Tube",
         "Students differentiate between inventions (man-made devices) and discoveries (natural facts).",
         ["Science", "Invention", "Discovery", "Laboratory", "Vaccine"],
         "LGS science chronology questions: matching scientists with their inventions.",
         "What is the difference between an 'invention' and a 'discovery'?",
         "An invention creates something completely new; a discovery finds something that already existed in nature."),
        
        ("Science", "Talking About Scientific Actions in Progress", "Conducting an experiment, Searching for a cure",
         "Students describe current research projects of contemporary scientists.",
         ["Current Science", "Conduct experiment", "Cure", "Microscope"],
         "Lab report analysis describing stem-cell and cancer research breakthroughs.",
         "What instrument do biologists use to examine tiny microorganisms invisible to the naked eye?",
         "A microscope."),
        
        ("Science", "Great Turkish and World Scientists", "Uğur Şahin, Özlem Türeci, Isaac Newton, Edison",
         "Students read biographical science articles highlighting COVID vaccine and gravity discoveries.",
         ["Uğur Şahin", "mRNA Vaccine", "Gravity", "Innovation"],
         "Classroom scientific symposium pitching revolutionary green tech ideas.",
         "Who developed the world's first successful mRNA COVID-19 vaccine?",
         "Dr. Uğur Şahin and Dr. Özlem Türeci (BioNTech)."),
        
        ("Science", "Ethics and Future of Science", "Cloning, Genetic Engineering, Artificial Intelligence",
         "Students evaluate ethical responsibilities in scientific experimentation.",
         ["Bioethics", "Gene Editing", "Responsibility", "Future"],
         "Debate: Should there be strict international ethical rules on genetic engineering?",
         "Why is scientific ethics essential in modern research?",
         "To ensure scientific progress benefits all humanity without causing biological harm or inequality."),

        # Unit 10: Natural Forces (33-36)
        ("Natural Forces", "Natural Disasters", "Earthquake, Avalanche, Flood, Drought, Tsunami, Volcanic Eruption",
         "Students identify natural disasters, causes, and environmental impact.",
         ["Natural Forces", "Earthquake", "Tsunami", "Avalanche", "Drought"],
         "Disaster map analysis: matching disaster names with global geographic zones.",
         "What natural disaster occurs when heavy rainfall causes rivers to overflow into cities?",
         "A flood."),
        
        ("Natural Forces", "Causes and Consequences of Disasters", "Loss of life, Destruction, Reforestation, Precautions",
         "Students evaluate human causes (deforestation, poor construction) behind disaster severity.",
         ["Causes", "Precautions", "Destruction", "Emergency"],
         "Formulating emergency earthquake preparedness guidelines.",
         "What is the most effective precaution against destructive earthquake damage?",
         "Constructing solid, earthquake-resistant buildings on stable geological ground."),
        
        ("Natural Forces", "LGS 1. Genel Tekrar Denemesi", "LGS Full Mock 1: 10/10 Target",
         "Students complete a full LGS exam simulation with detailed question-by-question analysis.",
         ["LGS Mock 1", "Tam Puan", "Speed & Accuracy", "Exam Strategy"],
         "Analysis of student performance data and common pitfall options.",
         "How should you approach a chart-based question in LGS English?",
         "Read the question stem first, check what the chart represents, and verify each option against the numbers."),
        
        ("Natural Forces", "LGS Final Denemesi ve Mezuniyet", "LGS 10'da 10 Şampiyonlar Kampı ve Veda",
         "Students complete the final LGS English confidence exam and receive exam day advice.",
         ["LGS Final", "10/10 Net", "Champions", "Success"],
         "Final exam motivation, calm mindset techniques, and celebration.",
         "What is the winning formula for achieving 10/10 in LGS English?",
         "Confident vocabulary knowledge, careful reading of the question stem, and elimination of trap options!")
    ]
    assert len(u) == 36, f"Eng 8 count: {len(u)}"
    return {
        'title': '8. Sınıf',
        'subtitle': 'LGS İngilizce Hazırlık (Sınav Odaklı 10 Ünite)',
        'badge': 'LGS İngilizce',
        'weeks': _make_weeks(u, 'İNG.8')
    }

print("Loading grades for İngilizce...")
g5 = get_eng_5()
g6 = get_eng_6()
g7 = get_eng_7()
g8 = get_eng_8()

print(f"Week counts: G5={len(g5['weeks'])}, G6={len(g6['weeks'])}, G7={len(g7['weeks'])}, G8={len(g8['weeks'])}")

grades_data = {
    5: g5,
    6: g6,
    7: g7,
    8: g8,
}

output_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'lib', 'data', 'subjects', 'ingilizce_data.dart'
)

generate_dart_file(
    subject_id='ingilizce',
    subject_name='İngilizce',
    short_code='İNG',
    description='Communication, Life, Health, Science, Natural Forces and LGS Prep',
    icon_name='language_rounded',
    primary_hex='0xFF2563EB', # Blue
    accent_hex='0xFF3B82F6',
    grades_data=grades_data,
    output_path=output_path
)

print("İngilizce generated successfully!")
