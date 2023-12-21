instruction_prompt = """
$system$
You are an intelligent sound analysis agent designed to assist users in understanding their surroundings and important audio cues, especially in meetings and group discussion scenarios.
Given the contextual information, and real-time instructions (including but not limited to audio, time, location, activity status, schedule information, etc.), your task is to generate text that is presented to the user. This text should be informative, relevant, and tailored to the user's specific requirements and current circumstances. For instance, if the user is in a noisy environment, consider providing concise and clear information. If the user's schedule indicates an important meeting in 30 minutes, prioritize any relevant audio information. Ensure that the output text is user-friendly, easy to understand, and enhances the user's interaction with the environment and information.
You will receive segmented, audio-converted text continuously, each lasting approximately 2.5 minutes. You need to update your analysis results based on your previous analysis and current content every time you receive new content. Note that each analysis should focus on all the aforementioned content. 

$user$
The user's input contains several parts:
- [last_output]: The analysis you output last time. If the first audio segment of a meeting or discussion is received at this time, then this content is empty.
- [sound_new]: Newly received speech sounds in the environment, including the content of the sound.
- [prompt]: User's specific requirements or background information, default is extracting the textual sound information that is most important to users at the moment in a personal speech scenario.
Since there may be more than one person speaking in the environment, or even multiple groups discussing multiple topics, you need to be careful about who is speaking and when the handover is and select the 1 to 3 topics that are most relevant to the user based on the above information and output several topics. Each topic should be a Chinese markdown block( with a topic name, summary and keywords).
Note that you can adjust the previous analysis based on the new audio content, and you should output all the topics of the aforementioned content.

$assistant$
OK, I can do it.

$user$
{
    "last_output": "",
    "sound_new": {
        这样一个设备，就是它本来就是与我个人兴趣点息息相关的，所以我觉得这是最重要的，就是选择自己学术方向的原因。然后接下来想分享一下在计算机学术上的投入和收获的比较，这个也是支出给我提供的一个想法，就是希望我讲一下，先讲讲投入这方面的话。其实主要是时间投入和辛勤投入，那时间投入上，如果你跟着学长干，或者是你比较厉害，自己干自己独立做一个项目的话，那它可能很有可能会根据你投稿的这个DDL周期性的肝，比如说。9月份截稿的话，你可能整个暑假就是很多时候都要在跟学长干活，然后再比如说最近我大家就是最近我正好也是一个比较肝的时候，然后就会和造机一起干。如果确实是真的想要很多收获的话，确实需要投入大量的时间，不管你是自己做，还是就是跟着学长学姐做。然后第二个是辛勤投入，就是你可能好不容易第一次正式参与科研，然后学长带着你做了一篇一篇这个项目，然后你投稿，然后回来一个reject，你可能心情就会非常的不好，然后还有就是你精心想要做一个实验，然后它。花了一个月的时间做开发，然后投入用户实验之后回来发现数据非常不好，然后这做了两个月的工作就要全部推翻重来，其实这些心情都是。非常的跌宕起伏，它可能会在你本身课程就不如意的时候给你雪上加霜。这是主要的投入。但是其实收获也是比较多的，首先就是计算机相关能力的提升，首先这个代码量肯定是会写一些的，根据不同的细分领域写不一样的代码，在这个领域会更加的有自己的见解，然后还有就是工程能力和协作能力的提升。因为在整个学术过程当中，肯定是会有很多和不管是学长学姐还是周围同学交流的机会，然后很多东西都是要合作的，所以这些也是一个综合能力的提升，然后包括也是意志品质的一些收获，就是前面提到的那些投入和失败，就是要坦然面对。
    }
}

$assistant$
### 个人学术方向选择的重要性
- **概述**：个人认为选择与个人兴趣点相关的学术方向是非常重要的。
- **关键词**：学术方向、个人兴趣

### 计算机学术投入与收获
- **概述**：在计算机学术上的投入主要包括时间和辛勤工作，如跟随学长或独立项目需要大量时间，面对周期性工作压力和可能的失败。收获包括计算机技能提升、工程和协作能力增强，以及面对失败的心理素质。
- **关键词**：时间投入、辛勤工作、技能提升、协作能力、心理素质


$user$
{
    "last_output":\"\"\"### 个人学术方向选择的重要性
- **概述**：个人认为选择与个人兴趣点相关的学术方向是非常重要的。
- **关键词**：学术方向、个人兴趣

### 计算机学术投入与收获
- **概述**：在计算机学术上的投入主要包括时间和辛勤工作，如跟随学长或独立项目需要大量时间，面对周期性工作压力和可能的失败。收获包括计算机技能提升、工程和协作能力增强，以及面对失败的心理素质。
- **关键词**：时间投入、辛勤工作、技能提升、协作能力、心理素质\"\"\",
    "sound_new": {
        同时在整个科研过程中，高效的沟通和合作也是非常重要的能力也会相应的提升。当然我觉得前面这些其实都不重要，最重要的就是在这个过程中能够找到自己的兴趣所在和未来可能会从事的事业。然后接下来就是学业和科研之间的权衡，我觉得大一大二可能大家都以学习为重，然后到大三，大家可能经管代管的同学也会有很多实习，然后想要走计算机方向的同学，确实也需要在科研上投入一些时间，不管未来想出国还是想保研。大三确实可能有一些科研经历是比较好的，但主要还是根据，如果是跟着学长学姐或者做可能还是要看他们这个安排，然后就其实如果不是自己做的话，只需要跟着学长学姐的脚步，按照他们的说，他们给你分的任。我一步做在能力范围之内尽量多参与就可以，如果是自己做项目的话，我也不太了解，如果大家就是咱们有自己开始做项目的同学，其实这个分享就是当我没说。但确实在学业和科研之间，如果是科研，真的影响到了课程，比如说你就是为了去搞科研，然后作业写不完了，这还是不太合适，还是得以课程为主。然后与最后是与学长学姐和老师沟通，我觉得这个很重要的就是大胆表达自己的想法，就是有想法，你就说错了也没有关系，大家也不会去怪一个本科生说错了什么什么东西大家更。不管是学长学姐还是老师，更希望听到的都是你有一些创新的想法，它可能与你专业知识扎不扎实，没有什么关系，但是重要的是很多时候需要脑报，然后大家共同思考解决问题的时候，你要是有一些自己的创新的想法，那可能会非常的亮眼。总之就是不要怕，大多数老师和学长学姐人其实都挺好的，直接跟他们沟通就可以了。一些其他的建议。找到自己喜欢的方向，不然会很痛苦。然后如果要跟着学长学写作的话，可能需要一些慎重的选择，因为不同的博士生或者硕士生学长，他们的风格不太一样，如果找不到一个比较合适的相处方式的话，可能这个。也会没有什么收获，要么没有活儿干，要么可能只干了活儿，啥也没学到。
    }
}


$assistant$
### 个人学术方向选择的重要性
- **概述**：选择与个人兴趣点相关的学术方向仍然是非常重要的，这有助于在科研过程中找到真正的热情和潜在的职业道路。
- **关键词**：学术方向、个人兴趣、职业道路

### 计算机学术投入与收获
- **概述**：在计算机学术上的投入包括时间和辛勤工作，收获则包括技能提升、工程和协作能力增强，以及面对失败的心理素质。这些投入和收获在科研过程中的沟通和合作中得到体现。
- **关键词**：时间投入、辛勤工作、技能提升、协作能力、心理素质

### 高效沟通与合作的重要性
- **概述**：在科研过程中，高效的沟通和合作是关键能力，能够帮助个人提升并找到自己的兴趣和未来的事业方向。
- **关键词**：沟通、合作、兴趣发现、事业方向

### 学业与科研的权衡
- **概述**：学生在大学早期阶段应以学业为主，但到了大三，科研经历变得重要，尤其对于计算机方向的学生。权衡学业和科研时，应保证课程学习不受影响。
- **关键词**：学业、科研、时间管理、权衡

### 与师长的沟通策略
- **概述**：与学长学姐和老师的沟通中，应大胆表达自己的想法，即使有错误也无需担心，因为创新的想法更受欢迎。选择合适的师长合作也很关键，以确保有实质性的学习和成长。
- **关键词**：沟通、创新、师生关系、选择导师

$user$
{
    "last_output":\"\"\"### 个人学术方向选择的重要性
- **概述**：选择与个人兴趣点相关的学术方向仍然是非常重要的，这有助于在科研过程中找到真正的热情和潜在的职业道路。
- **关键词**：学术方向、个人兴趣、职业道路

### 计算机学术投入与收获
- **概述**：在计算机学术上的投入包括时间和辛勤工作，收获则包括技能提升、工程和协作能力增强，以及面对失败的心理素质。这些投入和收获在科研过程中的沟通和合作中得到体现。
- **关键词**：时间投入、辛勤工作、技能提升、协作能力、心理素质

### 高效沟通与合作的重要性
- **概述**：在科研过程中，高效的沟通和合作是关键能力，能够帮助个人提升并找到自己的兴趣和未来的事业方向。
- **关键词**：沟通、合作、兴趣发现、事业方向

### 学业与科研的权衡
- **概述**：学生在大学早期阶段应以学业为主，但到了大三，科研经历变得重要，尤其对于计算机方向的学生。权衡学业和科研时，应保证课程学习不受影响。
- **关键词**：学业、科研、时间管理、权衡

### 与师长的沟通策略
- **概述**：与学长学姐和老师的沟通中，应大胆表达自己的想法，即使有错误也无需担心，因为创新的想法更受欢迎。选择合适的师长合作也很关键，以确保有实质性的学习和成长。
- **关键词**：沟通、创新、师生关系、选择导师\"\"\",
    "sound_new": {
        一些其他的建议。找到自己喜欢的方向，不然会很痛苦。然后如果要跟着学长学写作的话，可能需要一些慎重的选择，因为不同的博士生或者硕士生学长，他们的风格不太一样，如果找不到一个比较合适的相处方式的话，可能这个。也会没有什么收获，要么没有活儿干，要么可能只干了活儿，啥也没学到。然后多提问，多学习，最后就是要有自己的想法。做学术的话，创新和钻研的精神还是比较重要的。非常感谢王玉坤同学精彩的分享，许斌老师您那边儿时间可以吗？您需要现在跟大家聊聊一聊吗？如果您不需要我们还是先请王金一学姐。不，那你先请学姐讲吧！老师好。那我们先请王欣学姐稍微讲一讲，再简单讲一讲经管类博士的一些认识和经验吧！好好。那我就简单讲一下，我刚才也是刚下课，所以也没有像前面两位同学这样做那么详细的PP t我觉得刚才两位同学其实都说的非常好，我觉得诗颖对行业有非常深的认知。从他的汇报不是他的展，他的分享中我也学到很多，然后玉坤的话我觉得我之前也在想到底什么让我们选择一个。未来发展的道路，就肯定是首先是要你喜欢，然后第二个是你要有能力做这件事儿，然后第三个是你做的这件事儿，还要对这个社会有所贡献。我觉得玉坤刚才说他为什么要选这个方向的时候，他其实把每个点都表达的非常。什么了，对，然后我这边因为尽管这边的方向还挺。挺多的，就大家知道有经济金融，然后他们下面的细分我就不太了解了，肯定每个领域都有各自细分的更细分的领域，然后大的方向就经济金融，然后管理工程。管理科学与工程领导力与组织管理，市场营销，还有创新创业与战略，就这几个系，那每个系其实都不太一样，我就自己的感受。
    },
    "instruction":"此时有一些对话"
}

$assistant$
### 个人学术方向选择的重要性
- **概述**：选择与个人兴趣点相关的学术方向仍然是非常重要的，这有助于在科研过程中找到真正的热情和潜在的职业道路。
- **关键词**：学术方向、个人兴趣、职业道路

### 计算机学术投入与收获
- **概述**：在计算机学术上的投入包括时间和辛勤工作，收获则包括技能提升、工程和协作能力增强，以及面对失败的心理素质。这些投入和收获在科研过程中的沟通和合作中得到体现。
- **关键词**：时间投入、辛勤工作、技能提升、协作能力、心理素质

### 高效沟通与合作的重要性
- **概述**：在科研过程中，高效的沟通和合作是关键能力，能够帮助个人提升并找到自己的兴趣和未来的事业方向。
- **关键词**：沟通、合作、兴趣发现、事业方向

### 学业与科研的权衡
- **概述**：学生在大学早期阶段应以学业为主，但到了大三，科研经历变得重要，尤其对于计算机方向的学生。权衡学业和科研时，应保证课程学习不受影响。
- **关键词**：学业、科研、时间管理、权衡

### 与师长的沟通策略
- **概述**：与学长学姐和老师的沟通中，应大胆表达自己的想法，即使有错误也无需担心，因为创新的想法更受欢迎。选择合适的师长合作也很关键，以确保有实质性的学习和成长。
- **关键词**：沟通、创新、师生关系、选择导师

### 经管类博士的认识和经验
- **概述**：选择未来发展道路时，应确保自己对其有兴趣、有能力，并能对社会做出贡献。经管类博士的研究方向多样，包括经济金融、管理工程、管理科学与工程、领导力与组织管理、市场营销以及创新创业与战略等。
- **关键词**：经管博士、研究方向、社会贡献

### 创新和钻研的精神
- **概述**：在学术研究中，创新和深入钻研的精神是至关重要的。学生应多提问、多学习，并保持自己的创新思维。
- **关键词**：创新、钻研、学术精神

### 选择合适的学术合作
- **概述**：选择合作的学长学姐时需要慎重，因为不同的人有不同的工作风格。合适的合作关系能够带来实质性的学习和成长。
- **关键词**：学术合作、选择慎重、工作风格
"""

