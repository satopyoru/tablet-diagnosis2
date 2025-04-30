# タブレット教材データ
tablet_data = [
    {
        "id": "smile_zemi",
        "name": "スマイルゼミ",
        "monthly_fee": 3278,
        "initial_fee": 11000,
        "grade_range": ["kindergarten", "lower_elementary", "upper_elementary", "junior_high"],
        "subjects": ["japanese", "math", "english", "science", "social", "programming"],
        "features": ["learning_management", "subject_variety", "exercise_quantity", "ai_learning"],
        "strengths": [
            "全科目に対応しており学習範囲が広い",
            "AIによる個別最適化学習",
            "豊富な問題数と動画解説",
            "保護者向け管理アプリが充実"
        ],
        "weaknesses": [
            "月額費用が比較的高め",
            "専用タブレットが必要で初期費用がかかる",
            "自由度が低く応用力がつきにくい"
        ],
        "description": "スマイルゼミは、幼児から中学生まで対応した総合的なタブレット教材です。AIが子どもの理解度に合わせて問題を出題し、効率的な学習をサポートします。"
    },
    {
        "id": "challenge_touch",
        "name": "チャレンジタッチ",
        "monthly_fee": 2980,
        "initial_fee": 0,
        "grade_range": ["kindergarten", "lower_elementary", "upper_elementary"],
        "subjects": ["japanese", "math", "english", "science", "social"],
        "features": ["learning_management", "subject_variety", "online_support"],
        "strengths": [
            "進研ゼミのノウハウを活かした質の高い教材",
            "初期費用が不要でコストパフォーマンスが良い",
            "オンラインでの質問・相談サービスあり",
            "紙教材との併用で効果的"
        ],
        "weaknesses": [
            "プログラミング教育が弱い",
            "中学生向けコースがない",
            "問題数がやや少なめ"
        ],
        "description": "ベネッセの「進研ゼミ」のタブレット版で、質の高い学習コンテンツと、紙の教材とのハイブリッド学習が特徴です。"
    },
    {
        "id": "risu_kids",
        "name": "RISUきっず",
        "monthly_fee": 2980,
        "initial_fee": 0,
        "grade_range": ["kindergarten", "lower_elementary", "upper_elementary"],
        "subjects": ["math"],
        "features": ["ai_learning", "exercise_quantity", "interactive"],
        "strengths": [
            "AI技術による個別最適化が高精度",
            "算数・数学に特化した深い学び",
            "子どもの「わからない」を見逃さない仕組み",
            "自分のペースで先取り学習が可能"
        ],
        "weaknesses": [
            "算数・数学のみの対応",
            "総合的な学習には他の教材も必要",
            "タブレットを別途用意する必要がある"
        ],
        "description": "RISU（リス）きっずは算数・数学に特化したタブレット教材で、AIが子どもの理解度を分析し、一人ひとりに最適な問題を提供します。"
    },
    {
        "id": "qubena",
        "name": "Qubena（キュビナ）",
        "monthly_fee": 2178,
        "initial_fee": 0,
        "grade_range": ["lower_elementary", "upper_elementary", "junior_high"],
        "subjects": ["math", "english"],
        "features": ["ai_learning", "interactive", "exercise_quantity"],
        "strengths": [
            "AI技術による徹底した個別最適化",
            "思考過程までAIが分析し弱点を特定",
            "学校の授業進度に合わせやすい",
            "コストパフォーマンスが高い"
        ],
        "weaknesses": [
            "算数・数学と英語のみの対応",
            "保護者向け機能がやや少なめ",
            "タブレットを別途用意する必要がある"
        ],
        "description": "Qubenaは数学と英語に特化したAI学習教材で、子どもの解答プロセスを分析して、つまずきポイントに合わせた問題を出題します。"
    },
    {
        "id": "z_kai_tablet",
        "name": "Z会タブレットコース",
        "monthly_fee": 4400,
        "initial_fee": 11000,
        "grade_range": ["lower_elementary", "upper_elementary", "junior_high"],
        "subjects": ["japanese", "math", "english", "science", "social"],
        "features": ["subject_variety", "exercise_quantity", "learning_management"],
        "strengths": [
            "難関校受験にも対応した高品質な教材",
            "思考力・記述力を重視したカリキュラム",
            "丁寧な添削指導と解説",
            "自ら考える力を育てる教育方針"
        ],
        "weaknesses": [
            "月額費用が高め",
            "初期費用がかかる",
            "基礎固めより発展学習向き",
            "ボリュームが多く負担に感じる場合も"
        ],
        "description": "Z会タブレットコースは、思考力・表現力を重視した難関校受験にも対応する高品質な学習教材です。"
    },
    {
        "id": "gainax_kids",
        "name": "ガンバレ！ぼくらのプログラミング",
        "monthly_fee": 1980,
        "initial_fee": 0,
        "grade_range": ["lower_elementary", "upper_elementary"],
        "subjects": ["programming"],
        "features": ["interactive", "online_support"],
        "strengths": [
            "プログラミング教育に特化",
            "実際にゲームを作りながら学べる",
            "オンラインサポートが充実",
            "月額費用が比較的安め"
        ],
        "weaknesses": [
            "プログラミングのみの対応",
            "総合的な学習には他の教材も必要",
            "タブレットを別途用意する必要がある"
        ],
        "description": "ガイナックスが提供するプログラミング学習教材で、ゲーム制作を通じてプログラミングの基礎から応用まで楽しく学べます。"
    },
    {
        "id": "kodomo_challenge",
        "name": "こどもちゃれんじ タブレット版",
        "monthly_fee": 2480,
        "initial_fee": 0,
        "grade_range": ["kindergarten"],
        "subjects": ["japanese", "math", "english", "comprehensive"],
        "features": ["interactive", "learning_management"],
        "strengths": [
            "幼児教育のパイオニアならではの質の高いコンテンツ",
            "遊びながら学べる工夫が満載",
            "しまじろうというキャラクターで親しみやすい",
            "知育玩具との連携"
        ],
        "weaknesses": [
            "小学生以上には物足りない内容",
            "学習要素よりも遊びの要素が強い場合も",
            "タブレットを別途用意する必要がある"
        ],
        "description": "こどもちゃれんじのタブレット版は、人気キャラクター「しまじろう」と一緒に、遊びながら幼児期に必要な能力を育てます。"
    },
    {
        "id": "digital_drill",
        "name": "デジタルドリル",
        "monthly_fee": 1280,
        "initial_fee": 0,
        "grade_range": ["lower_elementary", "upper_elementary", "junior_high"],
        "subjects": ["japanese", "math", "english", "science", "social"],
        "features": ["exercise_quantity"],
        "strengths": [
            "非常にリーズナブルな月額費用",
            "基礎的な問題を繰り返し練習できる",
            "シンプルで使いやすいインターフェース",
            "学校の教科書に準拠"
        ],
        "weaknesses": [
            "AI機能や個別最適化機能はない",
            "解説が少なめでサポートが薄い",
            "応用力を養う問題が少ない",
            "タブレットを別途用意する必要がある"
        ],
        "description": "デジタルドリルは基礎学力の定着を目的とした、シンプルで手頃な価格のタブレット学習教材です。"
    }
]

