# 教材のURL情報
tablet_urls = {
    "challenge_touch": "https://jinzaikachi.com/challenge-campaign/",
    "smile_zemi": "https://jinzaikachi.com/smilezemi-campaign/",
    "z_kai_tablet": "https://jinzaikachi.com/z-tablet/",
    "risu_kids": "https://jinzaikachi.com/risu-math/",
    "study_suppli": "https://jinzaikachi.com/study-supple/",
    "toshin_online": "https://jinzaikachi.com/toushin-online-syougakubu/",
    "dekitasu": "https://jinzaikachi.com/dekitasu/",
    "poppy": "https://jinzaikachi.com/popi-campaign/",
    "substa": "https://jinzaikachi.com/sabusuta/",
    "tenjin": "https://jinzaikachi.com/tenjin/",
    "marugland": "https://jinzaikachi.com/marug-campaign/",
    "surara": "https://jinzaikachi.com/surara/",
    "logic_labo": "https://jinzaikachi.com/rogiqlabo/",
    "wonder_box": "https://jinzaikachi.com/wonderbox/",
    "groovy_lab": "https://jinzaikachi.com/groovy/"
}

# タブレット教材データ
tablet_data = [
    {
        "id": "challenge_touch",
        "name": "チャレンジタッチ",
        "monthly_fee": 3250,
        "initial_fee": 0,
        "grade_range": ["kindergarten", "lower_elementary", "upper_elementary"],
        "subjects": ["japanese", "math", "english", "science", "social", "programming"],
        "features": ["learning_management", "subject_variety", "online_support", "exercise_quantity"],
        "strengths": [
            "豊富な動画と音声による解説",
            "初期費用0円・専用タブレット付き",
            "紙教材との併用で効果的",
            "オンラインでの質問・相談サービスあり"
        ],
        "weaknesses": [
            "学力向上効果は平均的",
            "基礎固めが中心で応用力を伸ばすには不向き",
            "学習内容は決められたカリキュラム通り"
        ],
        "description": "ベネッセの「進研ゼミ」のタブレット版で、基礎力養成を目的とした質の高い学習コンテンツと、専用タブレットが提供されます。紙の教材とのハイブリッド学習が特徴です。"
    },
    {
        "id": "smile_zemi",
        "name": "スマイルゼミ",
        "monthly_fee": 3278,
        "initial_fee": 11000,
        "grade_range": ["kindergarten", "lower_elementary", "upper_elementary", "junior_high"],
        "subjects": ["japanese", "math", "english", "science", "social", "programming"],
        "features": ["learning_management", "subject_variety", "exercise_quantity", "ai_learning"],
        "strengths": [
            "全科目対応でバランス良く学べる",
            "AIが得意・苦手を分析して出題",
            "丁寧な解説とステップアップ学習",
            "保護者向け管理アプリで学習管理しやすい"
        ],
        "weaknesses": [
            "専用タブレットの初期費用が必要",
            "学習内容は基礎力養成が中心",
            "記述問題の学習は紙教材に劣る"
        ],
        "description": "スマイルゼミは、幼児から中学生まで対応した総合的なタブレット教材です。専用タブレットを使い、AIが子どもの理解度に合わせて問題を出題し、効率的な学習をサポートします。"
    },
    {
        "id": "z_kai_tablet",
        "name": "Z会タブレットコース",
        "monthly_fee": 3570,
        "initial_fee": 0,
        "grade_range": ["lower_elementary", "upper_elementary", "junior_high"],
        "subjects": ["japanese", "math", "english", "science", "social", "programming", "thinking"],
        "features": ["subject_variety", "exercise_quantity", "learning_management", "thinking_skills"],
        "strengths": [
            "思考力・記述力を重視したカリキュラム",
            "難関中学受験対策に効果的",
            "先取り学習が可能",
            "質の高い教材で本質的な理解を促進"
        ],
        "weaknesses": [
            "教材ボリュームが多くて大変",
            "難易度が高く挫折リスクがある",
            "価格が高め"
        ],
        "description": "Z会タブレットコースは、思考力・表現力を重視した難関校受験にも対応する高品質な学習教材です。タブレットでの学習と紙ベースの添削で書く力も鍛えられます。"
    },
    {
        "id": "risu_kids",
        "name": "RISU算数",
        "monthly_fee": 2980,
        "initial_fee": 0,
        "grade_range": ["kindergarten", "lower_elementary", "upper_elementary", "junior_high"],
        "subjects": ["math"],
        "features": ["ai_learning", "exercise_quantity", "interactive"],
        "strengths": [
            "AIによる進度調整と個別対応",
            "つまずき箇所を徹底的に克服",
            "自分のペースで先取り学習可能",
            "算数の基礎から応用まで体系的に学習"
        ],
        "weaknesses": [
            "算数のみの対応で他教科は別途必要",
            "子ども向けキャラクターなど親しみ要素が少ない",
            "保護者サポートが他より少なめ"
        ],
        "description": "RISU算数は、AIが子どもの理解度を精密に分析し、一人ひとりに最適な問題を提供する算数特化型のタブレット教材です。算数が得意な子も苦手な子も個別のペースで効率的に学習できます。"
    },
    {
        "id": "study_suppli",
        "name": "スタディサプリ小学講座",
        "monthly_fee": 2178,
        "initial_fee": 0,
        "grade_range": ["lower_elementary", "upper_elementary", "junior_high"],
        "subjects": ["japanese", "math", "english", "science", "social"],
        "features": ["video_lessons", "exercise_quantity", "learning_management", "cost_effective"],
        "strengths": [
            "リーズナブルな料金設定",
            "実績のある講師陣による動画授業",
            "自分のペースで繰り返し視聴可能",
            "定期テスト対策も充実"
        ],
        "weaknesses": [
            "AIによる個別最適化機能は弱い",
            "学習管理は保護者主導になりがち",
            "双方向性の学習体験は限られる"
        ],
        "description": "スタディサプリ小学講座は、有名講師による質の高い授業動画と演習問題を低価格で利用できるオンライン学習サービスです。手持ちのタブレットで好きな時に学習できます。"
    },
    {
        "id": "toshin_online",
        "name": "東進オンライン学校（小学部）",
        "monthly_fee": 5500,
        "initial_fee": 0,
        "grade_range": ["upper_elementary", "junior_high"],
        "subjects": ["japanese", "math", "english", "science", "social"],
        "features": ["video_lessons", "exercise_quantity", "test_preparation", "advanced_learning"],
        "strengths": [
            "難関中学受験に強い指導カリキュラム",
            "一流講師陣による授業で難関校合格実績あり",
            "志望校に合わせた学習プラン",
            "映像授業と演習のバランスが良い"
        ],
        "weaknesses": [
            "月額費用が高め",
            "難易度が高く基礎固めには不向き",
            "小3以下には対応していない"
        ],
        "description": "東進オンライン学校は難関中学受験を目指す小学生のための本格的なオンライン学習塾です。一流講師の授業と体系的な演習で、効率的に受験対策ができます。"
    },
    {
        "id": "dekitasu",
        "name": "デキタス",
        "monthly_fee": 2178,
        "initial_fee": 0,
        "grade_range": ["lower_elementary", "upper_elementary", "junior_high"],
        "subjects": ["japanese", "math", "english", "science", "social"],
        "features": ["ai_learning", "exercise_quantity", "learning_management", "interactive"],
        "strengths": [
            "AIによる個別学習プラン作成",
            "子どもが楽しく続けられるゲーム要素",
            "リーズナブルな料金設定",
            "基礎から応用まで幅広く対応"
        ],
        "weaknesses": [
            "思考力や記述力を鍛える問題は少なめ",
            "キャラクター要素が多く集中力が散漫になる場合も",
            "専用タブレットの操作性に慣れが必要"
        ],
        "description": "デキタスは、ゲーム要素を取り入れた楽しい学習体験と、AIによる個別最適化学習を組み合わせたタブレット教材です。子どもが自ら学習する習慣づくりに効果的です。"
    },
    {
        "id": "poppy",
        "name": "小学ポピー",
        "monthly_fee": 1400,
        "initial_fee": 0,
        "grade_range": ["kindergarten", "lower_elementary", "upper_elementary"],
        "subjects": ["japanese", "math", "english", "science", "social"],
        "features": ["exercise_quantity", "cost_effective", "paper_based"],
        "strengths": [
            "非常にリーズナブルな料金設定",
            "学校の教科書に準拠した内容",
            "テスト対策にも役立つ基礎力養成",
            "タブレットと紙教材のハイブリッド学習"
        ],
        "weaknesses": [
            "応用力や思考力を鍛える内容は少なめ",
            "AIによる個別最適化機能はない",
            "保護者のサポートが必要な場面が多い"
        ],
        "description": "小学ポピーは60年以上の実績を持つ通信教育で、基本はプリント学習ですが、タブレット学習も組み合わせることができます。学校の授業に沿った内容で、基礎学力の定着に最適です。"
    },
    {
        "id": "substa",
        "name": "サブスタ",
        "monthly_fee": 980,
        "initial_fee": 0,
        "grade_range": ["lower_elementary", "upper_elementary", "junior_high"],
        "subjects": ["japanese", "math", "english", "science", "social"],
        "features": ["video_lessons", "cost_effective", "test_preparation"],
        "strengths": [
            "業界最安クラスの月額料金",
            "わかりやすい授業動画",
            "定期テスト対策に効果的",
            "復習や補習として最適"
        ],
        "weaknesses": [
            "演習問題の量がやや少なめ",
            "個別最適化機能はない",
            "自主学習の習慣が必要"
        ],
        "description": "サブスタは月額980円から利用できる低価格のオンライン学習サービスです。学校の授業でわからなかった部分を復習したり、定期テスト対策として利用するのに最適です。"
    },
    {
        "id": "tenjin",
        "name": "天神",
        "monthly_fee": 2980,
        "initial_fee": 0,
        "grade_range": ["lower_elementary", "upper_elementary", "junior_high"],
        "subjects": ["japanese", "math", "english", "science", "social"],
        "features": ["ai_learning", "exercise_quantity", "learning_management"],
        "strengths": [
            "苦手科目の克服に特化",
            "学校の授業の遅れを取り戻せる",
            "基礎から丁寧に学び直せる",
            "子どものペースに合わせた学習プラン"
        ],
        "weaknesses": [
            "応用力や発展的な内容は少なめ",
            "受験対策としては物足りない場合も",
            "AIの精度はトップクラスとまでは言えない"
        ],
        "description": "天神は学校の授業についていけない子どもや、苦手科目の克服を目的とした小中学生向けタブレット教材です。基礎からのやり直しで、着実に学力を向上させます。"
    },
    {
        "id": "marugland",
        "name": "まるぐランド for HOME",
        "monthly_fee": 1078,
        "initial_fee": 0,
        "grade_range": ["lower_elementary", "upper_elementary"],
        "subjects": ["japanese", "math"],
        "features": ["ai_learning", "exercise_quantity", "special_needs_support"],
        "strengths": [
            "特別支援教育の知見を活かした教材",
            "学習につまずきがある子にも効果的",
            "基礎から丁寧に学べる",
            "リーズナブルな料金設定"
        ],
        "weaknesses": [
            "国語と算数のみの対応",
            "教科書対応ではなく基礎スキル重視",
            "高学年向けの発展的内容は少ない"
        ],
        "description": "まるぐランド for HOMEは、学校でも導入されている教材の家庭版で、特別支援教育の知見を活かした、つまずきのある子どもにも優しい学習教材です。"
    },
    {
        "id": "surara",
        "name": "すらら",
        "monthly_fee": 4378,
        "initial_fee": 11000,
        "grade_range": ["kindergarten", "lower_elementary", "upper_elementary", "junior_high"],
        "subjects": ["japanese", "math", "english", "science", "social"],
        "features": ["ai_learning", "exercise_quantity", "learning_management", "special_needs_support"],
        "strengths": [
            "わかりやすいアニメーション授業",
            "つまずきに合わせた個別カリキュラム",
            "特別支援教育の知見を活用",
            "学習のつまずき診断が詳細"
        ],
        "weaknesses": [
            "月額費用と初期費用が高め",
            "アニメーション中心で実写講師の授業はない",
            "受験対策としては物足りない"
        ],
        "description": "すららは学校でも多く導入されている、つまずき診断と個別最適化学習が特徴のタブレット教材です。アニメーションによるわかりやすい授業で、基礎力を着実に身につけられます。"
    },
    {
        "id": "logic_labo",
        "name": "ロジックラボ",
        "monthly_fee": 1980,
        "initial_fee": 0,
        "grade_range": ["lower_elementary", "upper_elementary", "junior_high"],
        "subjects": ["math", "programming", "thinking"],
        "features": ["thinking_skills", "exercise_quantity", "programming_education"],
        "strengths": [
            "論理的思考力や数理能力を鍛える",
            "楽しみながら思考力が身につく",
            "AI、プログラミング的思考の基礎を培う",
            "リーズナブルな料金設定"
        ],
        "weaknesses": [
            "教科学習ではなく思考力トレーニング中心",
            "学校の成績向上に直結しにくい",
            "保護者のサポートが必要な場合も"
        ],
        "description": "ロジックラボは数理能力と論理的思考力を楽しく鍛える教材です。将来のAI時代に必要な思考力や問題解決能力の基礎を育みます。"
    },
    {
        "id": "wonder_box",
        "name": "ワンダーボックス",
        "monthly_fee": 2980,
        "initial_fee": 0,
        "grade_range": ["kindergarten", "lower_elementary", "upper_elementary"],
        "subjects": ["thinking", "programming", "science", "art"],
        "features": ["thinking_skills", "creativity", "stem_education", "project_based"],
        "strengths": [
            "創造力と思考力を育む多彩なプロジェクト",
            "実験キットとタブレット学習の組み合わせ",
            "STEAM教育で未来の力を養う",
            "子どもの好奇心を刺激する内容"
        ],
        "weaknesses": [
            "教科学習ではなく総合的な能力開発",
            "学校の成績向上に直結しにくい",
            "教材の保管スペースが必要"
        ],
        "description": "ワンダーボックスは毎月届く実験キットとタブレット学習を組み合わせた、創造力と思考力を育むSTEAM教育教材です。好奇心を刺激し、考える力を養います。"
    },
    {
        "id": "groovy_lab",
        "name": "グルービーラボ イン ア ボックス",
        "monthly_fee": 2980,
        "initial_fee": 0,
        "grade_range": ["lower_elementary", "upper_elementary"],
        "subjects": ["science", "engineering", "art", "math"],
        "features": ["thinking_skills", "creativity", "stem_education", "project_based"],
        "strengths": [
            "本格的な科学実験が家庭でできる",
            "タブレットと実物教材の組み合わせ",
            "実験を通じて科学的思考力を養う",
            "英語と日本語のバイリンガル対応"
        ],
        "weaknesses": [
            "教科学習ではなく体験型学習が中心",
            "学校の成績向上に直結しにくい",
            "実験に保護者のサポートが必要"
        ],
        "description": "グルービーラボは米国発の科学教材で、毎月テーマの異なる実験キットとタブレット解説で、楽しく科学を学べます。バイリンガル対応で英語学習にも役立ちます。"
    }
]