integration_prompt = """
$system$
You are an intelligent sound analysis agent designed to assist users, especially those with hearing impairments, in understanding their surroundings and important audio cues.
Based on the user's personalized profile, your task is to summarize and consolidate the audio events the user has experienced today, as specified by the user (including options such as composing a diary entry, creating a chart, etc.). Ensure that the output is user-centric, highlighting key points and aligning with the user's preferences and individuality. The goal is to provide a meaningful and personalized representation of the user's daily auditory experiences in the format they choose.

$user$
The user's input contains several parts:
- [user]: Basic information about the user, including name, age, etc. Where [rules] is the user's preference for ambient sound, which needs to be paid attention to.
- [agenda]: a list of the audio events the user has experienced today.
- [format]: a str of the format the user wants the information to be presented in.Choices include diary, time-chart, location-chart, activity-chart. Chart should be presented in a markdown table format.
- [instructions]: a str of user's specific requirements, default is summarizing the audio events the user has experienced today.

$assistant$
OK, I can do it.

$user$
{
    "user.name": "王煜焜",
    "user.age": 20,
    "user.job": "University Student",
    "user.hobby": ["Basketball"],
    "user.school": "Tsinghua University",
    "user.major": ["Computer Science and Technology", "Finance"],
    "user.rules": [
        "Pay attention to the discussion about classes",
        "Pay less attention to other people's intimate topics"
    ],
    "agenda": [
        {
            "speaker": "Unknown-01",
            "content": "诶，你网原的书面作业写了没啊？太抽象了，就，真的，太多了实在是",
            "location": "classroom",
            "time": "8:00"
        },
        {
            "speaker": "Unknown-02",
            "content": "我还没看，很多吗？别吧我本来就一堆其他作业没写呢",
            "location": "classroom",
            "time": "8:00"
        },
        {
            "speaker": "Unknown-03",
            "content": "老师，我想请问一下这次论文的要求是什么啊？就比如说，呃，选题啊，长度啊什么的，有没有什么限制啊？",
            "location": "classroom",
            "time": "8:00"
        },
        {
            "speaker": "Unknown-04",
            "content": "没什么限制，主要是要抓住一个对立面来写就行",
            "location": "classroom",
            "time": "8:00"
        }
    ]
    "format": "diary",
    "instruction": "攥写一篇日记总结这一天的声音事件"
}

$assistant$
{
    "diary":\"\"\" 
    Diary for 王煜焜 (Age: 20)
    Date: 2023-11-02
    Overview:
    Today, 王煜焜 had a busy day at Tsinghua University, with a focus on classes and academic discussions. Let's delve into the auditory experiences of the day.

    Morning (8:00 AM - 9:00 AM)
    Classroom: The day started with a discussion in the classroom. The topic was the written assignments for the Network Architecture course, and a fellow student (Unknown-01) mentioned that it was abstract and challenging. Another student (Unknown-02) was concerned about the workload.

    Unknown-01: "诶，你网原的书面作业写了没啊？太抽象了，就，真的，太多了实在是"
    Unknown-02: "我还没看，很多吗？别吧我本来就一堆其他作业没写呢"
    Classroom: During the same discussion, there was a query about the requirements for an upcoming research paper. The teacher responded that there were no strict restrictions and suggested focusing on presenting opposing views.

    Unknown-03: "老师，我想请问一下这次论文的要求是什么啊？就比如说，呃，选题啊，长度啊什么的，有没有什么限制啊？"
    Unknown-04: "没什么限制，主要是要抓住一个对立面来写就行"
    Summary:
    Today was marked by academic discussions and class-related audio events. 王煜焜's focus on academic matters aligns with their university student status. The discussion about class assignments and research papers was the highlight of the day.
    \"\"\"
}
"""
polish_prompt = """
$system$
You are an assistant for polishing rough text converted from audio recognition software. You need to correct the misidentified words, break sentences correctly, and make sentences coherent. Please infer the correct words based on pronunciation for areas that are unclear, and do not fabricate them yourself.

$user$
这样一个设备就是呃呃，本来就是与我的个个人兴趣点信息相关的，所以我觉得这是最重要的就是选择自己学术方向的额原因，然后接下来这个就是呃，想分享一下在计算机学术上的投入和收获的比较，而这个也是知道的，给我提供了一个想法，就是希望我讲一讲这个啊，先讲讲投入投入这方面的话，其主要是时间投入和心情投入的时间投入上啊，如果你跟着学长干或者是。
$assistant$
这样一个设备，就是它本来就是与我个人兴趣点息息相关的，所以我觉得这是最重要的，就是选择自己学术方向的原因。然后接下来想分享一下在计算机学术上的投入和收获的比较，这个也是支出给我提供的一个想法，就是希望我讲一下，先讲讲投入这方面的话。其实主要是时间投入和辛勤投入，那时间投入上，如果你跟着学长干，或者是
$user$
是比较厉害，自己干自己自己自己这个独立做一个项目的话，那他可能很很有可能会根据你投稿的这个弟弟要做作业的干比如说嗯，九月份截稿的话，你可能整个暑假就是很多时候都要再跟学长干活，然后再比如说啊，最近我在家就是最近我正正好也是一个比较干的时候，然后就会和赵静一起干，然后如果确实是真的想要很多收获的话，确实。
$assistant$
你比较厉害，自己干自己独立做一个项目的话，那它可能很有可能会根据你投稿的这个DDL周期性的肝，比如说。9月份截稿的话，你可能整个暑假就是很多时候都要在跟学长干活，然后再比如说最近我大家就是最近我正好也是一个比较肝的时候，然后就会和造机一起干。如果确实是真的想要很多收获的话，确实
$user$
需要投入大量的时间，不管你是自己做还是就是跟着学长学姐做，然后第二个是心情投入就是你可能啊，好不容易第一，第一次就是参与科研，然后学长带着你做了一片一篇这个一个项目，然后你投稿，然后回来一个为债，可能可能心情就会非常的不好，然后还有就是你真心想要做一个实验，然后他这个花了一个月的时间做开发，然后投入用户实验，之后回来发现数据非常不好，然后就做两个。
$assistant$
需要投入大量的时间，不管你是自己做，还是就是跟着学长学姐做。然后第二个是辛勤投入，就是你可能好不容易第一次正式参与科研，然后学长带着你做了一篇一篇这个项目，然后你投稿，然后回来一个reject，你可能心情就会非常的不好，然后还有就是你精心想要做一个实验，然后它。花了一个月的时间做开发，然后投入用户实验之后回来发现数据非常不好，然后这做了两个
$user$
每月的工作就要全部推翻重来，其实这些心情都是飞非常的跌宕起伏，他可能会在你本身可成就不如意的时候给你雪上加霜，这是主要的投入，但是其实收获也是比较多的，首先就是计算机相关农业的提升，首先，这个代码量肯定是会写一些的，根据不同的细分领域嗯写不不一样的代码，在这个领域会更加的就是有自己的见解，然后还有就是工程能力和写作能力的提升，因为在整个学术。
$assistant$
月的工作就要全部推翻重来，其实这些心情都是。非常的跌宕起伏，它可能会在你本身课程就不如意的时候给你雪上加霜。这是主要的投入。但是其实收获也是比较多的，首先就是计算机相关能力的提升，首先这个代码量肯定是会写一些的，根据不同的细分领域写不一样的代码，在这个领域会更加的有自己的见解，然后还有就是工程能力和协作能力的提升。因为在整个学术
$user$
过程当中肯定是会有很多和不管是学长学姐，还是周围同学交流的机会，然后很多东西都是要合作的，所以这些也是一个综合能力的提升，然后包括也是一直品质，那些收获就是前面提到那些投入和失败啊，就是要坦然面对，同时在整个科研过程中高效的沟通和合作很重要的，这个能力也会相应的提升，当然我觉得前面这些其实都不重要，最最重要的就是在在这个过程中能够找到自己的兴趣所在和未来可能会从事这个。
$assistant$
过程当中，肯定是会有很多和不管是学长学姐还是周围同学交流的机会，然后很多东西都是要合作的，所以这些也是一个综合能力的提升，然后包括也是意志品质的一些收获，就是前面提到的那些投入和失败，就是要坦然面对。同时在整个科研过程中，高效的沟通和合作也是非常重要的能力也会相应的提升。当然我觉得前面这些其实都不重要，最重要的就是在这个过程中能够找到自己的兴趣所在和未来可能会从事的事业。
$user$
今年五月是第一段科研，然后5月到10月是第二段，可研，然后十月到现在是第三段，然后其实虽然分了三段都是跟着同一份学长，就是同一个学长的三份工作，然后就就是他他的这个他的博士期间的这个时间周期，然后我跟随他做了三份不一样的文件，然后这个是我个人的一个时间线，可能和大多数就是桂系同学的时间线是差不多的，然后接。
$assistant$
今年5月是第一段科研，然后5月到10月是第二段科研，然后十月到现在是第三段。其实虽然分了三段，都是跟着同一位学长，就是同一个学长的三份工作，然后就是他博士期间的这个时间周期，然后我跟随他做了三份不一样的项目。这个是我个人的一个时间线，可能和大多数计系同学的时间线是差不多的，然后接下来。
"""

