import csv

raw_beats = [
    ("P1.001", "PROLOGUE", "Scene 1: Christ on the Cross", """Stage Settings\nThe ‘stage’ represents Clare’s cell in her monastery at San Damiano. It is split like a triangle into 3 sections around the font in the centre. For the sake of a unified language, let's call these the ‘three stations of her cell’. The first station ( facing the audience directly on all sides at the top of the font) is a small clothes rack and a simple chair. The second station ( down stage right) is a straw mat where she sleeps. The Third Station ( down stage left) is a little table with a chair)\nClare plays and performs intermittently between the three stations.\nFrancis, a primary character in the play, walks in between these stations as if a memory in her mind. He sits on the stage right of the sanctuary. But for the beginning of the show, father is seated in the pews. A two person choir sits stage left of the altar. Most of the action takes place below the sanctuary around the three stations of the cell."""),
    ("P1.002", "PROLOGUE", "Scene 1: Christ on the Cross", """Scene 1: Christ on the Cross"""),
    ("P1.003", "PROLOGUE", "Scene 1: Christ on the Cross", """SOUND: The sound is the first ‘actor’. When the church is silent and the house ‘announcement’ has been made, we hear a ‘BREATHING’ happen, low breaths. After 15 seconds this is interrupted by a cacophony of modern noise which enters the church. Sounds of the city, advertistements, roles of a woman are being read off like a list."""),
    ("P1.004", "PROLOGUE", "Scene 1: Christ on the Cross", """Media: Mouse clicks, Traffic, News, Ambulance, consumerism, people buying stocks, news..different parts of the world news. Overload the audience > illuminating the cross in the middle of the screen (St Francis is gazing at Christ) - offs like a tv"""),
    ("P1.005", "PROLOGUE", "Scene 1: Christ on the Cross", """Action: Clare awakes from her sleep on the straw matt. It is noisy and she cups her ears.( a high pitched sound envelopes the space followed by a deep low resonance into an immediate and sudden stop)"""),
    ("P1.006", "PROLOGUE", "Scene 1: Christ on the Cross", """Francis slowly rises from his seat in the pews and stands at the sanctuary, prays to Christ on the cross"""),
    ("P1.007", "PROLOGUE", "Scene 1: Christ on the Cross", """Lighting Action: All the sounds suddenly stop with a spotlight on Francis once he reaches the cross. And media/spotlight on Christ."""),
    ("P1.008", "PROLOGUE", "Scene 1: Christ on the Cross", """Lighting Action: Lights wash to reveal Clare gazing at Francis."""),
    ("P1.009", "PROLOGUE", "Scene 1: Christ on the Cross", """Clare slowly gets off the bed and sees Francis."""),
    ("P1.010", "PROLOGUE", "Scene 1: Christ on the Cross", """Clare walks to Francis, gazes at him in station 1."""),
    ("P1.011", "PROLOGUE", "Scene 1: Christ on the Cross", """Slowly all the noises start to fade away."""),
    ("P1.012", "PROLOGUE", "Scene 1: Christ on the Cross", """Francis bows and takes his seat at the sanctuary."""),
    ("P1.013", "PROLOGUE", "Scene 1: Christ on the Cross", """Clare gazes at Christ. She starts to walk towards the chair."""),
    ("P1.014", "PROLOGUE", "Scene 1: Christ on the Cross", """Sound: Starts to build to support the acapella lord’s prayer hum."""),
    ("P1.015", "PROLOGUE", "Scene 1: Christ on the Cross", """Choir: Acappela Humming/Quiet Prayer."""),
    ("P1.016", "PROLOGUE", "Scene 1: Christ on the Cross", """PATER NOSTER\nPater Noster, qui es in caelis,\nSanctificetur nomen tuum,\nAdveniat regnum tuum,\nFiat voluntas tua,\nsicut in caelo et in terra.\nGive is this day our daily bread,\nForgive us our trespasses,\nAs we forgive those who trespass against us.\nLead us not into temptation but deliver us from evil\nAmen."""),
    ("P1.017", "PROLOGUE", "Scene 1: Christ on the Cross", """Action: Clare comes out of prayer. She looks at the audience."""),
    ("P1.018", "PROLOGUE", "Scene 1: Christ on the Cross", """When I came to know Him —truly know Him—I felt it here. (She touches her heart.) So deeply. And I thought… ah. This is it. I wanted to give myself completely to Him. To be His bride. His everlasting virgin bride."""),
    ("P1.019", "PROLOGUE", "Scene 1: Christ on the Cross", """She smiles.\nSo you have come to listen to my life story eh ?"""),
    ("P1.020", "PROLOGUE", "Scene 1: Christ on the Cross", """I was born a long time ago. 1194. I think I am the oldest person in this church today. Anyone else here born in 1194? No? She chuckles. Ah, I thought not."""),
    ("P1.021", "PROLOGUE", "Scene 1: Christ on the Cross", """I was born into a good family. A very good family. We had money, land, and a beautiful home.\nI was loved, very, very loved."""),
    ("P1.022", "PROLOGUE", "Scene 1: Christ on the Cross", """But for a girl like me. There was a life already written."""),
    ("P1.023", "PROLOGUE", "Scene 1: Christ on the Cross", """Media: Bring them to the medieval space, with the castle, land, wealth.\n(caricature of medieval times)"""),
    ("P1.024", "PROLOGUE", "Scene 1: Christ on the Cross", """Sound: Medieval time/tone music"""),
    ("P1.025", "PROLOGUE", "Scene 1: Christ on the Cross", """Now, I know what you’re thinking. She gestures to herself. “But Clare, you were wealthy!”\nSi,si I was very wealthy."""),
    ("P1.026", "PROLOGUE", "Scene 1: Christ on the Cross", """What more could a woman want? I had everything.\nBeat.\nWell…\nSometimes you can have everything and still feel trapped."""),
    ("P1.027", "PROLOGUE", "Scene 1: Christ on the Cross", """You see, I was no ordinary Medieval woman. I had a mind of my own. Opinions. Desires. And as a woman? She gives a little shrug.\nThere were certain things you simply did not decide for yourself."""),
    ("P1.028", "PROLOGUE", "Scene 1: Christ on the Cross", """You see my Padre—he had big plans for me! He wanted me to get married to a good husband from a good family. Sounds like a good arrangement no?"""),
    ("P1.029", "PROLOGUE", "Scene 1: Christ on the Cross", """Media: Various male caricatures. As posed by sharda and altered on AI."""),
    ("P1.030", "PROLOGUE", "Scene 1: Christ on the Cross", """No! A transaction, really. But for the women of my time, this was completely normal."""),
    ("P1.031", "PROLOGUE", "Scene 1: Christ on the Cross", """She looks at the audience.\nYou understand, no? Everything would be settled. And why not? I was eighteen. Beautiful. I was in the flower of my youth."""),
    ("P1.032", "PROLOGUE", "Scene 1: Christ on the Cross", """She smiles, then lets it fade.\nAnd yet… something was missing."""),
    ("P1.033", "PROLOGUE", "Scene 1: Christ on the Cross", """Sound enters"""),
    ("P1.034", "PROLOGUE", "Scene 1: Christ on the Cross", """CLARE\nBut I was loved, yes very loved, especially by my mama, Ortolana who instilled in all her children, a deep deep faith in God. The most important thing mi mama Ortolana taught us is that Christ was not only to be worshipped inside a church…."""),
    ("P1.035", "PROLOGUE", "Scene 1: Christ on the Cross", """My madre saw the world differently.\nMy madre saw God everywhere.\nEverywhere…"""),
    ("P1.036", "PROLOGUE", "Scene 1: Christ on the Cross", """Media : we see cities/landscapes of impoverished countries, skid row America, parts of Eastern Europe, Africa, Gaza… > (media connects and goes back in time to next scene)"""),
    ("P1.037", "PROLOGUE", "Scene 1: Christ on the Cross", """Especially in the poor who were everywhere."""),
    ("P1.038", "PROLOGUE", "Scene 1: Christ on the Cross", """Sound : Transition"""),
    ("P1.039", "PROLOGUE", "Scene 1: Christ on the Cross", """I knew something was missing in my life but I didn't realise what it was until I heard the voice of one man speak…"""),
    ("A1.001", "ACT I", "Scene 1: The Meeting of Francis", """ACT I — THE MEETING OF FRANCIS\nAction: Clare moves to the rack. She removes her white head piece and black cloth to portray a younger version of herself."""),
    ("A1.002", "ACT I", "Scene 1: The Meeting of Francis", """Media: > back in time transition to > The town of Assisi, horses, burrows, market, people walking, a city square."""),
    ("A1.003", "ACT I", "Scene 1: The Meeting of Francis", """Action: Francis rises from his Chair and moves to the step in front of the font He signs."""),
    ("A1.004", "ACT I", "Scene 1: The Meeting of Francis", """Sound: Sound underlies Francis as he signs."""),
    ("A1.005", "ACT I", "Scene 1: The Meeting of Francis", """Francis: “We have been called to heal wounds, to unite what has fallen apart, and to bring home those who have lost their way.”"""),
    ("A1.006", "ACT I", "Scene 1: The Meeting of Francis", """Choir: “We have been called to heal wounds, to unite what has fallen apart, and to bring home those who have lost their way.”"""),
    ("A1.007", "ACT I", "Scene 1: The Meeting of Francis", """CLARE: … Francis."""),
    ("A1.008", "ACT I", "Scene 1: The Meeting of Francis", """She watches him. She whispers to the audience.\nHe is a merchant’s son- like me—born into wealth. My padre thinks that he is mad. Mad! A rich man’s son, throwing away his fine clothes, sleeping in the streets, shouting about Christ as though the whole world had forgotten Him. And then, they say, he even stripped himself bare."""),
    ("A1.009", "ACT I", "Scene 1: The Meeting of Francis", """She gives a little disbelieving laugh.\nImagine! Mamma mia. What kind of madness is this?"""),
    ("A1.010", "ACT I", "Scene 1: The Meeting of Francis", """Clare weaves in and out of the audience in the pews, watching Francis give his ‘speech’"""),
    ("A1.011", "ACT I", "Scene 1: The Meeting of Francis", """Francis: The treasure of blessed poverty is so very precious and divine that we are not worthy to possess it in our vile bodies."""),
    ("A1.012", "ACT I", "Scene 1: The Meeting of Francis", """Choir: The treasure of blessed poverty is so very precious and divine that we are not worthy to possess it in our vile bodies."""),
    ("A1.013", "ACT I", "Scene 1: The Meeting of Francis", """CLARE: I didn't see this madness. Instead, I saw a man on fire. Whenever Francis spoke, he lit such a passion inside of me that it felt as if we were both engulfed in flames."""),
    ("A1.014", "ACT I", "Scene 1: The Meeting of Francis", """Sound design: Heartbeat"""),
    ("A1.015", "ACT I", "Scene 1: The Meeting of Francis", """CLARE: Over time, Francis's words grew inside of me like a fetus forming inside a womb, at first, a nothingness and then ever so delicately, it starts to take shape, a little curve becomes a spine, a bud becomes a hand, until a face gathers itself, the eyes, the nose, the mouth and then finally, the heartbeat."""),
    ("A1.016", "ACT I", "Scene 1: The Meeting of Francis", """Francis turns to see Clare. Their eyes meet.\nEventually, our eyes would meet, and then our minds and then our hearts."""),
    ("A1.017", "ACT I", "Scene 1: The Meeting of Francis", """ACTION: Francis and Clare circle each other."""),
    ("A1.018", "ACT I", "Scene 1: The Meeting of Francis", """Media: Possible night imagery/stars etc. Something cosmic to show their union."""),
    ("A1.019", "ACT I", "Scene 1: The Meeting of Francis", """Heartbeat - heart/ children/ light/ cosmic imagery\nSoundscape sound"""),
    ("A1.020", "ACT I", "Scene 1: The Meeting of Francis", """CLARE: ( STILL CIRCLING) Francis and I met on several occasions, where we broke bread and simply talked about our love of God."""),
    ("A1.021", "ACT I", "Scene 1: The Meeting of Francis", """Those were some of the happiest moments of my life.\nMeeting Francis filled up that emptiness in the pit of my stomach.\nWith every meeting, I felt more and more ALIVE."""),
    ("A1.022", "ACT I", "Scene 1: The Meeting of Francis", """ACTION: They stop circling. Francis and Clare acknowledge each other with a nod and Francis goes to sit down by the altar."""),
    ("A1.023", "ACT I", "Scene 1: The Meeting of Francis", """(silence)"""),
    ("A1.024", "ACT I", "Scene 1: The Meeting of Francis", """CLARE: (continues circling on her own) Through Francis, I realised that I had everything but desired none of it. I wanted to become as poor as the poor. To become so devoid of the material things of this world that I may become a channel of God's love."""),
    ("A1.025", "ACT I", "Scene 1: The Meeting of Francis", """(She stops circling)\nI knew what I had to do."""),
    ("A2.001", "ACT I", "Scene 2: Palm Sunday Escape", """Sound Design: The streets fill with the sound of noise, people gathering for Palm Sunday/ sound of something joyous and yet ominous."""),
    ("A2.002", "ACT I", "Scene 2: Palm Sunday Escape", """Media: We see Palms on the screen. - see if can get news footage of this"""),
    ("A2.003", "ACT I", "Scene 2: Palm Sunday Escape", """ACTION: Clare walks to the ‘tree/clothes rack’ and takes a Palm Sunday Branch off from it."""),
    ("A2.004", "ACT I", "Scene 2: Palm Sunday Escape", """CLARE: (Holding a Palm in her hand and waving it in the air)"""),
    ("A2.005", "ACT I", "Scene 2: Palm Sunday Escape", """It was Palm Sunday, 18th March 1212. I wore my finest dress. ( She takes the robe off a branch and wears it)"""),
    ("A2.006", "ACT I", "Scene 2: Palm Sunday Escape", """Placing all my trust in Jesus, on that Palm Sunday (takes the palm), I decided to leave my world behind. My home, my family. I decided to follow Francis."""),
    ("A2.007", "ACT I", "Scene 2: Palm Sunday Escape", """ACTION: Lights go down, a lamp is lit and swung, the choir swings these lamps. Clare narrates the escape in complete darkness."""),
    ("A2.008", "ACT I", "Scene 2: Palm Sunday Escape", """CLARE: We left at midnight. Me dressed in my finest clothes, slipped through the door of the dead (sound cue to hear BANG BANG BANG) All the while, in great fear of being caught by my family, I slipped through the gates of my house, stealthily making my way past the Guards of Assisi, down a deep, rocky and muddy slope into the Valley. My heart racing, sweat rolling down my cheeks and tears in my eyes, yet the knowing, the knowing Francis and his brothers were waiting for me, in that valley, waiting for me, to come home."""),
    ("A2.009", "ACT I", "Scene 2: Palm Sunday Escape", """Media: POV Clare running down a valley/ hill slope late at night. Hear your breath - POV found footage style - blair watch project (Film) > clare runs into a church (coand slams the door shut."""),
    ("A2.010", "ACT I", "Scene 2: Palm Sunday Escape", """ACTION: The swinging of the oil lamps stops. The lights come back on and Clare is at the foot of Francis. Francis receives her. He takes out a pair of scissors and is about to cut her hair, as he does, he throws the scissors down. She runs to pick it up, asking for him to cut her hair again- he repeats throwing the scissors away twice more until finally, he cuts Clare's Hair."""),
    ("A2.011", "ACT I", "Scene 2: Palm Sunday Escape", """A male choir member hands Clare her habit and black cloth. She changes into her habit, removes her cloak. Francis is kneeling in front of Christ."""),
    ("A2.012", "ACT I", "Scene 2: Palm Sunday Escape", """Choir: Make me a channel of your peace."""),
    ("A2.013", "ACT I", "Scene 2: Palm Sunday Escape", """CLARE: “Once this is cut, there is no returning to the life you knew”, said Francis, right before he chopped off my hair. I was ready. I wanted to give myself completely. ( she gestures above) I was ready… But I wasn't leaving my life, I was giving it to God."""),
    ("A2.014", "ACT I", "Scene 2: Palm Sunday Escape", """Clare walks into her cell."""),
    ("B1.001", "ACT II", "Scene 1: Rebuild My House", """ACT 2\nACTION: Clare moves towards the font. There is silence. Francis is still kneeling in front of Christ."""),
    ("B1.002", "ACT II", "Scene 1: Rebuild My House", """Media: Lightning sound Strike\nSound: Lightning + Possible Whisper (Possibly Sean)"""),
    ("B1.003", "ACT II", "Scene 1: Rebuild My House", """Voice of CHRIST: “Francis, rebuild my house.”"""),
    ("B1.004", "ACT II", "Scene 1: Rebuild My House", """ACTION: Francis gets up, profound moment, Stretches out his arms, bows and leaves the sanctuary. ( He sits back down on his chair. )"""),
    ("B1.005", "ACT II", "Scene 1: Rebuild My House", """CLARE: (Clare moves to where Francis was kneeling and takes his place)"""),
    ("B1.006", "ACT II", "Scene 1: Rebuild My House", """San Damiano. The abandoned church where Francis heard Christ speak directly to him.\n‘Rebuild my house.’"""),
    ("B1.007", "ACT II", "Scene 1: Rebuild My House", """And so Francis obeyed and with his brothers, using their bare hands. Brick by brick. Day after day, they rebuilt San Damiano. Of course—he— (She points upwards.) —was asking Francis to rebuild much more than just this little abandoned church!"""),
    ("B1.008", "ACT II", "Scene 1: Rebuild My House", """But for me... San Damiano became my place of rest, my place of prayer, my...home."""),
    ("B1.009", "ACT II", "Scene 1: Rebuild My House", """Sound: cicadas"""),
    ("B1.010", "ACT II", "Scene 1: Rebuild My House", """ACTION:\nClare walks slowly into her cell to a window by her desk. The sound of cicadas begins."""),
    ("B1.011", "ACT II", "Scene 1: Rebuild My House", """Media: Garden/ night? Stars?"""),
    ("B1.012", "ACT II", "Scene 1: Rebuild My House", """CLARE:\nIf you listen closely to the sound of the cicadas, you can hear them chant, Deus,Deus,Deus, God, God, God."""),
    ("B1.013", "ACT II", "Scene 1: Rebuild My House", """For the next 40 years, I would live here- simply. No niceties. No four course dinners. No possessions."""),
    ("B1.014", "ACT II", "Scene 1: Rebuild My House", """She is quiet"""),
    ("B1.015", "ACT II", "Scene 1: Rebuild My House", """I was home, here, God’s home for me, surrounded by God, everywhere.\nDeus,Deus,Deus.\nSolitude, Peace."""),
    ("B1.016", "ACT II", "Scene 1: Rebuild My House", """But life away from my carrisima famiglia (dearest family) didn't come without its hardships. I am human after all."""),
    ("B1.017", "ACT II", "Scene 1: Rebuild My House", """My padre was furious at what I had done.\nYou think I didn't ache for my family? I am only human."""),
    ("B1.018", "ACT II", "Scene 1: Rebuild My House", """I had to learn to let go of my father’s home to totally give myself to God.\nUnder Francis and his brothers, The Franciscan way of living, there was a new home to build.\nAnd now there was a new branch of this tree to grow, The Order of the Poor Ladies."""),
    ("B2.001", "ACT II", "Scene 2: Agnes Arrives", """I felt nervous, afraid and even alone. I was in a world within a world at San Damiano and Francis and his brothers were out in the world. We could not have been further apart and yet- I just knew, my father was looking after me."""),
    ("B2.002", "ACT II", "Scene 2: Agnes Arrives", """Media: sunrise (cosmic mode)"""),
    ("B2.003", "ACT II", "Scene 2: Agnes Arrives", """And then one day, as I slowly came out of prayer- there she was, in the corner of my eyes, My sister Agnes. And that new branch which was all alone, suddenly felt its leaves and spread its roots."""),
    ("B2.004", "ACT II", "Scene 2: Agnes Arrives", """ACTION: Clare turns around and sees St Agnes, her younger sister, emerge from the sanctuary."""),
    ("B2.005", "ACT II", "Scene 2: Agnes Arrives", """Song: Agnes comes on singing “Jesus loves me” In Italian"""),
    ("B2.006", "ACT II", "Scene 2: Agnes Arrives", """AGNES: Mea soror. (My sister)"""),
    ("B2.007", "ACT II", "Scene 2: Agnes Arrives", """CLARE: Mea soror. (My sister) you have followed me."""),
    ("B2.008", "ACT II", "Scene 2: Agnes Arrives", """ACTION: Clare puts on the veil and habit for her sister. The two sisters embrace."""),
    ("B2.009", "ACT II", "Scene 2: Agnes Arrives", """MUSIC:\nSong Interlude ‘Story of St Clare’: Sung by either Friar Derrick or Acapella Choir."""),
    ("C1.001", "ACT III", "Scene 1: Mirrors of Love", """ACT 3\nScene 1\nACTION:\nThe scene opens with Clare and Francis circling each other. As if they are mirrors of each other. They both end up gazing at Christ."""),
    ("C1.002", "ACT III", "Scene 1: Mirrors of Love", """Francis and her gaze at each other. Francis walks to Stage Right by the tree. Clare remains gazing at Francis.\nFrancis remains on stage the entire time watching this scene take place."""),
    ("C1.003", "ACT III", "Scene 1: Mirrors of Love", """CLARE: Some of you may think, I am in love with Francis ( She chuckles) You are not wrong, you are not right! It was through Francis—that I discovered my own fire burning, a hidden treasure in my own heart set aflame. Cor meum aredebat. ( my heart was burning!)"""),
    ("C1.004", "ACT III", "Scene 1: Mirrors of Love", """But it is Christ I am in love with, not Francis."""),
    ("C1.005", "ACT III", "Scene 1: Mirrors of Love", """To know Christ, I had to follow him into his poverty. To become like him. I needed to live as he did. No property to our name. No belongings. No possession."""),
    ("C1.006", "ACT III", "Scene 1: Mirrors of Love", """(she walks towards the font and gazes into the reflection of the water)\nTo contemplate, consider, gaze and imitate him."""),
    ("C2.001", "ACT III", "Scene 2: The Sisterhood", """Media (a convergence of women)\nAI Timelapse\nAs Clare speaks, the women begin to enter one by one. They simply arrive, as women arriving at San Damiano. (AI this part - women walking in and out of monastery)"""),
    ("C2.002", "ACT III", "Scene 2: The Sisterhood", """ACTION: Sister Agnes walks onto stage and places a bowl before her with a jug. Clare looks at her sister and then all the sisters on the screen/media."""),
    ("C2.003", "ACT III", "Scene 2: The Sisterhood", """Agnes places the bowl into the hands of Clare and helps her pour the water into the bowl."""),
    ("C2.004", "ACT III", "Scene 2: The Sisterhood", """Clare gestures to Agnes and she proceeds to wash Agnes’s foot."""),
    ("C2.005", "ACT III", "Scene 2: The Sisterhood", """CLARE: And as time went by, it wasn’t just me who wanted this. My dear sister joined me and then, after my dear padre’s death, even my sweet mama Ortolana. Other women of my time, women who grew tired of all social norms, of idly spending their days counting nuggets of gold, collecting diamonds and pearls—of hoping for the love of husbands rather than the love of life itself—these women came with burning hearts through the doors of San Damiano. All wanting to be the virgins of Christ."""),
    ("C2.006", "ACT III", "Scene 2: The Sisterhood", """CLARE:\nOur sisterhood was growing.\nFrancis ordered me to be their mother. Oh, at first I declined! No, I couldn’t. I wouldn’t."""),
    ("C2.007", "ACT III", "Scene 2: The Sisterhood", """How could one be superior over another? We were all sisters in poverty."""),
    ("C2.008", "ACT III", "Scene 2: The Sisterhood", """Movement: She dries Agnes’s foot for her."""),
    ("C2.009", "ACT III", "Scene 2: The Sisterhood", """But over time, I accepted the role Francis wanted me to step into. I became the Mother of the Order of the Poor Ladies."""),
    ("C2.010", "ACT III", "Scene 2: The Sisterhood", """(Approaches an audience member) May I have the honor of washing your feet?"""),
    ("C2.011", "ACT III", "Scene 2: The Sisterhood", """CLARE: (she washes an audience member's foot) Mama mia, are you enjoying it? (to audience member) It is a bit like a foot massage, no? A free foot massage. (They share a laugh)"""),
    ("C2.012", "ACT III", "Scene 2: The Sisterhood", """She becomes more solemn."""),
    ("C2.013", "ACT III", "Scene 2: The Sisterhood", """Francis placed me at the helm of the Poor Clares. It was a big responsibility to train them to ignore the needs of the fragile body, not to give into carnal frivolity- to forget their father’s homes to be pleasing to God- to understand labour so they do not become a kind of careless sluggish. To be silent- to hear God and allow holy love in."""),
    ("C2.014", "ACT III", "Scene 2: The Sisterhood", """She dries the audience members' feet."""),
    ("C2.015", "ACT III", "Scene 2: The Sisterhood", """You see, for me, it was never suffering for the sake of suffering. It was becoming like Him. And if He entered into poverty, if He entered into suffering, then I wanted to follow Him there. As he sacrificed his life for us on that cross, I would carry my cross for life- to become like him."""),
    ("C2.016", "ACT III", "Scene 2: The Sisterhood", """Silence."""),
    ("C2.017", "ACT III", "Scene 2: The Sisterhood", """CLARE: Was that a good foot massage? Wonderful. Please, please, give this person some love, show them some love for being so brave."""),
    ("C2.018", "ACT III", "Scene 2: The Sisterhood", """Clare smiles, followed by silence."""),
    ("C3.001", "ACT III", "Scene 3: The Departure of Francis", """SEAN makes a guest appearance. Canticle of Creatures begins to play on guitar. (https://www.youtube.com/watch?v=rxJ-lgBjdMM) (finger pluckstyle)"""),
    ("C3.002", "ACT III", "Scene 3: The Departure of Francis", """CLARE: Through it all, I had Francis as my spiritual guide. He came so often to preach to us sisters. He was our anchor in the night, our sunshine in the day- our sun, our moon, our stars."""),
    ("C3.003", "ACT III", "Scene 3: The Departure of Francis", """Francis walks and sits in front of Clare, She washes his feet."""),
    ("C3.004", "ACT III", "Scene 3: The Departure of Francis", """In 1225, after all his travels, after receiving the stigmata, his journey to the East- My Francis was nearly blind, body broken down by severe fasting, malaria... He could barely walk."""),
    ("C3.005", "ACT III", "Scene 3: The Departure of Francis", """He came to be with us sisters. I built him a small reed house just outside our monastery in our garden and cared for him."""),
    ("C3.006", "ACT III", "Scene 3: The Departure of Francis", """The song is sung and she washes his feet quietly."""),
    ("C3.007", "ACT III", "Scene 3: The Departure of Francis", """And then one day, Francis was gone."""),
    ("C4.001", "ACT III", "Scene 4: The First Letter", """Scene 3\nSound : The Canticle of Creatures Transitions.\nChoir: Canticle of Creatures Transition to end\nSean: Transition to end of song."""),
    ("C4.002", "ACT III", "Scene 4: The First Letter", """MOVEMENT PIECE:\nFrancis slowly leaves the stage, ritually- following the slowness or melancholy of the music."""),
    ("C4.003", "ACT III", "Scene 4: The First Letter", """Once Francis is completely off stage, Clare whispers.\nCLARE: “O blessed Father, What will become of us without you?”\nSilence"""),
    ("C4.004", "ACT III", "Scene 4: The First Letter", """Scene 4\nClare walks to her desk. She is staring out of the window."""),
    ("C4.005", "ACT III", "Scene 4: The First Letter", """CLARE:\nWhen Francis passed on, I was hit by an overwhelming grief. I withdrew into a profound silence."""),
    ("C4.006", "ACT III", "Scene 4: The First Letter", """My comrade. My brother. My mentor. My guide. My heart."""),
    ("C4.007", "ACT III", "Scene 4: The First Letter", """For me, as far away as the Moon was from my Earth, what comforted me was knowing that I could at least look at the night sky and know you are there. You are near. You are near me, my Francis."""),
    ("C4.008", "ACT III", "Scene 4: The First Letter", """Beat.\nWe are human, after all.\nBeat."""),
    ("C4.009", "ACT III", "Scene 4: The First Letter", """She looks towards Christ.\nCLARE:\nAnd so I learned to let go."""),
    ("C4.010", "ACT III", "Scene 4: The First Letter", """Clare is deteriorating physically. She gets weaker and it is shown in her stature."""),
    ("C4.011", "ACT III", "Scene 4: The First Letter", """Light: A light shines bright by her desk. She notices it."""),
    ("C4.012", "ACT III", "Scene 4: The First Letter", """(Clare gets up and experiences a light, she moves towards it and it leads her to her desk)"""),
    ("C4.013", "ACT III", "Scene 4: The First Letter", """But out of that grief, there shone a light. ( she lifts a piece of paper to the light. It is a letter.)"""),
    ("C4.014", "ACT III", "Scene 4: The First Letter", """A princess who chose to give everything to Christ."""),
    ("C4.015", "ACT III", "Scene 4: The First Letter", """Media: Show St Agnes of Prague - news style AI - Princess that gave everything up to be poor - find or create scenes"""),
    ("C4.016", "ACT III", "Scene 4: The First Letter", """A princess (beat) Agnes of Prague, choosing to abandon her Royalty to become a Poor lady. She left everything behind to follow the ways of Francis and his friars and the ways of the Order of the Poor Ladies."""),
    ("C4.017", "ACT III", "Scene 4: The First Letter", """A light in the darkness. She became my second comrade."""),
    ("C4.018", "ACT III", "Scene 4: The First Letter", """(She moves to the reflection in the water-likened to a mirror)"""),
    ("C4.019", "ACT III", "Scene 4: The First Letter", """And if I was gazing at Francis, gazing at Christ, Agnes of Prague would gaze at me gazing at Christ. All of us, Mirrors of love. All reflecting the heart of Jesus."""),
    ("C4.020", "ACT III", "Scene 4: The First Letter", """Choir: Hymn Transitions into Act 4 as she is writing."""),
    ("C4.021", "ACT III", "Scene 4: The First Letter", """The media plays"""),
    ("D1.001", "ACT IV", "Scene 1: The Soldiers", """ACT 4\nScene 1\nMovement: Clare is seen writing, with pen and paper (visibly weaker)- until something magical happens and she starts to move and dance with the pen and paper full of physicality."""),
    ("D1.002", "ACT IV", "Scene 1: The Soldiers", """MEDIA OLDER CLARE (LETTER 1) VOICE OVER :\n(she writes) Dear Agnes of Prague…hmmm, how shall i put this to her… you chose a simple life of poverty so that you could belong completely to Jesus Christ. And you chose the most wonderful bridegroom anyone could ever have—Jesus himself."""),
    ("D1.003", "ACT IV", "Scene 1: The Soldiers", """Oh Agnes…\nIf you love him, you will remain pure. If you stay close to him, he will make you holy. If you give yourself to him completely, your life will belong to God. Jesus is stronger than any earthly ruler. He is more generous and beautiful than anyone else. His love is gentler than any human love. His kindness is beyond comparison. He has already embraced you."""),
    ("D1.004", "ACT IV", "Scene 1: The Soldiers", """So, my beloved sister, you are now the bride, the sister, and even the mother of Christ because your whole life belongs to him."""),
    ("D1.005", "ACT IV", "Scene 1: The Soldiers", """SOUND:\nSound of the soldiers entering Assisi.The sound builds. This sound is also mixed with modern sounds of traffic handphones etc."""),
    ("D1.006", "ACT IV", "Scene 1: The Soldiers", """(She hears the sounds of soldiers, her face seems distressed and worried )"""),
    ("D1.007", "ACT IV", "Scene 1: The Soldiers", """Media: On-coming soldiers / could be spliced with war/ tanks etc"""),
    ("D1.008", "ACT IV", "Scene 1: The Soldiers", """Sound of Voices :\n“What do we do, Mother? The soldiers are coming!”\n“They are coming close! They're going to kill us!”\n“Oh Lord, Jesus our Saviour, help us!”"""),
    ("D1.009", "ACT IV", "Scene 1: The Soldiers", """“ I am afraid!We are trapped! Lord, Lord save us!”"""),
    ("D1.010", "ACT IV", "Scene 1: The Soldiers", """ACTION: Clare is seen to put her pen and paper down. She draws close, worried and pacing. The sound of the soldiers approaching is unbearable, she is filled with fear and uncertainty until she finally breaks."""),
    ("D1.011", "ACT IV", "Scene 1: The Soldiers", """CLARE: Dear Lord, what shall be done? What can I do to stop this?\nDear Lord! Please, please protect us! Where are you!?"""),
    ("D1.012", "ACT IV", "Scene 1: The Soldiers", """She kneels down and prays to Jesus."""),
    ("D1.013", "ACT IV", "Scene 1: The Soldiers", """CLARE:\nJesus, please protect your Poor Ladies, who have only ever shown you love!\nI cannot do this alone!"""),
    ("D1.014", "ACT IV", "Scene 1: The Soldiers", """VOICE OF CHRIST AS A CHILD:\nI will always protect you."""),
    ("D1.015", "ACT IV", "Scene 1: The Soldiers", """Clare hears the voice and reacts with profound calm and walks towards the Eucharist. She takes it and holds it up out the walls of Assisi to the soldiers."""),
    ("D1.016", "ACT IV", "Scene 1: The Soldiers", """Media: There is another magical moment here of profound clarity and magical calm, perhaps shown through the media."""),
    ("D1.017", "ACT IV", "Scene 1: The Soldiers", """ACTION: After a long beat, the soldiers withdraw and leave. We can create sound to feel this. Leaving Clare and the sisters, perhaps also shown in multi-media, alone on the stage. Relieved. Breathing fast but relieved."""),
    ("D1.018", "ACT IV", "Scene 1: The Soldiers", """MEDIA : The image of a mirror comes unto the media. It is meant to reflect the audience at that point as if we are gazing into a reflection where we gaze, contemplate, maybe within the reflection, we see Christ in the mirror or image or a heart or the Sacred Eucharist."""),
    ("D1.019", "ACT IV", "Scene 1: The Soldiers", """The only sound left is the sound of Clare breathing her heartbeat."""),
    ("D1.020", "ACT IV", "Scene 1: The Soldiers", """Clare: Do not be afraid. He is here, he has always been here."""),
    ("D2.001", "ACT IV", "Scene 2: The Second Letter", """Scene 2\nShe is writing but is frail and weaker. While this is shown in the media, she walks to the water font. A light as if a mirror is reflected into the water shining back at her. )"""),
    ("D2.002", "ACT IV", "Scene 2: The Second Letter", """Multi Media OLDER CLARE (Letter 2): ( she stares into the mirror, on multi media) My beloved sister, Agnes of Bohemia. You have turned from an earthly kingdom and chosen Christ. So remember why you began. What you have chosen, hold fast. What you have begun, do not abandon. Embrace the poor Christ. Follow Him. Gaze upon Him. Consider Him. Contemplate Him. If you suffer with Him, you will share in His glory. Hold fast to Christ. And keep walking.\nYour sister, Clare."""),
    ("D2.003", "ACT IV", "Scene 2: The Second Letter", """She drops her pen and is visibly a lot weaker but yet, holding onto faith, she walks to station 1 ( by the cross) and says the rosary."""),
    ("D2.004", "ACT IV", "Scene 2: The Second Letter", """Choir: A Christmas Hymn is sung typically the ones sung on christmas eve"""),
    ("D3.001", "ACT IV", "Scene 3: Christmas Eve Mass", """Scene 3\nClare’s sister Agnes comes onto stage and forces Clare to eat but she refuses. Agnes tries again. Clare refuses."""),
    ("D3.002", "ACT IV", "Scene 3: Christmas Eve Mass", """AGNES:\nSister, please eat. If our dear Father Francis were alive, he would have reminded you to eat too. Do not punish yourself so severely. Remember too, you are unwell."""),
    ("D3.003", "ACT IV", "Scene 3: Christmas Eve Mass", """CLARE:\nSister, do not tell the others that I have not eaten. Sometimes I get so carried away in my thirst for Christ, I myself forget myself."""),
    ("D3.004", "ACT IV", "Scene 3: Christmas Eve Mass", """AGNES:\nSister, let me help you up. Let us get ready for Christmas Eve Mass."""),
    ("D3.005", "ACT IV", "Scene 3: Christmas Eve Mass", """Clare falls down each time Agnes attempts to help her."""),
    ("D3.006", "ACT IV", "Scene 3: Christmas Eve Mass", """CLARE:\nMy Agnes… my Agnes, It seems that I am unable to attend Mass tonight."""),
    ("D3.007", "ACT IV", "Scene 3: Christmas Eve Mass", """AGNES:\nLooking concerned. It is best if you rest here tonight. Mia mama Ortolana will be joining us too in the chapel. We will pray for you, dear one. ( she makes to leave) See you after Mass."""),
    ("D3.008", "ACT IV", "Scene 3: Christmas Eve Mass", """OLDER CLARE: Good. Good. Thank you My Agnes, my sweet sister.\nAgnes leaves. Clare watches her go. She begins to sob."""),
    ("D3.009", "ACT IV", "Scene 3: Christmas Eve Mass", """Oh, my … All my life I have wanted to be strong for Him, and now I can barely even stand."""),
    ("D3.010", "ACT IV", "Scene 3: Christmas Eve Mass", """She laughs softly through her tears. She looks towards Christ."""),
    ("D3.011", "ACT IV", "Scene 3: Christmas Eve Mass", """OLDER CLARE:\nMy Lord. My Lord. ( she breaks down laughing in tears and irony)\nLord God, Look, I have been left here alone with you."""),
    ("D3.012", "ACT IV", "Scene 3: Christmas Eve Mass", """A moment of silence."""),
    ("D3.013", "ACT IV", "Scene 3: Christmas Eve Mass", """Then—A holy light begins to fill the barren cell. At first, faintly, Clare hears the distant ringing of church bells. She looks up. The sound grows.The Mass. The liturgy. The voices of the congregation. The great organ. The hymns. The grey, empty cell is transformed by light and sound. It is as though the walls have fallen away and Clare has been given a glimpse of the Mass she is unable to attend.Clare is completely overwhelmed.She rises instinctively, then stops. She sees something beyond the mass.Her breath catches.Slowly, she kneels.She weeps—not from sorrow now, but from wonder.She makes the sign of the cross.Clare remains there, gazing upwards, utterly still.The music continues.The light holds."""),
    ("D3.014", "ACT IV", "Scene 3: Christmas Eve Mass", """Replicate a 13th century mass with AI\nChoir: Sings a very vibrant and upbeat Hymn/Song/Prayer"""),
    ("D3.015", "ACT IV", "Scene 3: Christmas Eve Mass", """CLARE:\nBlessed be the Lord Jesus Christ.\nSilence.\nYou did not leave me.\nShe smiles."""),
    ("D3.016", "ACT IV", "Scene 3: Christmas Eve Mass", """I heard them all. The singing. The prayers. All those solemnities...\nI was there."""),
    ("D3.017", "ACT IV", "Scene 3: Christmas Eve Mass", """She looks around her cell.\nAnd yet... I was here."""),
    ("D3.018", "ACT IV", "Scene 3: Christmas Eve Mass", """Beat.\nThank you, Lord.\nShe kneels in prayer."""),
    ("D3.019", "ACT IV", "Scene 3: Christmas Eve Mass", """SOUND: Then, slowly, everything fades except the sound of her breathing and her heart beat."""),
    ("D3.020", "ACT IV", "Scene 3: Christmas Eve Mass", """Hymn: Make me a channel of your peace replays and transitions into the next act."""),
    ("D4.001", "ACT IV", "Scene 4: The Final Letters", """Third Letter— PART TWO\nACTION: Clare has reached the peak of her frailty. She is kneeling and recites the third letter. As if in prayer to Agnes. As if her thoughts could telepath and Agnes would receive her words."""),
    ("D4.002", "ACT IV", "Scene 4: The Final Letters", """OLDER CLARE (letter three):\nMy beloved Agnes,\nHold fast to what you have begun. ( she coughs) Hold fast to Christ. (she stands up weakly)"""),
    ("D4.003", "ACT IV", "Scene 4: The Final Letters", """Look upon Him. (she looks to Christ, back towards the audience)\nConsider Him.\nContemplate Him."""),
    ("D4.004", "ACT IV", "Scene 4: The Final Letters", """He whom the heavens cannot contain has chosen to dwell within you (she turns to address the audience)\nSo make room for Him. If you suffer with Him ( she almost falls over )\nOh my, God give me strength"""),
    ("D4.005", "ACT IV", "Scene 4: The Final Letters", """If you suffer with him, you will share in His glory.\nKeep looking at Him. Keep walking."""),
    ("D4.006", "ACT IV", "Scene 4: The Final Letters", """Your sister,\nClare."""),
    ("D4.007", "ACT IV", "Scene 4: The Final Letters", """Choir: Make me a channel of your peace transitions to an ending. ."""),
    ("D4.008", "ACT IV", "Scene 4: The Final Letters", """CLARE:\nWe are coming close to the ending of my story.\n(She sits on her stool.)"""),
    ("D4.009", "ACT IV", "Scene 4: The Final Letters", """You might wonder, ‘But why Clare? Must we live to suffer?’\nI invite you to imagine now. Imagine giving up everything- having nothing to your name. No wealth, no property, no shoes on your feet even- nothing. Nothing belongs to you on this Earth."""),
    ("D4.010", "ACT IV", "Scene 4: The Final Letters", """What is left in that nothingness?\nAh now I see, you see."""),
    ("D4.011", "ACT IV", "Scene 4: The Final Letters", """In that nothingness, there is still Christ.\nThis is what it is to suffer. This is the privilege of poverty."""),
    ("D4.012", "ACT IV", "Scene 4: The Final Letters", """(she looks up at Christ)"""),
    ("D4.013", "ACT IV", "Scene 4: The Final Letters", """Remember how I said, I was born into a life written for me? In this same way, even in the church of my time, as a woman, life was already written for us."""),
    ("D4.014", "ACT IV", "Scene 4: The Final Letters", """I wanted so much to live in the privilege of poverty (Privilegium Paupertatis), and The sisters and I desperately wanted to be given the right to live with no possession of anything material- property, land- absolutely nothing."""),
    ("D4.015", "ACT IV", "Scene 4: The Final Letters", """To live simply by the goodwill of the donation of alms. But at the time, The Pope, even though fond of me, as I was of him, was worried that as women, we would not be able to manage this extreme poverty. That as women, we needed to have corporate ownership, land for farming at least in order to sustain ourselves."""),
    ("D4.016", "ACT IV", "Scene 4: The Final Letters", """I had to unwrite the life written for women in monastic living and write a new rule. I demanded the right to live in the privilege of poverty."""),
    ("D4.017", "ACT IV", "Scene 4: The Final Letters", """.....And I knew I was sick, frail and perhaps, dare I say, even dying. There was little time left ( she coughs )"""),
    ("D4.018", "ACT IV", "Scene 4: The Final Letters", """Media: A repeat of the first part, noise and intro and worldly matters and the Jesus cross being illuminated."""),
    ("D4.019", "ACT IV", "Scene 4: The Final Letters", """CLARE ( FOURTH LETTER) :\nClare writes and her words are shown on the screen as if it were a touch phone screen. She types only the first few sentences."""),
    ("D4.020", "ACT IV", "Scene 4: The Final Letters", """Media & said by Clare:\nMy beloved sister Agnes of Prague,"""),
    ("D4.021", "ACT IV", "Scene 4: The Final Letters", """When the world becomes noisy or confusing, remember where your heart belongs. Place your mind in the mirror of eternity. Place your soul in the splendour of heaven. Place your heart in Christ. Look at Him until you become like Him. He gave Himself completely for you. So give yourself completely to Him."""),
    ("D4.022", "ACT IV", "Scene 4: The Final Letters", """( She walks to the font and gazes into it as a mirror)\n( The media stops displaying the text)"""),
    ("D4.023", "ACT IV", "Scene 4: The Final Letters", """And remember Mary, who carried Christ within her. You too can carry Him within your heart."""),
    ("D4.024", "ACT IV", "Scene 4: The Final Letters", """Our blessed Father Francis taught us to fast, but remember, each of you, that our flesh is not made of bronze, nor our strength of stone. I know how severely some of you fast, in your own ways. Do not be so hard on yourselves. We must care for the body so that we may continue to praise the Lord."""),
    ("D4.025", "ACT IV", "Scene 4: The Final Letters", """Our poverty is not punishment. Your poverty is not punishment. It is your gift.\nIt is love."""),
    ("D4.026", "ACT IV", "Scene 4: The Final Letters", """Rejoice, each and all of you. Remember to carry Christ within you.\nAnd remember me, remember me and my sisters in your prayers.\nAlways,\nYour sister in Christ, Clare."""),
    ("D4.027", "ACT IV", "Scene 4: The Final Letters", """Choir: Canticle of Creatures in a more traditional tone. . The choir comes downstage to join Clare. She is sitting by the Font."""),
    ("E1.001", "EPILOGUE", "Scene 1: Learning to Gaze", """EPILOGUE\nACTION: Clare gazes at Christ by the font. (Christ is lit)"""),
    ("E1.002", "EPILOGUE", "Scene 1: Learning to Gaze", """CLARE: I have spent my life learning to gaze.\nNot to possess.\nNot to hold, not even to be held…\nOnly to remain.\nTo look upon him, until I became, little by little, what I was looking at."""),
    ("E1.003", "EPILOGUE", "Scene 1: Learning to Gaze", """Clare is looking up at Christ.Christ is illuminated."""),
    ("E1.004", "EPILOGUE", "Scene 1: Learning to Gaze", """11 AUGUST 1253\nClare of Assisi died at San Damiano."""),
    ("E1.005", "EPILOGUE", "Scene 1: Learning to Gaze", """Two days earlier:\nPope Innocent IV approves the Rule of Life she had written for her sisters.\nThe first rule written by a womanfor a community of women religious."""),
    ("E1.006", "EPILOGUE", "Scene 1: Learning to Gaze", """Clare looks at the audience. Black out.""")
]