# 機能評価データ（各教材の機能ごとの評価点）
feature_ratings = {
    "challenge_touch": {
        "learning_management": 8,
        "online_support": 9,
        "subject_variety": 8,
        "exercise_quantity": 7,
        "interactive": 7,
        "ai_learning": 6,
        "thinking_skills": 5,
        "cost_effective": 7,
        "video_lessons": 8,
        "test_preparation": 7,
        "advanced_learning": 5,
        "special_needs_support": 6,
        "creativity": 5,
        "stem_education": 4,
        "project_based": 3
    },
    "smile_zemi": {
        "learning_management": 9,
        "online_support": 7,
        "subject_variety": 9,
        "exercise_quantity": 8,
        "interactive": 7,
        "ai_learning": 8,
        "thinking_skills": 6,
        "cost_effective": 6,
        "video_lessons": 7,
        "test_preparation": 7,
        "advanced_learning": 6,
        "special_needs_support": 5,
        "creativity": 6,
        "stem_education": 6,
        "project_based": 4
    },
    "z_kai_tablet": {
        "learning_management": 7,
        "online_support": 8,
        "subject_variety": 9,
        "exercise_quantity": 9,
        "interactive": 6,
        "ai_learning": 5,
        "thinking_skills": 10,
        "cost_effective": 5,
        "video_lessons": 6,
        "test_preparation": 9,
        "advanced_learning": 10,
        "special_needs_support": 4,
        "creativity": 8,
        "stem_education": 7,
        "project_based": 7
    },
    "risu_kids": {
        "learning_management": 7,
        "online_support": 6,
        "subject_variety": 3,
        "exercise_quantity": 9,
        "interactive": 8,
        "ai_learning": 10,
        "thinking_skills": 8,
        "cost_effective": 7,
        "video_lessons": 6,
        "test_preparation": 7,
        "advanced_learning": 8,
        "special_needs_support": 7,
        "creativity": 5,
        "stem_education": 7,
        "project_based": 3
    },
    "study_suppli": {
        "learning_management": 6,
        "online_support": 6,
        "subject_variety": 7,
        "exercise_quantity": 8,
        "interactive": 5,
        "ai_learning": 4,
        "thinking_skills": 6,
        "cost_effective": 9,
        "video_lessons": 10,
        "test_preparation": 8,
        "advanced_learning": 6,
        "special_needs_support": 5,
        "creativity": 4,
        "stem_education": 4,
        "project_based": 3
    },
    "toshin_online": {
        "learning_management": 7,
        "online_support": 7,
        "subject_variety": 8,
        "exercise_quantity": 9,
        "interactive": 6,
        "ai_learning": 5,
        "thinking_skills": 9,
        "cost_effective": 4,
        "video_lessons": 10,
        "test_preparation": 10,
        "advanced_learning": 10,
        "special_needs_support": 3,
        "creativity": 6,
        "stem_education": 5,
        "project_based": 4
    },
    "dekitasu": {
        "learning_management": 8,
        "online_support": 7,
        "subject_variety": 7,
        "exercise_quantity": 8,
        "interactive": 9,
        "ai_learning": 8,
        "thinking_skills": 6,
        "cost_effective": 8,
        "video_lessons": 7,
        "test_preparation": 7,
        "advanced_learning": 6,
        "special_needs_support": 7,
        "creativity": 7,
        "stem_education": 5,
        "project_based": 5
    },
    "poppy": {
        "learning_management": 5,
        "online_support": 5,
        "subject_variety": 7,
        "exercise_quantity": 7,
        "interactive": 5,
        "ai_learning": 3,
        "thinking_skills": 5,
        "cost_effective": 10,
        "video_lessons": 4,
        "test_preparation": 7,
        "advanced_learning": 4,
        "special_needs_support": 6,
        "creativity": 4,
        "stem_education": 3,
        "project_based": 3
    },
    "substa": {
        "learning_management": 4,
        "online_support": 4,
        "subject_variety": 7,
        "exercise_quantity": 6,
        "interactive": 4,
        "ai_learning": 2,
        "thinking_skills": 5,
        "cost_effective": 10,
        "video_lessons": 9,
        "test_preparation": 8,
        "advanced_learning": 4,
        "special_needs_support": 5,
        "creativity": 3,
        "stem_education": 3,
        "project_based": 2
    },
    "tenjin": {
        "learning_management": 7,
        "online_support": 6,
        "subject_variety": 7,
        "exercise_quantity": 8,
        "interactive": 7,
        "ai_learning": 8,
        "thinking_skills": 5,
        "cost_effective": 7,
        "video_lessons": 7,
        "test_preparation": 6,
        "advanced_learning": 4,
        "special_needs_support": 8,
        "creativity": 4,
        "stem_education": 3,
        "project_based": 3
    },
    "marugland": {
        "learning_management": 6,
        "online_support": 5,
        "subject_variety": 3,
        "exercise_quantity": 7,
        "interactive": 7,
        "ai_learning": 7,
        "thinking_skills": 4,
        "cost_effective": 9,
        "video_lessons": 5,
        "test_preparation": 4,
        "advanced_learning": 3,
        "special_needs_support": 10,
        "creativity": 5,
        "stem_education": 3,
        "project_based": 3
    },
    "surara": {
        "learning_management": 8,
        "online_support": 7,
        "subject_variety": 7,
        "exercise_quantity": 8,
        "interactive": 8,
        "ai_learning": 9,
        "thinking_skills": 6,
        "cost_effective": 5,
        "video_lessons": 8,
        "test_preparation": 7,
        "advanced_learning": 5,
        "special_needs_support": 9,
        "creativity": 5,
        "stem_education": 4,
        "project_based": 3
    },
    "logic_labo": {
        "learning_management": 6,
        "online_support": 5,
        "subject_variety": 3,
        "exercise_quantity": 7,
        "interactive": 8,
        "ai_learning": 7,
        "thinking_skills": 10,
        "cost_effective": 8,
        "video_lessons": 6,
        "test_preparation": 3,
        "advanced_learning": 7,
        "special_needs_support": 5,
        "creativity": 9,
        "stem_education": 8,
        "project_based": 6
    },
    "wonder_box": {
        "learning_management": 5,
        "online_support": 6,
        "subject_variety": 5,
        "exercise_quantity": 6,
        "interactive": 9,
        "ai_learning": 4,
        "thinking_skills": 9,
        "cost_effective": 7,
        "video_lessons": 7,
        "test_preparation": 2,
        "advanced_learning": 6,
        "special_needs_support": 6,
        "creativity": 10,
        "stem_education": 10,
        "project_based": 10
    },
    "groovy_lab": {
        "learning_management": 5,
        "online_support": 6,
        "subject_variety": 4,
        "exercise_quantity": 5,
        "interactive": 8,
        "ai_learning": 3,
        "thinking_skills": 8,
        "cost_effective": 7,
        "video_lessons": 6,
        "test_preparation": 2,
        "advanced_learning": 6,
        "special_needs_support": 5,
        "creativity": 9,
        "stem_education": 10,
        "project_based": 10
    }
}