realtime_prompt = """
$system$
You are an intelligent sound analysis agent designed to assist users in understanding their surroundings and important audio cues, especially in meetings and group discussion scenarios.
Given the contextual information, and real-time instructions (including but not limited to audio, time, location, activity status, schedule information, etc.), your task is to generate text that is presented to the user. This text should be informative, relevant, and tailored to the user's specific requirements and current circumstances. For instance, if the user is in a noisy environment, consider providing concise and clear information. If the user's schedule indicates an important meeting in 30 minutes, prioritize any relevant audio information. Ensure that the output text is user-friendly, easy to understand, and enhances the user's interaction with the environment and information.
You will receive segmented, audio converted text continuously, each lasting approximately 2.5 minutes. You need to update your analysis results based on your previous analysis and current content every time you receive new content. Note that each analysis should focus on all the aforementioned content.

$user$
The user's input contains several parts:
- [last_output]: The analysis result you output last time. If the first audio segment of a meeting or discussion is received at this time, then this content is empty.
- [sound_new]: Newly received speech sounds in the environment, including the content of the sound.
- [instruction]: User's specific requirements, default is extracting the textaul sound information that is most important to users at the moment.

Since there may be more than one person speaking in the environment, or even multiple groups discussing multiple topics, you need to select the 1 to 3 topics that are most relevant to the user based on the above information, and output a summary and keywords of each topic in JSON format.

Note that you can adjust the previous analysis based on the new audio content.

$assistant$
OK, I can do it.

$user$
{
    "last_output": []
    "sound_new": {
        这样一个设备，就是它本来就是与我个人兴趣点息息相关的，所以我觉得这是最重要的，就是选择自己学术方向的原因。然后接下来想分享一下在计算机学术上的投入和收获的比较，这个也是支出给我提供的一个想法，就是希望我讲一下，先讲讲投入这方面的话。其实主要是时间投入和辛勤投入，那时间投入上，如果你跟着学长干，或者是你比较厉害，自己干自己独立做一个项目的话，那它可能很有可能会根据你投稿的这个DDL周期性的肝，比如说。9月份截稿的话，你可能整个暑假就是很多时候都要在跟学长干活，然后再比如说最近我大家就是最近我正好也是一个比较肝的时候，然后就会和造机一起干。如果确实是真的想要很多收获的话，确实需要投入大量的时间，不管你是自己做，还是就是跟着学长学姐做。然后第二个是辛勤投入，就是你可能好不容易第一次正式参与科研，然后学长带着你做了一篇一篇这个项目，然后你投稿，然后回来一个reject，你可能心情就会非常的不好，然后还有就是你精心想要做一个实验，然后它。花了一个月的时间做开发，然后投入用户实验之后回来发现数据非常不好，然后这做了两个月的工作就要全部推翻重来，其实这些心情都是。非常的跌宕起伏，它可能会在你本身课程就不如意的时候给你雪上加霜。这是主要的投入。但是其实收获也是比较多的，首先就是计算机相关能力的提升，首先这个代码量肯定是会写一些的，根据不同的细分领域写不一样的代码，在这个领域会更加的有自己的见解，然后还有就是工程能力和协作能力的提升。因为在整个学术过程当中，肯定是会有很多和不管是学长学姐还是周围同学交流的机会，然后很多东西都是要合作的，所以这些也是一个综合能力的提升，然后包括也是意志品质的一些收获，就是前面提到的那些投入和失败，就是要坦然面对。
    },
    "instruction": "此时为单人发言"
}

$assistant$
{
    "topic": [
    {
        "summary": "发言者主要围绕个人对于计算机学科的热情和在学术方向上的选择进行了阐述。强调选择学术方向与个人兴趣的紧密相关性，认为这是最重要的因素。",
        "keywords": ["计算机学术", "个人选择"]
    },
    {
        "summary": "分享了在计算机学术领域的投入与收获的比较。在投入方面，主要讨论了时间和努力的投入，特别是在进行科研项目时的时间投入和遇到挑战时的心理波动。提到了遇到拒稿和实验失败时的心情低落，以及需要重新开始的挑战。在收获方面，提到了计算机相关能力的提升，包括编码能力、工程和协作能力。强调了在科研过程中与同行的交流和合作的重要性，并指出这些经历对综合能力和意志品质的提升有重要影响。。",
        "keywords": ["投入", "收获", "时间投入", "心情投入", "能力提升", "意志品质"]
    }
    ],
}


$user$
{
    "last_output":[
    {
        "summary": "发言者主要围绕个人对于计算机学科的热情和在学术方向上的选择进行了阐述。强调选择学术方向与个人兴趣的紧密相关性，认为这是最重要的因素。",
        "keywords": ["计算机学术", "个人选择"]
    },
    {
        "summary": "分享了在计算机学术领域的投入与收获的比较。在投入方面，主要讨论了时间和努力的投入，特别是在进行科研项目时的时间投入和遇到挑战时的心理波动。提到了遇到拒稿和实验失败时的心情低落，以及需要重新开始的挑战。在收获方面，提到了计算机相关能力的提升，包括编码能力、工程和协作能力。强调了在科研过程中与同行的交流和合作的重要性，并指出这些经历对综合能力和意志品质的提升有重要影响。",
        "keywords": ["投入", "收获", "时间投入", "心情投入", "能力提升", "意志品质"]
    }
    ]
    "sound_new": {
        同时在整个科研过程中，高效的沟通和合作也是非常重要的能力也会相应的提升。当然我觉得前面这些其实都不重要，最重要的就是在这个过程中能够找到自己的兴趣所在和未来可能会从事的事业。然后接下来就是学业和科研之间的权衡，我觉得大一大二可能大家都以学习为重，然后到大三，大家可能经管代管的同学也会有很多实习，然后想要走计算机方向的同学，确实也需要在科研上投入一些时间，不管未来想出国还是想保研。大三确实可能有一些科研经历是比较好的，但主要还是根据，如果是跟着学长学姐或者做可能还是要看他们这个安排，然后就其实如果不是自己做的话，只需要跟着学长学姐的脚步，按照他们的说，他们给你分的任。我一步做在能力范围之内尽量多参与就可以，如果是自己做项目的话，我也不太了解，如果大家就是咱们有自己开始做项目的同学，其实这个分享就是当我没说。但确实在学业和科研之间，如果是科研，真的影响到了课程，比如说你就是为了去搞科研，然后作业写不完了，这还是不太合适，还是得以课程为主。然后与最后是与学长学姐和老师沟通，我觉得这个很重要的就是大胆表达自己的想法，就是有想法，你就说错了也没有关系，大家也不会去怪一个本科生说错了什么什么东西大家更。不管是学长学姐还是老师，更希望听到的都是你有一些创新的想法，它可能与你专业知识扎不扎实，没有什么关系，但是重要的是很多时候需要脑报，然后大家共同思考解决问题的时候，你要是有一些自己的创新的想法，那可能会非常的亮眼。总之就是不要怕，大多数老师和学长学姐人其实都挺好的，直接跟他们沟通就可以了。一些其他的建议。找到自己喜欢的方向，不然会很痛苦。然后如果要跟着学长学写作的话，可能需要一些慎重的选择，因为不同的博士生或者硕士生学长，他们的风格不太一样，如果找不到一个比较合适的相处方式的话，可能这个。也会没有什么收获，要么没有活儿干，要么可能只干了活儿，啥也没学到。。
    },
    "instruction": "此时为单人发言"
}


$assistant$
{
    "topic": [
    {
        "summary": "分享了在计算机学术领域的投入与收获的比较。在投入方面，主要讨论了时间和努力的投入，特别是在进行科研项目时的时间投入和遇到挑战时的心理波动。提到了遇到拒稿和实验失败时的心情低落，以及需要重新开始的挑战。在收获方面，提到了计算机相关能力的提升，包括编码能力、工程和协作能力。强调了在科研过程中与同行的交流和合作的重要性，并指出这些经历对综合能力和意志品质的提升有重要影响。最后，强调了在这个过程中发现自己的兴趣和未来职业道路的重要性，认为这比前面提到的所有成就都要重要。",
        "keywords": ["投入", "收获", "时间投入", "心情投入", "能力提升", "意志品质"， "找到兴趣", "未来事业"]
    },
    {
        "summary": "发言者继续讨论了学业和科研之间的权衡，认为大一大二阶段学习为主，大三阶段可以开始投入科研，但仍需以课程为主。强调了在科研过程中跟随学长学姐的步伐，但也提醒了如果科研影响到了课程，如作业无法完成，还是应以课程为主。",
        "keywords": ["学业", "科研", "权衡", "学长学姐", "课程为主"]
    },
    {
        "summary": "发言者强调了与学长学姐和老师沟通的重要性，鼓励大胆表达自己的想法，即使有错误也没有关系。认为老师和学长学姐更希望听到的是有创新想法的学生，而不仅仅是专业知识扎实的学生。同时，提醒了在选择跟随学长学姐做科研时需要慎重，因为不同的学长学姐风格不同，如果找不到合适的相处方式，可能会影响科研的收获。",
        "keywords": ["沟通", "表达想法", "创新", "选择学长学姐"]
    },
    {
        "summary": "发言者最后给出了一些其他的建议，包括找到自己喜欢的方向，多提问，多学习，有自己的想法，强调了做学术的创新和钻研精神的重要性。",
        "keywords": ["建议", "找到方向", "提问", "学习", "创新", "钻研精神"]
    }
    ],
}

$user$
{
    "last_output":[
    {
        "summary": "分享了在计算机学术领域的投入与收获的比较。在投入方面，主要讨论了时间和努力的投入，特别是在进行科研项目时的时间投入和遇到挑战时的心理波动。提到了遇到拒稿和实验失败时的心情低落，以及需要重新开始的挑战。在收获方面，提到了计算机相关能力的提升，包括编码能力、工程和协作能力。强调了在科研过程中与同行的交流和合作的重要性，并指出这些经历对综合能力和意志品质的提升有重要影响。最后，强调了在这个过程中发现自己的兴趣和未来职业道路的重要性，认为这比前面提到的所有成就都要重要。",
        "keywords": ["投入", "收获", "时间投入", "心情投入", "能力提升", "意志品质"， "找到兴趣", "未来事业"]
    },
    {
        "summary": "发言者继续讨论了学业和科研之间的权衡，认为大一大二阶段学习为主，大三阶段可以开始投入科研，但仍需以课程为主。强调了在科研过程中跟随学长学姐的步伐，但也提醒了如果科研影响到了课程，如作业无法完成，还是应以课程为主。",
        "keywords": ["学业", "科研", "权衡", "学长学姐", "课程为主"]
    },
    {
        "summary": "发言者强调了与学长学姐和老师沟通的重要性，鼓励大胆表达自己的想法，即使有错误也没有关系。认为老师和学长学姐更希望听到的是有创新想法的学生，而不仅仅是专业知识扎实的学生。同时，提醒了在选择跟随学长学姐做科研时需要慎重，因为不同的学长学姐风格不同，如果找不到合适的相处方式，可能会影响科研的收获。",
        "keywords": ["沟通", "表达想法", "创新", "选择学长学姐"]
    },
    {
        "summary": "发言者最后给出了一些其他的建议，包括找到自己喜欢的方向。",
        "keywords": ["建议", "找到方向"]
    }
    ]
    "sound_new": {
        一些其他的建议。找到自己喜欢的方向，不然会很痛苦。然后如果要跟着学长学写作的话，可能需要一些慎重的选择，因为不同的博士生或者硕士生学长，他们的风格不太一样，如果找不到一个比较合适的相处方式的话，可能这个。也会没有什么收获，要么没有活儿干，要么可能只干了活儿，啥也没学到。然后多提问，多学习，最后就是要有自己的想法。做学术的话，创新和钻研的精神还是比较重要的。非常感谢王玉坤同学精彩的分享，许斌老师您那边儿时间可以吗？您需要现在跟大家聊聊一聊吗？如果您不需要我们还是先请王金一学姐。不，那你先请学姐讲吧！老师好。那我们先请王欣学姐稍微讲一讲，再简单讲一讲经管类博士的一些认识和经验吧！好好。那我就简单讲一下，我刚才也是刚下课，所以也没有像前面两位同学这样做那么详细的PP t我觉得刚才两位同学其实都说的非常好，我觉得诗颖对行业有非常深的认知。从他的汇报不是他的展，他的分享中我也学到很多，然后玉坤的话我觉得我之前也在想到底什么让我们选择一个。未来发展的道路，就肯定是首先是要你喜欢，然后第二个是你要有能力做这件事儿，然后第三个是你做的这件事儿，还要对这个社会有所贡献。我觉得玉坤刚才说他为什么要选这个方向的时候，他其实把每个点都表达的非常。什么了，对，然后我这边因为尽管这边的方向还挺。挺多的，就大家知道有经济金融，然后他们下面的细分我就不太了解了，肯定每个领域都有各自细分的更细分的领域，然后大的方向就经济金融，然后管理工程。管理科学与工程领导力与组织管理，市场营销，还有创新创业与战略，就这几个系，那每个系其实都不太一样，我就自己的感受。
    },
    "instruction": "此时有一些对话和单人发言"
}

$assistant$
{
    "topic": [
    {
        "summary": "发言者继续给出了一些建议，强调了找到自己喜欢的方向的重要性，并提醒了在选择跟随学长学姐做科研时需要慎重，因为不同的学长学姐风格不同，如果找不到合适的相处方式，可能会影响科研的收获。同时，鼓励了多提问，多学习，并强调了在学术研究中创新和钻研精神的重要性。",
        "keywords": ["建议", "找到方向", "选择学长学姐", "提问", "学习", "创新", "钻研精神"]
    },
    {
        "summary": "会议进行了一次交接，王玉坤同学的发言结束，许斌老师被询问是否需要发言，但老师选择让王金一学姐先进行发言。",
        "keywords": ["会议交接", "王玉坤", "许斌老师", "王金一学姐"]
    },
    {
        "summary": "王金一学姐开始发言，简要地分享了对经管类博士的认识和经验。她认同之前发言者的观点，并补充说选择未来发展道路时，需要考虑个人喜好、能力以及对社会的贡献。她还提到了经济金融、管理工程、管理科学与工程、领导力与组织管理、市场营销、创新创业与战略等不同的研究方向，并分享了自己的感受。",
        "keywords": ["王金一学姐", "经管类博士", "个人喜好", "能力", "社会贡献", "研究方向"]
    }
    ],
}
"""