# 機能評価データ（各教材の機能ごとの評価点）
feature_ratings = {
    "smile_zemi": {
        "learning_management": 9,
        "online_support": 7,
        "subject_variety": 9,
        "exercise_quantity": 8,
        "interactive": 7,
        "ai_learning": 8
    },
    "challenge_touch": {
        "learning_management": 8,
        "online_support": 9,
        "subject_variety": 8,
        "exercise_quantity": 7,
        "interactive": 7,
        "ai_learning": 6
    },
    "risu_kids": {
        "learning_management": 7,
        "online_support": 6,
        "subject_variety": 3,
        "exercise_quantity": 9,
        "interactive": 8,
        "ai_learning": 10
    },
    "qubena": {
        "learning_management": 6,
        "online_support": 5,
        "subject_variety": 4,
        "exercise_quantity": 8,
        "interactive": 9,
        "ai_learning": 10
    },
    "z_kai_tablet": {
        "learning_management": 7,
        "online_support": 8,
        "subject_variety": 9,
        "exercise_quantity": 9,
        "interactive": 6,
        "ai_learning": 5
    },
    "gainax_kids": {
        "learning_management": 5,
        "online_support": 8,
        "subject_variety": 2,
        "exercise_quantity": 6,
        "interactive": 10,
        "ai_learning": 4
    },
    "kodomo_challenge": {
        "learning_management": 6,
        "online_support": 7,
        "subject_variety": 6,
        "exercise_quantity": 5,
        "interactive": 9,
        "ai_learning": 3
    },
    "digital_drill": {
        "learning_management": 4,
        "online_support": 3,
        "subject_variety": 7,
        "exercise_quantity": 10,
        "interactive": 4,
        "ai_learning": 2
    }
}