headers = [
    "Beat ID", "Chapter", "Production Scene", "Full Script Text / Action",
    "Dramatic Purpose / Emotional State", "SHARDA / CLARE — Position & Performance State",
    "Other Performer / Staging Action", "Profile Light 1", "Profile Light 2",
    "Projector / Multimedia", "Choir / Vocal Layer", "SFX / Playback Layer",
    "Analog Synth Layer", "Cue IN Trigger", "Development / Behaviour",
    "Cue OUT Trigger", "Transition / Next State", "Standby / Operator Notes",
    "Design Status"
]

rows = []

for beat in raw_beats:
    b_id, chap, scene, text = beat
    
    # Defaults
    purpose = "TBD - DIRECTORIAL"
    sharda = "HOLD"
    other = "HOLD"
    l1 = "HOLD"
    l2 = "HOLD"
    media = "NONE"
    choir = "NONE"
    sfx = "NONE"
    synth = "TBD"
    status = "TBD"
    
    tl = text.lower()
    
    # Simple heuristic parsing
    if "action:" in tl or "movement:" in tl or "clare" in tl or "she" in tl:
        sharda = "TBD - Update from text"
        status = "CUE"
        if "kneel" in tl: sharda = "Kneeling"
        elif "walk" in tl: sharda = "Walking"
        elif "sit" in tl: sharda = "Sitting"
        
    if "francis" in tl or "agnes" in tl or "choir" in tl or "voice" in tl:
        other = "TBD - Update from text"
        status = "CUE"
        
    if "light" in tl:
        l1 = "CUE"
        l2 = "CUE"
        status = "CUE"
        
    if "media:" in tl or "projector" in tl or "screen" in tl:
        media = "CUE - " + text.split("\\n")[0][:100]
        status = "CUE"
        
    if "sound:" in tl or "sound design:" in tl or "sfx" in tl:
        sfx = "CUE - " + text.split("\\n")[0][:100]
        status = "CUE"
        
    if "choir:" in tl or "song:" in tl or "music:" in tl or "hymn" in tl:
        choir = "CUE - " + text.split("\\n")[0][:100]
        status = "CUE"
        
    # Manual overrides for the first beat
    if b_id == "P1.001":
        purpose = "Establish environment"
        sharda = "Intermittently between 3 stations"
        other = "Francis seated stage right. Choir stage left."
        status = "LOCKED"
        
    # Cue IN Trigger (first few words)
    words = text.replace("\\n", " ").split()
    cin = " ".join(words[:5]) + "..." if words else "TBD"
    
    rows.append({
        "Beat ID": b_id,
        "Chapter": chap,
        "Production Scene": scene,
        "Full Script Text / Action": text.replace("\\n", "  "),
        "Dramatic Purpose / Emotional State": purpose,
        "SHARDA / CLARE — Position & Performance State": sharda,
        "Other Performer / Staging Action": other,
        "Profile Light 1": l1,
        "Profile Light 2": l2,
        "Projector / Multimedia": media,
        "Choir / Vocal Layer": choir,
        "SFX / Playback Layer": sfx,
        "Analog Synth Layer": synth,
        "Cue IN Trigger": cin,
        "Development / Behaviour": "TBD",
        "Cue OUT Trigger": "TBD",
        "Transition / Next State": "TBD",
        "Standby / Operator Notes": "",
        "Design Status": status
    })

with open("master_production_cue_matrix.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    writer.writerows(rows)
    
print("Successfully generated master_production_cue_matrix.csv")
